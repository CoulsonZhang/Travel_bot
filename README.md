#My_Travel_Bot   

Hi, this is my first natural language understanding and SQL database manipulation involved chat_bot  
For better data structure and managment, I split the definition of function in different py files for management.  
Followings are my distribution of py files.  

The_bot: the main conversation loop between bot and user. Most function here are defined in following py files.  
Natural: the natural languaage method file, including Rasa NlU intent identification function  
Responses: Round response function defined here, function used in part1 & part2.   
api_method: the functions related api are defined in this file      
sql_method: the method related manipulation of Winetable.db   
Telegram_warpper: the implement of chat_bot through telegram  
nlu.md: the rasa intent identifier training data   
test & test2 py file are playround for function development and usage trial  

! Telegram token located in another py file which is not pushed in Git for safety reason.  !

This graph shows my conversation pattern:  
![Image discription](https://github.com/CoulsonZhang/Travel_bot/blob/master/Inprocess/flow_map.jpg)

#Demo vide:
https://youtu.be/R0HvtCG8Ii0

#contact info:
telegram: @coulsonZ
