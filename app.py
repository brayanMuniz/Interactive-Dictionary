import json
import difflib
# Todo Delete the data and get it from an api
data = json.load(open('data.json'))
# Please dont print the data or open the file
word = input("What word would you like to look for?").lower()
if word in data:
    print(data[word][0])
else:
    closeWords = difflib.get_close_matches(word, data)
    closestWord = closeWords[0]
    print(f'Did you mean {closestWord}')
    answer = input("Type Y or N.\n")
    if answer == "Y":
        print(data[closestWord][0])
    else:
        print("Ok byeeeeeeeee")
