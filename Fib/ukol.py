a0 = 0
a1 = 1
a = 0
num = int(input("cislo"))
num1 = 0
while num1 < num:
    a1 = (a1+a0)
    print(a1)
    a0 = (a1+a0)
    print(a0)
    num1 += 1
    