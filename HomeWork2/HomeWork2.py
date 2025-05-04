import customtkinter as ctk
import screeninfo
root = ctk.CTk()
ctk.set_appearance_mode("dark")

def left():
    result.configure(text="Ти втратив голову", font=('Montserrat', 12))

def mid():
    result.configure(text="Ти втратив життя", font=('Montserrat', 12))

def right():
    result.configure(text="Ти втратив коня", font=('Montserrat', 12))

w1 = root.winfo_screenwidth()
h1 = root.winfo_screenheight()
root.geometry(f'300x300+{int(w1/2)}+{int(h1/2-150)}')

label = ctk.CTkLabel(root, text="Направо підеш – коня втратиш!\nНаліво підеш – голову втратиш!"
                                "\nПрямо підеш – життя втратиш!"
                                "\nЗроби свій вибір:", justify="center", font=('Montserrat', 13))
label.pack(pady=10)

btn1 = ctk.CTkButton(root, text='Ліво', command=left, font=('Montserrat', 12), fg_color="purple3", hover_color="purple4")
btn1.pack(ipadx=30, pady=0)

btn2 = ctk.CTkButton(root, text='Прямо', command=mid, font=('Montserrat', 12), fg_color="purple3", hover_color="purple4")
btn2.pack(ipadx=30, pady=10)

btn3 = ctk.CTkButton(root, text='Право', command=right, font=('Montserrat', 12), fg_color="purple3", hover_color="purple4")
btn3.pack(ipadx=30)

result = ctk.CTkLabel(root, text="")
result.pack(pady=10)

root.mainloop()
