import sys
input = sys.stdin.readline
import re

def first(string):
    return string.lower()

def second(string):
    p = re.compile("[^a-z0-9\-_.]")
    ret_str = p.sub("",string)
    return ret_str

def third(string):
    p = re.compile("\.+")
    ret_str =  p.sub(".",string)
    return ret_str

def forth(string):
    if string and string[0] == '.':
            string = string[1:]

    if string and string[-1] == '.':
            string = string[:-1]

    return string
        
def fifth(string):
    if string :
        return string
    else :
        return "a"

def sixth(string):
    L = len(string)
    if L >= 16 :
        string = string[:15]
        if string[-1] == '.':
            string = string[:-1]

    return string

def seventh(string):
    L = len(string)
    while L <  3 :
        string += string[-1]
        L += 1
    return string

def solution(string):
    string = first(string)
    # print("first",string)
    string = second(string)
    # print("second",string)
    string = third(string)
    # print("third",string)
    string = forth(string)
    # print("forth",string)
    string = fifth(string)
    # print("fifth",string)
    string = sixth(string)
    # print("sixth",string)
    string = seventh(string)
    # print("seventh",string)

    return string


inp_str = input()
print(solution(inp_str))
    

# ..ab.89JH07^&798..dfgd-_fUUIH*&*^..
# aaa.aa.aaaaaaa.aaaaddd