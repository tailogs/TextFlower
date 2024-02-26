import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


def search_string():
    file_path = file_label.cget("text")
    if file_path == "Select file":
        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, "The file is not selected")
        return
    
    try:
        with open(file_path, 'r', encoding="UTF-8") as file:
            content = file.read()

        array = eval(content)

        search_string = entry.get().lower()

        found = False
        for subarray in array:
            if search_string in [element.lower() for element in subarray]:
                result_text.delete('1.0', tk.END)
                result_text.insert(tk.END, str(subarray))
                found = True

        if not found:
            result_text.delete('1.0', tk.END)
            result_text.insert(tk.END, "Не найдено")
    except Exception as e:
        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, f"File reading error: {str(e)}")


def load_default_file():
    default_file_path = "seed.txt"
    file_label.config(text=default_file_path)


def choose_file():
    file_path = filedialog.askopenfilename(title="Select file", filetypes=[("Text file", "*.txt")])
    if file_path:
        file_label.config(text=file_path)


window = tk.Tk()
window.title("textFlower")
window.resizable(width=False, height=False)

window.configure(bg="#FFB6C1")

style = ttk.Style()
style.configure("TLabel", background="#FFB6C1", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12))

top_frame = tk.Frame(window, bg="#FFB6C1")
bottom_frame = tk.Frame(window, bg="#FFB6C1")

label = ttk.Label(top_frame, text="Что ты хочешь найти??")
label.pack(pady=10)

entry = ttk.Entry(top_frame)
entry.pack()

button = ttk.Button(top_frame, text="Найти", command=search_string, style="TButton")
style.map("TButton", foreground=[('active', '#FF4500'), ('pressed', '#FF6347')], background=[('active', '#FFA07A'), ('pressed', '#FA8072')])
button.pack(pady=10)

result_text = tk.Text(bottom_frame, height=5, width=40, font=("Helvetica", 11))
result_text.pack(pady=10)

file_label = ttk.Label(bottom_frame, text="")
file_label.pack(pady=5)

load_default_file()  # Загрузка файла по умолчанию

top_frame.pack(pady=30)
bottom_frame.pack(pady=30)

window.mainloop()
