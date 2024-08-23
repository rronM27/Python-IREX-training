#read and process lines
with open("example.txt","r") as file:
    for line in file:
        cleaned_line=line.strip()
        print(cleaned_line)

#split lines into words
with open("example.txt","r") as file:
    for line in file:
        words=line.strip().split()
        print(words)

#concatinating strings
name="Alice"
age=30
with open("example.txt","w") as file:
     file.write("Name: "+name+"\n")
     file.write("Age: "+str(age)+"\n")
#fortting strings
with open("example.txt","w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"age: {age}\n")

#Reading modifing and writing data
with open("example.txt","r") as infile, open("output.txt","w") as outfile:
    for line in infile:
        cleaned_line=line.strip()
        modified_line=cleaned_line.replace("Line 1 ","Line X")
        outfile.write(modified_line+"\n")
