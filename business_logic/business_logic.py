import os
import sys
import traceback
from multiprocessing import Process
from threading import Thread

from PyQt5.QtWidgets import QMessageBox

from application.business_logic.ip_address_check import IpChecker
from application.gui.uis.windows.main_window.functions_main_window import MainFunctions

ip_checker = IpChecker()
def catch_error(func):
    def inner_func(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(type(e).__name__)
            error_msg = str(e)
            error_msg += "\n\n\n\n"
            error_msg += str(traceback.format_exc())
            msg.setInformativeText(error_msg)
            msg.setWindowTitle(type(e).__name__)
            msg.exec_()

    return inner_func


@catch_error
def go_to_page_1(main_window_object):
    MainFunctions.set_page(main_window_object, main_window_object.ui.load_pages.page_1)


@catch_error
def go_to_page_2(main_window_object):
    MainFunctions.set_page(main_window_object, main_window_object.ui.load_pages.page_2)


@catch_error
def go_to_page_3(main_window_object):
    MainFunctions.set_page(main_window_object, main_window_object.ui.load_pages.page_3)


@catch_error
def go_to_page_4(main_window_object):
    MainFunctions.set_page(main_window_object, main_window_object.ui.load_pages.page_4)


@catch_error
def set_location_and_autogain(setup_window_object):
    set_location(setup_window_object)
    start_autogain(setup_window_object)
    setup_window_object.step_1_complete = True


@catch_error
def set_location(setup_window_object):
    text_latitude = setup_window_object.lineedit_latitude.text()
    text_longitude = setup_window_object.lineedit_longitude.text()
    command = f"sudo readsb-set-location {text_latitude} {text_longitude}"
    print(command)
    os.system(command)
    print("Set_Location")


@catch_error
def start_autogain(setup_window_object):
    command = "sudo autogain1090"
    print(command)
    os.system(command)
    print("Autogain")


# @catch_error
# def set_ip_address(setup_window_object):
#     print("Set_IP_Address")
#     setup_window_object.step_2_complete = True


@catch_error
def autofill_ip_address(setup_window_object):
    setup_window_object.lineedit_ip_address.setText(ip_checker.current_ip_address)


@catch_error
def look_for_ip_address_change(setup_window_object):
    text_ip_address = setup_window_object.lineedit_ip_address.text()
    t = Thread(target=ip_checker.start_for_ip_address, args= (text_ip_address, ), daemon=True)
    t.start()
    print("Serving Forever To Check IP_Change")
    setup_window_object.step_2_complete = True


@catch_error
def check_for_next_step_enable_pg_2(setup_window_object):
    if setup_window_object.push_button_step_1.isEnabled() and setup_window_object.push_button_step_2.isEnabled():
        setup_window_object.push_button_next_pg_2.setEnabled(True)
    else:
        setup_window_object.push_button_next_pg_2.setEnabled(False)


@catch_error
def on_latitude_longitude_changed(setup_window_object):
    text_latitude = setup_window_object.lineedit_latitude.text()
    text_longitude = setup_window_object.lineedit_longitude.text()
    setup_window_object.step_1_complete = False

    if text_longitude and text_latitude:
        if text_longitude != "" and text_latitude != "":
            setup_window_object.push_button_step_1.setEnabled(True)
        else:
            setup_window_object.push_button_step_1.setEnabled(False)
    else:
        setup_window_object.push_button_step_1.setEnabled(False)
    check_for_next_step_enable_pg_2(setup_window_object)


@catch_error
def on_ip_address_changed(setup_window_object):
    text_ip_address = setup_window_object.lineedit_ip_address.text()
    split_text = text_ip_address.split('.')
    setup_window_object.step_2_complete = False

    if text_ip_address:
        if len(split_text) == 4 and split_text[0] != "" and split_text[1] != "" and split_text[2] != "" and split_text[
            3] != "":
            setup_window_object.push_button_step_2.setEnabled(True)

        else:
            setup_window_object.push_button_step_2.setEnabled(False)
    else:
        setup_window_object.push_button_step_2.setEnabled(False)
    check_for_next_step_enable_pg_2(setup_window_object)


@catch_error
def start(setup_window_object):
    if not setup_window_object.step_1_complete:
        set_location_and_autogain(setup_window_object)

    if not setup_window_object.step_2_complete:
        look_for_ip_address_change(setup_window_object)

    setup_window_object.title_label_pg_4.setText("Finished..!")
    setup_window_object.push_button_next_pg_4.setText("Close")
    ip_address = ip_checker.current_ip_address
    msg = f"Visit your homepage at {ip_address}/tar1090.\nYou can see your data at {ip_address}/graphs1090,\nCreate your wallet at wallet.defli.network."
    setup_window_object.ui.load_pages.row_status_label.setText(msg)
    setup_window_object.push_button_next_pg_4.setEnabled(True)
    # ToDo: Remove printing functions and use logger instead.


@catch_error
def reset(setup_window_object):
    pass


@catch_error
def close_window(setup_window_object):
    setup_window_object.parent.win.close()
    # sys.exit()


class DefliException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
