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
    if b == 0:
        return False

def rootsg(a,b,c):
    """ to find one root """
    root2 = - c / b
    return root2

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

def main():
    """ main function """
    infile = open("quadabc.txt","r")   # open file 
    for line in infile:
        line = line.strip()   
        if line == "":  # ignore blank lines
            continue
        if line[0] == "#":  # ignore comments
            continue
        # print line  # for debugging
        a,b,c = get_abc(line) # extract a,b,c
        print "(a,b,c): ", a,b,c 
        if a == 0:     #specail cases where a = 0
            if  b == 0:
                if c == 0:
                    case1 = rootsd(a,b,c)
                    print case1
                    print
                elif c != 0:
                    case2 = rootsf(a,b,c)   
                    if case2 == False:
                        print "No real or complex roots"
                        print
            elif b != 0:
                if c == 0:
                     x = 0
                     print x
                     print
                elif c != 0:
                    case3 = rootsg(a,b,c)
                    print case3
                    print

        elif a != 0:  # use the quadratic formula
            d = descriminant(a,b,c)  # discriminant
            #print d # for debugging
            if d == 0:  # case 4: perfect square
                case4 = rootsi(a,b)
                print case4
                print
            elif d > 0:  # case 5: two real roots
                case5 = rootsj(a,b,d)
                print case5
                print
            elif d < 0:  # case 6: two complex roots
                i = cmath.sqrt(-1)
                case6 = rootsk(a,b,d,i)
                print case6   
    infile.close()
if __name__ == "__main__":
    main()
