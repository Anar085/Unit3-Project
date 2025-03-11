import sqlite3
import threading
from datetime import datetime
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.toast import toast
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import MDScreen
from secure_password import encrypt_password, check_hash2
from kivymd.uix.list import  OneLineIconListItem
from my_lib import Database_Manager
from kivy.uix.widget import Widget
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import *
from kivy.graphics import Color, Rectangle, Line, Ellipse
from kivy.uix.label import Label
from kivymd.uix.button import MDRaisedButton
from kivymd.app import MDApp
from kivy.properties import StringProperty


#Login and Register
class LoginScreen(MDScreen):
    current_user=None
    current_role=None

    def try_login(self):
        username=self.ids.username_login.text
        password=self.ids.password_login.text
        if not username or not password:
            self.ids.login_error.text="Please enter both username and password"
            return
        db=Database_Manager('pos.db')
        search_user=f"SELECT * FROM users where username='{username}'"
        user_info=db.search_one(search_user)
        db.close()
        if user_info and check_hash2(password,user_info[2]):
            LoginScreen.current_user=user_info[1]
            LoginScreen.current_role=user_info[3]
            if user_info[3].lower()=="waiter":
                self.manager.current="Waiter_Inside"
            else:
                self.manager.current="Admin_Inside"
        else:
            self.ids.login_error.text="Invalid credentials"
    def clear_errors(self):
        self.ids.username_login.error=False
        self.ids.password_login.error=False

class RegisterScreen(MDScreen):
    def try_register(self):
        username=self.ids.username_reg.text.strip()
        password1=self.ids.password_reg.text.strip()
        password2=self.ids.password_check_reg.text.strip()
        role=self.ids.dropdown_reg.text.strip()
        admin_code=self.ids.res_password.text.strip()
        self.clear_errors()
        if not username:
            self.ids.username_reg.error=True
            self.ids.username_reg.helper_text="Username cannot be empty"
            return
        if not password1:
            self.ids.password_reg.error=True
            self.ids.password_reg.helper_text="Password cannot be empty"
            return
        if not password2:
            self.ids.password_check_reg.error=True
            self.ids.password_check_reg.helper_text="Confirm password cannot be empty"
            return
        if password1!=password2:
            self.ids.password_check_reg.error=True
            self.ids.password_check_reg.helper_text="Passwords do not match"
            return
        if admin_code!="res2025":
            self.ids.res_password.error=True
            self.ids.reg_error.text="Invalid restaurant password"
            return
        if not role or role=="Select Role":
            self.ids.reg_error.text="Please select a role"
            return

        check_query=f"SELECT * FROM users WHERE username='{username}'"
        db=Database_Manager("pos.db")
        result=db.search_all(query=check_query)
        if len(result)>0:
            self.ids.username_reg.error=True
            self.ids.username_reg.helper_text="Username or email already exists"
            return
        if len(password1)*len(password2)*len(username)!=0:
            password_hash=encrypt_password(password1)
            insert_query=f"""INSERT INTO users (username, password, role) 
                                VALUES ('{username}','{password_hash}','{role}')"""
            db.run_save(query=insert_query)
            db.close()
            LoginScreen.current_user=username
            self.parent.current="LoginScreen"

    def create_role_menu(self, input_menu):
        role_items=[
            {"text":"Administrator"},
            {"text":"Waiter"}
        ]
        role_list=[]
        for item in role_items:
            role_dict={
                "text":item["text"],
                "viewclass":"OneLineListItem",
                "on_release":lambda x=item["text"]:self.button_pressed(x)
            }
            role_list.append(role_dict)

        self.role_menu=MDDropdownMenu(
            caller=input_menu,
            items=role_list,
            width_mult=3
        )
        self.role_menu.open()

    def button_pressed(self,role):
        self.ids.dropdown_reg.text=f"{role}"
        self.role_menu.dismiss()
    def clear_errors(self):
        self.ids.username_reg.error=False
        self.ids.password_reg.error=False
        self.ids.password_check_reg.error=False
