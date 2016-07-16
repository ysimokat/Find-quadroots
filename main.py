#!/usr/bin/env python

import cmath

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

def rootsd(a,b,c):
    """ a = 0, all complex numbers are roots """
    return "All complex numbers are roots" 

def rootsf(a,b,c):
    """ when a = 0, no real/complex roots """
    return "No real or complex roots"

def rootsg(a,b,c):
    """ to find one root """
    root2 = - c / b
    return root2

def rootsh(a,b,c):
    """ a,c = 0, b is real number """
    x = 0 / b
    return x

def rootsi(a,b):
    """ b^2-4ac = 0, perfect roots """
    root = - b / (2 * a)
    return root

def rootsj(a,b,d):
    """ b^2-4ac > 0,two real roots """
    xplus = (- b + cmath.sqrt(d)) / (2 * a)
    xminus = (- b - cmath.sqrt(d)) / (2 * a)
    return xplus,xminus

def rootsk(a,b,d,i):
    """ when b^2-4ac is negetive """
    xplus = (- b + i * cmath.sqrt(d)) / (2 * a)
    xminus = (- b - i * cmath.sqrt(d)) / (2 * a)
    return xplus,xminus

def print_line(a,b,c,r):
    print "==============================================================" 
    print "(a,b,c) = (%4.1f,%4.1f,%4.1f)" % (a,b,c) 
    print "--------------------------------------------------------------" 
    print "f(x) = (%2.1f) * x ** 2 + (%2.1f) * x + (%2.1f)" % (a,b,c) 
    print "--------------------------------------------------------------" 
    print "roots = %s" % (str(r)) 
    
def writefile(outfile,a,b,c,r):
    outfile.write("===========================================================" + "\n")
    outfile.write("(a,b,c) = (%4.1f,%4.1f,%4.1f)" % (a,b,c) + "\n")
    outfile.write("-----------------------------------------------------------" + "\n")
    outfile.write("f(x) = (%2.1f) * x ** 2 + (%2.1f) * x + (%2.1f)" % (a,b,c) + "\n")
    outfile.write("-----------------------------------------------------------" + "\n")
    outfile.write("roots = %s" % (str(r)) + "\n")
        
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
        if a == 0:     #specail cases where a = 0
            if  b == 0:
                if c == 0:
                    r = rootsd(a,b,c)
                elif c != 0:
                    r = rootsf(a,b,c)   
            elif b != 0:
                if c == 0:
                    r = rootsh(a,b,c)
                elif c != 0:
                    r = rootsg(a,b,c)

        elif a != 0:  # use the quadratic formula
            if d == 0:  # case 4: perfect square
                r = rootsi(a,b)
            elif d > 0:  # case 5: two real roots
                r = rootsj(a,b,d)
            elif d < 0:  # case 6: two complex roots
                i = cmath.sqrt(-1)
                r = rootsk(a,b,d,i)
        print_line(a,b,c,r)
        writefile(outfile,a,b,c,r)
    infile.close() # close input file
    outfile.close() # close output file
if __name__ == "__main__":
    main()
