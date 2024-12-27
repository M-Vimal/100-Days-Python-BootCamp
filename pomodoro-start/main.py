from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


window = Tk()
window.geometry("600x600")
window.title("pomodoro")
window.config(pady=100, padx=70)




# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text = "00:00")
    timer_label.config(text="Timer")

    check_mark.config(text="")

    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps+=1

    if reps % 8 == 0:
        timer_label.config(text="LONG BREAK",fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        timer_label.config(text="SHORT BREAK",fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        timer_label.config(text="WORK",fg=GREEN)
        count_down(WORK_MIN * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    min = math.floor(count/60)
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"
    canvas.itemconfig(timer_text,text = f"{min}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        c_marks = ""
        session = math.floor(reps/2)
        for _ in range(session):
            c_marks += "✔"
            check_mark.config(text=c_marks)



        start_timer()
    

# ---------------------------- UI SETUP ------------------------------- #



timer_label = Label(fg=GREEN,font=(FONT_NAME, 30, "bold"))
timer_label.grid(column=2,row=1)


canvas = Canvas(height=300,width=300)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(150,150,image = tomato_img)
timer_text = canvas.create_text(150,150,text='00:00',fill='white',font=(FONT_NAME, 20, "bold"))
canvas.grid(column=2,row=2)

start_button = Button(text='Start',command=start_timer)
start_button.grid(column=0,row=3)

check_mark = Label()
check_mark.grid(column=2,row=3)

reset_button = Button(text='Reset',command=reset)
reset_button.grid(column=3,row=3)
window.mainloop()