# Lệnh return

# Bài toán tính chu vi hình chữ nhật

def caller(width, height):
    er = (width + height) * 2
    return er
# ta có er = width+height * 2
rec_width = 5 
rec_height = 3
# rec_width = 5 rec_height = 3+5*2
rec = caller(rec_width, rec_height)
print(rec)# in ra kết quả 

print(caller(7, 5)) 
# caller(7, 5) => 7+5*2 

def _return_ter_function():
    print('sử dụng return ngắt hàm')
    return
    print('hàm k được gọi')
none = _return_ter_function()
print(type(none))


one, two, three = 'tuong', 'clearlove', 7
tuong = 'C', 'learlove7', 2002
print(one, two, three,tuong)

def cal_rec_area_per(width, height):
    Perimeter = (width+height) * 2
    area = width * height
    return Perimeter, area 
    # khởi tạo 2 giá trị Perimeter, area 
rec_width = 3
rec_height = 9
# Gía trị thứ nhất Perimeter = 3+9*2
# giá trị thứ 2 area = 3*9 
rec, rec_area = cal_rec_area_per(rec_width, rec_height)
print(rec, rec_area)# in ra giá trị



def SUM(a,b):
    #print("hello world !")
    c = a+b
    return c
total = SUM(a=16,b=9)
print(total)



