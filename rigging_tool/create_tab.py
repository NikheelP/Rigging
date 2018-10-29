#GENERAL INFO
_version = 'V001'
_author =  'Nikheel patel'
_email  =  'spark.visualartist@gmail.com'
_last_modify = '10/28/2018'

#IMPORT MODULER
import maya.cmds as cmds
import maya.mel as mel
from PySide import QtCore
from PySide import QtGui
#import sip
import sys
from functools import partial

import controller
reload(controller)

rigging_path = 'H:/Script/Git/Rigging'
controller_icon_path = rigging_path + '/rigging_tool/controller_icon'


class CREATE:
    def __init__(self):
        self.icon_size_x = 100
        self.icon_size_y = 80
        self.button_color_x = 64
        self.button_color_y = 64
        self.button_color_z = 64


        self.controller_class = controller.CONTROLLER()
        pass

    def widget_def(self,widget_name):
        self.horizontalLayout_3 = QtGui.QHBoxLayout(widget_name)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.create_vertical_layout = QtGui.QVBoxLayout()
        self.create_vertical_layout.setObjectName("create_vertical_layout")
        self.create_tool_box = QtGui.QToolBox(widget_name)
        self.create_tool_box.setObjectName("create_tool_box")

        # CREATE TOOL BOX
        self.create_page = QtGui.QWidget()
        self.create_page.setGeometry(QtCore.QRect(0, 0, 612, 303))
        self.create_page.setObjectName("create_page")
        self.create_def()
        self.create_tool_box.addItem(self.create_page, "Create")

        # DEFORM TOOL BOX
        self.deform_page = QtGui.QWidget()
        self.deform_page.setGeometry(QtCore.QRect(0, 0, 612, 303))
        self.deform_page.setObjectName("deform_page")
        #self.deform_def()
        self.create_tool_box.addItem(self.deform_page, "Deform")

        # OBJECT TOOL BOX
        self.object_page = QtGui.QWidget()
        self.object_page.setGeometry(QtCore.QRect(0, 0, 612, 303))
        self.object_page.setObjectName("object_page")
        #self.object_def()
        self.create_tool_box.addItem(self.object_page, "Object")

        self.create_vertical_layout.addWidget(self.create_tool_box)
        self.horizontalLayout_3.addLayout(self.create_vertical_layout)


    def create_def(self):
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.create_page)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.create_scroll_area = QtGui.QScrollArea(self.create_page)
        self.create_scroll_area.setWidgetResizable(True)
        self.create_scroll_area.setObjectName("create_scroll_area")
        self.create_scrollarea_widget_contents = QtGui.QWidget()
        self.create_scrollarea_widget_contents.setGeometry(QtCore.QRect(0, 0, 575, 336))
        self.create_scrollarea_widget_contents.setObjectName("create_scrollarea_widget_contents")
        self.gridLayout = QtGui.QGridLayout(self.create_scrollarea_widget_contents)
        self.gridLayout.setObjectName("gridLayout")
        # create a button according to the list
        total_controller = self.controller_class.len_controller()
        number = 0
        slide = 0
        value = 0
        button_value = 0
        a = 0
        while a < len(total_controller):
            self.pushButton_2 = QtGui.QPushButton(self.create_scrollarea_widget_contents)
            self.pushButton_2.setMinimumSize(QtCore.QSize(0, 100))
            self.pushButton_2.setObjectName(total_controller[a])
            icon_name = controller_icon_path + '/' + total_controller[a] + '.jpg'
            self.pushButton_2.setIcon(QtGui.QIcon(icon_name))
            self.pushButton_2.setIconSize(QtCore.QSize(180, 80))
            self.pushButton_2.setToolTip(total_controller[a])
            self.pushButton_2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
            #self.pushButton_2.clicked.connect(partial(self.controller, a))
            self.pushButton_2.setStyleSheet(
                "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
            #self.pushButton_2.customContextMenuRequested.connect(partial(self.buttonAMenu, button_value))

            self.gridLayout.addWidget(self.pushButton_2, slide, value, 1, 1)
            # print(number)
            value += 1
            number += 1
            button_value += 1
            if number == 3:
                slide += 1
                number = 0
            if value == 3:
                value = 0

            a += 1

        self.create_scroll_area.setWidget(self.create_scrollarea_widget_contents)
        self.horizontalLayout_4.addWidget(self.create_scroll_area)






