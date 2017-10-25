import json

#loads a dictionary of English words
#returns a dictionary
def load_dictionary():
        filename = "dictionary.json"
        with open(filename,"r") as dictionary:
            validWords = json.load(dictionary)

        return validWords

#Sort strings by character ASCII values while retaining value order
#returns a list of integers
def order_word(word):
    letterValues = []
    for letter in word:
        letterValues.append(ord(letter))

    letterValuesSorted = sorted(letterValues)

    placeData = {}
    for i in range(len(letterValues)):
        placeData[letterValuesSorted[i]] = i+1

    letterRanks = []
    for i in range(len(letterValues)):
        for k,v in placeData.items():
            if k == letterValues[i]:
                letterRanks.append(v)

    for i in range(1,len(letterRanks)):
        if letterRanks[i] == letterRanks[i-1]:
            letterRanks[i-1] = letterRanks[i] - 1

    return letterRanks

#Get a "word" from the user in the form of integer value order.
#returns a list of integers
def get_user_word():
    word = []
    userNumber = 0
    print("Enter your keyword values. -1 to stop: ")
    while(userNumber != -1):
        userNumber = int(input("Value: "))
        if(userNumber != -1):
            word.append(userNumber)

    return word


if __name__ == '__main__':
    englishWords = load_dictionary()
    userWord = get_user_word()
    matchWords = []
    for key in englishWords:
        if(len(key) == len(userWord)):
            if(order_word(key)) == userWord:
                matchWords.append(key)

    print(matchWords)


