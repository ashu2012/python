
#------------Q2-----------------------------------------------------------------
def count_letters(fruit):
    """
    >>> count_letters('a')
    1
    >>> count_letters("banana")
    3
    """
    if len(fruit)==1 :
        if fruit == 'a':
            print 1
        else:
            print 0
    else:
        count = 0
        for char in fruit:
            if char == 'a':
                count += 1
        print count


#------------Q5-----------------------------------------------------------------
def reverse(s):
    """
      >>> reverse('happy')
      'yppah'
      >>> reverse('Python')
      'nohtyP'
      >>> reverse("")
      ''
      >>> reverse("P")
      'P'
    """
    i=len(s)-1
    outputStr=""
    while i>=0:
        outputStr=outputStr+s[i]
        i=i-1
    return outputStr

#------------Q6-----------------------------------------------------------------
def mirror(s):
    """
      >>> mirror("good")
      'gooddoog'
      >>> mirror("yes")
      'yessey'
      >>> mirror('Python')
      'PythonnohtyP'
      >>> mirror("")
      ''
      >>> mirror("a")
      'aa'
      """
    revStr=reverse(s)
    return s+revStr


#------------Q7-----------------------------------------------------------------

def remove_letter(letter, strng):
    """
      >>> remove_letter('a', 'apple')
      'pple'
      >>> remove_letter('a', 'banana')
      'bnn'
      >>> remove_letter('z', 'banana')
      'banana'
      >>> remove_letter('i', 'Mississippi')
      'Msssspp'
    """
    outputStr=""
    for i in strng:
        if i==letter:
            continue
        else:
            outputStr=outputStr+i

    return outputStr

#------------Q8-----------------------------------------------------------------
def is_palindrome(s):
    """
      >>> is_palindrome('abba')
      True
      >>> is_palindrome('abab')
      False
      >>> is_palindrome('tenet')
      True
      >>> is_palindrome('banana')
      False
      >>> is_palindrome('straw warts')
      True
    """
    loopConterEnd=0
    if len(s)%2==0:
        loopCounterEnd=len(s)/2
    else:
        loopCounterEnd=len(s)/2
    i=0
    while i<= loopConterEnd:
        if (s[i]!=s[len(s)-i-1]):
            return  False
        i=i+1
    return  True


def count(sub, s):
    """
      >>> count('is', 'Mississippi')
      2
      >>> count('an', 'banana')
      2
      >>> count('ana', 'banana')
      2
      >>> count('nana', 'banana')
      1
      >>> count('nanan', 'banana')
      0
    """
    count=0
    stringToMatch = sub
    lenOfSub=len(sub)
    for i in range(0, len(s)-lenOfSub+1):
        ifExist= True
        #start searching for string match at given point in string
        for j in  range(0, len(stringToMatch)):
            #print "j=" + str(j)
            if(s[i+j]!= stringToMatch[j]):
                ifExist = False
                break

        #increment the count as we have found a match
        if(ifExist):
            count= count+1


    return  count

def remove(sub, s):
    """
      >>> remove('an', 'banana')
      'bana'
      >>> remove('cyc', 'bicycle')
      'bile'
      >>> remove('iss', 'Mississippi')
      'Missippi'
      >>> remove('egg', 'bicycle')
      'bicycle'
    """
    count=0
    stringToMatch = sub
    lenOfSub=len(sub)
    outPutStr=s[:]
    for i in range(0, len(s)-lenOfSub+1):
        ifExist= True
        #start searching for string match at given point in string
        for j in  range(0, len(stringToMatch)):
            #print "j=" + str(j)
            if(s[i+j]!= stringToMatch[j]):
                ifExist = False
                break

        #increment the count as we have found a match
        if(ifExist):
            outPutStr=s[:i]+s[i+lenOfSub:]
            break



    return  outPutStr


def remove_all(sub, s):
    """
      >>> remove_all('an', 'banana')
      'ba'
      >>> remove_all('cyc', 'bicycle')
      'bile'
      >>> remove_all('iss', 'Mississippi')
      'Mippi'
      >>> remove_all('eggs', 'bicycle')
      'bicycle'
    """
    count=0
    stringToMatch = sub
    lenOfSub=len(sub)
    outPutStr=""
    previousMatchIndex=0
    currentMatchIndex=0
    for i in range(0, len(s)-lenOfSub+1):
        ifExist= True
        #start searching for string match at given point in string
        for j in  range(0, len(stringToMatch)):
            #print "j=" + str(j)
            if(s[i+j]!= stringToMatch[j]):
                ifExist = False
                break

        #increment the count as we have found a match
        if(ifExist):
            currentMatchIndex=i
            outPutStr=outPutStr +s[previousMatchIndex:currentMatchIndex]
            previousMatchIndex=currentMatchIndex+lenOfSub







    outPutStr=outPutStr +s[previousMatchIndex:]
    return  outPutStr

if __name__== "__main__":
    import doctest
    doctest.testmod()
