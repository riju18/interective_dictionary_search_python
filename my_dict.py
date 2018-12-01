import json
import os
from difflib import SequenceMatcher as sm   # to get the ratio of matched words
from difflib import get_close_matches       # get closely releted words

folder = os.path.dirname(os.path.abspath(__file__))
datafile = os.path.join(folder,'data.json')

data = json.load(open(datafile))

def descrip(key):
    if not key in data:       # if search key isn't found in file
        mesg = get_close_matches(key, data.keys(), n=5)  # get most close 5 words
        if len(mesg) > 0:
            yesOrNo = input('did u mean "%s" instead, press y/n or Y/N:' % get_close_matches(
                key, data.keys())[0])

            if yesOrNo == 'y' or yesOrNo == 'Y':
                result = ''
                value = data[get_close_matches(key, data.keys())[0]]
                for i in value:
                    result += i
                result += '\n\n suggested words: '
                for i in mesg:
                    result += i+', '
                result += result[:-2]
                result += '\n\n' + '"' + key + '"' + ' matched with suggested words: '
                for i in mesg:
                    matchPercen = str(sm(None, key, i).ratio())
                    result += matchPercen + ' , '
                return result[:-2]    
                       
            elif yesOrNo == 'n' or yesOrNo == 'N':
                return 'word isn\'t found'
            else:
                return 'y/n or Y/N input error'    

    else:                       # if search key is found in file
        valus = data[key]
        result = ''
        for i in valus:
            result += i
        return result
    
userInput = input()
print(descrip(userInput.lower()))

