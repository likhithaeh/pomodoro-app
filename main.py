from tkinter import *
from tkinter import messagebox
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#FFE6E1"
RED = "#FF3F33"
DARK_GREEN = "#075B5E"
GREEN = "#9FC87E"
MAGENTA = "#D2665A"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_button_clicked():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    title_label.config(text="Timer")
    check_mark_label.config(text="")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_button_clicked():
    global reps
    reps += 1
    if reps % 8==0:
        count_down(LONG_BREAK_MIN*60)
        messagebox.showinfo(title="Long break",message="Woohoo! You were productive for 2 hours straight!💪✨\nNow, you have 20 mins. Go outside,talk to humans(😉) and avoid using any devices🙃")
        title_label.config(text="Long Break",fg=RED)
    elif reps % 2==0:
        count_down(SHORT_BREAK_MIN*60)
        messagebox.showinfo(title = "Short Break", message = "Well done!👏 You get 5 mins for a break.\nTake a walk and drink water\nAnd make sure you come back!😜")
        title_label.config(text="Short Break", fg=DARK_GREEN)
    else:
        count_down(WORK_MIN*60)
        title_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minute = count//60
    second = count%60
    if second < 10:
        second = f"0{second}"
    if minute < 10:
        minute = f"0{minute}"
    canvas.itemconfig(timer_text, text = f"{minute}:{second}")
    if count > 0 :
        global timer
        timer=window.after(1000,count_down, count-1)
    if count==0:
        start_button_clicked()
        mark = ""
        for _ in range(reps//2):
            mark += "✅"
        check_mark_label.config(text=mark)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(bg = PINK,padx=150,pady=100)

title_label = Label(text="Timer", font=(FONT_NAME, 45, "bold"), fg=MAGENTA, bg=PINK)
title_label.grid(column=1, row=0)

check_mark_label = Label(fg=GREEN, font=(FONT_NAME, 15, "bold"), bg=PINK)
check_mark_label.grid(column=1, row=3)

canvas = Canvas(width = 200, height=224, bg = PINK,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image = tomato_img)
timer_text = canvas.create_text(100,130, text = "00:00", fill = "white", font = (FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)


start_button = Button(text="Start",command=start_button_clicked,highlightthickness = 0)
start_button.grid(column=0,row=2)

reset_button = Button(text = "Reset",command=reset_button_clicked,highlightthickness = 0)
reset_button.grid(column=2,row=2)

window.mainloop()
