import customtkinter as ctk
from PIL import Image
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Меню кафе")
root.geometry("350x600")
root.resizable(False,False)

menu_items = [
    ("Борщ", "images/borsch.jpg"),
    ("Вареники", "images/varenyky.png"),
    ("Картопля фрі", "images/fries.jpg"),
    ("Піца", "images/pizza.png"),
    ("Стейк", "images/steak.jpg"),
    ("Лазанья", "images/lasagna.jpg"),
    ("Морозиво", "images/ice_cream.jpg"),
    ("Чай", "images/tea.jpg"),
    ("Кава", "images/coffee.jpg")
]

selected_items = {}


def update_selection():
    chosen_dishes = []
    for item, var in selected_items.items():
        if var.get() == 1:
            chosen_dishes.append(item)

    result_text.delete("1.0", ctk.END)
    result_text.insert(ctk.END, "\n".join(chosen_dishes))

    with open("selected_dishes.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(chosen_dishes))


frame = ctk.CTkFrame(root)
frame.pack(pady=10, padx=10, fill="both", expand=True)

columns = 3
for i, (item, img_path) in enumerate(menu_items):
    item_frame = ctk.CTkFrame(frame)
    item_frame.grid(
        row=i // columns,
        column=i % columns,
        padx=5,
        pady=5,
        sticky="nsew"
    )

    var = ctk.IntVar()
    if os.path.exists(img_path):

        img = ctk.CTkImage(
            light_image=Image.open(img_path),
            size=(80, 80)
        )
    else:
        img = None

    label = ctk.CTkLabel(
        item_frame,
        text=item,
        image=img,
        compound="top",
        wraplength=80
    )
    if img:
        label.image = img
    label.pack(pady=5)

    check = ctk.CTkCheckBox(
        item_frame,
        text="Обрати",
        variable=var,
        command=update_selection
    )
    check.pack(pady=5)

    selected_items[item] = var

result_text = ctk.CTkTextbox(root, height=100, width=350)
result_text.pack(pady=20)

root.mainloop()