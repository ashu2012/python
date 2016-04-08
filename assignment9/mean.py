from sys import argv

def sumNum(lst):
    currSum=0.0
    for i in lst:
        currSum=currSum+float(i)
    return currSum

def meanOfCommandline():
    lst = argv[1:]
    lenlst=len(lst)
    sumlst= sumNum(lst)
    return sumlst/lenlst

if __name__=="__main__":
    print meanOfCommandline()