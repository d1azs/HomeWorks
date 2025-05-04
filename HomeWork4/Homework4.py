import customtkinter as ctk
import re
import math

history_list = []
def calc(key):
    current_text = entry1.get()
    if key == "=":
        try:
            result = eval(current_text)
            entry1.delete(0, 'end')
            entry1.insert('end', str(result))
            history_list.append(f'{current_text} = {result}')
        except Exception as e:
            print(f'Error: {e}')
    elif key == "C":
        entry1.delete(0, 'end')
    elif key == "⌫":
        entry1.delete(len(current_text) - 1, 'end')
    elif key == "x2":
        if current_text:
            numbers = re.findall(r'-?\d+\.?\d*', current_text)
            if numbers:
                last_number = numbers[-1]
                squared_number = str(float(last_number) ** 2)
                new_text = current_text[:len(current_text) - len(last_number)] + squared_number
                entry1.delete(0, 'end')
                entry1.insert('end', new_text)
    elif key == "√x":
        if current_text:
            numbers = re.findall(r'-?\d+\.?\d*', current_text)
            if numbers:
                last_number = numbers[-1]
                if float(last_number) < 0:
                    return
                else:
                    squared_number = str(round(math.sqrt(float(last_number)), 2))
                    new_text = current_text[:len(current_text) - len(last_number)] + squared_number
                    entry1.delete(0, 'end')
                    entry1.insert('end', new_text)
    elif key == "1/x":
        if current_text:
            numbers = re.findall(r'-?\d+\.?\d*', current_text)
            if numbers:
                last_number = numbers[-1]
                if float(last_number) == 0:
                    return
                else:
                    inverse_number = str(round(1 / float(last_number), 2))
                    new_text = current_text[:len(current_text) - len(last_number)] + inverse_number
                    entry1.delete(0, 'end')
                    entry1.insert('end', new_text)
    elif key == "+/-":
        if current_text:
            numbers = re.findall(r'-?\d+\.?\d*', current_text)
            if numbers:
                last_number = numbers[-1]
                if last_number.startswith('-'):
                    new_number = last_number[1:]
                else:
                    new_number = '-' + last_number
                new_text = current_text[:len(current_text) - len(last_number)] + new_number
                entry1.delete(0, 'end')
                entry1.insert('end', new_text)
    else:
        entry1.insert('end', key)

def history():
    app = ctk.CTk()
    app.title('Історія')
    texbox=ctk.CTkTextbox(app, font=("Montserrat", 25))
    texbox.pack()
    for i in history_list:
        texbox.insert('1.0',f'{i}\n')
    app.mainloop()

root = ctk.CTk()
root.geometry("400x580")
root.configure(bg="black")
root.resizable(False, False)

btn1=ctk.CTkButton(root,height=20,
                   width=20,
                   text='Історія',
                   fg_color = "purple3",
                   hover_color = "purple4",
                   command=history)
btn1.place(x=345, y=0)
entry_frame = ctk.CTkFrame(root, fg_color="black")
entry_frame.pack(pady=20)

entry1 = ctk.CTkEntry(entry_frame, width=380, height=80, font=("Montserrat", 30),
                      justify='right', fg_color="black", text_color="white",
                      border_width=0)
entry1.pack(pady=10, padx=10)

mylist = [
    '(', ')', 'C', '⌫',
    '1/x', 'x2', '√x', '/',
    '7', '8', '9', '*',
    '4', '5', '6', '-',
    '1', '2', '3', '+',
    '+/-', '0', '.', '='
]

dark_buttons = {'(', ')', 'C', '⌫', '1/x', 'x2', '√x','/', '*', '-', '+'}
light_buttons = {'7','8', '9', '4', '5', '6','1', '2', '3','0', '.', '+/-'}



def get_button_style(text):
    if text in dark_buttons:
        return {'fg_color': "#323232", 'hover_color': "#3b3b3b"}
    elif text in light_buttons:
        return {'fg_color': "#3b3b3b", 'hover_color': "#323232"}
    elif text == "=":
        return {'fg_color': "purple3", 'hover_color': "purple4"}
    return {}


rows, cols = 6, 4
button_frame = ctk.CTkFrame(root, fg_color="black")
button_frame.pack(side="bottom", fill="both", expand=True, pady=10)

for i, item in enumerate(mylist):
    style = get_button_style(item)
    button = ctk.CTkButton(button_frame, text=item, command=lambda x=item: calc(x),
                           font=("Montserrat", 17), text_color="white",
                           width=95, height=65, corner_radius=5, **style)
    button.grid(row=i // cols, column=i % cols, padx=2, pady=2)

root.mainloop()