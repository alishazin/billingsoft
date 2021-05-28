
# importing kivy and kivymd modules

from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import NoTransition, FadeTransition
from kivymd.uix.card import MDCard
from timeit import default_timer as timer  
from kivymd.uix.behaviors import HoverBehavior
from kivymd.theming import ThemableBehavior
from kivy.properties import StringProperty, BooleanProperty, NumericProperty
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.button import (MDFillRoundFlatButton, MDIconButton, MDRaisedButton, MDTextButton, MDFlatButton, MDRoundFlatButton)
from kivy.uix.modalview import ModalView, AnchorLayout
from kivymd.uix.behaviors import RectangularElevationBehavior, CircularRippleBehavior, CircularElevationBehavior, FocusBehavior
from kivy.uix.behaviors import ButtonBehavior
from kivy import utils
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.clock import Clock
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list import OneLineListItem, TwoLineListItem, ThreeLineListItem, MDList
from kivy.uix.textinput import TextInput
from kivymd.uix.dialog import MDDialog
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.menu import MDDropdownMenu 
from kivymd.uix.dropdownitem import MDDropDownItem
from kivymd.uix.tooltip import MDTooltip
from kivy.uix.recycleview import RecycleView
from kivy.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.popup import Popup
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.snackbar import BaseSnackbar
from kivymd.toast import toast

# importing libraries other than kivy and kivymd

import sqlite3

import tkinter

import pandas as pd 

import re

import datetime

import os 

import time

import csv

import json

from threading import Thread

import matplotlib.pyplot as plt
import numpy as np

# recycleview and item in bin screen

class RecycleListItemBackup(MDCard):
    text = StringProperty()
    sec_text = StringProperty()
    ter_text = StringProperty()

class RecycleListItemPricedetails(MDCard):
    name = StringProperty()
    code = StringProperty()

# recycleview and item in class ModalPriceDetails

class RVPriceDetails(RecycleView):
    def update(self,matched_list):
        self.data = [{ 'name':i[0], 'code':f'Item Code : {i[1]}'} for i in matched_list]

class RVBackup(RecycleView):
    def update(self,list_):
        list_.reverse()
        self.data = [{'text' : str(i[0]),'sec_text' : f'{str(i[1])} ₹ Per {str(i[2])}','ter_text' : f'Item Code: {str(i[3])}'} for i in list_ ]

# recycleview and item in billing screen (search product name)

class RecycleListItem(MDCard):
    text = StringProperty()

class RV(RecycleView):
    def update(self,matched_list):
        matched_list.reverse()
        self.data = [{'text' : f'  {str(i)}'} for i in matched_list]

# recycleview and item in class CusDetailsSearch

class RecycleListItem2(MDCard):
    text = StringProperty()

class RV2(RecycleView):
    def update(self,matched_list):
        matched_list.reverse()
        self.data = [{'text' : f'  {str(i)}'} for i in matched_list]

# recycleview and item in db screen

class RecycleListItemdb(MDCard):
    text = StringProperty()
    sec_text = StringProperty()
    ter_text = StringProperty()

class RVdb(RecycleView):
    def update(self,list_):
        list_.reverse()
        self.data = [{'text' : str(i[0]),'sec_text' : f'{str(i[1])} ₹ Per {str(i[2])}','ter_text' : f'Item Code: {str(i[3])}'} for i in list_ ]

# recycleview and item in class CusContactnoSearch

class RecycleListItem3(MDCard):
    text = StringProperty()

class RV3(RecycleView):
    def update(self,matched_list):
        matched_list.reverse()
        self.data = [{'text' : f'  {str(i)}'} for i in matched_list]

# recycleview and item in customer info screen

class RecycleListItemcus(MDCard):
    name = StringProperty()
    phno = StringProperty()

class RVcus(RecycleView):
    def update(self,matched_list):
        matched_list.reverse()
        self.data = [{'name': str(i[0]),'phno': str(i[1])} for i in matched_list ]

# recycleview and item in bill details screen

class RecycleListItemBillDetails(MDCard):
    name = StringProperty()
    phno = StringProperty()
    timedate = StringProperty()
    total = StringProperty()

class RVbilldetails(RecycleView):
    def update(self,matched_list):
        matched_list.reverse()
        self.data = [{'name': f'[color=#808080]Bill No:[/color]  {str(i[0])}', 'phno': f'[color=#808080]Contact No:[/color]  {str(i[1])}' , 'timedate': f'[color=#808080]Date:[/color]  {str(i[3])}', 'total': f'[color=#808080]Total:[/color]  {str(i[2])} ₹' } for i in matched_list]

# popup screen after pressing graph screen buttons (for graph customization)

class ModalPopularDay(ModalView):
    pass

class ModalPopularTime(ModalView):
    pass

class ModalPriceDetails(ModalView):
    def on_pre_open(self):
        conn = sqlite3.connect('BillSoft.db')
        c = conn.cursor()

        c.execute('SELECT * FROM prodetailsdb')
        check_db = c.fetchall()
        matched_list = []
        for i in check_db:
            temp_list = []
            temp_list.append(i[0])
            temp_list.append(i[3])
            matched_list.append(temp_list)
        
        conn.commit()
        conn.close()

        self.ids.rv.update(matched_list)

class ModalEarnedProduct(ModalView):
    pass

class ModalSoldProduct(ModalView):
    pass

class ModalCusVisit(ModalView):
    pass

class ModalMoneySpend(ModalView):
    pass

# layout opened at the time of searching customer name in billing screen

class CusDetailsSearch(MDRelativeLayout):
    pass

# layout opened at the time of searching customer contact number in billing screen

class CusContactnoSearch(MDRelativeLayout):
    pass

# snackbar appeared after adding or deleting products

class CustomSnackbar(BaseSnackbar):
    text = StringProperty()
    icon = StringProperty()

# colorful button in graph screen 

class GraphMDCard(MDCard, HoverBehavior):
    def on_enter(self):
        self.parent.padding = 0

    def on_leave(self):
        self.parent.padding = 7

# Kivy Widgets with HoverBehavior and/or ThemableBehavior

class FocusMDCheckbox(MDCheckbox, ThemableBehavior, HoverBehavior):
    def on_enter(self):
        self.opacity = .7
    
    def on_leave(self):
        self.opacity = 1

class FocusMDRoundFlatButton(MDRoundFlatButton, ThemableBehavior, HoverBehavior):
    def on_enter(self):
        self.line_width = 2

    def on_leave(self):
        self.line_width = 1

class FocusMDIconButton(MDIconButton, ThemableBehavior, HoverBehavior):
    def on_enter(self):
        self.opacity = .5

    def on_leave(self):
        self.opacity = 1

class FocusMDTextButton(MDTextButton,ThemableBehavior,HoverBehavior):
    def on_enter(self):
        self.underline = True

    def on_leave(self):
        self.underline = False

class FocusMDRaisedButton(MDRaisedButton, ThemableBehavior, HoverBehavior):
    def on_enter(self):
        self.opacity = .5

    def on_leave(self):
        self.opacity = 1

class FocusMDDropDownItem(MDDropDownItem, ThemableBehavior, HoverBehavior):
    def on_enter(self):
        self.opacity = .7

    def on_leave(self):
        self.opacity = 1

class FocusMDFillRoundFlatButton(MDFillRoundFlatButton, HoverBehavior):
    def on_enter(self):
        self.opacity = 1

    def on_leave(self):
        self.opacity = 1.5

class FocusMDIconButton(MDIconButton, ThemableBehavior, HoverBehavior):
    def on_enter(self):
        self.opacity = 1

    def on_leave(self):
        self.opacity = 1.5

# textinput(grid) in billing screen edited for recogonising arrow inputs

class ArrowSensitiveTextInput(TextInput):

    def move_right(self):
        for i in self_list2.children:
            if i.ids.inp.r == self.r:
                i.ids.inp.focus = True
        application.list_cursor.append(2)

    def move_left(self):
        for i in self_list1.children:
            if i.ids.inp.r == self.r:
                i.ids.inp.focus = True
        application.list_cursor.append(1)

    def keyboard_on_key_up(self, window, keycode):
        key, key_str = keycode
        k = self.interesting_keys.get(key)
        if k:
            key = (None, None, k, 1)
            self._key_up(key)

        if keycode == (274, 'down'):
            list_of_self1 = list(self.parent.parent.parent.children)
            for i in list_of_self1:
                if i.ids.inp.r == self.r + 1:
                    i.ids.inp.focus = True
            if self.c == 0:
                application.list_cursor.append(1)
            else:
                application.list_cursor.append(2)

        if keycode == (273, 'up'):
            list_of_self2 = list(self.parent.parent.parent.children)
            for i in list_of_self2:
                if i.ids.inp.r == self.r - 1:
                    i.ids.inp.focus = True

        if keycode == (275, 'right'):
            if len(self.text) == 0:
                if self.c == 0:
                    self.move_right()
            else:
                if self.cursor[0] == len(self.text):
                    application.list_cursor.append(1)
                    if application.list_cursor[-1] == 1 and application.list_cursor[-2] == 1:
                        self.move_right()
                else:
                    application.list_cursor.append(0)

        if keycode == (276, 'left'):
            if len(self.text) == 0:
                self.move_left()
            else: 
                if self.cursor[0] == 0:
                    application.list_cursor.append(2)
                    if application.list_cursor[-1] == 2 and application.list_cursor[-2] == 2:
                        self.move_left()
                else:
                    application.list_cursor.append(0)

# 1st column of the grid in billing screen 

class ProNameListItem(MDCard):
    text = StringProperty()
    focus_ = BooleanProperty()
    row = NumericProperty()

# 2nd column of the grid in billing screen 

class QtyListItem(MDCard):
    text = StringProperty()
    focus_ = BooleanProperty()
    row = NumericProperty()

# toolbar on the left item and layout

class LeftLayoutItem(MDIconButton, ThemableBehavior, HoverBehavior):
    def on_enter(self):
        self.user_font_size = 30

    def on_leave(self):
        self.user_font_size = 25

class LeftLayout(MDRelativeLayout, ThemableBehavior, HoverBehavior, RectangularElevationBehavior):
    def on_enter(self):

        animate1 = Animation(
            elevation = 30,
            md_bg_color = utils.get_color_from_hex('#61D5D2'),
            duration = .12
        )

        animate1.start(self)

    def on_leave(self):

        a = application()
        a.theme_cls.primary_palette = 'Cyan'

        animate_back1 = Animation(
            elevation = 5,
            md_bg_color = a.theme_cls.primary_color,
            duration = .12
        )

        animate_back1.start(self)

# ModalView with spinner after sign up

class SpinnerModal(ModalView):
    def on_pre_open(self):
        self.auto_dismiss = False
        self.background = ''
        self.background_color = utils.get_color_from_hex('#FFFFFF')
        self.size_hint = .35,.2
        self.pos_hint = {'center_x': .6, 'center_y': .5}

# close button layout in all the close button with ModalView

class BillCloseButton(CircularElevationBehavior,MDRelativeLayout):
    pass

# ModalView with spinner short version after log in 

class SpinnerModalShort(ModalView):
    def on_pre_open(self):
        self.auto_dismiss = False
        self.background = ''
        self.background_color = utils.get_color_from_hex('#FFFFFF')
        self.size_hint = .1,.1
        self.pos_hint = {'center_x': .6, 'center_y': .5}

# ModalView used while loading graphs

class LoadingView(ModalView):
    pass

# ModalView used after generating bill

class FullScreenBillView(ModalView):
    text_ = StringProperty()
    text1 = StringProperty()
    text2 = StringProperty()
    text3 = StringProperty()

    def on_pre_open(self):
        self.ids.anim_butt.icon = 'database'
        self.ids.add_db_butt.disabled = False

# ModalView used for reviewing bill in bill screen

class FullScreenBillReview(ModalView):
    text_ = StringProperty()
    text1 = StringProperty()
    text2 = StringProperty()
    text3 = StringProperty()

# ModalView used for showing customer location in customer info screen

class LocationDetails(ModalView):
    name = StringProperty()
    phno = StringProperty()
    loc = StringProperty()

# textfield with hide password used in log in and sign in screen's

class ClickableTextFieldRound(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()

# jumping icon of database in class FullScreenBillView

class AnimMDIconIconButton(MDIconButton):
    def start_anim(self):

        def anim2(interval):
            animate2.start(self)

        def anim3(interval):
            animate3.start(self)

        def anim4(interval):
            self.icon = 'database'
            self.theme_text_color = 'Custom'
            self.text_color = self.theme_cls.primary_color

        animate1 = Animation(
            pos_hint = {'center_x':.9,'center_y': .06},
            duration = .2
        )

        animate2 = Animation(
            pos_hint = {'center_x':.9,'center_y': .01},
            duration = .2
        )

        animate3 = Animation(
            pos_hint = {'center_x':.9,'center_y': .045},
            duration = .2
        )

        animate1.start(self)
        Clock.schedule_once(anim2, .2)
        Clock.schedule_once(anim3, .4)
        Clock.schedule_once(anim4, .6)

# used in log in and sign in screens for showing app icon in the middle and for reducing its opacity

class LoginCard(MDCard, HoverBehavior):
    def on_enter(self):
        self.elevation = 20

    def on_leave(self):
        self.elevation = 10

# main app class
# most of the functions are from this class

class application(MDApp):

    # initialisation of variable's used
    list_cursor = [0,0]
    login = False
    check_occurence_db = 'packet'
    search_for_in_db = 'Products'
    cus_info_search = 'Name'
    bill_details_search = 'Bill No'
    rv_busy = False
    bill_proname_search_cursor = None

    # database initialisation:
    conn = sqlite3.connect('BillSoft.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS security(
            username text,
            password text
            )''')
    c.execute("SELECT *,oid FROM security")
    security_check_db1 = c.fetchall()
    if len(security_check_db1) == 0: 
        sign_up = False
    else:
        sign_up = True

    c.execute('''CREATE TABLE IF NOT EXISTS prodetailsdb(
            name text PRIMARY KEY,
            price float,
            qty text,
            code text
            )''')
    c.execute('''CREATE TABLE IF NOT EXISTS overallproname(
            count text
            )''')
    c.execute('''CREATE TABLE IF NOT EXISTS overallbillno(
            count text
            )''')
    c.execute('''CREATE TABLE IF NOT EXISTS billdetails(
            con_no text,
            total text,
            bill_no text
            )''')
    c.execute('''CREATE TABLE IF NOT EXISTS cusdetails(
            name text,
            phno text PRIMARY KEY,
            location text
            )''')
    c.execute("SELECT *,oid FROM overallproname")
    check_count = c.fetchall()
    if len(check_count) == 0:
        c.execute("INSERT INTO overallproname VALUES ('0')")
    else:
        pass

    c.execute("SELECT *,oid FROM overallbillno")
    check_count2 = c.fetchall()
    if len(check_count2) == 0:
        c.execute("INSERT INTO overallbillno VALUES ('1')")
    else:
        pass

    conn.commit()
    conn.close()

    # other files where data is stored, Their initialisation
    if os.path.exists('backup.csv') == False:
        file_create = open('backup.csv','w')
        file_create.close()
    else:
        pass 

    if os.path.exists('ptracker.csv') == False:
        file_create2 = open('ptracker.csv','w')
        file_create2.close()
    else:
        pass

    if os.path.exists('billextra.json') == False:
        dict_start = {
            'bill' : {},
            'timedate' : {}
        }
        file_create3 = open('billextra.json','w')
        json.dump(dict_start,file_create3)
        file_create3.close()
    else:
        pass

    def build(self):
        self.screen = Builder.load_file('main.kv')
        self.theme_cls.primary_palette = 'Cyan'
        self.title = 'Billing Software'
        self.icon = 'img.png'
        return self.screen

    def on_start(self):
        if self.sign_up == False:
            self.screen.ids.screen_manager.transition = NoTransition()
            self.screen.ids.screen_manager.current = 'sign up screen'
            self.screen.ids.username_.focus = True
        else:
            self.screen.ids.screen_manager.transition = NoTransition()
            self.screen.ids.screen_manager.current = 'log in screen'
            self.screen.ids.username.focus = True

        global self_list1
        global self_list2

        self_list1 = self.screen.ids.pro_name
        self_list2 = self.screen.ids.qty

        self.backslah_warn = MDDialog(
            text='[color=#000000]Usage of backslash(\) can crash the application, so please dont use backslash while adding products or entering any details[/color]',
            buttons= [
                FocusMDRaisedButton(
                    text='GOT IT',
                    on_release= lambda x : self.dismiss_warning()
                )
            ] 
        )

        self.additional_wid = CusDetailsSearch()
        self.screen.ids.main_lay_bill.add_widget(
            self.additional_wid
        )

        self.additional_wid2 = CusContactnoSearch()
        self.screen.ids.main_lay_bill.add_widget(
            self.additional_wid2
        )

    def sign_up_(self,username,password,cpassword):

        def username_space_check(text):
            text_before = text
            text_test = text
            text_after = text_test.replace(' ','*')
            if text_before == text_after:
                return True
            else:
                return False

        if len(username.strip()) == 0 or len(password.strip()) == 0 or len(cpassword.strip()) == 0:
            pass
        else:
            if username_space_check(username) == True:
                if len(password) > 5:
                    if password == cpassword:
                        self.screen.ids.errors_pass.text = ''
                        keyword = f"INSERT INTO security VALUES ('{username}','{password}')"
                        conn = sqlite3.connect('BillSoft.db')
                        c = conn.cursor()
                        c.execute("SELECT *,oid FROM security")
                        c.execute(keyword)
                        conn.commit()
                        conn.close()
                        spinnerpopup = SpinnerModal()
                        spinnerpopup.open()
                    else:
                        self.screen.ids.errors_pass.text =  "* Password confirmation failed "
                        return 
                else:
                    self.screen.ids.errors_pass.text =  "* Password should contain more than 5 characters "
                    return
            else:
                self.screen.ids.errors_pass.text =  "* username should not contain space "
                return

    def log_in(self, username, password):

        def child_func(interval):
            spinnershort.dismiss()
            self.screen.ids.welcome_text.text = f'Welcome Back, {username_glob}'
            self.screen.ids.screen_manager.transition = FadeTransition()
            self.screen.ids.screen_manager.transition.clearcolor = 1,1,1,1
            self.screen.ids.screen_manager.current = 'splash screen'
            self.login = True

        if len(username) == 0 or len(password) == 0:
            pass
        else:
            conn = sqlite3.connect('BillSoft.db')
            c = conn.cursor()
            c.execute("SELECT *,oid FROM security")
            check_db = c.fetchall()
            username_org = check_db[0][0]
            password_org = check_db[0][1]

            if username_org == username:
                if password_org == password:
                    username_glob = username
                    spinnershort = SpinnerModalShort()
                    spinnershort.open()
                    Clock.schedule_once(child_func, .5)
                else:
                    self.screen.ids.errors_pass2.text = '* Incorrect password '
                    return
            else:
                self.screen.ids.errors_pass2.text = '* Incorrect username '
                return

            conn.commit()
            conn.close()

    def left_layout_press(self,master,obj,name):
        if self.login == True:
            for i in master.children:
                i.theme_text_color = 'Custom'
                i.text_color = 0,0,0,1
                
            obj.theme_text_color = 'Custom'
            obj.text_color = 1,1,1,1
            self.screen.ids.screen_manager.transition = FadeTransition()
            self.screen.ids.screen_manager.transition.clearcolor = 1,1,1,1
            self.screen.ids.screen_manager.current = name
        else:
            pass

    def filter_caps(self,text,obj):
        obj.text = text.upper()

    def bill_screen_enter(self):
        conn = sqlite3.connect('BillSoft.db')
        c = conn.cursor()
        c.execute('SELECT *,oid FROM overallbillno')
        check_db = c.fetchall()
        self.screen.ids.cus_bill_no.text = check_db[0][0]
        conn.commit()
        conn.close()
        test_list = list(self.screen.ids.qty.children)
        if len(test_list) == 0:
            self.row_no = 0
            self.screen.ids.qty.add_widget(
                QtyListItem(row=0)
            )
            self.screen.ids.pro_name.add_widget(
                ProNameListItem(row=0)
            )
            self.screen.ids.cus_name.focus = True
        else:
            pass

    def from_pro_to_qty(self,obj):
        listitem = obj.parent.parent
        pro_name_list = list(obj.parent.parent.parent.children)
        count = 0
        for i in pro_name_list:
            if i == listitem:
                break
            count += 1

        qty_list = self.screen.ids.qty.children
        count2 = 0
        for i in qty_list:
            if count2 == count:
                i.ids.inp.focus = True
                break
            count2 += 1

    def from_qty_to_pro(self,obj):
        if obj.a == 0:
            self.row_no += 1
            self.screen.ids.qty.add_widget(
                QtyListItem(row=self.row_no)
            )

            self.screen.ids.pro_name.add_widget(
                ProNameListItem(focus_=True,row=self.row_no)
            )
            obj.a = 1
        else:
            listitem = obj.parent.parent
            qty_list = list(obj.parent.parent.parent.children)
            qty_list.reverse()
            count = 0
            for i in qty_list:
                if i == listitem:
                    break
                count += 1
            
            pro_name_list = list(self.screen.ids.pro_name.children)
            pro_name_list.reverse()
            count2 = 0
            for i in pro_name_list:
                if count2 == count + 1:
                    i.ids.inp.focus = True
                    break
                count2 += 1

    def from_con_no_to_bill(self):
        list_of_self = list(self.screen.ids.pro_name.children) 
        list_of_self.reverse()
        for i in list_of_self:
            i.ids.inp.focus = True
            break

    def when_check_clicked_db(self,checkbox,value,id_,text_self):
        if value == False:
            text_self.color = 0,0,0,1
            self.check_occurence_db = ''
        if value == True:
            self.check_occurence_db = id_

    def dismiss_quotes_warning(self):
        self.quotes_warning.dismiss()
    
    def add_new_item_db(self,proname,price):
        try:
            if float(price) > 0:
                pass
            else:
                return
        except:
            return
        check_back_slash = '\\' in proname
        check_quotes = "'" in proname or '''"''' in proname
        if len(proname.strip()) == 0 or len(price) == 0 or self.check_occurence_db == '':
            pass
        elif check_back_slash == True:
            self.refresh_db_screen(1)
            self.backslah_warn.open()
        elif check_quotes:
            self.refresh_db_screen(1)
            self.quotes_warning = MDDialog(
                text = """[color=#000000]Please avoid the usage of (') and (") while adding products[/color]""",
                buttons = [
                    FocusMDRaisedButton(
                        text = 'GOT IT',
                        on_release = lambda x: self.dismiss_quotes_warning()
                    )
                ] 
            )
            self.quotes_warning.open()
        else:
            conn = sqlite3.connect('BillSoft.db')
            c = conn.cursor()
            c.execute('SELECT *,oid FROM overallproname')
            check_ovr_db = c.fetchall()
            latest_code = int(check_ovr_db[0][0])
            c.execute('SELECT *,oid FROM prodetailsdb')
            keyword = f"INSERT INTO prodetailsdb VALUES ('{proname.strip()}','{float(price)}','{self.check_occurence_db}','{latest_code + 1}')"
            try:
                c.execute(keyword)
                mini_keyword = f"UPDATE overallproname SET count = '{latest_code + 1}' WHERE oid = 1"
                c.execute('SELECT *,oid FROM overallproname')
                c.execute(mini_keyword)
            except sqlite3.IntegrityError:
                self.unique_proname = MDDialog(
                    type = 'alert',
                    text = '[color=#000000]Product Name is Common, Try Changing It[/color]',
                    buttons=[
                        FocusMDRaisedButton(
                            text='GOT IT',on_release= lambda x: self.dismiss_unique_proname_dialog()
                        )
                    ]
                )
                self.unique_proname.open()
            else:
                self.snackbar_conf_add = CustomSnackbar(
                    text = f'Product {proname.strip()} is Added',
                    size_hint = (1,.05),
                    snackbar_x="10",
                    snackbar_y="10",
                    radius = [10,10,10,10],
                    icon = 'information',
                    duration = 2
                )
                self.snackbar_conf_add.size_hint_x = (
                    Window.width - (self.snackbar_conf_add.snackbar_x * 2)
                ) / Window.width
                self.snackbar_conf_add.open()
                self.refresh_db_screen(1)
                self.write_price_to_csv(float(price),latest_code + 1)
            finally:
                conn.commit()
                conn.close()

    def dismiss_unique_proname_dialog(self):
        self.unique_proname.dismiss()

    def refresh_db_screen(self,instance):

        if instance == 1:
            self.screen.ids.proname.text = ''
            self.screen.ids.price_.text = ''
            self.screen.ids.check_pck.active = True
            self.screen.ids.check_kg.active = False

    def delete_from_db_conf(self,name):
        self.curr_delete_proname = name
        self.conf_delete_dialog = MDDialog(
            text = f'[color=#000000]Delete {name} ?[/color]',
            buttons = [
                MDFlatButton(
                    text = 'Cancel',
                    on_release = lambda x : self.conf_delete_dialog_dismiss()
                ),
                FocusMDRaisedButton(
                    text = 'Delete',
                    on_release = lambda x : self.delete_from_db()
                )
            ]
        )
        self.conf_delete_dialog.open()

    def conf_delete_dialog_dismiss(self):
        self.conf_delete_dialog.dismiss()

    def write_onto_backup_csv(self,list_):
        with open('backup.csv','at') as file_:
            csv_writer = csv.writer(file_)
            csv_writer.writerow(list_)

    def delete_from_db(self):
        self.conf_delete_dialog.dismiss()
        name = self.curr_delete_proname
        self.delete_conf_snackbar = CustomSnackbar(
            text = f'Product {name} is deleted Successfully',
            size_hint = (1,.05),
            snackbar_x="10",
            snackbar_y="10",
            radius = [10,10,10,10],
            icon = 'information',
            duration = 2
        )
        self.delete_conf_snackbar.size_hint_x = (
            Window.width - (self.delete_conf_snackbar.snackbar_x * 2)
        ) / Window.width
        self.delete_conf_snackbar.open()

        conn = sqlite3.connect('BillSoft.db')
        c = conn.cursor()

        c.execute('SELECT *,oid FROM prodetailsdb')
        minidb_check = c.fetchall()
        details_backup = ''
        for i in minidb_check:
            if i[0] == self.curr_delete_proname:
                details_backup = [i[0],i[1],i[2],i[3]]
        self.write_onto_backup_csv(details_backup)

        c.execute('SELECT *,oid FROM prodetailsdb')
        db_check = c.fetchall()
        for i in db_check:
            if i[0] == name:
                self.glob_proname = i[0]
                self.glob_price = i[1]
                self.glob_unit = i[2]

        keyword = f"DELETE FROM prodetailsdb WHERE name = '{name}'"
        c.execute(keyword)

        conn.commit()
        conn.close()

        self.db_screen_enter()

    def repeat_check_list(self,list_,instance=0):
        return_list = []
        for i in list_:
            if i not in return_list:
                return_list.append(i)
        if instance == 0:
            if return_list == list_:
                return True
            else:
                return False
        else:
            return return_list

    def generate_visual_bill(self,list1,list2,cus_name,cus_contact_no,cus_bill_no):
        self.curr_cus_name = cus_name
        self.curr_cus_contact_no = cus_contact_no
        self.curr_cus_bill_no = cus_bill_no
        if self.curr_cus_name.strip() == '' or self.curr_cus_contact_no.strip() == '' or self.curr_cus_bill_no.strip() == '':
            pass
        else: 
            proname_list = []
            list1_children = list(list1.children)
            list1_children.reverse()
            for i in list1_children:
                if len(i.ids.inp.text.strip()) != 0:
                    proname_list.append(i.ids.inp.text.strip())
                else:
                    proname_list.append(None)

            qty_list = []
            list2_children = list(list2.children)
            list2_children.reverse()
            for i in list2_children:
                if len(i.ids.inp.text.strip()) != 0:
                    qty_list.append(i.ids.inp.text.strip())
                else:
                    qty_list.append(None)

            bill_list = []
            for i in range(len(proname_list)):
                temp_list = [str(proname_list[i]),str(qty_list[i])]
                bill_list.append(temp_list)

            bill_proper = []
            error_list = [] # value recieved, recieved space, missing
            for pro,qt in bill_list:
                if pro == 'None' and qt == 'None':
                    pass
                elif pro != 'None' and qt != 'None':
                    bill_proper.append([pro,qt])
                else:
                    if pro == 'None':
                        error_list.append([qt,'Quantity','Product Name']) # appending available valuest o give error message
                    else:
                        error_list.append([pro,'Product Name','Quantity'])

            if error_list == []:
                self.screen.ids.bill_error_view.text = ''

                pro_only = []
                for pro,qty in bill_proper:
                    pro_only.append(pro)

                conn = sqlite3.connect('BillSoft.db')
                c = conn.cursor()
                c.execute('SELECT *,oid FROM prodetailsdb')
                check_db = c.fetchall()
                all_pro_name = []
                for i in check_db:
                    all_pro_name.append(i[0])

                conn.commit()
                conn.close()

                out_of_db_list = []
                for i in pro_only:
                    if i in all_pro_name:
                        pass
                    else:
                        out_of_db_list.append(i)

                if out_of_db_list == []:
                    self.screen.ids.bill_error_view.text = ''

                    if self.repeat_check_list(pro_only) == True:
                        self.screen.ids.bill_error_view.text = ''

                        self.start_db_check_bill(bill_proper)

                    else:
                        self.screen.ids.bill_error_view.text = '\nError:\nA Product Name is repeated'

                else:
                    error_str = ''
                    for i in self.repeat_check_list(out_of_db_list,1):
                        error_str += f',{i}'
                    error_str = error_str[1::]
                    self.screen.ids.bill_error_view.text = f'\nError:\nThe Following Product Names Are Invalid :- {error_str}'

            else:
                error_message = ''
                for i in error_list:
                    error_message += f"\nError:\nRecieved '{i[0]}' as {i[1]}, 'None' Recieved as {i[2]}\n"
                self.screen.ids.bill_error_view.text = error_message

    def dismiss_warning(self):
        self.backslah_warn.dismiss()

    def dismiss_rv2(self,obj,state):
        if state == False:
            self.additional_wid.ids.rv2.update([])
            self.additional_wid.size_hint = .001,.001
            self.screen.ids.cus_bill_no.disabled = False
            bill_main = list(self.screen.ids.pro_name.children)
            bill_main.reverse()
            count = 0
            for i in bill_main:
                if count == 2:
                    break
                i.disabled = False
                count += 1
        if state == True:
            if self.screen.ids.cus_name.text.strip() != '':
                self.customer_name_list_only(self.screen.ids.cus_name.text)

    def start_db_check_bill(self,bill):
        if len(bill) != 0:
            conn = sqlite3.connect('BillSoft.db')
            c = conn.cursor()

            for i in bill:
                keyword = f"SELECT * FROM prodetailsdb WHERE name = '{i[0]}'"
                c.execute(keyword)
                check_db = c.fetchall()
                i.append(check_db[0][1])
                i.append(check_db[0][2])
                
            approvalfinal = []
            for i in bill:
                approval1 = None
                if i[-1] == 'packet':
                    try:
                        if int(eval(i[1])) == float(i[1]):
                            approval1 = True
                    except:
                        self.screen.ids.bill_error_view.text = '\nError:\nQuantity is provided in a wrong format'
                        return
                    if approval1 == True:
                        if float(i[1]) > 0:
                            approvalfinal.append(1)
                        else:
                            approvalfinal.append(0)
                            self.screen.ids.bill_error_view.text = '\nError:\nQuantity should be a positive number'
                    else:
                        approvalfinal.append(0)
                        self.screen.ids.bill_error_view.text = '\nError:\nProducts referred to be sold as packets should not have non integers as quantity'
                    
                else:
                    if float(i[1]) > 0:
                        approvalfinal.append(1)
                    else:
                        self.screen.ids.bill_error_view.text = '\nError:\nQuantity should be a positive number'
                        approvalfinal.append(0)

            conn.commit()
            conn.close()

            self.final_customer_check(bill) if set(approvalfinal) == {1} else print()
        else:
            self.screen.ids.bill_error_view.text = '\nError:\nEmpty Bill'

    def final_customer_check(self,bill):
        self.temp_bill_space = bill
        conn = sqlite3.connect('BillSoft.db')
        c = conn.cursor()

        c.execute('SELECT * FROM cusdetails')
        check_phno = c.fetchall()
        new_cus = True
        other_errors = False
        for i in check_phno:
            if i[1] == self.curr_cus_contact_no.strip():
                if i[0] == self.curr_cus_name.strip():
                    new_cus = False
                else:
                    self.same_phno_diff_name = MDDialog(
                        text = '[color=#000000]A customer with same contact number already exist[/color]',
                        buttons = [
                            FocusMDRaisedButton(
                                text = 'GOT IT',
                                on_release = lambda x: self.dismiss_same_phno_diff_name()
                            )
                        ]
                    )
                    other_errors = True
                    self.same_phno_diff_name.open()
            else:
                pass
        conn.commit()
        conn.close()
        if other_errors == True:
            pass
        else:
            if new_cus == True:
                self.new_customer_to_db = MDDialog(
                    text = '[color=#000000]Cannot find a customer with given details, Assume he/she is a new one[/color]',
                    buttons = [
                        MDFlatButton(
                            text = 'Not New!',
                            on_release = lambda x: self.not_new()
                        ),
                        FocusMDRaisedButton(
                            text = 'New One',
                            on_release = lambda x: self.new_one_continue()
                        )
                    ]
                )
                self.new_customer_to_db.open()
            else:
                self.temp_bill_space = ''
                self.newcustomer_bool = False
                self.final_bill(bill)

    def dismiss_same_phno_diff_name(self):
        self.same_phno_diff_name.dismiss()

    def not_new(self):
        self.new_customer_to_db.dismiss()
        self.temp_bill_space = ''

    def new_one_continue(self):
        self.new_customer_to_db.dismiss()
        self.newcustomer_bool = True
        self.final_bill(self.temp_bill_space)

    def final_bill(self,bill):
        self.screen.ids.bill_error_view.text = "\nBill Generated Successfully"
        self.open_full_bill_view(bill)

    def cus_search_lay(self,text,obj):
        obj.text = text.upper()

        if text.isupper() or text.isdigit():
            self.customer_name_list_only(text)

        if text.strip() == '':
            self.additional_wid.size_hint = .001,.001
            self.screen.ids.cus_bill_no.disabled = False
            bill_main = list(self.screen.ids.pro_name.children)
            bill_main.reverse()
            count = 0
            for i in bill_main:
                if count == 2:
                    break
                i.disabled = False
                count += 1

    def customer_name_list_only(self,text):
        self.screen.ids.cus_bill_no.disabled = True
        bill_main = list(self.screen.ids.pro_name.children)
        bill_main.reverse()
        count = 0
        for i in bill_main:
            if count == 2:
                break
            i.disabled = True
            count += 1
        self.additional_wid.size_hint = .25,.24
        conn = sqlite3.connect('BillSoft.db')
        c = conn.cursor()

        c.execute('SELECT * FROM cusdetails')
        check_db = c.fetchall()
        try:
            if self.screen.ids.icon_butt_more.a == 0:
                matched_list = []
                for i in check_db:
                    check = re.findall(f'^{text.strip()}', str(i[0]))
                    if check:
                        matched_list.append(str(i[0]))

                conn.commit()
                conn.close()
            else:
                matched_list = []
                for i in check_db:
                    check = re.findall(f'{text.strip()}+', str(i[0]))
                    if check:
                        matched_list.append(str(i[0]))
        except:
            self.screen.ids.cus_name.text = ''
            self.backslah_warn.open()

            conn.commit()
            conn.close()

        self.additional_wid.ids.rv2.update(matched_list)

    def fill_cus_name_search_result(self,text):
        self.screen.ids.cus_name.text = text[2::]
        self.additional_wid.size_hint = .001,.001
        self.screen.ids.cus_bill_no.disabled = False
        bill_main = list(self.screen.ids.pro_name.children)
        bill_main.reverse()
        count = 0
        for i in bill_main:
            if count == 2:
                break
            i.disabled = False
            count += 1
        self.screen.ids.cus_name.focus = True

    def caps_search_pro_bill(self,text,obj,instance=0):
        obj.text = text.upper()

        if text.isupper() or text.isdigit():
            self.rv_busy = True
            try:
                self.bill_proname_search_cursor.foreground_color = 0,0,0,1
            except:
                pass
            self.bill_proname_search_cursor = obj
            self.bill_proname_search_cursor.focus = True
            self.bill_proname_search_cursor.foreground_color = 1,0,0,1
            conn = sqlite3.connect('BillSoft.db')
            c = conn.cursor()
            c.execute('SELECT *,oid FROM prodetailsdb')
            check_db = c.fetchall()
            if self.screen.ids.icon_butt_more.a == 0:
                matching_proname = []
                try:
                    for i in check_db:
                        check = re.findall(f'^{text.strip()}',str(i[0]))
                        if check:
                            matching_proname.append(str(i[0]))
                except:
                    obj.text = ''
                    self.backslah_warn.open()

                conn.commit()
                conn.close()
                self.screen.ids.search_proname_bill.update(matching_proname)
            else:
                matching_proname_extra = []
                try:
                    for i in check_db:
                        check = re.findall(f'{text.strip()}+',str(i[0]))
                        if check:
                            matching_proname_extra.append(str(i[0]))
                        self.screen.ids.search_proname_bill.update(matching_proname_extra)
                except:
                    obj.text = ''
                    self.backslah_warn.open()
                finally:
                    conn.commit()
                    conn.close()

        if text == '':
            self.rv_busy = False
            self.screen.ids.search_proname_bill.update([])
                

    def fill_proname_bill_from_search(self,text_):
        self.bill_proname_search_cursor.text = str(text_)[2::]
        self.bill_proname_search_cursor.focus = True

    def show_more_anime(self,anim):

        if self.screen.ids.icon_butt_more.a == 0:
            animate = Animation(
                height = 118,
                md_bg_color = self.theme_cls.primary_color,
                duration = .1
            )
            self.screen.ids.icon_butt_more.icon = 'chevron-down'
            self.screen.ids.icon_butt_more.a = 1
            try:
                self.caps_search_pro_bill(self.bill_proname_search_cursor.text,self.bill_proname_search_cursor)
            except:
                pass
        else:
            animate = Animation(
                height = 0,
                md_bg_color = (1,1,1,1),
                duration = .1
            )
            self.screen.ids.icon_butt_more.icon = 'chevron-up'
            self.screen.ids.icon_butt_more.a = 0
            try:
                self.caps_search_pro_bill(self.bill_proname_search_cursor.text,self.bill_proname_search_cursor)
            except:
                pass

        animate.start(anim)

    def on_focus_proname_list_item(self,obj,active):
        if active == True:
            self.caps_search_pro_bill(obj.text,obj)

    def empty_rv(self):
        self.screen.ids.search_proname_bill.update([])
        try:
            self.bill_proname_search_cursor.foreground_color = 0,0,0,1
        except:
            pass
        self.bill_proname_search_cursor = None

    def open_full_bill_view(self,bill):
        self.curr_bill_generated = bill
        popup = FullScreenBillView(
            text1 = f'Bill No: {self.curr_cus_bill_no.strip()}',
            text2 = f'Customer Name: {self.curr_cus_name.strip()}',
            text3 = f'Contact No: {self.curr_cus_contact_no.strip()}'
        )
        popup.open()
        
        self.curr_total_bill = 0
        for i in bill:
            if i[3] == 'packet':
                i[3] = 'pck(s)'
            temp_total = float(i[2]) * float(i[1])
            self.curr_total_bill += temp_total
            popup.ids.bill_pro.add_widget(
                OneLineListItem(text=i[0],bg_color=utils.get_color_from_hex('#EDF0BD'))
            )
            popup.ids.bill_qty.add_widget(
                OneLineListItem(text=f'{float(i[1])} {i[3]}',bg_color=utils.get_color_from_hex('#F0CABD'))
            )
            popup.ids.bill_price.add_widget(
                OneLineListItem(text=f'{temp_total} ₹',bg_color=utils.get_color_from_hex('#B9E3EC'))
            )
        
        popup.ids.bill_pro.add_widget(
            OneLineListItem(text='',bg_color=utils.get_color_from_hex('#CEF5DD'))
        )
        popup.ids.bill_qty.add_widget(
            OneLineListItem(text=f'Total :',bg_color=utils.get_color_from_hex('#CEF5DD'))
        )
        popup.ids.bill_price.add_widget(
            OneLineListItem(text=f'{self.curr_total_bill} ₹',bg_color=utils.get_color_from_hex('#CEF5DD'))
        )

    def add_to_db(self):
        a = datetime.datetime.now()
        time_details_trash = [
            a.strftime('%A'),
            a.strftime('%d'),
            a.strftime('%m'),
            a.strftime('%Y'),
            a.strftime('%H'),
            a.strftime('%M'),
            ]
        time_details = []
        for i in time_details_trash:
            time_details.append(str(i))

        del time_details_trash

        conn = sqlite3.connect('BillSoft.db')
        c = conn.cursor()

        if self.newcustomer_bool == True:
            c.execute('SELECT * FROM cusdetails')

            keyword = f"INSERT INTO cusdetails VALUES ('{self.curr_cus_name.strip()}','{self.curr_cus_contact_no.strip()}','None')"
            c.execute(keyword)

        c.execute('SELECT * FROM billdetails')

        keyword = f"""INSERT INTO billdetails VALUES ("{self.curr_cus_contact_no.strip()}","{self.curr_total_bill}","{self.curr_cus_bill_no}")"""
        c.execute(keyword)

        c.execute('SELECT *,oid FROM overallbillno')

        keyword = f"UPDATE overallbillno SET count = '{int(self.curr_cus_bill_no) + 1}' WHERE oid = 1"
        c.execute(keyword)

        conn.commit()
        conn.close()
        self.write_onto_json_bill(self.curr_bill_generated, time_details, self.curr_cus_bill_no)

        self.screen.ids.cus_name.text = ''
        self.screen.ids.cus_contact_no.text = ''
        self.screen.ids.bill_error_view.text = ''
        self.screen.ids.pro_name.clear_widgets()
        self.screen.ids.qty.clear_widgets()
        self.bill_screen_enter()
    
    def write_onto_json_bill(self,bill_list,time_list,bill_no):
        with open('billextra.json','r+') as file:
            curr_data = json.loads(file.read())
            billdict = curr_data['bill'].update({str(bill_no):list(bill_list)})
            timedict = curr_data['timedate'].update({str(bill_no):list(time_list)})

        with open('billextra.json','w') as file:
            json.dump(curr_data,file,indent=2)

    def fill_cus_contactno_search_result(self,text):
        self.screen.ids.cus_contact_no.text = text.strip()
        self.additional_wid2.size_hint = .001,.001
        self.disabling_widgets_for_rv3(False)
        self.screen.ids.cus_contact_no.focus = True

    def disabling_widgets_for_rv3(self,instance):
        main_bill = list(self.screen.ids.qty.children)
        main_bill.reverse()
        count = 0
        for i in main_bill:
            if count == 2:
                break
            i.disabled = instance
            count += 1

        self.screen.ids.details_view_icon.disabled = instance

    def dismiss_rv3(self,obj,state):
        if state == True:
            if self.screen.ids.cus_contact_no.text.strip() != '':
                self.additional_wid2.size_hint = .25,.24
                self.cus_con_no_list_only(self.screen.ids.cus_contact_no.text)
                self.disabling_widgets_for_rv3(True)
        if state == False:
            self.additional_wid2.size_hint = .001,.001
            self.disabling_widgets_for_rv3(False)

    def cus_con_no_list_only(self,text):
        conn = sqlite3.connect('BillSoft.db')
        c = conn.cursor()
        matched_list = []

        name = self.screen.ids.cus_name.text.strip()

        if name == '':
            c.execute('SELECT * FROM cusdetails')
            check_all = c.fetchall()
            for i in check_all:
                check = re.findall(f'^{text}', str(i[1]))
                if check:
                    matched_list.append(str(i[1]))
        else:
            if self.screen.ids.icon_butt_more.a == 0:
                c.execute('SELECT * FROM cusdetails')
                check_all = c.fetchall()
                for i in check_all:
                    if str(i[0]) == name:
                        check = re.findall(f'^{text}', str(i[1]))
                        if check:
                            matched_list.append(str(i[1]))
            else:
                c.execute('SELECT * FROM cusdetails')
                check_all = c.fetchall()
                for i in check_all:
                    check = re.findall(f'^{text}', str(i[1]))
                    if check:
                        matched_list.append(str(i[1]))

        conn.commit()
        conn.close()

        self.additional_wid2.ids.rv3.update(matched_list)

    def search_contact_no_billing_screen(self,text):
        if self.screen.ids.cus_contact_no.text.strip() != '':
            self.additional_wid2.size_hint = .25,.24
            self.disabling_widgets_for_rv3(True)
            self.cus_con_no_list_only(self.screen.ids.cus_contact_no.text)
        if self.screen.ids.cus_contact_no.text.strip() == '':
            self.additional_wid2.size_hint = .001,.001
            self.disabling_widgets_for_rv3(False)
            self.additional_wid2.ids.rv3.update([])

    def open_drop_down_sort(self,obj):
        menu_labels = [
        {
            "text": f"{i}"
            } for i in ['Products','Item Code']
        ]
        self.drop_db_pro = MDDropdownMenu(
            caller=obj,
            items=menu_labels,
            position="bottom",
            width_mult=2.3
        )
        self.drop_db_pro.bind(on_release=self.search_db_pro_drop)
        self.drop_db_pro.open()

    def db_screen_enter(self):
        self.screen.ids.search_pro_db.text = ''
        conn = sqlite3.connect('BillSoft.db')
        c = conn.cursor()

        c.execute('SELECT * FROM prodetailsdb')
        check_db = c.fetchall()
        matched_list = []
        for i in check_db:
            temp_list = []
            temp_list.append(str(i[0]))
            temp_list.append(str(i[1]))
            temp_list.append(str(i[2]))
            temp_list.append(str(i[3]))
            matched_list.append(temp_list)

        self.screen.ids.rvdb.update(matched_list)

        conn.commit()
        conn.close()

    def caps_search_db_pro(self,text,obj):

        def child_func(interval):
            self.db_screen_enter()

        obj.text = text.upper()

        if text.strip() == '':
            self.db_screen_enter()

        if text.isupper() or text.isdigit():
            conn = sqlite3.connect('BillSoft.db')
            c = conn.cursor()

            c.execute('SELECT * FROM prodetailsdb')
            check_db = c.fetchall()
            matched_list = []
            try:
                if self.search_for_in_db == 'Products':
                    if self.screen.ids.show_more_check.state == 'normal':
                        for i in check_db:
                            check = re.findall(f'^{text.strip()}', str(i[0]))
                            if check:
                                temp_list = []
                                temp_list.append(str(i[0]))
                                temp_list.append(str(i[1]))
                                temp_list.append(str(i[2]))
                                temp_list.append(str(i[3]))
                                matched_list.append(temp_list)

                    if self.screen.ids.show_more_check.state == 'down':
                        for i in check_db:
                            check = re.findall(f'{text.strip()}+', str(i[0]))
                            if check:
                                temp_list = []
                                temp_list.append(str(i[0]))
                                temp_list.append(str(i[1]))
                                temp_list.append(str(i[2]))
                                temp_list.append(str(i[3]))
                                matched_list.append(temp_list)
                else:
                    for i in check_db:
                        check = re.findall(f'^{text.strip()}', str(i[3]))
                        if check:
                            temp_list = []
                            temp_list.append(str(i[0]))
                            temp_list.append(str(i[1]))
                            temp_list.append(str(i[2]))
                            temp_list.append(str(i[3]))
                            matched_list.append(temp_list)
            except:
                obj.text = ''
                self.backslah_warn.open()
                Clock.schedule_once(child_func, .2)
            else:
                self.screen.ids.rvdb.update(matched_list)
            finally:
                conn.commit()
                conn.close()

    def search_db_pro_drop(self,text,item):
        if item.text == 'Products':
            self.screen.ids.search_pro_db.hint_text = 'Search in Products'
            self.screen.ids.sort_label_db_pro.text = 'Products'
            self.screen.ids.search_pro_db.input_filter = None
            self.search_for_in_db = 'Products'
            self.caps_search_db_pro(self.screen.ids.search_pro_db.text,self.screen.ids.search_pro_db)
        else:
            self.screen.ids.search_pro_db.hint_text = 'Search in Item Code'
            self.screen.ids.sort_label_db_pro.text = 'Item Code'
            self.screen.ids.search_pro_db.input_filter = 'int'
            self.search_for_in_db = 'Item Code'
            self.caps_search_db_pro(self.screen.ids.search_pro_db.text,self.screen.ids.search_pro_db)

        self.drop_db_pro.dismiss()

    def checkbox_active_show_more_db_pro(self,checkbox,value):
        self.caps_search_db_pro(self.screen.ids.search_pro_db.text,self.screen.ids.search_pro_db)

    def edit_from_db_pro(self,text,screen_change=1):
        conn = sqlite3.connect('BillSoft.db')
        c = conn.cursor()

        c.execute('SELECT * FROM prodetailsdb')
        check_db = c.fetchall()
        for i in check_db:
            if str(i[0]) == text:
                self.glob_edit_price = str(i[1])
                self.glob_edit_unit = str(i[2])
                self.glob_edit_itemcode = str(i[3])

        conn.commit()
        conn.close()
        self.screen.ids.edit_itemcode.text = self.glob_edit_itemcode
        self.screen.ids.edit_proname.text = text
        self.screen.ids.edit_price.text = self.glob_edit_price
        self.screen.ids.edit_unit.text = self.glob_edit_unit
        if screen_change == 1:
            self.screen.ids.edit_error_lab.text = ''
            self.screen.ids.screen_manager.transition = FadeTransition()
            self.screen.ids.screen_manager.transition.clearcolor = 1,1,1,1
            self.screen.ids.screen_manager.current = 'edit pro screen'

    def back_from_edit_screen(self):
        self.screen.ids.screen_manager.transition = FadeTransition()
        self.screen.ids.screen_manager.transition.clearcolor = 1,1,1,1
        self.screen.ids.screen_manager.current = 'db screen'
        self.screen.ids.edit_error_lab.text = ''
        toast('No changes made')
    
    def confirm_edit_price(self,edited_price,proname,itemcode):
        access = True
        try:
            if float(self.glob_edit_price) == float(edited_price):
                self.screen.ids.screen_manager.transition = FadeTransition()
                self.screen.ids.screen_manager.transition.clearcolor = 1,1,1,1
                self.screen.ids.screen_manager.current = 'db screen'
                self.screen.ids.edit_error_lab.text = ''
                toast('No changes made') 
                access = False
        except:
            self.screen.ids.edit_error_lab.text = '* Price is provided in a wrong format'
            return
        else:
            if access == True:
                if float(edited_price) > 0:
                    self.screen.ids.edit_error_lab.text = '' 
                    conn = sqlite3.connect('BillSoft.db')
                    c = conn.cursor()

                    c.execute('SELECT * FROM prodetailsdb')
                    keyword = f"UPDATE prodetailsdb SET price = '{float(edited_price)}' WHERE name = '{str(proname)}'"
                    c.execute(keyword)

                    conn.commit()
                    conn.close() 
                    self.screen.ids.screen_manager.transition = FadeTransition()
                    self.screen.ids.screen_manager.transition.clearcolor = 1,1,1,1
                    self.screen.ids.screen_manager.current = 'db screen'
                    self.screen.ids.edit_error_lab.text = ''
                    self.write_price_to_csv(edited_price,itemcode)
                else:
                    self.screen.ids.edit_error_lab.text = '* Price should be a positive number'

    def write_price_to_csv(self,price,code):
        a = datetime.datetime.now()
        list_ = [
            str(a.strftime('%d')),
            str(a.strftime('%m')),
            str(a.strftime('%Y')),
            str(float(price)),
            str(code)
            ]
        with open('ptracker.csv','a') as file:
            writer = csv.writer(file)
            writer.writerow(list_)

    def on_enter_cus_info_screen(self):
        conn = sqlite3.connect('BillSoft.db')
        c = conn.cursor()
        self.screen.ids.search_cus_details.text = ''

        c.execute('SELECT * FROM cusdetails')
        check_db = c.fetchall()
        matched_list = []
        for i in check_db:
            temp_list = []
            temp_list.append(str(i[0]))
            temp_list.append(str(i[1]))
            matched_list.append(temp_list)

        conn.commit()
        conn.close()
        self.screen.ids.rvcus.update(matched_list)

    def caps_search_cus_details(self,text,obj):

        obj.text = text.upper()

        if text.strip() == '':
            self.on_enter_cus_info_screen()

        if text.isupper() or text.isdigit():
            try:
                conn = sqlite3.connect('BillSoft.db')
                c = conn.cursor()
                c.execute('SELECT * FROM cusdetails')
                check_db = c.fetchall()
                if self.cus_info_search == 'Name':
                    if self.screen.ids.show_more_check_cus_details.state == 'normal':
                        matched_list = []
                        for i in check_db:
                            check = re.findall(f'^{text.strip()}',str(i[0]))
                            if check:
                                temp_list = []
                                temp_list.append(str(i[0]))
                                temp_list.append(str(i[1]))
                                matched_list.append(temp_list)
                    else:
                        matched_list = []
                        for i in check_db:
                            check = re.findall(f'{text.strip()}+',str(i[0]))
                            if check:
                                temp_list = []
                                temp_list.append(str(i[0]))
                                temp_list.append(str(i[1]))
                                matched_list.append(temp_list)
                else:
                    matched_list = []
                    for i in check_db:
                        check = re.findall(f'^{text.strip()}',str(i[1]))
                        if check:
                            temp_list = []
                            temp_list.append(str(i[0]))
                            temp_list.append(str(i[1]))
                            matched_list.append(temp_list)
            except:
                self.backslah_warn.open()
                obj.text = ''
            else:
                self.screen.ids.rvcus.update(matched_list)
            finally:
                conn.commit()
                conn.close()
            

    def open_drop_down_sort_cus_details(self,obj):
        menu_labels2 = [
        {
            "text": f"{i}"
            } for i in ['Name','Contact No']
        ]
        self.drop_cus_info = MDDropdownMenu(
            caller=obj,
            items=menu_labels2,
            position="bottom",
            width_mult=2.3
        )
        self.drop_cus_info.bind(on_release=self.search_cus_info)
        self.drop_cus_info.open()

    def search_cus_info(self,text,item):
        if item.text == 'Name':
            self.screen.ids.search_cus_details.hint_text = f'Search In {item.text}'
            self.screen.ids.search_cus_details.input_filter = None
            self.screen.ids.sort_label_cus_details.text = str(item.text)
            self.cus_info_search = 'Name'
            self.caps_search_cus_details(self.screen.ids.search_cus_details.text,self.screen.ids.search_cus_details)
        else:
            self.screen.ids.search_cus_details.hint_text = f'Search In {item.text}'
            self.screen.ids.search_cus_details.input_filter = 'int'
            self.screen.ids.sort_label_cus_details.text = str(item.text)
            self.cus_info_search = 'Contact No'
            self.caps_search_cus_details(self.screen.ids.search_cus_details.text,self.screen.ids.search_cus_details)

        self.drop_cus_info.dismiss()

    def checkbox_active_show_more_cus_details(self,checkbox,value):
        self.caps_search_cus_details(self.screen.ids.search_cus_details.text,self.screen.ids.search_cus_details)

    def location_show_cus(self,phno,name):
        conn = sqlite3.connect('BillSoft.db')
        c = conn.cursor()
        keyword = f"SELECT * FROM cusdetails WHERE phno = '{phno}'"
        c.execute(keyword)
        check_db = c.fetchall()
        location = check_db[0][2]
        if location == 'None':
            self.reset = ''
            self.popup_screen = LocationDetails(
                name = f'Name: {name}',
                phno = f'Contact No: {phno}',
                loc = ''
            )
        else:
            self.reset = location
            self.popup_screen = LocationDetails(
                name = f'Name: {name}',
                phno = f'Contact No: {phno}',
                loc = location
            )
        self.popup_screen.open()
        self.popup_screen.ids.inploc.focus = True

        conn.commit()
        conn.close()

    def change_location(self,location,phno):
        if location.strip() == '' or location.strip() == 'NONE':
            toast('Invalid location')
        else:
            if location.strip() == self.reset:
                toast('No changes made')
            else:
                conn = sqlite3.connect('BillSoft.db')
                c = conn.cursor()

                c.execute("SELECT * FROM cusdetails")
                keyword = f"UPDATE cusdetails SET location = '{location.strip()}' WHERE phno = '{phno[12::]}'"
                c.execute(keyword)
                conn.commit()
                conn.close()

            self.popup_screen.dismiss()

    def on_focus_loc_edit_cus(self,obj,active,sep):
        if active == True:
            animate = Animation(
                size_hint = (1,.03),
                duration = .1
            )
            animate.start(sep)
        else:
            animate = Animation(
                size_hint = (1,.008),
                duration = .1
            )
            animate.start(sep)

    def on_enter_bill_details(self):
        conn = sqlite3.connect('BillSoft.db')
        c = conn.cursor()
        self.screen.ids.search_bill_details.text = ''

        c.execute('SELECT * FROM billdetails')
        check_db = c.fetchall()
        matched_list = []
        for i in check_db:
            temp_list = []
            temp_list.append(i[2])
            temp_list.append(i[0])
            temp_list.append(i[1])
            matched_list.append(temp_list)

        with open('billextra.json','r+') as file:
            data = json.loads(file.read())
            for i in matched_list:
                bill_no = str(i[0])    
                timedict = data['timedate'][bill_no]
                date_str = f'{timedict[1]}-{timedict[2]}-{timedict[3]}'
                i.append(date_str)
            
        conn.commit()
        conn.close()

        self.screen.ids.rvbill.update(matched_list)

    def open_drop_down_sort_bill_details(self,obj):
        menu_labels3 = [
        {
            "text": f"{i}"
            } for i in ['Bill No','Contact No']
        ]
        self.drop_bill_details = MDDropdownMenu(
            caller=obj,
            items=menu_labels3,
            position="bottom",
            width_mult=2.3
        )
        self.drop_bill_details.bind(on_release=self.search_bill_info)
        self.drop_bill_details.open()

    def search_bill_info(self,text,item):
        if item.text == 'Bill No':
            self.screen.ids.search_bill_details.hint_text = f'Search In {item.text}'
            self.screen.ids.sort_label_bill_details.text = str(item.text)
            self.bill_details_search = 'Bill No'
            self.caps_search_bill_details(self.screen.ids.search_bill_details.text,self.screen.ids.search_bill_details)
        else:
            self.screen.ids.search_bill_details.hint_text = f'Search In {item.text}'
            self.screen.ids.sort_label_bill_details.text = str(item.text)
            self.bill_details_search = 'Contact No'
            self.caps_search_bill_details(self.screen.ids.search_bill_details.text,self.screen.ids.search_bill_details)

        self.drop_bill_details.dismiss()

    def caps_search_bill_details(self,text,obj):

        def child_func(interval):
            self.on_enter_bill_details()
    
        if text.isdigit():
            conn = sqlite3.connect('BillSoft.db')
            c = conn.cursor()
            c.execute('SELECT * FROM billdetails')
            check_db = c.fetchall()
            matched_list = []
            try:
                if self.bill_details_search == 'Bill No':
                    for i in check_db:
                        check = re.findall(f'^{text.strip()}',str(i[2]))
                        if check:
                            temp_list = []
                            temp_list.append(i[2])
                            temp_list.append(i[0])
                            temp_list.append(i[1])
                            matched_list.append(temp_list)
                    if len(matched_list) != 0:
                        with open('billextra.json','r+') as file:
                            data = json.loads(file.read())
                            for i in matched_list:
                                bill_no = str(i[0])    
                                timedict = data['timedate'][bill_no]
                                date_str = f'{timedict[1]}-{timedict[2]}-{timedict[3]}'
                                i.append(date_str)
                else:
                    for i in check_db:
                        check = re.findall(f'^{text.strip()}',str(i[0]))
                        if check:
                            temp_list = []
                            temp_list.append(i[2])
                            temp_list.append(i[0])
                            temp_list.append(i[1])
                            matched_list.append(temp_list)
                    if len(matched_list) != 0:
                        with open('billextra.json','r+') as file:
                            data = json.loads(file.read())
                            for i in matched_list:
                                bill_no = str(i[0])    
                                timedict = data['timedate'][bill_no]
                                date_str = f'{timedict[1]}-{timedict[2]}-{timedict[3]}'
                                i.append(date_str)
            except:
                self.backslah_warn.open()
                Clock.schedule_once(child_func, .2)
            else:
                self.screen.ids.rvbill.update(matched_list)
            finally:
                conn.commit()
                conn.close()

        if text.strip() == '':
            self.on_enter_bill_details()

    def get_bill_from_csv(self,file_name,bill_no):
        with open(file_name,'r+') as file:
            datas = json.loads(file.read())
            bill = datas['bill'][bill_no]
            return list(bill)

    def get_cus_name_by_con_no(self,con_no):
        conn = sqlite3.connect('BillSoft.db')
        c = conn.cursor()
        c.execute(f"SELECT * FROM cusdetails WHERE phno = '{con_no}'")
        check_db = c.fetchall()
        name = check_db[0][0]
        conn.commit()
        conn.close()
        return name

    def regenerate_existing_bill(self,bill_no,con_no):
        cus_name = self.get_cus_name_by_con_no(con_no[36::])
        repopup = FullScreenBillReview(
            text1 = f'Bill No: {bill_no[33::]}',
            text2 = f'Customer Name: {cus_name}',
            text3 = f'Contact No: {con_no[36::]}'
        )
        repopup.open()

        bill = self.get_bill_from_csv('billextra.json', str(bill_no)[33::])

        curr_total_bill = 0
        for i in bill:
            if i[3] == 'packet':
                i[3] = 'pck(s)'
            temp_total = float(i[2]) * float(i[1])
            curr_total_bill += temp_total
            repopup.ids.bill_pro.add_widget(
                OneLineListItem(text=i[0],bg_color=utils.get_color_from_hex('#EDF0BD'))
            )
            repopup.ids.bill_qty.add_widget(
                OneLineListItem(text=f'{float(i[1])} {i[3]}',bg_color=utils.get_color_from_hex('#F0CABD'))
            )
            repopup.ids.bill_price.add_widget(
                OneLineListItem(text=f'{temp_total} ₹',bg_color=utils.get_color_from_hex('#B9E3EC'))
            )
        
        repopup.ids.bill_pro.add_widget(
            OneLineListItem(text='',bg_color=utils.get_color_from_hex('#CEF5DD'))
        )
        repopup.ids.bill_qty.add_widget(
            OneLineListItem(text=f'Total :',bg_color=utils.get_color_from_hex('#CEF5DD'))
        )
        repopup.ids.bill_price.add_widget(
            OneLineListItem(text=f'{curr_total_bill} ₹',bg_color=utils.get_color_from_hex('#CEF5DD'))
        )

    # graph area

    def on_enter_graph_screen(self,header,des_icon,des_sep):

        def child_func(interval):
            animate_header.start(header)

        def child_func2(interval):
            animate_sep2.start(des_sep)

        animate_header = Animation(
            color = (0,0,0,.8),
            duration = .6
        )

        animate_icon = Animation(
            pos_hint = {'center_x': .85,'center_y':.8},
            duration = .6
        )

        animate_sep = Animation(
            size_hint = (1,.007),
            duration = .6
        )

        animate_sep2 = Animation(
            md_bg_color = self.theme_cls.primary_color,
            duration = .4
        )

        animate_icon.start(des_icon)
        animate_sep.start(des_sep)
        Clock.schedule_once(child_func, .4) 
        Clock.schedule_once(child_func2, .6)

    def graph_show(self,interval):
        colors = ['#3771EF','#DAB839','#DD602F','#CE2FDD','#2FDD8F']
        plt.bar(self.x_axis,self.y_axis,color=colors)
        plt.title(self.title_graph,size=20,color='darkgreen')
        plt.xlabel(self.xlabel,size=14,color='red')
        plt.ylabel(self.ylabel,size=14,color='red')
        if self.grid == True:
            plt.grid(linestyle = '-')
        plt.show()
        self.loading.dismiss()

    def cus_money_spend_pre(self):
        self.modal_money_spend = ModalMoneySpend()
        self.modal_money_spend.open()

    def cus_money_spend(self,name_check,grid_check):

        self.modal_money_spend.dismiss()

        self.loading = LoadingView()
        self.loading.open()

        if name_check.active == True:
            self.x_axis_sort_money_spend = 'Name'
            self.xlabel = 'Name'
        else:
            self.x_axis_sort_money_spend = 'Contact No'
            self.xlabel = 'Contact No'
        if grid_check.active == True:
            self.grid = True
        else:
            self.grid = False
        
        self.ylabel = 'Money Spend (₹)'
        self.title_graph = 'Most Money Spend'

        conn = sqlite3.connect('BillSoft.db')
        c = conn.cursor()

        c.execute('SELECT * FROM billdetails')
        check_db = c.fetchall()
        calculate_dict = {}
        for i in check_db:
            try:
                calculate_dict[str(i[0])] += float(i[1])
            except:
                calculate_dict[str(i[0])] = float(i[1])

        if len(calculate_dict) > 5:
            count = 0
            calculate_dict_dummy = calculate_dict
            calculate_dict = {}
            for k,v in calculate_dict_dummy.items():
                calculate_dict[k] = v 
                count += 1
                if count == 5:
                    break
        
        df = pd.Series(calculate_dict)
        df.sort_values(inplace=True,ascending=False)

        calculate_dict = {}
        for i in df.index:
            calculate_dict[i] = df[i]
        del df

        x_axis = []
        y_axis = []
        for k,v in calculate_dict.items():
            x_axis.append(k)
            y_axis.append(v)

        if self.x_axis_sort_money_spend == 'Name':
            count = 0
            for i in x_axis:
                c.execute(f"SELECT * FROM cusdetails WHERE phno = '{i}'")
                check_cus = c.fetchall()
                cus_name = check_cus[0][0]
                x_axis[count] = cus_name
                count += 1

        conn.commit()
        conn.close()

        self.x_axis = np.array(x_axis)
        self.y_axis = np.array(y_axis)
        del x_axis
        del y_axis

        Clock.schedule_once(self.graph_show,.5)

    def cus_visit_pre(self):
        self.modal_cus_visit = ModalCusVisit()
        self.modal_cus_visit.open()

    def cus_visit(self,name_check,grid_check):
        self.modal_cus_visit.dismiss()

        self.loading = LoadingView()
        self.loading.open()

        if name_check.active == True:
            self.x_axis_sort_money_spend = 'Name'
            self.xlabel = 'Name'
        else:
            self.x_axis_sort_money_spend = 'Contact No'
            self.xlabel = 'Contact No'
        if grid_check.active == True:
            self.grid = True
        else:
            self.grid = False
        
        self.ylabel = 'No. Of Visit(s)'
        self.title_graph = 'Most Visits'

        conn = sqlite3.connect('BillSoft.db')
        c = conn.cursor()

        c.execute('SELECT * FROM billdetails')
        check_db = c.fetchall()
        calculate_dict = {}
        for i in check_db:
            try:
                calculate_dict[str(i[0])] += 1
            except:
                calculate_dict[str(i[0])] = 1

        if len(calculate_dict) > 5:
            count = 0
            calculate_dict_dummy = calculate_dict
            calculate_dict = {}
            for k,v in calculate_dict_dummy.items():
                calculate_dict[k] = v 
                count += 1
                if count == 5:
                    break
        
        df = pd.Series(calculate_dict)
        df.sort_values(inplace=True,ascending=False)

        calculate_dict = {}
        for i in df.index:
            calculate_dict[i] = df[i]
        del df

        x_axis = []
        y_axis = []
        for k,v in calculate_dict.items():
            x_axis.append(k)
            y_axis.append(v)

        if self.x_axis_sort_money_spend == 'Name':
            count = 0
            for i in x_axis:
                c.execute(f"SELECT * FROM cusdetails WHERE phno = '{i}'")
                check_cus = c.fetchall()
                cus_name = check_cus[0][0]
                x_axis[count] = cus_name
                count += 1

        conn.commit()
        conn.close()

        self.x_axis = np.array(x_axis)
        self.y_axis = np.array(y_axis)
        del x_axis
        del y_axis

        Clock.schedule_once(self.graph_show,.5)

    def sold_product_pre(self):
        self.modal_sold_product = ModalSoldProduct()
        self.modal_sold_product.open()

    def sold_product(self,x_axis_name,grid):
        self.modal_sold_product.dismiss()

        self.loading = LoadingView()
        self.loading.open()

        if grid.active == True:
            self.grid = True
        else:
            self.grid = False

        all_bill = []
        with open('billextra.json','r+') as file:
            data = json.loads(file.read())
            for i in data['bill']:
                all_bill.append(data['bill'][i])

        product_dict = {}
        for i in all_bill:
            for x in i:
                try:
                    product_dict[x[0]] += float(x[1])
                except:
                    product_dict[x[0]] = float(x[1])

        df = pd.Series(product_dict)
        df.sort_values(inplace=True,ascending=False)

        conn = sqlite3.connect('BillSoft.db')
        c = conn.cursor()
        c.execute('SELECT * FROM prodetailsdb')
        check_db = c.fetchall()
        all_products = []
        for i in check_db:
            all_products.append(i[0])
        conn.commit()
        conn.close()

        product_dict = {}
        count = 0
        for i in df.index:
            if str(i) in all_products:
                product_dict[i] = df[i]
                count += 1
                if count == 5:
                    break
        del df

        x_axis = []
        y_axis = []
        for k,v in product_dict.items():
            x_axis.append(k)
            y_axis.append(v)

        self.xlabel = 'Product Name'
        self.ylabel = 'No Of Product(s) Sold'
        self.title_graph = 'Most Sold Product'

        if x_axis_name.active == False:
            self.xlabel = 'Item Code'
            conn = sqlite3.connect('BillSoft.db')
            c = conn.cursor()
            x_axis_temp = x_axis
            x_axis = []
            for i in x_axis_temp:
                c.execute(f"SELECT * FROM prodetailsdb WHERE name = '{i}'")
                check_db = c.fetchall()
                x_axis.append(check_db[0][-1])
            conn.commit()
            conn.close()

        self.x_axis = np.array(x_axis)
        self.y_axis = np.array(y_axis)
        del x_axis
        del y_axis

        Clock.schedule_once(self.graph_show,.5)

    def earned_product_pre(self):
        self.modal_earned_product = ModalEarnedProduct()
        self.modal_earned_product.open()

    def earned_product(self,x_axis_name,grid):

        self.modal_earned_product.dismiss()

        self.loading = LoadingView()
        self.loading.open()

        if grid.active == True:
            self.grid = True
        else:
            self.grid = False

        all_bill = []
        with open('billextra.json','r+') as file:
            data = json.loads(file.read())
            for i in data['bill']:
                all_bill.append(data['bill'][i])

        product_dict = {}
        for i in all_bill:
            for x in i:
                try:
                    product_dict[x[0]] += float(x[2]) * float(x[1])
                except:
                    product_dict[x[0]] = float(x[2]) * float(x[1])

        df = pd.Series(product_dict)
        df.sort_values(inplace=True,ascending=False)

        conn = sqlite3.connect('BillSoft.db')
        c = conn.cursor()
        c.execute('SELECT * FROM prodetailsdb')
        check_db = c.fetchall()
        all_products = []
        for i in check_db:
            all_products.append(i[0])
        conn.commit()
        conn.close()

        product_dict = {}
        count = 0
        for i in df.index:
            if str(i) in all_products:
                product_dict[i] = df[i]
                count += 1
                if count == 5:
                    break
        del df

        x_axis = []
        y_axis = []
        for k,v in product_dict.items():
            x_axis.append(k)
            y_axis.append(v)

        self.xlabel = 'Product Name'
        self.ylabel = 'Money Earned'
        self.title_graph = 'Most Earned Product'

        if x_axis_name.active == False:
            self.xlabel = 'Item Code'
            conn = sqlite3.connect('BillSoft.db')
            c = conn.cursor()
            x_axis_temp = x_axis
            x_axis = []
            for i in x_axis_temp:
                c.execute(f"SELECT * FROM prodetailsdb WHERE name = '{i}'")
                check_db = c.fetchall()
                x_axis.append(check_db[0][-1])
            conn.commit()
            conn.close()

        self.x_axis = np.array(x_axis)
        self.y_axis = np.array(y_axis)
        del x_axis
        del y_axis

        Clock.schedule_once(self.graph_show,.5)

    def price_details_pre(self):
        self.modal_price_details = ModalPriceDetails()
        self.modal_price_details.open()

    def search_price_details_screen(self,obj,text):
        obj.text = text.upper()

        if text.strip() == '':
            self.modal_price_details.on_pre_open()

        if text.isupper() or text.isdigit():
            conn = sqlite3.connect('BillSoft.db')
            c = conn.cursor()
            c.execute('SELECT * FROM prodetailsdb')
            check_db = c.fetchall()
            if self.modal_price_details.ids.sort_label_price_details.text == 'Products':
                if self.modal_price_details.ids.show_more_check.state == 'down':
                    matched_list = []
                    for i in check_db:
                        try:
                            check = re.findall(f'{text.strip()}+',str(i[0]))
                        except:
                            self.backslah_warn.open()
                            obj.text = ''
                        else:
                            if check:
                                temp_list = []
                                temp_list.append(str(i[0]))
                                temp_list.append(str(i[-1]))
                                matched_list.append(temp_list)
                else:
                    matched_list = []
                    for i in check_db:
                        try:
                            check = re.findall(f'^{text.strip()}',str(i[0]))
                        except:
                            self.backslah_warn.open()
                            obj.text = ''
                        else:
                            if check:
                                temp_list = []
                                temp_list.append(str(i[0]))
                                temp_list.append(str(i[-1]))
                                matched_list.append(temp_list)
            else:
                matched_list = []
                for i in check_db:
                    try:
                        check = re.findall(f'{text.strip()}+',str(i[-1]))
                    except:
                        self.backslah_warn.open()
                        obj.text = ''
                    else:
                        if check:
                            temp_list = []
                            temp_list.append(str(i[0]))
                            temp_list.append(str(i[-1]))
                            matched_list.append(temp_list)

            self.modal_price_details.ids.rv.update(matched_list)

            conn.commit()
            conn.close()

    def open_drop_down_price_details(self,obj):
        menu_labels = [
        {
            "text": f"{i}"
            } for i in ['Products','Item Code']
        ]
        self.drop_price_screen = MDDropdownMenu(
            caller=obj,
            items=menu_labels,
            position="auto",
            width_mult=2.3
        )
        self.drop_price_screen.bind(on_release=self.search_price_details_drop_item)
        self.drop_price_screen.open()

    def search_price_details_drop_item(self,obj,item):
        self.modal_price_details.ids.sort_label_price_details.text = item.text
        self.modal_price_details.ids.textinput.hint_text = f'Search in {item.text}'
        self.drop_price_screen.dismiss()
        self.search_price_details_screen(self.modal_price_details.ids.textinput,self.modal_price_details.ids.textinput.text)

    def checkbox_active_show_more_price_details(self,checkbox,value):
        self.search_price_details_screen(self.modal_price_details.ids.textinput,self.modal_price_details.ids.textinput.text)

    def product_price(self,code,name):

        self.loading = LoadingView()
        self.loading.open()

        self.title_graph = f'Price Variation(s) in {name}'
        self.xlabel = 'Date' 
        self.ylabel = 'Price'

        self.x_axis = []
        self.y_axis = []
        with open('ptracker.csv','r') as file:
            reader = csv.reader(file)
            count = 1
            for i in reader:
                if len(i) != 0:
                    if i[4] == code:
                        self.x_axis.append(f'{i[0]}-{i[1]}-{i[2]}({count})')
                        self.y_axis.append(float(i[3]))
                        count += 1

        if len(self.x_axis) == 1:
            self.loading.dismiss()
            self.limited_data = MDDialog(
                text = '[color=#000000]Not enough data for plotting graph[/color]',
                buttons = [ 
                    FocusMDRaisedButton(
                        text = 'Got it',
                        on_release = lambda x : self.limited_data.dismiss()
                    )
                ]
                )
            self.limited_data.open()
        else:
            Clock.schedule_once(self.line_graph,.5)

    def line_graph(self,interval):
        plt.plot(self.x_axis,self.y_axis)
        plt.title(self.title_graph,size=20,color='darkgreen')
        plt.xlabel(self.xlabel,size=14,color='red')
        plt.ylabel(self.ylabel,size=14,color='red')
        plt.grid(linestyle = '-')
        plt.show()

        self.loading.dismiss()

    def popular_time_pre(self):
        self.modal_popular_time = ModalPopularTime()
        self.modal_popular_time.open()

    def popular_time(self,grid):
        self.modal_popular_time.dismiss()

        self.loading = LoadingView()
        self.loading.open()

        if grid.state == 'down':
            self.grid = True
        else:
            self.grid = False

        self.title_graph = 'Popular Time'
        self.xlabel = 'Time (Hour)'
        self.ylabel = 'No. Of Customer(s)'

        time_dict = {}
        with open('billextra.json','r+') as file:
            data = json.loads(file.read())
            for i in data['timedate']:
                try:
                    time_dict[data['timedate'][i][-2]] += 1
                except:
                    time_dict[data['timedate'][i][-2]] = 1

        df = pd.Series(time_dict)
        df.sort_index(inplace=True,ascending=True)

        self.x_axis = []
        self.y_axis = []
        for i in df.index:
            self.x_axis.append(i)
            self.y_axis.append(df[i])
        del df

        Clock.schedule_once(self.graph_show,.5)

    def popular_day_pre(self):
        self.modal_popular_day = ModalPopularDay()
        self.modal_popular_day.open()

    def popular_day(self,grid):
        self.modal_popular_day.dismiss()

        self.loading = LoadingView()
        self.loading.open()

        if grid.state == 'down':
            self.grid = True
        else:
            self.grid = False

        self.title_graph = 'Popular Day'
        self.xlabel = 'Day'
        self.ylabel = 'No. Of Customer(s)'

        time_dict = {
            'Sunday' : 0,
            'Monday' : 0,
            'Tuesday' : 0,
            'Wednesday' : 0,
            'Thursday' : 0,
            'Friday' : 0,
            'Saturday' : 0
        }
        with open('billextra.json','r+') as file:
            data = json.loads(file.read())
            for i in data['timedate']:
                time_dict[data['timedate'][i][0]] += 1

        self.x_axis = []
        self.y_axis = []
        for k,v in time_dict.items():
            self.x_axis.append(k)
            self.y_axis.append(v)
        
        Clock.schedule_once(self.graph_show,.5)

    def backup_screen_enter(self):
        self.screen.ids.search_backup.text = ''
        with open('backup.csv','r+') as file:
            reader = csv.reader(file)
            all_ = []
            for i in reader:
                if len(i) != 0:
                    all_.append(i)

        self.screen.ids.rvbackup.update(all_)

    def open_drop_down_sort_backup(self,obj):
        menu_labels = [
        {
            "text": f"{i}"
            } for i in ['Products','Item Code']
        ]
        self.drop_backup_screen = MDDropdownMenu(
            caller=obj,
            items=menu_labels,
            position="auto",
            width_mult=2.3
        )
        self.drop_backup_screen.bind(on_release=self.search_backup_drop_item)
        self.drop_backup_screen.open()

    def search_backup_drop_item(self,obj,item):
        self.screen.ids.sort_label_backup.text = item.text
        self.screen.ids.search_backup.hint_text = f'Search in {item.text}'
        self.caps_search_backup(self.screen.ids.search_backup.text,self.screen.ids.search_backup)
        self.drop_backup_screen.dismiss()

    def caps_search_backup(self,text,obj):
        obj.text = text.upper()

        if text.strip() == '':
            self.backup_screen_enter()

        if text.isupper() or text.isdigit():
            conn = sqlite3.connect('BillSoft.db')
            c = conn.cursor()
            c.execute('SELECT * FROM prodetailsdb')
            check_db = c.fetchall()
            if self.screen.ids.sort_label_backup.text == 'Products':
                if self.screen.ids.show_more_check_backup.state == 'down':
                    with open('backup.csv','r+') as file:
                        reader = csv.reader(file)
                        all_ = []
                        for i in reader:
                            if len(i) != 0:
                                try:
                                    check = re.findall(f'{text.strip()}+',str(i[0]))
                                except:
                                    self.backslah_warn.open()
                                    obj.text = ''
                                else:
                                    if check:
                                        all_.append(i)
                else:
                    with open('backup.csv','r+') as file:
                        reader = csv.reader(file)
                        all_ = []
                        for i in reader:
                            if len(i) != 0:
                                try:
                                    check = re.findall(f'^{text.strip()}',str(i[0]))
                                except:
                                    self.backslah_warn.open()
                                    obj.text = ''
                                else:
                                    if check:
                                        all_.append(i)
            else:
                with open('backup.csv','r+') as file:
                    reader = csv.reader(file)
                    all_ = []
                    for i in reader:
                        if len(i) != 0:
                            try:
                                check = re.findall(f'^{text.strip()}',str(i[3]))
                            except:
                                self.backslah_warn.open()
                                obj.text = ''
                            else:
                                if check:
                                    all_.append(i)

            conn.commit()
            conn.close()

            self.screen.ids.rvbackup.update(all_)

    def checkbox_active_show_more_backup(self,checkbox,value):
        self.caps_search_backup(self.screen.ids.search_backup.text,self.screen.ids.search_backup)

    def pass_hide_sec(self,obj,textfield):
        if textfield.password == True:
            obj.icon = 'eye'
            textfield.password = False
            textfield.focus = True
        else:
            obj.icon = 'eye-off'
            textfield.password = True
            textfield.focus = True

    def on_enter_sec_screen(self,user_t,pass_t,icon_eye):
        icon_eye.icon = 'eye-off'
        pass_t.password = True
        conn = sqlite3.connect('BillSoft.db')
        c = conn.cursor()
        c.execute("SELECT *,oid FROM security")
        check_db = c.fetchall()
        user_t.text = check_db[0][0]
        pass_t.text = check_db[0][1]
        conn.commit()
        conn.close()

    def reset_pass(self,username,password):
        self.screen.ids.screen_manager.transition = FadeTransition()
        self.screen.ids.screen_manager.transition.clearcolor = 1,1,1,1
        self.screen.ids.screen_manager.current = 'change password screen'
        self.screen.ids.username_change.text = username
        self.curr_change_password = password

    def back_from_change_pass(self,instance=0):
        self.screen.ids.screen_manager.transition = FadeTransition()
        self.screen.ids.screen_manager.transition.clearcolor = 1,1,1,1
        self.screen.ids.screen_manager.current = 'security screen'
        if instance == 1:
            toast('No changes made')

    def confirm_pass_change(self,password,cpassword):
        if len(password.strip()) == 0 or len(cpassword.strip()) == 0:
            pass
        else:
            if len(password) > 5:
                if password == cpassword:
                    if password == self.curr_change_password:
                        self.back_from_change_pass()
                        toast('No changes made')
                        self.curr_change_password = ''
                    else:
                        self.screen.ids.err_conf_pass.text = ''
                        conn = sqlite3.connect('BillSoft.db')
                        c = conn.cursor()
                        c.execute("SELECT *,oid FROM security")
                        c.execute(f"UPDATE security SET password = '{password}' WHERE oid = 1")
                        conn.commit()
                        conn.close()
                        self.back_from_change_pass()
                        toast('Password changed')
                else:
                    self.screen.ids.err_conf_pass.text =  "* Password confirmation failed "
                    return 
            else:
                self.screen.ids.err_conf_pass.text =  "* Password should contain more than 5 characters "
                return

if __name__ == '__main__':
    application().run()   
    

