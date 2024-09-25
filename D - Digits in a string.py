num = input()
for char in num:
  if char.isdigit(): # akn jodi char digit hoi toahole yes print korbe
    print("Yes")
  else:
    print("No")

#hacker rank a same ans nai ni tai amra nicher man ta bosabo:
digits=['0','1','2','3','4','5','6','7','8','9']
n=str(input())
c=0
for i in n:
    if i not in digits:
        c+=1
    else:
        pass
if c!=0:
    print('No')
else:
    print('Yes')
