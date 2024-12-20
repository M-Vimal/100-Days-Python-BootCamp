from tkinter import *


window = Tk()
window.title("Miles to Km")
window.geometry("600x600")
window.config(padx=200,pady=200)



def calculate_km():
    m = int(miles.get())
    ans = Label(window,text = round(m * 1.609344,2))
    ans.grid(column=2,row=2)


miles = Entry(window)
miles.grid(column=2,row=1)



miles_lable = Label(window,text="miles")
miles_lable.grid(column=3,row=1)



label = Label(window,text="is equal to")
label.grid(column=1,row=2)


label2 = Label(window,text="KM")
label2.grid(column=4,row=2)


btn = Button(window,text="calculate",command=calculate_km)
btn.grid(column=2,row=3)



window.mainloop()