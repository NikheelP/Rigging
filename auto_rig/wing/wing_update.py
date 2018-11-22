

# basic import  or add command
from PySide import QtCore
from PySide import QtGui
import rig_helper
reload(rig_helper)

class WING_UPDATE:

    def __init__(self):
        self.rig_helper_class = rig_helper.rig_help()

    def ui(self,widget):
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
        self.head_name_scroll_area = QtGui.QScrollArea(self.head_splitter)
        self.head_name_scroll_area.setWidgetResizable(True)
        self.head_name_scroll_area.setObjectName("head_name_scroll_area")
        self.head_name_scrollArea_widget_contents = QtGui.QWidget()
        self.head_name_scrollArea_widget_contents.setGeometry(QtCore.QRect(0, 0, 642, 64))
        self.head_name_scrollArea_widget_contents.setObjectName("head_name_scrollArea_widget_contents")
        self.gridLayout_15 = QtGui.QGridLayout(self.head_name_scrollArea_widget_contents)
        self.gridLayout_15.setObjectName("gridLayout_15")

    def get_detail_update_def(self):
        self.arm_detail_scroll_area = QtGui.QScrollArea(self.head_splitter)
        self.arm_detail_scroll_area.setWidgetResizable(True)
        self.arm_detail_scroll_area.setObjectName("arm_detail_scroll_area")
        self.arm_detail_scrollArea_widget_contents = QtGui.QWidget()
        self.arm_detail_scrollArea_widget_contents.setGeometry(QtCore.QRect(0, 0, 489, 350))
        self.arm_detail_scrollArea_widget_contents.setObjectName("arm_detail_scrollArea_widget_contents")

        # UPDATE
        self.arm_detail_2_scrollArea = QtGui.QScrollArea(self.arm_detail_scrollArea_widget_contents)
        self.arm_detail_2_scrollArea.setMinimumSize(QtCore.QSize(0, 207))
        self.arm_detail_2_scrollArea.setWidgetResizable(True)
        self.arm_detail_2_scrollArea.setObjectName("arm_detail_2_scroll_area")
        self.arm_detail_scrollArea_widget_contents_2 = QtGui.QWidget()
        self.arm_detail_scrollArea_widget_contents_2.setGeometry(QtCore.QRect(0, 0, 469, 275))
        self.arm_detail_scrollArea_widget_contents_2.setObjectName("arm_detail_2_scrollArea_widget_contents")

        self.verticalLayout_4 = QtGui.QVBoxLayout(self.arm_detail_scrollArea_widget_contents_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.arm_mirror_group_box = QtGui.QGroupBox(self.arm_detail_scrollArea_widget_contents_2)
        self.arm_mirror_group_box.setTitle("")
        self.arm_mirror_group_box.setObjectName("arm_mirror_group_box")
        self.horizontalLayout_19 = QtGui.QHBoxLayout(self.arm_mirror_group_box)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.arm_mirror_grid_layout = QtGui.QGridLayout()
        self.arm_mirror_grid_layout.setObjectName("arm_mirror_grid_layout")

        # MIRROR
        self.wing_mirror_check_box = QtGui.QCheckBox(self.arm_mirror_group_box)
        self.wing_mirror_check_box.setObjectName("arm_mirror_check_box")
        self.wing_mirror_check_box.setText('Mirror')
        #self.wing_mirror_check_box.stateChanged.connect(self.mirror_status_def)
        self.attr_list.append(self.wing_mirror_check_box)
        self.arm_mirror_grid_layout.addWidget(self.wing_mirror_check_box, 0, 0, 1, 1)

        # LEFT
        self.wing_left_check_box = QtGui.QCheckBox(self.arm_mirror_group_box)
        self.wing_left_check_box.setObjectName("arm_left_check_box")
        self.wing_left_check_box.setText('Left')
        self.attr_list.append(self.wing_left_check_box)
        self.arm_mirror_grid_layout.addWidget(self.wing_left_check_box, 1, 0, 1, 1)

        # RIGHT
        self.wing_right_check_box = QtGui.QCheckBox(self.arm_mirror_group_box)
        self.wing_right_check_box.setObjectName("arm_right_check_box")
        self.wing_right_check_box.setText('Right')
        self.attr_list.append(self.wing_right_check_box)
        self.arm_mirror_grid_layout.addWidget(self.wing_right_check_box, 1, 1, 1, 1)

        # CLAVICAL
        self.wing_type_combo_box = QtGui.QComboBox(self.arm_mirror_group_box)
        self.wing_type_combo_box.setObjectName("wing_type_combo")
        self.wing_type_combo_box.addItem("Dragon")
        self.wing_type_combo_box.addItem("Bird")
        self.attr_list.append(self.wing_type_combo_box)
        #self.wing_type_combo_box.currentIndexChanged.connect(self.update_wing_type_combo_box_def)
        self.arm_mirror_grid_layout.addWidget(self.wing_type_combo_box, 2, 0, 1, 3)

        self.horizontalLayout_19.addLayout(self.arm_mirror_grid_layout)
        self.verticalLayout_4.addWidget(self.arm_mirror_group_box)

        self.arm_bone_group_box = QtGui.QGroupBox(self.arm_detail_scrollArea_widget_contents_2)
        self.arm_bone_group_box.setTitle("")
        self.arm_bone_group_box.setObjectName("arm_bone_group_box")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.arm_bone_group_box)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.arm_bone_grid_layout = QtGui.QGridLayout()
        self.arm_bone_grid_layout.setObjectName("arm_bone_grid_layout")

        # UPPER ARM BONE
        # UPPER ARM BONE LABEL
        self.upper_wing_base_jnt_label = QtGui.QLabel(self.arm_bone_group_box)
        self.upper_wing_base_jnt_label.setObjectName("upper_wing_base_jnt_label")
        self.upper_wing_base_jnt_label.setText('Upper Wing Jnt')
        self.attr_list.append(self.upper_wing_base_jnt_label)
        self.arm_bone_grid_layout.addWidget(self.upper_wing_base_jnt_label, 0, 0, 1, 1)
        # UPPER ARM BONE LINE EDIT
        self.upper_wing_base_jnt_line_edit = QtGui.QLineEdit(self.arm_bone_group_box)
        self.upper_wing_base_jnt_line_edit.setObjectName("arm_upper_arm_bone_line_edit")
        self.attr_list.append(self.upper_wing_base_jnt_line_edit)
        self.arm_bone_grid_layout.addWidget(self.upper_wing_base_jnt_line_edit, 0, 1, 1, 1)

        # LOWER ARM BONE
        # LOWER ARM BONE LABEL
        self.lower_wing_base_jnt_label = QtGui.QLabel(self.arm_bone_group_box)
        self.lower_wing_base_jnt_label.setObjectName("lower_wing_base_jnt_label")
        self.lower_wing_base_jnt_label.setText('Lower Wing Jnt')
        self.attr_list.append(self.lower_wing_base_jnt_label)
        self.arm_bone_grid_layout.addWidget(self.lower_wing_base_jnt_label, 1, 0, 1, 1)
        # LOWER ARM BONE LINE EDIT
        self.lower_wing_base_jnt_line_edit = QtGui.QLineEdit(self.arm_bone_group_box)
        self.lower_wing_base_jnt_line_edit.setObjectName("lower_wing_base_jnt_line_edit")
        self.attr_list.append(self.lower_wing_base_jnt_line_edit)
        self.arm_bone_grid_layout.addWidget(self.lower_wing_base_jnt_line_edit, 1, 1, 1, 1)

        self.verticalLayout_5.addLayout(self.arm_bone_grid_layout)
        self.verticalLayout_4.addWidget(self.arm_bone_group_box)

        self.arm_hand_double_wrist_group_box = QtGui.QGroupBox(self.arm_detail_scrollArea_widget_contents_2)
        self.arm_hand_double_wrist_group_box.setTitle("")
        self.arm_hand_double_wrist_group_box.setObjectName("arm_hand_double_wrist_group_box")
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.arm_hand_double_wrist_group_box)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.arm_hand_double_wrist_grid_layout = QtGui.QGridLayout()
        self.arm_hand_double_wrist_grid_layout.setObjectName("arm_hand_double_wrist_grid_layout")

        # HAND
        self.wing_hand_check_box = QtGui.QCheckBox(self.arm_hand_double_wrist_group_box)
        self.wing_hand_check_box.setObjectName("arm_hand_check_box")
        self.wing_hand_check_box.setText('Hand')
        #self.wing_hand_check_box.stateChanged.connect(self.wing_hand_check_update_def)
        self.arm_hand_double_wrist_grid_layout.addWidget(self.wing_hand_check_box, 0, 0, 1, 1)

        self.verticalLayout_9.addLayout(self.arm_hand_double_wrist_grid_layout)
        self.verticalLayout_4.addWidget(self.arm_hand_double_wrist_group_box)

        self.arm_finger_group_box = QtGui.QGroupBox(self.arm_detail_scrollArea_widget_contents_2)
        self.arm_finger_group_box.setTitle("")
        self.arm_finger_group_box.setObjectName("arm_finger_group_box")
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.arm_finger_group_box)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.arm_finger_grid_layout = QtGui.QGridLayout()
        self.arm_finger_grid_layout.setObjectName("arm_finger_grid_layout")

        # FINGER

        self.verticalLayout_10.addLayout(self.arm_finger_grid_layout)
        self.verticalLayout_4.addWidget(self.arm_finger_group_box)

        self.arm_name_parent_group_box = QtGui.QGroupBox(self.arm_detail_scrollArea_widget_contents_2)
        self.arm_name_parent_group_box.setTitle("")
        self.arm_name_parent_group_box.setObjectName("arm_name_parent_group_box")
        self.gridLayout_26 = QtGui.QGridLayout(self.arm_name_parent_group_box)
        self.gridLayout_26.setObjectName("gridLayout_26")

        # ARM NAME
        # ARM NAME LABEL
        self.wing_name_label = QtGui.QLabel(self.arm_name_parent_group_box)
        self.wing_name_label.setObjectName("wing_name_label")
        self.wing_name_label.setText('Name')
        self.attr_list.append(self.wing_name_label)
        self.gridLayout_26.addWidget(self.wing_name_label, 0, 0, 1, 1)
        # ARM NAME BUTTON
        self.wing_name_button = QtGui.QPushButton(self.arm_name_parent_group_box)
        self.wing_name_button.setMinimumSize(QtCore.QSize(297, 0))
        self.wing_name_button.setObjectName("wing_name_button")
        self.wing_name_button.setText("None")
        #self.wing_name_button.clicked.connect(self.rename)
        self.attr_list.append(self.wing_name_button)
        self.gridLayout_26.addWidget(self.wing_name_button, 0, 1, 1, 1)

        # ARM PARENT
        # ARM PARENT LABEL
        self.wing_parent_label = QtGui.QLabel(self.arm_name_parent_group_box)
        self.wing_parent_label.setObjectName("wing_parent_label")
        self.wing_parent_label.setText('Parent')
        self.attr_list.append(self.wing_parent_label)
        self.gridLayout_26.addWidget(self.wing_parent_label, 1, 0, 1, 1)
        # ARM PARENT BUTTON
        self.wing_parent_button = QtGui.QPushButton(self.arm_name_parent_group_box)
        self.wing_parent_button.setObjectName("wing_parent_button")
        self.wing_parent_button.setText("None")
        #self.wing_parent_button.clicked.connect(self.parent)
        self.attr_list.append(self.wing_parent_button)
        self.gridLayout_26.addWidget(self.wing_parent_button, 1, 1, 1, 1)

        self.verticalLayout_4.addWidget(self.arm_name_parent_group_box)
        self.arm_detail_2_scrollArea.setWidget(self.arm_detail_scrollArea_widget_contents_2)

        # UPDATE AND DELETE BUTTON
        self.gridLayout_18 = QtGui.QGridLayout(self.arm_detail_scrollArea_widget_contents)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.head_update_scroll_area = QtGui.QScrollArea(self.arm_detail_scrollArea_widget_contents)
        self.head_update_scroll_area.setMaximumSize(QtCore.QSize(16777215, 49))
        self.head_update_scroll_area.setWidgetResizable(True)
        self.head_update_scroll_area.setObjectName("head_update_scroll_area")
        self.head_update_scrollArea_widget_contents = QtGui.QWidget()
        self.head_update_scrollArea_widget_contents.setGeometry(QtCore.QRect(0, 0, 469, 47))
        self.head_update_scrollArea_widget_contents.setObjectName("head_update_scrollArea_widget_contents")
        self.gridLayout_17 = QtGui.QGridLayout(self.head_update_scrollArea_widget_contents)
        self.gridLayout_17.setObjectName("gridLayout_17")

        # UPDATE BUTTON
        self.wing_update_button = QtGui.QPushButton(self.head_update_scrollArea_widget_contents)
        self.wing_update_button.setObjectName("wing_update_button")
        self.wing_update_button.setText('Update (Wing name)')
        self.attr_list.append(self.wing_update_button)
        #self.wing_update_button.clicked.connect(self.wing_update_button_def)
        self.gridLayout_17.addWidget(self.wing_update_button, 1, 0, 1, 1)
        #

        # DELETE BUTTON
        self.wing_delete_button = QtGui.QPushButton(self.head_update_scrollArea_widget_contents)
        self.wing_delete_button.setObjectName("wing_delete_button")
        self.wing_delete_button.setText('Delete(Wing Name)')
        self.attr_list.append(self.wing_delete_button)
        self.gridLayout_17.addWidget(self.wing_delete_button, 1, 1, 1, 1)

        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_17.addItem(spacerItem9, 0, 0, 1, 1)

        self.head_update_scroll_area.setWidget(self.head_update_scrollArea_widget_contents)
        self.gridLayout_18.addWidget(self.head_update_scroll_area, 1, 0, 1, 1)

        self.gridLayout_18.addWidget(self.arm_detail_2_scrollArea, 0, 0, 1, 1)
        self.arm_detail_scroll_area.setWidget(self.arm_detail_scrollArea_widget_contents)
        self.verticalLayout.addWidget(self.head_splitter)

        self.arm_detail_scroll_area.setWidget(self.arm_detail_scrollArea_widget_contents)
        self.verticalLayout.addWidget(self.head_splitter)
