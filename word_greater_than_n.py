def longword(n,str):
    word_len=[]
    text=str.split(" ")
    for x in text:
        if len(x)>n:
            word_len.append(x)
    return word_len
print(longword(3,"fox is cruel"))