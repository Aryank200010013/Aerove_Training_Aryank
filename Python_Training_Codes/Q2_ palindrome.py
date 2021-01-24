num0=int(input())
num=num0
case=0
j=1


while (case==0):
    num=num+j
    num1=num
    digit=0
    rev=0

    while (num1 != 0):
        num1=int(num1/10)
        digit=digit+1

    #print(digit)
    num1=num

    for k in range(0,digit):
        rev=rev*(10)+(num1 % 10)
        num1=(int(num1/10))

    num1=num

    if (num1==rev):
        print(num)
        case=1