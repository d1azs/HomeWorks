import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("light")
root = ctk.CTk()
root.geometry("1280x720")
root.resizable(False, False)

scrollable_frame = ctk.CTkScrollableFrame(root, width=1280, height=720, fg_color='white')
scrollable_frame.pack(fill="both", expand=True)

logo = ctk.CTkLabel(scrollable_frame,
                    text="",
                    bg_color='white',
                    image=ctk.CTkImage(Image.open("images/AudiLogo.png"),
                    size=(110, 63)))
logo.pack()

image_label = ctk.CTkLabel(scrollable_frame, text='', image=ctk.CTkImage(Image.open('images/AudiQ6e-tron.jpg'), size=(1280, 720)))
image_label.pack()

overlay_label = ctk.CTkLabel(scrollable_frame, text="Новий Audi Q6 e-tron", text_color='black', font=("Montserrat", 30), bg_color='transparent')
overlay_label.place(x=50, y=70)

overlay_label2 = ctk.CTkLabel(scrollable_frame, text="Захоплююча продуктивність", text_color='black', font=("Montserrat", 22), bg_color='transparent')
overlay_label2.place(x=50, y=130)

def show_Q6ETron():
    scrollable_frame.pack_forget()
    image_car = ctk.CTkLabel(root,
                             text='Audi Q6 e-tron\n'
                                  '2500000 ₴',
                             image=ctk.CTkImage(Image.open("images/Q6-e-tron.webp"),
                             size=(960, 540)),
                             compound='top',
                             font=("Montserrat", 35, 'bold'))
    image_car.pack()

    bought_button = ctk.CTkButton(root, text="Придбати модель",
                                  corner_radius=0,
                                  command=lambda: bought_car('Q6 e-tron', "2500000 ₴"),
                                  fg_color='#2e2e2e',
                                  text_color='white',
                                  hover_color='#636363',
                                  font=("Montserrat", 15, 'bold'),
                                  width=250,
                                  height=35)
    bought_button.pack(pady=10)

    back_button = ctk.CTkButton(root, text="Повернутися до головної",
                                command=lambda: return_to_models(image_car, back_button, bought_button),
                                corner_radius=0,
                                fg_color='#2e2e2e',
                                text_color='white',
                                hover_color='#636363',
                                font=("Montserrat", 15, 'bold'),
                                width=200,
                                height=25)
    back_button.place(x=50, y=50)


button_purchase = ctk.CTkButton(scrollable_frame,
                                text='ПРИДБАТИ',
                                corner_radius=0,
                                fg_color='white',
                                text_color='black',
                                hover_color='#dee2e6',
                                width=170,
                                height=40,
                                font=("Montserrat", 15),
                                command=show_Q6ETron)

button_purchase.place(x=50, y=185)

models_label1 = ctk.CTkLabel(scrollable_frame, text="Моделі", text_color='black', font=("Montserrat", 18, 'bold'), bg_color='transparent')
models_label1.pack()

type_models_label1 = ctk.CTkLabel(scrollable_frame, text="Тип автомобіля", text_color='grey', font=("Montserrat", 18, 'normal'), bg_color='transparent')
type_models_label1.pack()

def change_on_types():
    scrollable_frame_horizontal2 = ctk.CTkScrollableFrame(scrollable_frame, width=1280, height=150, fg_color='white', corner_radius=10, orientation='horizontal')
    scrollable_frame_horizontal2.pack(fill="x", expand=True)

    models = [
        {"type": "Limousine", "image_path": "images/A5.webp", "name": "A5", "price": "1500000 ₴"},
        {"type": "Limousine", "image_path": "images/A6.webp", "name": "A6", "price": "1800000 ₴"},
        {"type": "Sportback", "image_path": "images/A7.webp", "name": "A7", "price": "2200000 ₴"},
        {"type": "Limousine", "image_path": "images/A8.webp", "name": "A8", "price": "3000000 ₴"},
        {"type": "Compact SUV", "image_path": "images/Q3.webp", "name": "Q3", "price": "1600000 ₴"},
        {"type": "SUV", "image_path": "images/Q5.jpg", "name": "Q5", "price": "2100000 ₴"},
        {"type": "Electric SUV", "image_path": "images/Q6-e-tron.webp", "name": "Q6", "price": "2500000 ₴"},
        {"type": "Coupe SUV", "image_path": "images/Q8.webp", "name": "Q8", "price": "3300000 ₴"}
    ]

    for idx, model in enumerate(models):
        label = ctk.CTkLabel(
            scrollable_frame_horizontal2,
            text=model["type"],
            image=ctk.CTkImage(Image.open(model["image_path"]), size=(180, 120)),
            compound='top',
            font=("Montserrat", 15, 'bold')
        )

        label.grid(column=idx, row=0)
        label.bind("<Button-1>", lambda event, name=model["name"], price=model["price"], path=model["image_path"]: show_car(event, path, name, price))

    return scrollable_frame_horizontal2

def change_on_models():
    scrollable_frame_horizontal = ctk.CTkScrollableFrame(scrollable_frame, width=1280, height=150, fg_color='white', corner_radius=10, orientation='horizontal')
    scrollable_frame_horizontal.pack(fill="x", expand=True)

    models = [
        {"name": "A5", "image_path": "images/A5.webp", "price": "1500000 ₴"},
        {"name": "A6", "image_path": "images/A6.webp", "price": "1800000 ₴"},
        {"name": "A7", "image_path": "images/A7.webp", "price": "2200000 ₴"},
        {"name": "A8", "image_path": "images/A8.webp", "price": "3000000 ₴"},
        {"name": "Q3", "image_path": "images/Q3.webp", "price": "1600000 ₴"},
        {"name": "Q5", "image_path": "images/Q5.jpg", "price": "2100000 ₴"},
        {"name": "Q6 e-tron", "image_path": "images/Q6-e-tron.webp", "price": "2500000 ₴"},
        {"name": "Q8", "image_path": "images/Q8.webp", "price": "3300000 ₴"}
    ]

    for idx, model in enumerate(models):
        label = ctk.CTkLabel(
            scrollable_frame_horizontal,
            text=model["name"],
            image=ctk.CTkImage(Image.open(model["image_path"]), size=(180, 120)),
            compound='top',
            font=("Montserrat", 15, 'bold')
        )
        label.grid(column=idx, row=0)
        label.bind("<Button-1>", lambda event, name=model["name"], price=model["price"], path=model["image_path"]: show_car(event, path, name, price))

    return scrollable_frame_horizontal

def bought_car(car,price):
    with open("paycheck.txt", "w", encoding="utf-8") as file:
        file.write(f"--Ти придбав авто--\n"
                   f"Чек\n"
                   f"{price}\n"
                   f"Audi {car}\n")

def show_car(event, image_path, car_name, price):
    scrollable_frame.pack_forget()
    image_car = ctk.CTkLabel(root,
                             text=f'Audi {car_name}\n'
                                  f'Ціна {price}',
                             image=ctk.CTkImage(Image.open(image_path),
                             size=(960, 540)),
                             compound='top',
                             font=("Montserrat", 35, 'bold'))
    image_car.pack()

    bought_button = ctk.CTkButton(root, text="Придбати модель",
                                  corner_radius=0,
                                  command=lambda: bought_car(car_name, price),
                                  fg_color='#2e2e2e',
                                  text_color='white',
                                  hover_color='#636363',
                                  font=("Montserrat", 15, 'bold'),
                                  width=250,
                                  height=35)
    bought_button.pack(pady=10)

    back_button = ctk.CTkButton(root, text="Повернутися до моделей",
                                command=lambda: return_to_models(image_car, back_button, bought_button),
                                corner_radius=0,
                                fg_color='#2e2e2e',
                                text_color='white',
                                hover_color='#636363',
                                font=("Montserrat", 15, 'bold'),
                                width=250,
                                height=35)
    back_button.place(x=50, y=50)





def return_to_models(image_car, back_button, bought_button):
    image_car.pack_forget()
    back_button.place_forget()
    bought_button.pack_forget()
    scrollable_frame.pack(fill="both", expand=True)

def on_label_click_type(event):
    global scrollable_frame_horizontal2
    type_models_label1.configure(text_color='black', font=("Montserrat", 18, 'bold'))
    models_label1.configure(text_color='grey', font=("Montserrat", 18, 'normal'))
    if 'scrollable_frame_horizontal' in globals():
        scrollable_frame_horizontal.pack_forget()
    scrollable_frame_horizontal2 = change_on_types()

type_models_label1.bind("<Button-1>", on_label_click_type)

def on_label_click_model(event):
    models_label1.configure(text_color='black', font=("Montserrat", 18, 'bold'))
    type_models_label1.configure(text_color='grey', font=("Montserrat", 18, 'normal'))
    if 'scrollable_frame_horizontal2' in globals():
        scrollable_frame_horizontal2.pack_forget()
    global scrollable_frame_horizontal
    scrollable_frame_horizontal = change_on_models()

models_label1.bind("<Button-1>", on_label_click_model)
scrollable_frame_horizontal = change_on_models()

root.mainloop()