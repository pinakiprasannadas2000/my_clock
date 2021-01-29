from tkinter import *
from tkinter import ttk, messagebox
from datetime import date
import time

# ---------------------------------------------global variables---------------------------------------------
countdown_timer = None
seconds = 0
prev_second = 0
lap_number = 1
work_count = 1
work_index = 0
work_list = []

# ---------------------------------------------setting up the window---------------------------------------------
root = Tk()
root.title("I AM SUPER CLOCK")
root.geometry("1200x650+0+0")
root.config(bg="white")
root.resizable(False, False)


# ---------------------------------------------all functions---------------------------------------------
def clear():
    clear_frame2()

    # title
    title2 = Label(frame2, font=("times new roman", 25, "bold"), bg="light grey", fg="black")
    title2.pack(side=TOP, fill=X)

    digital_clock.config(state=NORMAL)
    default_timer.config(state=NORMAL)
    stopwatch.config(state=NORMAL)
    costume_timer.config(state=NORMAL)
    world_clock.config(state=NORMAL)


def clear_frame2():
    for widget in frame2.winfo_children():
        widget.destroy()
    frame2.pack_forget()


def default_timer():
    digital_clock.config(state=DISABLED)
    stopwatch.config(state=DISABLED)
    costume_timer.config(state=DISABLED)
    world_clock.config(state=DISABLED)

    clear_frame2()

    # title
    title2 = Label(frame2, text="DEFAULT TIMER", font=("times new roman", 25, "bold"), bg="light grey", fg="black")
    title2.pack(side=TOP, fill=X)

    clear_button = Button(title2, text="EXIT", font=("times new roman", 25, "bold"), bg="red", fg="white",
                          activebackground="red", activeforeground="white", command=clear)
    clear_button.pack(side=RIGHT)

    # hour combobox
    hour_label = Label(frame2, text="HOUR", font=("times new roman", 15, "bold"), bg="light yellow", fg="black")
    hour_label.place(x=262, y=70)

    hour_values = []
    for i in range(100):
        if len(str(i)) == 1:
            i = "0" + str(i)
        hour_values.append(str(i))

    hour_variable = StringVar()
    hour_combobox = ttk.Combobox(frame2, font=("times new roman", 20, "bold"), textvariable=hour_variable,
                                 values=hour_values, state="readonly")
    hour_combobox.place(x=245, y=100, width=100)
    hour_variable.set("00")

    # minute combobox
    minute_label = Label(frame2, text="MINUTE", font=("times new roman", 15, "bold"), bg="light yellow", fg="black")
    minute_label.place(x=372, y=70)

    minute_values = []
    for i in range(60):
        if len(str(i)) == 1:
            i = "0" + str(i)
        minute_values.append(str(i))

    minute_variable = StringVar()
    minute_combobox = ttk.Combobox(frame2, font=("times new roman", 20, "bold"), textvariable=minute_variable,
                                   values=minute_values, state="readonly")
    minute_combobox.place(x=365, y=100, width=100)
    minute_variable.set("00")

    # second combobox
    second_label = Label(frame2, text="SECOND", font=("times new roman", 15, "bold"), bg="light yellow", fg="black")
    second_label.place(x=492, y=70)

    second_values = []
    for i in range(60):
        if len(str(i)) == 1:
            i = "0" + str(i)
        second_values.append(str(i))

    second_variable = StringVar()
    second_combobox = ttk.Combobox(frame2, font=("times new roman", 20, "bold"), textvariable=second_variable,
                                   values=second_values, state="readonly")
    second_combobox.place(x=485, y=100, width=100)
    second_variable.set("00")

    # hour countdown
    hour_label = Label(frame2, text="00", font=("times new roman", 25, "bold"), bg="#087587", fg="white")
    hour_label.place(x=245, y=315, width=100, height=100)

    hour_label2 = Label(frame2, text="HOUR", font=("times new roman", 15, "bold"), bg="#087587", fg="white")
    hour_label2.place(x=245, y=420, width=100, height=50)

    # minute countdown
    minute_label = Label(frame2, text="00", font=("times new roman", 25, "bold"), bg="#008EA4", fg="white")
    minute_label.place(x=365, y=315, width=100, height=100)

    minute_label2 = Label(frame2, text="MINUTE", font=("times new roman", 15, "bold"), bg="#008EA4", fg="white")
    minute_label2.place(x=365, y=420, width=100, height=50)

    # second countdown
    second_label = Label(frame2, text="00", font=("times new roman", 25, "bold"), bg="#DF002A", fg="white")
    second_label.place(x=485, y=315, width=100, height=100)

    second_label2 = Label(frame2, text="SECOND", font=("times new roman", 15, "bold"), bg="#DF002A", fg="white")
    second_label2.place(x=485, y=420, width=100, height=50)

    # buttons
    def start():
        start_button.config(state=DISABLED)

        hour = int(hour_variable.get())
        minute = int(minute_variable.get())
        second = int(second_variable.get())

        if hour == 0 and minute == 0 and second == 0:
            messagebox.showinfo(title="Costume Timer", message="Please select some seconds to start the timer.")
            start_button.config(state=NORMAL)
            return

        total_seconds = int((hour * 3600) + (minute * 60) + second)
        countdown(total_seconds)

    def countdown(total_seconds):
        global countdown_timer
        hour = int(total_seconds / 3600)
        minute = int((total_seconds % 3600) / 60)
        second = int((total_seconds % 3600) % 60)

        if len(str(hour)) == 1:
            hour = "0" + str(hour)
        if len(str(minute)) == 1:
            minute = "0" + str(minute)
        if len(str(second)) == 1:
            second = "0" + str(second)

        hour_label.config(text=f"{hour}")
        minute_label.config(text=f"{minute}")
        second_label.config(text=f"{second}")

        if total_seconds > 0:
            countdown_timer = frame2.after(1000, countdown, total_seconds - 1)
        else:
            frame2.after_cancel(countdown_timer)
            messagebox.showinfo(title="Default Timer", message=f"{hour} : {minute} : {second} is up!!")
            hour_variable.set("00")
            minute_variable.set("00")
            second_variable.set("00")
            start_button.config(state=NORMAL)

    def clear_in_default_timer():
        frame2.after_cancel(countdown_timer)
        hour_variable.set("00")
        minute_variable.set("00")
        second_variable.set("00")
        hour_label.config(text="00")
        minute_label.config(text="00")
        second_label.config(text="00")
        start_button.config(state=NORMAL)

    start_button = Button(frame2, text="START", font=("times new roman", 15, "bold"), bg="green", fg="white",
                          activebackground="green", activeforeground="white", command=start)
    start_button.place(x=620, y=315, width=150)

    pause_button = Button(frame2, text="PAUSE", font=("times new roman", 15, "bold"), bg="orange", fg="white",
                          activebackground="orange", activeforeground="white")
    pause_button.place(x=620, y=372.5, width=150)

    clear_button = Button(frame2, text="CLEAR", font=("times new roman", 15, "bold"), bg="red", fg="white",
                          activebackground="red", activeforeground="white", command=clear_in_default_timer)
    clear_button.place(x=620, y=430, width=150)


def costume_timer():
    global work_list

    digital_clock.config(state=DISABLED)
    stopwatch.config(state=DISABLED)
    default_timer.config(state=DISABLED)
    world_clock.config(state=DISABLED)

    clear_frame2()

    # title
    title2 = Label(frame2, text="COSTUME TIMER", font=("times new roman", 25, "bold"), bg="light grey", fg="black")
    title2.pack(side=TOP, fill=X)

    clear_button = Button(title2, text="EXIT", font=("times new roman", 25, "bold"), bg="red", fg="white",
                          activebackground="red", activeforeground="white", command=clear)
    clear_button.pack(side=RIGHT)

    # text area
    work_frame_area = Frame(frame2, bg="white", bd=2, relief=RIDGE)
    work_frame_area.place(x=10, y=80, width=430, height=420)

    work_text_area = Text(work_frame_area, bg="white", fg="black", font=("times new roman", 15, "bold"), state=DISABLED)
    work_text_area.pack(fill=BOTH, expand=1)

    # work entry
    def add_work():
        global work_count
        work_text_area.config(state=NORMAL)
        work_text_area.delete("1.0", END)

        work_name = work_entry.get()

        if work_name == "":
            messagebox.showerror(title="Costume Timer", message="Please enter the work name.")
            return

        hour = int(hour_variable.get())
        minute = int(minute_variable.get())
        second = int(second_variable.get())

        if hour == 0 and minute == 0 and second == 0:
            messagebox.showerror(title="Costume Timer", message="Please select some seconds to start the timer.")
            start_button.config(state=NORMAL)
            return

        if len(str(hour)) == 1:
            hour = "0" + str(hour)
        if len(str(minute)) == 1:
            minute = "0" + str(minute)
        if len(str(second)) == 1:
            second = "0" + str(second)

        work_dict = {
            "work": work_name,
            "time": {
                "hour": hour,
                "minute": minute,
                "second": second
            }
        }

        work_list.append(work_dict)
        for i in work_list:
            work_text_area.config(state=NORMAL)
            work_text_area.insert(END, f"{work_count}. {i['work']} -- {i['time']['hour']} : {i['time']['minute']} : "
                                       f"{i['time']['second']}\n")
            work_text_area.config(state=DISABLED)
        work_entry.delete(0, END)

        hour_variable.set("00")
        minute_variable.set("00")
        second_variable.set("00")
        start_button.config(state=NORMAL)

    work_label = Label(frame2, text="Work name: ", font=("times new roman", 15, "bold"), bg="light yellow", fg="black")
    work_label.place(x=450, y=70)
    work_entry = Entry(frame2, font=("times new roman", 15, "bold"), bg="light yellow", fg="black")
    work_entry.place(x=570, y=70, width=180)

    add_button = Button(frame2, text="ADD", font=("times new roman", 15, "bold"), bg="orange", fg="white",
                        activebackground="orange", activeforeground="white", command=add_work)
    add_button.place(x=760, y=70, width=60, height=27)

    # hour combobox
    hour_label = Label(frame2, text="HOUR", font=("times new roman", 15, "bold"), bg="light yellow", fg="black")
    hour_label.place(x=467, y=100)

    hour_values = []
    for i in range(100):
        if len(str(i)) == 1:
            i = "0" + str(i)
        hour_values.append(str(i))

    hour_variable = StringVar()
    hour_combobox = ttk.Combobox(frame2, font=("times new roman", 20, "bold"), textvariable=hour_variable,
                                 values=hour_values, state="readonly")
    hour_combobox.place(x=450, y=130, width=100)
    hour_variable.set("00")

    # minute combobox
    minute_label = Label(frame2, text="MINUTE", font=("times new roman", 15, "bold"), bg="light yellow", fg="black")
    minute_label.place(x=577, y=100)

    minute_values = []
    for i in range(60):
        if len(str(i)) == 1:
            i = "0" + str(i)
        minute_values.append(str(i))

    minute_variable = StringVar()
    minute_combobox = ttk.Combobox(frame2, font=("times new roman", 20, "bold"), textvariable=minute_variable,
                                   values=minute_values, state="readonly")
    minute_combobox.place(x=570, y=130, width=100)
    minute_variable.set("00")

    # second combobox
    second_label = Label(frame2, text="SECOND", font=("times new roman", 15, "bold"), bg="light yellow", fg="black")
    second_label.place(x=697, y=100)

    second_values = []
    for i in range(60):
        if len(str(i)) == 1:
            i = "0" + str(i)
        second_values.append(str(i))

    second_variable = StringVar()
    second_combobox = ttk.Combobox(frame2, font=("times new roman", 20, "bold"), textvariable=second_variable,
                                   values=second_values, state="readonly")
    second_combobox.place(x=690, y=130, width=100)
    second_variable.set("00")

    # hour countdown
    hour_label = Label(frame2, text="00", font=("times new roman", 25, "bold"), bg="#087587", fg="white")
    hour_label.place(x=450, y=345, width=100, height=70)

    hour_label2 = Label(frame2, text="HOUR", font=("times new roman", 15, "bold"), bg="#087587", fg="white")
    hour_label2.place(x=450, y=420, width=100, height=30)

    # minute countdown
    minute_label = Label(frame2, text="00", font=("times new roman", 25, "bold"), bg="#008EA4", fg="white")
    minute_label.place(x=570, y=345, width=100, height=70)

    minute_label2 = Label(frame2, text="MINUTE", font=("times new roman", 15, "bold"), bg="#008EA4", fg="white")
    minute_label2.place(x=570, y=420, width=100, height=30)

    # second countdown
    second_label = Label(frame2, text="00", font=("times new roman", 25, "bold"), bg="#DF002A", fg="white")
    second_label.place(x=690, y=345, width=100, height=70)

    second_label2 = Label(frame2, text="SECOND", font=("times new roman", 15, "bold"), bg="#DF002A", fg="white")
    second_label2.place(x=690, y=420, width=100, height=30)

    # buttons
    def start():
        hour_variable.set("00")
        minute_variable.set("00")
        second_variable.set("00")

        global work_index
        if work_index >= len(work_list):
            return

        start_button.config(state=DISABLED)
        clear_button.config(state=NORMAL)

        current_work = work_list[work_index]

        hour = int(current_work["time"]["hour"])
        minute = int(current_work["time"]["minute"])
        second = int(current_work["time"]["second"])

        total_seconds = int((hour * 3600) + (minute * 60) + second)
        countdown(total_seconds)

        work_index = work_index + 1

    def countdown(total_seconds):
        global countdown_timer
        hour = int(total_seconds / 3600)
        minute = int((total_seconds % 3600) / 60)
        second = int((total_seconds % 3600) % 60)

        if len(str(hour)) == 1:
            hour = "0" + str(hour)
        if len(str(minute)) == 1:
            minute = "0" + str(minute)
        if len(str(second)) == 1:
            second = "0" + str(second)

        hour_label.config(text=f"{hour}")
        minute_label.config(text=f"{minute}")
        second_label.config(text=f"{second}")

        if total_seconds > 0:
            countdown_timer = frame2.after(1000, countdown, total_seconds - 1)
        else:
            frame2.after_cancel(countdown_timer)
            messagebox.showinfo(title="Costume Timer", message="Time is up!!")
            start()
            hour_variable.set("00")
            minute_variable.set("00")
            second_variable.set("00")
            start_button.config(state=NORMAL)

    def clear_in_costume_timer():
        global work_list, work_index

        frame2.after_cancel(countdown_timer)
        hour_variable.set("00")
        minute_variable.set("00")
        second_variable.set("00")
        hour_label.config(text="00")
        minute_label.config(text="00")
        second_label.config(text="00")
        work_text_area.config(state=NORMAL)
        work_text_area.delete("1.0", END)
        work_text_area.config(state=DISABLED)
        start_button.config(state=DISABLED)

        work_list = []
        work_index = 0

    start_button = Button(frame2, text="START", font=("times new roman", 15, "bold"), bg="green", fg="white",
                          activebackground="green", activeforeground="white", command=start, state=DISABLED)
    start_button.place(x=450, y=460, width=100)

    pause_button = Button(frame2, text="PAUSE", font=("times new roman", 15, "bold"), bg="orange", fg="white",
                          activebackground="orange", activeforeground="white", state=DISABLED)
    pause_button.place(x=570, y=460, width=100)

    clear_button = Button(frame2, text="CLEAR", font=("times new roman", 15, "bold"), bg="red", fg="white",
                          activebackground="red", activeforeground="white", command=clear_in_costume_timer,
                          state=DISABLED)
    clear_button.place(x=690, y=460, width=100)


def world_clock():
    digital_clock.config(state=DISABLED)
    stopwatch.config(state=DISABLED)
    costume_timer.config(state=DISABLED)
    default_timer.config(state=DISABLED)

    clear_frame2()

    # title
    title2 = Label(frame2, text="WORLD CLOCK", font=("times new roman", 25, "bold"), bg="light grey", fg="black")
    title2.pack(side=TOP, fill=X)

    clear_button = Button(title2, text="EXIT", font=("times new roman", 25, "bold"), bg="red", fg="white",
                          activebackground="red", activeforeground="white", command=clear)
    clear_button.pack(side=RIGHT)


def stopwatch():
    digital_clock.config(state=DISABLED)
    default_timer.config(state=DISABLED)
    costume_timer.config(state=DISABLED)
    world_clock.config(state=DISABLED)

    clear_frame2()

    # title
    title2 = Label(frame2, text="STOPWATCH", font=("times new roman", 25, "bold"), bg="light grey", fg="black")
    title2.pack(side=TOP, fill=X)

    clear_button = Button(title2, text="EXIT", font=("times new roman", 25, "bold"), bg="red", fg="white",
                          activebackground="red", activeforeground="white", command=clear)
    clear_button.pack(side=RIGHT)

    laps_text_frame = Frame(frame2, bd=2, relief=RIDGE, bg="white")
    laps_text_frame.place(x=10, y=80, width=435, height=425)

    scroll_y = Scrollbar(laps_text_frame, orient=VERTICAL)
    scroll_y.pack(side=RIGHT, fill=Y)

    laps_text = Text(laps_text_frame, font=("times new roman", 15), bg="light blue", yscrollcommand=scroll_y.set)
    laps_text.pack(fill=BOTH, expand=1)
    scroll_y.config(command=laps_text.yview)

    # salary_frame2 = Frame(salary_frame, bd=2, relief=RIDGE, bg="white")
    # salary_frame2.place(x=0, y=37, relwidth=1, height=270)
    #
    # scroll_y = Scrollbar(salary_frame2, orient=VERTICAL)
    # scroll_y.pack(side=RIGHT, fill=Y)
    #
    # txt_salary_receipt = Text(salary_frame2, font=("times new roman", 15), bg="light yellow",
    #                           yscrollcommand=scroll_y.set)
    # txt_salary_receipt.pack(fill=BOTH, expand=1)
    # scroll_y.config(command=txt_salary_receipt.yview)

    # hour
    hour_label = Label(frame2, text="00", font=("times new roman", 25, "bold"), bg="#087587", fg="white")
    hour_label.place(x=460, y=100, width=100, height=100)

    hour_label2 = Label(frame2, text="HOUR", font=("times new roman", 15, "bold"), bg="#087587", fg="white")
    hour_label2.place(x=460, y=205, width=100, height=50)

    # minute
    minute_label = Label(frame2, text="00", font=("times new roman", 25, "bold"), bg="#008EA4", fg="white")
    minute_label.place(x=580, y=100, width=100, height=100)

    minute_label2 = Label(frame2, text="MINUTE", font=("times new roman", 15, "bold"), bg="#008EA4", fg="white")
    minute_label2.place(x=580, y=205, width=100, height=50)

    # second
    second_label = Label(frame2, text="00", font=("times new roman", 25, "bold"), bg="#DF002A", fg="white")
    second_label.place(x=700, y=100, width=100, height=100)

    second_label2 = Label(frame2, text="SECOND", font=("times new roman", 15, "bold"), bg="#DF002A", fg="white")
    second_label2.place(x=700, y=205, width=100, height=50)

    # buttons
    def start():
        start_button.config(state=DISABLED)
        pause_button.config(state=NORMAL)
        reset_button.config(state=NORMAL)
        lap_button.config(state=NORMAL)

        new_seconds = 0
        go_on_second(new_seconds)

    def go_on_second(new_seconds):
        global seconds, countdown_timer
        seconds = new_seconds
        hour = int(new_seconds / 3600)
        minute = int((new_seconds % 3600) / 60)
        second = int((new_seconds % 3600) % 60)

        if len(str(hour)) == 1:
            hour = "0" + str(hour)
        if len(str(minute)) == 1:
            minute = "0" + str(minute)
        if len(str(second)) == 1:
            second = "0" + str(second)

        hour_label.config(text=f"{hour}")
        minute_label.config(text=f"{minute}")
        second_label.config(text=f"{second}")

        if int(hour) < 100:
            countdown_timer = frame2.after(1000, go_on_second, new_seconds + 1)

    def reset():
        frame2.after_cancel(countdown_timer)
        start_button.config(state=NORMAL)
        pause_button.config(state=DISABLED)
        reset_button.config(state=DISABLED)
        lap_button.config(state=DISABLED)
        hour_label.config(text="00")
        minute_label.config(text="00")
        second_label.config(text="00")

        laps_text.config(state=NORMAL)
        laps_text.delete("1.0", END)
        laps_text.config(state=DISABLED)

    def lap():
        global lap_number, prev_second
        hour = int(seconds / 3600)
        minute = int((seconds % 3600) / 60)
        second = int((seconds % 3600) % 60)

        if len(str(hour)) == 1:
            hour = "0" + str(hour)
        if len(str(minute)) == 1:
            minute = "0" + str(minute)
        if len(str(second)) == 1:
            second = "0" + str(second)

        difference_in_seconds = seconds - prev_second
        d_hour = int(difference_in_seconds / 3600)
        d_minute = int((difference_in_seconds % 3600) / 60)
        d_second = int((difference_in_seconds % 3600) % 60)
        if len(str(d_hour)) == 1:
            d_hour = "0" + str(d_hour)
        if len(str(d_minute)) == 1:
            d_minute = "0" + str(d_minute)
        if len(str(d_second)) == 1:
            d_second = "0" + str(d_second)

        laps_text.config(state=NORMAL)
        laps_text.insert(END, f"{lap_number} -- {hour} : {minute} : {second} -- {d_hour} : {d_minute} : {d_second}\n")
        laps_text.config(state=DISABLED)

        lap_number = lap_number + 1
        prev_second = seconds

    start_button = Button(frame2, text="START", font=("times new roman", 15, "bold"), bg="green", fg="white",
                          activebackground="green", activeforeground="white", command=start)
    start_button.place(x=580, y=300, width=100)

    pause_button = Button(frame2, text="PAUSE", font=("times new roman", 15, "bold"), bg="orange", fg="white",
                          activebackground="orange", activeforeground="white", state=DISABLED)
    pause_button.place(x=460, y=350, width=100)

    reset_button = Button(frame2, text="RESET", font=("times new roman", 15, "bold"), bg="black", fg="white",
                          activebackground="black", activeforeground="white", state=DISABLED, command=reset)
    reset_button.place(x=580, y=350, width=100)

    lap_button = Button(frame2, text="LAP", font=("times new roman", 15, "bold"), bg="red", fg="white",
                        activebackground="red", activeforeground="white", state=DISABLED, command=lap)
    lap_button.place(x=700, y=350, width=100)


def digital_clock():
    default_timer.config(state=DISABLED)
    stopwatch.config(state=DISABLED)
    costume_timer.config(state=DISABLED)
    world_clock.config(state=DISABLED)

    clear_frame2()

    # title
    title2 = Label(frame2, text="DIGITAL CLOCK", font=("times new roman", 25, "bold"), bg="light grey", fg="black")
    title2.pack(side=TOP, fill=X)

    clear_button = Button(title2, text="EXIT", font=("times new roman", 25, "bold"), bg="red", fg="white",
                          activebackground="red", activeforeground="white", command=clear)
    clear_button.pack(side=RIGHT)

    # hour
    hour_label = Label(frame2, text="12", font=("times new roman", 25, "bold"), bg="#087587", fg="white")
    hour_label.place(x=200, y=150, width=100, height=100)

    hour_label2 = Label(frame2, text="HOUR", font=("times new roman", 15, "bold"), bg="#087587", fg="white")
    hour_label2.place(x=200, y=255, width=100, height=50)

    # minute
    minute_label = Label(frame2, text="12", font=("times new roman", 25, "bold"), bg="#008EA4", fg="white")
    minute_label.place(x=310, y=150, width=100, height=100)

    minute_label2 = Label(frame2, text="MINUTE", font=("times new roman", 15, "bold"), bg="#008EA4", fg="white")
    minute_label2.place(x=310, y=255, width=100, height=50)

    # second
    second_label = Label(frame2, text="12", font=("times new roman", 25, "bold"), bg="#DF002A", fg="white")
    second_label.place(x=420, y=150, width=100, height=100)

    second_label2 = Label(frame2, text="SECOND", font=("times new roman", 15, "bold"), bg="#DF002A", fg="white")
    second_label2.place(x=420, y=255, width=100, height=50)

    # noon
    noon_label = Label(frame2, text="AM", font=("times new roman", 25, "bold"), bg="#DF002A", fg="white")
    noon_label.place(x=530, y=150, width=100, height=100)

    noon_label2 = Label(frame2, text="NOON", font=("times new roman", 15, "bold"), bg="#DF002A", fg="white")
    noon_label2.place(x=530, y=255, width=100, height=50)

    # clock function
    def clock():
        # getting current time
        hour = str(time.strftime("%H"))
        minute = str(time.strftime("%M"))
        second = str(time.strftime("%S"))

        # validating and configuring
        if int(hour) > 12 and int(minute) > 0:
            noon_label.config(text="PM")

        if int(hour) > 12:
            hour = str(int(hour) - 12)
            if len(hour) == 1:
                hour = "0" + hour

        hour_label.config(text=hour)
        minute_label.config(text=minute)
        second_label.config(text=second)

        # continuous running of clock function
        hour_label.after(ms=1000, func=clock)

    clock()


# ---------------------------------------------title---------------------------------------------
title = Label(root, text="Watashi wa sūpākurokkudesu", font=("times new roman", 35, "bold"), bg="#262626", fg="white")
title.pack(side=TOP, fill=X)

created_by = Label(root, text="by PINAKI PRASANNA DAS", font=("times new roman", 20, "bold"), bg="red", fg="white")
created_by.pack(side=BOTTOM)

# ---------------------------------------------date---------------------------------------------
today = date.today().strftime("%B %d, %Y")
date_label = Label(root, text=f"{today}", font=("times new roman", 20, "bold"), bg="white", fg="#262626")
date_label.place(x=70, y=90)

# ---------------------------------------------frame 1---------------------------------------------
frame1 = Frame(root, bd=3, relief=RIDGE, bg="light blue")
frame1.place(x=50, y=150, width=245, height=440)

# buttons
digital_clock = Button(frame1, text="Digital Clock", font=("times new roman", 18, "bold"), bg="orange", fg="white",
                       activebackground="orange", activeforeground="white", command=digital_clock)
digital_clock.place(x=20, y=30, width=200, height=50)

world_clock = Button(frame1, text="World Clock", font=("times new roman", 18, "bold"), bg="orange", fg="white",
                     activebackground="orange", activeforeground="white", command=world_clock)
world_clock.place(x=20, y=110, width=200, height=50)

stopwatch = Button(frame1, text="Stopwatch", font=("times new roman", 18, "bold"), bg="orange", fg="white",
                   activebackground="orange", activeforeground="white", command=stopwatch)
stopwatch.place(x=20, y=190, width=200, height=50)

costume_timer = Button(frame1, text="Costume Timer", font=("times new roman", 18, "bold"), bg="orange", fg="white",
                       activebackground="orange", activeforeground="white", command=costume_timer)
costume_timer.place(x=20, y=270, width=200, height=50)

default_timer = Button(frame1, text="Default Timer", font=("times new roman", 18, "bold"), bg="orange", fg="white",
                       activebackground="orange", activeforeground="white", command=default_timer)
default_timer.place(x=20, y=350, width=200, height=50)

# ---------------------------------------------frame 2---------------------------------------------
frame2 = Frame(root, bd=3, relief=RIDGE, bg="light yellow")
frame2.place(x=360, y=70, width=830, height=520)

root.mainloop()
