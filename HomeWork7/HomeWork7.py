import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import random
import json
from captcha.image import ImageCaptcha
from CTkTable import *
import string


def generate_captcha():
    letters = string.ascii_uppercase + string.digits
    return "".join(random.choices(letters, k=6))


def create_captcha_image(captcha_text):
    image_captcha = ImageCaptcha(width=200, height=80)
    image = image_captcha.generate_image(captcha_text)
    return ctk.CTkImage(light_image=image, size=(200, 80))


root = ctk.CTk()
root.geometry("400x550")
root.title("User Management System")


def load_users():
    try:
        with open('register_form.json', 'r') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return {"username": "", "password": ""}
    except json.JSONDecodeError:
        return {"username": "", "password": ""}


def save_users(users_data):
    with open('register_form.json', 'w') as json_file:
        json.dump(users_data, json_file, indent=4)


def switch_to_register(frame):
    def verify_captcha():
        user_input = entry_register3.get()

        if user_input == captcha_text and entry_register.get() and entry_register2.get():
            username = entry_register.get()

            try:
                with open('register_form.json', 'r') as json_file:
                    register_data = json.load(json_file)

                if register_data.get('username') == username:
                    CTkMessagebox(title="Error", message="Username already exists!", icon="cancel")
                    return

            except FileNotFoundError:
                register_data = {}

            register_data = {
                "username": entry_register.get(),
                "password": entry_register2.get()
            }

            with open('register_form.json', 'w') as json_file:
                json.dump(register_data, json_file, indent=4)

            CTkMessagebox(message="Registration successful!", icon="check", option_1="Thanks")
            frame_register.pack_forget()
            switch_to_login()

        else:
            CTkMessagebox(title="Error", message="Something went wrong!!!", icon="cancel")

    frame.pack_forget()

    frame_register = ctk.CTkFrame(root)
    frame_register.pack(fill='both', expand=True)

    l1_register = ctk.CTkLabel(frame_register, text='Register')
    l1_register.pack(pady=10)

    entry_register = ctk.CTkEntry(frame_register, placeholder_text='Username')
    entry_register.pack()

    entry_register2 = ctk.CTkEntry(frame_register, placeholder_text='Password')
    entry_register2.pack(pady=10)

    captcha_text = generate_captcha()
    captcha_image = create_captcha_image(captcha_text)

    captcha_label = ctk.CTkLabel(frame_register, image=captcha_image, text="")
    captcha_label.pack(pady=10)

    entry_register3 = ctk.CTkEntry(frame_register, placeholder_text='Enter captcha')
    entry_register3.pack(pady=10)

    button_register = ctk.CTkButton(frame_register, text='Submit', command=verify_captcha)
    button_register.pack()


def switch_to_log_form(username, password, frame):
    frame.pack_forget()

    frame_log_form = ctk.CTkFrame(root)
    frame_log_form.pack(fill='both', expand=True)

    data = [
        ["Username", "Password"],
        [username, "****"]
    ]

    table = CTkTable(frame_log_form, values=data, width=350)
    table.pack(fill="x", pady=10)

    entry_new_username = ctk.CTkEntry(frame_log_form, placeholder_text='New Username', width=200)
    entry_new_username.pack(pady=5)

    entry_new_password = ctk.CTkEntry(frame_log_form, placeholder_text='New Password', width=200)
    entry_new_password.pack(pady=5)

    def add_user():
        new_username = entry_new_username.get()
        new_password = entry_new_password.get()

        if new_username and new_password:
            user_data = load_users()

            if "username" in user_data:
                user_data = [{"username": user_data["username"], "password": user_data["password"]}]
            elif type(user_data) != list:
                user_data = []

            for user in user_data:
                if user["username"] == new_username:
                    CTkMessagebox(title="Error", message="Username already exists!", icon="cancel")
                    return

            user_data.append({"username": new_username, "password": new_password})
            save_users(user_data)

            data.append([new_username, "****"])
            table.update_values(data)

            entry_new_username.delete(0, 'end')
            entry_new_password.delete(0, 'end')
            CTkMessagebox(title="Success", message="User added successfully!", icon="check")
        else:
            CTkMessagebox(title="Error", message="Username and password cannot be empty!", icon="cancel")

    button_add_user = ctk.CTkButton(frame_log_form, text='Add User', command=add_user, width=200)
    button_add_user.pack(pady=10)

    entry_delete_username = ctk.CTkEntry(frame_log_form, placeholder_text='Username to Delete', width=200)
    entry_delete_username.pack(pady=5)

    def delete_user():
        username_to_delete = entry_delete_username.get()

        if not username_to_delete:
            CTkMessagebox(title="Error", message="Please enter a username to delete!", icon="cancel")
            return

        user_data = load_users()

        if "username" in user_data:
            if user_data["username"] == username_to_delete:
                save_users({})
                while len(data) > 1:
                    data.pop()
                table.update_values(data)
                entry_delete_username.delete(0, 'end')
                CTkMessagebox(title="Success", message="User deleted successfully!", icon="check")
                return
            else:
                CTkMessagebox(title="Error", message="User not found!", icon="cancel")
                return

        if type(user_data) == list:
            for i, user in enumerate(user_data):
                if user["username"] == username_to_delete:
                    user_data.pop(i)
                    save_users(user_data)

                    for i, row in enumerate(data):
                        if i > 0 and row[0] == username_to_delete:
                            data.pop(i)
                            break
                    table.update_values(data)

                    entry_delete_username.delete(0, 'end')
                    CTkMessagebox(title="Success", message="User deleted successfully!", icon="check")
                    return

            CTkMessagebox(title="Error", message="User not found!", icon="cancel")

    button_delete_user = ctk.CTkButton(frame_log_form, text='Delete User', command=delete_user, width=200)
    button_delete_user.pack(pady=10)

    def logout():
        frame_log_form.pack_forget()
        switch_to_login()

    button_logout = ctk.CTkButton(frame_log_form, text='Logout', command=logout, width=200)
    button_logout.pack(pady=10)


def switch_to_login():
    def check():
        username = entry_login.get()
        password = entry_login_2.get()
        try:
            with open('register_form.json', 'r') as json_file:
                register_data = json.load(json_file)

            if type(register_data) == dict:
                if username == register_data.get('username') and password == register_data.get('password'):
                    CTkMessagebox(title="Success", message="Login successful!", icon="check")
                    switch_to_log_form(username, password, frame_login)
                else:
                    CTkMessagebox(title="Error", message="Incorrect username or password!", icon="cancel")
            elif type(register_data) == list:
                user_found = False
                for user in register_data:
                    if username == user.get('username') and password == user.get('password'):
                        CTkMessagebox(title="Success", message="Login successful!", icon="check")
                        switch_to_log_form(username, password, frame_login)
                        user_found = True
                        break
                if not user_found:
                    CTkMessagebox(title="Error", message="Incorrect username or password!", icon="cancel")
            else:
                CTkMessagebox(title="Error", message="Invalid user data format!", icon="cancel")
        except FileNotFoundError:
            CTkMessagebox(title="Error", message="No registered user found!", icon="cancel")
        except json.JSONDecodeError:
            CTkMessagebox(title="Error", message="User data file is corrupted!", icon="cancel")

    frame_login = ctk.CTkFrame(root)
    frame_login.pack(fill='both', expand=True)

    l1_login = ctk.CTkLabel(frame_login, text='Login')
    l1_login.pack(pady=10)

    entry_login = ctk.CTkEntry(frame_login, placeholder_text='Username')
    entry_login.pack()

    entry_login_2 = ctk.CTkEntry(frame_login, placeholder_text='Password', show="*")
    entry_login_2.pack(pady=10)

    button_login_1 = ctk.CTkButton(frame_login, text='Login', command=check)
    button_login_1.pack()

    button_login_2 = ctk.CTkButton(frame_login, text='Register', command=lambda x=frame_login: switch_to_register(x))
    button_login_2.pack(pady=10)


switch_to_login()

root.mainloop()