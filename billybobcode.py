def billyBobSimulator(userMessage):
    wordlist=[]
    charList=[]
    mainList=[]

    userMessage = userMessage.lower()
    userMessage = userMessage.replace(","," ")
    userMessage = userMessage.replace("!"," ")
    userMessage = userMessage.replace(";"," ")
    userMessage = userMessage.replace("-"," ")
    userMessage = userMessage.replace("."," ")
    userMessage = userMessage.replace("?"," ")
    userMessage = userMessage.replace("("," ")
    userMessage = userMessage.replace(")"," ")

    wordList = userMessage.split()

    for word in wordList:
        charList = list(word)
        s = sorted(charList)
        mainList.append(s)
        
    newString=""
    for word in mainList:
        for i in word:
            newString = newString + i
        newString = newString + " "

    return(newString)

print(billyBobSimulator("This is certainly a dastardly plan"))

secretMessage = billyBobSimulator("Send the code fourty-two to all the secret agents!")
print(secretMessage)