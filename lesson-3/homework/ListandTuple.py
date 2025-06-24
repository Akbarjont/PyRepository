1. Create and Access List Elements
Create a list containing five different fruits and print the third fruit.

  fruits = ['olma', 'anor', 'nok', 'uzum', 'behi']
print(fruits[2])

2. Concatenate Two Lists
Create two lists of numbers and concatenate them into a single list.

list1 = ['123', '456', '789']
list2 = ['987', '654', '321']
list3 = list1+list2
print(list3)

3. Extract Elements from a List
Given a list of numbers, extract the first, middle, and last elements and store them in a new list.

list4 = ['123', '456', '789', '987', '654', '321']
newlist = (list4[0], list4[len(list4)//2], list4[-1])
print(newlist)

4. Convert List to Tuple
Create a list of your five favorite movies and convert it into a tuple.

  list5 = ['Gladiator', 'Interstellar', 'The Departed', 'Jurassic Park', 'Mikki 17']
tuple(list5)

5. Check Element in a List
Given a list of cities, check if "Paris" is in the list and print the result.

  list6 = ['Maris', 'Haris', 'Taris', 'Karis', 'Paris']
if 'Paris' in list6:
        print('Yes, Paris is there') 
else: 
        print('No Paris in the list')


6. Duplicate a List Without Using Loops
Create a list of numbers and duplicate it without using loops.

list7 = [3, 1, 4, 6, 7]
list8 = list7.copy()
print(list8)

7. Swap First and Last Elements of a List
Given a list of numbers, swap the first and last elements.

list8[0], list8[-1] = list8[-1], list8[0]
print(list8)

8. Slice a Tuple
Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.

tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tuple1[3:7])

9. Count Occurrences in a List
Create a list of colors and count how many times "blue" appears in the list.

list9 = ['white', 'blue', 'red', 'blue', 'green']
print(list9.count('blue'))

10. Find the Index of an Element in a Tuple
Given a tuple of animals, find the index of "lion".

  tuple2 = ('cow', 'dog', 'lion')
print(tuple2.index('lion'))

11. Merge Two Tuples
Create two tuples of numbers and merge them into a single tuple.

tuple3 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tuple4 = (2, 5, 6, 9, 3, 1, 4, 8, 9, 10)
tuple5 = tuple3 + tuple4
print(tuple5)

12. Find the Length of a List and Tuple
Given a list and a tuple, find and print their lengths.

  print(list9)
print(tuple5)
print(len(list9), len(tuple5))
  
13. Convert Tuple to List
Create a tuple of five numbers and convert it into a list.

tuple6 = tuple5[0:5]
list10 = list(tuple6)
print(tuple6)
print(list10)

14. Find Maximum and Minimum in a Tuple
Given a tuple of numbers, find and print the maximum and minimum values.

print(tuple6)
print(max(tuple6))
print(min(tuple6))

15. Reverse a Tuple
Create a tuple of words and print it in reverse order.

tuple8 = tuple(list9)
print(tuple8)
print(tuple(reversed((tuple8))))
