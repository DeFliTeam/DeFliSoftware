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
from PyQt5.QtCore import QSize, Qt, QRect, QCoreApplication, QMetaObject
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QVBoxLayout, QStackedWidget, QSizePolicy, QWidget, QFrame, QSpacerItem, QLabel, \
    QScrollArea, QHBoxLayout, QLayout


# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(996, 753)
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pages.sizePolicy().hasHeightForWidth())
        self.pages.setSizePolicy(sizePolicy)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"font-size: 14pt")
        self.horizontalLayout = QHBoxLayout(self.page_1)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.welcome_base = QFrame(self.page_1)
        self.welcome_base.setObjectName(u"welcome_base")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.welcome_base.sizePolicy().hasHeightForWidth())
        self.welcome_base.setSizePolicy(sizePolicy1)
        self.welcome_base.setMinimumSize(QSize(300, 300))
        self.welcome_base.setMaximumSize(QSize(300, 150))
        self.welcome_base.setFrameShape(QFrame.NoFrame)
        self.welcome_base.setFrameShadow(QFrame.Raised)
        self.center_page_layout = QVBoxLayout(self.welcome_base)
        self.center_page_layout.setSpacing(10)
        self.center_page_layout.setObjectName(u"center_page_layout")
        self.center_page_layout.setContentsMargins(0, 0, 0, 0)
        self.logo = QFrame(self.welcome_base)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(300, 120))
        self.logo.setMaximumSize(QSize(300, 120))
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setFrameShadow(QFrame.Raised)
        self.logo_layout = QVBoxLayout(self.logo)
        self.logo_layout.setSpacing(0)
        self.logo_layout.setObjectName(u"logo_layout")
        self.logo_layout.setContentsMargins(0, 0, 0, 0)

        self.center_page_layout.addWidget(self.logo)

        self.vSpacer_logo_lalbel = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.center_page_layout.addItem(self.vSpacer_logo_lalbel)

        self.label = QLabel(self.welcome_base)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.center_page_layout.addWidget(self.label)

        self.vSpacer_label_btn = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.center_page_layout.addItem(self.vSpacer_label_btn)

        self.btn_start_frame = QFrame(self.welcome_base)
        self.btn_start_frame.setObjectName(u"btn_start_frame")
        sizePolicy1.setHeightForWidth(self.btn_start_frame.sizePolicy().hasHeightForWidth())
        self.btn_start_frame.setSizePolicy(sizePolicy1)
        self.btn_start_frame.setMinimumSize(QSize(0, 50))
        self.btn_start_frame.setFrameShape(QFrame.StyledPanel)
        self.btn_start_frame.setFrameShadow(QFrame.Raised)
        self.btn_start_layout = QVBoxLayout(self.btn_start_frame)
        self.btn_start_layout.setObjectName(u"btn_start_layout")

        self.center_page_layout.addWidget(self.btn_start_frame)


        self.horizontalLayout.addWidget(self.welcome_base)

        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.page_2.sizePolicy().hasHeightForWidth())
        self.page_2.setSizePolicy(sizePolicy2)
        self.page_2_layout = QVBoxLayout(self.page_2)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.scroll_area_pg_2 = QScrollArea(self.page_2)
        self.scroll_area_pg_2.setObjectName(u"scroll_area_pg_2")
        self.scroll_area_pg_2.setStyleSheet(u"background: transparent;")
        self.scroll_area_pg_2.setFrameShape(QFrame.NoFrame)
        self.scroll_area_pg_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_pg_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_pg_2.setWidgetResizable(True)
        self.contents_pg_2 = QWidget()
        self.contents_pg_2.setObjectName(u"contents_pg_2")
        self.contents_pg_2.setGeometry(QRect(0, 0, 232, 299))
        self.contents_pg_2.setStyleSheet(u"background: transparent;")
        self.verticalLayout = QVBoxLayout(self.contents_pg_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.LogoAndTitle_pg_2 = QHBoxLayout()
        self.LogoAndTitle_pg_2.setObjectName(u"LogoAndTitle_pg_2")
        self.LogoAndTitle_pg_2.setSizeConstraint(QLayout.SetFixedSize)
        self.title_label_pg_2 = QLabel(self.contents_pg_2)
        self.title_label_pg_2.setObjectName(u"title_label_pg_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.title_label_pg_2.sizePolicy().hasHeightForWidth())
        self.title_label_pg_2.setSizePolicy(sizePolicy3)
        self.title_label_pg_2.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(16)
        self.title_label_pg_2.setFont(font)
        self.title_label_pg_2.setStyleSheet(u"font-size: 16pt")
        self.title_label_pg_2.setAlignment(Qt.AlignCenter)

        self.LogoAndTitle_pg_2.addWidget(self.title_label_pg_2)


        self.verticalLayout.addLayout(self.LogoAndTitle_pg_2)

        self.verticalSpacer_title_conent_pg_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_title_conent_pg_2)

        self.step1_title = QHBoxLayout()
        self.step1_title.setObjectName(u"step1_title")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.step1_title.addItem(self.horizontalSpacer)

        self.step1_title_label = QLabel(self.contents_pg_2)
        self.step1_title_label.setObjectName(u"step1_title_label")

        self.step1_title.addWidget(self.step1_title_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.step1_title.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.step1_title)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.row_1_pg_2 = QHBoxLayout()
        self.row_1_pg_2.setObjectName(u"row_1_pg_2")
        self.row1_column1_pg_2 = QFrame(self.contents_pg_2)
        self.row1_column1_pg_2.setObjectName(u"row1_column1_pg_2")
        self.row1_column1_pg_2.setFrameShape(QFrame.NoFrame)
        self.row1_column1_pg_2.setFrameShadow(QFrame.Raised)
        self.row1_column1_pg_2_layout = QVBoxLayout(self.row1_column1_pg_2)
        self.row1_column1_pg_2_layout.setSpacing(0)
        self.row1_column1_pg_2_layout.setObjectName(u"row1_column1_pg_2_layout")
        self.row1_column1_pg_2_layout.setContentsMargins(0, 0, 0, 0)

        self.row_1_pg_2.addWidget(self.row1_column1_pg_2)

        self.row1_column2_pg_2 = QFrame(self.contents_pg_2)
        self.row1_column2_pg_2.setObjectName(u"row1_column2_pg_2")
        self.row1_column2_pg_2.setFrameShape(QFrame.NoFrame)
        self.row1_column2_pg_2.setFrameShadow(QFrame.Raised)
        self.row1_column2_pg_2_layout = QVBoxLayout(self.row1_column2_pg_2)
        self.row1_column2_pg_2_layout.setSpacing(0)
        self.row1_column2_pg_2_layout.setObjectName(u"row1_column2_pg_2_layout")
        self.row1_column2_pg_2_layout.setContentsMargins(0, 0, 0, 0)

        self.row_1_pg_2.addWidget(self.row1_column2_pg_2)


        self.verticalLayout.addLayout(self.row_1_pg_2)

        self.row2_pg_2 = QHBoxLayout()
        self.row2_pg_2.setObjectName(u"row2_pg_2")
        self.row2_column1_pg_2 = QFrame(self.contents_pg_2)
        self.row2_column1_pg_2.setObjectName(u"row2_column1_pg_2")
        self.row2_column1_pg_2.setFrameShape(QFrame.NoFrame)
        self.row2_column1_pg_2.setFrameShadow(QFrame.Raised)
        self.row2_column1_pg_2_layout = QVBoxLayout(self.row2_column1_pg_2)
        self.row2_column1_pg_2_layout.setSpacing(0)
        self.row2_column1_pg_2_layout.setObjectName(u"row2_column1_pg_2_layout")
        self.row2_column1_pg_2_layout.setContentsMargins(0, 0, 0, 0)

        self.row2_pg_2.addWidget(self.row2_column1_pg_2)

        self.row2_column2_pg_2 = QFrame(self.contents_pg_2)
        self.row2_column2_pg_2.setObjectName(u"row2_column2_pg_2")
        self.row2_column2_pg_2.setFrameShape(QFrame.NoFrame)
        self.row2_column2_pg_2.setFrameShadow(QFrame.Raised)
        self.row2_column2_pg_2_layout = QVBoxLayout(self.row2_column2_pg_2)
        self.row2_column2_pg_2_layout.setSpacing(0)
        self.row2_column2_pg_2_layout.setObjectName(u"row2_column2_pg_2_layout")
        self.row2_column2_pg_2_layout.setContentsMargins(0, 0, 0, 0)

        self.row2_pg_2.addWidget(self.row2_column2_pg_2)


        self.verticalLayout.addLayout(self.row2_pg_2)

        self.row3_pg_2 = QHBoxLayout()
        self.row3_pg_2.setObjectName(u"row3_pg_2")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.row3_pg_2.addItem(self.horizontalSpacer_5)

        self.row3_column1_pg_2 = QFrame(self.contents_pg_2)
        self.row3_column1_pg_2.setObjectName(u"row3_column1_pg_2")
        self.row3_column1_pg_2.setFrameShape(QFrame.StyledPanel)
        self.row3_column1_pg_2.setFrameShadow(QFrame.Raised)
        self.row3_column1_pg_2_layout = QVBoxLayout(self.row3_column1_pg_2)
        self.row3_column1_pg_2_layout.setObjectName(u"row3_column1_pg_2_layout")

        self.row3_pg_2.addWidget(self.row3_column1_pg_2)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.row3_pg_2.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.row3_pg_2)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.step2_title = QHBoxLayout()
        self.step2_title.setObjectName(u"step2_title")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.step2_title.addItem(self.horizontalSpacer_3)

        self.step2_title_label = QLabel(self.contents_pg_2)
        self.step2_title_label.setObjectName(u"step2_title_label")

        self.step2_title.addWidget(self.step2_title_label)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.step2_title.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.step2_title)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.row4_pg_2 = QHBoxLayout()
        self.row4_pg_2.setObjectName(u"row4_pg_2")
        self.row4_pg_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.row4_column1_pg_2 = QFrame(self.contents_pg_2)
        self.row4_column1_pg_2.setObjectName(u"row4_column1_pg_2")
        self.row4_column1_pg_2.setFrameShape(QFrame.StyledPanel)
        self.row4_column1_pg_2.setFrameShadow(QFrame.Raised)
        self.row4_column1_pg_2_layout = QVBoxLayout(self.row4_column1_pg_2)
        self.row4_column1_pg_2_layout.setObjectName(u"row4_column1_pg_2_layout")

        self.row4_pg_2.addWidget(self.row4_column1_pg_2)

        self.row4_column2_pg_2 = QFrame(self.contents_pg_2)
        self.row4_column2_pg_2.setObjectName(u"row4_column2_pg_2")
        self.row4_column2_pg_2.setFrameShape(QFrame.StyledPanel)
        self.row4_column2_pg_2.setFrameShadow(QFrame.Raised)
        self.row4_column2_pg_2_layout = QVBoxLayout(self.row4_column2_pg_2)
        self.row4_column2_pg_2_layout.setObjectName(u"row4_column2_pg_2_layout")

        self.row4_pg_2.addWidget(self.row4_column2_pg_2)


        self.verticalLayout.addLayout(self.row4_pg_2)

        self.row5_pg_2 = QHBoxLayout()
        self.row5_pg_2.setObjectName(u"row5_pg_2")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.row5_pg_2.addItem(self.horizontalSpacer_7)

        self.row5_column1_pg_2 = QFrame(self.contents_pg_2)
        self.row5_column1_pg_2.setObjectName(u"row5_column1_pg_2")
        self.row5_column1_pg_2.setFrameShape(QFrame.StyledPanel)
        self.row5_column1_pg_2.setFrameShadow(QFrame.Raised)
        self.row5_column1_pg_2_layout = QVBoxLayout(self.row5_column1_pg_2)
        self.row5_column1_pg_2_layout.setObjectName(u"row5_column1_pg_2_layout")

        self.row5_pg_2.addWidget(self.row5_column1_pg_2)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.row5_pg_2.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addLayout(self.row5_pg_2)

        self.vSpaver_content_navigation_pg_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.vSpaver_content_navigation_pg_2)

        self.row_navigation_layout_pg_2 = QHBoxLayout()
        self.row_navigation_layout_pg_2.setObjectName(u"row_navigation_layout_pg_2")
        self.row_navigation_layout_pg_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.row_navigation_layout_pg_2.setContentsMargins(-1, -1, 0, 0)
        self.navigationBarSpacer_pg_2 = QFrame(self.contents_pg_2)
        self.navigationBarSpacer_pg_2.setObjectName(u"navigationBarSpacer_pg_2")
        self.navigationBarSpacer_pg_2.setMinimumSize(QSize(200, 0))
        self.navigationBarSpacer_pg_2.setFrameShape(QFrame.NoFrame)
        self.navigationBarSpacer_pg_2.setFrameShadow(QFrame.Raised)
        self.navigationBarSpacerLayout_pg_2 = QVBoxLayout(self.navigationBarSpacer_pg_2)
        self.navigationBarSpacerLayout_pg_2.setSpacing(0)
        self.navigationBarSpacerLayout_pg_2.setObjectName(u"navigationBarSpacerLayout_pg_2")
        self.navigationBarSpacerLayout_pg_2.setContentsMargins(0, 0, 0, 0)
        self.hSpacerNavBar_pg_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.navigationBarSpacerLayout_pg_2.addItem(self.hSpacerNavBar_pg_2)


        self.row_navigation_layout_pg_2.addWidget(self.navigationBarSpacer_pg_2)

        self.navigationBarBack_pg_2 = QFrame(self.contents_pg_2)
        self.navigationBarBack_pg_2.setObjectName(u"navigationBarBack_pg_2")
        self.navigationBarBack_pg_2.setFrameShape(QFrame.NoFrame)
        self.navigationBarBack_pg_2.setFrameShadow(QFrame.Raised)
        self.navigationBarBackLayout_pg_2 = QVBoxLayout(self.navigationBarBack_pg_2)
        self.navigationBarBackLayout_pg_2.setSpacing(0)
        self.navigationBarBackLayout_pg_2.setObjectName(u"navigationBarBackLayout_pg_2")
        self.navigationBarBackLayout_pg_2.setContentsMargins(0, -1, 0, 0)

        self.row_navigation_layout_pg_2.addWidget(self.navigationBarBack_pg_2)

        self.navigationBarNext_pg_2 = QFrame(self.contents_pg_2)
        self.navigationBarNext_pg_2.setObjectName(u"navigationBarNext_pg_2")
        self.navigationBarNext_pg_2.setFrameShape(QFrame.NoFrame)
        self.navigationBarNext_pg_2.setFrameShadow(QFrame.Raised)
        self.navigationBarNextLayout_pg_2 = QVBoxLayout(self.navigationBarNext_pg_2)
        self.navigationBarNextLayout_pg_2.setObjectName(u"navigationBarNextLayout_pg_2")
        self.navigationBarNextLayout_pg_2.setContentsMargins(0, -1, 0, 0)

        self.row_navigation_layout_pg_2.addWidget(self.navigationBarNext_pg_2)


        self.verticalLayout.addLayout(self.row_navigation_layout_pg_2)

        self.scroll_area_pg_2.setWidget(self.contents_pg_2)

        self.page_2_layout.addWidget(self.scroll_area_pg_2)

        self.pages.addWidget(self.page_2)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4_layout = QVBoxLayout(self.page_4)
        self.page_4_layout.setObjectName(u"page_4_layout")
        self.scroll_area_pg_4 = QScrollArea(self.page_4)
        self.scroll_area_pg_4.setObjectName(u"scroll_area_pg_4")
        self.scroll_area_pg_4.setStyleSheet(u"background: transparent;")
        self.scroll_area_pg_4.setFrameShape(QFrame.NoFrame)
        self.scroll_area_pg_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_pg_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_pg_4.setWidgetResizable(True)
        self.contents_pg_4 = QWidget()
        self.contents_pg_4.setObjectName(u"contents_pg_4")
        self.contents_pg_4.setGeometry(QRect(0, 0, 968, 725))
        self.contents_pg_4.setStyleSheet(u"background: transparent;")
        self.verticalLayout_4 = QVBoxLayout(self.contents_pg_4)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.LogoAndTitle_pg_4 = QHBoxLayout()
        self.LogoAndTitle_pg_4.setObjectName(u"LogoAndTitle_pg_4")
        self.LogoAndTitle_pg_4.setSizeConstraint(QLayout.SetFixedSize)
        self.title_label_pg_4 = QLabel(self.contents_pg_4)
        self.title_label_pg_4.setObjectName(u"title_label_pg_4")
        sizePolicy3.setHeightForWidth(self.title_label_pg_4.sizePolicy().hasHeightForWidth())
        self.title_label_pg_4.setSizePolicy(sizePolicy3)
        self.title_label_pg_4.setMaximumSize(QSize(16777215, 40))
        self.title_label_pg_4.setFont(font)
        self.title_label_pg_4.setStyleSheet(u"font-size: 16pt")
        self.title_label_pg_4.setAlignment(Qt.AlignCenter)

        self.LogoAndTitle_pg_4.addWidget(self.title_label_pg_4)


        self.verticalLayout_4.addLayout(self.LogoAndTitle_pg_4)

        self.verticalSpacer_title_conent_pg_4 = QSpacerItem(20, 150, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_4.addItem(self.verticalSpacer_title_conent_pg_4)

        self.row_1_layout_pg_4 = QHBoxLayout()
        self.row_1_layout_pg_4.setObjectName(u"row_1_layout_pg_4")
        self.row_1_layout_pg_4.setSizeConstraint(QLayout.SetMinimumSize)
        self.content_column1_pg_4 = QFrame(self.contents_pg_4)
        self.content_column1_pg_4.setObjectName(u"content_column1_pg_4")
        self.content_column1_pg_4.setFrameShape(QFrame.StyledPanel)
        self.content_column1_pg_4.setFrameShadow(QFrame.Raised)
        self.content_column1_pg_4_layout = QVBoxLayout(self.content_column1_pg_4)
        self.content_column1_pg_4_layout.setObjectName(u"content_column1_pg_4_layout")

        self.row_1_layout_pg_4.addWidget(self.content_column1_pg_4)

        self.row_1_layout_pg_4.setStretch(0, 10)

        self.verticalLayout_4.addLayout(self.row_1_layout_pg_4)

        self.verticalSpacer_4 = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.row_status = QHBoxLayout()
        self.row_status.setObjectName(u"row_status")
        self.row_status_label = QLabel(self.contents_pg_4)
        self.row_status_label.setObjectName(u"row_status_label")

        self.row_status.addWidget(self.row_status_label)


        self.verticalLayout_4.addLayout(self.row_status)

        self.vSpaver_content_navigation_pg_4 = QSpacerItem(20, 150, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_4.addItem(self.vSpaver_content_navigation_pg_4)

        self.row_2_layout_pg_4 = QHBoxLayout()
        self.row_2_layout_pg_4.setObjectName(u"row_2_layout_pg_4")
        self.row_2_layout_pg_4.setSizeConstraint(QLayout.SetMinimumSize)
        self.row_2_layout_pg_4.setContentsMargins(-1, -1, 0, 0)
        self.navigationBarSpacer_pg_4 = QFrame(self.contents_pg_4)
        self.navigationBarSpacer_pg_4.setObjectName(u"navigationBarSpacer_pg_4")
        self.navigationBarSpacer_pg_4.setMinimumSize(QSize(200, 0))
        self.navigationBarSpacer_pg_4.setFrameShape(QFrame.StyledPanel)
        self.navigationBarSpacer_pg_4.setFrameShadow(QFrame.Raised)
        self.navigationBarSpacerLayout_pg_4 = QVBoxLayout(self.navigationBarSpacer_pg_4)
        self.navigationBarSpacerLayout_pg_4.setObjectName(u"navigationBarSpacerLayout_pg_4")
        self.hSpacerNavBar_pg_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.navigationBarSpacerLayout_pg_4.addItem(self.hSpacerNavBar_pg_4)


        self.row_2_layout_pg_4.addWidget(self.navigationBarSpacer_pg_4)

        self.navigationBarBack_pg_4 = QFrame(self.contents_pg_4)
        self.navigationBarBack_pg_4.setObjectName(u"navigationBarBack_pg_4")
        self.navigationBarBack_pg_4.setFrameShape(QFrame.StyledPanel)
        self.navigationBarBack_pg_4.setFrameShadow(QFrame.Raised)
        self.navigationBarBackLayout_pg_4 = QVBoxLayout(self.navigationBarBack_pg_4)
        self.navigationBarBackLayout_pg_4.setObjectName(u"navigationBarBackLayout_pg_4")

        self.row_2_layout_pg_4.addWidget(self.navigationBarBack_pg_4)

        self.navigationBarNext_pg_4 = QFrame(self.contents_pg_4)
        self.navigationBarNext_pg_4.setObjectName(u"navigationBarNext_pg_4")
        self.navigationBarNext_pg_4.setFrameShape(QFrame.StyledPanel)
        self.navigationBarNext_pg_4.setFrameShadow(QFrame.Raised)
        self.navigationBarNextLayout_pg_4 = QVBoxLayout(self.navigationBarNext_pg_4)
        self.navigationBarNextLayout_pg_4.setObjectName(u"navigationBarNextLayout_pg_4")

        self.row_2_layout_pg_4.addWidget(self.navigationBarNext_pg_4)


        self.verticalLayout_4.addLayout(self.row_2_layout_pg_4)

        self.scroll_area_pg_4.setWidget(self.contents_pg_4)

        self.page_4_layout.addWidget(self.scroll_area_pg_4)

        self.pages.addWidget(self.page_4)

        self.main_pages_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label.setText(QCoreApplication.translate("MainPages", u"Install assistant for DeFli", None))
        self.title_label_pg_2.setText(QCoreApplication.translate("MainPages", u"Installation Steps", None))
        self.step1_title_label.setText(QCoreApplication.translate("MainPages", u"Step1: Set Location", None))
        self.step2_title_label.setText(QCoreApplication.translate("MainPages", u"Step2: Set IP Address", None))
        self.title_label_pg_4.setText(QCoreApplication.translate("MainPages", u"Setting Up....", None))
        self.row_status_label.setText("")
    # retranslateUi

