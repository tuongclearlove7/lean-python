def Play_Matrix(matrix_x, matrix_y, matrix_1, matrix_2):
    print("",matrix_x,"\n",matrix_y,"\n", matrix_1,"\n",matrix_2)
    
arr = [
         [1,2,3,[0,1,2,[1,2,3],
         [2,3,4],[3,4,5]]],
         [4,5,6],[7,8,9]]

print('',arr[0][3][0:3])
print('',arr[0][3][3])
print('',arr[0][3][4])
print('',arr[0][3][5])

Play_Matrix(arr[0][3][0:3],arr[0][0:3],arr[1],arr[2])


   






