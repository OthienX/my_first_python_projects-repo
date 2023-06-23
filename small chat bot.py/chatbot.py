import re
import long_responses as long

def message_probability(user_message, recognised_word, single_response = False, required_response[]):
 message_certainity = 0
 has_required_words = True
 #counting how many words are present in each predicted messsage
 for word in user_message:
     if word in recognised_words:
         message_certainity += 1
 # calculating the precentage of recognised words in a user message
 percentage = float(message_certainity)/ float (len(recognised_words))
 for words in required_words:
     if word not in user_message:
         has_required_words =1
 def get_response(user_input):
     split_message = re.split(r'\s+|[,;!,-]\s*', user_input.lower())
     response = check_all_message(split_message)
 # testing the response system
 while True:
     print('Bot '+ get_response(input('you :')))

