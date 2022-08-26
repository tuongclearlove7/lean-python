 # đệ quy

def sum(list):
    if not list:
        return 0 # return  bắt đầu từ 0 
    else:
        return list[0] + sum(list[1:])

print(sum([1]))
# call sum 1,2,3,4 (+1) 
# sum 2,3,4 (+2) 
# sum 3,4 (+3)
# sum 4 (+4) 
# (0)      
print(sum([1,2,3,4]))
print(sum([1,2,3,4,5]))
print("""           [1,2,3,4]            10 <________
#             /\                           |
#            /  \                          |
#         1 + [2,3,4]                      |
#             /\                    1 + (2+3+4+0)
#            /  \                          ^
#          2 + [3,4]                       |
#             /\                      2 + (3+4+0)
#            /  \                          ^
#           3 + [4]                        |
#             /\                       3 + (4+0)
#            /  \                          ^
#           4   [ ]                        | 
#                |                       4+(0)
#                0                         ^
#                |_________________________|      """)

print('_______________________________________________')
def cal_sum(lists):
    if not lists: return 0
    return call_sum(lists)
def call_sum(lists):
    return lists[0] + cal_sum(lists[2:])
print(cal_sum([1,2,3,4,5,6,7]))
# chạy tương tự


def sum(list):
    return 0 if not list else list[0]+sum(list[1:])
print(sum([1,2,3]))
# chạy tương tự

def cal_sum(lists):
    index, *r = lists
    return index if not r else index + cal_sum(r)
print(cal_sum([1,2,3]))
# chạy tương tự

#def cal_sum(lists):
 #   return list[0] if len(lists) == 1 else lists[0] + cal_sum(lists[1:])
#print(cal_sum([])) eror

def sum(list):
    return 0 if not list else list[0]+sum(list[1:])
print(sum([]))# không có phần tử nào trong list 
#nên trả ra  = 0


def cal_sum(lists):
    index, *r = lists
    return index if not r else index + cal_sum(r)
print(cal_sum([[1,2], [3,4], [5,6]]))
# liên kết các phần tử trong các list thành 1 list

def cal_sum(lists):
    index, *r = lists
    return index if not r else index + cal_sum(r)
print(cal_sum(['t','u','o','n','g']))
# liên kết các phần tử trong các list thành 1 list




