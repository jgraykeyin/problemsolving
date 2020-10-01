words = ['the', 'quick', 'brown', 'fox', 'jumped','over','lazy', 'dog', 'indeed', 'this', 'is', 'droid', 'you', 'are', 'looking', 'for', 'it', 'remarkable', 'did', 'not', 'notice']
 
def spell_check(words,s):
    spellList = []
    s = s.replace(","," ")
    s = s.replace("!"," ")
    s = s.replace(";"," ")
    s = s.replace("-"," ")
    s = s.replace("."," ")
    s = s.replace("?"," ")
    s = s.replace("("," ")
    s = s.replace(")"," ")

    wordList = s.split()

    for i in wordList:
        if i.lower() in words:
            #print("Match")
            pass
        else:
            #print("Not Matching: {}".format(i))
            spellList.append(i)
    return(spellList)


# spell_check(words, "The quick brown fox jumped over the lazy dog!") 
#returns an empty list due to no mistakes.
 
#spell_check(words, "Indeed, this is the drood you are looking for; it is remarkable you did not notice!") 
#returns ['drood'] since this is not in the list.

print(spell_check(words, "The quick broon droid jumped ovr the lazy fox"))
#returns ['broon', 'ovr']

#spell_check(words, "The QuicK! brooN. dRoId, JumPeD; Ovr? the (laZy-foX)") 
#returns ['brooN', 'Ovr']