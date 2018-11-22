

# basic import  or add command
from PySide import QtCore
from PySide import QtGui
import rig_helper,arm_create
reload(rig_helper)
reload(arm_create)

class ADD_NEW:

    def __init__(self):
        self.arm_finger_label     = {}
        self.arm_finger_line_edit = {}
        self.arm_finger_line_edit = {}
        self.finger_label_list    = {}
        self.rig_helper_class = rig_helper.rig_help()
        self.arm_create_class = arm_create.ARM_CREATE()


    def ui(self, widget, layout):
        self.widget = widget
        self.layout = layout

        self.arm_grid_layout = QtGui.QGridLayout()
        self.arm_grid_layout.setObjectName("arm_grid_layout")

        # MIRROR CHECKBOX
        self.mirror_check_box = QtGui.QCheckBox(self.widget)
        self.mirror_check_box.setObjectName("mirror_check_box")
        self.mirror_check_box.setText('Mirror')
        self.mirror_check_box.setChecked(True)
        self.mirror_check_box.stateChanged.connect(self.mirror_def)
        self.arm_grid_layout.addWidget(self.mirror_check_box, 0, 0, 1, 1)

        # LEFT HAND CHECKBOX
        self.left_hand_check_box = QtGui.QCheckBox(self.widget)
        self.left_hand_check_box.setObjectName("left_hand_check_box")
        self.left_hand_check_box.setText('Left Hand')
        self.left_hand_check_box.setChecked(True)
        self.arm_grid_layout.addWidget(self.left_hand_check_box, 1, 0, 1, 1)

        # RIGHT HAND CHECKBOX
        self.right_hand_check_box = QtGui.QCheckBox(self.widget)
        self.right_hand_check_box.setObjectName("right_hand_check_box")
        self.right_hand_check_box.setText('Right Hand')
        self.right_hand_check_box.setChecked(True)
        self.arm_grid_layout.addWidget(self.right_hand_check_box, 1, 1, 1, 1)

        # UPPER ARM ROLL BONE LABEL
        self.upper_arm_roll_bone_label = QtGui.QLabel(self.widget)
        self.upper_arm_roll_bone_label.setObjectName("upper_arm_roll_bone_label")
        self.upper_arm_roll_bone_label.setText('Upper Arm Roll Bone')
        self.arm_grid_layout.addWidget(self.upper_arm_roll_bone_label, 3, 0, 1, 1)
        # UPPER ARM ROLL BONE LINE EDIT
        self.upper_arm_roll_bone_line_edit = QtGui.QLineEdit(self.widget)
        self.upper_arm_roll_bone_line_edit.setObjectName("upper_arm_roll_bone_line_edit")
        self.validator = QtGui.QDoubleValidator()
        self.upper_arm_roll_bone_line_edit.setValidator(self.validator)
        self.upper_arm_roll_bone_line_edit.setText(str(5))
        self.arm_grid_layout.addWidget(self.upper_arm_roll_bone_line_edit, 3, 1, 1, 3)

        # LOWER ARM ROLL BONE LABEL
        self.lower_arm_roll_bone = QtGui.QLabel(self.widget)
        self.lower_arm_roll_bone.setObjectName("lower_arm_roll_bone")
        self.lower_arm_roll_bone.setText('Lower Arm Roll Bone')
        self.arm_grid_layout.addWidget(self.lower_arm_roll_bone, 4, 0, 1, 1)
        # LOWER ARM ROLL BONE LINE EDIT
        self.lower_arm_roll_bone_line_edit = QtGui.QLineEdit(self.widget)
        self.lower_arm_roll_bone_line_edit.setObjectName("lower_arm_roll_bone_line_edit")
        self.lower_arm_roll_bone_line_edit.setValidator(self.validator)
        self.lower_arm_roll_bone_line_edit.setText(str(5))
        self.arm_grid_layout.addWidget(self.lower_arm_roll_bone_line_edit, 4, 1, 1, 3)

        # HAND CHECKBOX
        self.hand_check_box = QtGui.QCheckBox(self.widget)
        self.hand_check_box.setObjectName("hand_check_box")
        self.hand_check_box.setText('Hand')
        self.hand_check_box.stateChanged.connect(self.hand_check_box_def)
        self.arm_grid_layout.addWidget(self.hand_check_box, 5, 0, 1, 1)

        # NO OF FINGER LABEL
        self.no_finer_label = QtGui.QLabel(self.widget)
        self.no_finer_label.setObjectName("no_finer_label")
        self.no_finer_label.setText('No Finger')
        self.no_finer_label.setDisabled(True)
        self.arm_grid_layout.addWidget(self.no_finer_label, 6, 0, 1, 1)
        # NO OF FINGER LINE EDIT
        self.no_finger_line_edit = QtGui.QLineEdit(self.widget)
        self.no_finger_line_edit.setObjectName("no_finger_line_edit")
        self.no_finger_line_edit.setDisabled(True)
        self.no_finger_line_edit.setValidator(self.validator)
        self.no_finger_line_edit.setText('0')
        self.no_finger_line_edit.textChanged.connect(self.no_finger_line_edit_def)
        self.arm_grid_layout.addWidget(self.no_finger_line_edit, 6, 1, 1, 3)

        # ARM BUTTON
        self.arm_create_button = QtGui.QPushButton(self.widget)
        self.arm_create_button.setObjectName("arm_create_button")
        self.arm_create_button.setText('Create Arm')
        self.arm_create_button.clicked.connect(self.new_arm_def)
        self.arm_grid_layout.addWidget(self.arm_create_button, 7, 0, 1, 4)

        self.spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.arm_grid_layout.addItem(self.spacerItem, 9, 0, 1, 1)
        self.layout.addLayout(self.arm_grid_layout)

    def clear(self):
        self.rig_helper_class.clearLayout(self.arm_grid_layout)

    def mirror_def(self):
        self.rig_helper_class.mirror_def(self.mirror_check_box,self.left_hand_check_box,self.right_hand_check_box)

    def no_finger_line_edit_def(self):
        # get the value
        grid_value = 6
        self.arm_create_button.deleteLater()
        # delete the latest one
        a = 0
        while a < len(self.arm_finger_label):
            self.arm_finger_label[a].deleteLater()
            self.arm_finger_line_edit[a].deleteLater()
            a += 1
        self.arm_finger_label = {}
        self.arm_finger_line_edit = {}
        if self.no_finger_line_edit.text() != '':
            self.no_finger_line_edit_query = int(self.no_finger_line_edit.text())
            a = 0
            value = 0
            while a < self.no_finger_line_edit_query:
                # FINGER_2 LABEL
                grid_value = 6 + a + 1

                self.arm_finger_label[value] = QtGui.QLabel(self.widget)
                self.arm_finger_label[value].setObjectName("finger_2_label")
                self.arm_finger_label[value].setText('Finger ' + str(a + 1))
                self.arm_grid_layout.addWidget(self.arm_finger_label[value], grid_value, 0, 1, 3)
                # FINGER_2 LINE EDIT
                self.arm_finger_line_edit[value] = QtGui.QLineEdit(self.widget)
                self.arm_finger_line_edit[value].setObjectName("finger_2_line_edit")
                self.arm_finger_line_edit[value].setValidator(self.validator)
                self.arm_finger_line_edit[value].setText(str(5))
                self.arm_grid_layout.addWidget(self.arm_finger_line_edit[value], grid_value, 1, 1, 3)
                value += 1
                a += 1
            grid_value += 1
            self.arm_create_button = QtGui.QPushButton(self.widget)
            self.arm_create_button.setObjectName("arm_create_button")
            self.arm_create_button.setText('Create Arm')
            self.arm_create_button.clicked.connect(self.new_arm_def)
            self.arm_grid_layout.addWidget(self.arm_create_button, grid_value, 0, 1, 4)
            grid_value += 1
            self.arm_grid_layout.addItem(self.spacerItem, grid_value, 0, 1, 1)

        else:
            grid_value += 1
            self.arm_create_button = QtGui.QPushButton(self.widget)
            self.arm_create_button.setObjectName("arm_create_button")
            self.arm_create_button.setText('Create Arm')
            self.arm_create_button.clicked.connect(self.new_arm_def)
            self.arm_grid_layout.addWidget(self.arm_create_button, grid_value, 0, 1, 4)
            grid_value += 1
            self.arm_grid_layout.addItem(self.spacerItem, grid_value, 0, 1, 1)

    def hand_check_box_def(self):
        # get the statu
        if self.hand_check_box.isChecked():
            self.no_finer_label.setDisabled(False)
            self.no_finger_line_edit.setDisabled(False)
            self.no_finger_line_edit.setText(str(4))
            a = 0
            while a < len(self.arm_finger_label):
                self.arm_finger_label[a].setDisabled(False)
                self.arm_finger_line_edit[a].setDisabled(False)
                a += 1
        else:
            self.no_finer_label.setDisabled(True)
            self.no_finger_line_edit.setDisabled(True)
            a = 0
            while a < len(self.arm_finger_label):
                self.arm_finger_label[a].setDisabled(True)
                self.arm_finger_line_edit[a].setDisabled(True)
                a += 1


    def new_arm_def(self):
        mirror = self.mirror_check_box.isChecked()
        left = self.left_hand_check_box.isChecked()
        right = self.right_hand_check_box.isChecked()
        upper_arm_bone = self.upper_arm_roll_bone_line_edit.text()
        lower_arm_bone = self.lower_arm_roll_bone_line_edit.text()
        hand = self.hand_check_box.isChecked()
        no_finger = self.no_finger_line_edit.text()
        a = 0
        finger_list = []
        while a < int(no_finger):
            finger_val = self.arm_finger_line_edit[a].text()
            finger_list.append(finger_val)
            a+=1


        prefix_name = 'Template'

        if left == True:
            base_pos = [0, 0, 0]
            shoulder_pos = [11, 6, 0]
            upper_hand_pos = [16, 3, 0]
            lbow_pos = [35, 1, -3]
            hand_pos = [54, 1, 0]
            hand_end_pos = [73, 0, 0]
            double_wrist_pos = [57, 1, 0]
            double_lbow_side_1_pos = [32, 1, -3]
            double_lbow_side_2_pos = [38, 1, -3]
            finger_default_pos = [54.0, 0, 0]
            base_ctrl_color = 'Blue'
            self.arm_create_class.arm_def(mirror=mirror,
                                          left_hand=left,
                                          right_hand=right,
                                          upper_arm_roll=upper_arm_bone,
                                          lower_arm_roll=lower_arm_bone,
                                          hand=hand,
                                          no_finger=no_finger,
                                          base_pos=base_pos,
                                          shoulder_pos=shoulder_pos,
                                          upper_hand_pos=upper_hand_pos,
                                          lbow_pos=lbow_pos,
                                          hand_pos=hand_pos,
                                          hand_end_pos=hand_end_pos,
                                          double_wrist_pos=double_wrist_pos,
                                          double_lbow_side_1_pos=double_lbow_side_1_pos,
                                          double_lbow_side_2_pos=double_lbow_side_2_pos,
                                          finger_default_pos=finger_default_pos,
                                          prefix_name=prefix_name,
                                          side='L',
                                          base_ctrl_color=base_ctrl_color,
                                          finger_list = finger_list)

        if right == True:
            base_pos = [0, 0, 0]
            shoulder_pos = [-11, 6, 0]
            upper_hand_pos = [-16, 3, 0]
            lbow_pos = [-35, 1, -3]
            hand_pos = [-54, 1, 0]
            hand_end_pos = [-73, 0, 0]
            double_wrist_pos = [-57, 1, 0]
            double_lbow_side_1_pos = [-32, 1, -3]
            double_lbow_side_2_pos = [-38, 1, -3]
            finger_default_pos = [-54.0, 0, 0]
            base_ctrl_color = 'Red'
            ctrl_list = self.arm_create_class.arm_def(mirror=mirror,
                                                      left_hand=left,
                                                      right_hand=right,
                                                      upper_arm_roll=upper_arm_bone,
                                                      lower_arm_roll=lower_arm_bone,
                                                      hand=hand,
                                                      no_finger=no_finger,
                                                      base_pos=base_pos,
                                                      shoulder_pos=shoulder_pos,
                                                      upper_hand_pos=upper_hand_pos,
                                                      lbow_pos=lbow_pos,
                                                      hand_pos=hand_pos,
                                                      hand_end_pos=hand_end_pos,
                                                      double_wrist_pos=double_wrist_pos,
                                                      double_lbow_side_1_pos=double_lbow_side_1_pos,
                                                      double_lbow_side_2_pos=double_lbow_side_2_pos,
                                                      finger_default_pos=finger_default_pos,
                                                      prefix_name=prefix_name,
                                                      side='R',base_ctrl_color=base_ctrl_color,
                                                      finger_list=finger_list)
        if mirror == True:
            self.rig_helper_class.mirror_value(ctrl_list=ctrl_list,
                                               side='R')
            new_list = []
            for each in ctrl_list:
                new_name = each.replace('R','L')
                new_list.append(new_name)

            self.rig_helper_class.mirror_value(ctrl_list=new_list,
                                               side='L')