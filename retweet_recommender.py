
# coding: utf-8

# In[1]:


import string
import re
import numpy as np
import pandas as pd
from pprint import pprint
import os  
import json
import warnings
import sys
warnings.filterwarnings("ignore",category=DeprecationWarning)


# In[2]:
#four input of this programs
#1.json line path 
#2.Id path in the single json files/  how to get the id in json/ format:   like  "lorreli-id" 
#3.sentence path in the single json files/ how to get the sentence in json  like "lorreli-sentence"
#4.topic path in the single json files




#output:
#the json line that will contains the top 10 related-topic twitters sorted by desceding orders of retweet.






class disaster_Recommendation(object):
    def __init__(self,jsonPath,idPath,sentencePath,topicPath,topic):
        self.jsonPath=jsonPath
        self.idPath=idPath
        self.sentencePath=sentencePath
        self.topicPath=topicPath
        self.topic=topic
        self.data=None
        self.target_data=None
        self.top_10=None
        self.output=None
    
    def runRecommendationSystem(self):
        self.getDataFrame() #get the data
        self.data["Prepocessed"]=self.data["Sentence"].apply(lambda x:self.changeSentenceFormat(x)) #get prepocessed data
        self.getSpecificTopicData()
        self.getSortedDict()
        self.getOutputData()
        
            
    
    #split the input sentence/id path like "loreleiJSONMapping-translatedText" to get the real data 
    def getWordsFromAlist(self,adict,aword):
        alist=aword.split("-")
        for i in range(0,len(alist)):
            new_dict=adict[alist[i]]
            adict=new_dict
        return adict
    
    
    #get the dataframe from json files 
    def getDataFrame(self):
        all_list=[]
        with open(self.jsonPath,"r") as data_input:
            for line in data_input:
                one_list=[]
                data=json.loads(line)
                one_list.append(self.getWordsFromAlist(data,self.idPath)) 
                one_list.append(self.getWordsFromAlist(data,self.sentencePath))
                one_list.append(self.getWordsFromAlist(data,self.topicPath))
                all_list.append(one_list)
            columns=["Id","Sentence","Topic"]
            data=pd.DataFrame(data=all_list,columns=columns)
        self.data=data
    
    
    #change the sentence format, replace the words starts with the http to url. and replace @XX to @someone, considering twitter situation because it is a same
    #twitter but give to the different persons. 
    def changeSentenceFormat(self,sentence):
        words_list=sentence.split(" ")
        new_word_list=[]
        for word in words_list:
            if word.startswith("@"):
                word="@someone"
            if word.startswith("http"):
                word="url"
            new_word_list.append(word)
        new_sentence=" ".join(new_word_list)
        return new_sentence
    
    #helper function to get the data
    def getSpecificTopic(self,alist,topic):
        if topic in alist:
            return True
        else:
            return False
    
    #get specific top data frame 
    def getSpecificTopicData(self):
        data=self.data.copy(deep=True)
        data["is"+str(self.topic)]=data["Topic"].apply(lambda x:self.getSpecificTopic(x,self.topic))
        new_data=data[data["is"+str(self.topic)]==True]
        new_data=new_data.drop("is"+str(self.topic),axis=1)
        self.target_data=new_data
    

    #get the sorted top 10 descending retweet twitters 
    def getSortedDict(self):
        adict={}
        for sentence in list(self.target_data["Prepocessed"]):
            if sentence not in adict:
                adict[sentence]=1
            else:
                adict[sentence]+=1

        sorted_dict=sorted(adict.items(),key=lambda x:-x[1])
        top10_sorted_dict=sorted_dict[:10]
        self.top_10=top10_sorted_dict
    
    #get output data 
    def getOutputData(self):
        final_list=[]
        for i in range(0,len(self.top_10)):
            sentence=self.top_10[i][0]
            count=self.top_10[i][1]

            new_data=self.target_data[self.target_data["Prepocessed"]==sentence].head(1)
            new_list=list(np.array(new_data)[0])
            new_list.append(count)
            adict={"Id":new_list[0],"Sentence":new_list[1],"Labels":new_list[2],"Retweet Count":new_list[4]}
            final_list.append(adict)
        self.output=final_list
    
    #write output to the json files 
    def writeToJson(self):
        output_file =open('Recommendation_System_Based_On_retweet_'+str(self.topic)+'_topic.json','w')
        for oneJson in self.output:
            output_file.write(json.dumps(oneJson))
            output_file.write("\n")


# In[4]:


if __name__=="__main__":
    json_line_path=sys.argv[1]
    id_path=sys.argv[2]
    text_path=sys.argv[3]
    labels_path=sys.argv[4]
    topic=sys.argv[5]
    
    recommender=disaster_Recommendation(json_line_path,id_path,text_path,labels_path,topic)
    recommender.runRecommendationSystem()
    recommender.writeToJson()

