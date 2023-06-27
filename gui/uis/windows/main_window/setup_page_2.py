# ///////////////////////////////////////////////////////////////
#
# BY: Mihir S. Shah
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////
# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QIcon, QIntValidator, QRegExpValidator
from PyQt5.QtWidgets import QTreeWidget, QLabel

from application.gui.core.functions import Functions
from application.gui.widgets import PyPushButton, PyLineEdit
from application.gui.widgets.py_list_view.py_list_view import PyListView
from application.utils.helper_functions import IP4Validator


# import logging


def create_page_2_widgets(setup_window_object):
    setup_window_object.step_1_complete = False
    setup_window_object.step_2_complete = False

    setup_window_object.ui.load_pages.title_label_pg_2.setStyleSheet(f'font-size: 30px')

    # Label for Step1
    setup_window_object.ui.load_pages.step1_title_label.setStyleSheet(f'font-size: 20px')

    # Label for Latitude
    setup_window_object.label_for_latitude = QLabel("Latitude")
    setup_window_object.label_for_latitude.setStyleSheet(f'font-size: 15px')
    setup_window_object.label_for_latitude.setAlignment(Qt.AlignCenter)
    setup_window_object.label_for_latitude.setMinimumWidth(100)

    # Line Edit for Latitude
    setup_window_object.lineedit_latitude = PyLineEdit(
        text="",
        place_holder_text="Enter Latitude",
        radius=8,
        border_size=2,
        color=setup_window_object.themes["app_color"]["text_foreground"],
        selection_color=setup_window_object.themes["app_color"]["white"],
        bg_color=setup_window_object.themes["app_color"]["bg_two"],
        bg_color_active=setup_window_object.themes["app_color"]["bg_three"],
        context_color=setup_window_object.themes["app_color"]["context_color"]
    )
    setup_window_object.lineedit_latitude.setMinimumHeight(35)
    setup_window_object.lineedit_latitude.setMinimumWidth(200)
    reg_ex_latitude = QRegExp("^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?)$")
    setup_window_object.lati_validator = QRegExpValidator(reg_ex_latitude, setup_window_object.lineedit_latitude)  # Create validator.
    setup_window_object.lineedit_latitude.setValidator(setup_window_object.lati_validator)  # Set validator.
    setup_window_object.lineedit_latitude.isReady = False

    # Label for Longitude
    setup_window_object.label_for_longitude = QLabel("Longitude")
    setup_window_object.label_for_longitude.setStyleSheet(f'font-size: 15px')
    setup_window_object.label_for_longitude.setAlignment(Qt.AlignCenter)
    setup_window_object.label_for_longitude.setMinimumWidth(100)

    # Line Edit for Longitude
    setup_window_object.lineedit_longitude = PyLineEdit(
        text="",
        place_holder_text="Enter longitude",
        radius=8,
        border_size=2,
        color=setup_window_object.themes["app_color"]["text_foreground"],
        selection_color=setup_window_object.themes["app_color"]["white"],
        bg_color=setup_window_object.themes["app_color"]["bg_two"],
        bg_color_active=setup_window_object.themes["app_color"]["bg_three"],
        context_color=setup_window_object.themes["app_color"]["context_color"]
    )
    setup_window_object.lineedit_longitude.setMinimumHeight(35)
    setup_window_object.lineedit_longitude.setMinimumWidth(200)
    reg_ex_longitude = QRegExp("^[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$")
    setup_window_object.long_validator = QRegExpValidator(reg_ex_longitude, setup_window_object.lineedit_longitude)
    setup_window_object.lineedit_longitude.setValidator(setup_window_object.long_validator)  # Set validator.
    setup_window_object.lineedit_longitude.isReady = False

    # # PUSH BUTTON Step1
    setup_window_object.push_button_step_1 = PyPushButton(
        text="Update Location",
        radius=8,
        color=setup_window_object.themes["app_color"]["text_foreground"],
        bg_color=setup_window_object.themes["app_color"]["dark_two"],
        bg_color_hover=setup_window_object.themes["app_color"]["dark_one"],
        font_color_hover=setup_window_object.themes["app_color"]["neon_red"],
        bg_color_pressed=setup_window_object.themes["app_color"]["dark_four"]
    )
    setup_window_object.push_button_step_1.setMinimumHeight(35)
    setup_window_object.push_button_step_1.setMinimumWidth(400)
    setup_window_object.push_button_step_1.setEnabled(False)

    setup_window_object.ui.load_pages.step2_title_label.setStyleSheet(f'font-size: 20px')

    # Label for IP Address
    setup_window_object.label_for_ip_address = QLabel("IP Address")
    setup_window_object.label_for_ip_address.setStyleSheet(f'font-size: 15px')
    setup_window_object.label_for_ip_address.setAlignment(Qt.AlignCenter)
    setup_window_object.label_for_ip_address.setMinimumWidth(100)

    # Line Edit for Longitude
    setup_window_object.lineedit_ip_address = PyLineEdit(
        text="",
        place_holder_text="192.168.0.25",
        radius=8,
        border_size=2,
        color=setup_window_object.themes["app_color"]["text_foreground"],
        selection_color=setup_window_object.themes["app_color"]["white"],
        bg_color=setup_window_object.themes["app_color"]["bg_two"],
        bg_color_active=setup_window_object.themes["app_color"]["bg_three"],
        context_color=setup_window_object.themes["app_color"]["context_color"]
    )
    setup_window_object.lineedit_ip_address.setMinimumHeight(35)
    setup_window_object.lineedit_ip_address.setMinimumWidth(200)
    reg_ex = QRegExp("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    setup_window_object.ip_validator = QRegExpValidator(reg_ex, setup_window_object.lineedit_ip_address)
    setup_window_object.lineedit_ip_address.setValidator(setup_window_object.ip_validator)
    # ip_validator = IP4Validator()
    # setup_window_object.lineedit_ip_address.setValidator(ip_validator)
    setup_window_object.lineedit_ip_address.isReady = False

    # # PUSH BUTTON Step2
    setup_window_object.push_button_step_2 = PyPushButton(
        text="Update IP Address",
        radius=8,
        color=setup_window_object.themes["app_color"]["text_foreground"],
        bg_color=setup_window_object.themes["app_color"]["dark_two"],
        bg_color_hover=setup_window_object.themes["app_color"]["dark_one"],
        font_color_hover=setup_window_object.themes["app_color"]["neon_red"],
        bg_color_pressed=setup_window_object.themes["app_color"]["dark_four"]
    )
    setup_window_object.push_button_step_2.setMinimumHeight(35)
    setup_window_object.push_button_step_2.setMinimumWidth(400)
    setup_window_object.push_button_step_2.setEnabled(False)

    # PUSH BUTTON Back
    setup_window_object.push_button_back_pg_2 = PyPushButton(
        text="Back",
        radius=8,
        color=setup_window_object.themes["app_color"]["text_foreground"],
        bg_color=setup_window_object.themes["app_color"]["bg_two"],
        bg_color_hover=setup_window_object.themes["app_color"]["bg_three"],
        bg_color_pressed=setup_window_object.themes["app_color"]["bg_one"]
    )
    setup_window_object.push_button_back_pg_2.setMinimumHeight(35)
    setup_window_object.push_button_back_pg_2.setMinimumWidth(130)
    setup_window_object.icon_back = QIcon(Functions.set_svg_icon("icon_arrow_left.svg"))
    setup_window_object.push_button_back_pg_2.set_icon_to_left(setup_window_object.icon_back)

    # PUSH BUTTON Next
    setup_window_object.push_button_next_pg_2 = PyPushButton(
        text="Start Server",
        radius=8,
        color=setup_window_object.themes["app_color"]["dark_one"],
        bg_color=setup_window_object.themes["app_color"]["neon_red"],
        bg_color_hover=setup_window_object.themes["app_color"]["dark_one"],
        font_color_hover=setup_window_object.themes["app_color"]["neon_red"],
        bg_color_pressed=setup_window_object.themes["app_color"]["dark_four"]
    )
    setup_window_object.push_button_next_pg_2.setMinimumHeight(35)
    setup_window_object.push_button_next_pg_2.setMinimumWidth(130)
    setup_window_object.icon_next = QIcon(Functions.set_svg_icon("icon_arrow_right.svg"))
    setup_window_object.push_button_next_pg_2.set_icon_to_right(setup_window_object.icon_next)
    setup_window_object.push_button_next_pg_2.setEnabled(False)

    # ADD WIDGETS
    setup_window_object.ui.load_pages.row1_column1_pg_2_layout.addWidget(setup_window_object.label_for_latitude)
    setup_window_object.ui.load_pages.row1_column2_pg_2_layout.addWidget(setup_window_object.lineedit_latitude)

    setup_window_object.ui.load_pages.row2_column1_pg_2_layout.addWidget(setup_window_object.label_for_longitude)
    setup_window_object.ui.load_pages.row2_column2_pg_2_layout.addWidget(setup_window_object.lineedit_longitude)

    setup_window_object.ui.load_pages.row3_column1_pg_2_layout.addWidget(setup_window_object.push_button_step_1)

    setup_window_object.ui.load_pages.row4_column1_pg_2_layout.addWidget(setup_window_object.label_for_ip_address)
    setup_window_object.ui.load_pages.row4_column2_pg_2_layout.addWidget(setup_window_object.lineedit_ip_address)

    setup_window_object.ui.load_pages.row5_column1_pg_2_layout.addWidget(setup_window_object.push_button_step_2)

    setup_window_object.ui.load_pages.navigationBarBackLayout_pg_2.addWidget(setup_window_object.push_button_back_pg_2)
    setup_window_object.ui.load_pages.navigationBarNextLayout_pg_2.addWidget(setup_window_object.push_button_next_pg_2)

    return setup_window_object
