# we will read the file

with open("Python/9-file handling/text.txt","r") as file :
    print(file.read())


with open("Python/9-file handling/text.txt","r") as file :
    f=file.readline()
    print(f)


with open("Python/9-file handling/text.txt","r") as file :
    f=file.readlines()
    print(f)

    