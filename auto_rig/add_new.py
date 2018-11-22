#GENERAL INFO
_version = 'V001'
_author =  'Nikheel patel'
_email  =  'spark.visualartist@gmail.com'
_last_modify = '10/28/2018'



# import modulers
import os
import maya.cmds as cmds
import maya.OpenMayaUI as omu
from functools import partial
import maya.api.OpenMaya as om
import maya.OpenMayaMPx as OpenMayaMPx
import maya.OpenMayaAnim as oma
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

# basic import  or add command
from PySide import QtCore
from PySide import QtGui
#import sip
import maya.mel as mel

import head_add_new,spine_add_new,arm_add_new,leg_add_new,tail_add_new,wing_add_new,face_add_new
reload(head_add_new)
reload(spine_add_new)
reload(arm_add_new)
reload(leg_add_new)
reload(tail_add_new)
reload(wing_add_new)
reload(face_add_new)



class ADD_NEW(MayaQWidgetDockableMixin, QtGui.QMainWindow):
    def __init__(self, parent=None):
        self.head_add_new_class = head_add_new.ADD_NEW()
        self.spine_add_new_class = spine_add_new.ADD_NEW()
        self.arm_add_new_class = arm_add_new.ADD_NEW()
        self.leg_add_new_class = leg_add_new.ADD_NEW()
        self.tail_add_new_class = tail_add_new.ADD_NEW()
        self.wing_add_new_class = wing_add_new.ADD_NEW()
        self.face_add_new_class = face_add_new.ADD_NEW()

        super(ADD_NEW, self).__init__(parent=parent)
        self.icon_size_x = 100
        self.icon_size_y = 80
        self.button_color_x = 64
        self.button_color_y = 64
        self.button_color_z = 64

        self.window_gui()

    def window_gui(self):
        # main window
        self.setWindowTitle('Add New')
        self.setObjectName("Add New")
        self.resize(645, 465)

        # CENTERAL WIDGET
        self.auto_rig_new_main_central_widget = QtGui.QWidget(self)
        self.auto_rig_new_main_central_widget.setObjectName("auto_rig_new_main_central_widget")
        self.verticalLayout = QtGui.QVBoxLayout(self.auto_rig_new_main_central_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.auto_rig_new_main_scroll_area = QtGui.QScrollArea(self.auto_rig_new_main_central_widget)
        self.auto_rig_new_main_scroll_area.setWidgetResizable(True)
        self.auto_rig_new_main_scroll_area.setObjectName("auto_rig_new_main_scroll_area")
        self.auto_rig_new_main_scrollArea_widget_contents = QtGui.QWidget()
        self.auto_rig_new_main_scrollArea_widget_contents.setGeometry(QtCore.QRect(0, 0, 625, 69))
        self.auto_rig_new_main_scrollArea_widget_contents.setObjectName("auto_rig_new_main_scrollArea_widget_contents")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.auto_rig_new_main_scrollArea_widget_contents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.auto_rig_new_grid_layout = QtGui.QGridLayout()
        self.auto_rig_new_grid_layout.setObjectName("auto_rig_new_grid_layout")

        self.add_new_checkbox_def()

        self.verticalLayout_4.addLayout(self.auto_rig_new_grid_layout)
        self.auto_rig_new_main_scroll_area.setWidget(self.auto_rig_new_main_scrollArea_widget_contents)
        self.verticalLayout.addWidget(self.auto_rig_new_main_scroll_area)

        # LOWER SCROLL PART
        self.common_scroll_area = QtGui.QScrollArea(self.auto_rig_new_main_central_widget)
        self.common_scroll_area.setMinimumSize(QtCore.QSize(0, 350))
        self.common_scroll_area.setWidgetResizable(True)
        self.common_scroll_area.setObjectName("common_scroll_area")
        self.common_scrollArea_widget_contents = QtGui.QWidget()
        self.common_scrollArea_widget_contents.setGeometry(QtCore.QRect(0, 0, 625, 348))
        self.common_scrollArea_widget_contents.setObjectName("common_scrollArea_widget_contents")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.common_scrollArea_widget_contents)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.common_scroll_area.setWidget(self.common_scrollArea_widget_contents)
        self.verticalLayout.addWidget(self.common_scroll_area)

        self.setCentralWidget(self.auto_rig_new_main_central_widget)

        return self

    def add_new_checkbox_def(self):

        # HEAD
        a = 0
        self.head_check_box = QtGui.QCheckBox(self.auto_rig_new_main_scrollArea_widget_contents)
        self.head_check_box.setObjectName("head_check_box")
        self.head_check_box.setText('Head')
        self.head_check_box.stateChanged.connect(partial(self.check_box_value_def, a))
        self.auto_rig_new_grid_layout.addWidget(self.head_check_box, 1, 0, 1, 1)

        # SPINE
        self.spine_check_box = QtGui.QCheckBox(self.auto_rig_new_main_scrollArea_widget_contents)
        self.spine_check_box.setObjectName("spine_check_box")
        self.spine_check_box.setText('Spine')
        self.spine_check_box.stateChanged.connect(partial(self.check_box_value_def, a + 2))
        self.auto_rig_new_grid_layout.addWidget(self.spine_check_box, 1, 1, 1, 1)

        # ARM
        self.arm_check_box = QtGui.QCheckBox(self.auto_rig_new_main_scrollArea_widget_contents)
        self.arm_check_box.setObjectName("arm_check_box")
        self.arm_check_box.setText('Arm')
        self.arm_check_box.stateChanged.connect(partial(self.check_box_value_def, a + 3))
        self.auto_rig_new_grid_layout.addWidget(self.arm_check_box, 1, 2, 1, 1)

        # LEG
        self.leg_check_box = QtGui.QCheckBox(self.auto_rig_new_main_scrollArea_widget_contents)
        self.leg_check_box.setObjectName("leg_check_box")
        self.leg_check_box.setText('Leg')
        self.leg_check_box.stateChanged.connect(partial(self.check_box_value_def, a + 4))
        self.auto_rig_new_grid_layout.addWidget(self.leg_check_box, 1, 3, 1, 1)

        # TAIL
        self.tail_check_box = QtGui.QCheckBox(self.auto_rig_new_main_scrollArea_widget_contents)
        self.tail_check_box.setObjectName("tail_check_box")
        self.tail_check_box.setText('Tail')
        self.tail_check_box.stateChanged.connect(partial(self.check_box_value_def, a + 5))
        self.auto_rig_new_grid_layout.addWidget(self.tail_check_box, 1, 4, 1, 1)

        # WING
        self.wing_check_box = QtGui.QCheckBox(self.auto_rig_new_main_scrollArea_widget_contents)
        self.wing_check_box.setObjectName("wing_check_box")
        self.wing_check_box.setText('Wing')
        self.wing_check_box.stateChanged.connect(partial(self.check_box_value_def, a + 6))
        self.auto_rig_new_grid_layout.addWidget(self.wing_check_box, 1, 5, 1, 1)

        # FACE
        self.face_check_box = QtGui.QCheckBox(self.auto_rig_new_main_scrollArea_widget_contents)
        self.face_check_box.setObjectName("face_check_box")
        self.face_check_box.setText('Face')
        self.face_check_box.stateChanged.connect(partial(self.check_box_value_def, a + 7))
        self.auto_rig_new_grid_layout.addWidget(self.face_check_box, 1, 6, 1, 1)

    def check_box_value_def(self, value, new):
        pass

        if value == 0:
            checkd = self.head_check_box.isChecked()
            # get the checkbox status
            if checkd == True:
                self.head_add_new_class.ui(self.common_scrollArea_widget_contents, self.verticalLayout_5)
            else:
                self.head_add_new_class.clear()

        if value == 2:
            checkd = self.spine_check_box.isChecked()
            # get the checkbox status
            if checkd == True:
                self.spine_add_new_class.ui(self.common_scrollArea_widget_contents, self.verticalLayout_5)
            else:
                self.spine_add_new_class.clear()

        if value == 3:
            checkd = self.arm_check_box.isChecked()
            # get the checkbox status
            if checkd == True:
                self.arm_add_new_class.ui(self.common_scrollArea_widget_contents, self.verticalLayout_5)
            else:
                self.arm_add_new_class.clear()

        if value == 4:
            checkd = self.leg_check_box.isChecked()
            # get the checkbox status
            if checkd == True:
                self.leg_add_new_class.ui(self.common_scrollArea_widget_contents, self.verticalLayout_5)
            else:
                self.leg_add_new_class.clear()

        if value == 5:
            checkd = self.tail_check_box.isChecked()
            # get the checkbox status
            if checkd == True:
                self.tail_add_new_class.ui(self.common_scrollArea_widget_contents, self.verticalLayout_5)
            else:
                self.tail_add_new_class.clear()

        if value == 6:
            checkd = self.wing_check_box.isChecked()
            # get the checkbox status
            if checkd == True:
                self.wing_add_new_class.ui(self.common_scrollArea_widget_contents, self.verticalLayout_5)
            else:
                self.wing_add_new_class.clear()

        if value == 7:
            checkd = self.face_check_box.isChecked()
            # get the checkbox status
            if checkd == True:
                self.face_add_new_class.ui(self.common_scrollArea_widget_contents, self.verticalLayout_5)
            else:
                self.face_add_new_class.clear()


    def face_new_def(self):
        pass

    def dockCloseEventTriggered(self):
        self.deleteLater()

    def run(self):
        self.show(dockable=True, floating=False, area='right')


try:
    w.dockCloseEventTriggered()
except:
    pass


def main():
    w = ADD_NEW()

    w.show()


