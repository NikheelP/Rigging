

# basic import  or add command
from PySide import QtCore
from PySide import QtGui
import rig_helper
reload(rig_helper)

class LEG_UPDATE:
    def __init__(self):
        self.rig_helper_class = rig_helper.rig_help()

    def ui(self, widget):
        self.update_widget = widget

        self.verticalLayout = QtGui.QVBoxLayout(self.update_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.head_splitter = QtGui.QSplitter(self.update_widget)
        self.head_splitter.setOrientation(QtCore.Qt.Vertical)
        self.head_splitter.setObjectName("head_splitter")

        self.attr_list = []

        # get the radio button
        self.get_update_radio_button()
        self.get_detail_update_def()


        # lock the attr
        self.rig_helper_class.lock_ui_attr(self.attr_list)

    def get_update_radio_button(self):
        self.leg_name_scroll_area = QtGui.QScrollArea(self.head_splitter)
        self.leg_name_scroll_area.setWidgetResizable(True)
        self.leg_name_scroll_area.setObjectName("leg_name_scroll_area")
        self.leg_name_scrollArea_widget_contents = QtGui.QWidget()
        self.leg_name_scrollArea_widget_contents.setGeometry(QtCore.QRect(0, 0, 642, 64))
        self.leg_name_scrollArea_widget_contents.setObjectName("leg_name_scrollArea_widget_contents")
        self.gridLayout_15 = QtGui.QGridLayout(self.leg_name_scrollArea_widget_contents)
        self.gridLayout_15.setObjectName("gridLayout_15")

    def get_detail_update_def(self):
        self.leg_detail_scroll_area = QtGui.QScrollArea(self.head_splitter)
        self.leg_detail_scroll_area.setWidgetResizable(True)
        self.leg_detail_scroll_area.setObjectName("leg_detail_scroll_area")
        self.leg_detail_scrollArea_widget_contents = QtGui.QWidget()
        self.leg_detail_scrollArea_widget_contents.setGeometry(QtCore.QRect(0, 0, 489, 350))
        self.leg_detail_scrollArea_widget_contents.setObjectName("leg_detail_scrollArea_widget_contents")

        # UPDATE
        self.leg_detail_2_scrollArea = QtGui.QScrollArea(self.leg_detail_scrollArea_widget_contents)
        self.leg_detail_2_scrollArea.setMinimumSize(QtCore.QSize(0, 207))
        self.leg_detail_2_scrollArea.setWidgetResizable(True)
        self.leg_detail_2_scrollArea.setObjectName("leg_detail_2_scroll_area")
        self.leg_detail_scrollArea_widget_contents_2 = QtGui.QWidget()
        self.leg_detail_scrollArea_widget_contents_2.setGeometry(QtCore.QRect(0, 0, 469, 275))
        self.leg_detail_scrollArea_widget_contents_2.setObjectName("leg_detail_2_scrollArea_widget_contents")

        self.verticalLayout_4 = QtGui.QVBoxLayout(self.leg_detail_scrollArea_widget_contents_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.leg_mirror_group_box = QtGui.QGroupBox(self.leg_detail_scrollArea_widget_contents_2)
        self.leg_mirror_group_box.setTitle("")
        self.leg_mirror_group_box.setObjectName("leg_mirror_group_box")
        self.horizontalLayout_19 = QtGui.QHBoxLayout(self.leg_mirror_group_box)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.leg_mirror_grid_layout = QtGui.QGridLayout()
        self.leg_mirror_grid_layout.setObjectName("leg_mirror_grid_layout")

        # MIRROR
        self.mirror_check_box = QtGui.QCheckBox(self.leg_mirror_group_box)
        self.mirror_check_box.setObjectName("leg_mirror_check_box")
        self.mirror_check_box.setText('Mirror')
        #self.mirror_check_box.stateChanged.connect(self.mirror_status_def)
        self.attr_list.append(self.mirror_check_box)
        self.leg_mirror_grid_layout.addWidget(self.mirror_check_box, 0, 0, 1, 1)

        # LEFT
        self.left_check_box = QtGui.QCheckBox(self.leg_mirror_group_box)
        self.left_check_box.setObjectName("leg_left_check_box")
        self.left_check_box.setText('Left')
        self.attr_list.append(self.left_check_box)
        self.leg_mirror_grid_layout.addWidget(self.left_check_box, 1, 0, 1, 1)

        # RIGHT
        self.right_check_box = QtGui.QCheckBox(self.leg_mirror_group_box)
        self.right_check_box.setObjectName("leg_right_check_box")
        self.right_check_box.setText('Right')
        self.attr_list.append(self.right_check_box)
        self.leg_mirror_grid_layout.addWidget(self.right_check_box, 1, 1, 1, 1)

        # CLAVICAL
        self.hip_check_box = QtGui.QCheckBox(self.leg_mirror_group_box)
        self.hip_check_box.setObjectName("leg_clavical_check_box")
        self.hip_check_box.setText('Hip')
        self.attr_list.append(self.hip_check_box)
        self.leg_mirror_grid_layout.addWidget(self.hip_check_box, 2, 0, 1, 1)

        # SCAPULA
        self.butt_check_box = QtGui.QCheckBox(self.leg_mirror_group_box)
        self.butt_check_box.setObjectName("leg_scapula_check_box")
        self.butt_check_box.setText('Butt')
        self.attr_list.append(self.butt_check_box)
        self.leg_mirror_grid_layout.addWidget(self.butt_check_box, 2, 1, 1, 1)

        self.horizontalLayout_19.addLayout(self.leg_mirror_grid_layout)
        self.verticalLayout_4.addWidget(self.leg_mirror_group_box)

        self.leg_bone_group_box = QtGui.QGroupBox(self.leg_detail_scrollArea_widget_contents_2)
        self.leg_bone_group_box.setTitle("")
        self.leg_bone_group_box.setObjectName("leg_bone_group_box")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.leg_bone_group_box)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.leg_bone_grid_layout = QtGui.QGridLayout()
        self.leg_bone_grid_layout.setObjectName("leg_bone_grid_layout")

        # UPPER ARM BONE
        # UPPER ARM BONE LABEL
        self.thine_to_knee_jnt_label = QtGui.QLabel(self.leg_bone_group_box)
        self.thine_to_knee_jnt_label.setObjectName("Thine_to_Knee_Jnt")
        self.thine_to_knee_jnt_label.setText('Thine to Knee Jnt')
        self.attr_list.append(self.thine_to_knee_jnt_label)
        self.leg_bone_grid_layout.addWidget(self.thine_to_knee_jnt_label, 0, 0, 1, 1)
        # UPPER ARM BONE LINE EDIT
        self.thine_to_knee_jnt_line_edit = QtGui.QLineEdit(self.leg_bone_group_box)
        self.thine_to_knee_jnt_line_edit.setObjectName("leg_upper_leg_bone_line_edit")
        self.attr_list.append(self.thine_to_knee_jnt_line_edit)
        self.leg_bone_grid_layout.addWidget(self.thine_to_knee_jnt_line_edit, 0, 1, 1, 1)

        # LOWER ARM BONE
        # LOWER ARM BONE LABEL
        self.knee_to_ball_jnt_label = QtGui.QLabel(self.leg_bone_group_box)
        self.knee_to_ball_jnt_label.setObjectName("Knee_to_Ball_Jnt")
        self.knee_to_ball_jnt_label.setText('Knee to Ball Bone')
        self.attr_list.append(self.knee_to_ball_jnt_label)
        self.leg_bone_grid_layout.addWidget(self.knee_to_ball_jnt_label, 1, 0, 1, 1)
        # LOWER ARM BONE LINE EDIT
        self.knee_to_ball_jnt_line_edit = QtGui.QLineEdit(self.leg_bone_group_box)
        self.knee_to_ball_jnt_line_edit.setObjectName("leg_lower_leg_bone_line_edit")
        self.attr_list.append(self.knee_to_ball_jnt_line_edit)
        self.leg_bone_grid_layout.addWidget(self.knee_to_ball_jnt_line_edit, 1, 1, 1, 1)

        self.verticalLayout_5.addLayout(self.leg_bone_grid_layout)
        self.verticalLayout_4.addWidget(self.leg_bone_group_box)

        self.leg_hand_double_wrist_group_box = QtGui.QGroupBox(self.leg_detail_scrollArea_widget_contents_2)
        self.leg_hand_double_wrist_group_box.setTitle("")
        self.leg_hand_double_wrist_group_box.setObjectName("leg_hand_double_wrist_group_box")
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.leg_hand_double_wrist_group_box)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.leg_hand_double_wrist_grid_layout = QtGui.QGridLayout()
        self.leg_hand_double_wrist_grid_layout.setObjectName("leg_hand_double_wrist_grid_layout")

        # HAND

        self.foot_check_box = QtGui.QCheckBox(self.leg_mirror_group_box)
        self.foot_check_box.setObjectName("leg_foot_checkbox")
        self.foot_check_box.setText('Foot')
        #self.foot_check_box.stateChanged.connect(self.update_foot_check_box_def)
        self.attr_list.append(self.foot_check_box)
        self.leg_hand_double_wrist_grid_layout.addWidget(self.foot_check_box, 0, 0, 1, 1)

        self.verticalLayout_9.addLayout(self.leg_hand_double_wrist_grid_layout)
        self.verticalLayout_4.addWidget(self.leg_hand_double_wrist_group_box)

        self.leg_finger_group_box = QtGui.QGroupBox(self.leg_detail_scrollArea_widget_contents_2)
        self.leg_finger_group_box.setTitle("")
        self.leg_finger_group_box.setObjectName("leg_finger_group_box")
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.leg_finger_group_box)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.leg_finger_grid_layout = QtGui.QGridLayout()
        self.leg_finger_grid_layout.setObjectName("leg_finger_grid_layout")

        # FINGER
        self.verticalLayout_10.addLayout(self.leg_finger_grid_layout)
        self.verticalLayout_4.addWidget(self.leg_finger_group_box)

        self.leg_name_parent_group_box = QtGui.QGroupBox(self.leg_detail_scrollArea_widget_contents_2)
        self.leg_name_parent_group_box.setTitle("")
        self.leg_name_parent_group_box.setObjectName("leg_name_parent_group_box")
        self.gridLayout_26 = QtGui.QGridLayout(self.leg_name_parent_group_box)
        self.gridLayout_26.setObjectName("gridLayout_26")

        # ARM NAME
        # ARM NAME LABEL
        self.leg_name_label = QtGui.QLabel(self.leg_name_parent_group_box)
        self.leg_name_label.setObjectName("leg_name_label")
        self.leg_name_label.setText('Name')
        self.attr_list.append(self.leg_name_label)
        self.gridLayout_26.addWidget(self.leg_name_label, 0, 0, 1, 1)
        # ARM NAME BUTTON
        self.leg_name_button = QtGui.QPushButton(self.leg_name_parent_group_box)
        self.leg_name_button.setMinimumSize(QtCore.QSize(297, 0))
        self.leg_name_button.setObjectName("leg_name_button")
        self.leg_name_button.setText('None)')
        #self.leg_name_button.clicked.connect(self.rename)
        self.attr_list.append(self.leg_name_button)
        self.gridLayout_26.addWidget(self.leg_name_button, 0, 1, 1, 1)

        # ARM PARENT
        # ARM PARENT LABEL
        self.leg_parent_label = QtGui.QLabel(self.leg_name_parent_group_box)
        self.leg_parent_label.setObjectName("leg_parent_label")
        self.leg_parent_label.setText('Parent')
        self.attr_list.append(self.leg_parent_label)
        self.gridLayout_26.addWidget(self.leg_parent_label, 1, 0, 1, 1)
        # ARM PARENT BUTTON
        self.leg_parent_button = QtGui.QPushButton(self.leg_name_parent_group_box)
        self.leg_parent_button.setObjectName("leg_parent_button")
        self.leg_parent_button.setText('None)')
        #self.leg_parent_button.clicked.connect(self.parent)
        self.attr_list.append(self.leg_parent_button)
        self.gridLayout_26.addWidget(self.leg_parent_button, 1, 1, 1, 1)

        self.verticalLayout_4.addWidget(self.leg_name_parent_group_box)
        self.leg_detail_2_scrollArea.setWidget(self.leg_detail_scrollArea_widget_contents_2)

        # UPDATE AND DELETE BUTTON
        self.gridLayout_18 = QtGui.QGridLayout(self.leg_detail_scrollArea_widget_contents)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.head_update_scroll_area = QtGui.QScrollArea(self.leg_detail_scrollArea_widget_contents)
        self.head_update_scroll_area.setMaximumSize(QtCore.QSize(16777215, 49))
        self.head_update_scroll_area.setWidgetResizable(True)
        self.head_update_scroll_area.setObjectName("head_update_scroll_area")
        self.head_update_scrollArea_widget_contents = QtGui.QWidget()
        self.head_update_scrollArea_widget_contents.setGeometry(QtCore.QRect(0, 0, 469, 47))
        self.head_update_scrollArea_widget_contents.setObjectName("head_update_scrollArea_widget_contents")
        self.gridLayout_17 = QtGui.QGridLayout(self.head_update_scrollArea_widget_contents)
        self.gridLayout_17.setObjectName("gridLayout_17")

        # UPDATE BUTTON
        self.leg_update_button = QtGui.QPushButton(self.head_update_scrollArea_widget_contents)
        self.leg_update_button.setObjectName("leg_update_button")
        self.leg_update_button.setText('Update (Leg name)')
        #self.leg_update_button.clicked.connect(self.leg_update_button_def)
        self.attr_list.append(self.leg_update_button)
        self.gridLayout_17.addWidget(self.leg_update_button, 1, 0, 1, 1)

        # DELETE BUTTON
        self.leg_delete_button = QtGui.QPushButton(self.head_update_scrollArea_widget_contents)
        self.leg_delete_button.setObjectName("leg_delete_button")
        self.leg_delete_button.setText('Delete(Leg Name)')
        self.attr_list.append(self.leg_delete_button)
        self.gridLayout_17.addWidget(self.leg_delete_button, 1, 1, 1, 1)

        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_17.addItem(spacerItem9, 0, 0, 1, 1)

        self.head_update_scroll_area.setWidget(self.head_update_scrollArea_widget_contents)
        self.gridLayout_18.addWidget(self.head_update_scroll_area, 1, 0, 1, 1)

        self.gridLayout_18.addWidget(self.leg_detail_2_scrollArea, 0, 0, 1, 1)
        self.leg_detail_scroll_area.setWidget(self.leg_detail_scrollArea_widget_contents)
        self.verticalLayout.addWidget(self.head_splitter)

        self.leg_detail_scroll_area.setWidget(self.leg_detail_scrollArea_widget_contents)
        self.verticalLayout.addWidget(self.head_splitter)


