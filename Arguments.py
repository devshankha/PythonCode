def mm(*args):
    print(type(args))
    for i in args:
        print(i,end=" ")

def myFun(**kwargs):
     for key, value in kwargs.items():

         print("%s == %s" % (key, value))


def nn(** kwargs):
    print(type(kwargs))
    for key,value in kwargs.items():
        print("Key is %s and value is %s"%(key,value))
        print("Key is {} and Value is {}".format(key, value))
#mm("This","is","cool")
nn(Name1="david",age="34")
#myFun(first ='Geeks', mid ='for', last='Geeks')