# Program: Count duplicate elements in a list
numbers= [10,20,30,10,40,30,50,50]

duplicate_count=0
for num in set(numbers):
  if numbers.count(num)> 1:
   duplicate_count= +1
   print(num, "appears", numbers.count(num), "times")
    
print("Total duplicate elements:", duplicate_count)


# Program: Count duplicate elements in a list
# Program: Count duplicate elements in a list
numbers= [10,20,30,10,40,30,50,50,10]
count=0
memory=[]
for i in numbers:
    if i in memory:
        continue
    else:
        for j in numbers:
            if i==j:
                count+=1
        print(i,"appears",count)
        memory.append(i)
        count=0
        
