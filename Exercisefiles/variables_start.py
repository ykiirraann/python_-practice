#example for variable

myint = 5
myfloat = 13.2
mystr = "This is a string"
mybool = True
mylist = [0, 1, "two", 3.2, False]
mytuple = (0,1,2)
mydict = {"one": 1, "two": 2}

#print(myint)
#print(myfloat)
#print(mystr)
#print(mybool)
#print(mylist)
#print(mytuple)
#print(mydict)


#re-declaring a variable
#myint = "abc"
#print(myint)

# # to access a member of a sequence type, use[]
# print(mylist[2])
# print(mytuple[1])

# # to slices to get parts of a sequence 
# print(mylist[1:5])
# print(mylist[1:5:2])

# # you can use slices to reverse a sequence
# print(mylist[::-1])

# dictionaries are accessed via keys
# print(mydict["one"])


# # ERROR : variables of different types cannot be combined
# print("string type" +str(123))


# Global vs,  local variable functions
# def someFunction():
#     mystr = "def"
#     print(mystr)
#     # this prints def and This is a string
# someFunction()
# print(mystr)

def someFunction():
    global mystr     #this changes the global scope value
    mystr = "def"
    print(mystr)
someFunction()
print(mystr)

del mystr    #deletes the previous var
print(mystr)


ball = "green";
print(ball);
