# 1. Sort a Dictionary by Value. Write a Python script to sort (ascending and descending) a dictionary by value.

my_dict = {'яблоко': 3, 'банан': 1, 'вишня': 4, 'апельсин': 2}
sorted_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
sorted_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Сортировка по возрастанию:")
print(sorted_asc)

print("\nСортировка по убыванию:")
print(sorted_desc)



# 2. Add a Key to a Dictionary. Write a Python script to add a key to a dictionary.

d = {0: 10, 1: 20}
d[2] = 30
print(d)

# 3. Concatenate Multiple Dictionaries. Write a Python script to concatenate the following dictionaries to create a new one.

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}


result = {}
for d in (dic1, dic2, dic3):
    result.update(d)
print(result)



# 4. Generate a Dictionary with Squares. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

n = 5
squares = {x: x*x for x in range(1, n+1)}
print(squares)



# 5. Dictionary of Squares (1 to 15). Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.

squares = {x: x**2 for x in range(1, 16)}
print(squares)


# 1. Create a Set. Write a Python program to create a set.

my_set = {1, 2, 3, 4, 5}
print(my_set)


# 2. Iterate Over a Set. Write a Python program to iterate over sets.

my_set = {'apple', 'banana', 'cherry'}
for item in my_set:
    print(item)


# 3. Add Member(s) to a Set. Write a Python program to add member(s) to a set.

my_set = {1, 2, 3}
my_set.add(4)
print("After adding 4:", my_set)
my_set.update([5, 6, 7])
print("After adding 5, 6, 7:", my_set)



# 4. Remove Item(s) from a Set. Write a Python program to remove item(s) from a given set.


my_set = {1, 2, 3, 4, 5}

my_set.remove(3)
print("remove(3):", my_set)


my_set.discard(10) 
print("discard(10):", my_set)


removed = my_set.pop()
print(f"pop(): {removed}, set: {my_set}")

my_set.clear()
print("clear():", my_set)



#. 5. Remove an Item if Present in the Set. Write a Python program to remove an item from a set if it is present in the set.
my_set = {1, 2, 3, 4, 5}

element = 3

if element in my_set:
    my_set.remove(element)
    print(f"{element} olib tashlandi: {my_set}")
else:
    print(f"{element} to‘plamda yo‘q: {my_set}")



