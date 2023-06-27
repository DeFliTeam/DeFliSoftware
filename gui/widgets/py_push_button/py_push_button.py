# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
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
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QLabel

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////


# STYLE
# ///////////////////////////////////////////////////////////////
style = '''
QPushButton {{
	border: none;
    padding-left: 10px;
    padding-right: 5px;
    color: {_color};
	border-radius: {_radius};	
	background-color: {_bg_color};
}}
QPushButton:hover {{
    color: {_font_color_hover};
	background-color: {_bg_color_hover};
}}
QPushButton:pressed {{	
    color: {_font_color_pressed};
	background-color: {_bg_color_pressed};
}}	
QPushButton:disabled  {{	
	background-color: {_bg_color_disabled};
}}
'''


# PY PUSH BUTTON
# ///////////////////////////////////////////////////////////////
class PyPushButton(QPushButton):
    def __init__(
            self,
            text,
            radius,
            color,
            bg_color,
            bg_color_hover,
            bg_color_pressed,
            font_color_hover=None,
            font_color_pressed=None,
            bg_color_disabled='#cec7c7',
            parent=None,
    ):
        super().__init__()

        # SET PARAMETRES
        self.setText(text)
        if parent != None:
            self.setParent(parent)
        self.setCursor(Qt.PointingHandCursor)

        if not font_color_hover:
            font_color_hover = color

        if not font_color_pressed:
            font_color_pressed = font_color_hover

        # SET STYLESHEET
        custom_style = style.format(
            _color=color,
            _radius=radius,
            _bg_color=bg_color,
            _bg_color_hover=bg_color_hover,
            _font_color_hover=font_color_hover,
            _font_color_pressed=font_color_pressed,
            _bg_color_pressed=bg_color_pressed,
            _bg_color_disabled=bg_color_disabled
        )
        self.setStyleSheet(custom_style)

    def set_icon_to_right(self, icon):
        icon_size = self.iconSize()
        # remove icon
        self.setIcon(QIcon())
        label_icon = QLabel()
        label_icon.setAttribute(Qt.WA_TranslucentBackground)
        label_icon.setAttribute(Qt.WA_TransparentForMouseEvents)
        lay = QHBoxLayout(self)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(label_icon, alignment=Qt.AlignRight)
        label_icon.setPixmap(icon.pixmap(icon_size))

    def set_icon_to_left(self, icon):
        icon_size = self.iconSize()
        # remove icon
        self.setIcon(QIcon())
        label_icon = QLabel()
        label_icon.setAttribute(Qt.WA_TranslucentBackground)
        label_icon.setAttribute(Qt.WA_TransparentForMouseEvents)
        lay = QHBoxLayout(self)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(label_icon, alignment=Qt.AlignLeft)
        label_icon.setPixmap(icon.pixmap(icon_size))
