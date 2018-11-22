

# basic import  or add command
from PySide import QtCore
from PySide import QtGui
import rig_helper,leg_create
reload(rig_helper)
reload(leg_create)

class ADD_NEW:

    def __init__(self):
        self.leg_finger_label = {}
        self.rig_helper_class = rig_helper.rig_help()
        self.leg_create_class = leg_create.LEG_CREATE()
        pass

    def ui(self, widget, layout):
        self.widget = widget
        self.layout = layout

        self.leg_grid_layout = QtGui.QGridLayout()
        self.leg_grid_layout.setObjectName("leg_grid_layout")

        # MIRROR CHECKBOX
        self.mirror_check_box = QtGui.QCheckBox(self.widget)
        self.mirror_check_box.setObjectName("mirror_check_box")
        self.mirror_check_box.setText('Mirror')
        self.mirror_check_box.setChecked(True)
        self.mirror_check_box.stateChanged.connect(self.mirror_def)
        self.leg_grid_layout.addWidget(self.mirror_check_box, 0, 0, 1, 1)

        # LEFT LEG CHECKBOX
        self.left_check_box = QtGui.QCheckBox(self.widget)
        self.left_check_box.setObjectName("left_check_box")
        self.left_check_box.setText('Left Leg')
        self.left_check_box.setChecked(True)
        self.leg_grid_layout.addWidget(self.left_check_box, 1, 0, 1, 1)

        # RIGHT LEG CHECKBOX
        self.right_check_box = QtGui.QCheckBox(self.widget)
        self.right_check_box.setObjectName("right_check_box")
        self.right_check_box.setText('Right Leg')
        self.right_check_box.setChecked(True)
        self.leg_grid_layout.addWidget(self.right_check_box, 1, 1, 1, 1)

        #Type of Leg
        self.type_leg_combo_box = QtGui.QComboBox(self.widget)
        self.type_leg_combo_box.setObjectName("type_leg_combo_box")
        self.type_leg_combo_box.addItem("Human")
        self.type_leg_combo_box.addItem("Animal_Front_Leg")
        self.type_leg_combo_box.addItem("Animal_Back_Leg")
        self.leg_grid_layout.addWidget(self.type_leg_combo_box, 2, 0, 1, 4)

        # HIP CHECKBOX
        self.hip_check_box = QtGui.QCheckBox(self.widget)
        self.hip_check_box.setObjectName("hip_check_box")
        self.hip_check_box.setText('Hip')
        self.leg_grid_layout.addWidget(self.hip_check_box, 3, 0, 1, 1)

        # BUTT CHECKBOX
        self.butt_check_box = QtGui.QCheckBox(self.widget)
        self.butt_check_box.setObjectName("butt_check_box")
        self.butt_check_box.setText('Butt')
        self.leg_grid_layout.addWidget(self.butt_check_box, 3, 1, 1, 1)

        # THINE TO KNEE LABEL
        self.thine_to_knee_jnt_label = QtGui.QLabel(self.widget)
        self.thine_to_knee_jnt_label.setObjectName("thine_to_knee_jnt_label")
        self.thine_to_knee_jnt_label.setText('Thine to knee Joint')
        self.leg_grid_layout.addWidget(self.thine_to_knee_jnt_label, 4, 0, 1, 1)
        # THING TO KNEE LINE EDIT
        self.thine_to_knee_jnt_line_edit = QtGui.QLineEdit(self.widget)
        self.thine_to_knee_jnt_line_edit.setObjectName("thine_to_knee_jnt_line_edit")
        self.validator = QtGui.QDoubleValidator()
        self.thine_to_knee_jnt_line_edit.setValidator(self.validator)
        self.thine_to_knee_jnt_line_edit.setText(str(5))
        self.leg_grid_layout.addWidget(self.thine_to_knee_jnt_line_edit, 4, 1, 1, 3)

        # KNEE TO BALL LABEL
        self.knee_to_ball_jnt_label = QtGui.QLabel(self.widget)
        self.knee_to_ball_jnt_label.setObjectName("knee_to_ball_jnt_label")
        self.knee_to_ball_jnt_label.setText('Knee to Ball Joint')
        self.leg_grid_layout.addWidget(self.knee_to_ball_jnt_label, 5, 0, 1, 1)
        # KNEE TO BALL LINE EDIT
        self.knee_to_foot_jnt_line_edit = QtGui.QLineEdit(self.widget)
        self.knee_to_foot_jnt_line_edit.setObjectName("knee_to_ball_jnt_line_edit")
        self.knee_to_foot_jnt_line_edit.setValidator(self.validator)
        self.knee_to_foot_jnt_line_edit.setText(str(5))
        self.leg_grid_layout.addWidget(self.knee_to_foot_jnt_line_edit, 5, 1, 1, 3)

        # FOOT CHECKBOX
        self.foot_check_box = QtGui.QCheckBox(self.widget)
        self.foot_check_box.setObjectName("foot_check_box")
        self.foot_check_box.setText('Foot')
        self.foot_check_box.stateChanged.connect(self.leg_check_box_def)
        self.leg_grid_layout.addWidget(self.foot_check_box, 6, 0, 1, 1)

        # NO OF THE FINGER LABEL
        self.no_of_finger_label = QtGui.QLabel(self.widget)
        self.no_of_finger_label.setObjectName("no_of_finger_label")
        self.no_of_finger_label.setText('No of Finger')
        self.no_of_finger_label.setDisabled(True)
        self.leg_grid_layout.addWidget(self.no_of_finger_label, 7, 0, 1, 1)
        # NO FO THE FINGER LINE EDIT
        self.no_finger_line_edit = QtGui.QLineEdit(self.widget)
        self.no_finger_line_edit.setObjectName("no_finger_line_edit")
        self.no_finger_line_edit.setValidator(self.validator)
        self.no_finger_line_edit.setDisabled(True)
        self.no_finger_line_edit.setText('0')
        self.no_finger_line_edit.textChanged.connect(self.no_finger_line_edit_def)
        self.leg_grid_layout.addWidget(self.no_finger_line_edit, 8, 1, 1, 3)

        # LEG BUTTON
        self.leg_create_button = QtGui.QPushButton(self.widget)
        self.leg_create_button.setObjectName("leg_create_button")
        self.leg_create_button.setText('Create Leg')
        self.leg_create_button.clicked.connect(self.new_leg_def)
        self.leg_grid_layout.addWidget(self.leg_create_button, 8, 0, 1, 4)

        self.spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.leg_grid_layout.addItem(self.spacerItem, 9, 0, 1, 1)
        self.layout.addLayout(self.leg_grid_layout)

    def clear(self):
        self.rig_helper_class.clearLayout(self.leg_grid_layout)

    def mirror_def(self):
        self.rig_helper_class.mirror_def(self.mirror_check_box,self.left_check_box,self.right_check_box)

    def leg_check_box_def(self):
        # get the statu
        self.no_finger_line_edit.setText(str(3))
        if self.foot_check_box.isChecked():
            self.no_of_finger_label.setDisabled(False)
            self.no_finger_line_edit.setDisabled(False)
        else:
            self.no_of_finger_label.setDisabled(True)
            self.no_finger_line_edit.setDisabled(True)

    def no_finger_line_edit_def(self):
        # get the value
        grid_value = 6
        self.leg_create_button.deleteLater()
        # delete the latest one
        a = 0
        while a < len(self.leg_finger_label):
            self.leg_finger_label[a].deleteLater()
            self.leg_finger_line_edit[a].deleteLater()
            a += 1
        self.leg_finger_label = {}
        self.leg_finger_line_edit = {}
        if self.no_finger_line_edit.text() != '':
            self.no_finger_line_edit_query = int(self.no_finger_line_edit.text())
            a = 0
            value = 0
            while a < self.no_finger_line_edit_query:
                # FINGER_2 LABEL
                grid_value = 9 + a + 1

                self.leg_finger_label[value] = QtGui.QLabel(self.widget)
                self.leg_finger_label[value].setObjectName("finger_2_label")
                self.leg_finger_label[value].setText('Finger ' + str(a + 1))
                self.leg_grid_layout.addWidget(self.leg_finger_label[value], grid_value, 0, 1, 3)
                # FINGER_2 LINE EDIT
                self.leg_finger_line_edit[value] = QtGui.QLineEdit(self.widget)
                self.leg_finger_line_edit[value].setObjectName("finger_2_line_edit")
                self.leg_finger_line_edit[value].setValidator(self.validator)
                self.leg_finger_line_edit[value].setText(str(5))
                self.leg_grid_layout.addWidget(self.leg_finger_line_edit[value], grid_value, 1, 1, 3)
                value += 1
                a += 1
            grid_value += 1
            self.leg_create_button = QtGui.QPushButton(self.widget)
            self.leg_create_button.setObjectName("leg_create_button")
            self.leg_create_button.setText('Create Leg')
            self.leg_create_button.clicked.connect(self.new_leg_def)
            self.leg_grid_layout.addWidget(self.leg_create_button, grid_value, 0, 1, 4)
            grid_value += 1
            self.leg_grid_layout.addItem(self.spacerItem, grid_value, 0, 1, 1)

        else:
            grid_value += 1
            self.leg_create_button = QtGui.QPushButton(self.widget)
            self.leg_create_button.setObjectName("leg_create_button")
            self.leg_create_button.setText('Create Arm')
            self.leg_create_button.clicked.connect(self.new_leg_def)
            self.leg_grid_layout.addWidget(self.leg_create_button, grid_value, 0, 1, 4)
            grid_value += 1
            self.leg_grid_layout.addItem(self.spacerItem, grid_value, 0, 1, 1)


    def new_leg_def(self):
        mirror = self.mirror_check_box.isChecked()
        left = self.left_check_box.isChecked()
        right = self.right_check_box.isChecked()
        type = self.type_leg_combo_box.currentText()
        hip = self.hip_check_box.isChecked()
        butt = self.butt_check_box.isChecked()
        thine_to_knee = self.thine_to_knee_jnt_line_edit.text()
        knee_to_foot = self.knee_to_foot_jnt_line_edit.text()
        foot = self.foot_check_box.isChecked()
        no_finger = self.no_finger_line_edit.text()
        hip_pos = [0, 88, 3]
        a = 0
        finger_list = []
        while a < int(no_finger):
            finger_val = self.leg_finger_line_edit[a].text()
            finger_list.append(finger_val)
            a += 1
        prefix_name = 'Template'

        if left  == True:
            side = 'L'
            base_color = 'Blue'
            if type == 'Human':
                pos_list = {}
                pos_list['thine_pos']  = [8.177, 83.76, 2.826]
                pos_list['shine_pos'] = [8.177, 48.005, 2.509]
                pos_list['foot_pos'] = [8.177, 9.675, -0.261]
                pos_list['ball_pos'] = [8.177, 0.681, 12.849]
                pos_list['end_pos'] = [8.177, 0.266, 22.085]
                pos_list['butt_pos'] = [8.177, 83.76, -2.319]
                pos_list['finger_default_pos'] = [7.764, 0, 16]
                pos_list['side_1_pos'] = [12.32406997680664, 0.018575215712189674, -34.387516021728516]
                pos_list['side_2_pos'] = [6.035772800445557, 0.018575211986899376, -34.387516021728516]

            if type == 'Animal_Front_Leg':
                pos_list = {}
                pos_list['scapula_pos'] = [7.953, 89.142, -7.015]
                pos_list['upper_hand_pos'] = [7.953, 67.2833480834961, 41.54819107055664]
                pos_list['shoulder_pos'] = [7.952999114990234, 52.012237548828125, 29.66240882873535]
                pos_list['lbow_pos'] = [7.952999114990234, 29.241947174072266, 32.31039810180664]
                pos_list['hand_pos'] = [7.952999114990234, 11.398856163024902, 30.00531005859375]
                pos_list['hand_offset_pos'] = [7.952999114990234, 2.2240066528320312, 33.85894775390625]
                pos_list['end_pos'] = [7.952999114990234, 0.007954543456435204, 37.533565521240234]
                pos_list['leg_side_1_pos'] = [10.791987419128418, -0.008373272605240345, 34.169864654541016]
                pos_list['leg_side_2_pos'] = [5.3170166015625, -0.008373272605240345, 34.169864654541016]
                pos_list['leg_back_pos'] = [7.952999114990234, 0.02303881198167801, 33.10665512084961]
                pos_list['Shoulder_Center_pos'] = [0, 93, 0]

            if type == 'Animal_Back_Leg':
                pos_list = {}
                pos_list['thine_pos'] = [9.094188690185547, 88.65216064453125, -40.670589447021484]
                pos_list['shine_pos'] = [9.094188690185547, 67.30301666259766, -30.152219772338867]
                pos_list['foot_pos'] = [9.094188690185547, 32.13379669189453, -44.1630744934082]
                pos_list['foot_offset_1'] = [9.094188690185547, 12.249735832214355, -41.12364959716797]
                pos_list['foot_offset_2'] = [9.094188690185547, 5.470892429351807, -37.380550384521484]
                pos_list['foot_offset_3'] = [9.094188690185547, 2.3224918842315674, -34.387516021728516]
                pos_list['foot_end'] = [9.094188690185547, -0.0035923428367823362, -30.59406089782715]
                pos_list['foot_back'] = [9.094188690185547, 0.0034828113857656717, -35.587162017822266]
                pos_list['foot_side_1'] = [12.32406997680664, 0.018575215712189674, -34.387516021728516]
                pos_list['foot_side_2'] = [6.035772800445557, 0.018575211986899376, -34.387516021728516]

            self.leg_create_class.leg_create(mirror=mirror,
                                             left_leg=left,
                                             right_leg=right,
                                             hip=hip,
                                             butt=butt,
                                             thine_to_knee=thine_to_knee,
                                             knee_to_foot=knee_to_foot,
                                             foot=foot,
                                             no_finger=no_finger,
                                             base_color=base_color,
                                             pos_list=pos_list,
                                             hip_pos = hip_pos,
                                             prefix_name=prefix_name,
                                             side=side,
                                             base_ctrl_color=base_color,
                                             finger_list=finger_list,
                                             type=type,
                                             leg_finger=self.leg_finger_line_edit)

        if right  == True:
            side = 'R'
            base_color = 'Red'
            if type == 'Human':
                pos_list = {}
                pos_list['thine_pos'] = [-8.177, 83.76, 2.826]
                pos_list['shine_pos'] = [-8.177, 48.005, 2.509]
                pos_list['foot_pos'] = [-8.177, 9.675, -0.261]
                pos_list['ball_pos'] = [-8.177, 0.681, 12.849]
                pos_list['end_pos'] = [-8.177, 0.266, 22.085]
                pos_list['butt_pos'] = [-8.177, 83.76, -2.319]

                pos_list['finger_default_pos'] = [-7.764, 0, 16]
                pos_list['side_1_pos'] = []
                pos_list['side_2_pos'] = []

            if type == 'Animal_Front_Leg':
                pos_list = {}
                pos_list['scapula_pos'] = [-7.952999114990234, 88.23869323730469, 26.783912658691406]
                pos_list['upper_hand_pos'] = [-7.952999114990234, 67.2833480834961, 41.54819107055664]
                pos_list['shoulder_pos'] = [-7.952999114990234, 52.012237548828125, 29.66240882873535]
                pos_list['lbow_pos'] = [-7.952999114990234, 29.241947174072266, 32.31039810180664]
                pos_list['hand_pos'] = [-7.952999114990234, 11.398856163024902, 30.00531005859375]
                pos_list['hand_offset_pos'] = [-7.952999114990234, 2.2240066528320312, 33.85894775390625]
                pos_list['end_pos'] = [-7.952999114990234, 0.007954543456435204, 37.533565521240234]
                pos_list['leg_side_1_pos'] = [-5.3170166015625, -0.008373272605240345, 34.169864654541016]
                pos_list['leg_side_2_pos'] = [-10.791987419128418, -0.008373272605240345, 34.169864654541016]
                pos_list['leg_back_pos'] = [-7.952999114990234, 0.02303881198167801, 33.10665512084961]
                pos_list['Shoulder_Center_pos'] = [0,93,0]

            if type == 'Animal_Back_Leg':
                pos_list = {}
                pos_list['thine_pos'] = [-9.094188690185547, 88.65216064453125, -40.670589447021484]
                pos_list['shine_pos'] = [-9.094188690185547, 67.30301666259766, -30.152219772338867]
                pos_list['foot_pos'] = [-9.094188690185547, 32.13379669189453, -44.1630744934082]
                pos_list['foot_offset_1'] = [-9.094188690185547, 12.249735832214355, -41.12364959716797]
                pos_list['foot_offset_2'] = [-9.094188690185547, 5.470892429351807, -37.380550384521484]
                pos_list['foot_offset_3'] = [-9.094188690185547, 2.3224918842315674, -34.387516021728516]
                pos_list['foot_end'] = [-9.094188690185547, -0.0035923428367823362, -30.59406089782715]
                pos_list['foot_back'] = [-9.094188690185547, 0.0034828113857656717, -35.587162017822266]
                pos_list['foot_side_1'] = [-6.035772800445557, 0.018575211986899376, -34.387516021728516]
                pos_list['foot_side_2'] = [-12.32406997680664, 0.018575215712189674, -34.387516021728516]


            self.leg_create_class.leg_create(mirror=mirror,
                                             left_leg=left,
                                             right_leg=right,
                                             hip=hip,
                                             butt=butt,
                                             thine_to_knee=thine_to_knee,
                                             knee_to_foot=knee_to_foot,
                                             foot=foot,
                                             no_finger=no_finger,
                                             base_color=base_color,
                                             pos_list=pos_list,
                                             hip_pos=hip_pos,
                                             prefix_name=prefix_name,
                                             side=side,
                                             base_ctrl_color=base_color,
                                             finger_list=finger_list,
                                             type=type,
                                             leg_finger=self.leg_finger_line_edit)

