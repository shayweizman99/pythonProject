# class HardDisk:
#
#     def __init__(self): #תפעל ראשונה ותגדיר את נתוני הדיסק הקשיח
#         self.size=100
#         self.used_space=0
#         self.num_files=0
#
#     def show_details(self): #מראה את פרטי הדיסק הקשיח
#         print(f"HardDisk size: {self.size}, used space {self.used_space}, number of files:{self.num_files}\
# , Free space: {self.free_space()}")
#
#     def free_space(self): #תחשב מקום פנוי בדיסק הקשיח
#         return self.size-self.used_space
#
#     def add_file(self,size,): #הוספת קובץ לדיסק קשיח
#         if size<=0:
#             return False , print("file with no size")
#         elif self.free_space()>=size:
#             self.used_space+=size
#             self.num_files+=1
#             return True
#         else:
#             return False, print("not enough space!")
#
#     def del_file(self, size): #מחיקת קובץ מהדיסק הקשיח
#         self.used_space-=size
#         self.num_files-=1
#         if self.used_space <0:
#             self.used_space =0
#         if self.num_files<0:
#             self.num.files=0




