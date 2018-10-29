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
        self.deform_def()
        self.create_tool_box.addItem(self.deform_page, "Deform")

        # OBJECT TOOL BOX
        self.object_page = QtGui.QWidget()
        self.object_page.setGeometry(QtCore.QRect(0, 0, 612, 303))
        self.object_page.setObjectName("object_page")
        self.object_def()
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

    def deform_def(self):
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.deform_page)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.deform_vertical_layout = QtGui.QVBoxLayout()
        self.deform_vertical_layout.setObjectName("deform_vertical_layout")
        self.deform_scroll_area = QtGui.QScrollArea(self.deform_page)
        self.deform_scroll_area.setWidgetResizable(True)
        self.deform_scroll_area.setObjectName("deform_scroll_area")
        self.deform_scrollarea_widget_contents = QtGui.QWidget()
        self.deform_scrollarea_widget_contents.setGeometry(QtCore.QRect(0, 0, 590, 281))
        self.deform_scrollarea_widget_contents.setObjectName("deform_scrollarea_widget_contents")
        self.gridLayout_2 = QtGui.QGridLayout(self.deform_scrollarea_widget_contents)
        self.gridLayout_2.setObjectName("gridLayout_2")

        # CLUSTER
        self.cluster_button = QtGui.QPushButton(self.deform_scrollarea_widget_contents)
        self.cluster_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Cluster'
        self.cluster_button.setObjectName(name)
        self.cluster_button.setText(name)
        button_tool_tip = 'select the object and create a cluster'
        self.cluster_button.setToolTip("<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))
        icon_path = controller_icon_path + '/cluster.png'
        self.cluster_button.setIcon(QtGui.QIcon(icon_path))
        self.cluster_button.setIconSize(QtCore.QSize(self.icon_size_x, self.icon_size_y))
        self.cluster_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        #self.cluster_button.clicked.connect(self.deform_cluster_def)
        self.gridLayout_2.addWidget(self.cluster_button, 0, 0, 1, 1)

        # WRAP
        self.wrap_button = QtGui.QPushButton(self.deform_scrollarea_widget_contents)
        self.wrap_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Wrap'
        self.wrap_button.setObjectName(name)
        self.wrap_button.setText(name)
        button_tool_tip = 'select the Two object with parent and child and create a wrap deformer'
        self.wrap_button.setToolTip("<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))
        icon_path = controller_icon_path + '/wrap.png'
        self.wrap_button.setIcon(QtGui.QIcon(icon_path))
        self.wrap_button.setIconSize(QtCore.QSize(self.icon_size_x, self.icon_size_y))
        self.wrap_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        #self.wrap_button.clicked.connect(self.deform_wrap_def)
        self.gridLayout_2.addWidget(self.wrap_button, 0, 1, 1, 1)

        # BLENDSHAPE
        self.blendshape_button = QtGui.QPushButton(self.deform_scrollarea_widget_contents)
        self.blendshape_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Blendshape'
        self.blendshape_button.setObjectName(name)
        self.blendshape_button.setText(name)
        button_tool_tip = 'select the Two object with child and parent and create a Blendshape node'
        self.blendshape_button.setToolTip("<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))
        icon_path = controller_icon_path + '/blendshape.png'
        self.blendshape_button.setIcon(QtGui.QIcon(icon_path))
        self.blendshape_button.setIconSize(QtCore.QSize(self.icon_size_x, self.icon_size_y))
        self.blendshape_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        #self.blendshape_button.clicked.connect(self.deform_blendshape_def)
        self.gridLayout_2.addWidget(self.blendshape_button, 0, 2, 1, 1)

        # LATTICS
        self.lattics_button = QtGui.QPushButton(self.deform_scrollarea_widget_contents)
        self.lattics_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Lattics'
        self.lattics_button.setObjectName(name)
        self.lattics_button.setText(name)
        button_tool_tip = 'select the Object and create a Lattics deformer'
        self.lattics_button.setToolTip("<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))
        icon_path = controller_icon_path + '/lattics.png'
        self.lattics_button.setIcon(QtGui.QIcon(icon_path))
        self.lattics_button.setIconSize(QtCore.QSize(self.icon_size_x, self.icon_size_y))
        self.lattics_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        #self.lattics_button.clicked.connect(self.deform_lattics_def)
        self.gridLayout_2.addWidget(self.lattics_button, 1, 0, 1, 1)

        # WIRE
        self.wire_button = QtGui.QPushButton(self.deform_scrollarea_widget_contents)
        self.wire_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Wire'
        self.wire_button.setObjectName(name)
        self.wire_button.setText(name)
        button_tool_tip = 'select the curve and select the object and create a wire deformer'
        self.wire_button.setToolTip("<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))
        icon_path = controller_icon_path + '/wire.png'
        self.wire_button.setIcon(QtGui.QIcon(icon_path))
        self.wire_button.setIconSize(QtCore.QSize(self.icon_size_x, self.icon_size_y))
        self.wire_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        #self.wire_button.clicked.connect(self.deform_wire_def)
        self.gridLayout_2.addWidget(self.wire_button, 1, 1, 1, 1)

        # JIGGLE
        self.jiggle_button = QtGui.QPushButton(self.deform_scrollarea_widget_contents)
        self.jiggle_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Jiggle'
        self.jiggle_button.setObjectName(name)
        self.jiggle_button.setText(name)
        button_tool_tip = 'select the Object and create a Jiggle Deformer'
        self.jiggle_button.setToolTip("<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))
        icon_path = controller_icon_path + '/jiggle.png'
        self.jiggle_button.setIcon(QtGui.QIcon(icon_path))
        self.jiggle_button.setIconSize(QtCore.QSize(self.icon_size_x, self.icon_size_y))
        self.jiggle_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        #self.jiggle_button.clicked.connect(self.deform_jiggle_def)
        self.gridLayout_2.addWidget(self.jiggle_button, 1, 2, 1, 1)

        # NON LINER BEND
        self.non_liner_bend_button = QtGui.QPushButton(self.deform_scrollarea_widget_contents)
        self.non_liner_bend_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Non Liner Bend'
        self.non_liner_bend_button.setObjectName(name)
        self.non_liner_bend_button.setText(name)
        button_tool_tip = 'select the Object and create a Non Liner Bend Deformer'
        self.non_liner_bend_button.setToolTip("<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))
        icon_path = controller_icon_path + '/bend.png'
        self.non_liner_bend_button.setIcon(QtGui.QIcon(icon_path))
        self.non_liner_bend_button.setIconSize(QtCore.QSize(self.icon_size_x, self.icon_size_y))
        self.non_liner_bend_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        #self.non_liner_bend_button.clicked.connect(self.deform_bend_def)
        self.gridLayout_2.addWidget(self.non_liner_bend_button, 2, 0, 1, 1)

        # NON LINER FLARE
        self.non_liner_flare_button = QtGui.QPushButton(self.deform_scrollarea_widget_contents)
        self.non_liner_flare_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Non Liner Flare'
        self.non_liner_flare_button.setObjectName(name)
        self.non_liner_flare_button.setText(name)
        button_tool_tip = 'select the Object and create a Non Liner Flare Deformer'
        self.non_liner_flare_button.setToolTip("<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))
        icon_path = controller_icon_path + '/flare.png'
        self.non_liner_flare_button.setIcon(QtGui.QIcon(icon_path))
        self.non_liner_flare_button.setIconSize(QtCore.QSize(self.icon_size_x, self.icon_size_y))
        self.non_liner_flare_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        #self.non_liner_flare_button.clicked.connect(self.deform_flare_def)
        self.gridLayout_2.addWidget(self.non_liner_flare_button, 2, 1, 1, 1)

        # NON LINER SQUASH
        self.non_liner_squash_button = QtGui.QPushButton(self.deform_scrollarea_widget_contents)
        self.non_liner_squash_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Non Liner Squash'
        self.non_liner_squash_button.setObjectName(name)
        self.non_liner_squash_button.setText(name)
        button_tool_tip = 'select the Object and create a Non Liner Squash Deformer'
        self.non_liner_squash_button.setToolTip("<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))
        icon_path = controller_icon_path + '/squash.png'
        self.non_liner_squash_button.setIcon(QtGui.QIcon(icon_path))
        self.non_liner_squash_button.setIconSize(QtCore.QSize(self.icon_size_x, self.icon_size_y))
        self.non_liner_squash_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        #self.non_liner_squash_button.clicked.connect(self.deform_squash_def)
        self.gridLayout_2.addWidget(self.non_liner_squash_button, 2, 2, 1, 1)

        # NON LINER SINE
        self.non_liner_sine_button = QtGui.QPushButton(self.deform_scrollarea_widget_contents)
        self.non_liner_sine_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Non Liner Sine'
        self.non_liner_sine_button.setObjectName(name)
        self.non_liner_sine_button.setText(name)
        button_tool_tip = 'select the Object and create a Non Liner Sine Deformer'
        self.non_liner_sine_button.setToolTip("<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))
        icon_path = controller_icon_path + '/sine.png'
        self.non_liner_sine_button.setIcon(QtGui.QIcon(icon_path))
        self.non_liner_sine_button.setIconSize(QtCore.QSize(self.icon_size_x, self.icon_size_y))
        self.non_liner_sine_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        #self.non_liner_sine_button.clicked.connect(self.deform_sine_def)
        self.gridLayout_2.addWidget(self.non_liner_sine_button, 3, 0, 1, 1)

        # NON LINER TWIST
        self.non_liner_twist_button = QtGui.QPushButton(self.deform_scrollarea_widget_contents)
        self.non_liner_twist_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Non Liner Twist'
        self.non_liner_twist_button.setObjectName(name)
        self.non_liner_twist_button.setText(name)
        button_tool_tip = 'select the Object and create a Non Liner Twist Deformer'
        self.non_liner_twist_button.setToolTip("<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))
        icon_path = controller_icon_path + '/twist.png'
        self.non_liner_twist_button.setIcon(QtGui.QIcon(icon_path))
        self.non_liner_twist_button.setIconSize(QtCore.QSize(self.icon_size_x, self.icon_size_y))
        self.non_liner_twist_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        #self.non_liner_twist_button.clicked.connect(self.deform_twist_def)
        self.gridLayout_2.addWidget(self.non_liner_twist_button, 3, 1, 1, 1)

        # NON LINER WAVE
        self.non_liner_wave_button = QtGui.QPushButton(self.deform_scrollarea_widget_contents)
        self.non_liner_wave_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Non Liner Wave'
        self.non_liner_wave_button.setObjectName(name)
        self.non_liner_wave_button.setText(name)
        button_tool_tip = 'select the Object and create a Non Liner Wave Deformer'
        self.non_liner_wave_button.setToolTip("<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))
        icon_path = controller_icon_path + '/wave.png'
        self.non_liner_wave_button.setIcon(QtGui.QIcon(icon_path))
        self.non_liner_wave_button.setIconSize(QtCore.QSize(self.icon_size_x, self.icon_size_y))
        #self.non_liner_wave_button.setStyleSheet("background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        #self.non_liner_wave_button.clicked.connect(self.deform_wave_def)
        self.gridLayout_2.addWidget(self.non_liner_wave_button, 3, 2, 1, 1)

        # SCULPTER
        self.sculpter_button = QtGui.QPushButton(self.deform_scrollarea_widget_contents)
        self.sculpter_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Sculpter'
        self.sculpter_button.setObjectName(name)
        self.sculpter_button.setText(name)
        button_tool_tip = 'select the Object and create a Sculpter Deformer'
        self.sculpter_button.setToolTip("<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))
        icon_path = controller_icon_path + '/sculpt.png'
        self.sculpter_button.setIcon(QtGui.QIcon(icon_path))
        self.sculpter_button.setIconSize(QtCore.QSize(self.icon_size_x, self.icon_size_y))
        self.sculpter_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        #self.sculpter_button.clicked.connect(self.deform_sculpter_def)
        self.gridLayout_2.addWidget(self.sculpter_button, 4, 0, 1, 1)

        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 5, 0, 1, 1)
        self.deform_scroll_area.setWidget(self.deform_scrollarea_widget_contents)
        self.deform_vertical_layout.addWidget(self.deform_scroll_area)
        self.horizontalLayout_5.addLayout(self.deform_vertical_layout)

    def object_def(self):
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.object_page)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.object_vertical_layout = QtGui.QVBoxLayout()
        self.object_vertical_layout.setObjectName("object_vertical_layout")
        self.object_scroll_area = QtGui.QScrollArea(self.object_page)
        self.object_scroll_area.setWidgetResizable(True)
        self.object_scroll_area.setObjectName("object_scroll_area")
        self.object_scrollArea_widget_contents = QtGui.QWidget()
        self.object_scrollArea_widget_contents.setGeometry(QtCore.QRect(0, 0, 590, 281))
        self.object_scrollArea_widget_contents.setObjectName("object_scrollArea_widget_contents")
        self.gridLayout_3 = QtGui.QGridLayout(self.object_scrollArea_widget_contents)
        self.gridLayout_3.setObjectName("gridLayout_3")

        # JOINT
        self.joint_button = QtGui.QPushButton(self.object_scrollArea_widget_contents)
        self.joint_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Joint'
        self.joint_button.setObjectName(name)
        self.joint_button.setText(name)
        icon_path = controller_icon_path + '/joint.svg'
        self.joint_button.setIcon(QtGui.QIcon(icon_path))
        self.joint_button.setIconSize(QtCore.QSize(self.icon_size_x, self.icon_size_y))
        button_tool_tip = 'Create a Joint Object'
        self.joint_button.setToolTip("<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))
        self.joint_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        #self.joint_button.clicked.connect(self.object_joint_def)
        self.gridLayout_3.addWidget(self.joint_button, 0, 0, 1, 1)

        # IK HANDLE SINGLE CHAIN
        self.ik_handle_single_chain_button = QtGui.QPushButton(self.object_scrollArea_widget_contents)
        self.ik_handle_single_chain_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Ik Handle Single chain'
        self.ik_handle_single_chain_button.setObjectName(name)
        self.ik_handle_single_chain_button.setText(name)
        icon_path = controller_icon_path + '/single_chain.svg'
        self.ik_handle_single_chain_button.setIcon(QtGui.QIcon(icon_path))
        self.ik_handle_single_chain_button.setIconSize(QtCore.QSize(self.icon_size_x, self.icon_size_y))
        self.ik_handle_single_chain_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        button_tool_tip = 'Create a Ik Handle Single chain Object'
        self.ik_handle_single_chain_button.setToolTip(
            "<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))
        #self.ik_handle_single_chain_button.clicked.connect(self.object_ik_single_chain_def)
        self.gridLayout_3.addWidget(self.ik_handle_single_chain_button, 0, 1, 1, 1)

        # IK HANDLE ROTATE CHAIN
        self.ik_handle_rotate_chain_button = QtGui.QPushButton(self.object_scrollArea_widget_contents)
        self.ik_handle_rotate_chain_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Ik Handle Rotate chain'
        self.ik_handle_rotate_chain_button.setObjectName(name)
        self.ik_handle_rotate_chain_button.setText(name)
        icon_path = controller_icon_path + '/rotate_chain.svg'
        self.ik_handle_rotate_chain_button.setIcon(QtGui.QIcon(icon_path))
        self.ik_handle_rotate_chain_button.setIconSize(QtCore.QSize(self.icon_size_x, self.icon_size_y))
        self.ik_handle_rotate_chain_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        button_tool_tip = 'Create a Ik Handle Rotate chain Object'
        self.ik_handle_rotate_chain_button.setToolTip(
            "<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))
        #self.ik_handle_rotate_chain_button.clicked.connect(self.object_ik_rotate_chain_def)
        self.gridLayout_3.addWidget(self.ik_handle_rotate_chain_button, 0, 2, 1, 1)

        # IK SPINE CHAIN
        self.ik_spine_handle_button = QtGui.QPushButton(self.object_scrollArea_widget_contents)
        self.ik_spine_handle_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Ik Spine chain'
        self.ik_spine_handle_button.setObjectName(name)
        self.ik_spine_handle_button.setText(name)
        icon_path = controller_icon_path + '/spine.svg'
        self.ik_spine_handle_button.setIcon(QtGui.QIcon(icon_path))
        self.ik_spine_handle_button.setIconSize(QtCore.QSize(self.icon_size_x, self.icon_size_y))
        self.ik_spine_handle_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        button_tool_tip = 'Create a Ik Spine chain Object'
        self.ik_spine_handle_button.setToolTip("<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))
        #self.ik_spine_handle_button.clicked.connect(self.object_ik_spine_chain_def)
        self.gridLayout_3.addWidget(self.ik_spine_handle_button, 1, 0, 1, 1)

        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 2, 0, 1, 1)
        self.object_scroll_area.setWidget(self.object_scrollArea_widget_contents)
        self.object_vertical_layout.addWidget(self.object_scroll_area)
        self.horizontalLayout_6.addLayout(self.object_vertical_layout)



