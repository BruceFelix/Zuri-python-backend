# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    with open(filename) as file:
        contents = file.read()
        return contents

def count_words():
    text = read_file_content("Reading-Text-Files/story.txt")
    text = text.split() #splits the string into a list
    frequency = [text.count(i) for i in text] #counts the number of occurrence of each word
    myDict = dict(zip(text, frequency)) #combines the frequency list with the text to form a dictionary
    return myDict

print(count_words())