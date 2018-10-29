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




class CREATE:
    def __init__(self):
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
        #self.create_tool_def()
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