import keyword

lst = [10,20,50,12,46,25,12,1,12,13]

product = 1
index = 0

while index<len(lst):
    product *= lst[index]
    index += 1

print("Product is: {}".format(product))