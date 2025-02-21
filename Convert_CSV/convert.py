import re
import csv
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk

'''''''''

# this was really just for fun because i needed a 'break' and a frontend to play around with!

'''''''''

def convert_file(input_file):
    
    #read
    with open(input_file, 'r', encoding='utf-8') as file:
        data = file.readlines()

    #urgh regex - thanks chatgpt
    # for com.apps
    pattern = re.compile(r'time="([\d\-:\s]+)"\s+type=([A-Z_]+)\s+package=([a-zA-Z0-9\.]+)')  

    csv_data = [['Timestamp', 'Activity Type', 'Application']]

    # loop lines - append time and duration
    for line in data:
        match = pattern.search(line)
        if match:
            timestamp, activity_type, duration = match.groups()
            csv_data.append([timestamp, activity_type, duration])

    # user save location
    output_file = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV files", "*.csv")],
        title="Save As"
    )

    if not output_file:  # User canceled the save dialog thanks chatgpt omg
        return None

    # to CSV
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(csv_data)
        return output_file
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save file: {e}")
        return None

def select_file():
    file_path = filedialog.askopenfilename(title="Select a text file", filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            output_file = convert_file(file_path)
            if output_file:  # if location chosen
                messagebox.showinfo("Success", f"File converted successfully!\nSaved as: {output_file}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

root = tk.Tk()
root.title("TXT to CSV Converter")
root.geometry("480x480")
root.configure(bg="#000000")
root.resizable(False, False)

# Background
bg_original = Image.open("assets/background.png")
bg_photo = ImageTk.PhotoImage(bg_original)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


# button hover functions
def on_enter(event):
    convert_button.config(fg="#95CF3F")

def on_leave(event):
    convert_button.config(fg="#ffffff")

# style
btn_style = {
    "font": ("Terminal", 22, "bold"),
    "bg": "#000000",
    "fg": "#ffffff",
    "padx": 28,
    "pady": 20,
    "bd": 0.5,
    "relief": "raised",
    "highlightthickness": 0,
    "overrelief": "groove",
}
head_style = {
    "font": ("Terminal", 20, "bold"),
    "bg": "#000000",
    "fg": "#ffffff",
    "padx": 34,
    "pady": 10,
}

# Widgets
heading = tk.Label(root, text='-> Select file \n-> Choose save location', **head_style)
heading.place(relx=0.5, rely=0.1, anchor="center")

convert_button = tk.Button(root, text="SELECT FILE", command=select_file, **btn_style)
convert_button.place(relx=0.5, rely=0.485, anchor="center")

# hover button
convert_button.bind("<Enter>", on_enter)  
convert_button.bind("<Leave>", on_leave)


root.mainloop()