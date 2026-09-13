a = "\nMohit is good"
# create the file with write mode.

# file =open("mohit.txt","w")
# file.write(a)

#Read the file with read() function.

# file=open("robot.txt","r")
# content =file.read()
# print(content)

# with key is also read the file in python
with open("mohit.txt","r") as file:
    content =file.read()
    print(content)

# append the text in file the perives text is not delete. add the text.
text=["\nmohit is good boy\n",
      "vicky is also a good boy\n",
      "saurave is bad boy in disenary"]
with open("robot.txt","a") as file:
    file.writelines(text)


file.close()