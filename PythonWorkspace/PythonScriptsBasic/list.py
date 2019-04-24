#List Count (very important, most cases used for Data Science)

numbers = [1,2,3,1,3,4,2,5]

#frequency of 1 in a list
print(numbers.count(1))

#frequency of 3 in a list
print(numbers.count(3))


#List Looping
lst = ['one','two','three','four']
for ele in lst:
    print(ele)


#-----------List Comprehension--------------
  
#following snippet is normal, i.e as same as other prog lang 
 
 #without list comprehension
squares = []
for i in range(10):
    squares.append(i**2)
print(squares)

#following snippent is special in python i.e "using list comprehension"
squares = [i**2 for i in range(10)]
print(squares)

#eg1
lst = [-10,-20,10,20,50]
new_lst = [i*2 for i in lst]
print("example 1: {}".format(new_lst))

#eg2 (filter to exclude negative number)
new_lst = [i for i in lst if i>=0]
print("example 2: {}".format(new_lst))

#eg3 (create list of tuples)
new_lst = [(i,i**2) for i in range(10) ]
print("example 3: {}".format(new_lst))


#-----------matrix-----------
#following snippet is to find out the transpose of the matrix in two different ways
transpose = []
matrix = [
    [1,2,3,4],[5,6,7,8],[9,10,11,12]
]
#1st method
for i in range(4):
    lst = []
    for row in matrix:                        
        lst.append(row[i])
    transpose.append(lst)
print(transpose)

#2nd method
transpose = [[row[i] for row in matrix] for i in range(4)]
print("2nd method: {}".format(transpose))

