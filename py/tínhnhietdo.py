print("nhập điểm trung bình của 8 môn: ")
toan = float(input())
van = float(input())
su = float(input())
dia = float(input())
ly = float(input())
hoa = float(input())
gdcd = float(input())
tin = float(input())
tb = (toan+van+su+dia+ly+hoa+gdcd+tin)/8
dem = 0
if toan > tb: dem += 1
if van > tb: dem += 1
if su > tb: dem += 1
if dia > tb: dem += 1
if ly > tb: dem += 1
if hoa > tb: dem += 1
if gdcd > tb: dem += 1
if tin > tb: dem += 1
print(f"điểm trung bình của 8 môn là : {tb:.2f}")
print("Số môn có điểm cao hơn1 trung bình là: ", dem)

