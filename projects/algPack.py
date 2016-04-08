"""
HS 608 Project 2: String and List Algorithms
Ashutosh pathak
Course cs608
Email:apathak2@dons.usfca.edu
https://usfca.instructure.com/courses/1559830/assignments/6565687

How to run the project by going in to the terminal and type
[Terminal] python algPack.py -v
"""

def repeatList(lst, n):
    """
    Returns a new list that is equivalent to lst * n, where * is the repetition operator.
    Assumes n is a positive integer.

    INPUT: first argument contains list and second argument is integer value
    OOUTPUT: List having n times element as currently exist in the list.
    Examples:
    >>> repeatList([1,2,3], 0)
    []
    >>> repeatList([1,2,3], 3)
    [1, 2, 3, 1, 2, 3, 1, 2, 3]
    >>> repeatList(['a',2,3], 3)
    ['a', 2, 3, 'a', 2, 3, 'a', 2, 3]
    >>> repeatList([], 3)
    []
    >>> repeatList(["ddd","sss","aaa"], 2)
    ['ddd', 'sss', 'aaa', 'ddd', 'sss', 'aaa']
    """
    outputList=[]
    for i in range(0, n):
        outputList= outputList+lst

    return outputList


def replace(lst, pos, item):
    """
    Modifies list lst so that its element at pos is replaced with item.
    Does not modify lst if pos is negative or pos >= length of lst.
    Assumes n is an integer.
    Nothing is returned.
    Input 1st argumnt is list , 2nd argument is integer value, 3rd argument:any integer, char, string , boolean,list
    ouput: none , original list is modified
    Examples:
    >>> mylist = [1,2,3]
    >>> replace(mylist, 2, 'z')
    >>> mylist
    [1, 2, 'z']
    >>> mylist = [6,1,4,2,3]
    >>> replace(mylist, 5, 'z')
    >>> mylist
    [6, 1, 4, 2, 3]
    >>> mylist = [6,1,4,2,3]
    >>> replace(mylist, -1, 'z')
    >>> mylist
    [6, 1, 4, 2, 3]
    >>> mylist = []
    >>> replace(mylist, 0, 'z')
    >>> mylist
    []
    >>> mylist = [1,2,3]
    >>> replace(mylist, 2, 5)
    >>> mylist
    [1, 2, 5]
    >>> mylist = [1,2,3]
    >>> replace(mylist, 2, ['a','b','c'])
    >>> mylist
    [1, 2, ['a', 'b', 'c']]
    >>> mylist = [1,2,3]
    >>> replace(mylist, 2, '')
    >>> mylist
    [1, 2, '']
    >>> mylist = [1,2,3]
    >>> replace(mylist, 2, 5)
    >>> mylist
    [1, 2, 5]
    """

    for i in range(0,len(lst)):
        if (i == pos):
            lst[i]= item


def countElem(lst, elem):
    """
    Returns the number of occurrences of element elem in list lst
    Input 1st argumnt is list , 2nd argument :any  char, string element
    ouput: count of occurance of element is list
    Examples:
    >>> countElem(['w', 'owl', 'w', 'awesome'], 'w')
    2
    >>> countElem(['w', 'owl', ' ', 'awesome'], ' ')
    1
    >>> countElem(['w', 'owl', 'w', 'awesome'], '')
    0
    >>> countElem([], 'w')
    0
    >>> countElem(['w', 'owl', [1,2], [1,2]], [1,2])
    2
    >>> countElem(['w', 'owl', [1,2], [1,[2],2]], [1,[2],2])
    1
    >>> countElem(['w', 'owl', 'w', 'awesome'], False)
    0
    >>> countElem(['w', 'owl', False, 'awesome'], False)
    1
    """
    count =0
    for i in lst:
        if i == elem:
            count=count+1
    return count



def findLast(lst, elem):
    """
    Returns the index of the last occurrence of element elem in list lst or -1 if elem does not
    occur in lst.
    Input 1st argument is list , 2nd argument :any  char, string element
    Ouput: count of occurance of element is list
    Examples:
    >>> findLast(['w', 'owl', 'w', 'awesome'], 'w')
    2
    >>> findLast(['w', 'owl', 'w', 'awesome'], 'a')
    -1
    >>> findLast([], 'w')
    -1
    >>> findLast(['w', 'owl', 'w', 'awesome'], '')
    -1
    >>> findLast(['w', 'owl', 'w', 'awesome'], 'owl')
    1
    >>> findLast([], '')
    -1
    >>> findLast([1,2,3,4,['w']], ['w'])
    4
    """
    index = -1
    currIndex=0
    for i in lst:
        if i== elem:
            index=currIndex

        currIndex=currIndex+1
    return index


def string2list(s):
    """
    Returns a list whose elements are each of the characters in string s as ordered in s
    Input : any string
    Ouput: list of char
    Examples:
    >>> string2list ('cat')
    ['c', 'a', 't']
    >>> string2list ('')
    []
    >>> string2list ('c')
    ['c']
    """
    outputList=[]
    for i in  s:
        outputList= outputList+[i]

    return outputList


def lastOccurMostFreqElem(lst):
    """
    Returns the index of the last occurrence of the element that most frequently occurs in list lst
    or -1 if lst is empty. If elements occur with equal frequency, returns index of the last of these.
    Examples:
    Input:generic list
    Output: Integer
    >>> lastOccurMostFreqElem([0,0,2,2,0,2])
    5
    >>> lastOccurMostFreqElem([3,2,2,3])
    3
    >>> lastOccurMostFreqElem([])
    -1
    >>> lastOccurMostFreqElem([0,1,2,3,4,5])
    5
    >>> lastOccurMostFreqElem([3,[2],[2],[3],False])
    2
    """
    if len(lst)==0:
        return  -1

    globalMostFrquent = lst[0]
    globalMostfrequentindex=0
    globalMostFrequestCount=1

    for i in range(0,len(lst)):
        currentMostFrquent = lst[i]
        currentMostfrequentindex=i
        currentMostFrequestCount=0
        for j in range (0, len(lst)):
            if(lst[j]== currentMostFrquent):
                currentMostfrequentindex=j
                currentMostFrequestCount= currentMostFrequestCount+1
            else:
                continue
        if(globalMostFrequestCount<=currentMostFrequestCount):
            globalMostFrequestCount=currentMostFrequestCount
            globalMostfrequentindex=currentMostfrequentindex
            globalMostFrquent=currentMostFrquent
        else:
            #do nothing
            continue

    return  globalMostfrequentindex



def FindVal(lst, val):
    # no init needed or can init resultIndex to -1
    """
    Input:generic list, val is any object  of primitive type or compund data type
    Output: Integer
    >>> lst =[1,2,3, False]
    >>> val=3
    >>> FindVal(lst,val)
    2
    >>> lst =[1,2,[3], False]
    >>> val=[3]
    >>> FindVal(lst,val)
    2
    >>> lst =[1,2,[3,[4]], False]
    >>> val=[3,[4]]
    >>> FindVal(lst,val)
    2
    >>> lst =[1,2,[3,[4,[5]]], False]
    >>> val=[3,[4,[5]]]
    >>> FindVal(lst,val)
    2
    >>> lst =[1,2,[3,[4,[5, "deepchking"]]], False]
    >>> val=[3,[4,[5,"deepchking"]]]
    >>> FindVal(lst,val)
    2
    >>> lst =[1,2,[3,[4,[5, 6.7]]], False]
    >>> val=[3,[4,[5, 6.7]]]
    >>> FindVal(lst,val)
    2
    """

    for i in range(len(lst)): # returns an index, so we use index traversal
        if lst[i] == val:
            return i
    return -1



def insert(s1, s2, pos):
    """
    Returns a new string that is equivalent to string s1 with string s2 inserted at index pos.
    Returns empty string if pos is negative or pos > length of s1.
    Assumes n is an integer.
    Input:s1 and s2 are string , pos is Integer
    Output: String
    Examples:
    >>> insert('', 'world!', 0)
    'world!'
    >>> insert('world', 's', 2)
    'wosrld'
    >>> insert('world', 's', 5)
    'worlds'
    >>> insert('world', '', 5)
    'world'
    >>> insert('', '', 5)
    -1
    >>> insert('', 'a', -2)
    -1
    """
    outputStr=""
    index=0
    if (pos >  len(s1) or pos <0):
        return  -1
    elif(pos== len(s1)):
        outputStr=s1+s2
        return  outputStr
    else:
        for i in s1:

            if (pos == index):
                outputStr= outputStr+ s2+i
            else:
                outputStr= outputStr+i

            index=index+1
        return  outputStr

def substring(s, pos1, pos2):
    """
    Returns a new string consisting of the characters of string s from pos1 to pos2-1 inclusive.
    Returns the empty string if there is no valid substring beginning at pos1 and ending at pos2-1.
    Assumes both pos1 and pos2 are integers.
    Input:s is  string , pos1, pos2 are Integer
    Output: String
    Examples:
    >>> substring('cat', 1, 3)
    'at'
    >>> substring('cat', 1, 5)
    ''
    >>> substring('', 0, 0)
    ''
    >>> substring('a', 0, 0)
    'a'
    >>> substring('ab', 1, 0)
    ''
    """
    outputStr=""
    if pos1 <=pos2 and pos1>=0 and pos2 <=len(s) :
        for i in range(0, len(s)):
            if (i >= pos1 and i <= pos2 ):
                outputStr = outputStr + s[i]
            else:
                continue
        return outputStr

    else:
        return outputStr


def str2int(s):
    """
    Returns an integer that is the integer equivalent of the string s.
    Assumes that s is the string version of a valid integer.
    Input:s is String
    Output: Integer
    Examples:
    >>> str2int('-1000092')
    -1000092
    >>> str2int('1000092')
    1000092
    >>> str2int('+1000092')
    1000092
    >>> str2int('0')
    0
    >>> str2int('-0')
    0
    """
    positiveInteger= True
    outputInteger=0
    for i in  s:

        if ord(i) >= ord('0') and ord(i)  <= ord('9'):
            outputInteger= outputInteger*10 +ord(i)-ord('0')
        elif (i=='-'):
                    positiveInteger= False


    if not(positiveInteger):
        outputInteger=outputInteger*(-1)
    else:
        #already a postive integer
        #do Nothing
        pass

    return outputInteger

def int2str(i):
    """
    Returns a string that is the string equivalent of valid integer i
    Input:i is Integer
    Output: String
    Examples:
    >>> int2str(-1000092)
    '-1000092'
    >>> int2str(1000092)
    '1000092'
    >>> int2str(0)
    '0'
    """
    outputStr=""
    isPositive=True
    if i<0:
        isPositive=False
        i=i *(-1)
    elif(i==0):
        outputStr='0'

    while i!=0:
        rem =i%10
        if (rem == 0):
            outputStr='0'+outputStr
        elif(rem==1):
            outputStr='1'+outputStr
        elif(rem==2):
            outputStr ='2'+outputStr
        elif(rem==3):
            outputStr ='3'+outputStr
        elif(rem==4):
            outputStr='4'+outputStr
        elif(rem==5):
            outputStr='5'+outputStr
        elif(rem==6):
            outputStr='6'+outputStr
        elif(rem==7):
            outputStr='7'+outputStr
        elif(rem ==8):
            outputStr='8'+outputStr
        elif(rem==9):
            outputStr='9'+outputStr
        i =i /10

    if not(isPositive):
        outputStr='-'+outputStr

    return outputStr



if __name__ == "__main__":
    import doctest
    doctest.testmod()

