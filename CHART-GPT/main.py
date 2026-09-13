import tkinter as tk

# Function to update the display
def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

# Function to clear display
def clear():
    entry.delete(0, tk.END)

# Function for backspace
def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

# Function to calculate result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create window
root = tk.Tk()
root.title("Calculator-for-Company")
root.geometry("350x500")
root.resizable(True, True)

# Display
entry = tk.Entry(
    root,
    font=("Arial", 24),
    bd=10,
    relief=tk.RIDGE,
    justify="right"
)
entry.pack(fill="both", padx=10, pady=10, ipady=10)

# Frame for buttons
frame = tk.Frame(root)
frame.pack()

# Button layout
buttons = [
    ["C", "⌫", "/", "*"],
    ["7", "8", "9", "-"],
    ["4", "5", "6", "+"],
    ["1", "2", "3", "="],
    ["0", ".", "", ""]
]

# Create buttons
for r, row in enumerate(buttons):
    for c, text in enumerate(row):
        if text == "":
            continue

        if text == "C":
            btn = tk.Button(
                frame, text=text, width=6, height=2,
                font=("Arial", 18), command=clear
            )

        elif text == "⌫":
            btn = tk.Button(
                frame, text=text, width=6, height=2,
                font=("Arial", 18), command=backspace
            )

        elif text == "=":
            btn = tk.Button(
                frame, text=text, width=6, height=2,
                font=("Arial", 18), command=calculate
            )

        else:
            btn = tk.Button(
                frame, text=text, width=6, height=2,
                font=("Arial", 18),
                command=lambda t=text: click(t)
            )

        btn.grid(row=r, column=c, padx=5, pady=5)

root.mainloop()