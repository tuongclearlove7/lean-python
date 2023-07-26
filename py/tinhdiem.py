print("nhập điểm")
toan = float(input('toan : '))
van = float(input('van : '))
ly = float(input('ly : '))
hoa = float(input('hoa : '))
gdcd = float(input('GDCD : '))
anhvan = float(input('t.anh : '))
diemkk = float(input('diemkk : '))
diemut = float(input('diemvung : '))
tb = (toan+van+ly+hoa+gdcd+anhvan)/6+diemkk+diemut
dem = 0
if toan > tb: dem += 1
if van > tb: dem += 1
if ly > tb: dem += 1
if hoa > tb: dem += 1
if gdcd > tb: dem += 1
if anhvan > tb: dem += 1
print(f"điểm trung bình của bạn là : {tb:.2f}")






