def cleanword(word):
    """
      >>> cleanword('what?')
      'what'
      >>> cleanword('"now!"')
      'now'
      >>> cleanword('?+="word!,@$()"')
      'word'
    """
    outputStr=""
    for i in word:
        if (ord(i)>=ord('a') and ord(i)<= ord('z'))or (ord(i)>= ord('A') and ord(i)<= ord('Z')):
            outputStr=outputStr+i
    return outputStr

def has_dashdash(s):
    """
      >>> has_dashdash('distance--but')
      True
      >>> has_dashdash('several')
      False
      >>> has_dashdash('critters')
      False
      >>> has_dashdash('spoke--fancy')
      True
      >>> has_dashdash('yo-yo')
      False
    """
    lst= s.split('--')
    if len(lst)==2:
        return  True
    else:
        return False

def extract_words(s):
    """
      >>> extract_words('Now is the time!  "Now", is the time? Yes, now.')
      ['now', 'is', 'the', 'time', 'now', 'is', 'the', 'time', 'yes', 'now']
      >>> extract_words('she tried to curtsey as she spoke--fancy')
      ['she', 'tried', 'to', 'curtsey', 'as', 'she', 'spoke', 'fancy']
    """
    lst= re.split("[!@#$%^&*()_+-=<>?/,.;:'\"\\\ \s]+",s)

    outputLst=[]
    for i in lst :
        if cleanword(i).lower() != '':
            outputLst = outputLst + [ cleanword(i).lower()]
    return outputLst

def wordcount(word, wordlist):
    """
      >>> wordcount('now', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
      ['now', 2]
      >>> wordcount('is', ['now', 'is', 'time', 'is', 'now', 'is', 'the', 'is'])
      ['is', 4]
      >>> wordcount('time', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
      ['time', 1]
      >>> wordcount('frog', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
      ['frog', 0]
    """
    count=0
    for i in wordlist:
        if i== word:
            count=count+1
    return [word,count]

def wordset(wordlist):
    """
      >>> wordset(['now', 'is', 'time', 'is', 'now', 'is', 'is'])
      ['is', 'now', 'time']
      >>> wordset(['I', 'a', 'a', 'is', 'a', 'is', 'I', 'am'])
      ['I', 'a', 'am', 'is']
      >>> wordset(['or', 'a', 'am', 'is', 'are', 'be', 'but', 'am'])
      ['a', 'am', 'are', 'be', 'but', 'is', 'or']
    """
    returnSet=[]
    for i in wordlist :
        ifExist= False
        for j in returnSet:
            if j ==i:
                ifExist=True
                break
            else:
                continue
        if not(ifExist):
            returnSet.append(i)
    returnSet.sort()
    return returnSet
                
def longestword(wordset):
    """
      >>> longestword(['a', 'apple', 'pear', 'grape'])
      5
      >>> longestword(['a', 'am', 'I', 'be'])
      2
      >>> longestword(['this', 'that', 'supercalifragilisticexpialidocious'])
      34
    """
    longestWord=wordset[0]
    longestWordLength=len(wordset[0])
    for i in wordset:
        if len(i)>longestWordLength:
            longestWordLength=len(i)
            longestWord=i
    return longestWordLength

if __name__ == '__main__':
    import doctest
    import  re
    doctest.testmod()