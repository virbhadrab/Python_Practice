def ChkPrime(no1):
    
    sum = 0
    value = 0 
    
    for i in range(len(no1)):
        flag = True
        value = int(no1[i]/2)
        if value==0:
            flag = False
        else:
            for j in range(2,value+1):
                if (no1[i]%j==0):
                    flag = False
                    break
                else:
                    flag = True
                
        if flag==True:
            sum = sum + no1[i]   
                
    return sum