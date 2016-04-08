from sys import argv

"""
run program using
python ques16.py alice_in_wonderland.txt  alice_counts.dat
"""
def display(i):
    if i == 10: return 'LF'
    if i == 13: return 'CR'
    if i == 32: return 'SPACE'
    return chr(i)

if __name__=="__main__":

    infile = open(argv[1], 'r')
    text = infile.read()
    print type(text)
    infile.close()

    counts = 128 * [0]

    for letter in text:
        counts[ord(letter)] += 1

    outfile = open(argv[2], 'w')
    outfile.write("%-12s%s\n" % ("Character", "Count"))
    outfile.write("=================\n")

    for i in range(len(counts)):
        if counts[i]:
            outfile.write("%-12s%d\n" % (display(i), counts[i]))

    outfile.close()