
f = open("employees.txt",'a')
f.write("\n HR: Elizabeth")
f.close()

f = open("employees.txt",'r')
for line in f:
    print(line)
f.close()
