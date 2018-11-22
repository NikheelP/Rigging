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



class CUSTOM:
    def __init__(self):
        self.icon_size_x = 100
        self.icon_size_y = 80
        self.button_color_x = 64
        self.button_color_y = 64
        self.button_color_z = 64
        pass

    def widget_def(self,widget_name):
        self.horizontalLayout_9 = QtGui.QHBoxLayout(widget_name)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.custom_scroll_area = QtGui.QScrollArea(widget_name)
        self.custom_scroll_area.setWidgetResizable(True)
        self.custom_scroll_area.setObjectName("custom_scroll_area")
        self.custom_scrollArea_widget_contents = QtGui.QWidget()
        self.custom_scrollArea_widget_contents.setGeometry(QtCore.QRect(0, 0, 548, 355))
        self.custom_scrollArea_widget_contents.setObjectName("custom_scrollArea_widget_contents")
        self.gridLayout_6 = QtGui.QGridLayout(self.custom_scrollArea_widget_contents)
        self.gridLayout_6.setObjectName("gridLayout_6")

        # CORRECTIVE BLENDSHAPE
        value = 0
        self.corrective_blendshape_button = QtGui.QPushButton(self.custom_scrollArea_widget_contents)
        self.corrective_blendshape_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Corrective Blendshape'
        self.corrective_blendshape_button.setObjectName(name)
        self.corrective_blendshape_button.setText(name)
        self.corrective_blendshape_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        button_tool_tip = 'Create a Corrective Blendshape'
        self.corrective_blendshape_button.setToolTip(
            "<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))
        self.corrective_blendshape_button.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        #self.corrective_blendshape_button.customContextMenuRequested.connect(partial(self.custom_menu_def, value))
        #self.corrective_blendshape_button.clicked.connect(corrective_blendshape.CORRECTIVE_BLENDSHAPE)
        self.gridLayout_6.addWidget(self.corrective_blendshape_button, 0, 0, 1, 1)

        # AXIS TWIST
        self.axis_twist_button = QtGui.QPushButton(self.custom_scrollArea_widget_contents)
        self.axis_twist_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Axis Twist'
        self.axis_twist_button.setObjectName(name)
        self.axis_twist_button.setText(name)
        self.axis_twist_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        button_tool_tip = 'Axis Twick'
        self.axis_twist_button.setToolTip("<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))
        self.axis_twist_button.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        #self.axis_twist_button.customContextMenuRequested.connect(partial(self.custom_menu_def, value + 1))
        #self.axis_twist_button.clicked.connect(axis_twist.AXIS_TWIST)
        self.gridLayout_6.addWidget(self.axis_twist_button, 0, 1, 1, 1)

        # RIGGING CHANNEL ID
        self.rigging_channed_id_button = QtGui.QPushButton(self.custom_scrollArea_widget_contents)
        self.rigging_channed_id_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Rigging Channel ID'
        self.rigging_channed_id_button.setObjectName(name)
        self.rigging_channed_id_button.setText(name)
        self.rigging_channed_id_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        button_tool_tip = 'Create Rigging Channel Id'
        self.rigging_channed_id_button.setToolTip(
            "<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))
        self.rigging_channed_id_button.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        #self.rigging_channed_id_button.customContextMenuRequested.connect(partial(self.custom_menu_def, value + 2))
        #self.rigging_channed_id_button.clicked.connect(rigging_channel_id.RIGGING_CHANNEL_ID)
        self.gridLayout_6.addWidget(self.rigging_channed_id_button, 0, 2, 1, 1)

        # BLENDSHAPE EDITOR
        self.blendshape_editor_button = QtGui.QPushButton(self.custom_scrollArea_widget_contents)
        self.blendshape_editor_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Blendshape Editor'
        self.blendshape_editor_button.setObjectName(name)
        self.blendshape_editor_button.setText(name)
        self.blendshape_editor_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        button_tool_tip = 'Blendshape Editor'
        self.blendshape_editor_button.setToolTip(
            "<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))
        self.blendshape_editor_button.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        #self.blendshape_editor_button.customContextMenuRequested.connect(partial(self.custom_menu_def, value + 3))
        #self.blendshape_editor_button.clicked.connect(blendshape_editor.BLENDSHAPE_EDITOR)
        self.gridLayout_6.addWidget(self.blendshape_editor_button, 1, 0, 1, 1)

        # RIGGING OUTLINER
        self.rigging_outliner_button = QtGui.QPushButton(self.custom_scrollArea_widget_contents)
        self.rigging_outliner_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Rigging Outliner'
        self.rigging_outliner_button.setObjectName(name)
        self.rigging_outliner_button.setText(name)
        self.rigging_outliner_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        button_tool_tip = 'Rigging Outliner'
        self.rigging_outliner_button.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        #self.rigging_outliner_button.customContextMenuRequested.connect(partial(self.custom_menu_def, value + 4))
        self.rigging_outliner_button.setToolTip("<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))
        #self.rigging_outliner_button.clicked.connect(rigging_outliner.RIGGING_OUTLINER)
        self.gridLayout_6.addWidget(self.rigging_outliner_button, 1, 1, 1, 1)

        # DROVE POLYGON OBJECT IN CURVE
        self.drove_polygone_object_in_curve_button = QtGui.QPushButton(self.custom_scrollArea_widget_contents)
        self.drove_polygone_object_in_curve_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Drove Polygone Object in Curve'
        self.drove_polygone_object_in_curve_button.setObjectName(name)
        self.drove_polygone_object_in_curve_button.setText(name)
        self.drove_polygone_object_in_curve_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        button_tool_tip = 'Drove Polygon Object to Curve'
        self.drove_polygone_object_in_curve_button.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        #self.drove_polygone_object_in_curve_button.customContextMenuRequested.connect(partial(self.custom_menu_def, value + 5))
        self.drove_polygone_object_in_curve_button.setToolTip(
            "<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))
        #self.drove_polygone_object_in_curve_button.clicked.connect(drove_poly_object_in_curve.DROVE_POLY_OBJECT_IN_CURVE)
        self.gridLayout_6.addWidget(self.drove_polygone_object_in_curve_button, 1, 2, 1, 1)

        # DROVE CUREVE ON SELECTION OBJECT
        self.drove_curve_on_selection_object_button = QtGui.QPushButton(self.custom_scrollArea_widget_contents)
        self.drove_curve_on_selection_object_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Drove Curve on Selection Object'
        self.drove_curve_on_selection_object_button.setObjectName(name)
        self.drove_curve_on_selection_object_button.setText(name)
        self.drove_curve_on_selection_object_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        button_tool_tip = 'Drove Curve on Selection Object'
        self.drove_curve_on_selection_object_button.setToolTip(
            "<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))
        self.drove_curve_on_selection_object_button.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        #self.drove_curve_on_selection_object_button.customContextMenuRequested.connect(partial(self.custom_menu_def, value + 6))
        #self.drove_curve_on_selection_object_button.clicked.connect(drove_curve_on_selected_object.DROVE_CURVE_ON_SELECTED_OBJECT)
        self.gridLayout_6.addWidget(self.drove_curve_on_selection_object_button, 2, 0, 1, 1)

        # POSE SPACE DEFORMER
        self.pose_space_deformer_button = QtGui.QPushButton(self.custom_scrollArea_widget_contents)
        self.pose_space_deformer_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Pose Space Deformer'
        self.pose_space_deformer_button.setObjectName(name)
        self.pose_space_deformer_button.setText(name)
        self.pose_space_deformer_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        button_tool_tip = 'Pose Space Deformer'
        self.pose_space_deformer_button.setToolTip(
            "<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))
        self.pose_space_deformer_button.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        #self.pose_space_deformer_button.customContextMenuRequested.connect(partial(self.custom_menu_def, value + 7))
        #self.pose_space_deformer_button.clicked.connect(pose_space_deformer.POSE_SPACE_DEFORMER)
        self.gridLayout_6.addWidget(self.pose_space_deformer_button, 2, 1, 1, 1)

        # CONTROLLER COLOR
        self.controller_color_button = QtGui.QPushButton(self.custom_scrollArea_widget_contents)
        self.controller_color_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Controller Color'
        self.controller_color_button.setObjectName(name)
        self.controller_color_button.setText(name)
        self.controller_color_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        button_tool_tip = 'Controller Color'
        self.controller_color_button.setToolTip("<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))
        self.controller_color_button.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        #self.controller_color_button.customContextMenuRequested.connect(partial(self.custom_menu_def, value + 8))
        #self.controller_color_button.clicked.connect(controller_color.main)
        self.gridLayout_6.addWidget(self.controller_color_button, 2, 2, 1, 1)

        # SAVE RIG TO JSON FILE
        self.save_rig_to_json_button = QtGui.QPushButton(self.custom_scrollArea_widget_contents)
        self.save_rig_to_json_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Save Rig to Json'
        self.save_rig_to_json_button.setObjectName(name)
        self.save_rig_to_json_button.setText(name)
        self.save_rig_to_json_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        button_tool_tip = 'Controller Color'
        self.save_rig_to_json_button.setToolTip("<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))
        self.save_rig_to_json_button.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        #self.save_rig_to_json_button.customContextMenuRequested.connect(partial(self.custom_menu_def, value + 8))
        #self.save_rig_to_json_button.clicked.connect(self.save_rig_to_json_button_class.save_json_file)
        self.gridLayout_6.addWidget(self.save_rig_to_json_button, 3, 0, 1, 1)

        #Resample Joint
        self.resample_jnt_button = QtGui.QPushButton(self.custom_scrollArea_widget_contents)
        self.resample_jnt_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'ReSample Jnt'
        self.resample_jnt_button.setObjectName(name)
        self.resample_jnt_button.setText(name)
        self.resample_jnt_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        button_tool_tip = 'Controller Color'
        self.resample_jnt_button.setToolTip("<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))
        self.resample_jnt_button.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        # self.save_rig_to_json_button.customContextMenuRequested.connect(partial(self.custom_menu_def, value + 8))
        # self.save_rig_to_json_button.clicked.connect(self.save_rig_to_json_button_class.save_json_file)
        self.gridLayout_6.addWidget(self.resample_jnt_button, 3, 1, 1, 1)

        self.custom_scroll_area.setWidget(self.custom_scrollArea_widget_contents)
        self.horizontalLayout_9.addWidget(self.custom_scroll_area)
