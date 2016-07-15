#!/usr/bin/env python
""" file:main.py
    -main program file for project 1
    -input file 'quadabc.txt'
    -strip white space from beginning and end of strings 
    -ignore blank lines and the comments
    -convert each string of three characters to a list of character
    -convert a list of three strings to floats a,b,c,print a,b,c out
    -calculate descriminant d = b^2 - 4ac
    -calculate quadratic x1 = (-b + sqrt(d))/(2a)
    -calculate quadratic x2 = (-b - sqrt(d))/(2a)
    -write output to 'quadroots.txt'
"""

def get_abc(line):
    """ line is a string
        extract to float a,b,c 
        return a,b,c
    """
    list1 = line.split()  # split on whitespace
    # print list1  # for debugging
    a = float(list1[0])
    b = float(list1[1])
    c = float(list1[2])
    # print a,b,c # for debugging
    return a,b,c

def main():
    infile = open("quadabc.txt","r")   # open file 
    for line in infile:
        line = line.strip()   
        if line == "":  # ignore blank lines
            continue
        if line[0] == "#":  # ignore comments
            continue
        # print line  # for debugging
        a,b,c = get_abc(line)
        print a,b,c
    infile.close()
if __name__ == "__main__":
    main()
