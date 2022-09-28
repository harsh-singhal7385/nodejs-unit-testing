""" Hello to python script  """

li = [1,2,3,4,5]
print("Normal List",li)
li.sort()
print("Ascending Order Sorting",li)
li.sort(reverse=True)
print("Descending Order Sorting",li)
li.sort()
lis = li[:3]
liss = li[-3:]
print("Sub Array of first 3 elements", lis)
print("Sub Array of last 3 elements", liss)
