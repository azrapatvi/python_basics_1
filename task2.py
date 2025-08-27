def sum_of_squares(numbers):
    return sum(x**2 for x in numbers)

res=sum_of_squares([1,2,3])
print(res)


def even_odd(numbers):
    even=[x for x in numbers if x%2==0]

    print(even)

even_odd([1,2,3,4,5])
    

dirty_data=[1, 2, 2, -3, "", None, 4, 5, 5, "hello", "hello"]

clean_data=set()

for item in dirty_data:
    if item==None or item=="":
        continue
    if isinstance(item, int) and item < 0:
        continue

    clean_data.add(item)
print(set(clean_data))

    
