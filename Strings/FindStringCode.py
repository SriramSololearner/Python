s=input()
l=s.split(' ')

for word in l:
    for i in range(len(word)//2):                   # world wide web
        l=[]
        x=abs(ord(word[i])-ord(word(len(word)-i-1)))
        l.append(x)
        print(l)

