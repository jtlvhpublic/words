#/usr/bin/env python3
import time 

# modified for python 3 - raw_input changed to input, and print statements arguments now in parenthesis
#the text user puts in
text = input("Enter things here")
wpm = int(input("How fast would you like to read?"))

#seconds between each list item post 
wpm_seconds = wpm/60

#takes each word and puts each one in their own 
def split_line(text):
    words = text.split()
    for current_word in words:
        print(current_word)
    return words # returns the words list to the calling program
        
print(split_line(text)) #prints result

#prints items per second time.sleep(seconds between posts)
for word in split_line(text): # iterates over the words in the list one word at a time
	print(word)
	time.sleep(wpm_seconds)