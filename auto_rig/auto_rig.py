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

import add_new
reload(add_new)


class AUTO_RIG:
    def __init__(self):
        pass

    def ui(self,widget):
        self.horizontalLayout_10 = QtGui.QHBoxLayout(widget)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")

        self.auto_rig_group_box = QtGui.QGroupBox(widget)
        self.auto_rig_group_box.setTitle("")
        self.auto_rig_group_box.setObjectName("auto_rig_group_box")
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.auto_rig_group_box)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.auto_rig_main_splitter = QtGui.QSplitter(self.auto_rig_group_box)
        self.auto_rig_main_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.auto_rig_main_splitter.setObjectName("auto_rig_main_splitter")

        # AUTO ROG LEFT SIDE
        self.auto_rig_secound_splitter = QtGui.QSplitter(self.auto_rig_main_splitter)
        self.auto_rig_secound_splitter.setOrientation(QtCore.Qt.Vertical)
        self.auto_rig_secound_splitter.setObjectName("auto_rig_secound_splitter")
        self.auto_rig_left_ui()

        # AUTO RIG TAB
        self.tabWidget = QtGui.QTabWidget(self.auto_rig_main_splitter)
        self.tabWidget.setMinimumSize(QtCore.QSize(400, 0))
        self.tabWidget.setObjectName("tabWidget")
        self.auto_rig_right_ui()

        self.horizontalLayout_11.addWidget(self.auto_rig_main_splitter)
        self.horizontalLayout_10.addWidget(self.auto_rig_group_box)

    def auto_rig_left_ui(self):
        # DISPLAY
        self.verticalLayoutWidget_4 = QtGui.QWidget(self.auto_rig_secound_splitter)
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.auto_rig_detail_vertical_layout = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.auto_rig_detail_vertical_layout.setObjectName("auto_rig_detail_vertical_layout")
        self.autot_rig_detail_scroll_area = QtGui.QScrollArea(self.verticalLayoutWidget_4)
        self.autot_rig_detail_scroll_area.setWidgetResizable(True)
        self.autot_rig_detail_scroll_area.setObjectName("autot_rig_detail_scroll_area")
        self.auto_rig_detail_scrollArea_widget_contents_ = QtGui.QWidget()
        self.auto_rig_detail_scrollArea_widget_contents_.setGeometry(QtCore.QRect(0, -43, 128, 151))
        self.auto_rig_detail_scrollArea_widget_contents_.setObjectName("auto_rig_detail_scrollArea_widget_contents_")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.auto_rig_detail_scrollArea_widget_contents_)
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        # HEAD LABEL
        self.head_label = QtGui.QLabel(self.auto_rig_detail_scrollArea_widget_contents_)
        self.head_label.setObjectName("head_label")
        #total = self.head_class.get_head()
        #self.head_label.setText('Head : ' + str(total))
        self.verticalLayout_6.addWidget(self.head_label)

        # SPINE LABEL
        self.spine_label = QtGui.QLabel(self.auto_rig_detail_scrollArea_widget_contents_)
        self.spine_label.setObjectName("spine_label")
        #total = self.spine_class.get_spine()
        #self.spine_label.setText('Spine : ' + str(total))
        self.verticalLayout_6.addWidget(self.spine_label)

        # LEG LABEL
        self.leg_label = QtGui.QLabel(self.auto_rig_detail_scrollArea_widget_contents_)
        self.leg_label.setObjectName("leg_label")
        #total = self.leg_class.get_leg()
        #self.leg_label.setText('Leg : ' + str(total))
        self.verticalLayout_6.addWidget(self.leg_label)

        # ARM LABEL
        self.arm_label = QtGui.QLabel(self.auto_rig_detail_scrollArea_widget_contents_)
        self.arm_label.setObjectName("arm_label")
        #total = self.arm_class.get_arm()
        #self.arm_label.setText('Arm : ' + str(total))
        self.verticalLayout_6.addWidget(self.arm_label)

        # TAIL LABEL
        self.tail_label = QtGui.QLabel(self.auto_rig_detail_scrollArea_widget_contents_)
        self.tail_label.setObjectName("tail_label")
        #total = self.tail_class.get_tail()
        #self.tail_label.setText('Tail : ' + str(total))
        self.verticalLayout_6.addWidget(self.tail_label)

        # WING LABEL
        self.wing_label = QtGui.QLabel(self.auto_rig_detail_scrollArea_widget_contents_)
        self.wing_label.setObjectName("wing_label")
        #total = self.wing_class.get_wing()
        #self.wing_label.setText('Wing : ' + str(total))
        self.verticalLayout_6.addWidget(self.wing_label)

        # FACE LABEL
        self.face_label = QtGui.QLabel(self.auto_rig_detail_scrollArea_widget_contents_)
        self.face_label.setObjectName("face_label")
        self.face_label.setText('Face : ')
        self.verticalLayout_6.addWidget(self.face_label)

        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem8)
        self.autot_rig_detail_scroll_area.setWidget(self.auto_rig_detail_scrollArea_widget_contents_)
        self.auto_rig_detail_vertical_layout.addWidget(self.autot_rig_detail_scroll_area)

        # SETUP
        self.verticalLayoutWidget_5 = QtGui.QWidget(self.auto_rig_secound_splitter)
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.auto_rig_setup_vertical_layout = QtGui.QVBoxLayout(self.verticalLayoutWidget_5)
        self.auto_rig_setup_vertical_layout.setObjectName("auto_rig_setup_vertical_layout")
        self.auto_rig_setup_scroll_area = QtGui.QScrollArea(self.verticalLayoutWidget_5)
        self.auto_rig_setup_scroll_area.setWidgetResizable(True)
        self.auto_rig_setup_scroll_area.setObjectName("auto_rig_setup_scroll_area")
        self.auto_rig_setup_scrollArea_widget_contents = QtGui.QWidget()
        self.auto_rig_setup_scrollArea_widget_contents.setGeometry(QtCore.QRect(0, -34, 128, 157))
        self.auto_rig_setup_scrollArea_widget_contents.setObjectName("auto_rig_setup_scrollArea_widget_contents")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.auto_rig_setup_scrollArea_widget_contents)
        self.verticalLayout_7.setObjectName("verticalLayout_7")

        # BONE SETUP
        self.bone_setup_button = QtGui.QPushButton(self.auto_rig_setup_scrollArea_widget_contents)
        self.bone_setup_button.setObjectName("bone_setup_button")
        self.bone_setup_button.setText('Bone Setup')
        #self.bone_setup_button.clicked.connect(self.bone_setup_class.bone_setup_create)
        self.verticalLayout_7.addWidget(self.bone_setup_button)

        # SKIN SETUP
        self.Skin_setup_button = QtGui.QPushButton(self.auto_rig_setup_scrollArea_widget_contents)
        self.Skin_setup_button.setObjectName("Skin_setup_button")
        self.Skin_setup_button.setText('Skin Setup')
        #self.Skin_setup_button.clicked.connect(self.skin_setup_class.skin_setup_create)
        self.verticalLayout_7.addWidget(self.Skin_setup_button)

        # FINALISE RIG
        self.finalise_rig_button = QtGui.QPushButton(self.auto_rig_setup_scrollArea_widget_contents)
        self.finalise_rig_button.setObjectName("finalise_rig_button")
        self.finalise_rig_button.setText('Finalize Rig')
        #self.finalise_rig_button.clicked.connect(self.finalize_rig_class.finalise_rig_create)
        self.verticalLayout_7.addWidget(self.finalise_rig_button)

        # DELETE TEMP RIG
        self.delete_temp_rig_button = QtGui.QPushButton(self.auto_rig_setup_scrollArea_widget_contents)
        self.delete_temp_rig_button.setObjectName("delete_temp_rig_button")
        self.delete_temp_rig_button.setText('Delete Temp Rig')
        #self.delete_temp_rig_button.clicked.connect(self.delete_temp_rig_class.delete_temp_rig)
        self.verticalLayout_7.addWidget(self.delete_temp_rig_button)

        # TWICK CONTROLLER
        self.twick_controller_button = QtGui.QPushButton(self.auto_rig_setup_scrollArea_widget_contents)
        self.twick_controller_button.setObjectName("twick_controller_button")
        self.twick_controller_button.setText('Twick Controller')
        #self.twick_controller_button.clicked.connect(self.twick_controller_class.twick_controller_create)
        self.verticalLayout_7.addWidget(self.twick_controller_button)

        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem8)
        self.auto_rig_setup_scroll_area.setWidget(self.auto_rig_setup_scrollArea_widget_contents)
        self.auto_rig_setup_vertical_layout.addWidget(self.auto_rig_setup_scroll_area)

        # NEW
        self.verticalLayoutWidget_6 = QtGui.QWidget(self.auto_rig_secound_splitter)
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.auto_rig_new_vertical_layout = QtGui.QVBoxLayout(self.verticalLayoutWidget_6)
        self.auto_rig_new_vertical_layout.setObjectName("auto_rig_new_vertical_layout")
        self.auto_rig_new_scroll_area = QtGui.QScrollArea(self.verticalLayoutWidget_6)
        self.auto_rig_new_scroll_area.setWidgetResizable(True)
        self.auto_rig_new_scroll_area.setObjectName("auto_rig_new_scroll_area")
        self.auto_rig_new_scrollArea_widget_contents = QtGui.QWidget()
        self.auto_rig_new_scrollArea_widget_contents.setGeometry(QtCore.QRect(0, -79, 128, 244))
        self.auto_rig_new_scrollArea_widget_contents.setObjectName("auto_rig_new_scrollArea_widget_contents")
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.auto_rig_new_scrollArea_widget_contents)
        self.verticalLayout_8.setObjectName("verticalLayout_8")

        # ADD NEW
        self.add_new_button = QtGui.QPushButton(self.auto_rig_new_scrollArea_widget_contents)
        self.add_new_button.setObjectName("add_new_button")
        self.add_new_button.setText('Add New')
        self.add_new_button.clicked.connect(add_new.main)
        self.verticalLayout_8.addWidget(self.add_new_button)

        # DELETE ALL HEAD
        self.delete_all_head_button = QtGui.QPushButton(self.auto_rig_new_scrollArea_widget_contents)
        self.delete_all_head_button.setObjectName("delete_all_head_button")
        self.delete_all_head_button.setText('Delete all Head')
        #self.delete_all_head_button.clicked.connect(partial(self.help_class.delete_all_part, 'Head_Grp'))
        self.verticalLayout_8.addWidget(self.delete_all_head_button)

        # DELETE ALL SPINE
        self.delete_all_spine_button = QtGui.QPushButton(self.auto_rig_new_scrollArea_widget_contents)
        self.delete_all_spine_button.setObjectName("delete_all_spine_button")
        self.delete_all_spine_button.setText('Delete All Spine')
        #self.delete_all_spine_button.clicked.connect(partial(self.help_class.delete_all_part, 'Spine_Grp'))
        self.verticalLayout_8.addWidget(self.delete_all_spine_button)

        # DELETE ALL ARM
        self.delete_all_arm_button = QtGui.QPushButton(self.auto_rig_new_scrollArea_widget_contents)
        self.delete_all_arm_button.setObjectName("delete_all_arm_button")
        self.delete_all_arm_button.setText('Delete All Arm')
        #self.delete_all_arm_button.clicked.connect(partial(self.help_class.delete_all_part, 'Arm_Grp'))
        self.verticalLayout_8.addWidget(self.delete_all_arm_button)

        # DELETE ALL LEG
        self.delete_all_leg_button = QtGui.QPushButton(self.auto_rig_new_scrollArea_widget_contents)
        self.delete_all_leg_button.setObjectName("delete_all_leg_button")
        self.delete_all_leg_button.setText('Delete All Leg')
        #self.delete_all_leg_button.clicked.connect(partial(self.help_class.delete_all_part, 'Leg_Grp'))
        self.verticalLayout_8.addWidget(self.delete_all_leg_button)

        # DELETE ALL TAIL
        self.delete_all_tail_button = QtGui.QPushButton(self.auto_rig_new_scrollArea_widget_contents)
        self.delete_all_tail_button.setObjectName("delete_all_tail_button")
        self.delete_all_tail_button.setText('Delete All Tail')
        #self.delete_all_tail_button.clicked.connect(partial(self.help_class.delete_all_part, 'Tail_Grp'))
        self.verticalLayout_8.addWidget(self.delete_all_tail_button)

        # DELETE ALL WING
        self.delete_all_wing_button = QtGui.QPushButton(self.auto_rig_new_scrollArea_widget_contents)
        self.delete_all_wing_button.setObjectName("delete_all_wing_button")
        self.delete_all_wing_button.setText('Delete All Wing')
        #self.delete_all_wing_button.clicked.connect(partial(self.help_class.delete_all_part, 'Wing_Grp'))
        self.verticalLayout_8.addWidget(self.delete_all_wing_button)

        # DELETE ALL FACE
        self.delete_all_face_button = QtGui.QPushButton(self.auto_rig_new_scrollArea_widget_contents)
        self.delete_all_face_button.setObjectName("delete_all_face_button")
        self.delete_all_face_button.setText('Delete All Face')
        #self.delete_all_face_button.clicked.connect(self.face_class.delete_all)
        self.verticalLayout_8.addWidget(self.delete_all_face_button)

        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem8)
        self.auto_rig_new_scroll_area.setWidget(self.auto_rig_new_scrollArea_widget_contents)
        self.auto_rig_new_vertical_layout.addWidget(self.auto_rig_new_scroll_area)

    def auto_rig_right_ui(self):
        # HEAD
        self.head_tab = QtGui.QWidget()
        self.head_tab.setObjectName("head_tab")
        #self.head_class.update_gui(self.head_tab)
        self.tabWidget.addTab(self.head_tab, "Head")

        # SPINE
        self.spine_tab = QtGui.QWidget()
        self.spine_tab.setObjectName("spine_tab")
        #self.spine_class.update_gui(self.spine_tab)
        self.tabWidget.addTab(self.spine_tab, 'Spine')

        # ARM
        self.arm_tab = QtGui.QWidget()
        self.arm_tab.setObjectName("arm_tab")
        #self.arm_class.update_gui(self.arm_tab)
        self.tabWidget.addTab(self.arm_tab, 'Arm')

        # LEG
        self.leg_tab = QtGui.QWidget()
        self.leg_tab.setObjectName("leg_tab")
        #self.leg_class.update_gui(self.leg_tab)
        self.tabWidget.addTab(self.leg_tab, 'Leg')

        # TAIL
        self.tail_tab = QtGui.QWidget()
        self.tail_tab.setObjectName("tail_tab")
        #self.tail_class.update_gui(self.tail_tab)
        self.tabWidget.addTab(self.tail_tab, 'Tail')

        # WING
        self.wing_tab = QtGui.QWidget()
        self.wing_tab.setObjectName("wing_tab")
        #self.wing_class.update_gui(self.wing_tab)
        self.tabWidget.addTab(self.wing_tab, 'Wing')

        # FACE
        self.face_tab = QtGui.QWidget()
        self.face_tab.setObjectName("face_tab")
        #self.face_class.update_gui(self.face_tab)
        self.tabWidget.addTab(self.face_tab, 'Face')

        # Controller
        self.controller_tab = QtGui.QWidget()
        self.controller_tab.setObjectName("Controller_tab")
        #self.controller_def()
        self.tabWidget.addTab(self.controller_tab, 'Controller')








