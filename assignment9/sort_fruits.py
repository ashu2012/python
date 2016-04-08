def filter(oldfile, newfile):
    infile = open(oldfile, 'r')
    lst=[]
    while True:
        text = infile.readline()
        if text == "":
           break
        else:
          lst.append(text)
    lst.sort()
    outfile = open(newfile, 'w')
    for i in lst:
        outfile.write(i)

    infile.close()
    outfile.close()


if __name__=="__main__":
    filter("unsorted_fruits.txt","sorted_fruits.txt")