def mainn():
    print ("How are you")
mainn()

def chin(name="David"):
    print("My name is ",name)
    return

def modify(fList):
    fList.append(4)
    fList.append(5)

def printinfo(arg1, *vartuple):
        "This prints a variable passed arguments"
        print("Output is ",arg1)
        for var in vartuple:
            print(var,end ="\t")

        return;



#chin()
myList = [1,2,3]
#modify(myList)
#print(myList)
#printinfo( 10 )
#printinfo( 70, 60, 50 )
# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2;

# Now you can call sum as a function
print (sum( 10, 20 ))




