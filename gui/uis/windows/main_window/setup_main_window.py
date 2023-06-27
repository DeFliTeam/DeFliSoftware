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

from application.gui.uis.windows.main_window import UI_MainWindow
from application.business_logic.business_logic import go_to_page_2, go_to_page_1, go_to_page_4, reset, start, \
    on_latitude_longitude_changed, on_ip_address_changed, set_location_and_autogain, close_window, \
    look_for_ip_address_change, autofill_ip_address
from application.gui.core.functions import Functions
# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////

# from .functions_main_window import *

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////


# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from application.gui.core.json_settings import Settings

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from application.gui.core.json_themes import Themes
from application.gui.uis.windows.main_window.functions_main_window import MainFunctions
from application.gui.widgets import PyGrips


# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
# from .functions_main_window import MainFunctions
from .setup_page_1 import create_page_1_widgets
from .setup_page_2 import create_page_2_widgets
from .setup_page_4 import create_page_4_widgets


# from .setup_page_3 import create_page_3_widgets
# from .setup_page_4 import create_page_4_widgets

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////

# MAIN FUNCTIONS 
# ///////////////////////////////////////////////////////////////


# PY WINDOW
# ///////////////////////////////////////////////////////////////
class SetupMainWindow:
    def __init__(self, parent, skip_ui_setup=False):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        if not skip_ui_setup:
            self.ui = UI_MainWindow()
            self.ui.setup_ui(self)

        self.parent = parent
        self.ui = self.parent.ui

    # ADD LEFT MENUS
    # ///////////////////////////////////////////////////////////////
    add_left_menus = [
        {
            "btn_icon": "icon_home.svg",
            "btn_id": "btn_home",
            "btn_text": "Home",
            "btn_tooltip": "Home page",
            "show_top": True,
            "is_active": True
        },

    ]

    # ADD TITLE BAR MENUS
    # ///////////////////////////////////////////////////////////////
    add_title_bar_menus = [
    ]

    # SETUP CUSTOM BTNs OF CUSTOM WIDGETS
    # Get sender() function when btn is clicked
    # ///////////////////////////////////////////////////////////////
    def setup_btns(self):
        if self.ui.title_bar.sender() != None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() != None:
            return self.ui.left_menu.sender()
        elif self.ui.left_column.sender() != None:
            return self.ui.left_column.sender()

    # SETUP MAIN WINDOW WITH CUSTOM PARAMETERS
    # ///////////////////////////////////////////////////////////////


    def setup_gui(self):
        # APP TITLE
        # ///////////////////////////////////////////////////////////////
        self.parent.setWindowTitle(self.parent.settings["app_name"])

        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        if self.parent.settings["custom_title_bar"]:
            self.parent.setWindowFlag(Qt.FramelessWindowHint)
            self.parent.setAttribute(Qt.WA_TranslucentBackground)

        # ADD GRIPS
        # ///////////////////////////////////////////////////////////////
        if self.parent.settings["custom_title_bar"]:
            self.parent.left_grip = PyGrips(self.parent, "left", self.parent.hide_grips)
            self.parent.right_grip = PyGrips(self.parent, "right", self.parent.hide_grips)
            self.parent.top_grip = PyGrips(self.parent, "top", self.parent.hide_grips)
            self.parent.bottom_grip = PyGrips(self.parent, "bottom", self.parent.hide_grips)
            self.parent.top_left_grip = PyGrips(self.parent, "top_left", self.parent.hide_grips)
            self.parent.top_right_grip = PyGrips(self.parent, "top_right", self.parent.hide_grips)
            self.parent.bottom_left_grip = PyGrips(self.parent, "bottom_left", self.parent.hide_grips)
            self.parent.bottom_right_grip = PyGrips(self.parent, "bottom_right", self.parent.hide_grips)

        # LEFT MENUS / GET SIGNALS WHEN LEFT MENU BTN IS CLICKED / RELEASED
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.parent.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)

        # SET SIGNALS
        self.parent.ui.left_menu.clicked.connect(self.parent.btn_clicked)
        self.parent.ui.left_menu.released.connect(self.parent.btn_released)

        # TITLE BAR / ADD EXTRA BUTTONS
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.parent.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

        # SET SIGNALS
        self.parent.ui.title_bar.clicked.connect(self.parent.btn_clicked)
        self.parent.ui.title_bar.released.connect(self.parent.btn_released)

        # ADD Title
        if self.parent.settings["custom_title_bar"]:
            self.parent.ui.title_bar.set_title(self.parent.settings["app_name"])
        else:
            self.parent.ui.title_bar.set_title("Welcome to " + self.parent.settings["app_name"])

        # LEFT COLUMN SET SIGNALS
        # ///////////////////////////////////////////////////////////////
        self.parent.ui.left_column.clicked.connect(self.parent.btn_clicked)
        self.parent.ui.left_column.released.connect(self.parent.btn_released)

        # SET INITIAL PAGE / SET LEFT AND RIGHT COLUMN MENUS
        # ///////////////////////////////////////////////////////////////
        MainFunctions.set_page(self.parent, self.parent.ui.load_pages.page_1)
        MainFunctions.set_left_column_menu(
            self.parent,
            menu=self.parent.ui.left_column.menus.menu_1,
            title="Settings Left Column",
            icon_path=Functions.set_svg_icon("icon_settings.svg")
        )
        MainFunctions.set_right_column_menu(self.parent, self.parent.ui.right_column.menu_1)


        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        # PAGES
        # ///////////////////////////////////////////////////////////////

        # PAGE 1 - ADD LOGO TO MAIN PAGE

        self = create_page_1_widgets(self)

        # PAGE 2
        self = create_page_2_widgets(self)

        # PAGE 3
        self = create_page_4_widgets(self)

        # ///////////////////////////////////////////////////////////////
        # END - EXAMPLE CUSTOM WIDGETS
        # ///////////////////////////////////////////////////////////////

        # ----------------------------Connections------------------------
        self.push_button_lets_go.clicked.connect(lambda: go_to_page_2(self))
        self.push_button_lets_go.clicked.connect(lambda: autofill_ip_address(self))

        self.push_button_step_1.clicked.connect(lambda: set_location_and_autogain(self))
        self.push_button_step_2.clicked.connect(lambda: look_for_ip_address_change(self))
        self.push_button_back_pg_2.clicked.connect(lambda: go_to_page_1(self))
        self.push_button_back_pg_2.clicked.connect(lambda: reset(self))
        self.push_button_next_pg_2.clicked.connect(lambda: go_to_page_4(self))
        self.push_button_next_pg_2.clicked.connect(lambda: start(self))

        self.lineedit_latitude.textChanged.connect(lambda: on_latitude_longitude_changed(self))
        self.lineedit_longitude.textChanged.connect(lambda: on_latitude_longitude_changed(self))

        self.lineedit_ip_address.textChanged.connect(lambda: on_ip_address_changed(self))

        # self.push_button_next_pg_4.clicked.connect(lambda: close_window())
        self.push_button_next_pg_4.clicked.connect(lambda: close_window(self))
        self.push_button_next_pg_4.clicked.connect(lambda: reset(self))

    # RESIZE GRIPS AND CHANGE POSITION
    # Resize or change position when window is resized
    # ///////////////////////////////////////////////////////////////
    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)
