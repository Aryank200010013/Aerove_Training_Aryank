fh=open("myFirstFile.txt","w")

limit=int(input())
first=0
last=0

for j in range(10**(limit-1),10**limit):
    for i in range(2,j):
       if (j % i) == 0:                     
           break
    else:
        last=first
        first=j
        if (first-last==2):
            print(f"{last} {first}")
            fh.write(f"{last} {first}")
            fh.write('\n')

            

       
       