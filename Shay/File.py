class File:
    def __init__(self, name,size): #תפעל ראשונה בעת הפעלת הקוד כדי לקבוע את הבסיס
        self.name=name
        self.size=size

    def __str__(self):  #תפקדיה להחזיר מחרוזת עם פרטי ההדפסה של האובייקט
        return f"File name: {self.name}, size: {self.size}"

    def __repr__(self): #כמו STR אך היא יודעת להדפיס ליסטים
        return f"File name: {self.name}, size: {self.size}"

    def __eq__(self, other):#השוואה של שם הקובץ
        if self.name==other.name:
            return True
        else:
            return False

    def __gt__(self, other):  #השוואת גדלים ולא כתובות
        if self.size>other.size:
            return True
        else:
            return False