import tkinter as tk
from tkinter import filedialog, messagebox

def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        entry_file_path.delete(0, tk.END)
        entry_file_path.insert(tk.END, file_path)

def perform_action():
    file_path = entry_file_path.get()
    # Здесь можно выполнять требуемые действия с файлом
    # и обновлять данные
    updated_data = "Новые данные"
    text_output.delete(1.0, tk.END)
    text_output.insert(tk.END, updated_data)

root = tk.Tk()
root.title("Мое красивое GUI")
root.configure(bg="#222222")

# Создаем метку и поле ввода для пути файла
label_file_path = tk.Label(root, text="Путь файла:", fg="white", bg="#222222")
label_file_path.pack()

entry_file_path = tk.Entry(root, width=50)
entry_file_path.pack()

# Создаем кнопку "Обзор" для выбора файла
button_browse = tk.Button(root, text="Обзор", command=browse_file, bg="#555555", fg="white")
button_browse.pack()

# Создаем кнопку "Выполнить действие"
button_action = tk.Button(root, text="Выполнить действие", command=perform_action, bg="#555555", fg="white")
button_action.pack()

# Создаем метку и текстовую область для выгрузки данных
label_output = tk.Label(root, text="Обновленные данные:", fg="white", bg="#222222")
label_output.pack()

text_output = tk.Text(root, width=50, height=10, bg="#333333", fg="white")
text_output.pack()

# Создаем консоль
console_label = tk.Label(root, text="Консоль:", fg="white", bg="#222222")
console_label.pack()

console_output = tk.Text(root, width=50, height=10, bg="#333333", fg="white")
console_output.pack()

def write_to_console(message):
    console_output.insert(tk.END, message + "\n")
    console_output.see(tk.END)

# Пример вывода сообщения в консоль
write_to_console("Привет, это моя консоль!")

root.mainloop()
