class WING:
    def __init__(self):
        self.another_sphere_list = []
        self.helper_class = helper.HELPER()
        self.controller_class = controller_rig.controler()
        self.connection_class = connection.CONNECTION()
        self.wing_finger_label = {}
        self.wing_finger_line_edit = {}

        self.sphere_list = []
        self.cluster_list = []
        self.cylinder_list = []
        self.ctrl_list = []
        self.crv_list = []

    def new(self, widget, layout):
        self.widget = widget
        self.wing_grid_layout = QtGui.QGridLayout()
        self.wing_grid_layout.setObjectName("wing_grid_layout")

        # MIRROR CHECK BOX
        self.wing_mirror_check_box = QtGui.QCheckBox(self.widget)
        self.wing_mirror_check_box.setObjectName("mirror_check_box")
        self.wing_mirror_check_box.setText('Mirror')
        self.wing_mirror_check_box.setChecked(True)
        self.wing_mirror_check_box.stateChanged.connect(self.mirror_status_def)
        self.wing_grid_layout.addWidget(self.wing_mirror_check_box, 0, 0, 1, 1)

        # LEFT WING CHECK BOX
        self.wing_left_check_box = QtGui.QCheckBox(self.widget)
        self.wing_left_check_box.setObjectName("left_check_box")
        self.wing_left_check_box.setText('Left Wing')
        self.wing_left_check_box.setChecked(True)
        self.wing_grid_layout.addWidget(self.wing_left_check_box, 1, 0, 1, 1)

        # RIGHT WING CHECK BOX
        self.wing_right_check_box = QtGui.QCheckBox(self.widget)
        self.wing_right_check_box.setObjectName("right_check_box")
        self.wing_right_check_box.setText('Righ Wing')
        self.wing_right_check_box.setChecked(True)
        self.wing_grid_layout.addWidget(self.wing_right_check_box, 1, 2, 1, 1)

        # WING TYPE COMBO BOX
        self.wing_type_combo_box = QtGui.QComboBox(self.widget)
        self.wing_type_combo_box.setObjectName("wing_type_combo")
        self.wing_type_combo_box.addItem("Dragon")
        self.wing_type_combo_box.addItem("Bird")
        self.wing_type_combo_box.currentIndexChanged.connect(self.wing_type_combo_box_def)
        self.wing_grid_layout.addWidget(self.wing_type_combo_box, 2, 0, 1, 4)

        # UPPER WING BASE JOINT LABEL
        self.upper_wing_base_jnt_label = QtGui.QLabel(self.widget)
        self.upper_wing_base_jnt_label.setObjectName("upper_wing_base_jnt_label")
        self.upper_wing_base_jnt_label.setText('Upper Wing Base Joint')
        self.wing_grid_layout.addWidget(self.upper_wing_base_jnt_label, 3, 0, 1, 1)
        # UPPER WING BASE JOINT LINE EDIT
        self.upper_wing_base_jnt_line_edit = QtGui.QLineEdit(self.widget)
        self.upper_wing_base_jnt_line_edit.setObjectName("upper_wing_base_jnt_line_edit")
        self.validator = QtGui.QDoubleValidator()
        self.upper_wing_base_jnt_line_edit.setValidator(self.validator)
        self.upper_wing_base_jnt_line_edit.setText(str(6))
        self.wing_grid_layout.addWidget(self.upper_wing_base_jnt_line_edit, 3, 1, 1, 3)

        # LOWER WING BASE JOINT LABEL
        self.lower_wing_base_jnt_label = QtGui.QLabel(self.widget)
        self.lower_wing_base_jnt_label.setObjectName("lower_wing_base_jnt_label")
        self.lower_wing_base_jnt_label.setText('Lower Wing Base Joint')
        self.wing_grid_layout.addWidget(self.lower_wing_base_jnt_label, 4, 0, 1, 1)
        # LOWER WING BASE JOINT LINE EDIT
        self.lower_wing_base_jnt_line_edit = QtGui.QLineEdit(self.widget)
        self.lower_wing_base_jnt_line_edit.setObjectName("lower_wing_base_jnt_line_edit")
        self.lower_wing_base_jnt_line_edit.setValidator(self.validator)
        self.lower_wing_base_jnt_line_edit.setText(str(6))
        self.wing_grid_layout.addWidget(self.lower_wing_base_jnt_line_edit, 4, 1, 1, 3)

        # HAND CHECK BOX
        self.wing_hand_check_box = QtGui.QCheckBox(self.widget)
        self.wing_hand_check_box.setObjectName("hand_check_box")
        self.wing_hand_check_box.setText('Wing Hand')
        self.wing_hand_check_box.stateChanged.connect(self.wing_hand_check_def)
        self.wing_grid_layout.addWidget(self.wing_hand_check_box, 5, 0, 1, 1)

        # NO OF FINGER LABEL
        self.wing_no_of_finger_label = QtGui.QLabel(self.widget)
        self.wing_no_of_finger_label.setObjectName("no_of_finger_label")
        self.wing_no_of_finger_label.setText('No Of Finger')
        self.wing_no_of_finger_label.setDisabled(True)
        self.wing_grid_layout.addWidget(self.wing_no_of_finger_label, 6, 0, 1, 1)
        # NO OF FINGER LINE EDIT
        self.wing_no_of_finger_line_edit = QtGui.QLineEdit(self.widget)
        self.wing_no_of_finger_line_edit.setObjectName("no_of_finger_line_edit")
        self.wing_no_of_finger_line_edit.setValidator(self.validator)
        self.wing_no_of_finger_line_edit.setDisabled(True)
        self.wing_no_of_finger_line_edit.textChanged.connect(self.no_finger_line_edit_def)
        self.wing_grid_layout.addWidget(self.wing_no_of_finger_line_edit, 6, 1, 1, 3)

        # CREATE WING
        self.create_wing_button = QtGui.QPushButton(self.widget)
        self.create_wing_button.setObjectName("create_wing_button")
        self.create_wing_button.setText('Create Wing')
        self.create_wing_button.clicked.connect(self.new_wing_def)
        self.wing_grid_layout.addWidget(self.create_wing_button, 7, 0, 1, 4)

        self.spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.wing_grid_layout.addItem(self.spacerItem, 8, 0, 1, 1)
        layout.addLayout(self.wing_grid_layout)

    def new_clear(self):
        self.helper_class.clearLayout(self.wing_grid_layout)

    def new_wing_def(self):
        # get the data
        self.wing_mirror_check_box_query = self.wing_mirror_check_box.isChecked()
        self.wing_left_check_box_query = self.wing_left_check_box.isChecked()
        self.wing_right_check_box_queru = self.wing_right_check_box.isChecked()
        self.wing_type_combo_box_query = self.wing_type_combo_box.currentText()
        self.upper_wing_base_jnt_line_edit_query = int(self.upper_wing_base_jnt_line_edit.text())
        self.lower_wing_base_jnt_line_edit_query = int(self.lower_wing_base_jnt_line_edit.text())

        # get the type
        if self.wing_type_combo_box_query == 'Dragon':
            self.wing_hand_check_box_query = self.wing_hand_check_box.isChecked()
            if self.wing_hand_check_box_query == True:
                self.wing_no_of_finger_line_edit_query = int(self.wing_no_of_finger_line_edit.text())
            self.type = 'Dragon'
            self.dragon_def()
        elif self.wing_type_combo_box_query == 'Bird':
            # self.wing_end_jnt_line_edit
            self.wing_end_jnt_line_edit_query = int(self.wing_end_jnt_line_edit.text())
            self.type = 'Bird'
            self.bird_def()

    def dragon_def(self):
        if self.wing_left_check_box_query == True:
            self.dragon_left_def()
        if self.wing_right_check_box_queru == True:
            self.dragon_right_def()

    def bird_def(self):
        if self.wing_left_check_box_query == True:
            self.bird_left_def()
        if self.wing_right_check_box_queru == True:
            self.bird_right_def()

    def dragon_left_def(self):
        # Chck if left val
        if cmds.objExists("*_L_Wing_Dragon_Tem_*_Main_Grp"):
            cmds.select("*_L_Wing_Dragon_Tem_*_Main_Grp")
            sel_main_grp = cmds.ls(sl=True)
            len_sel_main_grp = len(sel_main_grp)
            self.val = len_sel_main_grp + 1
        else:
            self.val = 1

        self.wing_side = 'L'
        self.prefix_name = 'Template'
        self.base_ctrl_color = 'Blue'
        self.wing_base_pos = [0, 0, 0]
        self.wing_shoulder_pos = [3.978, 3.344, 0]
        self.wing_upper_pos = [10.838, 5.503, 0]
        self.wing_lbow_pos = [39.802, 5.578, -5.31]
        self.wing_hand_pos = [69.438, 6.028, 3.403]
        self.wing_hand_2_pos = [75.194, 5.578, 4.147]
        self.wing_branch_1_1_pos = [80.749, 5.558, 3.007]
        self.wing_branch_1_2_pos = [120.568, 5.442, -3.569]
        self.wing_branch_1_3_pos = [144.519, 5.57, -21.348]
        self.wing_branch_1_4_pos = [158.283, 5.361, -37.462]
        self.wing_branch_2_1_pos = [78.766, 5.802, -1.023]
        self.wing_branch_2_2_pos = [104.89, 5.401, -34.693]
        self.wing_branch_2_3_pos = [109.776, 5.57, -66.382]
        self.wing_branch_2_4_pos = [108.887, 5.421, -92.353]
        self.wing_branch_3_1_pos = [72.002, 5.615, -1.492]
        self.wing_branch_3_2_pos = [68.684, 5.448, -40.505]
        self.wing_branch_3_3_pos = [58.507, 5.289, -67.983]
        self.wing_branch_3_4_pos = [45.556, 5.417, -89.574]
        self.wing_branch_4_1_pos = [39.075, 5.396, -10.858]
        self.wing_branch_4_2_pos = [35.639, 5.341, -31.178]
        self.wing_branch_4_3_pos = [29.772, 5.603, -46.35]
        self.wing_branch_4_4_pos = [23.898, 5.23, -55.344]
        self.finger_pos = [75.194, 5.578, 4.147]

        # create a sphere
        self.wing_sphere_name()

        # cylinder
        self.wing_cylinder_def()

        # create a controller
        self.controller_def()

        if self.wing_hand_check_box_query == True:
            self.finger_def()

        # put in one group
        self.final_group()

    def dragon_right_def(self):
        # Chck if left val
        if cmds.objExists("*_R_Wing_Dragon_Tem_*_Main_Grp"):
            cmds.select("*_R_Wing_Dragon_Tem_*_Main_Grp")
            sel_main_grp = cmds.ls(sl=True)
            len_sel_main_grp = len(sel_main_grp)
            self.val = len_sel_main_grp + 1
        else:
            self.val = 1

        self.wing_side = 'R'
        self.prefix_name = 'Template'
        self.base_ctrl_color = 'Red'
        self.wing_base_pos = [0, 0, 0]
        self.wing_shoulder_pos = [-3.978, 3.344, 0]
        self.wing_upper_pos = [-10.838, 5.503, 0]
        self.wing_lbow_pos = [-39.802, 5.578, -5.31]
        self.wing_hand_pos = [-69.438, 6.028, 3.403]
        self.wing_hand_2_pos = [-75.194, 5.578, 4.147]
        self.wing_branch_1_1_pos = [-80.749, 5.558, 3.007]
        self.wing_branch_1_2_pos = [-120.568, 5.442, -3.569]
        self.wing_branch_1_3_pos = [-144.519, 5.57, -21.348]
        self.wing_branch_1_4_pos = [-158.283, 5.361, -37.462]
        self.wing_branch_2_1_pos = [-78.766, 5.802, -1.023]
        self.wing_branch_2_2_pos = [-104.89, 5.401, -34.693]
        self.wing_branch_2_3_pos = [-109.776, 5.57, -66.382]
        self.wing_branch_2_4_pos = [-108.887, 5.421, -92.353]
        self.wing_branch_3_1_pos = [-72.002, 5.615, -1.492]
        self.wing_branch_3_2_pos = [-68.684, 5.448, -40.505]
        self.wing_branch_3_3_pos = [-58.507, 5.289, -67.983]
        self.wing_branch_3_4_pos = [-45.556, 5.417, -89.574]
        self.wing_branch_4_1_pos = [-39.075, 5.396, -10.858]
        self.wing_branch_4_2_pos = [-35.639, 5.341, -31.178]
        self.wing_branch_4_3_pos = [-29.772, 5.603, -46.35]
        self.wing_branch_4_4_pos = [-23.898, 5.23, -55.344]
        self.finger_pos = [-75.194, 5.578, 4.147]

        # create a sphere
        self.wing_sphere_name()

        # cylinder
        self.wing_cylinder_def()

        # create a controller
        self.controller_def()

        if self.wing_hand_check_box_query == True:
            self.finger_def()

        # put in one group
        self.final_group()

        if self.wing_mirror_check_box_query == True:
            self.mirror_value()

    def bird_left_def(self):
        # Chck if left val
        if cmds.objExists("*_L_Wing_Bird_Tem_*_Main_Grp"):
            cmds.select("*_L_Wing_Bird_Tem_*_Main_Grp")
            sel_main_grp = cmds.ls(sl=True)
            len_sel_main_grp = len(sel_main_grp)
            self.val = len_sel_main_grp + 1
        else:
            self.val = 1

        self.wing_side = 'L'
        self.prefix_name = 'Template'
        self.base_ctrl_color = 'Blue'
        self.wing_base_pos = [0, 0, 0]
        self.wing_upper_pos = [3.93, 4.608, 9.992]
        self.wing_shoulder_pos = [10.664, 17.259, -2.813]
        self.wing_lbow_pos = [22.144, 15.271, -4.362]
        self.wing_hand_pos = [34.554, 21.046, 2.625]
        self.wing_hand_end_pos = [52.766, 21.671, 4.299]

        # Wing Bird Sphere
        self.wing_bird_sphere_name()

        # WING BIRD CYLINDER
        self.wing_bird_cylinder_def()

        # WING BIRD CONTROLLER
        self.wing_bird_ctrl_def()

        # final group
        self.final_group()

    def bird_right_def(self):
        # Chck if left val
        if cmds.objExists("*_R_Wing_Bird_Tem_*_Main_Grp"):
            cmds.select("*_R_Wing_Bird_Tem_*_Main_Grp")
            sel_main_grp = cmds.ls(sl=True)
            len_sel_main_grp = len(sel_main_grp)
            self.val = len_sel_main_grp + 1
        else:
            self.val = 1

        self.wing_side = 'R'
        self.prefix_name = 'Template'
        self.base_ctrl_color = 'Red'
        self.wing_base_pos = [0, 0, 0]
        self.wing_upper_pos = [-3.93, 4.608, 9.992]
        self.wing_shoulder_pos = [-10.664, 17.259, -2.813]
        self.wing_lbow_pos = [-22.144, 15.271, -4.362]
        self.wing_hand_pos = [-34.554, 21.046, 2.625]
        self.wing_hand_end_pos = [-52.766, 21.671, 4.299]

        # Wing Bird Sphere
        self.wing_bird_sphere_name()

        # WING BIRD CYLINDER
        self.wing_bird_cylinder_def()

        # WING BIRD CONTROLLER
        self.wing_bird_ctrl_def()

        # final group
        self.final_group()

        if self.wing_mirror_check_box_query == True:
            self.mirror_value()

    def wing_bird_sphere_name(self):
        # create a sphere on each position
        self.sphere_list = []
        self.cluster_list = []
        self.cylinder_list = []
        self.ctrl_list = []
        self.crv_list = []

        # Base
        self.base_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Base_Tem_" + str(self.val)
        self.sphere_basic_def(self.base_common,
                              self.wing_base_pos)

        # upper Pos
        self.upper_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Upper_Tem_" + str(
            self.val)
        self.sphere_basic_def(self.upper_common,
                              self.wing_upper_pos)

        # shoulder Pos
        self.shoulder_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Shoulder_Tem_" + str(
            self.val)
        self.sphere_basic_def(self.shoulder_common,
                              self.wing_shoulder_pos)

        # lbow Pos
        self.lbow_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_lBow_Tem_" + str(self.val)
        self.sphere_basic_def(self.lbow_common,
                              self.wing_lbow_pos)

        # hand Pos
        self.hand_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Hand_Tem_" + str(self.val)
        self.sphere_basic_def(self.hand_common,
                              self.wing_hand_pos)

        # hand End Pos
        self.hand_end_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Hand_End_Tem_" + str(
            self.val)
        self.sphere_basic_def(self.hand_end_common,
                              self.wing_hand_end_pos)

    def wing_bird_cylinder_def(self):
        # base to upper
        self.base_to_upper_cyliner_common_middle = 'Base_to_Upper'
        self.cylinder_rotate = [0, 0, 0]
        self.first_sphere_name = self.helper_class.object_name(self.base_common, geo_name=True)
        self.secound_sphere_name = self.helper_class.object_name(self.upper_common, geo_name=True)
        self.cylinder_basic_def(self.base_to_upper_cyliner_common_middle,
                                self.cylinder_rotate,
                                self.first_sphere_name,
                                self.secound_sphere_name)

        # upper to shoulder
        self.upper_to_shoulder_cyliner_common_middle = 'Upper_to_Shoulder'
        self.cylinder_rotate = [0, 0, 90]
        self.first_sphere_name = self.helper_class.object_name(self.upper_common, geo_name=True)
        self.secound_sphere_name = self.helper_class.object_name(self.shoulder_common, geo_name=True)
        self.cylinder_basic_def(self.upper_to_shoulder_cyliner_common_middle,
                                self.cylinder_rotate,
                                self.secound_sphere_name,
                                self.first_sphere_name)

        # shoulder to lbow
        self.shoulder_to_lbow_cyliner_common_middle = 'Shoulder_to_lBow'
        self.cylinder_rotate = [0, 0, 90]
        self.first_sphere_name = self.helper_class.object_name(self.shoulder_common, geo_name=True)
        self.secound_sphere_name = self.helper_class.object_name(self.lbow_common, geo_name=True)
        self.cylinder_basic_def(self.shoulder_to_lbow_cyliner_common_middle,
                                self.cylinder_rotate,
                                self.secound_sphere_name,
                                self.first_sphere_name)

        # lbow to hand
        self.lbow_to_hand_cyliner_common_middle = 'lBow_to_Hand'
        self.cylinder_rotate = [0, 0, 90]
        self.first_sphere_name = self.helper_class.object_name(self.lbow_common, geo_name=True)
        self.secound_sphere_name = self.helper_class.object_name(self.hand_common, geo_name=True)
        self.cylinder_basic_def(self.lbow_to_hand_cyliner_common_middle,
                                self.cylinder_rotate,
                                self.secound_sphere_name,
                                self.first_sphere_name)

        # hand to hand2
        self.hand_to_hand_end_cyliner_common_middle = 'Hand_to_Hand_End'
        self.cylinder_rotate = [0, 0, 90]
        self.first_sphere_name = self.helper_class.object_name(self.hand_common, geo_name=True)
        self.secound_sphere_name = self.helper_class.object_name(self.hand_end_common, geo_name=True)
        self.cylinder_basic_def(self.hand_to_hand_end_cyliner_common_middle,
                                self.cylinder_rotate,
                                self.secound_sphere_name,
                                self.first_sphere_name)

    def wing_bird_ctrl_def(self):
        # CREATE CONTROLLER
        self.ctrl_lower_size = [0.5, 0.5, 0.5]
        self.ctrl_outer_size = [1.5, 1.5, 1.5]
        self.ctrl_rotate = [0, 0, 90]
        self.base_ctrl_freez_trans = True
        self.base_ctrl_freez_rotate = True
        self.base_ctrl_freez_scale = True

        # BASE CONTROLLER
        self.sphere_handle_name = self.helper_class.object_name(self.base_common, cluster_name=True) + 'Handle'
        self.cylinder_lower_handle_name = self.get_cyliner_clu_name('Lower',
                                                                    self.base_to_upper_cyliner_common_middle) + 'Handle'
        self.base_parent_const_list = [self.sphere_handle_name,
                                       self.cylinder_lower_handle_name]
        self.controller_small_big(base_name=self.base_common,
                                  parent_list=self.base_parent_const_list,
                                  pos=self.wing_base_pos,
                                  ctrl_rotate=self.ctrl_rotate)
        self.base_inner_ctrl = self.base_common + '_Inner_Ctrl'
        self.base_outer_ctrl = self.base_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.base_inner_ctrl)
        self.ctrl_list.append(self.base_outer_ctrl)

        # UPPER CONTROLLER
        self.sphere_handle_name = self.helper_class.object_name(self.upper_common, cluster_name=True) + 'Handle'
        self.cylinder_upper_handle_name = self.get_cyliner_clu_name('Upper',
                                                                    self.upper_to_shoulder_cyliner_common_middle) + 'Handle'
        self.base_parent_const_list = [self.sphere_handle_name,
                                       self.cylinder_upper_handle_name]
        self.controller_small_big(base_name=self.upper_common,
                                  parent_list=self.base_parent_const_list,
                                  pos=self.wing_upper_pos,
                                  ctrl_rotate=self.ctrl_rotate)
        self.upper_inner_ctrl = self.upper_common + '_Inner_Ctrl'
        self.upper_outer_ctrl = self.upper_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.upper_inner_ctrl)
        self.ctrl_list.append(self.upper_outer_ctrl)
        cmds.select(self.helper_class.object_name(self.upper_common, ctrl_outer_name=True),
                    self.helper_class.object_name(self.base_common, ctrl_outer_name=True))
        cmds.parent()

        # SHOULDER CONTROLLER
        self.sphere_handle_name = self.helper_class.object_name(self.shoulder_common, cluster_name=True) + 'Handle'
        self.cylinder_upper_handle_name = self.get_cyliner_clu_name('Upper',
                                                                    self.shoulder_to_lbow_cyliner_common_middle) + 'Handle'
        self.base_parent_const_list = [self.sphere_handle_name,
                                       self.cylinder_upper_handle_name]
        self.controller_small_big(base_name=self.shoulder_common,
                                  parent_list=self.base_parent_const_list,
                                  pos=self.wing_shoulder_pos,
                                  ctrl_rotate=self.ctrl_rotate)
        self.shoulder_inner_ctrl = self.shoulder_common + '_Inner_Ctrl'
        self.shoulder_outer_ctrl = self.shoulder_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.shoulder_inner_ctrl)
        self.ctrl_list.append(self.shoulder_outer_ctrl)
        cmds.select(self.helper_class.object_name(self.shoulder_common, ctrl_outer_name=True),
                    self.helper_class.object_name(self.upper_common, ctrl_outer_name=True))
        cmds.parent()

        # LBOW CONTROLLER
        self.sphere_handle_name = self.helper_class.object_name(self.lbow_common, cluster_name=True) + 'Handle'
        self.cylinder_upper_handle_name = self.get_cyliner_clu_name('Upper',
                                                                    self.lbow_to_hand_cyliner_common_middle) + 'Handle'
        self.base_parent_const_list = [self.sphere_handle_name,
                                       self.cylinder_upper_handle_name]
        self.controller_small_big(base_name=self.lbow_common,
                                  parent_list=self.base_parent_const_list,
                                  pos=self.wing_lbow_pos,
                                  ctrl_rotate=self.ctrl_rotate)
        self.lbow_inner_ctrl = self.lbow_common + '_Inner_Ctrl'
        self.lbow_outer_ctrl = self.lbow_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.lbow_inner_ctrl)
        self.ctrl_list.append(self.lbow_outer_ctrl)
        cmds.select(self.helper_class.object_name(self.lbow_common, ctrl_outer_name=True),
                    self.helper_class.object_name(self.shoulder_common, ctrl_outer_name=True))
        cmds.parent()

        # HAND CONTROLLER
        self.sphere_handle_name = self.helper_class.object_name(self.hand_common, cluster_name=True) + 'Handle'
        self.cylinder_upper_handle_name = self.get_cyliner_clu_name('Upper',
                                                                    self.hand_to_hand_end_cyliner_common_middle) + 'Handle'
        self.base_parent_const_list = [self.sphere_handle_name,
                                       self.cylinder_upper_handle_name]
        self.controller_small_big(base_name=self.hand_common,
                                  parent_list=self.base_parent_const_list,
                                  pos=self.wing_hand_pos,
                                  ctrl_rotate=self.ctrl_rotate)
        self.hand_inner_ctrl = self.hand_common + '_Inner_Ctrl'
        self.hand_outer_ctrl = self.hand_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.hand_inner_ctrl)
        self.ctrl_list.append(self.hand_outer_ctrl)
        cmds.select(self.helper_class.object_name(self.hand_common, ctrl_outer_name=True),
                    self.helper_class.object_name(self.lbow_common, ctrl_outer_name=True))
        cmds.parent()

        # HAND END CONTROLLER
        self.sphere_handle_name = self.helper_class.object_name(self.hand_end_common, cluster_name=True) + 'Handle'
        self.base_parent_const_list = [self.sphere_handle_name]
        self.controller_small_big(base_name=self.hand_end_common,
                                  parent_list=self.base_parent_const_list,
                                  pos=self.wing_hand_end_pos,
                                  ctrl_rotate=self.ctrl_rotate)
        self.hand_end_inner_ctrl = self.hand_end_common + '_Inner_Ctrl'
        self.hand_end_outer_ctrl = self.hand_end_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.hand_end_inner_ctrl)
        self.ctrl_list.append(self.hand_end_outer_ctrl)
        cmds.select(self.helper_class.object_name(self.hand_end_common, ctrl_outer_name=True),
                    self.helper_class.object_name(self.hand_common, ctrl_outer_name=True))
        cmds.parent()

        # do individual parent const
        self.cylinder_upper_handle_name = self.get_cyliner_clu_name('Upper',
                                                                    self.base_to_upper_cyliner_common_middle) + 'Handle'
        cmds.parentConstraint(self.upper_outer_ctrl, self.cylinder_upper_handle_name, mo=False)
        self.cylinder_upper_handle_name = self.get_cyliner_clu_name('Lower',
                                                                    self.upper_to_shoulder_cyliner_common_middle) + 'Handle'
        cmds.parentConstraint(self.shoulder_outer_ctrl, self.cylinder_upper_handle_name, mo=False)
        self.cylinder_upper_handle_name = self.get_cyliner_clu_name('Lower',
                                                                    self.shoulder_to_lbow_cyliner_common_middle) + 'Handle'
        cmds.parentConstraint(self.lbow_outer_ctrl, self.cylinder_upper_handle_name, mo=False)
        self.cylinder_upper_handle_name = self.get_cyliner_clu_name('Lower',
                                                                    self.lbow_to_hand_cyliner_common_middle) + 'Handle'
        cmds.parentConstraint(self.hand_outer_ctrl, self.cylinder_upper_handle_name, mo=False)
        self.cylinder_upper_handle_name = self.get_cyliner_clu_name('Lower',
                                                                    self.hand_to_hand_end_cyliner_common_middle) + 'Handle'
        cmds.parentConstraint(self.hand_end_outer_ctrl, self.cylinder_upper_handle_name, mo=False)

        # create a roll bone
        self.another_sphere_list = []
        self.roll_bone('Upper',
                       upper_object=self.shoulder_inner_ctrl,
                       lower_object=self.lbow_inner_ctrl,
                       no_of_bone=self.upper_wing_base_jnt_line_edit_query)
        self.grp_name = self.shoulder_inner_ctrl + '_' + self.lbow_inner_ctrl
        name = 'Shoulder'
        self.wing_feather(self.grp_name, name)

        self.another_sphere_list = []
        self.roll_bone('Lower',
                       upper_object=self.lbow_inner_ctrl,
                       lower_object=self.hand_inner_ctrl,
                       no_of_bone=self.lower_wing_base_jnt_line_edit_query)
        self.grp_name = self.lbow_inner_ctrl + '_' + self.hand_inner_ctrl + '_Grp'
        name = 'lBow'
        self.wing_feather(self.grp_name, name)

        self.another_sphere_list = []
        self.roll_bone('Lower_2',
                       upper_object=self.hand_inner_ctrl,
                       lower_object=self.hand_end_inner_ctrl,
                       no_of_bone=self.wing_end_jnt_line_edit_query)
        self.grp_name = self.hand_inner_ctrl + '_' + self.hand_end_inner_ctrl + '_Grp'
        name = 'Hand'
        self.wing_feather(self.grp_name, name)

    def wing_feather(self, grp_name, name):
        a = 0

        while a < len(self.another_sphere_list):

            # create a loc and get the position
            loc_name = 'Test_LOC'
            cmds.spaceLocator(n=loc_name, p=(0, 0, 0))
            self.helper_class.parent_constrain(self.another_sphere_list[a], [loc_name])
            translate_val = cmds.getAttr(loc_name + '.t')[0]
            translate_z = translate_val[2]

            b = 0
            while b < 6:

                # create a sphere and move
                translate_z -= 5
                pos_val = [translate_val[0],
                           translate_val[1],
                           translate_z]
                # self.prefix_name + "_" + self.wing_side  + "_Wing_" +  self.type + "_Base_Tem_" + str(self.val)
                sphere_common_name = self.prefix_name + "_" + self.wing_side + "_Wing_Feather_" + self.type + '_' + name + '_' + str(
                    a + 1) + '_' + str(b + 1) + '_Tem_' + str(self.val)
                # sphere_common_name = self.another_sphere_list[a] + '_Feather_' + name + '_' + str(a+1) + '_' + str(b+1)
                self.sphere_basic_def(sphere_common_name,
                                      pos_val)

                # create a controller
                # CREATE CONTROLLER
                self.ctrl_lower_size = [0.5, 0.5, 0.5]
                self.ctrl_outer_size = [1.5, 1.5, 1.5]
                self.ctrl_rotate = [90, 0, 0]
                self.base_ctrl_freez_trans = True
                self.base_ctrl_freez_rotate = True
                self.base_ctrl_freez_scale = True

                # BASE CONTROLLER
                self.sphere_handle_name = self.helper_class.object_name(sphere_common_name,
                                                                        cluster_name=True) + 'Handle'
                self.base_parent_const_list = [self.sphere_handle_name]
                self.controller_small_big(base_name=sphere_common_name,
                                          parent_list=self.base_parent_const_list,
                                          pos=pos_val,
                                          ctrl_rotate=self.ctrl_rotate)
                self.wing_feather_inner_ctrl = sphere_common_name + '_Inner_Ctrl'
                self.wing_feather_outer_ctrl = sphere_common_name + '_Outer_Ctrl'
                self.ctrl_list.append(self.wing_feather_inner_ctrl)
                self.ctrl_list.append(self.wing_feather_outer_ctrl)
                if b == 0:
                    cmds.select(self.wing_feather_outer_ctrl)
                    new_grp_name = grp_name + '_' + str(a) + '_Grp'
                    cmds.group(n=new_grp_name)
                    cmds.select(new_grp_name)
                    cmds.CenterPivot()
                    sphere_name = self.helper_class.object_name(sphere_common_name, geo_name=True)
                    cmds.parentConstraint(self.another_sphere_list[a], new_grp_name, mo=True)

                    # make a grp
                    self.finger_grp_name = 'Finger_Grp'
                    if cmds.objExists(self.finger_grp_name):
                        cmds.select(new_grp_name, self.finger_grp_name)
                        cmds.parent()
                    else:
                        cmds.select(new_grp_name)
                        cmds.group(n=self.finger_grp_name)

                b += 1

            # create a cylinder
            b = 0
            while b < 6:
                sphere_common_name = self.prefix_name + "_" + self.wing_side + "_Wing_Feather_" + self.type + '_' + name + '_' + str(
                    a + 1) + '_' + str(b + 1) + '_Tem_' + str(self.val)
                previous_sphere_common = self.prefix_name + "_" + self.wing_side + "_Wing_Feather_" + self.type + '_' + name + '_' + str(
                    a + 1) + '_' + str(b) + '_Tem_' + str(self.val)
                if b == 0:
                    # sphere_common_name = self.another_sphere_list[a] + '_Feather_' + name + '_' + str(a+1) + '_' + str(b+1)
                    # base to upper
                    self.base_to_upper_cyliner_common_middle = 'Feather_' + name + '_' + str(
                        a + 1) + '_to_Feather_' + str(b + 1)
                    self.cylinder_rotate = [90, 0, 0]
                    self.first_sphere_name = self.another_sphere_list[a]
                    self.secound_sphere_name = self.helper_class.object_name(sphere_common_name, geo_name=True)
                    self.cylinder_basic_def(self.base_to_upper_cyliner_common_middle,
                                            self.cylinder_rotate,
                                            self.secound_sphere_name,
                                            self.first_sphere_name)
                    self.inner_ctrl_name = self.helper_class.object_name(sphere_common_name, ctrl_inner_name=True)
                    cmds.parentConstraint(self.another_sphere_list[a], self.upper_cluster_handle, mo=False)
                    cmds.parentConstraint(self.inner_ctrl_name, self.lower_cluster_handle, mo=False)
                else:
                    self.base_to_upper_cyliner_common_middle = 'Feather_' + name + '_' + str(
                        a + 1) + '_to_Feather_' + str(b + 1)
                    self.cylinder_rotate = [90, 0, 0]
                    # Template_L_Leg_Upper_0_Tem_1_Geo_Feather_1_1_CluHandle
                    self.first_sphere_name = self.helper_class.object_name(previous_sphere_common, geo_name=True)
                    self.secound_sphere_name = self.helper_class.object_name(sphere_common_name, geo_name=True)
                    self.cylinder_basic_def(self.base_to_upper_cyliner_common_middle,
                                            self.cylinder_rotate,
                                            self.secound_sphere_name,
                                            self.first_sphere_name)

                b += 1

            cmds.select(loc_name)
            cmds.delete()

            a += 1

        a = 0
        while a < len(self.another_sphere_list):
            b = 0
            while b < 6:
                # create a indivial parent
                self.base_to_upper_cyliner_common_middle = 'Feather_' + name + '_' + str(a + 1) + '_to_Feather_' + str(
                    b + 1)
                self.previous_base_to_upper_cyliner_common_middle = 'Feather_' + name + '_' + str(
                    a + 1) + '_to_Feather_' + str(b + 2)
                self.lower_clu_handle_name = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_" + self.base_to_upper_cyliner_common_middle + "_Lower_Tem_" + str(
                    self.val) + '_CluHandle'
                self.upper_clu_handle_name = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_" + self.base_to_upper_cyliner_common_middle + "_Upper_Tem_" + str(
                    self.val) + '_CluHandle'

                self.previous_lower_clu_handle_name = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_" + self.previous_base_to_upper_cyliner_common_middle + "_Lower_Tem_" + str(
                    self.val) + '_CluHandle'
                self.previous_upper_clu_handle_name = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_" + self.previous_base_to_upper_cyliner_common_middle + "_Upper_Tem_" + str(
                    self.val) + '_CluHandle'

                self.sphere_common_name = self.prefix_name + "_" + self.wing_side + "_Wing_Feather_" + self.type + '_' + name + '_' + str(
                    a + 1) + '_' + str(b + 1) + '_Tem_' + str(self.val)
                self.previous_common_name = self.prefix_name + "_" + self.wing_side + "_Wing_Feather_" + self.type + '_' + name + '_' + str(
                    a + 1) + '_' + str(b) + '_Tem_' + str(self.val)
                self.ctrl_name = self.sphere_common_name + '_Outer_Ctrl'
                self.previous_ctrl_name = self.previous_common_name + '_Outer_Ctrl'

                if b == 0:

                    cmds.parentConstraint(self.ctrl_name, self.lower_clu_handle_name, mo=False)
                    cmds.parentConstraint(self.ctrl_name, self.previous_upper_clu_handle_name, mo=False)
                else:

                    # create a indivial parent
                    cmds.select(self.ctrl_name, self.previous_ctrl_name)
                    cmds.parent()
                    cmds.parentConstraint(self.ctrl_name, self.lower_clu_handle_name, mo=False)
                    if cmds.objExists(self.previous_upper_clu_handle_name):
                        cmds.parentConstraint(self.ctrl_name, self.previous_upper_clu_handle_name, mo=False)

                b += 1
            a += 1

    def wing_sphere_name(self):
        # create a sphere on each position
        self.sphere_list = []
        self.cluster_list = []
        self.cylinder_list = []
        self.ctrl_list = []
        self.crv_list = []

        # Base
        self.base_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Base_Tem_" + str(self.val)
        self.sphere_basic_def(self.base_common,
                              self.wing_base_pos)

        # SHOULDER
        self.shoulder_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Shoulder_Tem_" + str(
            self.val)
        self.sphere_basic_def(self.shoulder_common,
                              self.wing_shoulder_pos)

        # UPPER WING
        self.upper_wing_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Upper_Tem_" + str(
            self.val)
        self.sphere_basic_def(self.upper_wing_common,
                              self.wing_upper_pos)

        # lBow
        self.wing_lbow_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_lBow_Tem_" + str(
            self.val)
        self.sphere_basic_def(self.wing_lbow_common,
                              self.wing_lbow_pos)

        # WING HAND
        self.wing_hand_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Hand_Tem_" + str(
            self.val)
        self.sphere_basic_def(self.wing_hand_common,
                              self.wing_hand_pos)

        # WING HAND 2
        self.wing_hand_2_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Hand_2_Tem_" + str(
            self.val)
        self.sphere_basic_def(self.wing_hand_2_common,
                              self.wing_hand_2_pos)

        # WING BRAMCH 1 1
        self.wing_branch_1_1_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_1_1_Tem_" + str(
            self.val)
        self.sphere_basic_def(self.wing_branch_1_1_common,
                              self.wing_branch_1_1_pos)

        # WING BRAMCH 1 2
        self.wing_branch_1_2_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_1_2_Tem_" + str(
            self.val)
        self.sphere_basic_def(self.wing_branch_1_2_common,
                              self.wing_branch_1_2_pos)

        # WING BRAMCH 1 3
        self.wing_branch_1_3_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_1_3_Tem_" + str(
            self.val)
        self.sphere_basic_def(self.wing_branch_1_3_common,
                              self.wing_branch_1_3_pos)

        # WING BRAMCH 1 4
        self.wing_branch_1_4_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_1_4_Tem_" + str(
            self.val)
        self.sphere_basic_def(self.wing_branch_1_4_common,
                              self.wing_branch_1_4_pos)

        # WING BRAMCH 2 1
        self.wing_branch_2_1_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_2_1_Tem_" + str(
            self.val)
        self.sphere_basic_def(self.wing_branch_2_1_common,
                              self.wing_branch_2_1_pos)

        # WING BRAMCH 2 2
        self.wing_branch_2_2_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_2_2_Tem_" + str(
            self.val)
        self.sphere_basic_def(self.wing_branch_2_2_common,
                              self.wing_branch_2_2_pos)

        # WING BRAMCH 2 3
        self.wing_branch_2_3_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_2_3_Tem_" + str(
            self.val)
        self.sphere_basic_def(self.wing_branch_2_3_common,
                              self.wing_branch_2_3_pos)

        # WING BRAMCH 2 4
        self.wing_branch_2_4_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_2_4_Tem_" + str(
            self.val)
        self.sphere_basic_def(self.wing_branch_2_4_common,
                              self.wing_branch_2_4_pos)

        # WING BRAMCH 3 1
        self.wing_branch_3_1_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_3_1_Tem_" + str(
            self.val)
        self.sphere_basic_def(self.wing_branch_3_1_common,
                              self.wing_branch_3_1_pos)

        # WING BRAMCH 3 2
        self.wing_branch_3_2_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_3_2_Tem_" + str(
            self.val)
        self.sphere_basic_def(self.wing_branch_3_2_common,
                              self.wing_branch_3_2_pos)

        # WING BRAMCH 3 3
        self.wing_branch_3_3_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_3_3_Tem_" + str(
            self.val)
        self.sphere_basic_def(self.wing_branch_3_3_common,
                              self.wing_branch_3_3_pos)

        # WING BRAMCH 3 4
        self.wing_branch_3_4_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_3_4_Tem_" + str(
            self.val)
        self.sphere_basic_def(self.wing_branch_3_4_common,
                              self.wing_branch_3_4_pos)

        # WING BRAMCH 4 1
        self.wing_branch_4_1_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_4_1_Tem_" + str(
            self.val)
        self.sphere_basic_def(self.wing_branch_4_1_common,
                              self.wing_branch_4_1_pos)

        # WING BRAMCH 4 2
        self.wing_branch_4_2_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_4_2_Tem_" + str(
            self.val)
        self.sphere_basic_def(self.wing_branch_4_2_common,
                              self.wing_branch_4_2_pos)

        # WING BRAMCH 4 4
        self.wing_branch_4_3_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_4_3_Tem_" + str(
            self.val)
        self.sphere_basic_def(self.wing_branch_4_3_common,
                              self.wing_branch_4_3_pos)

        # WING BRAMCH 4 4
        self.wing_branch_4_4_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_4_4_Tem_" + str(
            self.val)
        self.sphere_basic_def(self.wing_branch_4_4_common,
                              self.wing_branch_4_4_pos)

    def sphere_basic_def(self, common_name, pos):
        self.wing_hand_2_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Hand_2_Tem_" + str(
            self.val)
        self.wing_hand_2_sphere_name = common_name + "_Geo"
        self.wing_hand_2_sphere_clu_name = common_name + '_Clu'
        self.wing_hand_2_sphere_clu_handle_name = self.wing_hand_2_sphere_clu_name + 'Handle'
        self.sphere_list.append(self.wing_hand_2_sphere_name)
        self.cluster_list.append(self.wing_hand_2_sphere_clu_handle_name)
        self.helper_class.set_sphere_position(self.wing_hand_2_sphere_name,
                                              pos, self.wing_hand_2_sphere_clu_name)

    def wing_cylinder_def(self):
        # base to shoulder
        self.base_to_shoulder_cyliner_common_middle = 'Base_to_Shoulder'
        self.cylinder_rotate = [0, 0, 90]
        self.first_sphere_name = self.helper_class.object_name(self.base_common, geo_name=True)
        self.secound_sphere_name = self.helper_class.object_name(self.shoulder_common, geo_name=True)
        self.cylinder_basic_def(self.base_to_shoulder_cyliner_common_middle,
                                self.cylinder_rotate,
                                self.secound_sphere_name,
                                self.first_sphere_name)

        # shoulder to uppper wing
        self.shoulder_to_upper_common_middle = 'Shoulder_to_Upper'
        self.cylinder_rotate = [0, 0, 90]
        self.first_sphere_name = self.helper_class.object_name(self.shoulder_common, geo_name=True)
        self.secound_sphere_name = self.helper_class.object_name(self.upper_wing_common, geo_name=True)
        self.cylinder_basic_def(self.shoulder_to_upper_common_middle,
                                self.cylinder_rotate,
                                self.secound_sphere_name,
                                self.first_sphere_name)

        # upper wing to lbow
        self.upper_to_lbow_common_middle = 'Upper_to_lBow'
        self.cylinder_rotate = [0, 0, 90]
        self.first_sphere_name = self.helper_class.object_name(self.upper_wing_common, geo_name=True)
        self.secound_sphere_name = self.helper_class.object_name(self.wing_lbow_common, geo_name=True)
        self.cylinder_basic_def(self.upper_to_lbow_common_middle,
                                self.cylinder_rotate,
                                self.secound_sphere_name,
                                self.first_sphere_name)

        # upper wing to lbow
        self.lbow_to_hand_common_middle = 'lBow_to_Hand'
        self.cylinder_rotate = [0, 0, 90]
        self.first_sphere_name = self.helper_class.object_name(self.wing_lbow_common, geo_name=True)
        self.secound_sphere_name = self.helper_class.object_name(self.wing_hand_common, geo_name=True)
        self.cylinder_basic_def(self.lbow_to_hand_common_middle,
                                self.cylinder_rotate,
                                self.secound_sphere_name,
                                self.first_sphere_name)

        # upper wing to lbow
        self.hand_to_hand_2_common_middle = 'Hand_to_Hand_2'
        self.cylinder_rotate = [0, 0, 90]
        self.first_sphere_name = self.helper_class.object_name(self.wing_hand_common, geo_name=True)
        self.secound_sphere_name = self.helper_class.object_name(self.wing_hand_2_common, geo_name=True)
        self.cylinder_basic_def(self.hand_to_hand_2_common_middle,
                                self.cylinder_rotate,
                                self.secound_sphere_name,
                                self.first_sphere_name)

        # hand 2 to branch 1 1
        self.hand_2_to_branch_1_1_common_middle = 'Hand_2_to_Branch_1_1'
        self.cylinder_rotate = [0, 0, 90]
        self.first_sphere_name = self.helper_class.object_name(self.wing_hand_2_common, geo_name=True)
        self.secound_sphere_name = self.helper_class.object_name(self.wing_branch_1_1_common, geo_name=True)
        self.cylinder_basic_def(self.hand_2_to_branch_1_1_common_middle,
                                self.cylinder_rotate,
                                self.secound_sphere_name,
                                self.first_sphere_name)

        # branch 1 1 to branch 1 2
        self.branch_1_1_to_branch_1_2_common_middle = 'Branch_1_1_to_Branch_1_2'
        self.cylinder_rotate = [0, 0, 90]
        self.first_sphere_name = self.helper_class.object_name(self.wing_branch_1_1_common, geo_name=True)
        self.secound_sphere_name = self.helper_class.object_name(self.wing_branch_1_2_common, geo_name=True)
        self.cylinder_basic_def(self.branch_1_1_to_branch_1_2_common_middle,
                                self.cylinder_rotate,
                                self.secound_sphere_name,
                                self.first_sphere_name)

        # branch 1 2 to branch 1 3
        self.branch_1_2_to_branch_1_3_common_middle = 'Branch_1_2_to_Branch_1_3'
        self.cylinder_rotate = [0, 0, 90]
        self.first_sphere_name = self.helper_class.object_name(self.wing_branch_1_2_common, geo_name=True)
        self.secound_sphere_name = self.helper_class.object_name(self.wing_branch_1_3_common, geo_name=True)
        self.cylinder_basic_def(self.branch_1_2_to_branch_1_3_common_middle,
                                self.cylinder_rotate,
                                self.secound_sphere_name,
                                self.first_sphere_name)

        # branch 1 3 to branch 1 4
        self.branch_1_3_to_branch_1_4_common_middle = 'Branch_1_3_to_Branch_1_4'
        self.cylinder_rotate = [0, 0, 90]
        self.first_sphere_name = self.helper_class.object_name(self.wing_branch_1_3_common, geo_name=True)
        self.secound_sphere_name = self.helper_class.object_name(self.wing_branch_1_4_common, geo_name=True)
        self.cylinder_basic_def(self.branch_1_3_to_branch_1_4_common_middle,
                                self.cylinder_rotate,
                                self.secound_sphere_name,
                                self.first_sphere_name)

        # hand 2 to branch 2 1
        self.hand_2_to_branch_2_1_common_middle = 'Hand_2_to_Branch_2_1'
        self.cylinder_rotate = [90, 0, 0]
        self.first_sphere_name = self.helper_class.object_name(self.wing_hand_2_common, geo_name=True)
        self.secound_sphere_name = self.helper_class.object_name(self.wing_branch_2_1_common, geo_name=True)
        self.cylinder_basic_def(self.hand_2_to_branch_2_1_common_middle,
                                self.cylinder_rotate,
                                self.secound_sphere_name,
                                self.first_sphere_name)

        # branch 2 1 to branch 2 2
        self.branch_2_1_to_branch_2_2_common_middle = 'Branch_2_1_to_Branch_2_2'
        self.cylinder_rotate = [90, 0, 0]
        self.first_sphere_name = self.helper_class.object_name(self.wing_branch_2_1_common, geo_name=True)
        self.secound_sphere_name = self.helper_class.object_name(self.wing_branch_2_2_common, geo_name=True)
        self.cylinder_basic_def(self.branch_2_1_to_branch_2_2_common_middle,
                                self.cylinder_rotate,
                                self.secound_sphere_name,
                                self.first_sphere_name)

        # branch 2 2 to branch 2 3
        self.branch_2_2_to_branch_2_3_common_middle = 'Branch_2_2_to_Branch_2_3'
        self.cylinder_rotate = [90, 0, 0]
        self.first_sphere_name = self.helper_class.object_name(self.wing_branch_2_2_common, geo_name=True)
        self.secound_sphere_name = self.helper_class.object_name(self.wing_branch_2_3_common, geo_name=True)
        self.cylinder_basic_def(self.branch_2_2_to_branch_2_3_common_middle,
                                self.cylinder_rotate,
                                self.secound_sphere_name,
                                self.first_sphere_name)

        # branch 2 3 to branch 2 4
        self.branch_2_3_to_branch_2_4_common_middle = 'Branch_2_3_to_Branch_2_4'
        self.cylinder_rotate = [90, 0, 0]
        self.first_sphere_name = self.helper_class.object_name(self.wing_branch_2_3_common, geo_name=True)
        self.secound_sphere_name = self.helper_class.object_name(self.wing_branch_2_4_common, geo_name=True)
        self.cylinder_basic_def(self.branch_2_3_to_branch_2_4_common_middle,
                                self.cylinder_rotate,
                                self.secound_sphere_name,
                                self.first_sphere_name)

        # hand 2 to branch 3 1
        self.hand_2_to_branch_3_1_common_middle = 'Hand_2_to_Branch_3_1'
        self.cylinder_rotate = [90, 0, 0]
        self.first_sphere_name = self.helper_class.object_name(self.wing_hand_2_common, geo_name=True)
        self.secound_sphere_name = self.helper_class.object_name(self.wing_branch_3_1_common, geo_name=True)
        self.cylinder_basic_def(self.hand_2_to_branch_3_1_common_middle,
                                self.cylinder_rotate,
                                self.secound_sphere_name,
                                self.first_sphere_name)

        # branch 3 1 to branch 3 2
        self.branch_3_1_to_branch_3_2_common_middle = 'Branch_3_1_to_Branch_3_2'
        self.cylinder_rotate = [90, 0, 0]
        self.first_sphere_name = self.helper_class.object_name(self.wing_branch_3_1_common, geo_name=True)
        self.secound_sphere_name = self.helper_class.object_name(self.wing_branch_3_2_common, geo_name=True)
        self.cylinder_basic_def(self.branch_3_1_to_branch_3_2_common_middle,
                                self.cylinder_rotate,
                                self.secound_sphere_name,
                                self.first_sphere_name)

        # branch 3 2 to branch 3 3
        self.branch_3_2_to_branch_3_3_common_middle = 'Branch_3_2_to_Branch_3_3'
        self.cylinder_rotate = [90, 0, 0]
        self.first_sphere_name = self.helper_class.object_name(self.wing_branch_3_2_common, geo_name=True)
        self.secound_sphere_name = self.helper_class.object_name(self.wing_branch_3_3_common, geo_name=True)
        self.cylinder_basic_def(self.branch_3_2_to_branch_3_3_common_middle,
                                self.cylinder_rotate,
                                self.secound_sphere_name,
                                self.first_sphere_name)

        # branch 3 3 to branch 3 4
        self.branch_3_3_to_branch_3_4_common_middle = 'Branch_3_3_to_Branch_3_4'
        self.cylinder_rotate = [90, 0, 0]
        self.first_sphere_name = self.helper_class.object_name(self.wing_branch_3_3_common, geo_name=True)
        self.secound_sphere_name = self.helper_class.object_name(self.wing_branch_3_4_common, geo_name=True)
        self.cylinder_basic_def(self.branch_3_3_to_branch_3_4_common_middle,
                                self.cylinder_rotate,
                                self.secound_sphere_name,
                                self.first_sphere_name)

        # hand 2 to branch 4 1
        self.lbow_to_branch_4_1_common_middle = 'lBow_to_Branch_4_1'
        self.cylinder_rotate = [90, 0, 0]
        self.first_sphere_name = self.helper_class.object_name(self.wing_lbow_common, geo_name=True)
        self.secound_sphere_name = self.helper_class.object_name(self.wing_branch_4_1_common, geo_name=True)
        self.cylinder_basic_def(self.lbow_to_branch_4_1_common_middle,
                                self.cylinder_rotate,
                                self.secound_sphere_name,
                                self.first_sphere_name)

        # branch 4 1 to branch 4 2
        self.branch_4_1_to_branch_4_2_common_middle = 'Branch_4_1_to_Branch_4_2'
        self.cylinder_rotate = [90, 0, 0]
        self.first_sphere_name = self.helper_class.object_name(self.wing_branch_4_1_common, geo_name=True)
        self.secound_sphere_name = self.helper_class.object_name(self.wing_branch_4_2_common, geo_name=True)
        self.cylinder_basic_def(self.branch_4_1_to_branch_4_2_common_middle,
                                self.cylinder_rotate,
                                self.secound_sphere_name,
                                self.first_sphere_name)

        # branch 4 2 to branch 4 3
        self.branch_4_2_to_branch_4_3_common_middle = 'Branch_4_2_to_Branch_4_3'
        self.cylinder_rotate = [90, 0, 0]
        self.first_sphere_name = self.helper_class.object_name(self.wing_branch_4_2_common, geo_name=True)
        self.secound_sphere_name = self.helper_class.object_name(self.wing_branch_4_3_common, geo_name=True)
        self.cylinder_basic_def(self.branch_4_2_to_branch_4_3_common_middle,
                                self.cylinder_rotate,
                                self.secound_sphere_name,
                                self.first_sphere_name)

        # branch 4 3 to branch 4 4
        self.branch_4_3_to_branch_4_4_common_middle = 'Branch_4_3_to_Branch_4_4'
        self.cylinder_rotate = [90, 0, 0]
        self.first_sphere_name = self.helper_class.object_name(self.wing_branch_4_3_common, geo_name=True)
        self.secound_sphere_name = self.helper_class.object_name(self.wing_branch_4_4_common, geo_name=True)
        self.cylinder_basic_def(self.branch_4_3_to_branch_4_4_common_middle,
                                self.cylinder_rotate,
                                self.secound_sphere_name,
                                self.first_sphere_name)

    def cylinder_basic_def(self, common_middle,
                           rotate,
                           first_sphere_name,
                           secound_sphere_name):
        self.common_name = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_" + common_middle + "_Tem_" + str(
            self.val)
        self.cylinder_name = self.common_name + '_Geo'
        self.cylinder_lower_cylinder_cluster_name = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_" + common_middle + "_Lower_Tem_" + str(
            self.val) + '_Clu'
        self.cylinder_lower_cylinder_cluster_handle_name = self.cylinder_lower_cylinder_cluster_name + 'Handle'
        self.cylinder_upper_cylinder_cluster_name = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_" + common_middle + "_Upper_Tem_" + str(
            self.val) + '_Clu'
        self.cylinder_upper_cylinder_cluster_handle_name = self.cylinder_upper_cylinder_cluster_name + 'Handle'
        self.cylinder_rotate = rotate
        self.cluster_list.append(self.cylinder_lower_cylinder_cluster_handle_name)
        self.cluster_list.append(self.cylinder_upper_cylinder_cluster_handle_name)
        self.cylinder_list.append(self.cylinder_name)
        self.helper_class.set_cylinder_position(self.cylinder_name,
                                                self.cylinder_lower_cylinder_cluster_name,
                                                self.cylinder_upper_cylinder_cluster_name,
                                                first_sphere_name,
                                                secound_sphere_name,
                                                rotate_val=[self.cylinder_rotate[0],
                                                            self.cylinder_rotate[1],
                                                            self.cylinder_rotate[2]])

        self.lower_cluster_handle = self.cylinder_lower_cylinder_cluster_handle_name
        self.upper_cluster_handle = self.cylinder_upper_cylinder_cluster_handle_name

    def controller_def(self):
        # CREATE CONTROLLER
        self.ctrl_lower_size = [0.5, 0.5, 0.5]
        self.ctrl_outer_size = [1.5, 1.5, 1.5]
        self.ctrl_rotate = [0, 0, 90]
        self.base_ctrl_freez_trans = True
        self.base_ctrl_freez_rotate = True
        self.base_ctrl_freez_scale = True

        # BASE CONTROLLER
        self.sphere_handle_name = self.helper_class.object_name(self.base_common, cluster_name=True) + 'Handle'
        self.cylinder_upper_handle_name = self.get_cyliner_clu_name('Upper',
                                                                    self.base_to_shoulder_cyliner_common_middle) + 'Handle'
        self.base_parent_const_list = [self.sphere_handle_name,
                                       self.cylinder_upper_handle_name]
        self.controller_small_big(base_name=self.base_common,
                                  parent_list=self.base_parent_const_list,
                                  pos=self.wing_base_pos)
        self.base_inner_ctrl = self.base_common + '_Inner_Ctrl'
        self.base_outer_ctrl = self.base_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.base_inner_ctrl)
        self.ctrl_list.append(self.base_outer_ctrl)

        # SHOULDER CONTROLLER
        self.sphere_handle_name = self.helper_class.object_name(self.shoulder_common, cluster_name=True) + 'Handle'
        self.cylinder_upper_handle_name = self.get_cyliner_clu_name('Lower',
                                                                    self.base_to_shoulder_cyliner_common_middle) + 'Handle'
        self.cylinder_lower_handle_name = self.get_cyliner_clu_name('Upper',
                                                                    self.shoulder_to_upper_common_middle) + 'Handle'
        self.base_parent_const_list = [self.sphere_handle_name,
                                       self.cylinder_upper_handle_name,
                                       self.cylinder_lower_handle_name]
        self.controller_small_big(base_name=self.shoulder_common,
                                  parent_list=self.base_parent_const_list,
                                  pos=self.wing_shoulder_pos)
        self.shoulder_inner_ctrl = self.shoulder_common + '_Inner_Ctrl'
        self.shoulder_outer_ctrl = self.shoulder_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.shoulder_inner_ctrl)
        self.ctrl_list.append(self.shoulder_outer_ctrl)

        # UPPER WING CONTROLLER
        self.sphere_handle_name = self.helper_class.object_name(self.upper_wing_common, cluster_name=True) + 'Handle'
        self.cylinder_upper_handle_name = self.get_cyliner_clu_name('Lower',
                                                                    self.shoulder_to_upper_common_middle) + 'Handle'
        self.cylinder_lower_handle_name = self.get_cyliner_clu_name('Upper',
                                                                    self.upper_to_lbow_common_middle) + 'Handle'
        self.base_parent_const_list = [self.sphere_handle_name,
                                       self.cylinder_upper_handle_name,
                                       self.cylinder_lower_handle_name]
        self.controller_small_big(base_name=self.upper_wing_common,
                                  parent_list=self.base_parent_const_list,
                                  pos=self.wing_upper_pos)
        self.upper_wing_outer_ctrl = self.helper_class.object_name(self.upper_wing_common,
                                                                   ctrl_outer_name=True)
        self.upper_wing_inner_ctrl = self.upper_wing_common + '_Inner_Ctrl'
        self.upper_wing_outer_ctrl = self.upper_wing_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.upper_wing_inner_ctrl)
        self.ctrl_list.append(self.upper_wing_outer_ctrl)

        # LBOW CONTROLLER
        self.sphere_handle_name = self.helper_class.object_name(self.wing_lbow_common, cluster_name=True) + 'Handle'
        self.cylinder_upper_handle_name = self.get_cyliner_clu_name('Lower',
                                                                    self.upper_to_lbow_common_middle) + 'Handle'
        self.cylinder_lower_handle_name = self.get_cyliner_clu_name('Upper', self.lbow_to_hand_common_middle) + 'Handle'
        self.cylinder_lower_handle_1_name = self.get_cyliner_clu_name('Upper',
                                                                      self.lbow_to_branch_4_1_common_middle) + 'Handle'
        self.base_parent_const_list = [self.sphere_handle_name,
                                       self.cylinder_upper_handle_name,
                                       self.cylinder_lower_handle_name,
                                       self.cylinder_lower_handle_1_name]
        self.controller_small_big(base_name=self.wing_lbow_common,
                                  parent_list=self.base_parent_const_list,
                                  pos=self.wing_lbow_pos)
        self.lbow_outer_ctrl = self.helper_class.object_name(self.wing_lbow_common,
                                                             ctrl_outer_name=True)
        self.lbow_inner_ctrl = self.wing_lbow_common + '_Inner_Ctrl'
        self.lbow_outer_ctrl = self.wing_lbow_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.lbow_inner_ctrl)
        self.ctrl_list.append(self.lbow_outer_ctrl)

        # HAND CONTROLLER
        self.sphere_handle_name = self.helper_class.object_name(self.wing_hand_common, cluster_name=True) + 'Handle'
        self.cylinder_upper_handle_name = self.get_cyliner_clu_name('Lower', self.lbow_to_hand_common_middle) + 'Handle'
        self.cylinder_lower_handle_name = self.get_cyliner_clu_name('Upper',
                                                                    self.hand_to_hand_2_common_middle) + 'Handle'
        self.base_parent_const_list = [self.sphere_handle_name,
                                       self.cylinder_upper_handle_name,
                                       self.cylinder_lower_handle_name]
        self.controller_small_big(base_name=self.wing_hand_common,
                                  parent_list=self.base_parent_const_list,
                                  pos=self.wing_hand_pos)
        self.hand_outer_ctrl = self.helper_class.object_name(self.wing_hand_common,
                                                             ctrl_outer_name=True)
        self.hand_inner_ctrl = self.wing_hand_common + '_Inner_Ctrl'
        self.hand_outer_ctrl = self.wing_hand_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.hand_inner_ctrl)
        self.ctrl_list.append(self.hand_outer_ctrl)

        # HAND 2 CONTROLLER
        self.sphere_handle_name = self.helper_class.object_name(self.wing_hand_2_common, cluster_name=True) + 'Handle'
        self.cylinder_upper_handle_name = self.get_cyliner_clu_name('Lower',
                                                                    self.hand_to_hand_2_common_middle) + 'Handle'
        self.cylinder_lower_handle_name = self.get_cyliner_clu_name('Upper',
                                                                    self.hand_2_to_branch_1_1_common_middle) + 'Handle'
        self.cylinder_lower_handle_1_name = self.get_cyliner_clu_name('Upper',
                                                                      self.hand_2_to_branch_2_1_common_middle) + 'Handle'
        self.cylinder_lower_handle_2_name = self.get_cyliner_clu_name('Upper',
                                                                      self.hand_2_to_branch_3_1_common_middle) + 'Handle'
        self.base_parent_const_list = [self.sphere_handle_name,
                                       self.cylinder_upper_handle_name,
                                       self.cylinder_lower_handle_name,
                                       self.cylinder_lower_handle_1_name,
                                       self.cylinder_lower_handle_2_name]
        self.controller_small_big(base_name=self.wing_hand_2_common,
                                  parent_list=self.base_parent_const_list,
                                  pos=self.wing_hand_2_pos)
        self.hand_2_outer_ctrl = self.helper_class.object_name(self.wing_hand_2_common,
                                                               ctrl_outer_name=True)
        self.hand_2_inner_ctrl = self.wing_hand_2_common + '_Inner_Ctrl'
        self.hand_2_outer_ctrl = self.wing_hand_2_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.hand_2_inner_ctrl)
        self.ctrl_list.append(self.hand_2_outer_ctrl)

        # BRANCH 1 1  CONTROLLER
        self.sphere_handle_name = self.helper_class.object_name(self.wing_branch_1_1_common,
                                                                cluster_name=True) + 'Handle'
        self.cylinder_upper_handle_name = self.get_cyliner_clu_name('Lower',
                                                                    self.hand_2_to_branch_1_1_common_middle) + 'Handle'
        self.cylinder_lower_handle_name = self.get_cyliner_clu_name('Upper',
                                                                    self.branch_1_1_to_branch_1_2_common_middle) + 'Handle'
        self.base_parent_const_list = [self.sphere_handle_name,
                                       self.cylinder_upper_handle_name,
                                       self.cylinder_lower_handle_name]
        self.controller_small_big(base_name=self.wing_branch_1_1_common,
                                  parent_list=self.base_parent_const_list,
                                  pos=self.wing_branch_1_1_pos)
        self.branch_1_1_inner_ctrl = self.wing_branch_1_1_common + '_Inner_Ctrl'
        self.branch_1_1_outer_ctrl = self.wing_branch_1_1_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.branch_1_1_inner_ctrl)
        self.ctrl_list.append(self.branch_1_1_outer_ctrl)

        # BRANCH 1 2  CONTROLLER
        self.sphere_handle_name = self.helper_class.object_name(self.wing_branch_1_2_common,
                                                                cluster_name=True) + 'Handle'
        self.cylinder_upper_handle_name = self.get_cyliner_clu_name('Lower',
                                                                    self.branch_1_1_to_branch_1_2_common_middle) + 'Handle'
        self.cylinder_lower_handle_name = self.get_cyliner_clu_name('Upper',
                                                                    self.branch_1_2_to_branch_1_3_common_middle) + 'Handle'
        self.base_parent_const_list = [self.sphere_handle_name,
                                       self.cylinder_upper_handle_name,
                                       self.cylinder_lower_handle_name]
        self.controller_small_big(base_name=self.wing_branch_1_2_common,
                                  parent_list=self.base_parent_const_list,
                                  pos=self.wing_branch_1_2_pos)
        self.branch_1_2_inner_ctrl = self.wing_branch_1_2_common + '_Inner_Ctrl'
        self.branch_1_2_outer_ctrl = self.wing_branch_1_2_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.branch_1_2_inner_ctrl)
        self.ctrl_list.append(self.branch_1_2_outer_ctrl)

        # BRANCH 1 3  CONTROLLER
        self.sphere_handle_name = self.helper_class.object_name(self.wing_branch_1_3_common,
                                                                cluster_name=True) + 'Handle'
        self.cylinder_upper_handle_name = self.get_cyliner_clu_name('Lower',
                                                                    self.branch_1_2_to_branch_1_3_common_middle) + 'Handle'
        self.cylinder_lower_handle_name = self.get_cyliner_clu_name('Upper',
                                                                    self.branch_1_3_to_branch_1_4_common_middle) + 'Handle'
        self.base_parent_const_list = [self.sphere_handle_name,
                                       self.cylinder_upper_handle_name,
                                       self.cylinder_lower_handle_name]
        self.controller_small_big(base_name=self.wing_branch_1_3_common,
                                  parent_list=self.base_parent_const_list,
                                  pos=self.wing_branch_1_3_pos)
        self.branch_1_3_inner_ctrl = self.wing_branch_1_3_common + '_Inner_Ctrl'
        self.branch_1_3_outer_ctrl = self.wing_branch_1_3_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.branch_1_3_inner_ctrl)
        self.ctrl_list.append(self.branch_1_3_outer_ctrl)

        # BRANCH 1 4  CONTROLLER
        self.sphere_handle_name = self.helper_class.object_name(self.wing_branch_1_4_common,
                                                                cluster_name=True) + 'Handle'
        self.cylinder_upper_handle_name = self.get_cyliner_clu_name('Lower',
                                                                    self.branch_1_3_to_branch_1_4_common_middle) + 'Handle'
        self.base_parent_const_list = [self.sphere_handle_name,
                                       self.cylinder_upper_handle_name]
        self.controller_small_big(base_name=self.wing_branch_1_4_common,
                                  parent_list=self.base_parent_const_list,
                                  pos=self.wing_branch_1_4_pos)
        self.branch_1_4_inner_ctrl = self.wing_branch_1_4_common + '_Inner_Ctrl'
        self.branch_1_4_outer_ctrl = self.wing_branch_1_4_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.branch_1_4_inner_ctrl)
        self.ctrl_list.append(self.branch_1_4_outer_ctrl)

        # BRANCH 2 1  CONTROLLER
        self.sphere_handle_name = self.helper_class.object_name(self.wing_branch_2_1_common,
                                                                cluster_name=True) + 'Handle'
        self.cylinder_upper_handle_name = self.get_cyliner_clu_name('Lower',
                                                                    self.hand_2_to_branch_2_1_common_middle) + 'Handle'
        self.cylinder_lower_handle_name = self.get_cyliner_clu_name('Upper',
                                                                    self.branch_2_1_to_branch_2_2_common_middle) + 'Handle'
        self.base_parent_const_list = [self.sphere_handle_name,
                                       self.cylinder_upper_handle_name,
                                       self.cylinder_lower_handle_name]
        self.controller_small_big(base_name=self.wing_branch_2_1_common,
                                  parent_list=self.base_parent_const_list,
                                  pos=self.wing_branch_2_1_pos,
                                  ctrl_rotate=[90, 0, 0])
        self.branch_2_1_inner_ctrl = self.wing_branch_2_1_common + '_Inner_Ctrl'
        self.branch_2_1_outer_ctrl = self.wing_branch_2_1_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.branch_2_1_inner_ctrl)
        self.ctrl_list.append(self.branch_2_1_outer_ctrl)

        # BRANCH 2 2  CONTROLLER
        self.sphere_handle_name = self.helper_class.object_name(self.wing_branch_2_2_common,
                                                                cluster_name=True) + 'Handle'
        self.cylinder_upper_handle_name = self.get_cyliner_clu_name('Lower',
                                                                    self.branch_2_1_to_branch_2_2_common_middle) + 'Handle'
        self.cylinder_lower_handle_name = self.get_cyliner_clu_name('Upper',
                                                                    self.branch_2_2_to_branch_2_3_common_middle) + 'Handle'
        self.base_parent_const_list = [self.sphere_handle_name,
                                       self.cylinder_upper_handle_name,
                                       self.cylinder_lower_handle_name]
        self.controller_small_big(base_name=self.wing_branch_2_2_common,
                                  parent_list=self.base_parent_const_list,
                                  pos=self.wing_branch_2_2_pos,
                                  ctrl_rotate=[90, 0, 0])
        self.branch_2_2_inner_ctrl = self.wing_branch_2_2_common + '_Inner_Ctrl'
        self.branch_2_2_outer_ctrl = self.wing_branch_2_2_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.branch_2_2_inner_ctrl)
        self.ctrl_list.append(self.branch_2_2_outer_ctrl)

        # BRANCH 2 3  CONTROLLER
        self.sphere_handle_name = self.helper_class.object_name(self.wing_branch_2_3_common,
                                                                cluster_name=True) + 'Handle'
        self.cylinder_upper_handle_name = self.get_cyliner_clu_name('Lower',
                                                                    self.branch_2_2_to_branch_2_3_common_middle) + 'Handle'
        self.cylinder_lower_handle_name = self.get_cyliner_clu_name('Upper',
                                                                    self.branch_2_3_to_branch_2_4_common_middle) + 'Handle'
        self.base_parent_const_list = [self.sphere_handle_name,
                                       self.cylinder_upper_handle_name,
                                       self.cylinder_lower_handle_name]
        self.controller_small_big(base_name=self.wing_branch_2_3_common,
                                  parent_list=self.base_parent_const_list,
                                  pos=self.wing_branch_2_3_pos,
                                  ctrl_rotate=[90, 0, 0])
        self.branch_2_3_inner_ctrl = self.wing_branch_2_3_common + '_Inner_Ctrl'
        self.branch_2_3_outer_ctrl = self.wing_branch_2_3_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.branch_2_3_inner_ctrl)
        self.ctrl_list.append(self.branch_2_3_outer_ctrl)

        # BRANCH 2 4  CONTROLLER
        self.sphere_handle_name = self.helper_class.object_name(self.wing_branch_2_4_common,
                                                                cluster_name=True) + 'Handle'
        self.cylinder_upper_handle_name = self.get_cyliner_clu_name('Lower',
                                                                    self.branch_2_3_to_branch_2_4_common_middle) + 'Handle'
        self.base_parent_const_list = [self.sphere_handle_name,
                                       self.cylinder_upper_handle_name]
        self.controller_small_big(base_name=self.wing_branch_2_4_common,
                                  parent_list=self.base_parent_const_list,
                                  pos=self.wing_branch_2_4_pos,
                                  ctrl_rotate=[90, 0, 0])
        self.branch_2_4_inner_ctrl = self.wing_branch_2_4_common + '_Inner_Ctrl'
        self.branch_2_4_outer_ctrl = self.wing_branch_2_4_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.branch_2_4_inner_ctrl)
        self.ctrl_list.append(self.branch_2_4_outer_ctrl)

        # BRANCH 3 1  CONTROLLER
        self.sphere_handle_name = self.helper_class.object_name(self.wing_branch_3_1_common,
                                                                cluster_name=True) + 'Handle'
        self.cylinder_upper_handle_name = self.get_cyliner_clu_name('Lower',
                                                                    self.hand_2_to_branch_3_1_common_middle) + 'Handle'
        self.cylinder_lower_handle_name = self.get_cyliner_clu_name('Upper',
                                                                    self.branch_3_1_to_branch_3_2_common_middle) + 'Handle'
        self.base_parent_const_list = [self.sphere_handle_name,
                                       self.cylinder_upper_handle_name,
                                       self.cylinder_lower_handle_name]
        self.controller_small_big(base_name=self.wing_branch_3_1_common,
                                  parent_list=self.base_parent_const_list,
                                  pos=self.wing_branch_3_1_pos,
                                  ctrl_rotate=[90, 0, 0])
        self.branch_3_1_inner_ctrl = self.wing_branch_3_1_common + '_Inner_Ctrl'
        self.branch_3_1_outer_ctrl = self.wing_branch_3_1_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.branch_3_1_inner_ctrl)
        self.ctrl_list.append(self.branch_3_1_outer_ctrl)

        # BRANCH 3 2  CONTROLLER
        self.sphere_handle_name = self.helper_class.object_name(self.wing_branch_3_2_common,
                                                                cluster_name=True) + 'Handle'
        self.cylinder_upper_handle_name = self.get_cyliner_clu_name('Lower',
                                                                    self.branch_3_1_to_branch_3_2_common_middle) + 'Handle'
        self.cylinder_lower_handle_name = self.get_cyliner_clu_name('Upper',
                                                                    self.branch_3_2_to_branch_3_3_common_middle) + 'Handle'
        self.base_parent_const_list = [self.sphere_handle_name,
                                       self.cylinder_upper_handle_name,
                                       self.cylinder_lower_handle_name]
        self.controller_small_big(base_name=self.wing_branch_3_2_common,
                                  parent_list=self.base_parent_const_list,
                                  pos=self.wing_branch_3_2_pos,
                                  ctrl_rotate=[90, 0, 0])
        self.branch_3_2_inner_ctrl = self.wing_branch_3_2_common + '_Inner_Ctrl'
        self.branch_3_2_outer_ctrl = self.wing_branch_3_2_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.branch_3_2_inner_ctrl)
        self.ctrl_list.append(self.branch_3_2_outer_ctrl)

        # BRANCH 3 3  CONTROLLER
        self.sphere_handle_name = self.helper_class.object_name(self.wing_branch_3_3_common,
                                                                cluster_name=True) + 'Handle'
        self.cylinder_upper_handle_name = self.get_cyliner_clu_name('Lower',
                                                                    self.branch_3_2_to_branch_3_3_common_middle) + 'Handle'
        self.cylinder_lower_handle_name = self.get_cyliner_clu_name('Upper',
                                                                    self.branch_3_3_to_branch_3_4_common_middle) + 'Handle'
        self.base_parent_const_list = [self.sphere_handle_name,
                                       self.cylinder_upper_handle_name,
                                       self.cylinder_lower_handle_name]
        self.controller_small_big(base_name=self.wing_branch_3_3_common,
                                  parent_list=self.base_parent_const_list,
                                  pos=self.wing_branch_3_3_pos,
                                  ctrl_rotate=[90, 0, 0])
        self.branch_3_3_inner_ctrl = self.wing_branch_3_3_common + '_Inner_Ctrl'
        self.branch_3_3_outer_ctrl = self.wing_branch_3_3_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.branch_3_3_inner_ctrl)
        self.ctrl_list.append(self.branch_3_3_outer_ctrl)

        # BRANCH 3 4  CONTROLLER
        self.sphere_handle_name = self.helper_class.object_name(self.wing_branch_3_4_common,
                                                                cluster_name=True) + 'Handle'
        self.cylinder_upper_handle_name = self.get_cyliner_clu_name('Lower',
                                                                    self.branch_3_3_to_branch_3_4_common_middle) + 'Handle'
        self.base_parent_const_list = [self.sphere_handle_name,
                                       self.cylinder_upper_handle_name]
        self.controller_small_big(base_name=self.wing_branch_3_4_common,
                                  parent_list=self.base_parent_const_list,
                                  pos=self.wing_branch_3_4_pos,
                                  ctrl_rotate=[90, 0, 0])
        self.branch_3_4_inner_ctrl = self.wing_branch_3_4_common + '_Inner_Ctrl'
        self.branch_3_4_outer_ctrl = self.wing_branch_3_4_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.branch_3_4_inner_ctrl)
        self.ctrl_list.append(self.branch_3_4_outer_ctrl)

        # BRANCH 4 1  CONTROLLER
        self.sphere_handle_name = self.helper_class.object_name(self.wing_branch_4_1_common,
                                                                cluster_name=True) + 'Handle'
        self.cylinder_upper_handle_name = self.get_cyliner_clu_name('Lower',
                                                                    self.lbow_to_branch_4_1_common_middle) + 'Handle'
        self.cylinder_lower_handle_name = self.get_cyliner_clu_name('Upper',
                                                                    self.branch_4_1_to_branch_4_2_common_middle) + 'Handle'
        self.base_parent_const_list = [self.sphere_handle_name,
                                       self.cylinder_upper_handle_name,
                                       self.cylinder_lower_handle_name]
        self.controller_small_big(base_name=self.wing_branch_4_1_common,
                                  parent_list=self.base_parent_const_list,
                                  pos=self.wing_branch_4_1_pos,
                                  ctrl_rotate=[90, 0, 0])
        self.branch_4_1_inner_ctrl = self.wing_branch_4_1_common + '_Inner_Ctrl'
        self.branch_4_1_outer_ctrl = self.wing_branch_4_1_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.branch_4_1_inner_ctrl)
        self.ctrl_list.append(self.branch_4_1_outer_ctrl)

        # BRANCH 4 2  CONTROLLER
        self.sphere_handle_name = self.helper_class.object_name(self.wing_branch_4_2_common,
                                                                cluster_name=True) + 'Handle'
        self.cylinder_upper_handle_name = self.get_cyliner_clu_name('Lower',
                                                                    self.branch_4_1_to_branch_4_2_common_middle) + 'Handle'
        self.cylinder_lower_handle_name = self.get_cyliner_clu_name('Upper',
                                                                    self.branch_4_2_to_branch_4_3_common_middle) + 'Handle'
        self.base_parent_const_list = [self.sphere_handle_name,
                                       self.cylinder_upper_handle_name,
                                       self.cylinder_lower_handle_name]
        self.controller_small_big(base_name=self.wing_branch_4_2_common,
                                  parent_list=self.base_parent_const_list,
                                  pos=self.wing_branch_4_2_pos,
                                  ctrl_rotate=[90, 0, 0])
        self.branch_4_2_inner_ctrl = self.wing_branch_4_2_common + '_Inner_Ctrl'
        self.branch_4_2_outer_ctrl = self.wing_branch_4_2_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.branch_4_2_inner_ctrl)
        self.ctrl_list.append(self.branch_4_2_outer_ctrl)

        # BRANCH 4 3  CONTROLLER
        self.sphere_handle_name = self.helper_class.object_name(self.wing_branch_4_3_common,
                                                                cluster_name=True) + 'Handle'
        self.cylinder_upper_handle_name = self.get_cyliner_clu_name('Lower',
                                                                    self.branch_4_2_to_branch_4_3_common_middle) + 'Handle'
        self.cylinder_lower_handle_name = self.get_cyliner_clu_name('Upper',
                                                                    self.branch_4_3_to_branch_4_4_common_middle) + 'Handle'
        self.base_parent_const_list = [self.sphere_handle_name,
                                       self.cylinder_upper_handle_name,
                                       self.cylinder_lower_handle_name]
        self.controller_small_big(base_name=self.wing_branch_4_3_common,
                                  parent_list=self.base_parent_const_list,
                                  pos=self.wing_branch_4_3_pos,
                                  ctrl_rotate=[90, 0, 0])
        self.branch_4_3_inner_ctrl = self.wing_branch_4_3_common + '_Inner_Ctrl'
        self.branch_4_3_outer_ctrl = self.wing_branch_4_3_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.branch_4_3_inner_ctrl)
        self.ctrl_list.append(self.branch_4_3_outer_ctrl)

        # BRANCH 4 4  CONTROLLER
        self.sphere_handle_name = self.helper_class.object_name(self.wing_branch_4_4_common,
                                                                cluster_name=True) + 'Handle'
        self.cylinder_upper_handle_name = self.get_cyliner_clu_name('Lower',
                                                                    self.branch_4_3_to_branch_4_4_common_middle) + 'Handle'
        self.base_parent_const_list = [self.sphere_handle_name,
                                       self.cylinder_upper_handle_name]
        self.controller_small_big(base_name=self.wing_branch_4_4_common,
                                  parent_list=self.base_parent_const_list,
                                  pos=self.wing_branch_4_4_pos,
                                  ctrl_rotate=[90, 0, 0])
        self.branch_4_4_inner_ctrl = self.wing_branch_4_4_common + '_Inner_Ctrl'
        self.branch_4_4_outer_ctrl = self.wing_branch_4_4_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.branch_4_4_inner_ctrl)
        self.ctrl_list.append(self.branch_4_4_outer_ctrl)

        # roll bone
        self.roll_bone('Upper',
                       self.upper_wing_inner_ctrl,
                       self.lbow_inner_ctrl,
                       self.upper_wing_base_jnt_line_edit_query)
        self.roll_bone('Lower',
                       self.lbow_inner_ctrl,
                       self.hand_inner_ctrl,
                       self.lower_wing_base_jnt_line_edit_query)

        self.parent_def()

    def controller_small_big(self, base_name, parent_list, pos, ctrl_rotate=[0, 0, 90], base_ctrl_freez_rotate=True):
        self.ctrl_lower_size = [0.5, 0.5, 0.5]
        self.ctrl_outer_size = [0.8, 0.8, 0.8]

        self.base_ctrl_freez_trans = True
        self.base_ctrl_freez_rotate = base_ctrl_freez_rotate
        self.base_ctrl_freez_scale = True

        # SMALL CONTROLLER
        self.base_inner_ctrl = base_name + '_Inner_Ctrl'
        self.base_ctrl_size_ctrl = self.ctrl_lower_size
        self.base_ctrl_roate = ctrl_rotate
        self.base_parent_const_list = parent_list
        self.helper_class.set_controller(self.base_inner_ctrl, pos, self.base_ctrl_size_ctrl,
                                         self.base_ctrl_roate, self.base_parent_const_list, self.base_parent_const_list,
                                         color=self.base_ctrl_color,
                                         freez_trans=self.base_ctrl_freez_trans,
                                         freez_rotate=self.base_ctrl_freez_rotate,
                                         freez_scale=self.base_ctrl_freez_scale)

        # BIF CONTROLLER
        self.base_outer_ctrl = base_name + '_Outer_Ctrl'
        self.base_ctrl_size_ctrl = self.ctrl_outer_size
        self.base_ctrl_roate = ctrl_rotate
        self.base_parent_const_list = []
        self.helper_class.set_controller(self.base_outer_ctrl, pos, self.base_ctrl_size_ctrl,
                                         self.base_ctrl_roate, self.base_parent_const_list, self.base_parent_const_list,
                                         color=self.base_ctrl_color,
                                         freez_trans=self.base_ctrl_freez_trans,
                                         freez_rotate=self.base_ctrl_freez_rotate,
                                         freez_scale=self.base_ctrl_freez_scale)
        cmds.select(self.base_inner_ctrl, self.base_outer_ctrl)
        cmds.parent()

        self.inner_ctrl = base_name + '_Inner_Ctrl'
        self.outer_ctrl = base_name + '_Outer_Ctrl'

    def get_cyliner_clu_name(self, type, common_middle):
        if type == 'Upper':
            name = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_" + common_middle + "_Upper_Tem_" + str(
                self.val) + '_Clu'
            return name
        if type == 'Lower':
            name = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_" + common_middle + "_Lower_Tem_" + str(
                self.val) + '_Clu'
            return name

    def roll_bone(self, type, upper_object, lower_object, no_of_bone):
        # create a curve
        self.curve_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_" + type + "_Tem_" + str(
            self.val)
        self.curve_name = self.curve_common + '_Crv'
        self.curve_shape_name = self.curve_name + 'Shape'
        self.curve_0_clu_name = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_" + type + "_0_Tem_" + str(
            self.val) + '_Clu'
        self.curve_0_clu_handle_name = self.curve_0_clu_name + 'Handle'
        self.curve_1_clu_name = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_" + type + "_1_Tem_" + str(
            self.val) + '_Clu'
        self.curve_1_clu_handle_name = self.curve_1_clu_name + 'Handle'
        self.crv_list.append(self.curve_name)
        cmds.curve(d=1, p=[(0, 0, 0), (12, 0, 0)], k=[0, 1], n=self.curve_name)
        self.shape_name = cmds.listRelatives(self.curve_name, s=True)[0]
        cmds.rename(self.shape_name, self.curve_shape_name)
        cmds.select(self.curve_name + ".cv[0]")
        cmds.cluster(n=self.curve_0_clu_name)
        self.helper_class.parent_constrain(upper_object,
                                           [self.curve_0_clu_handle_name])
        cmds.select(self.curve_name + ".cv[1]")
        cmds.cluster(n=self.curve_1_clu_name)
        self.helper_class.parent_constrain(lower_object,
                                           [self.curve_1_clu_handle_name])
        self.cluster_list.append(self.curve_0_clu_handle_name)
        self.cluster_list.append(self.curve_1_clu_handle_name)

        # create a point on curve
        a = 0
        toal_minus = 0.2
        value = 1 - toal_minus
        average_val = value / (no_of_bone - 1)
        start_val = 0.1
        while a < no_of_bone:
            common_name = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_" + type + "_" + str(
                a) + "_Tem_" + str(self.val)
            self.poc_name = common_name + '_POC'
            self.sphere_name = common_name + '_Geo'
            cmds.createNode('pointOnCurveInfo', n=self.poc_name)
            cmds.connectAttr((self.curve_shape_name + '.worldSpace[0]'),
                             (self.poc_name + '.inputCurve'),
                             f=True)
            cmds.polySphere(r=1, sx=6, sy=6, ax=(0, 1, 0), cuv=2, ch=1, n=self.sphere_name)
            cmds.connectAttr((self.poc_name + '.position'),
                             (self.sphere_name + '.translate'),
                             f=True)
            self.sphere_list.append(self.sphere_name)
            self.another_sphere_list.append(self.sphere_name)
            self.helper_class.transform_rotation_scale_visible(self.sphere_name)

            cmds.setAttr((self.poc_name + '.parameter'), start_val)
            start_val += average_val

            # setAttr "Template_L_Arm_Lower_0_Tem_1_POC.parameter" 0.2;

            a += 1

    def finger_def(self):
        a = 0
        self.rot_val = 150.0 / self.wing_no_of_finger_line_edit_query
        rot_val = self.rot_val
        while a < self.wing_no_of_finger_line_edit_query:
            self.each_finger = int(self.wing_finger_line_edit[a].text())
            # create a locator and set the position
            loc_list = []

            b = 0
            loc_pos = 3
            while b < self.each_finger:
                loc_name = 'LOC_' + str(b + 1)
                cmds.spaceLocator(n=loc_name, p=(loc_pos, 0, 0))
                cmds.CenterPivot()
                loc_list.append(loc_name)
                loc_pos += 3
                loc_grp_name = 'LOC_Grp'
                if cmds.objExists(loc_grp_name):
                    cmds.select(loc_name, loc_grp_name)
                    cmds.parent()
                else:
                    cmds.select(loc_name)
                    cmds.group(n=loc_grp_name)
                    cmds.move(0, 0, 0,
                              loc_grp_name + '.scalePivot',
                              loc_grp_name + '.rotatePivot')

                b += 1

            cmds.select(loc_grp_name)
            cmds.move(self.finger_pos[0],
                      self.finger_pos[1],
                      self.finger_pos[2])
            if self.wing_side == 'L':
                cmds.setAttr((loc_grp_name + '.ry'), -(rot_val))
            else:
                cmds.setAttr((loc_grp_name + '.sx'), -1)
                cmds.setAttr((loc_grp_name + '.ry'), (rot_val))
            rot_val += self.rot_val

            b = 0
            while b < self.each_finger:
                new_loc = 'New_LOC'
                cmds.spaceLocator(n=new_loc, p=(0, 0, 0))
                cmds.parentConstraint(loc_list[b], new_loc, mo=False)
                get_trans = cmds.xform(new_loc, q=1, ws=1, rp=1)
                get_rot = cmds.getAttr(new_loc + '.r')[0]

                # now create a sphere on the pos
                self.common_name = self.prefix_name + "_" + self.wing_side + '_Wing_' + self.type + '_Finger_' + str(
                    a + 1) + '_' + str(b + 1) + '_Tem_' + str(self.val)
                self.sphere_basic_def(self.common_name,
                                      get_trans)

                # create a controller
                self.finger_handle_name = self.helper_class.object_name(self.common_name, cluster_name=True) + 'Handle'
                self.cylinder_upper_handle_name = self.get_cyliner_clu_name('Upper',
                                                                            self.base_to_shoulder_cyliner_common_middle) + 'Handle'
                self.base_parent_const_list = [self.finger_handle_name]
                self.controller_small_big(base_name=self.common_name,
                                          parent_list=self.base_parent_const_list,
                                          pos=get_trans,
                                          ctrl_rotate=get_rot,
                                          base_ctrl_freez_rotate=False)
                self.finger_inner_ctrl = self.common_name + '_Inner_Ctrl'
                self.finger_outer_ctrl = self.common_name + '_Outer_Ctrl'

                cmds.select(self.finger_outer_ctrl)
                cmds.rotate(0, 0, 90, r=True, os=True, fo=True)
                # get the rotate val

                cmds.select(new_loc)
                cmds.delete()
                b += 1

            b = 0
            while b < self.each_finger:
                # create a cylinder
                self.common_name = self.prefix_name + "_" + self.wing_side + '_Wing_' + self.type + '_Finger_' + str(
                    a + 1) + '_' + str(b + 1) + '_Tem_' + str(self.val)
                self.outer_ctrl_name = self.common_name + '_Outer_Ctrl'
                self.inner_ctrl_name = self.common_name + '_Inner_Ctrl'
                ctrl_rotate_val = cmds.getAttr(self.outer_ctrl_name + '.r')[0]
                if b == 0:
                    # Template_L_Wing_" +  self.type + "_Hand_2_Tem_1_Outer_Ctrl
                    upper_geo_name = self.prefix_name + "_" + self.wing_side + '_Wing_' + self.type + '_Hand_2_Tem_' + str(
                        self.val) + '_Geo'
                    upper_outer_ctrl_name = self.prefix_name + "_" + self.wing_side + '_Wing_' + self.type + '_Hand_2_Tem_' + str(
                        self.val) + '_Outer_Ctrl'
                    upper_inner_ctrl_name = self.prefix_name + "_" + self.wing_side + '_Wing_' + self.type + '_Hand_2_Tem_' + str(
                        self.val) + '_Inner_Ctrl'
                    current_geo_name = self.common_name + '_Geo'

                    common_name = 'Base_to_Finger_' + str(a + 1)
                    self.cylinder_basic_def(common_middle=common_name,
                                            rotate=ctrl_rotate_val,
                                            first_sphere_name=current_geo_name,
                                            secound_sphere_name=upper_geo_name)

                    cmds.select(self.outer_ctrl_name, upper_outer_ctrl_name)
                    cmds.parent()
                    cmds.parentConstraint(upper_inner_ctrl_name, self.upper_cluster_handle, mo=True)
                    cmds.parentConstraint(self.inner_ctrl_name, self.lower_cluster_handle, mo=True)

                else:

                    # Template_L_Wing_" +  self.type + "_Hand_2_Tem_1_Outer_Ctrl
                    upper_common = self.prefix_name + "_" + self.wing_side + '_Wing_' + self.type + '_Finger_' + str(
                        a + 1) + '_' + str(b) + '_Tem_' + str(self.val)
                    upper_geo_name = upper_common + '_Geo'
                    upper_outer_ctrl_name = upper_common + '_Outer_Ctrl'
                    upper_inner_ctrl_name = upper_common + '_Inner_Ctrl'
                    current_geo_name = self.common_name + '_Geo'

                    common_name = ('%s_to_%s' % (str(a + 1), str(b + 1)))
                    self.cylinder_basic_def(common_middle=common_name,
                                            rotate=ctrl_rotate_val,
                                            first_sphere_name=current_geo_name,
                                            secound_sphere_name=upper_geo_name)

                    cmds.select(self.outer_ctrl_name, upper_outer_ctrl_name)
                    cmds.parent()
                    cmds.parentConstraint(upper_inner_ctrl_name, self.upper_cluster_handle, mo=True)
                    cmds.parentConstraint(self.inner_ctrl_name, self.lower_cluster_handle, mo=True)

                b += 1

            cmds.select(loc_grp_name)
            cmds.delete()
            a += 1

    def parent_def(self):
        self.helper_class.parent(self.helper_class.object_name(self.shoulder_common, ctrl_outer_name=True),
                                 self.helper_class.object_name(self.base_common, ctrl_outer_name=True))
        self.helper_class.parent(self.helper_class.object_name(self.upper_wing_common, ctrl_outer_name=True),
                                 self.helper_class.object_name(self.shoulder_common, ctrl_outer_name=True))
        self.helper_class.parent(self.helper_class.object_name(self.wing_lbow_common, ctrl_outer_name=True),
                                 self.helper_class.object_name(self.upper_wing_common, ctrl_outer_name=True))
        self.helper_class.parent(self.helper_class.object_name(self.wing_hand_common, ctrl_outer_name=True),
                                 self.helper_class.object_name(self.wing_lbow_common, ctrl_outer_name=True))
        self.helper_class.parent(self.helper_class.object_name(self.wing_hand_2_common, ctrl_outer_name=True),
                                 self.helper_class.object_name(self.wing_hand_common, ctrl_outer_name=True))
        self.helper_class.parent(self.helper_class.object_name(self.wing_branch_1_1_common, ctrl_outer_name=True),
                                 self.helper_class.object_name(self.wing_hand_2_common, ctrl_outer_name=True))
        self.helper_class.parent(self.helper_class.object_name(self.wing_branch_1_2_common, ctrl_outer_name=True),
                                 self.helper_class.object_name(self.wing_branch_1_1_common, ctrl_outer_name=True))
        self.helper_class.parent(self.helper_class.object_name(self.wing_branch_1_3_common, ctrl_outer_name=True),
                                 self.helper_class.object_name(self.wing_branch_1_2_common, ctrl_outer_name=True))
        self.helper_class.parent(self.helper_class.object_name(self.wing_branch_1_4_common, ctrl_outer_name=True),
                                 self.helper_class.object_name(self.wing_branch_1_3_common, ctrl_outer_name=True))

        self.helper_class.parent(self.helper_class.object_name(self.wing_branch_2_1_common, ctrl_outer_name=True),
                                 self.helper_class.object_name(self.wing_hand_2_common, ctrl_outer_name=True))
        self.helper_class.parent(self.helper_class.object_name(self.wing_branch_2_2_common, ctrl_outer_name=True),
                                 self.helper_class.object_name(self.wing_branch_2_1_common, ctrl_outer_name=True))
        self.helper_class.parent(self.helper_class.object_name(self.wing_branch_2_3_common, ctrl_outer_name=True),
                                 self.helper_class.object_name(self.wing_branch_2_2_common, ctrl_outer_name=True))
        self.helper_class.parent(self.helper_class.object_name(self.wing_branch_2_4_common, ctrl_outer_name=True),
                                 self.helper_class.object_name(self.wing_branch_2_3_common, ctrl_outer_name=True))

        self.helper_class.parent(self.helper_class.object_name(self.wing_branch_3_1_common, ctrl_outer_name=True),
                                 self.helper_class.object_name(self.wing_hand_2_common, ctrl_outer_name=True))
        self.helper_class.parent(self.helper_class.object_name(self.wing_branch_3_2_common, ctrl_outer_name=True),
                                 self.helper_class.object_name(self.wing_branch_3_1_common, ctrl_outer_name=True))
        self.helper_class.parent(self.helper_class.object_name(self.wing_branch_3_3_common, ctrl_outer_name=True),
                                 self.helper_class.object_name(self.wing_branch_3_2_common, ctrl_outer_name=True))
        self.helper_class.parent(self.helper_class.object_name(self.wing_branch_3_4_common, ctrl_outer_name=True),
                                 self.helper_class.object_name(self.wing_branch_3_3_common, ctrl_outer_name=True))

        self.helper_class.parent(self.helper_class.object_name(self.wing_branch_4_1_common, ctrl_outer_name=True),
                                 self.helper_class.object_name(self.wing_lbow_common, ctrl_outer_name=True))
        self.helper_class.parent(self.helper_class.object_name(self.wing_branch_4_2_common, ctrl_outer_name=True),
                                 self.helper_class.object_name(self.wing_branch_4_1_common, ctrl_outer_name=True))
        self.helper_class.parent(self.helper_class.object_name(self.wing_branch_4_3_common, ctrl_outer_name=True),
                                 self.helper_class.object_name(self.wing_branch_4_2_common, ctrl_outer_name=True))
        self.helper_class.parent(self.helper_class.object_name(self.wing_branch_4_4_common, ctrl_outer_name=True),
                                 self.helper_class.object_name(self.wing_branch_4_3_common, ctrl_outer_name=True))

    def final_group(self):
        self.sphere_group_name = self.prefix_name + '_' + self.wing_side + "_Wing_" + self.type + "_Tem_" + str(
            self.val) + "_Sphere_Grp"
        cmds.select(cl=True)
        for each in self.sphere_list:
            self.helper_class.parent_child_grp(parent=self.sphere_group_name,
                                               child=each)
        self.cluster_group_name = self.prefix_name + '_' + self.wing_side + "_Wing_" + self.type + "_Tem_" + str(
            self.val) + "_Cluster_Grp"
        cmds.select(cl=True)
        for each in self.cluster_list:
            self.helper_class.parent_child_grp(parent=self.cluster_group_name,
                                               child=each,
                                               vis=True)

        self.cylinder_group_name = self.prefix_name + '_' + self.wing_side + "_Wing_" + self.type + "_Tem_" + str(
            self.val) + "_Cylinder_Grp"
        cmds.select(cl=True)
        for each in self.cylinder_list:
            self.helper_class.parent_child_grp(parent=self.cylinder_group_name,
                                               child=each)

        # create curve grp
        self.curve_grp_name = self.prefix_name + '_' + self.wing_side + "_Wing_" + self.type + "_Tem_" + str(
            self.val) + "_Crv_Grp"
        cmds.select(cl=True)
        for each in self.crv_list:
            self.helper_class.parent_child_grp(parent=self.curve_grp_name,
                                               child=each)

        grp_list = [self.sphere_group_name,
                    self.cluster_group_name,
                    self.cylinder_group_name,
                    self.helper_class.object_name(self.base_common, ctrl_outer_name=True),
                    self.curve_grp_name]
        self.finger_grp_name = 'Finger_Grp'

        if cmds.objExists(self.finger_grp_name):
            grp_list.append(self.finger_grp_name)
        self.main_grp_name = self.prefix_name + '_' + self.wing_side + "_Wing_" + self.type + "_Tem_" + str(
            self.val) + '_Main_Grp'
        for each in grp_list:
            self.helper_class.parent_child_grp(parent=self.main_grp_name,
                                               child=each)
        self.arm_grp_name = 'Wing_Grp'
        self.helper_class.parent_child_grp(parent=self.arm_grp_name,
                                           child=self.main_grp_name,
                                           trans_rot_scale=False)
        self.helper_class.transform_rotation_scale_visible(self.arm_grp_name, v=False)

    def mirror_status_def(self):
        # get the statu
        if self.wing_mirror_check_box.isChecked():
            self.wing_left_check_box.setChecked(True)
            self.wing_right_check_box.setChecked(True)
        else:
            self.wing_left_check_box.setChecked(False)
            self.wing_right_check_box.setChecked(False)

    def wing_hand_check_def(self):
        # get the statu
        if self.wing_hand_check_box.isChecked():
            self.wing_no_of_finger_label.setDisabled(False)
            self.wing_no_of_finger_line_edit.setDisabled(False)
            self.wing_no_of_finger_line_edit.setText(str(3))
            a = 0
            while a < len(self.wing_finger_label):
                self.wing_finger_label[a].setDisabled(False)
                self.wing_finger_line_edit[a].setDisabled(False)
                a += 1

        else:
            self.wing_no_of_finger_label.setDisabled(True)
            self.wing_no_of_finger_line_edit.setDisabled(True)
            a = 0
            while a < len(self.wing_finger_label):
                self.wing_finger_label[a].setDisabled(True)
                self.wing_finger_line_edit[a].setDisabled(True)
                a += 1

    def wing_hand_check_update_def(self):
        self.wing_hand_check_box_query = self.wing_hand_check_box.isChecked()
        if self.wing_hand_check_box_query == True:
            a = 0
            while a < len(self.wing_finger_line_edit):
                print(self.wing_finger_label[a])
                self.wing_finger_label[a].setDisabled(False)
                self.wing_finger_line_edit[a].setDisabled(False)
                a += 1
        else:
            a = 0
            while a < len(self.wing_finger_line_edit):
                self.wing_finger_label[a].setDisabled(True)
                self.wing_finger_line_edit[a].setDisabled(True)
                a += 1

    def no_finger_line_edit_def(self):
        # get the value
        grid_value = 8
        self.create_wing_button.deleteLater()
        # delete the latest one
        a = 0
        while a < len(self.wing_finger_label):
            self.wing_finger_label[a].deleteLater()
            self.wing_finger_line_edit[a].deleteLater()
            a += 1
        self.wing_finger_label = {}
        self.wing_finger_line_edit = {}
        if self.wing_no_of_finger_line_edit.text() != '':
            self.no_finger_line_edit_query = int(self.wing_no_of_finger_line_edit.text())
            a = 0
            value = 0
            while a < self.no_finger_line_edit_query:
                # FINGER_2 LABEL
                grid_value = 8 + a + 1

                self.wing_finger_label[value] = QtGui.QLabel(self.widget)
                self.wing_finger_label[value].setObjectName("finger_2_label")
                self.wing_finger_label[value].setText('Finger ' + str(a + 1))
                self.wing_grid_layout.addWidget(self.wing_finger_label[value], grid_value, 0, 1, 3)
                # FINGER_2 LINE EDIT
                self.wing_finger_line_edit[value] = QtGui.QLineEdit(self.widget)
                self.wing_finger_line_edit[value].setObjectName("finger_2_line_edit")
                self.wing_finger_line_edit[value].setValidator(self.validator)
                self.wing_finger_line_edit[value].setText(str(3))
                self.wing_grid_layout.addWidget(self.wing_finger_line_edit[value], grid_value, 1, 1, 3)
                value += 1
                a += 1
            grid_value += 1
            self.create_wing_button = QtGui.QPushButton(self.widget)
            self.create_wing_button.setObjectName("arm_create_button")
            self.create_wing_button.setText('Create Arm')
            self.create_wing_button.clicked.connect(self.new_wing_def)
            self.wing_grid_layout.addWidget(self.create_wing_button, grid_value, 0, 1, 4)
            grid_value += 1
            self.wing_grid_layout.addItem(self.spacerItem, grid_value, 0, 1, 1)

        else:
            grid_value += 1
            self.create_wing_button = QtGui.QPushButton(self.widget)
            self.create_wing_button.setObjectName("arm_create_button")
            self.create_wing_button.setText('Create Arm')
            self.create_wing_button.clicked.connect(self.new_wing_def)
            self.wing_grid_layout.addWidget(self.create_wing_button, grid_value, 0, 1, 4)
            grid_value += 1
            self.wing_grid_layout.addItem(self.spacerItem, grid_value, 0, 1, 1)

    def update_gui(self, widget):
        self.update_widget = widget

        self.verticalLayout = QtGui.QVBoxLayout(self.update_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.head_splitter = QtGui.QSplitter(self.update_widget)
        self.head_splitter.setOrientation(QtCore.Qt.Vertical)
        self.head_splitter.setObjectName("head_splitter")

        # get the radio button
        self.get_update_radio_button()
        self.get_detail_update_def()

        # lock the attr
        self.lock_attr()

    def get_update_radio_button(self):
        self.head_name_scroll_area = QtGui.QScrollArea(self.head_splitter)
        self.head_name_scroll_area.setWidgetResizable(True)
        self.head_name_scroll_area.setObjectName("head_name_scroll_area")
        self.head_name_scrollArea_widget_contents = QtGui.QWidget()
        self.head_name_scrollArea_widget_contents.setGeometry(QtCore.QRect(0, 0, 642, 64))
        self.head_name_scrollArea_widget_contents.setObjectName("head_name_scrollArea_widget_contents")
        self.gridLayout_15 = QtGui.QGridLayout(self.head_name_scrollArea_widget_contents)
        self.gridLayout_15.setObjectName("gridLayout_15")

        self.no_wing = self.helper_class.get_wing()
        a = 0
        value = 0
        grid_value = 0
        while a < len(self.no_wing):
            self.radio_button = QtGui.QRadioButton(self.head_name_scrollArea_widget_contents)
            self.radio_button.setObjectName(self.no_wing[a])
            self.radio_button.setText(self.no_wing[a])
            self.gridLayout_15.addWidget(self.radio_button, grid_value, value, 1, 1)
            self.radio_button.toggled.connect(partial(self.radio_button_change, a))
            value += 1
            if value == 3:
                value = 0
                grid_value += 1

            a += 1

        self.head_name_scroll_area.setWidget(self.head_name_scrollArea_widget_contents)

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
        self.wing_mirror_check_box.stateChanged.connect(self.mirror_status_def)
        self.arm_mirror_grid_layout.addWidget(self.wing_mirror_check_box, 0, 0, 1, 1)

        # LEFT
        self.wing_left_check_box = QtGui.QCheckBox(self.arm_mirror_group_box)
        self.wing_left_check_box.setObjectName("arm_left_check_box")
        self.wing_left_check_box.setText('Left')
        self.arm_mirror_grid_layout.addWidget(self.wing_left_check_box, 1, 0, 1, 1)

        # RIGHT
        self.wing_right_check_box = QtGui.QCheckBox(self.arm_mirror_group_box)
        self.wing_right_check_box.setObjectName("arm_right_check_box")
        self.wing_right_check_box.setText('Right')
        self.arm_mirror_grid_layout.addWidget(self.wing_right_check_box, 1, 1, 1, 1)

        # CLAVICAL
        self.wing_type_combo_box = QtGui.QComboBox(self.arm_mirror_group_box)
        self.wing_type_combo_box.setObjectName("wing_type_combo")
        self.wing_type_combo_box.addItem("Dragon")
        self.wing_type_combo_box.addItem("Bird")
        self.wing_type_combo_box.currentIndexChanged.connect(self.update_wing_type_combo_box_def)
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
        self.arm_bone_grid_layout.addWidget(self.upper_wing_base_jnt_label, 0, 0, 1, 1)
        # UPPER ARM BONE LINE EDIT
        self.upper_wing_base_jnt_line_edit = QtGui.QLineEdit(self.arm_bone_group_box)
        self.upper_wing_base_jnt_line_edit.setObjectName("arm_upper_arm_bone_line_edit")
        self.arm_bone_grid_layout.addWidget(self.upper_wing_base_jnt_line_edit, 0, 1, 1, 1)

        # LOWER ARM BONE
        # LOWER ARM BONE LABEL
        self.lower_wing_base_jnt_label = QtGui.QLabel(self.arm_bone_group_box)
        self.lower_wing_base_jnt_label.setObjectName("lower_wing_base_jnt_label")
        self.lower_wing_base_jnt_label.setText('Lower Wing Jnt')
        self.arm_bone_grid_layout.addWidget(self.lower_wing_base_jnt_label, 1, 0, 1, 1)
        # LOWER ARM BONE LINE EDIT
        self.lower_wing_base_jnt_line_edit = QtGui.QLineEdit(self.arm_bone_group_box)
        self.lower_wing_base_jnt_line_edit.setObjectName("lower_wing_base_jnt_line_edit")
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
        self.wing_hand_check_box.stateChanged.connect(self.wing_hand_check_update_def)
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
        self.gridLayout_26.addWidget(self.wing_name_label, 0, 0, 1, 1)
        # ARM NAME BUTTON
        self.wing_name_button = QtGui.QPushButton(self.arm_name_parent_group_box)
        self.wing_name_button.setMinimumSize(QtCore.QSize(297, 0))
        self.wing_name_button.setObjectName("wing_name_button")
        self.wing_name_button.setText("None")
        self.wing_name_button.clicked.connect(self.rename)
        self.gridLayout_26.addWidget(self.wing_name_button, 0, 1, 1, 1)

        # ARM PARENT
        # ARM PARENT LABEL
        self.wing_parent_label = QtGui.QLabel(self.arm_name_parent_group_box)
        self.wing_parent_label.setObjectName("wing_parent_label")
        self.wing_parent_label.setText('Parent')
        self.gridLayout_26.addWidget(self.wing_parent_label, 1, 0, 1, 1)
        # ARM PARENT BUTTON
        self.wing_parent_button = QtGui.QPushButton(self.arm_name_parent_group_box)
        self.wing_parent_button.setObjectName("wing_parent_button")
        self.wing_parent_button.setText("None")
        self.wing_parent_button.clicked.connect(self.parent)
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
        self.wing_update_button.clicked.connect(self.wing_update_button_def)
        self.gridLayout_17.addWidget(self.wing_update_button, 1, 0, 1, 1)
        #

        # DELETE BUTTON
        self.wing_delete_button = QtGui.QPushButton(self.head_update_scrollArea_widget_contents)
        self.wing_delete_button.setObjectName("wing_delete_button")
        self.wing_delete_button.setText('Delete(Wing Name)')
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

    def delete_all(self):
        print('now all Wing is going to delete')

    def radio_button_change(self, b, val):
        if val == True:
            # unlock the val
            self.unlock_attr()

            # get the value
            self.get_input_data(self.no_wing[b])

    def get_input_data(self, wing_name):
        self.wing_name = wing_name
        # self.base_common = self.prefix_name + "_" + self.wing_side  + "_Wing_" +  self.type + "_Base_Tem_" + str(self.val)

        wing_split = self.wing_name.split('_')
        self.wing_side = wing_split[0]
        self.type = wing_split[2]
        self.val = wing_split[-1]

        # get the prefix name
        # Template_L_Wing_Dragon_Tem_1_Main_Grp
        main_grp_name = "*_" + self.wing_side + "_Wing_" + self.type + "_Tem_" + str(self.val) + '_Main_Grp'
        cmds.select(main_grp_name)
        sel_main_grp = cmds.ls(sl=True)[0]
        self.prefix_name = sel_main_grp.split('_' + self.wing_side)[0]

        # MIRROR
        if self.wing_side == 'L':
            mirror_name = 'right_to_left'
        elif self.wing_side == 'R':
            mirror_name = 'left_to_right'
        mirror_grp_name = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + \
                          "_Base_Tem_" + str(self.val) + '_Outer_Ctrl_' + mirror_name + \
                          '_Mirror_Grp'
        if cmds.objExists(mirror_grp_name):
            self.wing_mirror_check_box.setChecked(True)

        if self.wing_side == 'L':
            if cmds.objExists(mirror_grp_name):
                self.wing_left_check_box.setChecked(True)
                self.wing_right_check_box.setChecked(True)
            else:
                self.wing_left_check_box.setChecked(True)
        if self.wing_side == 'R':
            if cmds.objExists(mirror_grp_name):
                self.wing_left_check_box.setChecked(True)
                self.wing_right_check_box.setChecked(True)
            else:
                self.wing_right_check_box.setChecked(True)

        if self.type == 'Dragon':
            self.wing_type_combo_box.setCurrentIndex(0)
        elif self.type == 'Bird':
            self.wing_type_combo_box.setCurrentIndex(1)

        # upper wing
        # Template_R_Wing_Dragon_Upper_1_Tem_1_Geo
        upper_geo = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + \
                    "_Upper_*_Tem_" + str(self.val) + '_Geo'
        cmds.select(upper_geo)
        sel_upper = cmds.ls(sl=True)
        self.upper_wing_base_jnt_line_edit.setText(str(len(sel_upper) - 1))

        # LOWER WING
        lower_geo = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + \
                    "_Lower_*_Tem_" + str(self.val) + '_Geo'
        lower_2_geo = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + \
                      "_Lower_2_*_Tem_" + str(self.val) + '_Geo'
        cmds.select(lower_geo)
        if cmds.objExists(lower_2_geo):
            cmds.select(lower_2_geo, d=True)
        sel_lower = cmds.ls(sl=True)
        self.lower_wing_base_jnt_line_edit.setText(str(len(sel_lower)))

        if self.type == 'Bird':
            lower_2_geo = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + \
                          "_Lower_2_*_Tem_" + str(self.val) + '_Geo'
            cmds.select(lower_2_geo)
            sel_lower = cmds.ls(sl=True)
            self.wing_end_jnt_line_edit.setText(str(len(sel_lower)))

        if self.type == 'Dragon':
            # get the hand
            # Template_R_Wing_Dragon_Finger_1_1_Tem_1_Outer_Ctrl
            finger_ctrl_name = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + \
                               "_Finger_1_1_Tem_" + str(self.val) + '_Outer_Ctrl'
            if cmds.objExists(finger_ctrl_name):
                self.wing_hand_check_box.setChecked(True)

            # get the no of the finger
            # Template_L_Wing_Dragon_Finger_1_1_Tem_1_Outer_Ctrl
            outer_ctrl = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + \
                         "_Finger_*_1_Tem_" + str(self.val) + '_Outer_Ctrl'
            if cmds.objExists(outer_ctrl):

                cmds.select(outer_ctrl)
                sel_outer_ctrl = cmds.ls(sl=True)

                a = 0
                self.wing_finger_label = {}
                self.wing_finger_line_edit = {}

                while a < len(sel_outer_ctrl):
                    # label
                    self.wing_finger_label[a] = QtGui.QLabel(self.arm_finger_group_box)
                    name = 'Finger ' + str(a + 1)
                    self.wing_finger_label[a].setObjectName(name)
                    self.wing_finger_label[a].setText(name)
                    self.arm_finger_grid_layout.addWidget(self.wing_finger_label[a], a, 0, 1, 1)

                    # line edit
                    self.wing_finger_line_edit[a] = QtGui.QLineEdit(self.arm_finger_group_box)
                    self.wing_finger_line_edit[a].setObjectName("arm_finger_3_lineEdit")
                    outer_ctrl_name = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + \
                                      '_Finger_' + str(a + 1) + '_*_Tem_' + str(self.val) + '_Outer_Ctrl'
                    cmds.select(outer_ctrl_name)
                    sel_ctrl = cmds.ls(sl=True)
                    self.wing_finger_line_edit[a].setText(str(len(sel_ctrl)))
                    self.arm_finger_grid_layout.addWidget(self.wing_finger_line_edit[a], a, 1, 1, 1)

                    a += 1

        # name button
        self.wing_name_button.setText(self.prefix_name)
        self.wing_parent_button.setText(self.parent_query())

    def lock_attr(self):
        self.wing_mirror_check_box.setDisabled(True)
        self.wing_left_check_box.setDisabled(True)
        self.wing_right_check_box.setDisabled(True)
        self.wing_type_combo_box.setDisabled(True)
        self.upper_wing_base_jnt_label.setDisabled(True)
        self.upper_wing_base_jnt_line_edit.setDisabled(True)
        self.lower_wing_base_jnt_label.setDisabled(True)
        self.lower_wing_base_jnt_line_edit.setDisabled(True)
        '''
        if self.wing_hand_check_box:
            self.wing_hand_check_box.setDisabled(True)
        '''
        self.wing_name_label.setDisabled(True)
        self.wing_name_button.setDisabled(True)
        self.wing_parent_label.setDisabled(True)
        self.wing_parent_button.setDisabled(True)
        self.wing_update_button.setDisabled(True)
        self.wing_delete_button.setDisabled(True)

    def unlock_attr(self):
        self.wing_mirror_check_box.setDisabled(False)
        self.wing_left_check_box.setDisabled(False)
        self.wing_right_check_box.setDisabled(False)
        self.wing_type_combo_box.setDisabled(False)
        self.upper_wing_base_jnt_label.setDisabled(False)
        self.upper_wing_base_jnt_line_edit.setDisabled(False)
        self.lower_wing_base_jnt_label.setDisabled(False)
        self.lower_wing_base_jnt_line_edit.setDisabled(False)
        '''
        if self.wing_hand_check_box:
            self.wing_hand_check_box.setDisabled(False)
        '''
        self.wing_name_label.setDisabled(False)
        self.wing_name_button.setDisabled(False)
        self.wing_parent_label.setDisabled(False)
        self.wing_parent_button.setDisabled(False)
        self.wing_update_button.setDisabled(False)
        self.wing_delete_button.setDisabled(False)

    def mirror_value(self):
        for each in self.ctrl_list:
            self.right_ctrl = each
            self.left_ctrl = each.replace('R', 'L')
            self.helper_class.mirror_grp(self.left_ctrl,
                                         self.right_ctrl)

    def wing_type_combo_box_def(self):
        self.wing_type_combo_box_query = self.wing_type_combo_box.currentText()
        if self.wing_type_combo_box_query == 'Dragon':
            if self.wing_end_jnt_label:
                self.wing_end_jnt_label.deleteLater()
                self.wing_end_jnt_line_edit.deleteLater()
            self.wing_hand_check_box = QtGui.QCheckBox(self.widget)
            self.wing_hand_check_box.setObjectName("hand_check_box")
            self.wing_hand_check_box.setText('Wing Hand')
            self.wing_hand_check_box.stateChanged.connect(self.wing_hand_check_def)
            self.wing_grid_layout.addWidget(self.wing_hand_check_box, 5, 0, 1, 1)

            # NO OF FINGER LABEL
            self.wing_no_of_finger_label = QtGui.QLabel(self.widget)
            self.wing_no_of_finger_label.setObjectName("no_of_finger_label")
            self.wing_no_of_finger_label.setText('No Of Finger')
            self.wing_no_of_finger_label.setDisabled(True)
            self.wing_grid_layout.addWidget(self.wing_no_of_finger_label, 6, 0, 1, 1)
            # NO OF FINGER LINE EDIT
            self.wing_no_of_finger_line_edit = QtGui.QLineEdit(self.widget)
            self.wing_no_of_finger_line_edit.setObjectName("no_of_finger_line_edit")
            self.wing_no_of_finger_line_edit.setValidator(self.validator)
            self.wing_no_of_finger_line_edit.setDisabled(True)
            self.wing_no_of_finger_line_edit.textChanged.connect(self.no_finger_line_edit_def)
            self.wing_grid_layout.addWidget(self.wing_no_of_finger_line_edit, 6, 1, 1, 3)
            a = 0
            while a < len(self.wing_finger_label):
                self.wing_finger_label[a].setDisabled(False)
                self.wing_finger_line_edit[a].setDisabled(False)
                a += 1
        elif self.wing_type_combo_box_query == 'Bird':
            self.wing_hand_check_box.deleteLater()
            self.wing_no_of_finger_label.deleteLater()
            self.wing_no_of_finger_line_edit.deleteLater()
            a = 0
            while a < len(self.wing_finger_label):
                self.wing_finger_label[a].deleteLater()
                self.wing_finger_line_edit[a].deleteLater()
                a += 1

            self.wing_end_jnt_label = QtGui.QLabel(self.widget)
            self.wing_end_jnt_label.setObjectName("Wing_End_label")
            self.wing_end_jnt_label.setText('Wing End')
            self.wing_grid_layout.addWidget(self.wing_end_jnt_label, 5, 0, 1, 3)

            self.wing_end_jnt_line_edit = QtGui.QLineEdit(self.widget)
            self.wing_end_jnt_line_edit.setObjectName("Wing_End_line_edit")
            self.wing_end_jnt_line_edit.setValidator(self.validator)
            self.wing_end_jnt_line_edit.setText(str(6))
            self.wing_grid_layout.addWidget(self.wing_end_jnt_line_edit, 5, 1, 1, 3)

    def mirror_value(self):
        for each in self.ctrl_list:
            self.right_ctrl = each
            self.left_ctrl = each.replace('R', 'L')
            self.helper_class.mirror_grp(self.left_ctrl,
                                         self.right_ctrl)

    def update_wing_type_combo_box_def(self):
        # get the option menu
        self.wing_type_combo_box_query = self.wing_type_combo_box.currentText()
        if self.wing_type_combo_box_query == 'Dragon':
            if self.wing_end_jnt_label:
                self.wing_end_jnt_label.deleteLater()
                self.wing_end_jnt_line_edit.deleteLater()

            self.wing_hand_check_box = QtGui.QCheckBox(self.arm_hand_double_wrist_group_box)
            self.wing_hand_check_box.setObjectName("hand_check_box")
            self.wing_hand_check_box.setText('Wing Hand')
            # self.wing_hand_check_box.stateChanged.connect(self.wing_hand_check_def)
            self.arm_hand_double_wrist_grid_layout.addWidget(self.wing_hand_check_box, 0, 0, 1, 1)

            a = 0
            self.sel_outer_ctrl = []
            while a < len(self.sel_outer_ctrl):
                # label
                self.wing_finger_label[a] = QtGui.QLabel(self.arm_finger_group_box)
                self.wing_finger_label[a].setObjectName(sel_outer_ctrl[a])
                self.wing_finger_label[a].setText(sel_outer_ctrl[a])
                self.arm_finger_grid_layout.addWidget(self.wing_finger_label[a], a, 0, 1, 1)

                # line edit
                self.wing_finger_line_edit[a] = QtGui.QLineEdit(self.arm_finger_group_box)
                self.wing_finger_line_edit[a].setObjectName("arm_finger_3_lineEdit")
                self.arm_finger_grid_layout.addWidget(self.wing_finger_line_edit[a], a, 1, 1, 1)

                a += 1


        elif self.wing_type_combo_box_query == 'Bird':
            self.wing_hand_check_box.deleteLater()
            a = 0
            while a < len(self.wing_finger_label):
                self.wing_finger_label[a].deleteLater()
                self.wing_finger_line_edit[a].deleteLater()
                a += 1

            self.wing_end_jnt_label = QtGui.QLabel(self.arm_bone_group_box)
            self.wing_end_jnt_label.setObjectName("Wing_End_label")
            self.wing_end_jnt_label.setText('Wing End')
            self.arm_bone_grid_layout.addWidget(self.wing_end_jnt_label, 2, 0, 1, 3)

            self.wing_end_jnt_line_edit = QtGui.QLineEdit(self.arm_bone_group_box)
            self.wing_end_jnt_line_edit.setObjectName("Wing_End_line_edit")
            self.validator = QtGui.QDoubleValidator()
            self.wing_end_jnt_line_edit.setValidator(self.validator)
            self.wing_end_jnt_line_edit.setText(str(6))
            self.arm_bone_grid_layout.addWidget(self.wing_end_jnt_line_edit, 2, 1, 1, 3)

    def parent_query(self):
        # Template_L_Wing_Bird_Base_Tem_1_Outer_Ctrl
        base_ctrl_name = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + \
                         "_Base_Tem_" + str(self.val) + '_Outer_Ctrl'
        value = cmds.listRelatives(base_ctrl_name, type='parentConstraint')
        if value == None:
            parent = 'None'
        else:
            parent = cmds.listConnections((value[0] + '.target[0].targetTranslate'), type='transform')[0]
        return parent

    def get_update_ui_def(self):
        # MIRROR
        self.wing_mirror_check_box_query = self.wing_mirror_check_box.isChecked()

        # LEFT
        self.wing_left_check_box_query = self.wing_left_check_box.isChecked()

        # RIGHT
        self.wing_right_check_box_queru = self.wing_right_check_box.isChecked()

        # TYPE
        self.wing_type_combo_box_query = self.wing_type_combo_box.currentText()

        # UPPER WING
        self.upper_wing_base_jnt_line_edit_query = int(self.upper_wing_base_jnt_line_edit.text())

        # LOWER WING
        self.lower_wing_base_jnt_line_edit_query = int(self.lower_wing_base_jnt_line_edit.text())

        if self.wing_type_combo_box_query == 'Dragon':
            self.wing_hand_check_box_query = self.wing_hand_check_box.isChecked()

        elif self.wing_type_combo_box_query == 'Bird':
            self.wing_end_jnt_line_edit_query = int(self.wing_end_jnt_line_edit.text())

    def controller_variable(self):
        if self.wing_type_combo_box_query == 'Dragon':
            # DRAGON VARIABLE
            self.base_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Base_Tem_" + str(
                self.val)

            # SHOULDER
            self.shoulder_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Shoulder_Tem_" + str(
                self.val)

            # UPPER WING
            self.upper_wing_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Upper_Tem_" + str(
                self.val)

            # lBow
            self.wing_lbow_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_lBow_Tem_" + str(
                self.val)

            # WING HAND
            self.wing_hand_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Hand_Tem_" + str(
                self.val)

            # WING HAND 2
            self.wing_hand_2_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Hand_2_Tem_" + str(
                self.val)

            # WING BRAMCH 1 1
            self.wing_branch_1_1_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_1_1_Tem_" + str(
                self.val)

            # WING BRAMCH 1 2
            self.wing_branch_1_2_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_1_2_Tem_" + str(
                self.val)

            # WING BRAMCH 1 3
            self.wing_branch_1_3_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_1_3_Tem_" + str(
                self.val)

            # WING BRAMCH 1 4
            self.wing_branch_1_4_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_1_4_Tem_" + str(
                self.val)

            # WING BRAMCH 2 1
            self.wing_branch_2_1_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_2_1_Tem_" + str(
                self.val)

            # WING BRAMCH 2 2
            self.wing_branch_2_2_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_2_2_Tem_" + str(
                self.val)

            # WING BRAMCH 2 3
            self.wing_branch_2_3_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_2_3_Tem_" + str(
                self.val)

            # WING BRAMCH 2 4
            self.wing_branch_2_4_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_2_4_Tem_" + str(
                self.val)

            # WING BRAMCH 3 1
            self.wing_branch_3_1_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_3_1_Tem_" + str(
                self.val)

            # WING BRAMCH 3 2
            self.wing_branch_3_2_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_3_2_Tem_" + str(
                self.val)

            # WING BRAMCH 3 3
            self.wing_branch_3_3_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_3_3_Tem_" + str(
                self.val)

            # WING BRAMCH 3 4
            self.wing_branch_3_4_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_3_4_Tem_" + str(
                self.val)

            # WING BRAMCH 4 1
            self.wing_branch_4_1_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_4_1_Tem_" + str(
                self.val)

            # WING BRAMCH 4 2
            self.wing_branch_4_2_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_4_2_Tem_" + str(
                self.val)

            # WING BRAMCH 4 4
            self.wing_branch_4_3_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_4_3_Tem_" + str(
                self.val)

            # WING BRAMCH 4 4
            self.wing_branch_4_4_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_4_4_Tem_" + str(
                self.val)

            # CYLINDER
            # base to shoulder
            self.base_to_shoulder_cyliner_common_middle = 'Base_to_Shoulder'

            # shoulder to uppper wing
            self.shoulder_to_upper_common_middle = 'Shoulder_to_Upper'

            # upper wing to lbow
            self.upper_to_lbow_common_middle = 'Upper_to_lBow'

            # upper wing to lbow
            self.lbow_to_hand_common_middle = 'lBow_to_Hand'

            # upper wing to lbow
            self.hand_to_hand_2_common_middle = 'Hand_to_Hand_2'

            # hand 2 to branch 1 1
            self.hand_2_to_branch_1_1_common_middle = 'Hand_2_to_Branch_1_1'

            # branch 1 1 to branch 1 2
            self.branch_1_1_to_branch_1_2_common_middle = 'Branch_1_1_to_Branch_1_2'

            # branch 1 2 to branch 1 3
            self.branch_1_2_to_branch_1_3_common_middle = 'Branch_1_2_to_Branch_1_3'

            # branch 1 3 to branch 1 4
            self.branch_1_3_to_branch_1_4_common_middle = 'Branch_1_3_to_Branch_1_4'

            # hand 2 to branch 2 1
            self.hand_2_to_branch_2_1_common_middle = 'Hand_2_to_Branch_2_1'

            # branch 2 1 to branch 2 2
            self.branch_2_1_to_branch_2_2_common_middle = 'Branch_2_1_to_Branch_2_2'

            # branch 2 2 to branch 2 3
            self.branch_2_2_to_branch_2_3_common_middle = 'Branch_2_2_to_Branch_2_3'

            # branch 2 3 to branch 2 4
            self.branch_2_3_to_branch_2_4_common_middle = 'Branch_2_3_to_Branch_2_4'

            # hand 2 to branch 3 1
            self.hand_2_to_branch_3_1_common_middle = 'Hand_2_to_Branch_3_1'

            # branch 3 1 to branch 3 2
            self.branch_3_1_to_branch_3_2_common_middle = 'Branch_3_1_to_Branch_3_2'

            # branch 3 2 to branch 3 3
            self.branch_3_2_to_branch_3_3_common_middle = 'Branch_3_2_to_Branch_3_3'

            # branch 3 3 to branch 3 4
            self.branch_3_3_to_branch_3_4_common_middle = 'Branch_3_3_to_Branch_3_4'

            # hand 2 to branch 4 1
            self.lbow_to_branch_4_1_common_middle = 'lBow_to_Branch_4_1'

            # branch 4 1 to branch 4 2
            self.branch_4_1_to_branch_4_2_common_middle = 'Branch_4_1_to_Branch_4_2'

            # branch 4 2 to branch 4 3
            self.branch_4_2_to_branch_4_3_common_middle = 'Branch_4_2_to_Branch_4_3'

            # branch 4 3 to branch 4 4
            self.branch_4_3_to_branch_4_4_common_middle = 'Branch_4_3_to_Branch_4_4'

            # CONTROLLER
            # BASE CONTROLLER
            self.base_inner_ctrl = self.base_common + '_Inner_Ctrl'
            self.base_outer_ctrl = self.base_common + '_Outer_Ctrl'

            # SHOULDER CONTROLLER
            self.shoulder_inner_ctrl = self.shoulder_common + '_Inner_Ctrl'
            self.shoulder_outer_ctrl = self.shoulder_common + '_Outer_Ctrl'

            # UPPER WING CONTROLLER
            self.upper_wing_inner_ctrl = self.upper_wing_common + '_Inner_Ctrl'
            self.upper_wing_outer_ctrl = self.upper_wing_common + '_Outer_Ctrl'

            # LBOW CONTROLLER
            self.lbow_inner_ctrl = self.wing_lbow_common + '_Inner_Ctrl'
            self.lbow_outer_ctrl = self.wing_lbow_common + '_Outer_Ctrl'

            # HAND CONTROLLER
            self.hand_inner_ctrl = self.wing_hand_common + '_Inner_Ctrl'
            self.hand_outer_ctrl = self.wing_hand_common + '_Outer_Ctrl'

            # HAND 2 CONTROLLER
            self.hand_2_inner_ctrl = self.wing_hand_2_common + '_Inner_Ctrl'
            self.hand_2_outer_ctrl = self.wing_hand_2_common + '_Outer_Ctrl'

            # BRANCH 1 1  CONTROLLER
            self.branch_1_1_inner_ctrl = self.wing_branch_1_1_common + '_Inner_Ctrl'
            self.branch_1_1_outer_ctrl = self.wing_branch_1_1_common + '_Outer_Ctrl'

            # BRANCH 1 2 CONTROLLER
            self.branch_1_2_inner_ctrl = self.wing_branch_1_2_common + '_Inner_Ctrl'
            self.branch_1_2_outer_ctrl = self.wing_branch_1_2_common + '_Outer_Ctrl'

            # BRANCH 1 3  CONTROLLER
            self.branch_1_3_inner_ctrl = self.wing_branch_1_3_common + '_Inner_Ctrl'
            self.branch_1_3_outer_ctrl = self.wing_branch_1_3_common + '_Outer_Ctrl'

            # BRANCH 1 4  CONTROLLER
            self.branch_1_4_inner_ctrl = self.wing_branch_1_4_common + '_Inner_Ctrl'
            self.branch_1_4_outer_ctrl = self.wing_branch_1_4_common + '_Outer_Ctrl'

            # BRANCH 2 1  CONTROLLER
            self.branch_2_1_inner_ctrl = self.wing_branch_2_1_common + '_Inner_Ctrl'
            self.branch_2_1_outer_ctrl = self.wing_branch_2_1_common + '_Outer_Ctrl'

            # BRANCH 2 2  CONTROLLER
            self.branch_2_2_inner_ctrl = self.wing_branch_2_2_common + '_Inner_Ctrl'
            self.branch_2_2_outer_ctrl = self.wing_branch_2_2_common + '_Outer_Ctrl'

            # BRANCH 2 3  CONTROLLER
            self.branch_2_3_inner_ctrl = self.wing_branch_2_3_common + '_Inner_Ctrl'
            self.branch_2_3_outer_ctrl = self.wing_branch_2_3_common + '_Outer_Ctrl'

            # BRANCH 2 4  CONTROLLER
            self.branch_2_4_inner_ctrl = self.wing_branch_2_4_common + '_Inner_Ctrl'
            self.branch_2_4_outer_ctrl = self.wing_branch_2_4_common + '_Outer_Ctrl'

            # BRANCH 3 1  CONTROLLER
            self.branch_3_1_inner_ctrl = self.wing_branch_3_1_common + '_Inner_Ctrl'
            self.branch_3_1_outer_ctrl = self.wing_branch_3_1_common + '_Outer_Ctrl'

            # BRANCH 3 2  CONTROLLER
            self.branch_3_2_inner_ctrl = self.wing_branch_3_2_common + '_Inner_Ctrl'
            self.branch_3_2_outer_ctrl = self.wing_branch_3_2_common + '_Outer_Ctrl'

            # BRANCH 3 3  CONTROLLER
            self.branch_3_3_inner_ctrl = self.wing_branch_3_3_common + '_Inner_Ctrl'
            self.branch_3_3_outer_ctrl = self.wing_branch_3_3_common + '_Outer_Ctrl'

            # BRANCH 3 4  CONTROLLER
            self.branch_3_4_inner_ctrl = self.wing_branch_3_4_common + '_Inner_Ctrl'
            self.branch_3_4_outer_ctrl = self.wing_branch_3_4_common + '_Outer_Ctrl'

            # BRANCH 4 1  CONTROLLER
            self.branch_4_1_inner_ctrl = self.wing_branch_4_1_common + '_Inner_Ctrl'
            self.branch_4_1_outer_ctrl = self.wing_branch_4_1_common + '_Outer_Ctrl'

            # BRANCH 4 2  CONTROLLER
            self.branch_4_2_inner_ctrl = self.wing_branch_4_2_common + '_Inner_Ctrl'
            self.branch_4_2_outer_ctrl = self.wing_branch_4_2_common + '_Outer_Ctrl'

            # BRANCH 4 3  CONTROLLER
            self.branch_4_3_inner_ctrl = self.wing_branch_4_3_common + '_Inner_Ctrl'
            self.branch_4_3_outer_ctrl = self.wing_branch_4_3_common + '_Outer_Ctrl'

            # BRANCH 4 4  CONTROLLER
            self.branch_4_4_inner_ctrl = self.wing_branch_4_4_common + '_Inner_Ctrl'
            self.branch_4_4_outer_ctrl = self.wing_branch_4_4_common + '_Outer_Ctrl'

        elif self.wing_type_combo_box_query == 'Bird':
            # BIRD ARIABLE
            # Base
            self.base_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Base_Tem_" + str(
                self.val)

            # upper Pos
            self.upper_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Upper_Tem_" + str(
                self.val)

            # shoulder Pos
            self.shoulder_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Shoulder_Tem_" + str(
                self.val)

            # lbow Pos
            self.lbow_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_lBow_Tem_" + str(
                self.val)

            # hand Pos
            self.hand_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Hand_Tem_" + str(
                self.val)

            # hand End Pos
            self.hand_end_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Hand_End_Tem_" + str(
                self.val)

            # CYLINDER
            self.base_to_upper_cyliner_common_middle = 'Base_to_Upper'

            # upper to shoulder
            self.upper_to_shoulder_cyliner_common_middle = 'Upper_to_Shoulder'

            # shoulder to lbow
            self.shoulder_to_lbow_cyliner_common_middle = 'Shoulder_to_lBow'

            # lbow to hand
            self.lbow_to_hand_cyliner_common_middle = 'lBow_to_Hand'

            # hand to hand2
            self.hand_to_hand_end_cyliner_common_middle = 'Hand_to_Hand_End'

            # CONTROLLER
            # BASE CONTROLLER
            self.base_inner_ctrl = self.base_common + '_Inner_Ctrl'
            self.base_outer_ctrl = self.base_common + '_Outer_Ctrl'

            # UPPER CONTROLLER
            self.upper_inner_ctrl = self.upper_common + '_Inner_Ctrl'
            self.upper_outer_ctrl = self.upper_common + '_Outer_Ctrl'

            # SHOULDER CONTROLLER
            self.shoulder_inner_ctrl = self.shoulder_common + '_Inner_Ctrl'
            self.shoulder_outer_ctrl = self.shoulder_common + '_Outer_Ctrl'

            # LBOW CONTROLLER
            self.lbow_inner_ctrl = self.lbow_common + '_Inner_Ctrl'
            self.lbow_outer_ctrl = self.lbow_common + '_Outer_Ctrl'

            # HAND CONTROLLER
            self.hand_inner_ctrl = self.hand_common + '_Inner_Ctrl'
            self.hand_outer_ctrl = self.hand_common + '_Outer_Ctrl'

            # HAND END CONTROLLER
            self.hand_end_inner_ctrl = self.hand_end_common + '_Inner_Ctrl'
            self.hand_end_outer_ctrl = self.hand_end_common + '_Outer_Ctrl'

    def wing_update_button_def(self):
        # UI UPDATE
        self.get_update_ui_def()

        # contoller grp
        self.controller_variable()

        if self.wing_type_combo_box_query == 'Dragon':

            # UPPER ROLL
            upper_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + \
                           "_Upper_*_Tem_" + str(self.val)
            upper_geo = upper_common + '_Geo'
            # Template_L_Wing_Dragon_Upper_to_lBow_Tem_1_Geo
            upper_lbow_geo = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + \
                             "_Upper_to_lBow_Tem_" + str(self.val) + '_Geo'
            cmds.select(upper_geo)
            cmds.select(upper_lbow_geo, d=True)
            self.sel_upper = cmds.ls(sl=True)
            if self.upper_wing_base_jnt_line_edit_query != len(self.sel_upper):
                # create a upper roll
                self.roll_update_def('Upper', self.upper_wing_inner_ctrl,
                                     self.lbow_inner_ctrl, self.upper_wing_base_jnt_line_edit_query)
                self.final_group()

                if self.wing_mirror_check_box_query == True:
                    # rever the side
                    if self.wing_side == 'L':
                        value = 'R'
                    else:
                        value = 'L'
                    self.wing_side = value
                    self.controller_variable()
                    upper_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + \
                                   "_Upper_*_Tem_" + str(self.val)
                    upper_lbow_geo = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + \
                                     "_Upper_to_lBow_Tem_" + str(self.val) + '_Geo'
                    upper_geo = upper_common + '_Geo'
                    cmds.select(upper_geo)
                    cmds.select(upper_lbow_geo, d=True)
                    self.sel_upper = cmds.ls(sl=True)
                    self.roll_update_def('Upper', self.upper_wing_inner_ctrl,
                                         self.lbow_inner_ctrl, self.upper_wing_base_jnt_line_edit_query)
                    self.final_group()

                    if self.wing_side == 'L':
                        value = 'R'
                    else:
                        value = 'L'
                    self.wing_side = value
                    self.controller_variable()

            # LOWER ROLL
            lower_geo = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + \
                        "_Lower_*_Tem_" + str(self.val) + '_Geo'
            cmds.select(lower_geo)
            self.sel_upper = cmds.ls(sl=True)
            if self.lower_wing_base_jnt_line_edit_query != len(self.sel_upper):
                # create a upper roll
                self.roll_update_def('Lower', self.lbow_inner_ctrl,
                                     self.hand_inner_ctrl, self.lower_wing_base_jnt_line_edit_query)
                self.final_group()
                if self.wing_mirror_check_box_query == True:
                    if self.wing_side == 'L':
                        value = 'R'
                    else:
                        value = 'L'
                    self.wing_side = value
                    self.controller_variable()

                    lower_geo = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + \
                                "_Lower_*_Tem_" + str(self.val) + '_Geo'
                    cmds.select(lower_geo)
                    self.sel_upper = cmds.ls(sl=True)
                    self.roll_update_def('Lower', self.lbow_inner_ctrl,
                                         self.hand_inner_ctrl, self.lower_wing_base_jnt_line_edit_query)
                    self.final_group()

                    if self.wing_side == 'L':
                        value = 'R'
                    else:
                        value = 'L'
                    self.wing_side = value
                    self.controller_variable()

            # HAND
            if self.wing_hand_check_box_query == False:
                # Template_L_Wing_Dragon_Finger_1_1_Tem_1_Outer_Ctrl
                outer_finger_ctrl = self.prefix_name + "_" + self.wing_side + "_Wing_Dragon_Finger_1_1_Tem_" + str(
                    self.val) + '_Outer_Ctrl'
                if cmds.objExists(outer_finger_ctrl):
                    self.delete_finger()

                    if self.wing_mirror_check_box_query == True:
                        if self.wing_side == 'L':
                            value = 'R'
                        else:
                            value = 'L'
                        self.wing_side = value
                        self.controller_variable()

                        self.delete_finger()

                        if self.wing_side == 'L':
                            value = 'R'
                        else:
                            value = 'L'
                        self.wing_side = value
                        self.controller_variable()

                    # delete the later
                    a = 0
                    while a < len(self.wing_finger_line_edit):
                        # self.arm_create_button.deleteLater()
                        self.wing_finger_label[a].deleteLater()
                        self.wing_finger_line_edit[a].deleteLater()
                        a += 1
                    self.wing_finger_label = {}
                    self.wing_finger_line_edit = {}

            else:
                # get things
                a = 0
                while a < len(self.wing_finger_line_edit):
                    # get the line edit
                    # Template_L_Wing_Dragon_Finger_3_1_Tem_1_Outer_Ctrl
                    outer_finger_ctrl_name = self.prefix_name + "_" + self.wing_side + '_Wing_Dragon_Finger_' + str(
                        a + 1) + '_*_Tem_' + str(self.val) + '_Geo'
                    cmds.select(outer_finger_ctrl_name)
                    sel_outer = cmds.ls(sl=True)
                    # get the line edit
                    finger_query = int(self.wing_finger_line_edit[a].text())
                    if finger_query != len(sel_outer):
                        # delete all the finger
                        self.delete_finger()
                        # create a new finger
                        self.wing_no_of_finger_line_edit_query = len(self.wing_finger_line_edit)
                        # Template_L_Wing_Dragon_Hand_2_Tem_1_Outer_Ctrl
                        hand_ctrl = self.prefix_name + "_" + self.wing_side + '_Wing_Dragon_Hand_2_Tem_' + str(
                            self.val) + '_Outer_Ctrl'
                        get_trans = cmds.xform(hand_ctrl, q=1, ws=1, rp=1)
                        self.finger_pos = get_trans
                        if self.wing_side == 'L':
                            self.base_ctrl_color = 'Blue'
                        else:
                            self.base_ctrl_color = 'Red'
                        self.finger_def()
                        self.final_group()
                        if self.wing_mirror_check_box_query == True:
                            # rever the side
                            if self.wing_side == 'L':
                                value = 'R'
                            else:
                                value = 'L'
                            self.wing_side = value
                            self.controller_variable()
                            self.delete_finger()
                            # create a new finger
                            self.wing_no_of_finger_line_edit_query = len(self.wing_finger_line_edit)
                            # Template_L_Wing_Dragon_Hand_2_Tem_1_Outer_Ctrl
                            hand_ctrl = self.prefix_name + "_" + self.wing_side + '_Wing_Dragon_Hand_2_Tem_' + str(
                                self.val) + '_Outer_Ctrl'
                            get_trans = cmds.xform(hand_ctrl, q=1, ws=1, rp=1)
                            self.finger_pos = get_trans
                            if self.wing_side == 'L':
                                self.base_ctrl_color = 'Blue'
                            else:
                                self.base_ctrl_color = 'Red'
                            self.finger_def()
                            self.final_group()

                        pass

                    a += 1




        elif self.wing_type_combo_box_query == 'Bird':
            pass

    def roll_update_def(self, type, first, secound, line_edit):
        upper_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + \
                       '_' + type + '_*_Tem_' + str(self.val)

        curve_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + '_' + type + '_Tem_' + str(
            self.val)
        curve_name = curve_common + '_Crv'
        upper_poc = upper_common + '_POC'
        clu_handle_name = upper_common + '_CluHandle'
        # Template_L_Wing_Dragon_Upper_to_lBow_Lower_Tem_1_CluHandle
        # Template_L_Wing_Dragon_Upper_to_lBow_Upper_Tem_1_CluHandle
        upper_lbow = self.prefix_name + "_" + self.wing_side + '_Wing_Dragon_' + type + '_to_lBow_Upper_Tem_' + str(
            self.val) + '_CluHandle'
        lower_lbow = self.prefix_name + "_" + self.wing_side + '_Wing_Dragon_' + type + '_to_lBow_Lower_Tem_' + str(
            self.val) + '_CluHandle'

        cmds.select(self.sel_upper, curve_name, upper_poc, clu_handle_name)
        if type == 'Upper':
            cmds.select(upper_lbow, lower_lbow, d=True)
        cmds.delete()
        # create a new roll
        '''
        self.roll_bone(type,
                       self.upper_wing_inner_ctrl,
                       self.lbow_inner_ctrl,
                       self.upper_wing_base_jnt_line_edit_query)
        '''
        self.roll_bone(type,
                       first,
                       secound,
                       line_edit)

    def delete_finger(self):
        finger_common_name = self.prefix_name + "_" + self.wing_side + "_Wing_Dragon_Finger_*_*_Tem_" + str(self.val)
        geo_name = finger_common_name + '_Geo'
        clu_handle_name = finger_common_name + '_CluHandle'
        # Template_L_Wing_Dragon_Base_to_Finger_1_Upper_Tem_1_CluHandle
        finger_upper = self.prefix_name + "_" + self.wing_side + "_Wing_Dragon_Base_to_Finger_*_Upper_Tem_" + str(
            self.val) + '_CluHandle'

        cmds.select(geo_name, clu_handle_name, finger_upper)
        # cylinder
        a = 0
        while a < len(self.wing_finger_line_edit):
            cylinder_name = self.prefix_name + "_" + self.wing_side + '_Wing_Dragon_' + str(a + 1) + '_to_*_Tem_' + str(
                self.val) + '_Geo'
            lower_cluster_name = self.prefix_name + "_" + self.wing_side + '_Wing_Dragon_' + str(
                a + 1) + '_to_*_Lower_Tem_' + str(self.val) + '_CluHandle'
            upper_cluster_name = self.prefix_name + "_" + self.wing_side + '_Wing_Dragon_' + str(
                a + 1) + '_to_*_Upper_Tem_' + str(self.val) + '_CluHandle'
            outer_ctrl = self.prefix_name + "_" + self.wing_side + '_Wing_Dragon_Finger_' + str(
                a + 1) + '_1_Tem_' + str(self.val) + '_Outer_Ctrl'
            cmds.select(cylinder_name, lower_cluster_name, upper_cluster_name, outer_ctrl, add=True)
            a += 1
        cylinder_base = self.prefix_name + "_" + self.wing_side + "_Wing_Dragon_Base_to_Finger_*_Tem_" + str(
            self.val) + '_Geo'
        cmds.select(cylinder_base, add=True)
        cmds.delete()

    def rename(self):
        self.wing_mirror_check_box_query = self.wing_mirror_check_box.isChecked()
        if self.wing_mirror_check_box_query == True:
            if self.wing_side == 'L':
                value = 'R'
            elif self.wing_side == 'R':
                value = 'L'
            rename.main('Wing', self.wing_name, self.wing_name_button,
                        mirror_val=True,
                        mirror_side=value)
        else:
            rename.main('Wing', self.wing_name, self.wing_name_button,
                        mirror_val=False,
                        mirror_side='')

    def parent(self):
        parent.main('Wing', self.wing_name, self.wing_name_button)

    def controller_get_data(self, main_grp_name):
        # Template_L_Wing_Dragon_Tem_1_Main_Grp
        main_grp_split = main_grp_name.split('_')
        self.prefix_name = main_grp_split[0]
        self.wing_side = main_grp_split[1]
        self.type = main_grp_split[3]
        self.val = main_grp_split[5]

        self.ctrl_list = {}
        if self.type == 'Dragon':
            # Base
            self.base_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Base_Tem_" + str(
                self.val)
            self.base_ctrl_name = self.base_common + '_Inner_Ctrl'
            self.base_jnt_name = self.base_common + '_Jnt'
            self.base_ctrl_get_trans = cmds.xform(self.base_ctrl_name, q=1, ws=1, rp=1)
            self.base_ctrl_get_rot = cmds.getAttr(self.base_ctrl_name + '.r')

            # SHOULDER
            self.shoulder_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Shoulder_Tem_" + str(
                self.val)
            self.shoulder_ctrl_name = self.shoulder_common + '_Inner_Ctrl'
            self.shoulder_jnt_name = self.shoulder_common + '_Jnt'
            self.shoulder_ctrl_get_trans = cmds.xform(self.shoulder_ctrl_name, q=1, ws=1, rp=1)
            self.shoulder_ctrl_get_rot = cmds.getAttr(self.shoulder_ctrl_name + '.r')
            self.ctrl_list[self.shoulder_ctrl_name] = {}
            self.ctrl_list[self.shoulder_ctrl_name]['Trans'] = self.shoulder_ctrl_get_trans
            self.ctrl_list[self.shoulder_ctrl_name]['Rot'] = self.shoulder_ctrl_get_rot

            # UPPER WING
            self.upper_wing_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Upper_Tem_" + str(
                self.val)
            self.upper_wing_ctrl_name = self.upper_wing_common + '_Inner_Ctrl'
            self.upper_wing_jnt_name = self.upper_wing_common + '_Jnt'
            self.upper_wing_ctrl_get_trans = cmds.xform(self.upper_wing_ctrl_name, q=1, ws=1, rp=1)
            self.upper_wing_ctrl_get_rot = cmds.getAttr(self.upper_wing_ctrl_name + '.r')
            self.ctrl_list[self.upper_wing_ctrl_name] = {}
            self.ctrl_list[self.upper_wing_ctrl_name]['Trans'] = self.upper_wing_ctrl_get_trans
            self.ctrl_list[self.upper_wing_ctrl_name]['Rot'] = self.upper_wing_ctrl_get_rot

            # lBow
            self.wing_lbow_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_lBow_Tem_" + str(
                self.val)
            self.wing_lbow_ctrl_name = self.wing_lbow_common + '_Inner_Ctrl'
            self.wing_lbow_jnt_name = self.wing_lbow_common + '_Jnt'
            self.wing_lbow_ctrl_get_trans = cmds.xform(self.wing_lbow_ctrl_name, q=1, ws=1, rp=1)
            self.wing_lbow_ctrl_get_rot = cmds.getAttr(self.wing_lbow_ctrl_name + '.r')
            self.ctrl_list[self.wing_lbow_ctrl_name] = {}
            self.ctrl_list[self.wing_lbow_ctrl_name]['Trans'] = self.wing_lbow_ctrl_get_trans
            self.ctrl_list[self.wing_lbow_ctrl_name]['Rot'] = self.wing_lbow_ctrl_get_rot

            # WING HAND
            self.wing_hand_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Hand_Tem_" + str(
                self.val)
            self.wing_hand_ctrl_name = self.wing_hand_common + '_Inner_Ctrl'
            self.wing_hand_jnt_name = self.wing_hand_common + '_Jnt'
            self.wing_hand_ctrl_get_trans = cmds.xform(self.wing_hand_ctrl_name, q=1, ws=1, rp=1)
            self.wing_hand_ctrl_get_rot = cmds.getAttr(self.wing_hand_ctrl_name + '.r')
            self.ctrl_list[self.wing_hand_ctrl_name] = {}
            self.ctrl_list[self.wing_hand_ctrl_name]['Trans'] = self.wing_hand_ctrl_get_trans
            self.ctrl_list[self.wing_hand_ctrl_name]['Rot'] = self.wing_hand_ctrl_get_rot

            # WING HAND 2
            self.wing_hand_2_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Hand_2_Tem_" + str(
                self.val)
            self.wing_hand_2_ctrl_name = self.wing_hand_2_common + '_Inner_Ctrl'
            self.wing_hand_2_jnt_name = self.wing_hand_2_common + '_Jnt'
            self.wing_hand_2_ctrl_get_trans = cmds.xform(self.wing_hand_2_ctrl_name, q=1, ws=1, rp=1)
            self.wing_hand_2_ctrl_get_rot = cmds.getAttr(self.wing_hand_2_ctrl_name + '.r')
            self.ctrl_list[self.wing_hand_2_ctrl_name] = {}
            self.ctrl_list[self.wing_hand_2_ctrl_name]['Trans'] = self.wing_hand_2_ctrl_get_trans
            self.ctrl_list[self.wing_hand_2_ctrl_name]['Rot'] = self.wing_hand_2_ctrl_get_rot

            # WING BRAMCH 1 1
            self.wing_branch_1_1_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_1_1_Tem_" + str(
                self.val)
            self.wing_branch_1_1_ctrl_name = self.wing_branch_1_1_common + '_Inner_Ctrl'
            self.wing_branch_1_1_jnt_name = self.wing_branch_1_1_common + '_Jnt'
            self.wing_branch_1_1_ctrl_get_trans = cmds.xform(self.wing_branch_1_1_ctrl_name, q=1, ws=1, rp=1)
            self.wing_branch_1_1_ctrl_get_rot = cmds.getAttr(self.wing_branch_1_1_ctrl_name + '.r')
            self.ctrl_list[self.wing_branch_1_1_ctrl_name] = {}
            self.ctrl_list[self.wing_branch_1_1_ctrl_name]['Trans'] = self.wing_branch_1_1_ctrl_get_trans
            self.ctrl_list[self.wing_branch_1_1_ctrl_name]['Rot'] = self.wing_branch_1_1_ctrl_get_rot

            # WING BRAMCH 1 2
            self.wing_branch_1_2_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_1_2_Tem_" + str(
                self.val)
            self.wing_branch_1_2_ctrl_name = self.wing_branch_1_2_common + '_Inner_Ctrl'
            self.wing_branch_1_2_jnt_name = self.wing_branch_1_2_common + '_Jnt'
            self.wing_branch_1_2_ctrl_get_trans = cmds.xform(self.wing_branch_1_2_ctrl_name, q=1, ws=1, rp=1)
            self.wing_branch_1_2_ctrl_get_rot = cmds.getAttr(self.wing_branch_1_2_ctrl_name + '.r')
            self.ctrl_list[self.wing_branch_1_2_ctrl_name] = {}
            self.ctrl_list[self.wing_branch_1_2_ctrl_name]['Trans'] = self.wing_branch_1_2_ctrl_get_trans
            self.ctrl_list[self.wing_branch_1_2_ctrl_name]['Rot'] = self.wing_branch_1_2_ctrl_get_rot

            # WING BRAMCH 1 3
            self.wing_branch_1_3_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_1_3_Tem_" + str(
                self.val)
            self.wing_branch_1_3_ctrl_name = self.wing_branch_1_3_common + '_Inner_Ctrl'
            self.wing_branch_1_3_jnt_name = self.wing_branch_1_3_common + '_Jnt'
            self.wing_branch_1_3_ctrl_get_trans = cmds.xform(self.wing_branch_1_3_ctrl_name, q=1, ws=1, rp=1)
            self.wing_branch_1_3_ctrl_get_rot = cmds.getAttr(self.wing_branch_1_3_ctrl_name + '.r')
            self.ctrl_list[self.wing_branch_1_3_ctrl_name] = {}
            self.ctrl_list[self.wing_branch_1_3_ctrl_name]['Trans'] = self.wing_branch_1_3_ctrl_get_trans
            self.ctrl_list[self.wing_branch_1_3_ctrl_name]['Rot'] = self.wing_branch_1_3_ctrl_get_rot

            # WING BRAMCH 1 4
            self.wing_branch_1_4_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_1_4_Tem_" + str(
                self.val)
            self.wing_branch_1_4_ctrl_name = self.wing_branch_1_4_common + '_Inner_Ctrl'
            self.wing_branch_1_4_jnt_name = self.wing_branch_1_4_common + '_Jnt'
            self.wing_branch_1_4_ctrl_get_trans = cmds.xform(self.wing_branch_1_4_ctrl_name, q=1, ws=1, rp=1)
            self.wing_branch_1_4_ctrl_get_rot = cmds.getAttr(self.wing_branch_1_4_ctrl_name + '.r')
            self.ctrl_list[self.wing_branch_1_4_ctrl_name] = {}
            self.ctrl_list[self.wing_branch_1_4_ctrl_name]['Trans'] = self.wing_branch_1_4_ctrl_get_trans
            self.ctrl_list[self.wing_branch_1_4_ctrl_name]['Rot'] = self.wing_branch_1_4_ctrl_get_rot

            # WING BRAMCH 2 1
            self.wing_branch_2_1_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_2_1_Tem_" + str(
                self.val)
            self.wing_branch_2_1_ctrl_name = self.wing_branch_2_1_common + '_Inner_Ctrl'
            self.wing_branch_2_1_jnt_name = self.wing_branch_2_1_common + '_Jnt'
            self.wing_branch_2_1_ctrl_get_trans = cmds.xform(self.wing_branch_2_1_ctrl_name, q=1, ws=1, rp=1)
            self.wing_branch_2_1_ctrl_get_rot = cmds.getAttr(self.wing_branch_2_1_ctrl_name + '.r')
            self.ctrl_list[self.wing_branch_2_1_ctrl_name] = {}
            self.ctrl_list[self.wing_branch_2_1_ctrl_name]['Trans'] = self.wing_branch_2_1_ctrl_get_trans
            self.ctrl_list[self.wing_branch_2_1_ctrl_name]['Rot'] = self.wing_branch_2_1_ctrl_get_rot

            # WING BRAMCH 2 2
            self.wing_branch_2_2_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_2_2_Tem_" + str(
                self.val)
            self.wing_branch_2_2_ctrl_name = self.wing_branch_2_2_common + '_Inner_Ctrl'
            self.wing_branch_2_2_jnt_name = self.wing_branch_2_2_common + '_Jnt'
            self.wing_branch_2_2_ctrl_get_trans = cmds.xform(self.wing_branch_2_2_ctrl_name, q=1, ws=1, rp=1)
            self.wing_branch_2_2_ctrl_get_rot = cmds.getAttr(self.wing_branch_2_2_ctrl_name + '.r')
            self.ctrl_list[self.wing_branch_2_2_ctrl_name] = {}
            self.ctrl_list[self.wing_branch_2_2_ctrl_name]['Trans'] = self.wing_branch_2_2_ctrl_get_trans
            self.ctrl_list[self.wing_branch_2_2_ctrl_name]['Rot'] = self.wing_branch_2_2_ctrl_get_rot

            # WING BRAMCH 2 3
            self.wing_branch_2_3_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_2_3_Tem_" + str(
                self.val)
            self.wing_branch_2_3_ctrl_name = self.wing_branch_2_3_common + '_Inner_Ctrl'
            self.wing_branch_2_3_jnt_name = self.wing_branch_2_3_common + '_Jnt'
            self.wing_branch_2_3_ctrl_get_trans = cmds.xform(self.wing_branch_2_3_ctrl_name, q=1, ws=1, rp=1)
            self.wing_branch_2_3_ctrl_get_rot = cmds.getAttr(self.wing_branch_2_3_ctrl_name + '.r')
            self.ctrl_list[self.wing_branch_2_3_ctrl_name] = {}
            self.ctrl_list[self.wing_branch_2_3_ctrl_name]['Trans'] = self.wing_branch_2_3_ctrl_get_trans
            self.ctrl_list[self.wing_branch_2_3_ctrl_name]['Rot'] = self.wing_branch_2_3_ctrl_get_rot

            # WING BRAMCH 2 4
            self.wing_branch_2_4_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_2_4_Tem_" + str(
                self.val)
            self.wing_branch_2_4_ctrl_name = self.wing_branch_2_4_common + '_Inner_Ctrl'
            self.wing_branch_2_4_jnt_name = self.wing_branch_2_4_common + '_Jnt'
            self.wing_branch_2_4_ctrl_get_trans = cmds.xform(self.wing_branch_2_4_ctrl_name, q=1, ws=1, rp=1)
            self.wing_branch_2_4_ctrl_get_rot = cmds.getAttr(self.wing_branch_2_4_ctrl_name + '.r')
            self.ctrl_list[self.wing_branch_2_4_ctrl_name] = {}
            self.ctrl_list[self.wing_branch_2_4_ctrl_name]['Trans'] = self.wing_branch_2_4_ctrl_get_trans
            self.ctrl_list[self.wing_branch_2_4_ctrl_name]['Rot'] = self.wing_branch_2_4_ctrl_get_rot

            # WING BRAMCH 3 1
            self.wing_branch_3_1_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_3_1_Tem_" + str(
                self.val)
            self.wing_branch_3_1_ctrl_name = self.wing_branch_3_1_common + '_Inner_Ctrl'
            self.wing_branch_3_1_jnt_name = self.wing_branch_3_1_common + '_Jnt'
            self.wing_branch_3_1_ctrl_get_trans = cmds.xform(self.wing_branch_3_1_ctrl_name, q=1, ws=1, rp=1)
            self.wing_branch_3_1_ctrl_get_rot = cmds.getAttr(self.wing_branch_3_1_ctrl_name + '.r')
            self.ctrl_list[self.wing_branch_3_1_ctrl_name] = {}
            self.ctrl_list[self.wing_branch_3_1_ctrl_name]['Trans'] = self.wing_branch_3_1_ctrl_get_trans
            self.ctrl_list[self.wing_branch_3_1_ctrl_name]['Rot'] = self.wing_branch_3_1_ctrl_get_rot

            # WING BRAMCH 3 2
            self.wing_branch_3_2_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_3_2_Tem_" + str(
                self.val)
            self.wing_branch_3_2_ctrl_name = self.wing_branch_3_2_common + '_Inner_Ctrl'
            self.wing_branch_3_2_jnt_name = self.wing_branch_3_2_common + '_Jnt'
            self.wing_branch_3_2_ctrl_get_trans = cmds.xform(self.wing_branch_3_2_ctrl_name, q=1, ws=1, rp=1)
            self.wing_branch_3_2_ctrl_get_rot = cmds.getAttr(self.wing_branch_3_2_ctrl_name + '.r')
            self.ctrl_list[self.wing_branch_3_2_ctrl_name] = {}
            self.ctrl_list[self.wing_branch_3_2_ctrl_name]['Trans'] = self.wing_branch_3_2_ctrl_get_trans
            self.ctrl_list[self.wing_branch_3_2_ctrl_name]['Rot'] = self.wing_branch_3_2_ctrl_get_rot

            # WING BRAMCH 3 3
            self.wing_branch_3_3_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_3_3_Tem_" + str(
                self.val)
            self.wing_branch_3_3_ctrl_name = self.wing_branch_3_3_common + '_Inner_Ctrl'
            self.wing_branch_3_3_jnt_name = self.wing_branch_3_3_common + '_Jnt'
            self.wing_branch_3_3_ctrl_get_trans = cmds.xform(self.wing_branch_3_3_ctrl_name, q=1, ws=1, rp=1)
            self.wing_branch_3_3_ctrl_get_rot = cmds.getAttr(self.wing_branch_3_3_ctrl_name + '.r')
            self.ctrl_list[self.wing_branch_3_3_ctrl_name] = {}
            self.ctrl_list[self.wing_branch_3_3_ctrl_name]['Trans'] = self.wing_branch_3_3_ctrl_get_trans
            self.ctrl_list[self.wing_branch_3_3_ctrl_name]['Rot'] = self.wing_branch_3_3_ctrl_get_rot

            # WING BRAMCH 3 4
            self.wing_branch_3_4_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_3_4_Tem_" + str(
                self.val)
            self.wing_branch_3_4_ctrl_name = self.wing_branch_3_4_common + '_Inner_Ctrl'
            self.wing_branch_3_4_jnt_name = self.wing_branch_3_4_common + '_Jnt'
            self.wing_branch_3_4_ctrl_get_trans = cmds.xform(self.wing_branch_3_4_ctrl_name, q=1, ws=1, rp=1)
            self.wing_branch_3_4_ctrl_get_rot = cmds.getAttr(self.wing_branch_3_4_ctrl_name + '.r')
            self.ctrl_list[self.wing_branch_3_4_ctrl_name] = {}
            self.ctrl_list[self.wing_branch_3_4_ctrl_name]['Trans'] = self.wing_branch_3_4_ctrl_get_trans
            self.ctrl_list[self.wing_branch_3_4_ctrl_name]['Rot'] = self.wing_branch_3_4_ctrl_get_rot

            # WING BRAMCH 4 1
            self.wing_branch_4_1_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_4_1_Tem_" + str(
                self.val)
            self.wing_branch_4_1_ctrl_name = self.wing_branch_4_1_common + '_Inner_Ctrl'
            self.wing_branch_4_1_jnt_name = self.wing_branch_4_1_common + '_Jnt'
            self.wing_branch_4_1_ctrl_get_trans = cmds.xform(self.wing_branch_4_1_ctrl_name, q=1, ws=1, rp=1)
            self.wing_branch_4_1_ctrl_get_rot = cmds.getAttr(self.wing_branch_4_1_ctrl_name + '.r')
            self.ctrl_list[self.wing_branch_4_1_ctrl_name] = {}
            self.ctrl_list[self.wing_branch_4_1_ctrl_name]['Trans'] = self.wing_branch_4_1_ctrl_get_trans
            self.ctrl_list[self.wing_branch_4_1_ctrl_name]['Rot'] = self.wing_branch_4_1_ctrl_get_rot

            # WING BRAMCH 4 2
            self.wing_branch_4_2_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_4_2_Tem_" + str(
                self.val)
            self.wing_branch_4_2_ctrl_name = self.wing_branch_4_2_common + '_Inner_Ctrl'
            self.wing_branch_4_2_jnt_name = self.wing_branch_4_2_common + '_Jnt'
            self.wing_branch_4_2_ctrl_get_trans = cmds.xform(self.wing_branch_4_2_ctrl_name, q=1, ws=1, rp=1)
            self.wing_branch_4_2_ctrl_get_rot = cmds.getAttr(self.wing_branch_4_2_ctrl_name + '.r')
            self.ctrl_list[self.wing_branch_4_2_ctrl_name] = {}
            self.ctrl_list[self.wing_branch_4_2_ctrl_name]['Trans'] = self.wing_branch_4_2_ctrl_get_trans
            self.ctrl_list[self.wing_branch_4_2_ctrl_name]['Rot'] = self.wing_branch_4_2_ctrl_get_rot

            # WING BRAMCH 4 4
            self.wing_branch_4_3_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_4_3_Tem_" + str(
                self.val)
            self.wing_branch_4_3_ctrl_name = self.wing_branch_4_3_common + '_Inner_Ctrl'
            self.wing_branch_4_3_jnt_name = self.wing_branch_4_3_common + '_Jnt'
            self.wing_branch_4_3_ctrl_get_trans = cmds.xform(self.wing_branch_4_3_ctrl_name, q=1, ws=1, rp=1)
            self.wing_branch_4_3_ctrl_get_rot = cmds.getAttr(self.wing_branch_4_3_ctrl_name + '.r')
            self.ctrl_list[self.wing_branch_4_3_ctrl_name] = {}
            self.ctrl_list[self.wing_branch_4_3_ctrl_name]['Trans'] = self.wing_branch_4_3_ctrl_get_trans
            self.ctrl_list[self.wing_branch_4_3_ctrl_name]['Rot'] = self.wing_branch_4_3_ctrl_get_rot

            # WING BRAMCH 4 4
            self.wing_branch_4_4_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_4_4_Tem_" + str(
                self.val)
            self.wing_branch_4_4_ctrl_name = self.wing_branch_4_4_common + '_Inner_Ctrl'
            self.wing_branch_4_4_jnt_name = self.wing_branch_4_4_common + '_Jnt'
            self.wing_branch_4_4_ctrl_get_trans = cmds.xform(self.wing_branch_4_4_ctrl_name, q=1, ws=1, rp=1)
            self.wing_branch_4_4_ctrl_get_rot = cmds.getAttr(self.wing_branch_4_4_ctrl_name + '.r')
            self.ctrl_list[self.wing_branch_4_4_ctrl_name] = {}
            self.ctrl_list[self.wing_branch_4_4_ctrl_name]['Trans'] = self.wing_branch_4_4_ctrl_get_trans
            self.ctrl_list[self.wing_branch_4_4_ctrl_name]['Rot'] = self.wing_branch_4_4_ctrl_get_rot

            # UPPER ARM GEO
            # Template_L_Wing_Dragon_Upper_0_Tem_1_Geo
            self.upper_arm_jnt_list = {}
            geo_name = self.prefix_name + "_" + self.wing_side + "_Wing_Dragon_Upper_*_Tem_" + str(self.val) + '_Geo'
            # Template_L_Wing_Dragon_Upper_Tem_1_Geo
            upper_hand_common = self.prefix_name + "_" + self.wing_side + "_Wing_Dragon_Upper_to_lBow_Tem_" + str(
                self.val)
            upper_hand_ctrl = upper_hand_common + '_Geo'
            self.upper_hand_jnt = upper_hand_common + '_Jnt'
            if cmds.objExists(geo_name):
                cmds.select(geo_name)
                if cmds.objExists(upper_hand_ctrl):
                    cmds.select(upper_hand_ctrl, d=True)
                sel_geo = cmds.ls(sl=True)
                a = 0
                while a < len(sel_geo):
                    # get the position
                    sel_geo_get_trans = cmds.xform(sel_geo[a], q=1, ws=1, rp=1)
                    sel_geo_get_rot = cmds.getAttr(sel_geo[a] + '.r')
                    split_geo = sel_geo[a].split('_Geo')[0]
                    jnt_name = split_geo + '_Jnt'
                    self.upper_arm_jnt_list[sel_geo[a]] = {}
                    self.upper_arm_jnt_list[sel_geo[a]]['Trans'] = sel_geo_get_trans
                    self.upper_arm_jnt_list[sel_geo[a]]['Rot'] = sel_geo_get_rot
                    a += 1

            # LOWER JNT
            self.lower_arm_jnt_list = {}
            geo_name = self.prefix_name + "_" + self.wing_side + "_Wing_Dragon_Lower_*_Tem_" + str(self.val) + '_Geo'
            if cmds.objExists(geo_name):
                cmds.select(geo_name)
                sel_geo = cmds.ls(sl=True)
                a = 0
                while a < len(sel_geo):
                    # get the position
                    sel_geo_get_trans = cmds.xform(sel_geo[a], q=1, ws=1, rp=1)
                    sel_geo_get_rot = cmds.getAttr(sel_geo[a] + '.r')
                    split_geo = sel_geo[a].split('_Geo')[0]
                    jnt_name = split_geo + '_Jnt'

                    self.lower_arm_jnt_list[sel_geo[a]] = {}
                    self.lower_arm_jnt_list[sel_geo[a]]['Trans'] = sel_geo_get_trans
                    self.lower_arm_jnt_list[sel_geo[a]]['Rot'] = sel_geo_get_rot
                    a += 1

            # GET THE FINGER
            # Template_L_Wing_Dragon_Finger_1_1_Tem_1_Outer_Ctrl
            self.finger_list = []
            outer_finger_ctrl = self.prefix_name + "_" + self.wing_side + "_Wing_Dragon_Finger_*_1_Tem_" + str(
                self.val) + '_Inner_Ctrl'
            if cmds.objExists(outer_finger_ctrl):
                cmds.select(outer_finger_ctrl)
                sel_finger = cmds.ls(sl=True)
                for each_finger in sel_finger:
                    self.finger_list.append(each_finger)


        elif self.type == 'Bird':
            # Base
            self.base_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Base_Tem_" + str(
                self.val)
            self.base_ctrl_name = self.base_common + '_Inner_Ctrl'
            self.base_jnt_name = self.base_common + '_Jnt'
            self.base_ctrl_get_trans = cmds.xform(self.base_ctrl_name, q=1, ws=1, rp=1)
            self.base_ctrl_get_rot = cmds.getAttr(self.base_ctrl_name + '.r')

            # upper Pos
            self.upper_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Upper_Tem_" + str(
                self.val)
            self.upper_ctrl_name = self.upper_common + '_Inner_Ctrl'
            self.upper_jnt_name = self.upper_common + '_Jnt'
            self.upper_ctrl_get_trans = cmds.xform(self.upper_ctrl_name, q=1, ws=1, rp=1)
            self.upper_ctrl_get_rot = cmds.getAttr(self.upper_ctrl_name + '.r')
            self.ctrl_list[self.upper_ctrl_name] = {}
            self.ctrl_list[self.upper_ctrl_name]['Trans'] = self.upper_ctrl_get_trans
            self.ctrl_list[self.upper_ctrl_name]['Rot'] = self.upper_ctrl_get_rot

            # shoulder Pos
            self.shoulder_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Shoulder_Tem_" + str(
                self.val)
            self.shoulder_ctrl_name = self.shoulder_common + '_Inner_Ctrl'
            self.shoulder_jnt_name = self.shoulder_common + '_Jnt'
            self.shoulder_ctrl_get_trans = cmds.xform(self.shoulder_ctrl_name, q=1, ws=1, rp=1)
            self.shoulder_ctrl_get_rot = cmds.getAttr(self.shoulder_ctrl_name + '.r')
            self.ctrl_list[self.shoulder_ctrl_name] = {}
            self.ctrl_list[self.shoulder_ctrl_name]['Trans'] = self.shoulder_ctrl_get_trans
            self.ctrl_list[self.shoulder_ctrl_name]['Rot'] = self.shoulder_ctrl_get_rot

            # lbow Pos
            self.lbow_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_lBow_Tem_" + str(
                self.val)
            self.lbow_ctrl_name = self.lbow_common + '_Inner_Ctrl'
            self.lbow_jnt_name = self.lbow_common + '_Jnt'
            self.lbow_ctrl_get_trans = cmds.xform(self.lbow_ctrl_name, q=1, ws=1, rp=1)
            self.lbow_ctrl_get_rot = cmds.getAttr(self.lbow_ctrl_name + '.r')
            self.ctrl_list[self.lbow_ctrl_name] = {}
            self.ctrl_list[self.lbow_ctrl_name]['Trans'] = self.lbow_ctrl_get_trans
            self.ctrl_list[self.lbow_ctrl_name]['Rot'] = self.lbow_ctrl_get_rot

            # hand Pos
            self.hand_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Hand_Tem_" + str(
                self.val)
            self.hand_ctrl_name = self.hand_common + '_Inner_Ctrl'
            self.hand_jnt_name = self.hand_common + '_Jnt'
            self.hand_ctrl_get_trans = cmds.xform(self.hand_ctrl_name, q=1, ws=1, rp=1)
            self.hand_ctrl_get_rot = cmds.getAttr(self.hand_ctrl_name + '.r')
            self.ctrl_list[self.hand_ctrl_name] = {}
            self.ctrl_list[self.hand_ctrl_name]['Trans'] = self.hand_ctrl_get_trans
            self.ctrl_list[self.hand_ctrl_name]['Rot'] = self.hand_ctrl_get_rot

            # hand End Pos
            self.hand_end_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Hand_End_Tem_" + str(
                self.val)
            self.hand_end_ctrl_name = self.hand_end_common + '_Inner_Ctrl'
            self.hand_end_jnt_name = self.hand_end_common + '_Jnt'
            self.hand_end_get_trans = cmds.xform(self.hand_end_ctrl_name, q=1, ws=1, rp=1)
            self.hand_end_get_rot = cmds.getAttr(self.hand_end_ctrl_name + '.r')
            self.ctrl_list[self.hand_end_ctrl_name] = {}
            self.ctrl_list[self.hand_end_ctrl_name]['Trans'] = self.hand_end_get_trans
            self.ctrl_list[self.hand_end_ctrl_name]['Rot'] = self.hand_end_get_rot

            # _Wing_Feather_Bird_Shoulder_
            self.feather_shoulder = []
            # Template_L_Wing_Feather_Bird_Shoulder_1_1_Tem_1_Outer_Ctrl
            outer_finger_ctrl = self.prefix_name + "_" + self.wing_side + "_Wing_Feather_Bird_Shoulder_*_1_Tem_" + str(
                self.val) + '_Inner_Ctrl'
            if cmds.objExists(outer_finger_ctrl):
                cmds.select(outer_finger_ctrl)
                sel_finger = cmds.ls(sl=True)
                for each_finger in sel_finger:
                    self.feather_shoulder.append(each_finger)

            # _Wing_Feather_Bird_lBow_
            self.feather_lbow = []
            outer_finger_ctrl = self.prefix_name + "_" + self.wing_side + "_Wing_Feather_Bird_lBow_*_1_Tem_" + str(
                self.val) + '_Inner_Ctrl'
            if cmds.objExists(outer_finger_ctrl):
                cmds.select(outer_finger_ctrl)
                sel_finger = cmds.ls(sl=True)
                for each_finger in sel_finger:
                    self.feather_lbow.append(each_finger)

            # _Wing_Feather_Bird_Hand_
            self.feather_hand = []
            outer_finger_ctrl = self.prefix_name + "_" + self.wing_side + "_Wing_Feather_Bird_Hand_*_1_Tem_" + str(
                self.val) + '_Inner_Ctrl'
            if cmds.objExists(outer_finger_ctrl):
                cmds.select(outer_finger_ctrl)
                sel_finger = cmds.ls(sl=True)
                for each_finger in sel_finger:
                    self.feather_hand.append(each_finger)

            # Template_L_Wing_Bird_Upper_0_Tem_1_Geo
            # Template_L_Wing_Bird_Upper_Tem_1_Geo
            self.upper_arm_jnt_list = {}
            geo_name = self.prefix_name + "_" + self.wing_side + "_Wing_Bird_Upper_*_Tem_" + str(self.val) + '_Geo'
            # Template_L_Arm_Upper_Hand_Tem_1_Jnt
            upper_hand_common = self.prefix_name + "_" + self.wing_side + "_Wing_Bird_Upper_to_Shoulder_Tem_" + str(
                self.val)
            upper_hand_ctrl = upper_hand_common + '_Geo'
            self.upper_hand_jnt = upper_hand_common + '_Jnt'
            if cmds.objExists(geo_name):
                cmds.select(geo_name)
                if cmds.objExists(upper_hand_ctrl):
                    cmds.select(upper_hand_ctrl, d=True)
                sel_geo = cmds.ls(sl=True)
                a = 0
                while a < len(sel_geo):
                    # get the position
                    sel_geo_get_trans = cmds.xform(sel_geo[a], q=1, ws=1, rp=1)
                    sel_geo_get_rot = cmds.getAttr(sel_geo[a] + '.r')
                    split_geo = sel_geo[a].split('_Geo')[0]
                    jnt_name = split_geo + '_Jnt'

                    self.upper_arm_jnt_list[sel_geo[a]] = {}
                    self.upper_arm_jnt_list[sel_geo[a]]['Trans'] = sel_geo_get_trans
                    self.upper_arm_jnt_list[sel_geo[a]]['Rot'] = sel_geo_get_rot
                    a += 1

            # Template_L_Wing_Bird_Lower_0_Tem_1_Geo
            self.lower_arm_jnt_list = {}
            geo_name = self.prefix_name + "_" + self.wing_side + "_Wing_Bird_Lower_*_Tem_" + str(self.val) + '_Geo'
            geo_lower_2_name = self.prefix_name + "_" + self.wing_side + "_Wing_Bird_Lower_2_*_Tem_" + str(
                self.val) + '_Geo'
            # Template_L_Arm_Upper_Hand_Tem_1_Jnt
            if cmds.objExists(geo_name):
                cmds.select(geo_name)
                if cmds.objExists(geo_lower_2_name):
                    cmds.select(geo_lower_2_name, d=True)
                sel_geo = cmds.ls(sl=True)
                a = 0
                while a < len(sel_geo):
                    # get the position
                    sel_geo_get_trans = cmds.xform(sel_geo[a], q=1, ws=1, rp=1)
                    sel_geo_get_rot = cmds.getAttr(sel_geo[a] + '.r')
                    split_geo = sel_geo[a].split('_Geo')[0]
                    jnt_name = split_geo + '_Jnt'

                    self.lower_arm_jnt_list[sel_geo[a]] = {}
                    self.lower_arm_jnt_list[sel_geo[a]]['Trans'] = sel_geo_get_trans
                    self.lower_arm_jnt_list[sel_geo[a]]['Rot'] = sel_geo_get_rot
                    a += 1

            # Template_L_Wing_Bird_Lower_2_0_Tem_1_Geo
            self.lower_arm_2_jnt_list = {}
            geo_name = self.prefix_name + "_" + self.wing_side + "_Wing_Bird_Lower_2_*_Tem_" + str(self.val) + '_Geo'
            # Template_L_Arm_Upper_Hand_Tem_1_Jnt
            if cmds.objExists(geo_name):
                cmds.select(geo_name)
                sel_geo = cmds.ls(sl=True)
                a = 0
                while a < len(sel_geo):
                    # get the position
                    sel_geo_get_trans = cmds.xform(sel_geo[a], q=1, ws=1, rp=1)
                    sel_geo_get_rot = cmds.getAttr(sel_geo[a] + '.r')
                    split_geo = sel_geo[a].split('_Geo')[0]
                    jnt_name = split_geo + '_Jnt'

                    self.lower_arm_2_jnt_list[sel_geo[a]] = {}
                    self.lower_arm_2_jnt_list[sel_geo[a]]['Trans'] = sel_geo_get_trans
                    self.lower_arm_2_jnt_list[sel_geo[a]]['Rot'] = sel_geo_get_rot
                    a += 1

    def wing_create(self):
        # get the no of the human main grp
        self.grp_list = ['Wing_Grp']
        for each_grp in self.grp_list:
            # list of the all children
            if cmds.objExists(each_grp):
                children_list = cmds.listRelatives(each_grp, children=True)
                for each_child in children_list:
                    # get all the controller data
                    self.wing_data(each_child)

                    # FINAL THE ARM
                    self.final_wing_def()

    def wing_data(self, children_name):
        split_name = children_name.split('_')
        # Template_L_Wing_Dragon_Tem_1_Main_Grp
        self.prefix_name = split_name[0]
        self.wing_side = split_name[1]
        self.type = split_name[3]
        self.val = split_name[5]

        # get each ctrl position data
        self.get_each_pos_data(children_name)
        pass

    def get_each_pos_data(self, common_name):
        self.ctrl_list = {}
        self.common_list = []
        self.wing_branch_list = []

        # UPPER
        # Template_L_Wing_Dragon_Upper_Tem_1_Inner_Ctrl
        self.upper_wing_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Upper_Tem_" + str(
            self.val)
        self.upper_wing_inner_ctrl, self.upper_wing_jnt, self.upper_wing_ik_jnt, self.upper_wing_fk_jnt, \
        self.upper_wing_result_jnt = self.get_data_variable(self.upper_wing_common)

        # LBOW
        # Template_L_Wing_Dragon_lBow_Tem_1_Inner_Ctrl
        self.lbow_wing_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_lBow_Tem_" + str(
            self.val)
        self.lbow_wing_inner_ctrl, self.lbow_wing_jnt, self.lbow_wing_ik_jnt, self.lbow_wing_fk_jnt, \
        self.lbow_wing_result_jnt = self.get_data_variable(self.lbow_wing_common)

        # HAND
        # Template_L_Wing_Dragon_Hand_Tem_1_Inner_Ctrl
        self.hand_wing_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Hand_Tem_" + str(
            self.val)
        self.hand_wing_inner_ctrl, self.hand_wing_jnt, self.hand_wing_ik_jnt, self.hand_wing_fk_jnt, \
        self.hand_wing_result_jnt = self.get_data_variable(self.hand_wing_common)

        # HAND 2
        # Template_L_Wing_Dragon_Hand_2_Tem_1_Inner_Ctrl
        self.hand_2_wing_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Hand_2_Tem_" + str(
            self.val)
        self.hand_2_wing_inner_ctrl, self.hand_2_wing_jnt, self.hand_2_wing_ik_jnt, self.hand_2_wing_fk_jnt, \
        self.hand_2_wing_result_jnt = self.get_data_variable(self.hand_2_wing_common)

        self.shoulder_wing_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Shoulder_Tem_" + str(
            self.val)

        # BRANCH 1 1
        # Template_L_Wing_Dragon_Branch_1_1_Tem_1_Inner_Ctrl
        self.branch_1_1_wing_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_1_1_Tem_" + str(
            self.val)
        self.branch_1_1_wing_result_jnt = self.branch_1_1_wing_common + '_Result_Jnt'
        self.wing_branch_list.append(self.branch_1_1_wing_common)
        self.get_transform_rot_val(self.branch_1_1_wing_common + '_Inner_Ctrl')

        # BRANCH 1 2
        # Template_L_Wing_Dragon_Branch_1_2_Tem_1_Inner_Ctrl
        self.branch_1_2_wing_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_1_2_Tem_" + str(
            self.val)
        self.branch_1_2_wing_result_jnt = self.branch_1_2_wing_common + '_Result_Jnt'
        self.wing_branch_list.append(self.branch_1_2_wing_common)
        self.get_transform_rot_val(self.branch_1_2_wing_common + '_Inner_Ctrl')

        # BRANCH 1 3
        # Template_L_Wing_Dragon_Branch_1_3_Tem_1_Inner_Ctrl
        self.branch_1_3_wing_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_1_3_Tem_" + str(
            self.val)
        self.branch_1_3_wing_result_jnt = self.branch_1_3_wing_common + '_Result_Jnt'
        self.wing_branch_list.append(self.branch_1_3_wing_common)
        self.get_transform_rot_val(self.branch_1_3_wing_common + '_Inner_Ctrl')

        # BRANCH 1 4
        # Template_L_Wing_Dragon_Branch_1_4_Tem_1_Inner_Ctrl
        self.branch_1_4_wing_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_1_4_Tem_" + str(
            self.val)
        self.branch_1_4_wing_result_jnt = self.branch_1_4_wing_common + '_Result_Jnt'
        self.wing_branch_list.append(self.branch_1_4_wing_common)
        self.get_transform_rot_val(self.branch_1_4_wing_common + '_Inner_Ctrl')

        # BRANCH 2 1
        # Template_L_Wing_Dragon_Branch_2_1_Tem_1_Inner_Ctrl
        self.branch_2_1_wing_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_2_1_Tem_" + str(
            self.val)
        self.branch_2_1_wing_result_jnt = self.branch_2_1_wing_common + '_Result_Jnt'
        self.wing_branch_list.append(self.branch_2_1_wing_common)
        self.get_transform_rot_val(self.branch_2_1_wing_common + '_Inner_Ctrl')

        # BRANCH 2 2
        # Template_L_Wing_Dragon_Branch_2_2_Tem_1_Inner_Ctrl
        self.branch_2_2_wing_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_2_2_Tem_" + str(
            self.val)
        self.branch_2_2_wing_result_jnt = self.branch_2_2_wing_common + '_Result_Jnt'
        self.wing_branch_list.append(self.branch_2_2_wing_common)
        self.get_transform_rot_val(self.branch_2_2_wing_common + '_Inner_Ctrl')

        # BRANCH 2 3
        # Template_L_Wing_Dragon_Branch_2_3_Tem_1_Inner_Ctrl
        self.branch_2_3_wing_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_2_3_Tem_" + str(
            self.val)
        self.branch_2_3_wing_result_jnt = self.branch_2_3_wing_common + '_Result_Jnt'
        self.wing_branch_list.append(self.branch_2_3_wing_common)
        self.get_transform_rot_val(self.branch_2_3_wing_common + '_Inner_Ctrl')

        # BRANCH 2 4
        # Template_L_Wing_Dragon_Branch_2_4_Tem_1_Inner_Ctrl
        self.branch_2_4_wing_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_2_4_Tem_" + str(
            self.val)
        self.branch_2_4_wing_result_jnt = self.branch_2_4_wing_common + '_Result_Jnt'
        self.wing_branch_list.append(self.branch_2_4_wing_common)
        self.get_transform_rot_val(self.branch_2_4_wing_common + '_Inner_Ctrl')

        # BRANCH 3 1
        # Template_L_Wing_Dragon_Branch_3_1_Tem_1_Inner_Ctrl
        self.branch_3_1_wing_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_3_1_Tem_" + str(
            self.val)
        self.branch_3_1_wing_result_jnt = self.branch_3_1_wing_common + '_Result_Jnt'
        self.wing_branch_list.append(self.branch_3_1_wing_common)
        self.get_transform_rot_val(self.branch_3_1_wing_common + '_Inner_Ctrl')

        # BRANCH 3 2
        # Template_L_Wing_Dragon_Branch_3_2_Tem_1_Inner_Ctrl
        self.branch_3_2_wing_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_3_2_Tem_" + str(
            self.val)
        self.branch_3_2_wing_result_jnt = self.branch_3_2_wing_common + '_Result_Jnt'
        self.wing_branch_list.append(self.branch_3_2_wing_common)
        self.get_transform_rot_val(self.branch_3_2_wing_common + '_Inner_Ctrl')

        # BRANCH 3 3
        # Template_L_Wing_Dragon_Branch_3_3_Tem_1_Inner_Ctrl
        self.branch_3_3_wing_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_3_3_Tem_" + str(
            self.val)
        self.branch_3_3_wing_result_jnt = self.branch_3_3_wing_common + '_Result_Jnt'
        self.wing_branch_list.append(self.branch_3_3_wing_common)
        self.get_transform_rot_val(self.branch_3_3_wing_common + '_Inner_Ctrl')

        # BRANCH 3 4
        # Template_L_Wing_Dragon_Branch_3_4_Tem_1_Inner_Ctrl
        self.branch_3_4_wing_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_3_4_Tem_" + str(
            self.val)
        self.branch_3_4_wing_result_jnt = self.branch_3_4_wing_common + '_Result_Jnt'
        self.wing_branch_list.append(self.branch_3_4_wing_common)
        self.get_transform_rot_val(self.branch_3_4_wing_common + '_Inner_Ctrl')

        # BRANCH 4 1
        # Template_L_Wing_Dragon_Branch_4_1_Tem_1_Inner_Ctrl
        self.branch_4_1_wing_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_4_1_Tem_" + str(
            self.val)
        self.branch_4_1_wing_result_jnt = self.branch_4_1_wing_common + '_Result_Jnt'
        self.wing_branch_list.append(self.branch_4_1_wing_common)
        self.get_transform_rot_val(self.branch_4_1_wing_common + '_Inner_Ctrl')

        # BRANCH 4 2
        # Template_L_Wing_Dragon_Branch_4_2_Tem_1_Inner_Ctrl
        self.branch_4_2_wing_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_4_2_Tem_" + str(
            self.val)
        self.branch_4_2_wing_result_jnt = self.branch_4_2_wing_common + '_Result_Jnt'
        self.wing_branch_list.append(self.branch_4_2_wing_common)
        self.get_transform_rot_val(self.branch_4_2_wing_common + '_Inner_Ctrl')

        # BRANCH 4 3
        # Template_L_Wing_Dragon_Branch_4_3_Tem_1_Inner_Ctrl
        self.branch_4_3_wing_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_4_3_Tem_" + str(
            self.val)
        self.branch_4_3_wing_result_jnt = self.branch_4_3_wing_common + '_Result_Jnt'
        self.wing_branch_list.append(self.branch_4_3_wing_common)
        self.get_transform_rot_val(self.branch_4_3_wing_common + '_Inner_Ctrl')

        # BRANCH 4 4
        # Template_L_Wing_Dragon_Branch_4_4_Tem_1_Inner_Ctrl
        self.branch_4_4_wing_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Branch_4_4_Tem_" + str(
            self.val)
        self.branch_4_4_wing_result_jnt = self.branch_4_4_wing_common + '_Result_Jnt'
        self.wing_branch_list.append(self.branch_4_4_wing_common)
        self.get_transform_rot_val(self.branch_4_4_wing_common + '_Inner_Ctrl')

    def get_data_variable(self, common_name):
        inner_ctrl = common_name + '_Inner_Ctrl'
        tem_remove_name = self.helper_class.remove_tem(common_name)
        if cmds.objExists(inner_ctrl):
            #
            jnt_name = common_name + '_Jnt'
            ik_name = tem_remove_name + '_Ik_Jnt'
            fk_name = tem_remove_name + '_Fk_Jnt'
            result_name = tem_remove_name + '_Result_Jnt'

            # GET VAL
            get_trans = cmds.xform(inner_ctrl, q=1, ws=1, rp=1)
            get_rot = cmds.getAttr(inner_ctrl + '.r')

            # APPEND THE VALUE
            self.ctrl_list[inner_ctrl] = {}
            self.ctrl_list[inner_ctrl]['Trans'] = get_trans
            self.ctrl_list[inner_ctrl]['Rot'] = get_rot
            self.common_list.append(common_name)
            return inner_ctrl, jnt_name, ik_name, fk_name, result_name

    def get_transform_rot_val(self, inner_ctrl_name, trans=True, rot=True):
        self.ctrl_list[inner_ctrl_name] = {}
        if trans == True and rot == True:
            get_trans = cmds.xform(inner_ctrl_name, q=1, ws=1, rp=1)
            get_rot = cmds.getAttr(inner_ctrl_name + '.r')
            self.ctrl_list[inner_ctrl_name]['Trans'] = get_trans
            self.ctrl_list[inner_ctrl_name]['Rot'] = get_rot
        else:
            if trans == True:
                get_trans = cmds.xform(inner_ctrl_name, q=1, ws=1, rp=1)
                self.ctrl_list[inner_ctrl_name]['Trans'] = get_trans
            if rot == True:
                get_rot = cmds.getAttr(inner_ctrl_name + '.r')
                self.ctrl_list[inner_ctrl_name]['Rot'] = get_rot

    def final_wing_def(self):
        ik_jnt_list = []
        fk_jnt_list = []
        result_jnt_list = []

        root_grp_name = "Root_Grp"
        if cmds.objExists(root_grp_name):
            pass
        else:
            cmds.createNode('transform', n=root_grp_name)

        a = 0
        while a < len(self.common_list):
            common_name = self.helper_class.remove_tem(self.common_list[a])
            ik_jnt_name = common_name + '_Ik_Jnt'
            fk_jnt_name = common_name + '_Fk_Jnt'
            result_jnt_name = common_name + '_Result_Jnt'
            list = [ik_jnt_name, fk_jnt_name, result_jnt_name]
            for each_jnt in list:
                cmds.select(cl=True)
                controller_name = self.common_list[a] + '_Inner_Ctrl'
                cmds.joint(n=each_jnt, p=(self.ctrl_list[controller_name]['Trans'][0],
                                          self.ctrl_list[controller_name]['Trans'][1],
                                          self.ctrl_list[controller_name]['Trans'][2]))
            ik_jnt_list.append(ik_jnt_name)
            fk_jnt_list.append(fk_jnt_name)
            result_jnt_list.append(result_jnt_name)
            a += 1

        a = 0
        while a < len(self.wing_branch_list):
            result_jnt_name = self.wing_branch_list[a] + '_Result_Jnt'
            cmds.select(cl=True)
            controller_name = self.wing_branch_list[a] + '_Inner_Ctrl'
            cmds.joint(n=result_jnt_name, p=(self.ctrl_list[controller_name]['Trans'][0],
                                             self.ctrl_list[controller_name]['Trans'][1],
                                             self.ctrl_list[controller_name]['Trans'][2]))
            result_jnt_list.append(result_jnt_name)
            a += 1

        # parent the joint
        # self.helper_class.maya_parent(self.upper_wing_fk_jnt,self.shoulder_wing_fk_jnt)
        self.helper_class.maya_parent(self.lbow_wing_fk_jnt, self.upper_wing_fk_jnt)
        self.helper_class.maya_parent(self.hand_wing_fk_jnt, self.lbow_wing_fk_jnt)
        self.helper_class.maya_parent(self.hand_2_wing_fk_jnt, self.hand_wing_fk_jnt)

        # self.helper_class.maya_parent(self.upper_wing_ik_jnt,self.shoulder_wing_ik_jnt)
        self.helper_class.maya_parent(self.lbow_wing_ik_jnt, self.upper_wing_ik_jnt)
        self.helper_class.maya_parent(self.hand_wing_ik_jnt, self.lbow_wing_ik_jnt)
        self.helper_class.maya_parent(self.hand_2_wing_ik_jnt, self.hand_wing_ik_jnt)

        # self.helper_class.maya_parent(self.upper_wing_result_jnt,self.shoulder_wing_result_jnt)
        self.helper_class.maya_parent(self.lbow_wing_result_jnt, self.upper_wing_result_jnt)
        self.helper_class.maya_parent(self.hand_wing_result_jnt, self.lbow_wing_result_jnt)
        self.helper_class.maya_parent(self.hand_2_wing_result_jnt, self.hand_wing_result_jnt)
        self.helper_class.maya_parent(self.branch_1_1_wing_result_jnt, self.hand_2_wing_result_jnt)
        self.helper_class.maya_parent(self.branch_1_2_wing_result_jnt, self.branch_1_1_wing_result_jnt)
        self.helper_class.maya_parent(self.branch_1_3_wing_result_jnt, self.branch_1_2_wing_result_jnt)
        self.helper_class.maya_parent(self.branch_1_4_wing_result_jnt, self.branch_1_3_wing_result_jnt)

        self.helper_class.maya_parent(self.branch_2_1_wing_result_jnt, self.hand_2_wing_result_jnt)
        self.helper_class.maya_parent(self.branch_2_2_wing_result_jnt, self.branch_2_1_wing_result_jnt)
        self.helper_class.maya_parent(self.branch_2_3_wing_result_jnt, self.branch_2_2_wing_result_jnt)
        self.helper_class.maya_parent(self.branch_2_4_wing_result_jnt, self.branch_2_3_wing_result_jnt)

        self.helper_class.maya_parent(self.branch_3_1_wing_result_jnt, self.hand_2_wing_result_jnt)
        self.helper_class.maya_parent(self.branch_3_2_wing_result_jnt, self.branch_3_1_wing_result_jnt)
        self.helper_class.maya_parent(self.branch_3_3_wing_result_jnt, self.branch_3_2_wing_result_jnt)
        self.helper_class.maya_parent(self.branch_3_4_wing_result_jnt, self.branch_3_3_wing_result_jnt)

        self.helper_class.maya_parent(self.branch_4_1_wing_result_jnt, self.lbow_wing_result_jnt)
        self.helper_class.maya_parent(self.branch_4_2_wing_result_jnt, self.branch_4_1_wing_result_jnt)
        self.helper_class.maya_parent(self.branch_4_3_wing_result_jnt, self.branch_4_2_wing_result_jnt)
        self.helper_class.maya_parent(self.branch_4_4_wing_result_jnt, self.branch_4_3_wing_result_jnt)

        # Create a Branch Fk Controller
        # BRACH 1 1
        branch_list = [self.branch_1_1_wing_common, self.branch_1_2_wing_common, self.branch_1_3_wing_common,
                       self.branch_2_1_wing_common, self.branch_2_2_wing_common, self.branch_2_3_wing_common,
                       self.branch_3_1_wing_common, self.branch_3_2_wing_common, self.branch_3_3_wing_common,
                       self.branch_4_1_wing_common, self.branch_4_2_wing_common, self.branch_4_3_wing_common]
        a = 0
        for each in branch_list:
            ctrl_name = each + '_Ctrl'
            ctrl_shape_name = ctrl_name + 'Shape'
            result_name = each + '_Result_Jnt'
            self.controller_class.circle_ctrl()
            sel_obj = cmds.ls(sl=True)
            cmds.rename(sel_obj[0], ctrl_name)
            cmds.select(ctrl_shape_name, result_name)
            cmds.parent(r=True, s=True)
            cmds.select(ctrl_name)
            cmds.addAttr(result_name, ln="Stretch", at='double', min=-1, dv=0)
            cmds.setAttr((result_name + ".Stretch"), e=True, keyable=True)
            cmds.delete()

        cmds.setDrivenKeyframe((self.branch_1_2_wing_result_jnt + ".tx"),
                               currentDriver=(self.branch_1_1_wing_result_jnt + ".Stretch"))
        cmds.setAttr((self.branch_1_1_wing_result_jnt + ".Stretch"), -1)
        cmds.setAttr((self.branch_1_2_wing_result_jnt + ".tx"), 0)
        cmds.setDrivenKeyframe((self.branch_1_2_wing_result_jnt + ".tx"),
                               currentDriver=(self.branch_1_1_wing_result_jnt + ".Stretch"))
        mel.eval("selectKey -add -k -f -1 -f 0 %s;" % (self.branch_1_2_wing_result_jnt + "_translateX"))
        mel.eval('setInfinity -poi cycleRelative;')
        cmds.setAttr((self.branch_1_1_wing_result_jnt + ".Stretch"), 0)

        cmds.setDrivenKeyframe((self.branch_1_3_wing_result_jnt + ".tx"),
                               currentDriver=(self.branch_1_2_wing_result_jnt + ".Stretch"))
        cmds.setAttr((self.branch_1_2_wing_result_jnt + ".Stretch"), -1)
        cmds.setAttr((self.branch_1_3_wing_result_jnt + ".tx"), 0)
        cmds.setDrivenKeyframe((self.branch_1_3_wing_result_jnt + ".tx"),
                               currentDriver=(self.branch_1_2_wing_result_jnt + ".Stretch"))
        mel.eval("selectKey -add -k -f -1 -f 0 %s;" % (self.branch_1_3_wing_result_jnt + "_translateX"))
        mel.eval('setInfinity -poi cycleRelative;')
        cmds.setAttr((self.branch_1_2_wing_result_jnt + ".Stretch"), 0)

        cmds.setDrivenKeyframe((self.branch_1_4_wing_result_jnt + ".tx"),
                               currentDriver=(self.branch_1_3_wing_result_jnt + ".Stretch"))
        cmds.setAttr((self.branch_1_3_wing_result_jnt + ".Stretch"), -1)
        cmds.setAttr((self.branch_1_4_wing_result_jnt + ".tx"), 0)
        cmds.setDrivenKeyframe((self.branch_1_4_wing_result_jnt + ".tx"),
                               currentDriver=(self.branch_1_3_wing_result_jnt + ".Stretch"))
        mel.eval("selectKey -add -k -f -1 -f 0 %s;" % (self.branch_1_4_wing_result_jnt + "_translateX"))
        mel.eval('setInfinity -poi cycleRelative;')
        cmds.setAttr((self.branch_1_3_wing_result_jnt + ".Stretch"), 0)

        cmds.setDrivenKeyframe((self.branch_2_2_wing_result_jnt + ".tx"),
                               currentDriver=(self.branch_2_1_wing_result_jnt + ".Stretch"))
        cmds.setAttr((self.branch_2_1_wing_result_jnt + ".Stretch"), -1)
        cmds.setAttr((self.branch_2_2_wing_result_jnt + ".tx"), 0)
        cmds.setDrivenKeyframe((self.branch_2_2_wing_result_jnt + ".tx"),
                               currentDriver=(self.branch_2_1_wing_result_jnt + ".Stretch"))
        mel.eval("selectKey -add -k -f -1 -f 0 %s;" % (self.branch_2_2_wing_result_jnt + "_translateX"))
        mel.eval('setInfinity -poi cycleRelative;')
        cmds.setAttr((self.branch_2_1_wing_result_jnt + ".Stretch"), 0)

        cmds.setDrivenKeyframe((self.branch_2_3_wing_result_jnt + ".tx"),
                               currentDriver=(self.branch_2_2_wing_result_jnt + ".Stretch"))
        cmds.setAttr((self.branch_2_2_wing_result_jnt + ".Stretch"), -1)
        cmds.setAttr((self.branch_2_3_wing_result_jnt + ".tx"), 0)
        cmds.setDrivenKeyframe((self.branch_2_3_wing_result_jnt + ".tx"),
                               currentDriver=(self.branch_2_2_wing_result_jnt + ".Stretch"))
        mel.eval("selectKey -add -k -f -1 -f 0 %s;" % (self.branch_2_3_wing_result_jnt + "_translateX"))
        mel.eval('setInfinity -poi cycleRelative;')
        cmds.setAttr((self.branch_2_2_wing_result_jnt + ".Stretch"), 0)

        cmds.setDrivenKeyframe((self.branch_2_4_wing_result_jnt + ".tx"),
                               currentDriver=(self.branch_2_3_wing_result_jnt + ".Stretch"))
        cmds.setAttr((self.branch_2_3_wing_result_jnt + ".Stretch"), -1)
        cmds.setAttr((self.branch_2_4_wing_result_jnt + ".tx"), 0)
        cmds.setDrivenKeyframe((self.branch_2_4_wing_result_jnt + ".tx"),
                               currentDriver=(self.branch_2_3_wing_result_jnt + ".Stretch"))
        mel.eval("selectKey -add -k -f -1 -f 0 %s;" % (self.branch_2_4_wing_result_jnt + "_translateX"))
        mel.eval('setInfinity -poi cycleRelative;')
        cmds.setAttr((self.branch_2_3_wing_result_jnt + ".Stretch"), 0)

        cmds.setDrivenKeyframe((self.branch_3_2_wing_result_jnt + ".tx"),
                               currentDriver=(self.branch_3_1_wing_result_jnt + ".Stretch"))
        cmds.setAttr((self.branch_3_1_wing_result_jnt + ".Stretch"), -1)
        cmds.setAttr((self.branch_3_2_wing_result_jnt + ".tx"), 0)
        cmds.setDrivenKeyframe((self.branch_3_2_wing_result_jnt + ".tx"),
                               currentDriver=(self.branch_3_1_wing_result_jnt + ".Stretch"))
        mel.eval("selectKey -add -k -f -1 -f 0 %s;" % (self.branch_3_2_wing_result_jnt + "_translateX"))
        mel.eval('setInfinity -poi cycleRelative;')
        cmds.setAttr((self.branch_3_1_wing_result_jnt + ".Stretch"), 0)

        cmds.setDrivenKeyframe((self.branch_3_3_wing_result_jnt + ".tx"),
                               currentDriver=(self.branch_3_2_wing_result_jnt + ".Stretch"))
        cmds.setAttr((self.branch_3_2_wing_result_jnt + ".Stretch"), -1)
        cmds.setAttr((self.branch_3_3_wing_result_jnt + ".tx"), 0)
        cmds.setDrivenKeyframe((self.branch_3_3_wing_result_jnt + ".tx"),
                               currentDriver=(self.branch_3_2_wing_result_jnt + ".Stretch"))
        mel.eval("selectKey -add -k -f -1 -f 0 %s;" % (self.branch_3_3_wing_result_jnt + "_translateX"))
        mel.eval('setInfinity -poi cycleRelative;')
        cmds.setAttr((self.branch_3_2_wing_result_jnt + ".Stretch"), 0)

        cmds.setDrivenKeyframe((self.branch_3_4_wing_result_jnt + ".tx"),
                               currentDriver=(self.branch_3_3_wing_result_jnt + ".Stretch"))
        cmds.setAttr((self.branch_3_3_wing_result_jnt + ".Stretch"), -1)
        cmds.setAttr((self.branch_3_4_wing_result_jnt + ".tx"), 0)
        cmds.setDrivenKeyframe((self.branch_3_4_wing_result_jnt + ".tx"),
                               currentDriver=(self.branch_3_3_wing_result_jnt + ".Stretch"))
        mel.eval("selectKey -add -k -f -1 -f 0 %s;" % (self.branch_3_4_wing_result_jnt + "_translateX"))
        mel.eval('setInfinity -poi cycleRelative;')
        cmds.setAttr((self.branch_3_3_wing_result_jnt + ".Stretch"), 0)

        cmds.setDrivenKeyframe((self.branch_4_2_wing_result_jnt + ".tx"),
                               currentDriver=(self.branch_4_1_wing_result_jnt + ".Stretch"))
        cmds.setAttr((self.branch_4_1_wing_result_jnt + ".Stretch"), -1)
        cmds.setAttr((self.branch_4_2_wing_result_jnt + ".tx"), 0)
        cmds.setDrivenKeyframe((self.branch_4_2_wing_result_jnt + ".tx"),
                               currentDriver=(self.branch_4_1_wing_result_jnt + ".Stretch"))
        mel.eval("selectKey -add -k -f -1 -f 0 %s;" % (self.branch_4_2_wing_result_jnt + "_translateX"))
        mel.eval('setInfinity -poi cycleRelative;')
        cmds.setAttr((self.branch_4_1_wing_result_jnt + ".Stretch"), 0)

        cmds.setDrivenKeyframe((self.branch_4_3_wing_result_jnt + ".tx"),
                               currentDriver=(self.branch_4_2_wing_result_jnt + ".Stretch"))
        cmds.setAttr((self.branch_4_2_wing_result_jnt + ".Stretch"), -1)
        cmds.setAttr((self.branch_4_3_wing_result_jnt + ".tx"), 0)
        cmds.setDrivenKeyframe((self.branch_4_3_wing_result_jnt + ".tx"),
                               currentDriver=(self.branch_4_2_wing_result_jnt + ".Stretch"))
        mel.eval("selectKey -add -k -f -1 -f 0 %s;" % (self.branch_4_3_wing_result_jnt + "_translateX"))
        mel.eval('setInfinity -poi cycleRelative;')
        cmds.setAttr((self.branch_4_2_wing_result_jnt + ".Stretch"), 0)

        cmds.setDrivenKeyframe((self.branch_4_4_wing_result_jnt + ".tx"),
                               currentDriver=(self.branch_4_3_wing_result_jnt + ".Stretch"))
        cmds.setAttr((self.branch_4_3_wing_result_jnt + ".Stretch"), -1)
        cmds.setAttr((self.branch_4_4_wing_result_jnt + ".tx"), 0)
        cmds.setDrivenKeyframe((self.branch_4_4_wing_result_jnt + ".tx"),
                               currentDriver=(self.branch_4_3_wing_result_jnt + ".Stretch"))
        mel.eval("selectKey -add -k -f -1 -f 0 %s;" % (self.branch_4_4_wing_result_jnt + "_translateX"))
        mel.eval('setInfinity -poi cycleRelative;')
        cmds.setAttr((self.branch_4_3_wing_result_jnt + ".Stretch"), 0)

        # make a group
        fk_jnt_grp_name = self.upper_wing_fk_jnt + '_Grp'
        cmds.select(self.upper_wing_fk_jnt)
        cmds.group(n=fk_jnt_grp_name)

        ik_jnt_grp_name = self.upper_wing_ik_jnt + '_Grp'
        cmds.select(self.upper_wing_ik_jnt)
        cmds.group(n=ik_jnt_grp_name)

        result_jnt_grp_name = self.upper_wing_result_jnt + '_Grp'
        cmds.select(self.upper_wing_result_jnt)
        cmds.group(n=result_jnt_grp_name)

        cmds.select(self.upper_wing_fk_jnt, self.upper_wing_ik_jnt, self.upper_wing_result_jnt)
        cmds.joint(e=True, oj='xyz', secondaryAxisOrient='xup', ch=True, zso=True)

        # create a ik and fk switch
        self.controller_class.cube_ctrl()
        sel_obj = cmds.ls(sl=True)
        # self.prefix_name + "_" + self.wing_side  + "_Wing_" +  self.type + "_Branch_4_4_Tem_" + str(self.val)
        ik_fk_switch_name = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Ik_Fk_Switch_" + str(
            self.val) + '_Ctrl'
        ik_fk_switch_grp_name = ik_fk_switch_name + '_Grp'
        cmds.rename(sel_obj[0], ik_fk_switch_name)
        cmds.move(self.ctrl_list[self.hand_2_wing_inner_ctrl]['Trans'][0],
                  self.ctrl_list[self.hand_2_wing_inner_ctrl]['Trans'][1],
                  self.ctrl_list[self.hand_2_wing_inner_ctrl]['Trans'][2])
        # move -r -os -wd 0 0 -6.664142 ;
        cmds.move(0, 0, 6, r=True)
        cmds.group(n=ik_fk_switch_grp_name)
        self.helper_class.transform_rotation_scale_visible(ik_fk_switch_grp_name)
        cmds.select(ik_fk_switch_name)
        cmds.DeleteHistory()
        cmds.FreezeTransformations()
        cmds.parentConstraint(self.hand_2_wing_result_jnt, ik_fk_switch_name, mo=True)
        cmds.addAttr(ik_fk_switch_name, ln="IK_FK_Switch", at='double', min=0, max=1)
        cmds.setAttr((ik_fk_switch_name + ".IK_FK_Switch"), e=True, keyable=True)

        a = 0
        while a < len(ik_jnt_list):
            ik_jnt = ik_jnt_list[a]
            fk_jnt = fk_jnt_list[a]
            result_jnt = result_jnt_list[a]
            trans_blend_name = ik_jnt + '_' + fk_jnt + '_Trans_Blend_Color'

            self.connection_class.blend_one_val(blend_color_name=trans_blend_name,
                                                input_1=ik_jnt,
                                                input_2=fk_jnt,
                                                output=result_jnt,
                                                input_1_val='translate',
                                                input_2_val='translate',
                                                output_val='translate')
            rot_blend_name = ik_jnt + '_' + fk_jnt + '_Rot_Blend_Color'
            self.connection_class.blend_one_val(blend_color_name=rot_blend_name,
                                                input_1=ik_jnt,
                                                input_2=fk_jnt,
                                                output=result_jnt,
                                                input_1_val='rotate',
                                                input_2_val='rotate',
                                                output_val='rotate')
            cmds.connectAttr((ik_fk_switch_name + '.IK_FK_Switch'), (trans_blend_name + '.blender'), f=True)
            cmds.connectAttr((ik_fk_switch_name + '.IK_FK_Switch'), (rot_blend_name + '.blender'), f=True)
            cmds.connectAttr((ik_fk_switch_name + '.IK_FK_Switch'), (ik_jnt + '.v'), f=True)
            reverse_name = ik_fk_switch_name + '_' + fk_jnt + '_Reverse'
            self.connection_class.reverse_def(reverse_name=reverse_name,
                                              input=ik_fk_switch_name,
                                              output=fk_jnt,
                                              input_val='IK_FK_Switch',
                                              output_val='v')

            # Create a Controller for the Fk controller
            self.controller_class.circle_ctrl()
            common_name = self.helper_class.remove_tem(self.common_list[a])
            ctrl_name = common_name + '_Ctrl'
            ctrl_shape_name = ctrl_name + 'Shape'
            cmds.rename('circle_ctrl', ctrl_name)
            cmds.select(ctrl_shape_name, fk_jnt)
            cmds.parent(r=True, s=True)
            cmds.select(ctrl_name)
            cmds.delete()
            a += 1

        cmds.addAttr(self.upper_wing_fk_jnt, ln="Stretch", at='double', min=-1, dv=0)
        cmds.setAttr((self.upper_wing_fk_jnt + ".Stretch"), e=True, keyable=True)
        cmds.setDrivenKeyframe((self.lbow_wing_fk_jnt + ".tx"), currentDriver=(self.upper_wing_fk_jnt + ".Stretch"))
        cmds.setAttr((self.upper_wing_fk_jnt + ".Stretch"), -1)
        cmds.setAttr((self.lbow_wing_fk_jnt + ".tx"), 0)
        cmds.setDrivenKeyframe((self.lbow_wing_fk_jnt + ".tx"), currentDriver=(self.upper_wing_fk_jnt + ".Stretch"))
        mel.eval("selectKey -add -k -f -1 -f 0 %s;" % (self.lbow_wing_fk_jnt + "_translateX"))
        mel.eval('setInfinity -poi cycleRelative;')
        cmds.setAttr((self.upper_wing_fk_jnt + ".Stretch"), 0)

        cmds.addAttr(self.lbow_wing_fk_jnt, ln="Stretch", at='double', min=-1, dv=0)
        cmds.setAttr((self.lbow_wing_fk_jnt + ".Stretch"), e=True, keyable=True)
        cmds.setDrivenKeyframe((self.hand_wing_fk_jnt + ".tx"), currentDriver=(self.lbow_wing_fk_jnt + ".Stretch"))
        cmds.setAttr((self.lbow_wing_fk_jnt + ".Stretch"), -1)
        cmds.setAttr((self.hand_wing_fk_jnt + ".tx"), 0)
        cmds.setDrivenKeyframe((self.hand_wing_fk_jnt + ".tx"), currentDriver=(self.lbow_wing_fk_jnt + ".Stretch"))
        mel.eval("selectKey -add -k -f -1 -f 0 %s;" % (self.hand_wing_fk_jnt + "_translateX"))
        mel.eval('setInfinity -poi cycleRelative;')
        cmds.setAttr((self.lbow_wing_fk_jnt + ".Stretch"), 0)

        cmds.addAttr(self.hand_wing_fk_jnt, ln="Stretch", at='double', min=-1, dv=0)
        cmds.setAttr((self.hand_wing_fk_jnt + ".Stretch"), e=True, keyable=True)

        cmds.setDrivenKeyframe((self.hand_2_wing_fk_jnt + ".tx"), currentDriver=(self.hand_wing_fk_jnt + ".Stretch"))
        cmds.setAttr((self.hand_wing_fk_jnt + ".Stretch"), -1)
        cmds.setAttr((self.hand_2_wing_fk_jnt + ".tx"), 0)
        cmds.setDrivenKeyframe((self.hand_2_wing_fk_jnt + ".tx"), currentDriver=(self.hand_wing_fk_jnt + ".Stretch"))
        mel.eval("selectKey -add -k -f -1 -f 0 %s;" % (self.hand_2_wing_fk_jnt + "_translateX"))
        mel.eval('setInfinity -poi cycleRelative;')
        cmds.setAttr((self.hand_wing_fk_jnt + ".Stretch"), 0)

        cmds.setAttr((ik_fk_switch_name + '.IK_FK_Switch'), 1)

        if self.wing_side == 'L':
            color_name = 'Blue'
        else:
            color_name = 'Red'
        for each in fk_jnt_list:
            ctrl_name = each.replace('Jnt', 'Ctrl')
            ctrl_shape_name = ctrl_name + 'Shape'
            self.controller_class.circle_ctrl()
            sel_obj = cmds.ls(sl=True)
            cmds.rename(sel_obj[0], ctrl_name)
            self.helper_class.color_val(color_name, ctrl_name)
            cmds.select(ctrl_shape_name, each)
            cmds.parent(r=True, s=True)
            cmds.select(ctrl_name)
            cmds.delete()
            a += 1

        # create a the controller ik position
        handle_ctrl_name = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_IK_" + str(
            self.val) + '_Ctrl'
        handle_ctrl_grp_name = handle_ctrl_name + '_Grp'
        self.controller_class.hand_ctrl()
        cmds.select('hand_ctrl')
        sel_obj = cmds.ls(sl=True)
        cmds.rename(sel_obj[0], handle_ctrl_name)
        cmds.select(handle_ctrl_name)
        cmds.move(self.ctrl_list[self.hand_wing_inner_ctrl]['Trans'][0],
                  self.ctrl_list[self.hand_wing_inner_ctrl]['Trans'][1],
                  self.ctrl_list[self.hand_wing_inner_ctrl]['Trans'][2])
        # move -r -os -wd 0 0 -6.664142 ;

        cmds.setAttr((handle_ctrl_name + '.sx'), 5)
        cmds.setAttr((handle_ctrl_name + '.sy'), 5)
        cmds.setAttr((handle_ctrl_name + '.sz'), 5)
        cmds.DeleteHistory()
        cmds.FreezeTransformations()
        cmds.select(handle_ctrl_name)
        cmds.group(n=handle_ctrl_grp_name)
        cmds.connectAttr((ik_fk_switch_name + '.IK_FK_Switch'), (handle_ctrl_grp_name + '.v'), f=True)
        self.helper_class.color_val(color_name, handle_ctrl_name)

        ik_handle_name = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_IK_" + str(
            self.val) + '_Handle'
        cmds.ikHandle(n=ik_handle_name,
                      sj=self.upper_wing_ik_jnt,
                      ee=self.hand_wing_ik_jnt,
                      sol='ikRPsolver')
        cmds.setAttr((ik_handle_name + '.v'), 0)
        cmds.select(ik_handle_name, handle_ctrl_name)
        cmds.parent()

        ik_hand_handle_name = self.prefix_name + "_" + self.wing_side + "_Wing_Hand_" + self.type + "_IK_" + str(
            self.val) + '_Handle'
        cmds.ikHandle(n=ik_hand_handle_name,
                      sj=self.hand_wing_ik_jnt,
                      ee=self.hand_2_wing_ik_jnt,
                      sol='ikSCsolver')
        cmds.setAttr((ik_hand_handle_name + '.v'), 0)
        cmds.select(ik_hand_handle_name, handle_ctrl_name)
        cmds.parent()

        # Create a Polvector controller
        wing_lbow_loc_name = self.prefix_name + "_" + self.wing_side + "_Wing_lBow_" + self.type + "_" + str(
            self.val) + '_Loc'
        cmds.spaceLocator(n=wing_lbow_loc_name, p=(self.ctrl_list[self.lbow_wing_inner_ctrl]['Trans'][0],
                                                   self.ctrl_list[self.lbow_wing_inner_ctrl]['Trans'][1],
                                                   self.ctrl_list[self.lbow_wing_inner_ctrl]['Trans'][2]))
        cmds.select(wing_lbow_loc_name)
        # cmds.move(0,0,12,r=True)
        cmds.DeleteHistory()
        cmds.FreezeTransformations()
        cmds.CenterPivot()
        cmds.select(wing_lbow_loc_name, ik_handle_name)
        cmds.poleVectorConstraint()
        cmds.setAttr((wing_lbow_loc_name + '.v'), 0)

        self.controller_class.traiangle_new_ctrl()
        lbow_ctrl_name = self.prefix_name + "_" + self.wing_side + "_Wing_lBow_" + self.type + "_" + str(
            self.val) + '_Ctrl'
        lbow_ctrl_grp_name = lbow_ctrl_name + '_Grp'
        cmds.rename('Triangle_new_ctrl', lbow_ctrl_name)
        cmds.select(lbow_ctrl_name)
        cmds.parentConstraint(wing_lbow_loc_name, lbow_ctrl_name, mo=False)
        cmds.select(lbow_ctrl_name + '_parentConstraint1')
        cmds.delete()
        cmds.select(lbow_ctrl_name)
        cmds.move(0, 0, 12, r=True)
        lbow_world_pos = cmds.getAttr(lbow_ctrl_name + '.t')[0]
        cmds.select(lbow_ctrl_name)
        cmds.DeleteHistory()
        cmds.FreezeTransformations()
        cmds.select(wing_lbow_loc_name, lbow_ctrl_name)
        cmds.parent()
        cmds.select(lbow_ctrl_name)
        cmds.group(n=lbow_ctrl_grp_name)
        cmds.connectAttr((ik_fk_switch_name + '.IK_FK_Switch'), (lbow_ctrl_grp_name + '.v'))

        # CREATE A DIS BETWEEN THE SHOULDER AND THE HAND CONTROLLER

        upper_hand_to_hand_start_loc = self.prefix_name + "_" + self.wing_side + "_Wing_Upper_Hand_to_Hand_" + self.type + "_" + str(
            self.val) + '_Start_Ctrl'
        upper_hand_to_hand_end_loc = self.prefix_name + "_" + self.wing_side + "_Wing_Upper_Hand_to_Hand_" + self.type + "_" + str(
            self.val) + '_End_Ctrl'
        upper_hand_to_hand_dis = self.prefix_name + "_" + self.wing_side + "_Wing_Upper_Hand_to_Hand_" + self.type + "_" + str(
            self.val) + '_Dis'
        upper_hand_to_lbow_dis_shape = upper_hand_to_hand_dis + 'Shape'
        cmds.spaceLocator(n=upper_hand_to_hand_start_loc, p=(self.ctrl_list[self.upper_wing_inner_ctrl]['Trans'][0],
                                                             self.ctrl_list[self.upper_wing_inner_ctrl]['Trans'][1],
                                                             self.ctrl_list[self.upper_wing_inner_ctrl]['Trans'][2]))
        cmds.spaceLocator(n=upper_hand_to_hand_end_loc, p=(self.ctrl_list[self.hand_wing_inner_ctrl]['Trans'][0],
                                                           self.ctrl_list[self.hand_wing_inner_ctrl]['Trans'][1],
                                                           self.ctrl_list[self.hand_wing_inner_ctrl]['Trans'][2]))
        cmds.select(upper_hand_to_hand_start_loc, upper_hand_to_hand_end_loc)
        cmds.CenterPivot()
        cmds.distanceDimension()
        cmds.rename('distanceDimension1', upper_hand_to_hand_dis)
        cmds.select(upper_hand_to_hand_end_loc, handle_ctrl_name)
        cmds.parent()

        # make a stretch
        driver = upper_hand_to_lbow_dis_shape + '.distance'
        thine_length = cmds.getAttr(self.lbow_wing_ik_jnt + '.tx')
        shine_length = cmds.getAttr(self.hand_wing_ik_jnt + '.tx')
        sumlength = thine_length + shine_length
        cmds.setDrivenKeyframe(self.lbow_wing_ik_jnt, currentDriver=driver, driverValue=sumlength, attribute='tx',
                               value=thine_length)
        cmds.setDrivenKeyframe(self.lbow_wing_ik_jnt, currentDriver=driver, driverValue=sumlength * 2, attribute='tx',
                               value=thine_length * 2)

        cmds.setDrivenKeyframe(self.hand_wing_ik_jnt, currentDriver=driver, driverValue=sumlength, attribute='tx',
                               value=shine_length)
        cmds.setDrivenKeyframe(self.hand_wing_ik_jnt, currentDriver=driver, driverValue=sumlength * 2, attribute='tx',
                               value=shine_length * 2)

        mel.eval("selectKey -add -k -f 60.340366 -f 120.680733 %s;" % (self.lbow_wing_ik_jnt + "_translateX"))
        mel.eval('keyTangent -e -itt linear -ott linear;')
        mel.eval('setInfinity -poi cycleRelative;')
        mel.eval("selectKey -add -k -f 60.340366 -f 120.680733 %s;" % (self.hand_wing_ik_jnt + "_translateX"))
        mel.eval('keyTangent -e -itt linear -ott linear;')
        mel.eval('setInfinity -poi cycleRelative;')

        # make a center group
        cmds.select(fk_jnt_grp_name, ik_jnt_grp_name, result_jnt_grp_name, ik_fk_switch_grp_name, handle_ctrl_grp_name,
                    lbow_ctrl_grp_name, upper_hand_to_hand_start_loc, upper_hand_to_hand_dis)
        wing_grp_name = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_" + str(self.val) + '_Grp'
        cmds.group(n=wing_grp_name)
        cmds.select(wing_grp_name, root_grp_name)
        cmds.parent()

        cmds.select(ik_jnt_grp_name, result_jnt_grp_name, upper_hand_to_hand_start_loc, upper_hand_to_hand_dis)
        wing_do_not_touch_grp_name = self.prefix_name + "_" + self.wing_side + "_Wing_DO_NOT_TOUCH_" + self.type + "_" + str(
            self.val) + '_Grp'
        cmds.group(n=wing_do_not_touch_grp_name)

        cmds.select(ik_jnt_grp_name, upper_hand_to_hand_start_loc)
        wing_ik_const_grp_name = self.prefix_name + "_" + self.wing_side + "_Wing_Ik_Const_" + self.type + "_" + str(
            self.val) + '_Grp'
        cmds.group(n=wing_ik_const_grp_name)
        cmds.move(self.ctrl_list[self.upper_wing_inner_ctrl]['Trans'][0],
                  self.ctrl_list[self.upper_wing_inner_ctrl]['Trans'][1],
                  self.ctrl_list[self.upper_wing_inner_ctrl]['Trans'][2],
                  (wing_ik_const_grp_name + '.scalePivot'),
                  (wing_ik_const_grp_name + '.rotatePivot'))

        cmds.select(result_jnt_grp_name)
        wing_result_const_grp_name = self.prefix_name + "_" + self.wing_side + "_Wing_Result_Const_" + self.type + "_" + str(
            self.val) + '_Grp'
        cmds.group(n=wing_result_const_grp_name)
        cmds.move(self.ctrl_list[self.upper_wing_inner_ctrl]['Trans'][0],
                  self.ctrl_list[self.upper_wing_inner_ctrl]['Trans'][1],
                  self.ctrl_list[self.upper_wing_inner_ctrl]['Trans'][2],
                  (wing_result_const_grp_name + '.scalePivot'),
                  (wing_result_const_grp_name + '.rotatePivot'))

        cmds.select(fk_jnt_grp_name)
        wing_fk_const_grp_name = self.prefix_name + "_" + self.wing_side + "_Wing_Fk_Const_" + self.type + "_" + str(
            self.val) + '_Grp'
        cmds.group(n=wing_fk_const_grp_name)
        cmds.move(self.ctrl_list[self.upper_wing_inner_ctrl]['Trans'][0],
                  self.ctrl_list[self.upper_wing_inner_ctrl]['Trans'][1],
                  self.ctrl_list[self.upper_wing_inner_ctrl]['Trans'][2],
                  (wing_fk_const_grp_name + '.scalePivot'),
                  (wing_fk_const_grp_name + '.rotatePivot'))

        # Create a Loc and Point Const to all
        wing_const_loc_name = self.prefix_name + "_" + self.wing_side + "_Wing_Const_" + self.type + "_" + str(
            self.val) + '_Loc'
        cmds.spaceLocator(n=wing_const_loc_name, p=(self.ctrl_list[self.upper_wing_inner_ctrl]['Trans'][0],
                                                    self.ctrl_list[self.upper_wing_inner_ctrl]['Trans'][1],
                                                    self.ctrl_list[self.upper_wing_inner_ctrl]['Trans'][2]))

        wing_body_const_loc_name = self.prefix_name + "_" + self.wing_side + "_Wing_Body_Const_" + self.type + "_" + str(
            self.val) + '_Loc'
        cmds.spaceLocator(n=wing_body_const_loc_name, p=(self.ctrl_list[self.upper_wing_inner_ctrl]['Trans'][0],
                                                         self.ctrl_list[self.upper_wing_inner_ctrl]['Trans'][1],
                                                         self.ctrl_list[self.upper_wing_inner_ctrl]['Trans'][2]))

        wing_root_const_loc_name = self.prefix_name + "_" + self.wing_side + "_Wing_Root_Const_" + self.type + "_" + str(
            self.val) + '_Loc'
        cmds.spaceLocator(n=wing_root_const_loc_name, p=(self.ctrl_list[self.upper_wing_inner_ctrl]['Trans'][0],
                                                         self.ctrl_list[self.upper_wing_inner_ctrl]['Trans'][1],
                                                         self.ctrl_list[self.upper_wing_inner_ctrl]['Trans'][2]))

        cmds.select(wing_const_loc_name, wing_body_const_loc_name, wing_root_const_loc_name)
        cmds.DeleteHistory()
        cmds.FreezeTransformations()
        cmds.CenterPivot()
        cmds.pointConstraint(wing_const_loc_name, wing_ik_const_grp_name, mo=True)
        cmds.pointConstraint(wing_const_loc_name, wing_fk_const_grp_name, mo=True)
        cmds.pointConstraint(wing_const_loc_name, wing_result_const_grp_name, mo=True)

        # make the orient const
        cmds.orientConstraint(wing_const_loc_name, wing_fk_const_grp_name, mo=True)
        cmds.orientConstraint(wing_body_const_loc_name, wing_fk_const_grp_name, mo=True)
        cmds.orientConstraint(wing_root_const_loc_name, wing_fk_const_grp_name, mo=True)

        cmds.orientConstraint(wing_const_loc_name, wing_result_const_grp_name, mo=True)
        cmds.orientConstraint(wing_body_const_loc_name, wing_result_const_grp_name, mo=True)
        cmds.orientConstraint(wing_root_const_loc_name, wing_result_const_grp_name, mo=True)

        # connect the orient const to the attr
        cmds.addAttr(ik_fk_switch_name, ln="FK_Rotation_Space", at='enum', en='Shoulder:UpperBody:Root')
        cmds.setAttr((ik_fk_switch_name + ".FK_Rotation_Space"), e=True, keyable=True)

        cmds.setAttr((ik_fk_switch_name + ".FK_Rotation_Space"), 0)
        cmds.setAttr((wing_fk_const_grp_name + "_orientConstraint1." + wing_const_loc_name + 'W0'), 1)
        cmds.setAttr((wing_fk_const_grp_name + "_orientConstraint1." + wing_body_const_loc_name + 'W1'), 0)
        cmds.setAttr((wing_fk_const_grp_name + "_orientConstraint1." + wing_root_const_loc_name + 'W2'), 0)
        cmds.setAttr((wing_result_const_grp_name + "_orientConstraint1." + wing_const_loc_name + 'W0'), 1)
        cmds.setAttr((wing_result_const_grp_name + "_orientConstraint1." + wing_body_const_loc_name + 'W1'), 0)
        cmds.setAttr((wing_result_const_grp_name + "_orientConstraint1." + wing_root_const_loc_name + 'W2'), 0)
        cmds.setDrivenKeyframe((wing_fk_const_grp_name + "_orientConstraint1." + wing_const_loc_name + 'W0'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))
        cmds.setDrivenKeyframe((wing_fk_const_grp_name + "_orientConstraint1." + wing_body_const_loc_name + 'W1'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))
        cmds.setDrivenKeyframe((wing_fk_const_grp_name + "_orientConstraint1." + wing_root_const_loc_name + 'W2'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))
        cmds.setDrivenKeyframe((wing_result_const_grp_name + "_orientConstraint1." + wing_const_loc_name + 'W0'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))
        cmds.setDrivenKeyframe((wing_result_const_grp_name + "_orientConstraint1." + wing_body_const_loc_name + 'W1'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))
        cmds.setDrivenKeyframe((wing_result_const_grp_name + "_orientConstraint1." + wing_root_const_loc_name + 'W2'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))

        cmds.setAttr((ik_fk_switch_name + ".FK_Rotation_Space"), 1)
        cmds.setAttr((wing_fk_const_grp_name + "_orientConstraint1." + wing_const_loc_name + 'W0'), 0)
        cmds.setAttr((wing_fk_const_grp_name + "_orientConstraint1." + wing_body_const_loc_name + 'W1'), 1)
        cmds.setAttr((wing_fk_const_grp_name + "_orientConstraint1." + wing_root_const_loc_name + 'W2'), 0)
        cmds.setAttr((wing_result_const_grp_name + "_orientConstraint1." + wing_const_loc_name + 'W0'), 0)
        cmds.setAttr((wing_result_const_grp_name + "_orientConstraint1." + wing_body_const_loc_name + 'W1'), 1)
        cmds.setAttr((wing_result_const_grp_name + "_orientConstraint1." + wing_root_const_loc_name + 'W2'), 0)
        cmds.setDrivenKeyframe((wing_fk_const_grp_name + "_orientConstraint1." + wing_const_loc_name + 'W0'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))
        cmds.setDrivenKeyframe((wing_fk_const_grp_name + "_orientConstraint1." + wing_body_const_loc_name + 'W1'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))
        cmds.setDrivenKeyframe((wing_fk_const_grp_name + "_orientConstraint1." + wing_root_const_loc_name + 'W2'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))
        cmds.setDrivenKeyframe((wing_result_const_grp_name + "_orientConstraint1." + wing_const_loc_name + 'W0'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))
        cmds.setDrivenKeyframe((wing_result_const_grp_name + "_orientConstraint1." + wing_body_const_loc_name + 'W1'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))
        cmds.setDrivenKeyframe((wing_result_const_grp_name + "_orientConstraint1." + wing_root_const_loc_name + 'W2'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))

        cmds.setAttr((ik_fk_switch_name + ".FK_Rotation_Space"), 2)
        cmds.setAttr((wing_fk_const_grp_name + "_orientConstraint1." + wing_const_loc_name + 'W0'), 0)
        cmds.setAttr((wing_fk_const_grp_name + "_orientConstraint1." + wing_body_const_loc_name + 'W1'), 0)
        cmds.setAttr((wing_fk_const_grp_name + "_orientConstraint1." + wing_root_const_loc_name + 'W2'), 1)
        cmds.setAttr((wing_result_const_grp_name + "_orientConstraint1." + wing_const_loc_name + 'W0'), 0)
        cmds.setAttr((wing_result_const_grp_name + "_orientConstraint1." + wing_body_const_loc_name + 'W1'), 0)
        cmds.setAttr((wing_result_const_grp_name + "_orientConstraint1." + wing_root_const_loc_name + 'W2'), 1)
        cmds.setDrivenKeyframe((wing_fk_const_grp_name + "_orientConstraint1." + wing_const_loc_name + 'W0'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))
        cmds.setDrivenKeyframe((wing_fk_const_grp_name + "_orientConstraint1." + wing_body_const_loc_name + 'W1'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))
        cmds.setDrivenKeyframe((wing_fk_const_grp_name + "_orientConstraint1." + wing_root_const_loc_name + 'W2'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))
        cmds.setDrivenKeyframe((wing_result_const_grp_name + "_orientConstraint1." + wing_const_loc_name + 'W0'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))
        cmds.setDrivenKeyframe((wing_result_const_grp_name + "_orientConstraint1." + wing_body_const_loc_name + 'W1'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))
        cmds.setDrivenKeyframe((wing_result_const_grp_name + "_orientConstraint1." + wing_root_const_loc_name + 'W2'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))

        # Hide unwanted object
        list = [upper_hand_to_hand_start_loc, upper_hand_to_hand_end_loc, upper_hand_to_hand_dis]
        for each in list:
            cmds.setAttr((each + '.v'), 0)

        # blend with the root grp
        mult_div_name = self.prefix_name + "_" + self.wing_side + "_Wing_globalize_scale_" + self.type + "_" + str(
            self.val) + '_Mult'
        cmds.createNode('multiplyDivide', n=mult_div_name)
        # connectAttr -f Template_L_Thine_to_Foot_1_DisShape.distance multiplyDivide1.input1X;
        cmds.connectAttr((upper_hand_to_lbow_dis_shape + '.distance'), (mult_div_name + '.input1X'), f=True)
        cmds.connectAttr((root_grp_name + '.scale.scaleY'), (mult_div_name + '.input2.input2X'), f=True)
        # setAttr "multiplyDivide1.operation" 2;
        cmds.setAttr((mult_div_name + '.operation'), 2)
        cmds.connectAttr((mult_div_name + '.output.outputX'), (self.lbow_wing_ik_jnt + '_translateX.input'), f=True)
        cmds.connectAttr((mult_div_name + '.output.outputX'), (self.hand_wing_ik_jnt + '_translateX.input'), f=True)

        # Create a Wing shoulder
        # SHOULDER
        self.shoulder_wing_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Shoulder_Tem_" + str(
            self.val)
        self.shoulder_wing_inner_ctrl = self.shoulder_wing_common + '_Inner_Ctrl'
        tem_remove_name = self.helper_class.remove_tem(self.shoulder_wing_inner_ctrl)
        if cmds.objExists(self.shoulder_wing_inner_ctrl):
            self.shoulder_wing_result_jnt = tem_remove_name + '_Result_Jnt'
            shoulder_get_trans = cmds.xform(self.shoulder_wing_inner_ctrl, q=1, ws=1, rp=1)
            shoulder_get_rot = cmds.getAttr(self.shoulder_wing_inner_ctrl + '.r')

        # Create a joint
        self.shoulder_wing_end_common = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Shoulder_End_Tem_" + str(
            self.val)
        tem_remove_name = self.helper_class.remove_tem(self.shoulder_wing_end_common)
        self.shoulder_wing_end_result_jnt = tem_remove_name + '_Result_Jnt'

        cmds.select(cl=True)
        cmds.joint(n=self.shoulder_wing_result_jnt, p=(shoulder_get_trans[0],
                                                       shoulder_get_trans[1],
                                                       shoulder_get_trans[2]))
        cmds.joint(n=self.shoulder_wing_end_result_jnt, p=(self.ctrl_list[self.upper_wing_inner_ctrl]['Trans'][0],
                                                           self.ctrl_list[self.upper_wing_inner_ctrl]['Trans'][1],
                                                           self.ctrl_list[self.upper_wing_inner_ctrl]['Trans'][2]))
        cmds.select(cl=True)
        cmds.select(self.shoulder_wing_result_jnt)
        cmds.joint(e=True, oj='xyz', secondaryAxisOrient='xup', ch=True, zso=True)

        ik_shoulder_handle_name = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_IK_Shoulder_" + str(
            self.val) + '_Handle'
        cmds.ikHandle(n=ik_shoulder_handle_name,
                      sj=self.shoulder_wing_result_jnt,
                      ee=self.shoulder_wing_end_result_jnt,
                      sol='ikSCsolver')
        # Now Create a Controller
        self.controller_class.traiangle_new_ctrl()
        shoulder_wing_ctrl_name = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_IK_Shoulder_" + str(
            self.val) + '_Ctrl'
        cmds.rename('Triangle_new_ctrl', shoulder_wing_ctrl_name)
        cmds.select(shoulder_wing_ctrl_name)
        cmds.move(self.ctrl_list[self.upper_wing_inner_ctrl]['Trans'][0],
                  self.ctrl_list[self.upper_wing_inner_ctrl]['Trans'][1],
                  self.ctrl_list[self.upper_wing_inner_ctrl]['Trans'][2])
        cmds.move(0, 0, 6, r=True)
        cmds.DeleteHistory()
        cmds.FreezeTransformations()
        cmds.select(ik_shoulder_handle_name, shoulder_wing_ctrl_name)
        cmds.parent()

        # Shoulder wing Stretch
        upper_wing_hand_to_hand_start_loc = self.prefix_name + "_" + self.wing_side + "_Wing_Upper_Shoulder_to_Upper_Hand_" + self.type + "_" + str(
            self.val) + '_Start_Ctrl'
        upper_wing_hand_to_hand_end_loc = self.prefix_name + "_" + self.wing_side + "_Wing_Upper_Shoulder_to_Upper_Hand_" + self.type + "_" + str(
            self.val) + '_End_Ctrl'
        upper_wing_hand_to_hand_dis = self.prefix_name + "_" + self.wing_side + "_Wing_Upper_Shoulder_to_Upper_Hand_" + self.type + "_" + str(
            self.val) + '_Dis'
        upper_wing_hand_to_lbow_dis_shape = upper_wing_hand_to_hand_dis + 'Shape'
        cmds.spaceLocator(n=upper_wing_hand_to_hand_start_loc, p=(shoulder_get_trans[0],
                                                                  shoulder_get_trans[1],
                                                                  shoulder_get_trans[2]))
        cmds.spaceLocator(n=upper_wing_hand_to_hand_end_loc, p=(self.ctrl_list[self.upper_wing_inner_ctrl]['Trans'][0],
                                                                self.ctrl_list[self.upper_wing_inner_ctrl]['Trans'][1],
                                                                self.ctrl_list[self.upper_wing_inner_ctrl]['Trans'][2]))
        cmds.select(upper_wing_hand_to_hand_start_loc, upper_wing_hand_to_hand_end_loc)
        cmds.CenterPivot()
        cmds.distanceDimension()
        cmds.rename('distanceDimension1', upper_wing_hand_to_hand_dis)
        cmds.select(upper_wing_hand_to_hand_end_loc, shoulder_wing_ctrl_name)
        cmds.parent()

        # make a stretch
        driver = upper_wing_hand_to_lbow_dis_shape + '.distance'
        length = cmds.getAttr(self.shoulder_wing_end_result_jnt + '.tx')
        cmds.setDrivenKeyframe(self.shoulder_wing_end_result_jnt, currentDriver=driver, driverValue=length,
                               attribute='tx', value=length)
        cmds.setDrivenKeyframe(self.shoulder_wing_end_result_jnt, currentDriver=driver, driverValue=length * 2,
                               attribute='tx', value=length * 2)

        mel.eval("selectKey -add -k -f 7.191723 -f 14.383446 %s;" % (self.shoulder_wing_end_result_jnt + "_translateX"))
        mel.eval('keyTangent -e -itt linear -ott linear;')
        mel.eval('setInfinity -poi cycleRelative;')

        # Group Everything the shoulder
        cmds.select(self.shoulder_wing_result_jnt, shoulder_wing_ctrl_name, upper_wing_hand_to_hand_start_loc,
                    upper_wing_hand_to_hand_dis)
        shoulder_wing_grp = self.prefix_name + "_" + self.wing_side + "_Wing_Shoulder_" + self.type + "_" + str(
            self.val) + '_Grp'
        cmds.group(n=shoulder_wing_grp)
        # change the pivot
        cmds.move(shoulder_get_trans[0],
                  shoulder_get_trans[1],
                  shoulder_get_trans[2],
                  (shoulder_wing_grp + '.scalePivot'),
                  (shoulder_wing_grp + '.rotatePivot'))

        mult_div_name = self.prefix_name + "_" + self.wing_side + "_Wing_Shoulder_globalize_scale_" + self.type + "_" + str(
            self.val) + '_Mult'
        cmds.createNode('multiplyDivide', n=mult_div_name)
        # connectAttr -f Template_L_Thine_to_Foot_1_DisShape.distance multiplyDivide1.input1X;
        cmds.connectAttr((upper_wing_hand_to_lbow_dis_shape + '.distance'), (mult_div_name + '.input1X'), f=True)
        cmds.connectAttr((root_grp_name + '.scale.scaleY'), (mult_div_name + '.input2.input2X'), f=True)
        # setAttr "multiplyDivide1.operation" 2;
        cmds.setAttr((mult_div_name + '.operation'), 2)
        cmds.connectAttr((mult_div_name + '.output.outputX'), (self.shoulder_wing_end_result_jnt + '_translateX.input'),
                         f=True)

        # Shoulde Hide Unwanted
        list = [ik_shoulder_handle_name, upper_wing_hand_to_hand_end_loc, upper_wing_hand_to_hand_start_loc,
                upper_wing_hand_to_hand_dis]
        for each in list:
            cmds.setAttr((each + '.v'), 0)

        cmds.select(shoulder_wing_grp, root_grp_name)
        cmds.parent()

        # Shoulder_body_const_loc
        shoulder_body_const_loc_name = self.prefix_name + "_" + self.wing_side + "_Wing_Shoulder_Const_" + self.type + "_" + str(
            self.val) + '_Loc'
        cmds.spaceLocator(n=shoulder_body_const_loc_name, p=(shoulder_get_trans[0],
                                                             shoulder_get_trans[1],
                                                             shoulder_get_trans[2]))
        cmds.select(shoulder_body_const_loc_name)
        cmds.DeleteHistory()
        cmds.FreezeTransformations()
        cmds.CenterPivot()
        cmds.parentConstraint(shoulder_body_const_loc_name, shoulder_wing_grp, mo=True)
        cmds.select(shoulder_body_const_loc_name, shoulder_wing_grp, root_grp_name)
        cmds.parent()

        cmds.select(wing_const_loc_name, wing_body_const_loc_name, wing_root_const_loc_name, shoulder_wing_ctrl_name)
        cmds.parent()

        # Lock and hide the object
        trans_list = [ik_fk_switch_name,
                      self.branch_1_1_wing_result_jnt, self.branch_1_2_wing_result_jnt, self.branch_1_3_wing_result_jnt,
                      self.branch_2_1_wing_result_jnt, self.branch_2_2_wing_result_jnt, self.branch_2_3_wing_result_jnt,
                      self.branch_3_1_wing_result_jnt, self.branch_3_2_wing_result_jnt, self.branch_3_3_wing_result_jnt,
                      self.branch_4_1_wing_result_jnt, self.branch_4_2_wing_result_jnt, self.branch_4_3_wing_result_jnt]
        for each in trans_list:
            self.helper_class.transform_rotation_scale_visible(each, t=True, r=False, s=False)

        rot_list = [shoulder_wing_ctrl_name, lbow_ctrl_name, ik_fk_switch_name]
        for each in rot_list:
            self.helper_class.transform_rotation_scale_visible(each, t=False, r=True, s=False)

        scale_list = [shoulder_wing_ctrl_name, lbow_ctrl_name, ik_fk_switch_name, handle_ctrl_name,
                      self.branch_1_1_wing_result_jnt, self.branch_1_2_wing_result_jnt, self.branch_1_3_wing_result_jnt,
                      self.branch_2_1_wing_result_jnt, self.branch_2_2_wing_result_jnt, self.branch_2_3_wing_result_jnt,
                      self.branch_3_1_wing_result_jnt, self.branch_3_2_wing_result_jnt, self.branch_3_3_wing_result_jnt,
                      self.branch_4_1_wing_result_jnt, self.branch_4_2_wing_result_jnt, self.branch_4_3_wing_result_jnt]
        for each in scale_list:
            self.helper_class.transform_rotation_scale_visible(each, t=False, r=False, s=True)

    def bone_def(self):
        # get the no of the human main grp
        self.grp_list = ['Wing_Grp']
        for each_grp in self.grp_list:
            # list of the all children
            if cmds.objExists(each_grp):
                children_list = cmds.listRelatives(each_grp, children=True)
                for each_child in children_list:
                    # get all the controller data
                    self.wing_data(each_child)

                    self.final_bone_wing()

    def final_bone_wing(self):
        grp_namne = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + '_' + str(self.val) + '_Bone_Grp'
        main_grp_name = 'wing_Bone_Grp'

        list = [self.shoulder_wing_common, self.upper_wing_common, self.lbow_wing_common, self.hand_wing_common,
                self.hand_2_wing_common,
                self.branch_1_1_wing_common, self.branch_1_2_wing_common, self.branch_1_3_wing_common,
                self.branch_1_4_wing_common,
                self.branch_2_1_wing_common, self.branch_2_2_wing_common, self.branch_2_3_wing_common,
                self.branch_2_4_wing_common,
                self.branch_3_1_wing_common, self.branch_3_2_wing_common, self.branch_3_3_wing_common,
                self.branch_3_4_wing_common,
                self.branch_4_1_wing_common, self.branch_4_2_wing_common, self.branch_4_3_wing_common,
                self.branch_4_4_wing_common, ]

        for each in list:
            ctrl_name = each + '_Outer_Ctrl'
            bone_name = each + '_Bone'
            get_pos = cmds.xform(ctrl_name, q=1, ws=1, rp=1)
            cmds.select(cl=True)
            cmds.joint(n=bone_name, p=(get_pos[0], get_pos[1], get_pos[2]))

        # Template_L_Wing_Dragon_Finger_1_1_Tem_1_Outer_Ctrl
        finger_list = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Finger_*_1_Tem_" + str(
            self.val) + '_Outer_Ctrl'
        cmds.select(finger_list)
        sel_finger = cmds.ls(sl=True)
        a = 0
        while a < len(sel_finger):

            finger_name_list = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Finger_" + str(
                a + 1) + "_*_Tem_" + str(self.val) + '_Outer_Ctrl'
            cmds.select(finger_name_list)
            sel_finger_new = cmds.ls(sl=True)
            b = 0
            while b < len(sel_finger_new):
                split_name = sel_finger_new[b].split('_Outer_Ctrl')[0]
                get_pos = cmds.xform(sel_finger_new[b], q=1, ws=1, rp=1)
                bone_name = split_name + '_Bone'
                cmds.select(cl=True)
                cmds.joint(n=bone_name, p=(get_pos[0], get_pos[1], get_pos[2]))
                if b == 0:
                    hand_bone_jnt = self.hand_2_wing_common + '_Bone'
                    cmds.parent(bone_name, hand_bone_jnt)
                else:
                    split_name = sel_finger_new[b - 1].split('_Outer_Ctrl')[0]
                    previous_jnt = split_name + '_Bone'
                    cmds.parent(bone_name, previous_jnt)

                b += 1
            a += 1

        shoulder_jnt = self.shoulder_wing_common + '_Bone'
        upper_wing_jnt = self.upper_wing_common + '_Bone'
        lbow_jnt = self.lbow_wing_common + '_Bone'
        hand_jnt = self.hand_wing_common + '_Bone'
        hand_2_jnt = self.hand_2_wing_common + '_Bone'
        branc_1_1_jnt = self.branch_1_1_wing_common + '_Bone'
        branc_1_2_jnt = self.branch_1_2_wing_common + '_Bone'
        branc_1_3_jnt = self.branch_1_3_wing_common + '_Bone'
        branc_1_4_jnt = self.branch_1_4_wing_common + '_Bone'
        branc_2_1_jnt = self.branch_2_1_wing_common + '_Bone'
        branc_2_2_jnt = self.branch_2_2_wing_common + '_Bone'
        branc_2_3_jnt = self.branch_2_3_wing_common + '_Bone'
        branc_2_4_jnt = self.branch_2_4_wing_common + '_Bone'
        branc_3_1_jnt = self.branch_3_1_wing_common + '_Bone'
        branc_3_2_jnt = self.branch_3_2_wing_common + '_Bone'
        branc_3_3_jnt = self.branch_3_3_wing_common + '_Bone'
        branc_3_4_jnt = self.branch_3_4_wing_common + '_Bone'
        branc_4_1_jnt = self.branch_4_1_wing_common + '_Bone'
        branc_4_2_jnt = self.branch_4_2_wing_common + '_Bone'
        branc_4_3_jnt = self.branch_4_3_wing_common + '_Bone'
        branc_4_4_jnt = self.branch_4_4_wing_common + '_Bone'

        cmds.parent(upper_wing_jnt, shoulder_jnt)
        cmds.parent(lbow_jnt, upper_wing_jnt)
        cmds.parent(hand_jnt, lbow_jnt)
        cmds.parent(hand_2_jnt, hand_jnt)
        cmds.parent(branc_1_1_jnt, hand_2_jnt)
        cmds.parent(branc_1_2_jnt, branc_1_1_jnt)
        cmds.parent(branc_1_3_jnt, branc_1_2_jnt)
        cmds.parent(branc_1_4_jnt, branc_1_3_jnt)
        cmds.parent(branc_2_1_jnt, hand_2_jnt)
        cmds.parent(branc_2_2_jnt, branc_2_1_jnt)
        cmds.parent(branc_2_3_jnt, branc_2_2_jnt)
        cmds.parent(branc_2_4_jnt, branc_2_3_jnt)

        cmds.parent(branc_3_1_jnt, hand_2_jnt)
        cmds.parent(branc_3_2_jnt, branc_3_1_jnt)
        cmds.parent(branc_3_3_jnt, branc_3_2_jnt)
        cmds.parent(branc_3_4_jnt, branc_3_3_jnt)

        cmds.parent(branc_4_1_jnt, lbow_jnt)
        cmds.parent(branc_4_2_jnt, branc_4_1_jnt)
        cmds.parent(branc_4_3_jnt, branc_4_2_jnt)
        cmds.parent(branc_4_4_jnt, branc_4_3_jnt)

        # put everything in one grp
        self.helper_class.grp_create(object_name=shoulder_jnt,
                                     grp_name=grp_namne)

        self.helper_class.grp_create(object_name=grp_namne,
                                     grp_name=main_grp_name)

    def controller_twick_def(self):
        # get the no of the human main grp
        self.grp_list = ['Wing_Grp']
        for each_grp in self.grp_list:
            # list of the all children
            if cmds.objExists(each_grp):
                children_list = cmds.listRelatives(each_grp, children=True)
                for each_child in children_list:
                    # get all the controller data
                    self.wing_data(each_child)

                    self.final_controller_def()

    def final_controller_def(self):
        grp_name = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_" + str(
            self.val) + '_Twick_Ctrl_Grp'
        main_grp_name = 'Wing_Twick_Ctrl_Grp'

        if self.wing_side == 'L':
            col = 'Blue'
        else:
            col = 'Red'

        list = [self.upper_wing_common, self.lbow_wing_common, self.hand_wing_common, self.hand_2_wing_common,
                self.shoulder_wing_common]
        for each in list:
            ctrl_name = each + '_Inner_Ctrl'
            twick_ctrl = each + '_Twick_Ctrl'
            pos = cmds.xform(ctrl_name, q=1, ws=1, rp=1)

            self.controller_class.circle_ctrl()
            cmds.rename('circle_ctrl', twick_ctrl)
            cmds.setAttr((twick_ctrl + '.rz'), 90)
            cmds.setAttr((twick_ctrl + '.tx'), pos[0])
            cmds.setAttr((twick_ctrl + '.ty'), pos[1])
            cmds.setAttr((twick_ctrl + '.tz'), pos[2])

            self.helper_class.color_val(color=col,
                                        obj_name=twick_ctrl)

            self.helper_class.grp_create(object_name=twick_ctrl,
                                         grp_name=grp_name)

        list = [self.branch_1_1_wing_common, self.branch_1_2_wing_common, self.branch_1_3_wing_common,
                self.branch_1_4_wing_common,
                self.branch_2_1_wing_common, self.branch_2_2_wing_common, self.branch_2_3_wing_common,
                self.branch_2_4_wing_common,
                self.branch_3_1_wing_common, self.branch_3_2_wing_common, self.branch_3_3_wing_common,
                self.branch_3_4_wing_common,
                self.branch_4_1_wing_common, self.branch_4_2_wing_common, self.branch_4_3_wing_common,
                self.branch_4_4_wing_common]

        for each in list:
            ctrl_name = each + '_Inner_Ctrl'
            twick_ctrl = each + '_Twick_Ctrl'
            pos = cmds.xform(ctrl_name, q=1, ws=1, rp=1)

            self.controller_class.circle_ctrl()
            cmds.rename('circle_ctrl', twick_ctrl)
            cmds.setAttr((twick_ctrl + '.rx'), 90)
            cmds.setAttr((twick_ctrl + '.tx'), pos[0])
            cmds.setAttr((twick_ctrl + '.ty'), pos[1])
            cmds.setAttr((twick_ctrl + '.tz'), pos[2])

            self.helper_class.color_val(color=col,
                                        obj_name=twick_ctrl)

            self.helper_class.grp_create(object_name=twick_ctrl,
                                         grp_name=grp_name)

        # Template_L_Wing_Dragon_Finger_1_1_Tem_1_Outer_Ctrl
        finger_list = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Finger_*_1_Tem_" + str(
            self.val) + '_Inner_Ctrl'
        cmds.select(finger_list)
        sel_finger = cmds.ls(sl=True)
        a = 0
        while a < len(sel_finger):
            finger_name_list = self.prefix_name + "_" + self.wing_side + "_Wing_" + self.type + "_Finger_" + str(
                a + 1) + "_*_Tem_" + str(self.val) + '_Inner_Ctrl'
            cmds.select(finger_name_list)
            sel_finger_new = cmds.ls(sl=True)
            b = 0
            while b < len(sel_finger_new):
                split_name = sel_finger_new[b].split('_Inner_Ctrl')[0]
                get_pos = cmds.xform(sel_finger_new[b], q=1, ws=1, rp=1)
                twick_ctrl_name = split_name + '_Twick_Ctrl'
                self.controller_class.circle_ctrl()
                cmds.rename('circle_ctrl', twick_ctrl_name)
                cmds.setAttr((twick_ctrl_name + '.rz'), 90)
                cmds.DeleteHistory()
                cmds.FreezeTransformations()

                cmds.setAttr((twick_ctrl_name + '.tx'), get_pos[0])
                cmds.setAttr((twick_ctrl_name + '.ty'), get_pos[1])
                cmds.setAttr((twick_ctrl_name + '.tz'), get_pos[2])

                self.helper_class.color_val(color=col,
                                            obj_name=twick_ctrl_name)
                self.helper_class.grp_create(object_name=twick_ctrl_name,
                                             grp_name=grp_name)
                b += 1
            a += 1

        self.helper_class.grp_create(object_name=grp_name,
                                     grp_name=main_grp_name)

    def get_wing(self):
        list = []
        self.grp_list = ['Wing_Grp']
        for each_grp in self.grp_list:
            # list of the all children
            if cmds.objExists(each_grp):
                children_list = cmds.listRelatives(each_grp, children=True)
                for each_child in children_list:
                    # get all the controller data
                    list.append(each_child)
        return len(list)


























