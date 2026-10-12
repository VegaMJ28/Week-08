#*.txt #text storage
#*.dat #object

#MYSQL databas



#storage into text file
file1 = open("mytext.txt", "w")
file1.writelines("\nHello World!")
file1.writelines(input("\nEnter your name?"))
file1.writelines("\nHave a nice day!")
file1.close()

file2 = open("mytext.txt", "r")
for line in file2:
    print(line)

if MJ in line:
    print (line)
file2.close()

