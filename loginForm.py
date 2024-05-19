from kivymd.uix.dialog import MDDialog
from harmonyHubDBConnect import cur, conn
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.screen import Screen
import re

Builder.load_file('style/loginform.kv')


class LoginForm(Screen):

    email = ""
    password = ""

    def logIn(self):
        email = self.ids.email.text
        password = self.ids.password.text
        app = MDApp.get_running_app()

        if self.has_cyrillic(email) or self.has_cyrillic(password):
            self.show_dialog("Please use only Latin characters for email and password.")
            return

        cur.execute("SELECT user_id FROM person WHERE email=? AND password=?", (email, password,))
        result = cur.fetchone()

        if result:
            user_id = result[0]
            app.switch_to_main()
        else:
            self.show_dialog("User not found or incorrect password")

        conn.commit()

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