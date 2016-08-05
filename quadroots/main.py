#!/usr/bin/env python

import cmath
import math
""" file:main.py
    -main program file for project 1
    -input file 'quadabc.txt'
    -strip white space from beginning and end of strings 
    -ignore blank lines and the comments
    -convert each string of three characters to a list of character
    -convert a list of three strings to floats a,b,c,print a,b,c out
    -calculate descriminant d = b^2 - 4ac
    -solve polynomial function
    -write output to 'quadroots.txt'
"""

def get_abc(line):
    """ line is a string
        extract to float a,b,c 
        return a,b,c
    """
    list1 = line.split()  # split on whitespace
    a = float(list1[0])
    b = float(list1[1])
    c = float(list1[2])
    return a,b,c

def descriminant(a,b,c):
    """ calculate descriminant """
    d = b ** 2 - 4 * a * c
    return d

def root_case1(a,b,c):
    """ a,b,c = 0, all complex numbers are roots """
    root = {'roots':'All complex numbers are roots'}
    return ("%(roots)s" % root)

def root_case2(a,b,c):
    """ a,b = 0,c != 0, no real/complex roots """
    root = {'roots':'No real or complex roots'}
    return ("%(roots)s" % root)

def root_case3(a,b,c):
    """ a,c = 0, b is a real number """
    x2 = 0 / b
    root = {'roots':x2}
    return ("%(roots)s" % (root))

def root_case4(a,b,c):
    """ a= 0 ,b,c != 0, to find one root """
    x1 = - c / b
    root = {'roots':x1}
    return ("%(roots)s" % (root))

def root_case5(a,b):
    """ b^2-4ac = 0, perfect roots """
    x3 = - b / (2 * a)
    root = {'roots':x3}
    return ("%(roots)s" % (root))

def root_case6(a,b,d):
    """ b^2-4ac > 0,two real roots """
    xplus = (- b + math.sqrt(d)) / (2 * a)
    xminus = (- b - math.sqrt(d)) / (2 * a)
    root = {'root1':xplus,'root2':xminus}
    return ("%(root1)s,%(root2)s" % (root))

def root_case7(a,b,d):
    """ when b^2-4ac is negetive """
    xplus = (- b +  cmath.sqrt(d)) / (2 * a)
    xminus = (- b -  cmath.sqrt(d)) / (2 * a)
    #root = {'root1':xplus,'root2':xminus}
    xplus_real = xplus.real
    xplus_imag = xplus.imag
    root1  = "(%2.2f + %2.2fi)"%(xplus_real,xplus_imag)
    root2  = "(%2.2f - %2.2fi)"%(xplus_real,xplus_imag)
    root = root1 +"\n "+ root2

    #return ("%(root1)s,%(root2)s" % (root))
    return root

def print_line(a,b,c,r):
    print "==============================================================" 
    print "(a,b,c) = (%4.1f,%4.1f,%4.1f)" % (a,b,c) 
    print "--------------------------------------------------------------" 
    print "f(x) = (%2.1f) * x^2 + (%2.1f) * x + (%2.1f)" % (a,b,c) 
    print "--------------------------------------------------------------" 
    print ("roots:\n %s" % (r)) 
    
def writefile(outfile,a,b,c,r):
    outfile.write("===========================================================" + "\n")
    outfile.write("(a,b,c) = (%4.1f,%4.1f,%4.1f)" % (a,b,c) + "\n")
    outfile.write("-----------------------------------------------------------" + "\n")
    outfile.write("f(x) = (%2.1f) * x^2 + (%2.1f) * x + (%2.1f)" % (a,b,c) + "\n")
    outfile.write("-----------------------------------------------------------" + "\n")
    outfile.write("roots:\n %s" % (r) + "\n")
        
def main():
    """ main function """
    infile = open("quadabc.txt","r")   # open file 
    outfile = open("quadroots.txt", "w") # only write 
    outfile.write("Yanhong Simokat" + "\n")
    outfile.write("Classid 111" + "\n")
    outfile.write("mcs260su16, project 1" + "\n")
    for line in infile:
        line = line.strip()   
        if line == "":  # ignore blank lines
            continue
        if line[0] == "#":  # ignore comments
            continue
        # print line  # for debugging
        a,b,c = get_abc(line) # extract a,b,c
        #print "(a,b,c): ", a,b,c  # for debugging
        d = descriminant(a,b,c)  # discriminant
        #print d # for debugging
        if a == 0 and b == 0 and c == 0:
            r = root_case1(a,b,c) # all complex numbers are roots
        elif a == 0 and b == 0 and c != 0:
            r = root_case2(a,b,c)   # no real or complex roots
        elif a == 0 and b != 0 and c == 0:
            r = root_case3(a,b,c) # root is zero
        elif a == 0 and b !=0 and c != 0:
            r = root_case4(a,b,c) # one roots
        elif a != 0 and d == 0:  # use the quadratic formula
            r = root_case5(a,b)
        elif a != 0 and d > 0:  # two real roots
            r = root_case6(a,b,d)
        elif a != 0 and d < 0:  # two complex roots
            r = root_case7(a,b,d)
        # print type(r)  #for debugging,r are strings
        print_line(a,b,c,r)
        writefile(outfile,a,b,c,r)
    infile.close() # close input file
    outfile.close() # close output file
if __name__ == "__main__":
    main()
