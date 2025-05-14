import tkinter as tk
from tkinter import ttk, Menu, messagebox as msg
import sys
import threading
from time import sleep
from tkinter import filedialog
from PIL import Image, ImageTk
import random
import time

BG_COLOR = "#f4f4f4"
CANVAS_BG = "#ffffff"
BUTTON_COLOR = "#4a90e2"
BUTTON_TEXT = "#ffffff"
FONT = ("Segoe UI", 10)

def upload_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")],
        title="Select an image"
    )
    if not file_path:
        return

    image = Image.open(file_path).resize((150, 100), Image.Resampling.LANCZOS)
    img_tk = ImageTk.PhotoImage(image)
    canvas2.image = img_tk
    canvas2.create_image(0, 0, anchor="nw", image=img_tk)

    global loading_label
    loading_label = ttk.Label(input_frame, text="Identifying...", foreground="blue")
    loading_label.grid(column=0, row=3, columnspan=2, pady=5)

    def delayed_generate():
        time.sleep(3)
        try:
            predicted = predict_number_from_image(file_path)
            number.set(str(predicted))
            win.after(0, generate)
        except Exception as e:
            msg.showerror("Image Error", f"Failed to process image:\n{str(e)}")
        finally:
            win.after(0, lambda: loading_label.destroy())

    threading.Thread(target=delayed_generate, daemon=True).start()

def draw_stem():
    canvas.create_line(51, 26, 51, 126, width=3)


def draw_ones(num):
    if num == 1:
        canvas.create_line(51, 26, 88, 26, width=3)
    elif num == 2:
        canvas.create_line(51, 56, 88, 56, width=3)
    elif num == 3:
        canvas.create_line(51, 26, 88, 56, width=3)
    elif num == 4:
        canvas.create_line(51, 56, 88, 26, width=3)
    elif num == 5:
        canvas.create_line(51, 26, 88, 26, width=3)
        canvas.create_line(51, 56, 88, 26, width=3)
    elif num == 6:
        canvas.create_line(88, 26, 88, 56, width=3)
    elif num == 7:
        canvas.create_line(51, 26, 88, 26, width=3)
        canvas.create_line(88, 26, 88, 56, width=3)
    elif num == 8:
        canvas.create_line(51, 56, 88, 56, width=3)
        canvas.create_line(88, 26, 88, 56, width=3)
    elif num == 9:
        canvas.create_line(51, 26, 88, 26, width=3)
        canvas.create_line(51, 56, 88, 56, width=3)
        canvas.create_line(88, 26, 88, 56, width=3)

def draw_tens(num):
    if num == 1:
        canvas.create_line(51, 26, 13, 26, width=3)
    elif num == 2:
        canvas.create_line(51, 56, 13, 56, width=3)
    elif num == 3:
        canvas.create_line(51, 26, 13, 56, width=3)
    elif num == 4:
        canvas.create_line(51, 56, 13, 26, width=3)
    elif num == 5:
        canvas.create_line(51, 26, 13, 26, width=3)
        canvas.create_line(51, 56, 13, 26, width=3)
    elif num == 6:
        canvas.create_line(13, 26, 13, 56, width=3)
    elif num == 7:
        canvas.create_line(51, 26, 13, 26, width=3)
        canvas.create_line(13, 26, 13, 56, width=3)
    elif num == 8:
        canvas.create_line(51, 56, 13, 56, width=3)
        canvas.create_line(13, 26, 13, 56, width=3)
    elif num == 9:
        canvas.create_line(51, 26, 13, 26, width=3)
        canvas.create_line(51, 56, 13, 56, width=3)
        canvas.create_line(13, 26, 13, 56, width=3)


def draw_hundreds(num):
    if num == 1:
        canvas.create_line(51, 126, 88, 126, width=3)
    elif num == 2:
        canvas.create_line(51, 96, 88, 96, width=3)
    elif num == 3:
        canvas.create_line(51, 126, 88, 96, width=3)
    elif num == 4:
        canvas.create_line(51, 96, 88, 126, width=3)
    elif num == 5:
        canvas.create_line(51, 126, 88, 126, width=3)
        canvas.create_line(51, 96, 88, 126, width=3)
    elif num == 6:
        canvas.create_line(88, 96, 88, 126, width=3)
    elif num == 7:
        canvas.create_line(51, 126, 88, 126, width=3)
        canvas.create_line(88, 96, 88, 126, width=3)
    elif num == 8:
        canvas.create_line(51, 96, 88, 96, width=3)
        canvas.create_line(88, 96, 88, 126, width=3)
    elif num == 9:
        canvas.create_line(51, 126, 88, 126, width=3)
        canvas.create_line(51, 96, 88, 96, width=3)
        canvas.create_line(88, 96, 88, 126, width=3)


def draw_thousands(num):
    if num == 1:
        canvas.create_line(51, 126, 13, 126, width=3)
    elif num == 2:
        canvas.create_line(51, 96, 13, 96, width=3)
    elif num == 3:
        canvas.create_line(51, 126, 13, 96, width=3)
    elif num == 4:
        canvas.create_line(51, 96, 13, 126, width=3)
    elif num == 5:
        canvas.create_line(51, 126, 13, 126, width=3)
        canvas.create_line(51, 96, 13, 126, width=3)
    elif num == 6:
        canvas.create_line(13, 96, 13, 126, width=3)
    elif num == 7:
        canvas.create_line(51, 126, 13, 126, width=3)
        canvas.create_line(13, 96, 13, 126, width=3)
    elif num == 8:
        canvas.create_line(51, 96, 13, 96, width=3)
        canvas.create_line(13, 96, 13, 126, width=3)
    elif num == 9:
        canvas.create_line(51, 126, 13, 126, width=3)
        canvas.create_line(51, 96, 13, 96, width=3)
        canvas.create_line(13, 96, 13, 126, width=3)

def generate_number(num):
    canvas.delete("all")
    tens, ones = divmod(num, 10)
    hundreds, tens = divmod(tens, 10)
    thousands, hundreds = divmod(hundreds, 10)

    draw_stem()
    draw_ones(ones)
    draw_tens(tens)
    draw_hundreds(hundreds)
    draw_thousands(thousands)

def predict_number_from_image(path):
    random_number = random.randint(1, 9999)
    return random_number


def generate(event=None):
    try:
        num = number.get()
        if len(num) > 4:
            raise ValueError("Input too long")
        num = int(num)
        if not (1 <= num <= 9999):
            raise ValueError("Out of range")
        generate_number(num)
    except Exception as e:
        msg.showerror("Invalid Input", "Please enter a number from 1 to 9999.\n" + str(e))

def count_up():
    def count_up_thread():
        for i in range(1, 10000):
            generate_number(i)
            sleep(1)
    threading.Thread(target=count_up_thread, daemon=True).start()


def _quit():
    if msg.askyesno("Exit Program", "Are you sure you want to exit?"):
        win.quit()
        win.destroy()
        sys.exit()

win = tk.Tk()
win.title("Cistercian Numerals")
win.configure(bg=BG_COLOR)
win.resizable(False, False)
win.geometry("600x250")

menu_bar = Menu(win)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Exit", command=_quit)
menu_bar.add_cascade(label="File", menu=file_menu)

help_menu = Menu(menu_bar, tearoff=0)
win.config(menu=menu_bar)

input_frame = ttk.Frame(win, padding=10)
input_frame.grid(column=0, row=0, sticky="nw", padx=10, pady=10)

ttk.Label(input_frame, text="Enter a number (1-9999):", font=FONT).grid(column=0, row=0, sticky="w", columnspan=2)

number = tk.StringVar()
entry = ttk.Entry(input_frame, width=12, textvariable=number, font=FONT)
entry.grid(column=0, row=1, sticky="w", pady=5)

generate_button = tk.Button(
    input_frame, text="Generate", command=generate,
    bg=BUTTON_COLOR, fg=BUTTON_TEXT, font=(FONT[0], 10, "bold"),
    relief="flat", padx=10, pady=5
)
generate_button.grid(column=1, row=1, padx=5)

canvas = tk.Canvas(win, width=101, height=150, bg=CANVAS_BG, highlightthickness=1, highlightbackground="#ccc")
canvas.grid(column=1, row=0, padx=20, pady=10)

upload_btn = tk.Button(
    input_frame, text="Upload Image", command=upload_image,
    bg="#6c757d", fg="white", font=(FONT[0], 10, "bold"),
    relief="flat", padx=10, pady=5
)
upload_btn.grid(column=0, row=2, columnspan=2, pady=10)


canvas2 = tk.Canvas(win, width=150, height=100, bg=CANVAS_BG, highlightthickness=1, highlightbackground="#ccc")
canvas2.grid(column=2, row=0, padx=20, pady=10)

entry.focus()
win.bind("<Return>", generate)

win.mainloop()
