# file=open("sample.txt","w") #if file does not exist then it will create and then write
# file.write("Hi, welcome to files concept..")
# file.close()

# file=open("example.txt","a")
# file.write("Appending this line.\n")
# file.close()

# file=open("sample.txt","r")
# content=file.read()
# print(content)

# creating a file using exclusive mode ('x') used to create a new file if it does not exist
# try:
#     file=open("newfile.txt","x")
#     file.write("Exclusive file data")
#     file.close()
# except FileExistsError:
#     print("File already exist!")


#read, readline(), readlines()- Methods to read file
#if we use "with" then no need close file it will handle it
# with open("sample.txt","w") as file: #when we are writing into a file then all previous content in file will be removed and current text is written in it
#     file.write("Line 1\nLine 2\nLine3\n")

# with open("sample.txt","r") as file:
#     content=file.read() #reads entire content
#     print(content)

# with open("sample.txt","r") as file:
#     content=file.readline() #reads a single line 
#     print(content)

# with open("sample.txt","r") as file:
#     content=file.readlines() #returns a list of each line
#     print(content)

#using write
# with open("sample.txt","a") as file: # to preserve the previous content of file using "a" mode
#     file.write("content of in this line")

# lst=["\ncontent1\n","content2\n","content3\n"]
# with open("sample.txt","a") as file:
#     file.writelines(lst)

#creating a temporary file
# with open("delete_me.txt","w") as file:
#     file.write("This file is deleted.\n")

# import os 
# if os.path.exists("delete_me.txt"):
#     os.remove("delete_me.txt")
#     print("File deleted successfully")
# else:
#     print("File not found.")

#try-except- Handles file-related errors gracefully

try:
    with open("non-existent.txt","r") as file:
        content=file.read()
        print(content)
except FileNotFoundError:
    print("File is not present")
except PermissionError:
    print("Error: Permission denied.")
except Exception as e:
    print(f"An unexpected error occured :{e}")



