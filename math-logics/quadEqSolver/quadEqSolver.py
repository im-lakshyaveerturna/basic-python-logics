#Quadratic equation solver
#Displays only integral roots
#Range limit: [-1000,1000] (speed limit maybe compromised significantly for longer ranges)


a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

count = 0
add = b
product = a*c

for i in range(-1000,1001):
    if count == 0:
        for n in range(-1000,1001):
            
            if (i*n) == product and (i + n) == add:
                print('Roots:', str(i) + ',', n)
                count += 1
        
            
if count == 0:
    print('No integral number roots')
            
     
    
            

         
            
        
