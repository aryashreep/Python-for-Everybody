# 8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt

# ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
# Iterates through each line in filehandle
for line in fh:
    #Iterates through each word on line
    for word in line.split():
        #Checks to see if word is already in list
        if not word in lst:
            #Appends words to list
            lst.append(word)
lst.sort()
print(lst)