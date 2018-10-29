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
        self.skinning_value_blend_def()
        self.skinning_tab_widget.addTab(self.skin_value_blend_tab, "Skinning Value Blend")

        self.component_tab = QtGui.QWidget()
        self.component_tab.setObjectName("component_tab")
        self.component_def()
        self.skinning_tab_widget.addTab(self.component_tab, "Component")

        self.horizontalLayout_12.addWidget(self.skinning_tab_widget)

    def skinning_tool_def(self):
        self.horizontalLayout_13 = QtGui.QHBoxLayout(self.skinning_tool_tab)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.skinning_tool_scroll_area = QtGui.QScrollArea(self.skinning_tool_tab)
        self.skinning_tool_scroll_area.setWidgetResizable(True)
        self.skinning_tool_scroll_area.setObjectName("skinning_tool_scroll_area")
        self.skinning_tool_scrollArea_widget_contents = QtGui.QWidget()
        self.skinning_tool_scrollArea_widget_contents.setGeometry(QtCore.QRect(0, 0, 655, 392))
        self.skinning_tool_scrollArea_widget_contents.setObjectName("skinning_tool_scrollArea_widget_contents")
        self.gridLayout_7 = QtGui.QGridLayout(self.skinning_tool_scrollArea_widget_contents)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.set_value_horizontal_slider = QtGui.QSlider(self.skinning_tool_scrollArea_widget_contents)
        self.set_value_horizontal_slider.setMinimumSize(QtCore.QSize(384, 0))
        self.set_value_horizontal_slider.setOrientation(QtCore.Qt.Horizontal)
        self.set_value_horizontal_slider.setObjectName("set_value_horizontal_slider")
        self.gridLayout_7.addWidget(self.set_value_horizontal_slider, 13, 2, 1, 1)

        # AVERAGE
        self.average_button = QtGui.QPushButton(self.skinning_tool_scrollArea_widget_contents)
        self.average_button.setObjectName("average_button")
        self.average_button.setText('Average Button')
        self.gridLayout_7.addWidget(self.average_button, 0, 0, 1, 4)

        # COPY
        self.copy_button = QtGui.QPushButton(self.skinning_tool_scrollArea_widget_contents)
        self.copy_button.setObjectName("copy_button")
        self.copy_button.setText('Copy')
        self.gridLayout_7.addWidget(self.copy_button, 1, 0, 1, 4)

        # SELECTED CONNECTED JOINT
        self.selected_connected_joint_button = QtGui.QPushButton(self.skinning_tool_scrollArea_widget_contents)
        self.selected_connected_joint_button.setObjectName("selected_connected_joint_button")
        self.selected_connected_joint_button.setText('Selected Connected Joint Button')
        self.gridLayout_7.addWidget(self.selected_connected_joint_button, 2, 0, 1, 4)

        # SMOOTH GROW
        self.smooth_grow_button = QtGui.QPushButton(self.skinning_tool_scrollArea_widget_contents)
        self.smooth_grow_button.setObjectName("smooth_grow_button")
        self.smooth_grow_button.setText('Smooth Grow')
        self.gridLayout_7.addWidget(self.smooth_grow_button, 3, 0, 1, 4)

        # EDGE OR VERTX LOOP
        self.edge_or_vertex_loop_button = QtGui.QPushButton(self.skinning_tool_scrollArea_widget_contents)
        self.edge_or_vertex_loop_button.setObjectName("edge_or_vertex_loop_button")
        self.edge_or_vertex_loop_button.setText('Edge or Vertex Loop')
        self.gridLayout_7.addWidget(self.edge_or_vertex_loop_button, 4, 0, 1, 4)

        # BONE LABEL
        self.bone_label_button = QtGui.QPushButton(self.skinning_tool_scrollArea_widget_contents)
        self.bone_label_button.setObjectName("bone_label_button")
        self.bone_label_button.setText('Bone Label')
        self.gridLayout_7.addWidget(self.bone_label_button, 5, 0, 1, 4)

        # COPY SKINWEIGHT
        self.copy_skin_weight_button = QtGui.QPushButton(self.skinning_tool_scrollArea_widget_contents)
        self.copy_skin_weight_button.setObjectName("copy_skin_weight_button")
        self.copy_skin_weight_button.setText('Copy Skin Weight')
        self.gridLayout_7.addWidget(self.copy_skin_weight_button, 6, 0, 1, 4)

        # SAVE SKINWEIGHT
        self.save_skin_weight_button = QtGui.QPushButton(self.skinning_tool_scrollArea_widget_contents)
        self.save_skin_weight_button.setObjectName("save_skin_weight_button")
        self.save_skin_weight_button.setText('Save Skin Weight')
        self.gridLayout_7.addWidget(self.save_skin_weight_button, 7, 0, 1, 4)

        # LOAD SKINWEIGHT
        self.load_skin_weight_button = QtGui.QPushButton(self.skinning_tool_scrollArea_widget_contents)
        self.load_skin_weight_button.setObjectName("load_skin_weight_button")
        self.load_skin_weight_button.setText('Load Skin Weight')
        self.gridLayout_7.addWidget(self.load_skin_weight_button, 8, 0, 1, 4)

        # COPY SKIN WEIGHT BASED ON SELECTION
        self.copy_skin_weiight_base_on_selection_button = QtGui.QPushButton(
            self.skinning_tool_scrollArea_widget_contents)
        self.copy_skin_weiight_base_on_selection_button.setObjectName("copy_skin_weiight_base_on_selection_button")
        self.copy_skin_weiight_base_on_selection_button.setText('Copy Skin Weight Base on Selection')
        self.gridLayout_7.addWidget(self.copy_skin_weiight_base_on_selection_button, 9, 0, 1, 4)

        # TRANSFER UV SKINNED GEO
        self.transfer_uv_skinned_geo_button = QtGui.QPushButton(self.skinning_tool_scrollArea_widget_contents)
        self.transfer_uv_skinned_geo_button.setObjectName("transfer_uv_skinned_geo_button")
        self.transfer_uv_skinned_geo_button.setText('Transfer UV Skinned geo')
        self.gridLayout_7.addWidget(self.transfer_uv_skinned_geo_button, 10, 0, 1, 4)

        # JOINT NAME OPTION MENU
        self.set_value_combo_box = QtGui.QComboBox(self.skinning_tool_scrollArea_widget_contents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.set_value_combo_box.sizePolicy().hasHeightForWidth())
        self.set_value_combo_box.setSizePolicy(sizePolicy)
        self.set_value_combo_box.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.set_value_combo_box.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.set_value_combo_box.setAutoFillBackground(False)
        self.set_value_combo_box.setEditable(False)
        self.set_value_combo_box.setInsertPolicy(QtGui.QComboBox.InsertAtTop)
        self.set_value_combo_box.setObjectName("set_value_combo_box")
        # Now Get the Skincluster
        skin_cluster_name = cmds.ls(type='skinCluster')
        for each in skin_cluster_name:
            self.set_value_combo_box.addItem(each)
        self.gridLayout_7.addWidget(self.set_value_combo_box, 11, 0, 1, 4)

        self.set_value_line_edit = QtGui.QLineEdit(self.skinning_tool_scrollArea_widget_contents)
        self.set_value_line_edit.setObjectName("set_value_line_edit")
        self.gridLayout_7.addWidget(self.set_value_line_edit, 13, 1, 1, 1)

        self.refresh_button = QtGui.QPushButton(self.skinning_tool_scrollArea_widget_contents)
        self.refresh_button.setObjectName("refresh_button")
        self.refresh_button.setText('Refresh')
        self.gridLayout_7.addWidget(self.refresh_button, 13, 3, 1, 1)

        spacerItem18 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem18, 12, 2, 1, 1)

        self.skinning_tool_scroll_area.setWidget(self.skinning_tool_scrollArea_widget_contents)
        self.horizontalLayout_13.addWidget(self.skinning_tool_scroll_area)

    def skinning_value_blend_def(self):
        self.horizontalLayout_14 = QtGui.QHBoxLayout(self.skin_value_blend_tab)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.skin_value_splitter = QtGui.QSplitter(self.skin_value_blend_tab)
        self.skin_value_splitter.setOrientation(QtCore.Qt.Vertical)
        self.skin_value_splitter.setObjectName("skin_value_splitter")
        self.influnce_joint_scroll_area = QtGui.QScrollArea(self.skin_value_splitter)
        self.influnce_joint_scroll_area.setWidgetResizable(True)
        self.influnce_joint_scroll_area.setObjectName("influnce_joint_scroll_area")
        self.influnce_joint_scrollArea_widget_contents = QtGui.QWidget()
        self.influnce_joint_scrollArea_widget_contents.setGeometry(QtCore.QRect(0, 0, 556, 46))
        self.influnce_joint_scrollArea_widget_contents.setObjectName("influnce_joint_scrollArea_widget_contents")
        self.gridLayout_8 = QtGui.QGridLayout(self.influnce_joint_scrollArea_widget_contents)
        self.gridLayout_8.setObjectName("gridLayout_8")

        #INFLUENCE JOINT
        self.influnce_joint_1_label = QtGui.QLabel(self.influnce_joint_scrollArea_widget_contents)
        self.influnce_joint_1_label.setObjectName("influnce_joint_1_label")
        self.influnce_joint_1_label.setText('Joint Name')
        self.gridLayout_8.addWidget(self.influnce_joint_1_label, 0, 0, 1, 1)

        #INFLUENCE JOINT LINE EDIT
        self.influnce_joint_1_line_edit = QtGui.QLineEdit(self.influnce_joint_scrollArea_widget_contents)
        self.influnce_joint_1_line_edit.setObjectName("influnce_joint_1_line_edit")
        self.gridLayout_8.addWidget(self.influnce_joint_1_line_edit, 0, 1, 1, 1)

        #INFLUENCE SLIDER
        self.influnce_joint_1_horizontal_slider = QtGui.QSlider(self.influnce_joint_scrollArea_widget_contents)
        self.influnce_joint_1_horizontal_slider.setMinimumSize(QtCore.QSize(419, 0))
        self.influnce_joint_1_horizontal_slider.setOrientation(QtCore.Qt.Horizontal)
        self.influnce_joint_1_horizontal_slider.setObjectName("influnce_joint_1_horizontal_slider")
        self.gridLayout_8.addWidget(self.influnce_joint_1_horizontal_slider, 0, 2, 1, 1)

        spacerItem19 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem19, 1, 1, 1, 1)
        self.influnce_joint_scroll_area.setWidget(self.influnce_joint_scrollArea_widget_contents)

        self.non_influnce_joint_scroll_area = QtGui.QScrollArea(self.skin_value_splitter)
        self.non_influnce_joint_scroll_area.setMinimumSize(QtCore.QSize(0, 252))
        self.non_influnce_joint_scroll_area.setWidgetResizable(True)
        self.non_influnce_joint_scroll_area.setObjectName("non_influnce_joint_scroll_area")
        self.non_influnce_joint_scrollArea_widget_contents = QtGui.QWidget()
        self.non_influnce_joint_scrollArea_widget_contents.setGeometry(QtCore.QRect(0, 0, 556, 233))
        self.non_influnce_joint_scrollArea_widget_contents.setObjectName("non_influnce_joint_scrollArea_widget_contents")
        self.gridLayout_9 = QtGui.QGridLayout(self.non_influnce_joint_scrollArea_widget_contents)
        self.gridLayout_9.setObjectName("gridLayout_9")

        #NON INFLUNCE JOINT NAME
        self.non_influnce_joint_1_label = QtGui.QLabel(self.non_influnce_joint_scrollArea_widget_contents)
        self.non_influnce_joint_1_label.setObjectName("non_influnce_joint_1_label")
        self.non_influnce_joint_1_label.setText('Joint Name')
        self.gridLayout_9.addWidget(self.non_influnce_joint_1_label, 0, 0, 1, 1)

        #NON INFLUNCE JONT LINE EDIT
        self.non_influnce_joint_1_line_edit = QtGui.QLineEdit(self.non_influnce_joint_scrollArea_widget_contents)
        self.non_influnce_joint_1_line_edit.setObjectName("non_influnce_joint_1_line_edit")
        self.gridLayout_9.addWidget(self.non_influnce_joint_1_line_edit, 0, 1, 1, 1)

        #NON INFLUNCE JOINT SLIDER
        self.non_influnce_joint_1_horizontal_slider = QtGui.QSlider(self.non_influnce_joint_scrollArea_widget_contents)
        self.non_influnce_joint_1_horizontal_slider.setMinimumSize(QtCore.QSize(419, 0))
        self.non_influnce_joint_1_horizontal_slider.setOrientation(QtCore.Qt.Horizontal)
        self.non_influnce_joint_1_horizontal_slider.setObjectName("non_influnce_joint_1_horizontal_slider")
        self.gridLayout_9.addWidget(self.non_influnce_joint_1_horizontal_slider, 0, 2, 1, 1)
        spacerItem20 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem20, 1, 1, 1, 1)
        self.non_influnce_joint_scroll_area.setWidget(self.non_influnce_joint_scrollArea_widget_contents)

        self.horizontalLayout_14.addWidget(self.skin_value_splitter)

    def component_def(self):
        self.horizontalLayout_15 = QtGui.QHBoxLayout(self.component_tab)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.component_tab_splitter = QtGui.QSplitter(self.component_tab)
        self.component_tab_splitter.setOrientation(QtCore.Qt.Vertical)
        self.component_tab_splitter.setObjectName("component_tab_splitter")
        self.component_scroll_area = QtGui.QScrollArea(self.component_tab_splitter)
        self.component_scroll_area.setMinimumSize(QtCore.QSize(0, 318))
        self.component_scroll_area.setWidgetResizable(True)
        self.component_scroll_area.setObjectName("component_scroll_area")
        self.component_scrollArea_widget_contents = QtGui.QWidget()
        self.component_scrollArea_widget_contents.setGeometry(QtCore.QRect(0, 0, 672, 325))
        self.component_scrollArea_widget_contents.setObjectName("component_scrollArea_widget_contents")
        self.gridLayout_11 = QtGui.QGridLayout(self.component_scrollArea_widget_contents)
        self.gridLayout_11.setObjectName("gridLayout_11")

        self.checkBox_4 = QtGui.QCheckBox(self.component_scrollArea_widget_contents)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_11.addWidget(self.checkBox_4, 0, 4, 1, 1)
        self.checkBox = QtGui.QCheckBox(self.component_scrollArea_widget_contents)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_11.addWidget(self.checkBox, 0, 1, 1, 1)
        spacerItem21 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem21, 8, 1, 1, 1)
        self.checkBox_3 = QtGui.QCheckBox(self.component_scrollArea_widget_contents)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_11.addWidget(self.checkBox_3, 0, 3, 1, 1)
        self.label_11 = QtGui.QLabel(self.component_scrollArea_widget_contents)
        self.label_11.setObjectName("label_11")
        self.gridLayout_11.addWidget(self.label_11, 0, 0, 1, 1)
        self.checkBox_2 = QtGui.QCheckBox(self.component_scrollArea_widget_contents)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_11.addWidget(self.checkBox_2, 0, 2, 1, 1)
        self.label_13 = QtGui.QLabel(self.component_scrollArea_widget_contents)
        self.label_13.setObjectName("label_13")
        self.gridLayout_11.addWidget(self.label_13, 2, 0, 1, 1)
        self.checkBox_5 = QtGui.QCheckBox(self.component_scrollArea_widget_contents)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout_11.addWidget(self.checkBox_5, 0, 5, 1, 1)
        self.label_12 = QtGui.QLabel(self.component_scrollArea_widget_contents)
        self.label_12.setObjectName("label_12")
        self.gridLayout_11.addWidget(self.label_12, 1, 0, 1, 1)
        self.lineEdit_6 = QtGui.QLineEdit(self.component_scrollArea_widget_contents)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_11.addWidget(self.lineEdit_6, 2, 2, 1, 1)
        self.lineEdit_5 = QtGui.QLineEdit(self.component_scrollArea_widget_contents)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(15, 0))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_11.addWidget(self.lineEdit_5, 2, 1, 1, 1)
        self.lineEdit_7 = QtGui.QLineEdit(self.component_scrollArea_widget_contents)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_11.addWidget(self.lineEdit_7, 2, 3, 1, 1)
        self.lineEdit_8 = QtGui.QLineEdit(self.component_scrollArea_widget_contents)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_11.addWidget(self.lineEdit_8, 2, 4, 1, 1)
        self.lineEdit_11 = QtGui.QLineEdit(self.component_scrollArea_widget_contents)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_11.addWidget(self.lineEdit_11, 3, 2, 1, 1)
        self.lineEdit_10 = QtGui.QLineEdit(self.component_scrollArea_widget_contents)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_11.addWidget(self.lineEdit_10, 3, 1, 1, 1)
        self.lineEdit_9 = QtGui.QLineEdit(self.component_scrollArea_widget_contents)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_11.addWidget(self.lineEdit_9, 2, 5, 1, 1)
        self.lineEdit_13 = QtGui.QLineEdit(self.component_scrollArea_widget_contents)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout_11.addWidget(self.lineEdit_13, 3, 4, 1, 1)
        self.lineEdit_12 = QtGui.QLineEdit(self.component_scrollArea_widget_contents)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout_11.addWidget(self.lineEdit_12, 3, 3, 1, 1)
        self.lineEdit_14 = QtGui.QLineEdit(self.component_scrollArea_widget_contents)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout_11.addWidget(self.lineEdit_14, 3, 5, 1, 1)
        self.label_14 = QtGui.QLabel(self.component_scrollArea_widget_contents)
        self.label_14.setObjectName("label_14")
        self.gridLayout_11.addWidget(self.label_14, 3, 0, 1, 1)
        self.label_15 = QtGui.QLabel(self.component_scrollArea_widget_contents)
        self.label_15.setObjectName("label_15")
        self.gridLayout_11.addWidget(self.label_15, 4, 0, 1, 1)
        self.label_16 = QtGui.QLabel(self.component_scrollArea_widget_contents)
        self.label_16.setObjectName("label_16")
        self.gridLayout_11.addWidget(self.label_16, 5, 0, 1, 1)
        self.label_17 = QtGui.QLabel(self.component_scrollArea_widget_contents)
        self.label_17.setObjectName("label_17")
        self.gridLayout_11.addWidget(self.label_17, 6, 0, 1, 1)
        self.lineEdit_15 = QtGui.QLineEdit(self.component_scrollArea_widget_contents)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.gridLayout_11.addWidget(self.lineEdit_15, 4, 1, 1, 1)
        self.lineEdit_16 = QtGui.QLineEdit(self.component_scrollArea_widget_contents)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.gridLayout_11.addWidget(self.lineEdit_16, 5, 1, 1, 1)
        self.lineEdit_17 = QtGui.QLineEdit(self.component_scrollArea_widget_contents)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.gridLayout_11.addWidget(self.lineEdit_17, 6, 1, 1, 1)
        self.lineEdit_18 = QtGui.QLineEdit(self.component_scrollArea_widget_contents)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.gridLayout_11.addWidget(self.lineEdit_18, 6, 2, 1, 1)
        self.lineEdit_19 = QtGui.QLineEdit(self.component_scrollArea_widget_contents)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.gridLayout_11.addWidget(self.lineEdit_19, 5, 2, 1, 1)
        self.lineEdit_20 = QtGui.QLineEdit(self.component_scrollArea_widget_contents)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.gridLayout_11.addWidget(self.lineEdit_20, 4, 2, 1, 1)
        self.lineEdit_21 = QtGui.QLineEdit(self.component_scrollArea_widget_contents)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.gridLayout_11.addWidget(self.lineEdit_21, 4, 3, 1, 1)
        self.lineEdit_22 = QtGui.QLineEdit(self.component_scrollArea_widget_contents)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.gridLayout_11.addWidget(self.lineEdit_22, 5, 3, 1, 1)
        self.lineEdit_23 = QtGui.QLineEdit(self.component_scrollArea_widget_contents)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.gridLayout_11.addWidget(self.lineEdit_23, 6, 3, 1, 1)
        self.lineEdit_24 = QtGui.QLineEdit(self.component_scrollArea_widget_contents)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.gridLayout_11.addWidget(self.lineEdit_24, 6, 4, 1, 1)
        self.lineEdit_25 = QtGui.QLineEdit(self.component_scrollArea_widget_contents)
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.gridLayout_11.addWidget(self.lineEdit_25, 5, 4, 1, 1)
        self.lineEdit_26 = QtGui.QLineEdit(self.component_scrollArea_widget_contents)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.gridLayout_11.addWidget(self.lineEdit_26, 4, 4, 1, 1)
        self.lineEdit_27 = QtGui.QLineEdit(self.component_scrollArea_widget_contents)
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.gridLayout_11.addWidget(self.lineEdit_27, 4, 5, 1, 1)
        self.lineEdit_28 = QtGui.QLineEdit(self.component_scrollArea_widget_contents)
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.gridLayout_11.addWidget(self.lineEdit_28, 5, 5, 1, 1)
        self.lineEdit_29 = QtGui.QLineEdit(self.component_scrollArea_widget_contents)
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.gridLayout_11.addWidget(self.lineEdit_29, 6, 5, 1, 1)
        self.component_scroll_area.setWidget(self.component_scrollArea_widget_contents)
        self.component_refresh_scroll_area = QtGui.QScrollArea(self.component_tab_splitter)
        self.component_refresh_scroll_area.setMinimumSize(QtCore.QSize(0, 48))
        self.component_refresh_scroll_area.setWidgetResizable(True)
        self.component_refresh_scroll_area.setObjectName("component_refresh_scroll_area")
        self.component_refresh_scrollArea_widget_contents = QtGui.QWidget()
        self.component_refresh_scrollArea_widget_contents.setGeometry(QtCore.QRect(0, 0, 672, 59))
        self.component_refresh_scrollArea_widget_contents.setObjectName("component_refresh_scrollArea_widget_contents")
        self.gridLayout_10 = QtGui.QGridLayout(self.component_refresh_scrollArea_widget_contents)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.component_refresh_button = QtGui.QPushButton(self.component_refresh_scrollArea_widget_contents)
        self.component_refresh_button.setObjectName("component_refresh_button")
        self.gridLayout_10.addWidget(self.component_refresh_button, 0, 0, 1, 1)
        self.component_refresh_lineEdit = QtGui.QLineEdit(self.component_refresh_scrollArea_widget_contents)
        self.component_refresh_lineEdit.setObjectName("component_refresh_lineEdit")
        self.gridLayout_10.addWidget(self.component_refresh_lineEdit, 0, 1, 1, 1)
        self.component_refresh_horizontal_slider = QtGui.QSlider(self.component_refresh_scrollArea_widget_contents)
        self.component_refresh_horizontal_slider.setMinimumSize(QtCore.QSize(402, 0))
        self.component_refresh_horizontal_slider.setOrientation(QtCore.Qt.Horizontal)
        self.component_refresh_horizontal_slider.setObjectName("component_refresh_horizontal_slider")
        self.gridLayout_10.addWidget(self.component_refresh_horizontal_slider, 0, 2, 1, 1)
        self.component_refresh_scroll_area.setWidget(self.component_refresh_scrollArea_widget_contents)
        self.horizontalLayout_15.addWidget(self.component_tab_splitter)
































