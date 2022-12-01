import dearpygui.dearpygui as dpg
from dearpygui.demo import show_demo
from licensing.models import *
from licensing.methods import Key, Helpers
from AuthHelper import AuthHelper
import time
import os

iconfig = {
    'WIN_WIDTH': 500,
    'WIN_HEIGHT': 400,
    'CUR_FILE_PATH': os.path.dirname(os.path.realpath(__file__))
}

local_key = ''
expiration = ''

dpg.create_context()

def key_cb(s,d):
    global local_key
    local_key = dpg.get_value(s)

def login_cb(s,d):
    #Your RSAPublicKey, Access Token, and ProductID from Cryptolens
    global expiration
    RSAPubKey = ''
    access_token = ''
    product_id = 17808
    auth = AuthHelper(access_token, RSAPubKey, product_id)

    if auth.authorize(local_key) == False:
        dpg.show_item(auth_fail_text)
        time.sleep(2)
        dpg.destroy_context()
    else:
        dpg.show_item(auth_pass_text)
        time.sleep(.5)
        expiration = auth.get_expiration()
        dpg.delete_item(item=main_win)
        dpg.show_item(item=win2)
        dpg.set_primary_window(win2, True)

with dpg.font_registry():
    title_font1 = dpg.add_font(iconfig['CUR_FILE_PATH'] + '\Fonts\OpenSans-Bold.ttf', 34)
    default_font = dpg.add_font(iconfig['CUR_FILE_PATH'] + '\Fonts\OpenSans-SemiBold.ttf', 20)
    icon_font = dpg.add_font(iconfig['CUR_FILE_PATH'] + '\Fonts\heydings_controls.ttf', 24)

with dpg.window(width = iconfig['WIN_WIDTH'], height = iconfig['WIN_HEIGHT'], no_title_bar=True, no_resize=True, no_move=True) as main_win:
    dpg.bind_font(default_font)

    title_text = dpg.add_text("Simple Auth Page")
    dpg.bind_item_font(title_text, title_font1)

    dpg.add_spacing(count=2, parent=main_win)

    dpg.bind_font(default_font)
    dpg.add_text("Enter your Auth Key Below:")
    local_key = dpg.add_input_text(label='', callback=key_cb)

    dpg.add_spacing(count=1, parent=main_win)
    dpg.add_button(label='Login', callback=login_cb, width=120)

    auth_fail_text = dpg.add_text('Login Failed', show=False)
    auth_pass_text = dpg.add_text('Success', show=False)

with dpg.window(width = iconfig['WIN_WIDTH'], height = iconfig['WIN_HEIGHT'], no_title_bar=True, no_resize=True, no_move=True, show=False) as win2:
    dpg.bind_font(default_font)

    title_text = dpg.add_text("Successful")
    dpg.bind_item_font(title_text, title_font1)

    dpg.add_text("Your license expires on: " + expiration)

#apply_main_theme()
#show_demo()
#dpg.show_style_editor()

dpg.create_viewport(title = 'Auth Program', width = iconfig['WIN_WIDTH']+16, height = iconfig['WIN_HEIGHT']+38)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window(main_win, True)
dpg.start_dearpygui()
dpg.destroy_context()