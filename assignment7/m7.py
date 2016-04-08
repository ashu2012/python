
def  count_letters(fruit):
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

if __name__== "__main__":
    import doctest
    doctest.testmod()
