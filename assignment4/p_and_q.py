def truth_table(expression):
    print " p      q      %s"  % expression
    length = len( " p      q      %s"  % expression)
    print length*"="

    for p in True, False:
        for q in True, False:
            print "%-7s %-7s %-7s" % (p, q, eval(expression))

truth_table("not(p or q)")
truth_table("p and q")
truth_table("not(p and q)")
truth_table("not(p) or not(q)")
truth_table("not(p) and not(q)")
