a = [1,2,3,4,5,6,7,8,9,10]
b = ['a','b','c','d','e','f','g','h','i','j']

c = {}
for i in range(len(a)):
    c[b[i]] = a[i]

print(c)    