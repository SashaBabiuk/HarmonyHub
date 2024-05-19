from kivymd.uix.dialog import MDDialog
from datetime import date
from harmonyHubDBConnect import cur, conn
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.screen import MDScreen
import re

Builder.load_file('style/registrationform.kv')

class RegistrationForm(MDScreen):
    def signUp(self):
        # Використання об'єкта курсора та підключення до бази даних
        cur.execute("SELECT COUNT(*) FROM person;")
        user_id = cur.fetchone()[0] + 1
        name_user = self.ids.name_user.text
        surname = self.ids.surname.text
        nickname = self.ids.nickname.text
        gender = self.ids.gender.text
        birthday = self.ids.birthday.text
        email = self.ids.email.text
        password = self.ids.password.text
        confirm_password = self.ids.confirm_password.text
        registration_date = date.today().strftime("%Y-%m-%d")

        if any(self.has_cyrillic(field) for field in
               [name_user, surname, nickname, gender, birthday, email, password, confirm_password]):
            self.show_dialog("Please use only Latin characters in all fields.")
            return

        if password == confirm_password and all([name_user, surname, email, password, confirm_password]):
            cur.execute("""
            INSERT INTO person(user_id, username, email, password, registration_date, type_id, settings_id, user_favorite_artist, user_favorite_group)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (user_id, nickname, email, password, registration_date, 1,user_id, 1, 1))
            conn.commit()
        else:
            self.show_dialog("Passwords do not match or some fields are empty.")

    def show_dialog(self, text):
        dialog = MDDialog(
            text=text,
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def has_cyrillic(self, text):
        return bool(re.search('[а-яА-Я]', text))
