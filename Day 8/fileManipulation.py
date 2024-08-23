file_path=("example.txt")
file=open(file_path,"r")
content=file.read()
print(content)
file.close()


# way nr 2
file_path=("example.txt")
with open(file_path,"r") as file:
    content=file.read()
    print(content)
file.close()
# write onto files
with open(file_path,"w") as file:
    file.write("hello world")
file.close()

# find file
import os
if os.path.exists("rron.txt"):
    print("found !!!")

