from Shay.File import File
from Shay.HardDisk_1 import HardDisk_1

file1=File("aa", 30)
file2=File("bb", 20)
file3=File("gg",5)

print(file3>file2)

hd = HardDisk_1()
hd.add_file(file1)
hd.add_file(file2)
hd.add_file(file3)
print(hd)

hd.del_file("gg")
print(hd)

