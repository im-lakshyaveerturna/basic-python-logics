#Quadratic equation solver
#Displays only integral roots
#Range limit: [-1000,1000] (c'mon, it's a python code with double for loops, you know... )


a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
count = 0

for i in range(-1000,1001):
    for n in range(-1000,1001):
        if int(i*n) == int(a*c) and int(i + n) == b and count == 0:
            print('Roots:',str(i)+',',n)
            count += 1
            
            
if count == 0:
    print('No integral number roots')
            
    
            

         
            
        
