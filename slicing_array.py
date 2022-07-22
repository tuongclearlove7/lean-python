#Viết chương trình chấp nhận một chuỗi số
#  phân tách bằng dấu phẩy từ giao diện điều khiển
#  tạo ra một danh sách và một tuple chứa mọi số.
#Ví dụ: Đầu vào được cung cấp là 34,67,55,33,12,98 thì đầu ra là:
#['34', '67', '55', '33', '12', '98']
#('34', '67', '55', '33', '12', '98')
#Viết lệnh yêu cầu nhập vào các giá trị 
# sau đó dùng quy tắc chuyển đổi kiểu dữ liệu để hoàn tất.
array = input("Nhập vào các giá trị : ")
l = array.split(",")# điều kiện phân tách bằng dấu phẩy
Lists = list(l)
t = tuple(l)
print(Lists)
print (t)

# Viết chương trình định nghĩa một class có ít nhất 2 method:
#getString: để nhận một chuỗi do người dùng nhập vào 
#print String: in chuỗi vừa nhập sang chữ hoa.
#Thêm vào các hàm hiểm tra đơn giản để kiểm tra method của class.
#Ví dụ: Chuỗi nhập vào là TUONGCLEARLOVE7
# thì đầu ra phải là: [TUONGCLEARLOVE7]
#Sử dụng __init__ để xây dựng các tham số.
# sử dụng mảng
class Input_string(object):
   def __init__(self):
       self.TUONG = ""
   def get_String(self):
       self.TUONG = input("Nhập chuỗi : ")
   def print_String(self):
       print (self.TUONG.upper())
stringObject = Input_string()
stringObject.get_String()
stringObject.print_String()

# bài tương tự tạo 1 biến nhập vào chuỗi từ người dùng (String)
# đầu ra là chữ viết Hoa
# Gợi ý : dùng phương thức upper
tuong = input(str("Nhập chuỗi : "))
print(tuong.upper())


#Viết một method tính giá trị bình phương của một số.
#Gợi ý:
#Sử dụng toán tử **.
x = int(input("Nhập một số : ")) 
def square(number): 
    return number ** 2
print(square(x)) #in bình phương của x

# viết một chương trình
# để in tài liệu về một số hàm Python được tích hợp sẵn như abs()
# int(), input() và thêm tài liệu cho hàm bạn tự định nghĩa.
#Gợi ý:
#Sử dụng __doc__
print (abs.__doc__)
print (int.__doc__)
print (input.__doc__)
def square(num):
    return num ** 2
def translate(translation = """ Dịch : Trả về giá trị tuyệt đối của đối số.
int ([x]) -> số nguyên
int (x, base = 10) -> integer
Chuyển một số hoặc chuỗi thành số nguyên hoặc trả về 0 nếu không có đối số
được tặng. Nếu x là một số, trả về x .__ int __ (). Đối với dấu chấm động
số, điều này cắt ngắn về không.
Nếu x không phải là số hoặc nếu là cơ số thì x phải là một chuỗi,
byte, hoặc phiên bản bytearray đại diện cho một số nguyên theo nghĩa đen trong
cơ sở cho trước. Chữ có thể đứng trước '+' hoặc '-' và được bao quanh
bởi khoảng trắng. Giá trị cơ sở mặc định là 10. Các cơ sở hợp lệ là 0 và 2-36.
Cơ sở 0 có nghĩa là giải thích cơ sở từ chuỗi dưới dạng một chữ số nguyên.
>>> int ('0b100', base = 0), 4
Đọc một chuỗi từ đầu vào chuẩn. Dòng mới ở cuối bị loại bỏ.
dấu dòng mới trước khi đọc đầu vào.
Nếu người dùng nhấn EOF (* nix: Ctrl-D, Windows: Ctrl-Z + Return)
hãy nâng hệ thống EOFError.On * nix, dòng đọc được sử dụng nếu có. không có"""):
    print(translation)
print(square.__doc__)
translate()


# viết chương trình Định nghĩa một lớp 
# gồm có tham số lớp và có cùng tham số instance
#Gợi ý: Khi định nghĩa tham số instance
#cần thêm nó vào __init__
#Bạn có thể khởi tạo một đối tượng với 
#tham số bắt đầu hoặc thiết lập giá trị sau đó.
class Person:# Định nghĩa lớp "name"
    name = "Person"
    def __init__(self, nickname = True):# self.name là biến instance
        self.name = nickname
my = Person("TuongClearlove")
print ("%s name is %s" % (Person.name, my.name))
crush = Person("ThaoRoser")
print ("%s name is %s" % (Person.name, crush.name))

#Viết chương trình
#và in giá trị theo công thức cho trước: Q = √([(2 * C * D)/H])
#(bằng chữ: Q bằng căn bậc hai của [(2 nhân C nhân D) chia H]. 
# Với giá trị cố định của C là 50 H là 30. 
# D là dãy giá trị tùy biến
# được nhập vào từ  người dùng
# các giá trị của D được phân cách bằng dấu phẩy.
#Ví dụ: Giả sử chuỗi giá trị của D nhập vào là
# 100,150,180 thì đầu ra sẽ là 18,22,24.
#Gợi ý : Nếu đầu ra nhận được là một số dạng thập phân
#bạn cần làm tròn thành giá trị gần nhất
# ví dụ 26.0 sẽ được in là 26.
#Trong trường hợp dữ liệu đầu vào được cung cấp cho câu hỏi
#nó được giả định là đầu vào do người dùng nhập từ người dùng
import math
c=50
h=30
value = []
items = [x for x in input("Nhập giá trị của d : ").split(",")]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
print (','.join(value))


#Viết một chương trình có 2 chữ số, X, Y 
# nhận giá trị từ đầu vào và tạo ra một mảng 2 chiều. 
# Giá trị phần tử trong hàng thứ i và cột thứ j của mảng phải là i*j.
#Lưu ý: i=0,1,...,X-1; j=0,1,...,Y-1.
#Ví dụ: Giá trị X, Y nhập vào là 3,5 thì 
# đầu ra là: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
#Viết lệnh để nhận giá trị X, Y từ giao diện điều khiển do người dùng nhập vào.
input_str = input("Nhập X, Y: ")
dimensions=[int(x) for x in input_str.split(',')]
row_Num = dimensions[0]# dimensions (kích thước)
col_Num = dimensions[1]
multi_list = [[0 for c in range(col_Num)] 
for i in range(row_Num)]
for i in range(row_Num):
    for c in range(col_Num):
        multi_list[i][c]= i*c
print(multi_list)

#Viết một chương trình chấp nhận chuỗi từ do người dùng nhập vào
# phân tách nhau bởi dấu phẩy và in những từ đó thành chuỗi theo thứ tự bảng chữ cái
# phân tách nhau bằng dấu phẩy.
#Giả sử đầu vào được nhập là: without,hello,bag,world
# thì đầu ra sẽ là: bag,hello,without,world.
#Trong trường hợp dữ liệu đầu vào được nhập vào chương trình nó nên được giả định
# là dữ liệu được người dùng nhập vào từ giao diện điều khiển.
items = [x for x in input("Nhập một chuỗi : ").split(',')]
items.sort()
print (','.join(items))

#Viết một chương trình chấp nhận chuỗi là các dòng được nhập vào
#chuyển các dòng này thành chữ in hoa và in ra màn hình. 
# Giả sử đầu vào là : #Hello world, Practice makes perfect
#Thì đầu ra sẽ là : HELLO WORLD , PRACTICE MAKES PERFECT
tuong = input("nhập vào chuỗi : ")
print(tuong.upper())

#Viết một chương trình chấp nhận đầu vào là một chuỗi các từ tách biệt bởi khoảng trắng
#loại bỏ các từ trùng lặp
# sắp xếp theo thứ tự bảng chữ cái, rồi in chúng.
#Giả sử đầu vào là: hello world and practice makes perfect and hello world again
#Thì đầu ra là: again and hello makes perfect practice world
#Gợi ý: Trong trường hợp dữ liệu đầu vào được nhập vào chương trình nó 
# nên được giả định là dữ liệu được người dùng nhập vào từ giao diện điều khiển.
#Sử dụng set để loại bỏ dữ liệu trùng lặp tự động và dùng sorted() để sắp xếp dữ liệu
s = input("Nhập chuỗi của bạn: ")
words = [word for word in s.split(" ")]
print (" ".join(sorted(list(set(words)))))

#Viết một chương trình chấp nhận đầu vào là chuỗi các số nhị phân 4 chữ số
#phân tách bởi dấu phẩy
#  kiểm tra xem chúng có chia hết cho 5 không. 
# Sau đó in các số chia hết cho 5 thành dãy phân tách bởi dấu phẩy.
#Ví dụ đầu vào là: 0100,0011,1010,1001
#Đầu ra sẽ là: 1010
value = []
items = [x for x in input("Nhập các số nhị phân : ").split(',')]
for p in items:
    int_p = int(p, 2)
    if not int_p%5:
        value.append(p)
print (','.join(value))

















