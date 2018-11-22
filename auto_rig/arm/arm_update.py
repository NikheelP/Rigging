

# basic import  or add command
from PySide import QtCore
from PySide import QtGui
import rig_helper
reload(rig_helper)

class ARM_UPDATE:
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
        self.head_name_scroll_area = QtGui.QScrollArea(self.head_splitter)
        self.head_name_scroll_area.setWidgetResizable(True)
        self.head_name_scroll_area.setObjectName("head_name_scroll_area")
        self.head_name_scrollArea_widget_contents = QtGui.QWidget()
        self.head_name_scrollArea_widget_contents.setGeometry(QtCore.QRect(0, 0, 642, 64))
        self.head_name_scrollArea_widget_contents.setObjectName("head_name_scrollArea_widget_contents")
        self.gridLayout_15 = QtGui.QGridLayout(self.head_name_scrollArea_widget_contents)
        self.gridLayout_15.setObjectName("gridLayout_15")
        pass

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
        self.mirror_check_box = QtGui.QCheckBox(self.arm_mirror_group_box)
        self.mirror_check_box.setObjectName("arm_mirror_check_box")
        self.mirror_check_box.setText('Mirror')
        #self.mirror_check_box.stateChanged.connect(self.mirror_status_def)
        self.attr_list.append(self.mirror_check_box)
        self.arm_mirror_grid_layout.addWidget(self.mirror_check_box, 0, 0, 1, 1)

        # LEFT
        self.left_hand_check_box = QtGui.QCheckBox(self.arm_mirror_group_box)
        self.left_hand_check_box.setObjectName("arm_left_check_box")
        self.left_hand_check_box.setText('Left')
        self.attr_list.append(self.left_hand_check_box)
        self.arm_mirror_grid_layout.addWidget(self.left_hand_check_box, 1, 0, 1, 1)

        # RIGHT
        self.right_hand_check_box = QtGui.QCheckBox(self.arm_mirror_group_box)
        self.right_hand_check_box.setObjectName("arm_right_check_box")
        self.right_hand_check_box.setText('Right')
        self.attr_list.append(self.right_hand_check_box)
        self.arm_mirror_grid_layout.addWidget(self.right_hand_check_box, 1, 1, 1, 1)

        # CLAVICAL
        self.clavical_check_box = QtGui.QCheckBox(self.arm_mirror_group_box)
        self.clavical_check_box.setObjectName("arm_clavical_check_box")
        self.clavical_check_box.setText('Clavical')
        self.attr_list.append(self.clavical_check_box)
        self.arm_mirror_grid_layout.addWidget(self.clavical_check_box, 2, 0, 1, 1)

        # SCAPULA
        self.scapula_check_box = QtGui.QCheckBox(self.arm_mirror_group_box)
        self.scapula_check_box.setObjectName("arm_scapula_check_box")
        self.scapula_check_box.setText('Scapula')
        self.attr_list.append(self.scapula_check_box)
        self.arm_mirror_grid_layout.addWidget(self.scapula_check_box, 2, 1, 1, 1)

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
        self.upper_arm_roll_bone_label = QtGui.QLabel(self.arm_bone_group_box)
        self.upper_arm_roll_bone_label.setObjectName("arm_upper_arm_bone_label")
        self.upper_arm_roll_bone_label.setText('Upper Arm Bone')
        self.attr_list.append(self.upper_arm_roll_bone_label)
        self.arm_bone_grid_layout.addWidget(self.upper_arm_roll_bone_label, 0, 0, 1, 1)
        # UPPER ARM BONE LINE EDIT
        self.upper_arm_roll_bone_line_edit = QtGui.QLineEdit(self.arm_bone_group_box)
        self.validator = QtGui.QDoubleValidator()
        self.upper_arm_roll_bone_line_edit.setObjectName("arm_upper_arm_bone_line_edit")
        self.upper_arm_roll_bone_line_edit.setValidator(self.validator)
        self.attr_list.append(self.upper_arm_roll_bone_line_edit)
        self.arm_bone_grid_layout.addWidget(self.upper_arm_roll_bone_line_edit, 0, 1, 1, 1)

        # LOWER ARM BONE
        # LOWER ARM BONE LABEL
        self.lower_arm_roll_bone = QtGui.QLabel(self.arm_bone_group_box)
        self.lower_arm_roll_bone.setObjectName("arm_lower_arm_bone_label")
        self.lower_arm_roll_bone.setText('Lower Arm Bone')
        self.attr_list.append(self.lower_arm_roll_bone)
        self.arm_bone_grid_layout.addWidget(self.lower_arm_roll_bone, 1, 0, 1, 1)
        # LOWER ARM BONE LINE EDIT
        self.lower_arm_roll_bone_line_edit = QtGui.QLineEdit(self.arm_bone_group_box)
        self.lower_arm_roll_bone_line_edit.setObjectName("arm_lower_arm_bone_line_edit")
        self.lower_arm_roll_bone_line_edit.setValidator(self.validator)
        self.attr_list.append(self.lower_arm_roll_bone_line_edit)
        self.arm_bone_grid_layout.addWidget(self.lower_arm_roll_bone_line_edit, 1, 1, 1, 1)

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
        self.hand_check_box = QtGui.QCheckBox(self.arm_hand_double_wrist_group_box)
        self.hand_check_box.setObjectName("arm_hand_check_box")
        self.hand_check_box.setText('Hand')
        #self.hand_check_box.stateChanged.connect(self.update_hand_check_box_def)
        self.attr_list.append(self.hand_check_box)
        self.arm_hand_double_wrist_grid_layout.addWidget(self.hand_check_box, 0, 0, 1, 1)

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
        self.arm_name_label = QtGui.QLabel(self.arm_name_parent_group_box)
        self.arm_name_label.setObjectName("arm_name_label")
        self.arm_name_label.setText('Name')
        self.attr_list.append(self.arm_name_label)
        self.gridLayout_26.addWidget(self.arm_name_label, 0, 0, 1, 1)
        # ARM NAME BUTTON
        self.arm_name_button = QtGui.QPushButton(self.arm_name_parent_group_box)
        self.arm_name_button.setMinimumSize(QtCore.QSize(297, 0))
        self.arm_name_button.setObjectName("arm_name_button")
        self.attr_list.append(self.arm_name_button)
        #self.arm_name_button.clicked.connect(self.rename)

        self.gridLayout_26.addWidget(self.arm_name_button, 0, 1, 1, 1)

        # ARM PARENT
        # ARM PARENT LABEL
        self.arm_parent_label = QtGui.QLabel(self.arm_name_parent_group_box)
        self.arm_parent_label.setObjectName("arm_parent_label")
        self.arm_parent_label.setText('Parent')
        self.attr_list.append(self.arm_parent_label)
        self.gridLayout_26.addWidget(self.arm_parent_label, 1, 0, 1, 1)
        # ARM PARENT BUTTON
        self.arm_parent_button = QtGui.QPushButton(self.arm_name_parent_group_box)
        self.arm_parent_button.setObjectName("arm_parent_button")
        self.attr_list.append(self.arm_parent_button)
        #self.arm_parent_button.clicked.connect(self.parent)

        self.gridLayout_26.addWidget(self.arm_parent_button, 1, 1, 1, 1)

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
        self.arm_update_button = QtGui.QPushButton(self.head_update_scrollArea_widget_contents)
        self.arm_update_button.setObjectName("arm_update_button")
        self.arm_update_button.setText('Update (Arm name)')
        #self.arm_update_button.clicked.connect(self.arm_update_button_def)
        self.attr_list.append(self.arm_update_button)
        self.gridLayout_17.addWidget(self.arm_update_button, 1, 0, 1, 1)

        # DELETE BUTTON
        self.arm_delete_button = QtGui.QPushButton(self.head_update_scrollArea_widget_contents)
        self.arm_delete_button.setObjectName("arm_delete_button")
        self.arm_delete_button.setText('Delete(Arm Name)')
        self.attr_list.append(self.arm_delete_button)
        #self.arm_delete_button.clicked.connect(self.arm_delete_button_def)
        self.gridLayout_17.addWidget(self.arm_delete_button, 1, 1, 1, 1)

        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_17.addItem(spacerItem9, 0, 0, 1, 1)

        self.head_update_scroll_area.setWidget(self.head_update_scrollArea_widget_contents)
        self.gridLayout_18.addWidget(self.head_update_scroll_area, 1, 0, 1, 1)

        self.gridLayout_18.addWidget(self.arm_detail_2_scrollArea, 0, 0, 1, 1)
        self.arm_detail_scroll_area.setWidget(self.arm_detail_scrollArea_widget_contents)
        self.verticalLayout.addWidget(self.head_splitter)

        self.arm_detail_scroll_area.setWidget(self.arm_detail_scrollArea_widget_contents)
        self.verticalLayout.addWidget(self.head_splitter)


