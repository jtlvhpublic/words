import time 

#the text user puts in
text = raw_input("Enter things here")
wpm = int(raw_input("How fast would you like to read?"))

#seconds between each list item post 
wpm_seconds = wpm/60

#takes each word and puts each one in their own 
def split_line(text):
    words = text.split()
    for current_word in words:
        print(current_word)
        
print split_line(text) #prints result

#prints items per second time.sleep(seconds between posts)
for text in split_line:
	print text
	time.sleep(wpm_seconds)