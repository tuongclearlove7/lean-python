import subprocess

result = subprocess.check_output('curl -F "Sobaodanh=02000149" diemthi.hcm.edu.vn/Home/Show')

print(result)

