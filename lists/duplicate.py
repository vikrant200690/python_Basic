numbers= [10,20,30,10,40,30,50,50]

duplicate_count=0
for num in set(numbers):
  if numbers.count(num)> 1:
   duplicate_count= +1
   print(num, "appears", numbers.count(num), "times")
    
print("Total duplicate elements:", duplicate_count)