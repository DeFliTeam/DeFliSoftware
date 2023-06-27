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
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////


from application.gui.core.functions import Functions
from application.gui.widgets import PyPushButton


def create_page_1_widgets(object):
    object.push_button_lets_go = PyPushButton(
        text="Start -->",
        radius=8,
        color=object.themes["app_color"]["dark_one"],
        bg_color=object.themes["app_color"]["neon_red"],
        bg_color_hover=object.themes["app_color"]["dark_one"],
        font_color_hover=object.themes["app_color"]["neon_red"],
        bg_color_pressed=object.themes["app_color"]["dark_four"]
    )
    object.push_button_lets_go.setMinimumHeight(40)
    object.logo_png = QPixmap(Functions.set_png_image("logo_home.png"))
    image_label = QLabel()
    object.ui.load_pages.logo_layout.addWidget(image_label, Qt.AlignCenter, Qt.AlignCenter)
    image_label.setPixmap(object.logo_png)
    object.ui.load_pages.btn_start_layout.addWidget(object.push_button_lets_go)
    return object
