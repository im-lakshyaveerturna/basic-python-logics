calclist= []
def calc():
    
    num = int(input('Enter a number: '))
    calclist.append(num)
    
    op = input('Enter a operator or enter "c" to calculate: ')
    
    if op != 'c': 
      calclist.append(op)
      
      num2 = int(input('Enter a number: '))
      calclist.append(num2)
      
      calc_real()

def calc_real():
    op = input('Enter an operator or enter "c" to calculate: ')
    
    if op == "c":
        
        
        lencalc = len(calclist)
        i = 0
        j = 0
        k = 0
        l = 0
        
        while i < lencalc:
            if calclist[i] == '/':
                if i - 1 >= 0 and i + 1 < lencalc:
                    
                    res = calclist[i-1] / calclist[i+1]
                    calclist[i-1] = res
                    calclist.pop(i)
                    
                    calclist.pop(i)
                    lencalc = len(calclist)
                    
                else:
                    print("Invalid input")
                    break
            else:
                i += 1
                
        while j < lencalc:
            if calclist[j] == '*':
                if j - 1 >= 0 and j + 1 < lencalc:
                    res = calclist[j-1] * calclist[j+1]
                    calclist[j-1] = res
                    calclist.pop(j)
                    calclist.pop(j)
                    lencalc = len(calclist)
                else:
                    print("Invalid input")
                    break
            else:
                j += 1
                
                
        while k < lencalc:
            if calclist[k] == '+':
                if k - 1 >= 0 and k + 1 < lencalc:
                    res = calclist[k-1] + calclist[k+1]
                    calclist[k-1] = res
                    calclist.pop(k)
                    calclist.pop(k)
                    lencalc = len(calclist)
                else:
                    print("Invalid input")
                    break
            else:
                k += 1
                
        while l < lencalc:
            if calclist[l] == '-':
                if l - 1 >= 0 and l + 1 < lencalc:
                    res = calclist[l-1] - calclist[l+1]
                    calclist[l-1] = res
                    calclist.pop(l)
                    calclist.pop(l)
                    lencalc = len(calclist)
                else:
                    print("Invalid input")
                    break
            else:
                l += 1
    else:
        num3 = int(input('Enter a number: '))
        calclist.append(op)
        calclist.append(num3)
    
        calc_real()

calc()
print(calclist[0])
