lists = [1,2,3,4,5]
print(lists[1])
# bỏ đi phần tử cần lấy trong mảng và xác định số đằng sau

# slicing cắt mảng
# [star : end : step]
my_list2 = [1,2,"python", False]
# cắt đi phần tử 1 
print(my_list2[1:])
# lấy list[1]
print(my_list2[:1])
# lấy phần tử cuối cùng sử dụng số âm
print(my_list2[-2])
# lấy toàn bộ list
print(my_list2[::])
# lấy số 1 và "python" step 2
print(my_list2[::2])
#lấy toàn bộ list và phần tử bị đảo ngược lại
print(my_list2[::-1])

#list có thể chứa này kiểu dữ liệu
list1 = [1,"python", False, None]
print(list1)

# tạo list rỗng
list2 = list()
print(list2)

my_list = [1,2,2,2,2,"python", True, False]
# truy xuất phần tử nằm sau list [2]
print(my_list[2])
# dùng hàm len để xác định có bao nhiêu phần tử trong list
print(len(my_list))
#dùng hàm index để biết đc vị trí của phần tử phần tìm
# index đếm từ 0
print(my_list.index(False))
# dùng hàm cout để biết được có bao nhiêu phần tử giống
# nhau nằm trong list
print(my_list.count(2))
# dùng for i in my_list:
# để lấy toàn bộ giá trị nằm trong list
for i in my_list:
    print(i)

language = ["python", "javascript", "css", "c++"]
print(language)
# dùng thêm biến index
# dùng hàm enumerate để xuất toàn bộ giá trị trong list
# biến index dùng để đếm giá trị nằm trong list
for index, language in enumerate(language):
    print(f"language : {index}: {language}")


language2 = ["python", "javascript", "css", "c++"]
# để đếm các phần tử trong list từ 1 ta cho vào star = 1
for index, language2 in enumerate(language2, start=1):
    print(f"language : {index}: {language2}")

# hàm del xóa phần tử nằm trong [index2] chạy  từ 3
index2 = [1, 2, "javascript", True]
del index2[3]
print(index2)






















