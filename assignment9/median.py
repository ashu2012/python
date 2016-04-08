from sys import argv
import ast

def medianOfCommandline():
    lst = argv[1:]
    lenlst=len(lst)
    if lenlst%2==0:
        return (float(lst[lenlst/2-1]) +float(lst[lenlst/2]))/2.0
    else:
        return ast.literal_eval(lst[lenlst/2])


if __name__=="__main__":
    print medianOfCommandline()