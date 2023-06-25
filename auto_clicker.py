import pyautogui
import tkinter as tk

# color palette
BACKGROUND_COLOR = "#F8F8F8"
BUTTON_COLOR = "#007FFF"
BUTTON_HOVER_COLOR = "#005B9E"
TEXT_COLOR = "#212121"
LABEL_COLOR = "#757575"

def click():
    pos = location_entry.get().split(',')
    x = int(pos[0])
    y = int(pos[1])
    n = int(n_entry.get())
    delay = float(delay_entry.get())
    for i in range(n):
        pyautogui.click(x=x, y=y, interval=delay)

def capture_location(event):
    if event.char == "c":
        x, y = pyautogui.position()
        location_entry.delete(0, tk.END)
        location_entry.insert(tk.END, f"{x}, {y}")

root = tk.Tk()
root.title("Auto Clicker")
root.config(bg=BACKGROUND_COLOR)

# Location entry
location_label = tk.Label(root, text="Location (x, y):", font=("Helvetica", 12), fg=LABEL_COLOR, bg=BACKGROUND_COLOR)
location_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

location_entry = tk.Entry(root, width=10, font=("Helvetica", 12))
location_entry.grid(row=0, column=1, padx=10, pady=10)

# N entry
n_label = tk.Label(root, text="N:", font=("Helvetica", 12), fg=LABEL_COLOR, bg=BACKGROUND_COLOR)
n_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

n_entry = tk.Entry(root, width=10, font=("Helvetica", 12))
n_entry.grid(row=1, column=1, padx=10, pady=10)

# Delay entry
delay_label = tk.Label(root, text="Delay (seconds):", font=("Helvetica", 12), fg=LABEL_COLOR, bg=BACKGROUND_COLOR)
delay_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

delay_entry = tk.Entry(root, width=10, font=("Helvetica", 12))
delay_entry.grid(row=2, column=1, padx=10, pady=10)

# Click button
click_button = tk.Button(root, text="Click", font=("Helvetica", 12), bg=BUTTON_COLOR, fg=TEXT_COLOR, activebackground=BUTTON_HOVER_COLOR, command=click)
click_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Capture instruction
capture_label = tk.Label(root, text="Press 'c' to capture the mouse position", font=("Helvetica", 10), fg=LABEL_COLOR, bg=BACKGROUND_COLOR)
capture_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Bind keypress event to capture_location function
root.bind('<Key>', capture_location)

# Set window position to center of the screen
window_width = 300
window_height = 250
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = int(screen_width/2 - window_width/2)
y_position = int(screen_height/2 - window_height/2)
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

root.mainloop()
