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


class SKINNING:
    def __init__(self):
        pass

    def ui(self,widget):
        self.horizontalLayout_12 = QtGui.QHBoxLayout(widget)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")

        self.skinning_tab_widget = QtGui.QTabWidget(widget)
        self.skinning_tab_widget.setObjectName("skinning_tab_widget")

        # SKINNING TOOL
        self.skinning_tool_tab = QtGui.QWidget()
        self.skinning_tool_tab.setObjectName("skinning_tool_tab")
        self.skinning_tool_def()
        self.skinning_tab_widget.addTab(self.skinning_tool_tab, "Skinning Tool")

        self.skin_value_blend_tab = QtGui.QWidget()
        self.skin_value_blend_tab.setObjectName("skin_value_blend_tab")
        #self.skinning_value_blend_def()
        self.skinning_tab_widget.addTab(self.skin_value_blend_tab, "Skinning Value Blend")

        self.component_tab = QtGui.QWidget()
        self.component_tab.setObjectName("component_tab")
        #self.component_def()
        self.skinning_tab_widget.addTab(self.component_tab, "Component")

        self.horizontalLayout_12.addWidget(self.skinning_tab_widget)



    def skinning_tool_def(self):
        self.horizontalLayout_2 = QtGui.QHBoxLayout(widget_name)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rigging_tool_tab_widget = QtGui.QTabWidget(widget_name)
        self.rigging_tool_tab_widget.setObjectName("rigging_tool_tab_widget")
        self.horizontalLayout_2.addWidget(self.rigging_tool_tab_widget)

        # NEW TAB
        self.rigging_tool_tab = QtGui.QWidget()
        self.rigging_tool_tab.setObjectName("rigging_tool_tab")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.rigging_tool_tab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rigging_tool_tab_widget = QtGui.QTabWidget(self.rigging_tool_tab)
        self.rigging_tool_tab_widget.setObjectName("rigging_tool_tab_widget")

        # CREATE
        self.create_tab = QtGui.QWidget()
        self.create_tab.setObjectName("create_tab")
        self.create_def(self.create_tab)
        self.rigging_tool_tab_widget.addTab(self.create_tab, "Create")

        # CONNECTION
        self.connection_tab = QtGui.QWidget()
        self.connection_tab.setObjectName("connection_tab")
        self.connection_def()
        self.rigging_tool_tab_widget.addTab(self.connection_tab, "Connection")

        # TRANSFER
        self.transfer_tab = QtGui.QWidget()
        self.transfer_tab.setObjectName("transfer_tab")
        self.transfer_def()
        self.rigging_tool_tab_widget.addTab(self.transfer_tab, "Transfer")

        # CUSTOM
        self.custom_tab = QtGui.QWidget()
        self.custom_tab.setObjectName("custom_tab")
        self.custom_def()
        self.rigging_tool_tab_widget.addTab(self.custom_tab, "Custom")

        self.horizontalLayout_2.addWidget(self.rigging_tool_tab_widget)