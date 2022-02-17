def swappingFiles():
    a=input("Enter the file 1:")
    b=input("Enter the file 2:")
    with open(a,'r') as a1:
        data_a=a1.read()
    with open(b,'r') as b1:
        data_b=b1.read()
    with open(a,'w') as a1:
        a1.write(data_b)
    with open(b,'w') as b1:
        b1.write(data_a)
swappingFiles()                    