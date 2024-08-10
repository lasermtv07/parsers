#!/usr/bin/python
import lex as l
import copy
s='25+3*5-8-4'
s=l.lex(s)
s.append('$')
print(s)
i=0
exp=[]
def prec(j):
    if j=='$': return -1
    elif type(j)==int or j.isdigit(): return 40
    elif j=='+' or j=='-': return 10
    elif j=='*' or j=='/': return 20
    elif j=='(' or j==')': return 50

def parseExp(minPrec=-1):
    global i
    exp=[]
    op=s[i]
    while prec(op)>=minPrec:
        print(op)
        if op in ['+','-','*','/']:
            if op=='-': print(exp)
            i+=1
            exp=[op,copy.deepcopy(exp),parseExp(prec(op))]
            i-=1
        if prec(op)==40:
            exp.append(int(op))
        i+=1
        #print(exp)
        try:
            op=s[i]
        except:
            return exp
        if prec(op)<=minPrec:
            return exp
    return exp
exp=parseExp()
print(exp)
