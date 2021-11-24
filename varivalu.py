#integer
a=2
print(a)
#output: 2
b=2010
print(b)
#floating point
pi=3.14
print(pi)
#output: 3.14
c="A"
print(c)
#String
name="Victor Moses"
print(name)
#output: Victor Moses
import keyword
print(keyword.kwlist)

#Empty value or null data type
x=None
print(x)
#Output:None

a=2
print(type(a))
#output:< 'int'>
name="Victor Moses"
print(type(name))
#output: < 'str'>

q=True
print(type(q))
#output:<type'bool'>

a,b,c=1,2,3
print(a,b,c)
#output: 1 2 3

a,b,_=1,2,3
print(a,b)
#output:1,2

a=b=c=1
print(a,b,c)
#output: 1 1 1

a=b=c=1 #all the three names a,b and c refer to same int objects with value 1
print(a,b,c)
b=2 #b now refers to another int object one with a value of 2
print(a,b,c)
#output: 1 2 1

x=y=[7,8,9] # x and y refer to the same list of objects just created
x=[13,8,9] # x now refers to the newly created list
print(y) # y sill refers to the list it was first assigned
#output: 7,8,9

x=y=[7,8,9]
x[0]=13 # we are updating the values of the list through one value x
print(y)
# output: 13 8 9

x=[1,2,[3,4,5],6,7] #this is nested list
print(x[2])
# output:[3 4 5]








