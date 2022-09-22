from re import L
import dearpygui.dearpygui as dpg
from dearpygui.demo import show_demo
from licensing.models import *
from licensing.methods import Key, Helpers
import os
import ctypes
import sys

WIN_WIDTH = 500
WIN_HEIGHT = 400

local_key = ''

RSAPubKey = "<RSAKeyValue><Modulus>h9XdlkrJJqAKK7pLHUvCSf4RJVPwjEl51TvzJuv9hmwVjm3WlpOgBBZSSiwrlq2FHv8aHbrXks1KbWcMqiKiAjnVuI+R/OCK305aoS2fiVPyJph2cJXSgFsB3fpTn7W5mV6RhWvVko0hvlmIZckeArVNslRFKmXRCTRcFNObfJwJbZFisPZsoVTKLGG5yYo75t4Bc7/qJyOVMvIq38oRCwe7cVpOrk9GcQfaoR6ojX+Xvg6BZ2LyjppRHDOlKQvs/bKjtCD/HD0LkuwvhzTH2i4tkhKkBPVTN6JE1iZSRO50f5pn6DviaDd015zBT95S4qdJYMsWl2x7dW/vjBX/hw==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"
auth = "WyIyNTk1NjAxMyIsIjlKenZCd0ZRdDR2TWdZemRtM1JxK3ltZ0VwRkpCaXpSRjhsa3RsU1QiXQ==" #Access Token


result = Key.activate(token=auth,\
                   rsa_pub_key=RSAPubKey,\
                   product_id=16868, \
                   key=local_key,\
                   machine_code=Helpers.GetMachineCode(v=2))



#	HIWCK-BVMNM-IARBB-QAHLH

dpg.create_context()

def key_cb(s,d):
    global local_key
    local_key = dpg.get_value(s)

def login_cb(s,d):
    global result
    result = Key.activate(token=auth,\
                rsa_pub_key=RSAPubKey,\
                product_id=16868, \
                key=local_key,\
                machine_code=Helpers.GetMachineCode(v=2))

    if result[0] == None or not Helpers.IsOnRightMachine(result[0], v=2):
        #dpg.show_item(auth_fail_text)
        ctypes.windll.user32.MessageBoxW(0, "Failed", "Auth", 0)
    else:
        #dpg.show_item(auth_pass_text)
        ctypes.windll.user32.MessageBoxW(0, "Success", "Auth", 0)



with dpg.font_registry():
    title_font = dpg.add_font('C:\Windows\Fonts\Kayak Sans Bold.otf', 20)
    default_font = dpg.add_font('C:\Windows\Fonts\Kayak Sans Bold.otf', 18)

with dpg.window(width = WIN_WIDTH, height = WIN_HEIGHT, no_title_bar=True, no_resize=True, no_move=True) as main_win:
    dpg.bind_font(default_font)

    title_text = dpg.add_text("Simple Auth Page")
    local_key = dpg.add_input_text(label='Auth key:', callback=key_cb)
    dpg.add_button(label='Login', callback=login_cb)




    auth_fail_text = dpg.add_text('Failed', show=False, tag='a')
    auth_pass_text = dpg.add_text('Success', show=False, tag='b')

with dpg.window(width = WIN_WIDTH, height = WIN_HEIGHT, no_title_bar=True, no_resize=True, no_move=True, show=False) as win_2:
    dpg.bind_font(default_font)

#apply_main_theme()

#show_demo()
#dpg.show_style_editor()

dpg.create_viewport(title = 'Auth Program', width = WIN_WIDTH+16, height = WIN_HEIGHT+38)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window(main_win, True)
dpg.start_dearpygui()
dpg.destroy_context()