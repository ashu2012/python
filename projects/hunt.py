'''
Project 1: Predicting Huntington's Disease
Ashutosh pathak
Course cs608
Email:apathak2@dons.usfca.edu
https://usfca.instructure.com/courses/1559830/assignments/6565686?module_item_id=16290536

How to run the project by going in to the terminal and type
[Terminal] python hunt.py -v

After that as per project requirement it will ask following user input:

[Shell]Enter your name: atp
[Shell]Enter you last name : atp
[Shell]Enter your DNA: cagacahCAG

output:
First Name : atp
Last Name : atp
Patient DNA : cagaCAGCA
The number of CAG repeats : 1
the classification and disease status: ('Normal', 'Unaffected')

There are few doc test are already written for your convenience.
Thanks for your time

'''

def countCAG(dna):
    """
    This function calculates the number of matches of CAG in given input
    dna. It does this by moving the window of match character ie "CAG" and comparing at every character in the
    given input dna. We have not used any built in string functions other than mentioned in project guidlines such as
    len().
    INPUT: String input of dna sequence
    OOUTPUT: Number of count of CAG in that dna
    Examples:
    >>> countCAG("CAG")
    1
    >>> countCAG("")
    0
    >>> countCAG("cagcagacag")
    0
    >>> countCAG("C")
    0
    >>> countCAG("CA")
    0
    >>> countCAG("CAGCA")
    1
    >>> countCAG("CAGCATCAGCAGCAG")
    1
    >>> countCAG("CAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCA")
    41
    """
    cagCount = 0
    stringToMatch = "CAG"
    previousCAGFound = False
    chainStart = False
    i=0
    while (i <= len(dna) - len(stringToMatch)):

        # Assume cag is found at current index
        currentCAGFound = True
        # start searching for string match at given point in string
        for j in range(0, len(stringToMatch)):
            if (dna[i + j] != stringToMatch[j]):
                # CAG not found our assumption is wrong, set varibale and break from loop
                #print dna[i+j]
                currentCAGFound = False
                break

        # we still didn't found first match. CAG chain has not started
        if (chainStart == False and currentCAGFound == False and previousCAGFound == False):
            # till we didn't find the chan start we take single step
            i = i + 1
            #print "1st elif i=" + str(i)
        # increment the count as we have found first match
        elif (chainStart == False and currentCAGFound == True and previousCAGFound == False):
            cagCount = cagCount + 1
            chainStart = True
            previousCAGFound = currentCAGFound
            i = i + len(stringToMatch)
            #print "2nd if after update i=" + str(i)
        elif (chainStart == True and currentCAGFound == True and previousCAGFound == True):
            # next CAG is found in chain of CAG
            previousCAGFound = currentCAGFound
            cagCount = cagCount + 1
            i = i + len(stringToMatch)
            #print "3rd elif i=" + str(i)
        elif (chainStart == True and currentCAGFound == False and previousCAGFound == True):
            # exit from current task , chain of CAG stopped
            #print "4th elif i=" + str(i)
            break
        else:
            # this will not reach as per logic
            #print "unreached"
            i = i + 1

    #print  cagCount
    return cagCount


def prediction(numCAG):
    """
    This function predicts the activity of disease depends on input parameter of numCAG
    which is calculated in previous function.
    INPUT : interger , denoting number of CAG in DNA
    OUTPUT : String based message saying how prone is dna for Hunting disease
    Examples:
    >>> prediction(27)
    ('Normal', 'Unaffected')
    >>> prediction(35)
    ('Intermediate', 'Unaffected')
    >>> prediction(42)
    ('Reduced Penetrance', 'Somewhat Affected')
    >>> prediction(45)
    ('Full Penetrance', 'Affected')
    """
    if(numCAG <28):
        return ('Normal','Unaffected' )
    elif (28 <=numCAG and numCAG <=36):
        return ('Intermediate', 'Unaffected')
    elif (37<=numCAG and numCAG <= 42):
        return ('Reduced Penetrance', 'Somewhat Affected')
    else:
        return ('Full Penetrance', 'Affected')




def get_input():
    #Your get_input function should return a tuple containing whatever the user input for first
    #name, last name and DNA, such as:
    #('Patricia', 'Francis-Lyon', 'CAGCAG')
    name=raw_input("Enter your name: ")
    last_name=raw_input( "Enter you last name : ")
    DNA= raw_input("Enter your DNA: ")
    return (name, last_name, DNA)

if __name__== "__main__":
    import doctest
    doctest.testmod()
    userInput=get_input()
    print "First Name : " +userInput[0]
    print "Last Name : " +userInput[1]
    print "Patient DNA : " +userInput[2]
    print "The number of CAG repeats : " + str(countCAG(userInput[2]))
    print "the classification and disease status: "+ str(prediction(countCAG(userInput[2])))




