from Shay.File import File
class HardDisk_1:
    def __init__(self,size=100): #תפעל ראשונה ותגדיר את נתוני הדיסק הקשיח
        self.size=100
        self.used_space=0
        self.files=[]

    def free_space(self): #תחשב מקום פנוי בדיסק הקשיח
        return self.size-self.used_space

    def add_file(self,file):
        if self.free_space()<file.size:
            print("not enough space")
            return False
        if file in self.files:
            print("File already exist")
            return False
        self.files.append(file)
        self.used_space+=file.size
        return True

    def __str__(self): #כאשר יש פרינט הוא מדפיס את התכולה ולא את הכתובת
        return f"Hard disk: size {self.size}, used space: {self.used_space}\
, files list: {self.files}"

    # def __gt__(self, other):  #השוואת גדלים ולא כתובות
    #     if self.size>other.size:
    #         return True
    #     else:
    #         return False

    def del_file(self,file_name): #מוחק את הקובץ. לפני כן מחפש אותו בליסט
        file = File(file_name,0)
        if file in self.files:
            i = self.files.index(file)
            self.used_space-=self.files[i].size
            self.files.remove(self.files[i])
        else:
            print(f"file: {file_name} does not exist")

