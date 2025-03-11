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

# custom buttons
class CustomRectButton(ButtonBehavior,Widget):
    text=StringProperty("Button")
    fill_color=ListProperty([0.8,0.8,0.8,1])
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            self.bg_color=Color(*self.fill_color)
            self.bg_rect=Rectangle()
            self.top_tab=Rectangle()
            self.bottom_tab=Rectangle()
            self.left_tab=Rectangle()
            self.right_tab=Rectangle()
            self.line_color=Color(0,0,0,1)
            self.line_main=Line()
            self.line_top=Line()
            self.line_bottom=Line()
            self.line_left=Line()
            self.line_right=Line()
        self.label=Label(text=self.text,font_size=30,color=(0,0,0,1),size_hint=(None,None))
        self.add_widget(self.label)
        self.bind(pos=self.update_graphics,size=self.update_graphics,text=self.update_text)
    def update_text(self,*args):
        self.label.text=self.text
        self.label.texture_update()
        self.label.size=self.label.texture_size
    def update_graphics(self, *args):
        #dimensions for the button body
        main_rect_width=100
        main_rect_height=60
        main_x=self.x+(self.width-main_rect_width)/2
        main_y=self.y+(self.height-main_rect_height)/2
        #dimensions for four small rectangles representin chairs
        tab_w,tab_h=20,20
        top_x=main_x+(main_rect_width-tab_w)/2
        top_y=main_y+main_rect_height
        bottom_x=top_x
        bottom_y=main_y-tab_h
        left_x=main_x-tab_w
        left_y=main_y+(main_rect_height-tab_h)/2
        right_x=main_x+main_rect_width
        right_y=left_y
        #background shapes
        self.bg_color.rgba=self.fill_color
        self.bg_rect.pos=(main_x,main_y)
        self.bg_rect.size=(main_rect_width,main_rect_height)
        self.top_tab.pos=(top_x,top_y)
        self.top_tab.size=(tab_w,tab_h)
        self.bottom_tab.pos=(bottom_x,bottom_y)
        self.bottom_tab.size=(tab_w,tab_h)
        self.left_tab.pos=(left_x,left_y)
        self.left_tab.size=(tab_w,tab_h)
        self.right_tab.pos=(right_x,right_y)
        self.right_tab.size=(tab_w,tab_h)
        #outlines
        self.line_main.rectangle=(main_x,main_y,main_rect_width,main_rect_height)
        self.line_top.rectangle=(top_x,top_y,tab_w,tab_h)
        self.line_bottom.rectangle=(bottom_x,bottom_y,tab_w,tab_h)
        self.line_left.rectangle=(left_x,left_y,tab_w,tab_h)
        self.line_right.rectangle=(right_x,right_y,tab_w,tab_h)
        #putting label to the center
        self.label.texture_update()
        self.label.size=self.label.texture_size
        self.label.center=(self.x+self.width/2,self.y+self.height/2)
    def on_press(self):
        print(f"Rectangular table button's text:{self.text}")

class CustomCircleButton(ButtonBehavior,Widget):
    text=StringProperty("Button")
    fill_color=ListProperty([0.8,0.8,0.8,1])
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            self.bg_color=Color(*self.fill_color)
            self.bg_ellipse=Ellipse()
            self.tab_top=Rectangle()
            self.tab_bottom=Rectangle()
            self.tab_left=Rectangle()
            self.tab_right=Rectangle()
            self.line_color=Color(0,0,0,1)
            self.line_ellipse=Line()
            self.line_top=Line()
            self.line_bottom=Line()
            self.line_left=Line()
            self.line_right=Line()
        self.label=Label(text=self.text,font_size=30,color=(0,0,0,1),size_hint=(None,None))
        self.add_widget(self.label)
        self.bind(pos=self.update_graphics,size=self.update_graphics,text=self.update_text)
        
    def update_text(self,*args):
        self.label.text=self.text
        self.label.texture_update()
        self.label.size=self.label.texture_size
    def update_graphics(self,*args):
        #button body dimesions
        circle_diam=80
        circle_x=self.x+(self.width-circle_diam)/2
        circle_y=self.y+(self.height-circle_diam)/2
    
        #four rectangular chairs
        tab_w,tab_h=20,20
        top_x=self.x+(self.width-tab_w)/2
        top_y=circle_y+circle_diam
        bottom_x=top_x
        bottom_y=circle_y-tab_h
        left_x=circle_x-tab_w
        left_y=self.y+(self.height-tab_h)/2
        right_x=circle_x+circle_diam
        right_y=left_y
        
        #place ellipse and chairs correctly
        self.bg_color.rgba=self.fill_color
        self.bg_ellipse.pos=(circle_x,circle_y)
        self.bg_ellipse.size=(circle_diam,circle_diam)
        self.tab_top.pos=(top_x,top_y)
        self.tab_top.size=(tab_w,tab_h)
        self.tab_bottom.pos=(bottom_x,bottom_y)
        self.tab_bottom.size=(tab_w,tab_h)
        self.tab_left.pos=(left_x,left_y)
        self.tab_left.size=(tab_w,tab_h)
        self.tab_right.pos=(right_x,right_y)
        self.tab_right.size=(tab_w,tab_h)
        
        #outlines
        self.line_ellipse.ellipse=(circle_x,circle_y,circle_diam,circle_diam)
        self.line_top.rectangle=(top_x,top_y,tab_w,tab_h)
        self.line_bottom.rectangle=(bottom_x,bottom_y,tab_w,tab_h)
        self.line_left.rectangle=(left_x,left_y,tab_w,tab_h)
        self.line_right.rectangle=(right_x,right_y,tab_w,tab_h)
        #put label to center
        self.label.texture_update()
        self.label.size=self.label.texture_size
        self.label.center=(self.x+self.width/2,self.y+self.height/2)
    def on_press(self):
        print(f"Circle button's text:{self.text}")

#Dialog
class QuantityDialog(MDBoxLayout):
    food_name=StringProperty("")
    food_price=StringProperty("")
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.ids.quantity_input.text="1"
    def validate_quantity(self):
        try:
            quantity=int(self.ids.quantity_input.text)
            if quantity<=0:
                return False,"Quantity must be positive"
            return True,quantity
        except ValueError:
            return False,"Quantity must be a number"
