import os
path = "c:\\Users\\devshankhasharm\\rr"
#os.rmdir(path)
path1 = "c:\\Users\\devshankhasharm\\AAAA"
#os.mkdir(path1,0o777)
path2 = "C:\\Users"
print(os.listdir(path2))
if 'Public12' in os.listdir(path2):
    print("It exists in the directory")
