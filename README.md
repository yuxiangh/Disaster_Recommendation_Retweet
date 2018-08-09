# Disaster_Recommendation_System_Retweet

# Background   

In disaster Prediction System, Retweet messages are the important messages we need to pay much attention because it may give you ideas where people need help, who are trapped in disasters. Information Science Institute Thor Project wants to build the disaster recommendation system to help government and rescue institution to save and help people more efficiently. 



# Stratigies     

For each specific topics, like food,water, evacuation. find the twitter messages has high retweet messages is super important because it reflects peoples' need. 




# Running programs on command line   
python3 /Users/yuxianghou/Desktop/retweet_recommender.py /Users/yuxianghou/Desktop/Recommendation_Conf.json




# Paramets in the Configure file
1.json line path:  The path of json line(one big json file includes all single json file)   
2.id_path: The id path of single json file    
3.text: The sentence path of single json file   
4.labels: the labels path of single json file   
5.topic: The topic we would like to know. (default is "rescue")  

# Example of parameters in configure file. 
One json file:
{"key1":{"id":XX, "text":XX}, "key2":{"labels"}}

Above example:   
id_path is "key1.id"   
text is "key1.text"  
labels is "key2.labels"



# Output:
The output is the json file which are sorted in desceding orders of retweet numbers




# Further Work:

In Disaster Recommendation System, Emotion and sentimental analysis are very important Because we need to detect some urgent and anxious twitter messages instead of some "happy ending" twitter messages like "XX are rescued! His family friends are so happy. "So we also need to give each twitter messages some emotion labels and scores.  



















