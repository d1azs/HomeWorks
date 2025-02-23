import customtkinter as ctk
from CTkMessagebox import *


root=ctk.CTk()
root.geometry('400x150')

root.title('Перевірка рівня цукру в крові')

msg_style_warning = {
    'button_color':'#efb700',
    'button_hover_color':'#ef9700',
    'justify':'center',
    'button_text_color':'black',
    'font':('Montserrat', 12)
}
msg_style_check = {
    'button_color':'#87df00',
    'button_hover_color':'#64ab00',
    'justify':'center',
    'button_text_color':'black',
    'font':('Montserrat', 12)
}
btn_style = {
    'font': ('Montserrat', 13),
    'fg_color': "purple3",
    'hover_color': "purple4",
    'text_color': "white",
}
def check_sugar_level():
    try:
        age = int(entry1.get())
        sugar = float(entry2.get())
        if 18 <= age <= 59:
            norm_min, norm_max = 4.11, 5.89
        elif 60 <= age <= 90:
            norm_min, norm_max = 4.56, 6.38
        elif age > 90:
            norm_min, norm_max = 4.16, 6.72
        else:
            CTkMessagebox(title="Помилка",
                          message="Вік має бути більше 18!",
                          icon="warning",
                          **msg_style_warning)
            return

        if norm_min <= sugar <= norm_max:
            CTkMessagebox(title="Рівень цукру",
                          message="Рівень цукру в нормі",
                          icon="check",
                          **msg_style_check)
        elif sugar < norm_min:
            CTkMessagebox(title="Рівень цукру",
                          message="Рівень цукру занизький",
                          icon="warning",
                          **msg_style_warning)
        else:
            CTkMessagebox(title="Рівень цукру",
                          message="Рівень цукру завищений",
                          icon="warning",
                          **msg_style_warning)
    except ValueError:
        CTkMessagebox(title="Помилка",
                      message="Будь ласка, введіть коректні значення!",
                      icon="warning",
                          **msg_style_warning)



frame = ctk.CTkFrame(root,
                     fg_color='transparent')
frame.pack(pady=15)

label1=ctk.CTkLabel(frame,
                    text='Вік (років):',
                    font=('Montserrat', 13))
label1.grid(row=0,column=0,padx=10)

entry1=ctk.CTkEntry(frame)
entry1.grid(row=0,column=1)

label2=ctk.CTkLabel(frame,
                    text="Рівень цукру (ммоль/л):",
                    font=('Montserrat', 13))
label2.grid(row=1,column=0,padx=10,pady=10)

entry2=ctk.CTkEntry(frame)
entry2.grid(row=1,column=1)

check_button = ctk.CTkButton(root,
                             text="Перевірити",
                             **btn_style,
                             command=check_sugar_level)
check_button.pack()

root.mainloop()