# module trong python
import my_module
# dùng lệnh import
# để gọi module vừa tạo là file my_module.py
# để gọi hàm được tạo sẵn trong file my_module.py
lists = [1,2,3,4,5]
lists = my_module.maxer(lists) # Hàm maxer vừa tạo đc gọi
print('max :',lists)
# số lớn nhất trong lists được gọi vì dùng hàm max 

lists = [1,2,3,4,5]
lists = my_module.miner(lists) # Hàm miner vừa tạo đc gọi
print('min :',lists)
# số bé nhất trong lists được gọi vì dùng hàm min 

print('___________________________________________________')


lists = ['Tuong', 'Clearlove7']
lists = my_module.maxer(lists) # Hàm maxer vừa tạo đc gọi
print(lists)

my_module.namit('Tuong')
# tuong được gán vào với phần tử trong hàm namit được truyền vào name

