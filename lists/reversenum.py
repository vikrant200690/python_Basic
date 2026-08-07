n = int(input("enter a number"))
store =0 
while n>0:
 last= n%10
 store = store*10 + last
 n=n//10
print(store)