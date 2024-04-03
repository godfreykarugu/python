
try:
    f = open("employees.txt", "r")
    try:
    #print(f.read())
    #print(f.readline())
    #print(f.readlines())
        for line in f:
            print(line)


    except:
        print('Something went wrong while printing the file')
    finally:
        f.close()
except:
    print("File not found")
