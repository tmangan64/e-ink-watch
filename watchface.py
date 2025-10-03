import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Watch")
root.geometry("200x200")

canvas = tk.Canvas(root, width=200, height=200, highlightthickness=0)
canvas.pack()

center_x = 100
center_y = 100
radius = 100

# Draw white circle
canvas.create_oval(
    center_x - radius, center_y - radius,
    center_x + radius, center_y + radius,
    outline="white",
    fill="white",
    width=2
)

# Digital time text
time_text = canvas.create_text(center_x, center_y, text="", fill="black", font=("Consolas", 35))
ampm_text = canvas.create_text(center_x, center_y, text="", fill="black", font=("Consolas", 15))

# Arc for the second hand (progress bar)
# Initially invisible (0 degrees)
second_arc = canvas.create_arc(
    center_x - radius + 4, 
    center_y - radius + 4,
    center_x + radius - 4, 
    center_y + radius - 4,
    start=90, 
    extent=0,  # start at top, 0 extent
    style=tk.ARC, 
    width=4, 
    outline="black"
)

def update_time():
    # Get current time
    current_hour = int(strftime("%I"))  # 12-hour format
    current_minute = strftime("%M")
    current_second = int(strftime("%S"))
    am_pm = strftime("%p")

    # Update digital time
    time_str = f"{current_hour}:{current_minute}"
    canvas.itemconfig(time_text, text=time_str)

    # Position AM/PM
    if am_pm == "AM":
        canvas.itemconfig(ampm_text, text="AM")
        canvas.coords(ampm_text, center_x - 30, center_y + 35)
    else:
        canvas.itemconfig(ampm_text, text="PM")
        canvas.coords(ampm_text, center_x + 30, center_y + 35)

    # Update second-hand progress arc
    # Each second = 6 degrees (360/60)
    canvas.itemconfig(second_arc, extent=-current_second * 6)

    # Schedule next update
    canvas.after(1000, update_time)

# Start updating
update_time()
root.mainloop()
