from tkinter import*
import calendar


def ShowCal():
    new_gui = Tk()
    new_gui.config(background="white")
    new_gui.geometry("600x600")
    new_gui.title("Calendar")
    #fetch_year = int(year_field.get())
    fetch_year = year_field.get()

    cal_content = calendar.calendar(fetch_year)
    
    cal_year = Label(new_gui,text=cal_content,font="Consolas 10 bold")
    cal_year.grid(row=3,column=1,padx=15)


    new_gui.mainloop()


    



#Driver code
if __name__ == '__main__':
    window = Tk()
    window.geometry("300x300")

    cal = Label(window,text="Calendar",bg="grey")
    cal.grid(row=1,column=1)

    year = Label(window,text="Enter Year" , bg="Green")
    year.grid(row=2,column=1)

    year_field = Entry(window)
    year_field.grid(row=3,column=1)


    show = Button(window,text="Show",bd=5,bg="red",command=ShowCal)
    show.grid(row=5,column=1)

    exit = Button(window,text="Exit",bd=5,bg="red")
    exit.grid(row=7,column=1)


    window.mainloop()