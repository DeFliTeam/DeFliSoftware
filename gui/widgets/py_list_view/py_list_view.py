# ///////////////////////////////////////////////////////////////
#
# BY: Mihir S.Shah
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
import os.path

from PyQt5.QtCore import QSize, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QListWidget, QAbstractItemView, QListWidgetItem

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////

from application.gui.core.functions import Functions


class PyListView(QListWidget):

    def __init__(self,
                 parent,
                 font_size = '15px'):
        super(PyListView, self).__init__(parent)
        self.setAcceptDrops(True)
        self.setIconSize(QSize(100, 100))
        self.setStyleSheet(f'font-size: {font_size}')
        self.setUniformItemSizes(True)
        # self.itemClicked.connect(self.print_selected_entry)
        self.setDragDropMode(QAbstractItemView.InternalMove)
        self.folder_icon = QPixmap(Functions.set_svg_icon("icon_folder.svg"))
        self.folder_icon.scaled(20, 20)
        self.file_icon = QPixmap(Functions.set_svg_icon("icon_file.svg"))
        self.file_icon.scaled(20, 20)
        self.no_icon = QPixmap(Functions.set_svg_icon("no_icon.svg"))
        self.no_icon.scaled(20, 20)
        # self.full_list = list()
        self.current_items_names = set()
        self.current_items = set()
        self.path_dict = dict()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            super(PyListView, self).dragEnterEvent(event)
            # event.ignore()

    def dragMoveEvent(self, event):
        super(PyListView, self).dragMoveEvent(event)

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            links = []
            for i, url in enumerate(event.mimeData().urls()):
                full_path = str(url.toLocalFile())
                temp_icon = self.get_icon_for(full_path)
                if self.is_already_added(full_path):
                    continue

                self.add_item(full_path, temp_icon)

            self.emit(pyqtSignal("dropped"), links)
            event.acceptProposedAction()
        else:
            super(PyListView, self).dropEvent(event)

    def add_item(self, full_path, temp_icon):
        name = os.path.split(full_path)[1]

        if not self.is_name_unique(name):
            name = self.get_unique_name(name, full_path)

        self.current_items_names.add(name)

        self.current_items.add(full_path)
        self.path_dict[name] = full_path
        if temp_icon:
            list_item = QListWidgetItem(temp_icon, name)
        else:
            list_item = QListWidgetItem(name)
        current_count = self.count()
        self.insertItem(current_count + 1, list_item)

    def get_icon_for(self, full_path):
        if os.path.isfile(full_path):
            return self.file_icon
        elif os.path.isdir(full_path):
            return self.folder_icon
        else:
            return self.no_icon

    def print_selected_entry(self, *args, **kwargs):
        print("Selected Entry: ", args[0].text())

    def is_already_added(self, full_path):
        return full_path in self.current_items

    def is_name_unique(self, name):
        return not(name in self.current_items_names)

    def get_unique_name(self, name, new_path):
        already_added = self.path_dict.get(name)
        return os.path.relpath(new_path, already_added)

    def get_data(self):
        return [self.path_dict[self.item(index).text()] for index in range(self.count())]

    def reset(self):
        if self.count() > 0:
            self.clear()
            self.path_dict = dict()
