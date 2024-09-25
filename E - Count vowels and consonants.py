vow = ['a','e','i','o','u','A','E','I','O','U']
value = str(input())
v=0
c=0
for i in value:
    if i in vow:
        v+=1
    else:
        c+=1
print("vowel is :", v)
print("consonent:", c)