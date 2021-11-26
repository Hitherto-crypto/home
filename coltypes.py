True+False==1 # 1+0==1
True*True==1 # 1*1==1

#LIST -an ordered collection of unique values
a=[1,2,3]
b=['a',1,'python',(1,2),[1,2]]
b[2]='something else' #allowed

a='123'
b=int(a)
a='123.456'
b=float(a)
#c=int(a) #Valueaerror: invalid literal forint( with base 10: '123.456

d=int(b) #123

a='hello'
list(a)
set(a)
tuple(a)

names=["Alice","Bob","Craig","Diana","Eric"]
print(names[0])
print(names[2])

print(names[-1])
print(names[-4])

names[0]="ann"
print(names

first_names={"Adam","Beth","Charlie"}
# you can build a set usimg the existing list:
my_list=[1,2,3]
my_set=set(my_list)

#check membership of the set using in:

if name in first_names:
    print(name)

