def lex(s):
    tok=[]
    c=""
    for i in s:
        if i=='+' or i=='-' or i=='*' or i=='/' or i=='(' or i==')':
            if c!='':tok.append(int(c))
            tok.append(i)
            c=""
        else:
            c+=i
    if c!='': tok.append(c)
    return tok
