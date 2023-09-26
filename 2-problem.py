popular_words = ("When I was One I had just begun When I was Two I was nearly new").split(" ")
ls = ['I', 'was', 'Three', 'near']

dic={}
for i in ls:
    if i in popular_words: 
        dic[i] = popular_words.count(i)
    else:
        dic[i] = 0
print(dic)
