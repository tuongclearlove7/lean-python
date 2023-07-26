import subprocess

result = subprocess.check_output('curl -F "Sobaodanh=40003588" diemthi.hcm.edu.vn/Home/Show')

print(result)
