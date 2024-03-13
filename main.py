import datetime
from tkinter import Tk, Canvas, PhotoImage, Label, Button

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"

RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✓"
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    checkmark_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps

    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    # count_down(work_seconds)
    if reps % 8 == 0:
        count_down(long_break_seconds)
        timer_label.config(text="Work", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_seconds)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_seconds)
        timer_label.config(text="Work", fg=GREEN)
    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(counter):
    global reps
    time_text = datetime.timedelta(seconds=counter)
    canvas.itemconfig(timer_text, text=time_text)
    if counter > 0:
        global timer
        timer = window.after(1000, count_down, counter - 1)
    elif reps <= 8:
        start_timer()
        marks = ""
        for _ in range(reps // 2):
            marks += CHECKMARK
        checkmark_label.config(text=marks)
    else:
        reps = 0


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(width=220, height=240, padx=100, pady=100, bg=YELLOW)
# count_down(5)
# window.after(1000, count_down, 5)

photo_image = PhotoImage(file="tomato.png")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightbackground=YELLOW)
canvas.create_image(102, 112, image=photo_image)
timer_text = canvas.create_text(104, 130, text="00:00", fill="white", font=(FONT_NAME, 22, "bold"))
canvas.grid(row=1, column=1)

# ---------------------------- LABELS ------------------------------- #
timer_label = Label(text="Timer")
timer_label.config(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
timer_label.grid(row=0, column=1)

checkmark_label = Label(text=CHECKMARK)
checkmark_label.config(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
checkmark_label.grid(row=3, column=1)

# ---------------------------- BUTTONS ------------------------------- #
start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()
