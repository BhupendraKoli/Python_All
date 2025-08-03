# create a file 
# write a python prohram to count the char in a file 

open("Python/9-file handling/text1.txt","w")

with open("Python/9-file handling/text1.txt","a") as file :
    file.write("Hello \n this is our file handling \n thank u")


with open("Python/9-file handling/text1.txt","r") as file :
    f=file.read()
    print(len(f))


# write a python program to count the number of lines in a file 

with open("Python/9-file handling/text1.txt","r") as file :
    f=file.readlines()
    print(len(f))

# write a python peogram to count the number of words in a file
    

with open("Python/9-file handling/text1.txt","r") as file :
      data = file.read()   
      w = data.split()
      w= len(w)
      print(w) 


# write a script to find and replace a word in a text file 

with open("Python/9-file handling/text1.txt","r") as file :
      data = file.read() 
      o="Hello"
      n="Bhupendra"
      new=data.replace(o,n)
      print(new)


# Write a Python program that asks the user for a word to find 
# and a word to replace it with. Then it opens a file named notes.txt, 
# replaces all occurrences of the word, and saves the changes in the same file.
# Open the file in read mode
# Ask the user for input
find = input("Enter the word to find: ")
replace = input("Enter the word to replace it with: ")
with open("Python/9-file handling/text1.txt", "r") as file:
    content = file.read()
updated = content.replace(find, replace)
with open("Python/9-file handling/text1.txt", "w") as file:
    file.write(updated)
print("All occurrences of the word have been replaced.")
