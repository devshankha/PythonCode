import os

#print(os.environ)
str = os.environ
print(os.environ)
if 'APPDATA' in str:
    print("APPDATA exists")
else:
    print("APPDATA doesnot exist")

# Note that the environment variable key-value pair must be a string, otherwise an error will be raised.
os.environ['MYSQL_VERSION'] = '5.7.18'
os.putenv('MYSQL_VERSION', '5.7.18')

print(os.getcwd())

#print(os.getcwdb())
print(os.name)

r = os.getcwd()

#replace all \ with /
r = r.replace("\\", "/")
#print("\"")
#print("\"\"")
#print(r)
out = os.path.isdir("C:\\Users\\sdsd")
print(out)
ff =os.path.join("c:\\", "Users")
print(os.path.isdir(ff))