from random import randint
class Lotto:
    def __init__(self):
        self.num_list=[]
        # self.max_win
        self.low=1
        self.up=45
        self.random_num()
        self.get_max_win()

    def random_num(self):
        for i in range(6):
            self.num_list.append(randint(self.low,self.up))

    def get_max_win(self):
        self.max_win=int(input("input max win: "))

    def show_num(self):
        print(self.num_list)

    def check_num(self,num):
        if num in self.num_list:
            return True
        else:
            return False

    def win(self,count):
        if count<=0:
            sum=0
        elif 2<=count<=5:
            sum=count*self.max_win/6
            sum=int(sum)
        else:
            sum=self.max_win
        return sum





