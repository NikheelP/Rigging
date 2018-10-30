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

#VARIABLE
_local_icon_path = 'C:/Program Files/Autodesk/Maya2016/icons'
sys.path.append(_local_icon_path)



class CONNECTION:
    def __init__(self):
        self.icon_size_x = 100
        self.icon_size_y = 80
        self.button_color_x = 64
        self.button_color_y = 64
        self.button_color_z = 64
        pass

    def widget_def(self,widget_name):
        self.horizontalLayout_7 = QtGui.QHBoxLayout(widget_name)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.connection_scroll_area = QtGui.QScrollArea(widget_name)
        self.connection_scroll_area.setWidgetResizable(True)
        self.connection_scroll_area.setObjectName("connection_scroll_area")
        self.connection_scrollarea_widget_contents = QtGui.QWidget()
        self.connection_scrollarea_widget_contents.setGeometry(QtCore.QRect(0, 0, 595, 442))
        self.connection_scrollarea_widget_contents.setObjectName("connection_scrollarea_widget_contents")
        self.gridLayout_4 = QtGui.QGridLayout(self.connection_scrollarea_widget_contents)
        self.gridLayout_4.setObjectName("gridLayout_4")

        # TRANSLATE
        self.translate_button = QtGui.QPushButton(self.connection_scrollarea_widget_contents)
        self.translate_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Translate'
        self.translate_button.setObjectName(name)
        self.translate_button.setText(name)
        icon_path = _local_icon_path + '/transform.svg'
        self.translate_button.setIcon(QtGui.QIcon(icon_path))
        self.translate_button.setIconSize(QtCore.QSize(self.icon_size_x, self.icon_size_y))
        self.translate_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        button_tool_tip = 'Create a Transform Connection between 2 Object Object'
        self.translate_button.setToolTip("<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))
        self.translate_button.clicked.connect(self.connection_transform_def)
        self.gridLayout_4.addWidget(self.translate_button, 0, 0, 1, 1)

        # ROTATE
        self.rotate_button = QtGui.QPushButton(self.connection_scrollarea_widget_contents)
        self.rotate_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Rotate'
        self.rotate_button.setObjectName(name)
        self.rotate_button.setText(name)
        icon_path = _local_icon_path + '/rotate.png'
        self.rotate_button.setIcon(QtGui.QIcon(icon_path))
        self.rotate_button.setIconSize(QtCore.QSize(self.icon_size_x, self.icon_size_y))
        self.rotate_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        button_tool_tip = 'Create a Rotate Connection between 2 Object Object'
        self.rotate_button.setToolTip("<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))
        self.rotate_button.clicked.connect(self.connection_rotate_def)
        self.gridLayout_4.addWidget(self.rotate_button, 0, 1, 1, 1)

        # SCALE
        self.scale_button = QtGui.QPushButton(self.connection_scrollarea_widget_contents)
        self.scale_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Scale'
        self.scale_button.setObjectName(name)
        self.scale_button.setText(name)
        icon_path = _local_icon_path + '/scale.png'
        self.scale_button.setIcon(QtGui.QIcon(icon_path))
        self.scale_button.setIconSize(QtCore.QSize(self.icon_size_x, self.icon_size_y))
        self.scale_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        button_tool_tip = 'Create a Scale Connection between 2 Object Object'
        self.scale_button.clicked.connect(self.connection_scale_def)
        self.scale_button.setToolTip("<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))

        self.gridLayout_4.addWidget(self.scale_button, 0, 2, 1, 1)

        # BLENDCOLOR
        self.blendcolor_button = QtGui.QPushButton(self.connection_scrollarea_widget_contents)
        self.blendcolor_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Blend Color'
        self.blendcolor_button.setObjectName(name)
        self.blendcolor_button.setText(name)
        icon_path = _local_icon_path + '/blendcolor.svg'
        self.blendcolor_button.setIcon(QtGui.QIcon(icon_path))
        self.blendcolor_button.setIconSize(QtCore.QSize(self.icon_size_x, self.icon_size_y))
        self.blendcolor_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        button_tool_tip = 'Create a Blend Color between 2 Object Object'
        #self.blendcolor_button.clicked.connect(self.connection_blend_def)
        self.blendcolor_button.setToolTip("<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))

        self.gridLayout_4.addWidget(self.blendcolor_button, 1, 0, 1, 1)

        # MULTIPLYDIVIDE
        self.mult_div_button = QtGui.QPushButton(self.connection_scrollarea_widget_contents)
        self.mult_div_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Mult Div'
        self.mult_div_button.setObjectName(name)
        self.mult_div_button.setText(name)
        icon_path = _local_icon_path + '/mult_div.svg'
        self.mult_div_button.setIcon(QtGui.QIcon(icon_path))
        self.mult_div_button.setIconSize(QtCore.QSize(self.icon_size_x, self.icon_size_y))
        self.mult_div_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        button_tool_tip = 'Create a Mult Div between 3 Object Object'
        #self.mult_div_button.clicked.connect(self.connection_mult_div_def)
        self.mult_div_button.setToolTip("<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))

        self.gridLayout_4.addWidget(self.mult_div_button, 1, 1, 1, 1)

        # REVERSE
        self.reverse_button = QtGui.QPushButton(self.connection_scrollarea_widget_contents)
        self.reverse_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Reverse'
        self.reverse_button.setObjectName(name)
        self.reverse_button.setText(name)
        icon_path = _local_icon_path + '/reverse.svg'
        self.reverse_button.setIcon(QtGui.QIcon(icon_path))
        self.reverse_button.setIconSize(QtCore.QSize(self.icon_size_x, self.icon_size_y))
        self.reverse_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        button_tool_tip = 'Create a reverse between 2 Object Object'
        self.reverse_button.setToolTip("<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))
        #self.reverse_button.clicked.connect(self.connection_reverse_def)
        self.gridLayout_4.addWidget(self.reverse_button, 1, 2, 1, 1)

        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem3, 2, 0, 1, 1)

        self.connection_scroll_area.setWidget(self.connection_scrollarea_widget_contents)
        self.horizontalLayout_7.addWidget(self.connection_scroll_area)

    def connection_transform_def(self):
        sel_obj = cmds.ls(sl=True)
        cmds.connectAttr((sel_obj[0] + '.translate'),(sel_obj[1] + '.translate'),f=True)

    def connection_rotate_def(self):
        sel_obj = cmds.ls(sl=True)
        cmds.connectAttr((sel_obj[0] + '.rotate'),(sel_obj[1] + '.rotate'),f=True)

    def connection_scale_def(self):
        sel_obj = cmds.ls(sl=True)
        cmds.connectAttr((sel_obj[0] + '.scale'),(sel_obj[1] + '.scale'),f=True)













