# we will write in contant 

# f=open("Python/9-file handling/text.txt","w")
# f.write("this is my first class of file handling ")
# f.close()


# f=open("Python/9-file handling/text.txt","w")
# f.write("this is my second class of file handling ")
# f.close()



# with 
with open("Python/9-file handling/text.txt","a") as file :
    file.write("\n this is form aappend mode \n")


with open("Python/9-file handling/text.txt","a") as file:
    file.writelines("Hello \n this is our file handling \n thank u ")