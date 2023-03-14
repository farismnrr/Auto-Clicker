import pyautogui
import tkinter as tk

# color palette
BACKGROUND_COLOR = "#F8F8F8"
BUTTON_COLOR = "#007FFF"
BUTTON_HOVER_COLOR = "#005B9E"
TEXT_COLOR = "#212121"
LABEL_COLOR = "#757575"

def click():
    x = int(x_entry.get())
    y = int(y_entry.get())
    n = int(n_entry.get())
    delay = float(delay_entry.get())
    for i in range(n):
        pyautogui.click(x=x, y=y, interval=delay)

def get_mouse_pos(event):
    if event.char == '`':
        x, y = pyautogui.position()
        x_entry.delete(0, tk.END)
        x_entry.insert(0, str(x))
        y_entry.delete(0, tk.END)
        y_entry.insert(0, str(y))

root = tk.Tk()
root.title("Auto Clicker")
root.config(bg=BACKGROUND_COLOR)

# X entry
x_label = tk.Label(root, text="X:", font=("Helvetica", 12), fg=LABEL_COLOR, bg=BACKGROUND_COLOR)
x_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
x_entry = tk.Entry(root, width=10, font=("Helvetica", 12))
x_entry.grid(row=0, column=1, padx=10, pady=10)

# Y entry
y_label = tk.Label(root, text="Y:", font=("Helvetica", 12), fg=LABEL_COLOR, bg=BACKGROUND_COLOR)
y_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
y_entry = tk.Entry(root, width=10, font=("Helvetica", 12))
y_entry.grid(row=1, column=1, padx=10, pady=10)

# N entry
n_label = tk.Label(root, text="N:", font=("Helvetica", 12), fg=LABEL_COLOR, bg=BACKGROUND_COLOR)
n_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
n_entry = tk.Entry(root, width=10, font=("Helvetica", 12))
n_entry.grid(row=2, column=1, padx=10, pady=10)

# Delay entry
delay_label = tk.Label(root, text="Delay (seconds):", font=("Helvetica", 12), fg=LABEL_COLOR, bg=BACKGROUND_COLOR)
delay_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
delay_entry = tk.Entry(root, width=10, font=("Helvetica", 12))
delay_entry.grid(row=3, column=1, padx=10, pady=10)

# Click button
click_button = tk.Button(root, text="Click", font=("Helvetica", 12), bg=BUTTON_COLOR, fg=TEXT_COLOR, activebackground=BUTTON_HOVER_COLOR, command=click)
click_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Get mouse position button
get_pos_button = tk.Button(root, text="Get Mouse Position", font=("Helvetica", 12), bg=BUTTON_COLOR, fg=TEXT_COLOR, activebackground=BUTTON_HOVER_COLOR)
get_pos_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Bind keypress event to get_mouse_pos function
root.bind('<KeyPress>', get_mouse_pos)

# Set window position to center of the screen
window_width = 300
window_height = 250
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = int(screen_width/2 - window_width/2)
y_position = int(screen_height/2 - window_height/2)
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

root.mainloop()
