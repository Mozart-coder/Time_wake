from tkinter import *
import datetime as dt
import matplotlib.pyplot as plt
import random


class PageUp:
    def __init__(self, window):

        self.window = window
        window.iconbitmap('C:/Users/acer/Documents/Historical_icon-icons.com_54175.ico')
        window.title("findwake")
        window.minsize(400,400)

        self.list_height = []
        self.list_count = []

        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var1_1 = IntVar()
        self.var2_1 = IntVar()

        self.padx = 5
        self.pady = 5

        self.label_sleep = Label(window,text = "sleep").grid(row =1,column = 2,padx = self.padx)

        self.label_hour = Label(window,text = "hour").grid(row = 2,column = 1,padx = self.padx)
        self.label_min = Label(window,text = "min").grid(row = 2,column = 3,padx =self.padx)

        vertical_hour = Scale(window,from_ = 0,to = 23,variable = self.var1)
        vertical_hour.grid(row = 3,column = 1,padx= self.padx, pady =self.pady)
        vertical_min = Scale(window,from_ = 0,to = 59,variable = self.var2)
        vertical_min.grid(row = 3,column = 3,padx = self.padx,pady = self.pady)

        label_wakeup = Label(window,text= "wake up").grid(row = 4,column = 2)

        vertical_hour2 = Scale(window,from_ = 0,to = 23,variable = self.var1_1)
        vertical_hour2.grid(row = 5,column = 1,padx = self.padx,pady= self.pady)
        vertical_min2 = Scale(window,from_ = 0,to = 59,variable = self.var2_1)
        vertical_min2.grid(row = 5,column = 3,padx = self.padx,pady = self.pady)

        button_create = Button(window,text = "create",command = self.cal)
        button_create.grid(row = 6,column = 1,padx= self.padx,pady = self.pady)
        button_createnow = Button(window,text = "create now",command = self.calnow)
        button_createnow.grid(row = 6,column = 3,padx=self.padx,pady =self.pady)
        button_graph =  Button(window,text = "see detail",command = self.makegraph)
        button_graph.grid(row = 7,column = 2,padx =self.padx,pady= self.pady)
        Button_save = Button(window,text = 'save',command = self.backup)
        Button_save.grid(row = 8,column = 2,padx =self.padx,pady =self.pady)

        self.label_output = Label(window)
        self.label_output.grid(row = 9,column = 2,pady =self.pady)



    def cal(self):
        hourza = self.var1.get()
        minza = self.var2.get()

        rd = random.randint(30,40)
        time = dt.timedelta(hours = hourza,minutes = minza)
        timefix = dt.timedelta(hours = 1,minutes=  rd)
        output = ''
        for i in range(1,11):
            time += timefix
            output += str(time) + "\n"
        self.label_output.configure(text = output)

    def calnow(self):
        now = dt.datetime.now()
        hourza = now.strftime("%H")
        minza = now.strftime("%M")
        #print(hourza,minza)
        rd = random.randint(30,40)
        time_now = dt.timedelta(hours = int(hourza),minutes=int(minza))
        timefix = dt.timedelta(hours = 1,minutes=  rd)
        output = ''
        for i in range(1,11):
            time_now += timefix
            output += str(time_now) + "\n"
        self.label_output.configure(text = output)

    def backup(self):
        hour_sleep = self.var1.get()
        min_sleep = self.var2.get()
        hour_wakeup = self.var1_1.get()
        min_wakeup = self.var2_1.get()

        time_sleep = dt.timedelta(hours = hour_sleep,minutes = min_sleep)
        time_wakeup = dt.timedelta(hours = hour_wakeup,minutes=  min_wakeup)
        
        result_time = (time_wakeup - time_sleep).seconds

        file = open("time.txt","a")
        file.write(str(result_time) + "\n")

    def makegraph(self):
        filetxt = open("time.txt","r")
        count = 0
        for line in filetxt:
            self.list_height.append(int(str(line)[:-1]))
            count += 1

        for i in range(1,count+1):
            self.list_count.append(i)

        plt.bar(self.list_count,self.list_height, width = 0.8, color = ['green'])
        plt.xlabel("time sleep")
        plt.ylabel("second")
        plt.title("time sleep")
        plt.show()

def main():
    window = Tk()
    app = PageUp(window)
    window.mainloop()

if __name__ == "__main__":
    main()
