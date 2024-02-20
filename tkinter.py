import tkinter as tk
from tkinter import filedialog, messagebox

def browse_files():
    file_paths = filedialog.askopenfilenames()
    if file_paths:
        entry_files.delete(1.0, tk.END)
        for file_path in file_paths:
            entry_files.insert(tk.END, file_path + '\n')

def perform_action():
    file_paths = entry_files.get(1.0, tk.END).split('\n')
    file_paths = [path.strip() for path in file_paths if path.strip()]
    # Здесь можно выполнять требуемые действия с файлами
    # и обновлять данные
    updated_data = "Новые данные"
    text_output.delete(1.0, tk.END)
    text_output.insert(tk.END, updated_data)

def my_function():
    messagebox.showinfo("Сообщение", "Функция выполняется!")

root = tk.Tk()
root.title("Мое красивое GUI")
root.configure(bg="#222222")

# Создаем метку и поле ввода для путей файлов
label_files = tk.Label(root, text="Пути файлов:", fg="white", bg="#222222")
label_files.pack()

entry_files = tk.Text(root, width=50, height=10)
entry_files.pack()

# Создаем кнопку "Обзор" для выбора файлов
button_browse = tk.Button(root, text="Обзор", command=browse_files, bg="#555555", fg="white")
button_browse.pack()

# Создаем кнопку "Выполнить действие"
button_action = tk.Button(root, text="Выполнить действие", command=perform_action, bg="#555555", fg="white")
button_action.pack()

# Создаем кнопку "Моя функция"
button_my_function = tk.Button(root, text="Моя функция", command=my_function, bg="#555555", fg="white")
button_my_function.pack()

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

