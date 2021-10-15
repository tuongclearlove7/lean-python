# A Python program to generate squares from 1 
# to 100 using yield and therefore generator 
  
# An infinite generator function that prints 
# next square number. It starts with 1 
def nextSquare(): 
    i = 1; # biến i = 1
# An Infinite loop to generate squares  
    while True: 
        yield i*i 
        i += 1 # khi i+=1 thì i*i = 1*1 = 1 
        # Next execution resumes
#from this point
# driver code to test above generator
# function 
for num in nextSquare(): 
    if num > 100: 
# Bình Phương các số từ 1 đến 10 thành các số chính phương 
# cho khi nào đến số chính phương 100  
         break    
    print(num)# in ra 1 dãy số chính phương từ 1 đến 100
