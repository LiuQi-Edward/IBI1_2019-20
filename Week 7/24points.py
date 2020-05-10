#def function
def calculate(numbers):
    global found
    global times
    if len(numbers)==1:
        if numbers[0]==24:
            found=True
        return#stop when getting 24
    
    for i in range(0,len(numbers)-1):
        for j in range(i+1,len(numbers)):
            
            #create a list without i and j and then add their result
            numbers_except=[]
            for k in range(0,len(numbers)):
                if k!=i and k!=j:
                    numbers_except.append(numbers[k])
            #+
            #Here, we can either add "if" sentence or not add it
            numbers_next=numbers_except+[numbers[i]+numbers[j]]
            calculate(numbers_next)
            times+=1
                    
            #-
            if found==False:
                if numbers[i]>numbers[j]:
                    numbers_next=numbers_except+[numbers[i]-numbers[j]]
                    calculate(numbers_next)
                    times+=1
                else:
                    numbers_next=numbers_except+[numbers[j]-numbers[i]]
                    calculate(numbers_next)
                    times+=1
                    
            #*
            if found==False:
                numbers_next=numbers_except+[numbers[i]*numbers[j]]
                calculate(numbers_next)
                times+=1
                
            #/
            if found==False:
                if numbers[j]!=0:
                    numbers_next=numbers_except+[numbers[i]/numbers[j]]
                    calculate(numbers_next)
                    times+=1
                if numbers[i]!=0:
                    numbers_next=numbers_except+[numbers[j]/numbers[i]]
                    calculate(numbers_next)
                    times+=1
    return




num = input("Please input numbers to compute 24:(use ',' to divide them) \n" )
num = num.split(',')


#check if input meet standards 
for i in range(0,len(num)):
    if num[i].count('.') !=0:
        print('The input number must be integers from 1 to 23')
        break
    num[i]=int(num[i])
    if num[i] >23.5 or num[i] < 0.5:
        print('The input number must be integers from 1 to 23')
        break

found=False
times=0
calculate(num)
if found:
    print('Yes')
else:
    print('No')
print('Recursion times: '+str(times))
