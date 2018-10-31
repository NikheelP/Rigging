class LEG:
    def __init__(self):
        self.helper_class = helper.HELPER()
        self.connection_class = connection.CONNECTION()
        self.controller_class = controller_rig.controler()
        self.leg_finger_label = {}
        self.leg_finger_line_edit = {}

        self.finger_label_list = {}
        self.leg_finger_line_edit = {}

        self.sphere_list = []
        self.cluster_list = []
        self.cylinder_list = []
        self.ctrl_list = []
        self.crv_list = []

    def new(self, widget, layout):
        self.widget = widget
        self.layout = layout

        self.leg_grid_layout = QtGui.QGridLayout()
        self.leg_grid_layout.setObjectName("leg_grid_layout")

        # MIRROR CHECKBOX
        self.mirror_check_box = QtGui.QCheckBox(self.widget)
        self.mirror_check_box.setObjectName("mirror_check_box")
        self.mirror_check_box.setText('Mirror')
        self.mirror_check_box.setChecked(True)
        self.mirror_check_box.stateChanged.connect(self.mirror_status_def)
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

        # HIP CHECKBOX
        self.hip_check_box = QtGui.QCheckBox(self.widget)
        self.hip_check_box.setObjectName("hip_check_box")
        self.hip_check_box.setText('Hip')
        self.leg_grid_layout.addWidget(self.hip_check_box, 2, 0, 1, 1)

        # BUTT CHECKBOX
        self.butt_check_box = QtGui.QCheckBox(self.widget)
        self.butt_check_box.setObjectName("butt_check_box")
        self.butt_check_box.setText('Butt')
        self.leg_grid_layout.addWidget(self.butt_check_box, 2, 1, 1, 1)

        # THINE TO KNEE LABEL
        self.thine_to_knee_jnt_label = QtGui.QLabel(self.widget)
        self.thine_to_knee_jnt_label.setObjectName("thine_to_knee_jnt_label")
        self.thine_to_knee_jnt_label.setText('Thine to knee Joint')
        self.leg_grid_layout.addWidget(self.thine_to_knee_jnt_label, 3, 0, 1, 1)
        # THING TO KNEE LINE EDIT
        self.thine_to_knee_jnt_line_edit = QtGui.QLineEdit(self.widget)
        self.thine_to_knee_jnt_line_edit.setObjectName("thine_to_knee_jnt_line_edit")
        self.validator = QtGui.QDoubleValidator()
        self.thine_to_knee_jnt_line_edit.setValidator(self.validator)
        self.thine_to_knee_jnt_line_edit.setText(str(5))
        self.leg_grid_layout.addWidget(self.thine_to_knee_jnt_line_edit, 3, 1, 1, 3)

        # KNEE TO BALL LABEL
        self.knee_to_ball_jnt_label = QtGui.QLabel(self.widget)
        self.knee_to_ball_jnt_label.setObjectName("knee_to_ball_jnt_label")
        self.knee_to_ball_jnt_label.setText('Knee to Ball Joint')
        self.leg_grid_layout.addWidget(self.knee_to_ball_jnt_label, 4, 0, 1, 1)
        # KNEE TO BALL LINE EDIT
        self.knee_to_ball_jnt_line_edit = QtGui.QLineEdit(self.widget)
        self.knee_to_ball_jnt_line_edit.setObjectName("knee_to_ball_jnt_line_edit")
        self.knee_to_ball_jnt_line_edit.setValidator(self.validator)
        self.knee_to_ball_jnt_line_edit.setText(str(5))
        self.leg_grid_layout.addWidget(self.knee_to_ball_jnt_line_edit, 4, 1, 1, 3)

        # FOOT CHECKBOX
        self.foot_check_box = QtGui.QCheckBox(self.widget)
        self.foot_check_box.setObjectName("foot_check_box")
        self.foot_check_box.setText('Foot')
        self.foot_check_box.stateChanged.connect(self.leg_check_box_def)
        self.leg_grid_layout.addWidget(self.foot_check_box, 5, 0, 1, 1)

        # NO OF THE FINGER LABEL
        self.no_of_finger_label = QtGui.QLabel(self.widget)
        self.no_of_finger_label.setObjectName("no_of_finger_label")
        self.no_of_finger_label.setText('No of Finger')
        self.no_of_finger_label.setDisabled(True)
        self.leg_grid_layout.addWidget(self.no_of_finger_label, 6, 0, 1, 1)
        # NO FO THE FINGER LINE EDIT
        self.no_finger_line_edit = QtGui.QLineEdit(self.widget)
        self.no_finger_line_edit.setObjectName("no_finger_line_edit")
        self.no_finger_line_edit.setValidator(self.validator)
        self.no_finger_line_edit.setDisabled(True)
        self.no_finger_line_edit.textChanged.connect(self.no_finger_line_edit_def)
        self.leg_grid_layout.addWidget(self.no_finger_line_edit, 6, 1, 1, 3)

        # LEG BUTTON
        self.leg_create_button = QtGui.QPushButton(self.widget)
        self.leg_create_button.setObjectName("leg_create_button")
        self.leg_create_button.setText('Create Leg')
        self.leg_create_button.clicked.connect(self.leg_leg_def)
        self.leg_grid_layout.addWidget(self.leg_create_button, 7, 0, 1, 4)

        self.spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.leg_grid_layout.addItem(self.spacerItem, 8, 0, 1, 1)
        self.layout.addLayout(self.leg_grid_layout)

    def new_clear(self):
        self.helper_class.clearLayout(self.leg_grid_layout)

    def leg_leg_def(self):
        # query eveything from the ui
        self.mirror_check_box_query = self.mirror_check_box.isChecked()
        self.left_check_box_query = self.left_check_box.isChecked()
        self.right_check_box_query = self.right_check_box.isChecked()
        self.hip_check_box_query = self.hip_check_box.isChecked()
        self.butt_check_box_query = self.butt_check_box.isChecked()
        self.thine_to_knee_jnt_line_edit_line_edit_query = int(self.thine_to_knee_jnt_line_edit.text())
        self.knee_to_ball_jnt_line_edit_query = int(self.knee_to_ball_jnt_line_edit.text())
        self.foot_check_box_query = self.foot_check_box.isChecked()
        if self.foot_check_box_query == True:
            self.no_finger_line_edit_query = int(self.no_finger_line_edit.text())

        if self.left_check_box_query == True:
            self.left_leg_def()
        if self.right_check_box_query == True:
            self.right_leg_def()

    def left_leg_def(self):
        # Chck if left val
        if cmds.objExists("*_L_Leg_Tem_*_Main_Grp"):
            cmds.select("*_L_Leg_Tem_*_Main_Grp")
            sel_main_grp = cmds.ls(sl=True)
            len_sel_main_grp = len(sel_main_grp)
            self.val = len_sel_main_grp + 1
        else:
            self.val = 1

        self.leg_side = 'L'
        self.prefix_name = 'Template'
        self.base_ctrl_color = 'Blue'
        self.thine_pos = [8.177, 83.76, 2.826]
        self.shine_pos = [8.177, 48.005, 2.509]
        self.foot_pos = [8.177, 9.675, -0.261]
        self.ball_pos = [8.177, 0.681, 12.849]
        self.end_pos = [8.177, 0.266, 22.085]
        self.butt_pos = [8.177, 83.76, -2.319]
        self.double_knee_1_pos = [8.177, 50.532, 2.509]
        self.double_knee_2_pos = [8.177, 45, 2.509]
        self.hip_pos = [0, 88, 3]
        self.finger_default_pos = [7.764, 0, 16]

        # create a sphere
        self.leg_sphere_def()

        # create a cylinder
        self.leg_cylinder_def()

        # controller
        self.controller_def()

        if self.foot_check_box_query == True:
            self.finger_def()

        if self.butt_check_box_query == True:
            self.butt_def()

        if self.hip_check_box_query == True:
            if self.mirror_check_box_query != True:
                print('this is the left hop')
                self.hip_def()

        # final grp
        self.final_group()

    def right_leg_def(self):
        # Chck if left val
        if cmds.objExists("*_R_Leg_Tem_*_Main_Grp"):
            cmds.select("*_R_Leg_Tem_*_Main_Grp")
            sel_main_grp = cmds.ls(sl=True)
            len_sel_main_grp = len(sel_main_grp)
            self.val = len_sel_main_grp + 1
        else:
            self.val = 1

        self.leg_side = 'R'
        self.prefix_name = 'Template'
        self.base_ctrl_color = 'Red'
        self.thine_pos = [-8.177, 83.76, 2.826]
        self.shine_pos = [-8.177, 48.005, 2.509]
        self.foot_pos = [-8.177, 9.675, -0.261]
        self.ball_pos = [-8.177, 0.681, 12.849]
        self.end_pos = [-8.177, 0.266, 22.085]
        self.butt_pos = [-8.177, 83.76, -2.319]
        self.double_knee_1_pos = [-8.177, 50.532, 2.509]
        self.double_knee_2_pos = [-8.177, 45, 2.509]
        self.hip_pos = [0, 88, 3]
        self.finger_default_pos = [-7.764, 0, 16]

        # create a sphere
        self.leg_sphere_def()

        # create a cylinder
        self.leg_cylinder_def()

        # controller
        self.controller_def()

        if self.foot_check_box_query == True:
            self.finger_def()

        if self.hip_check_box_query == True:
            self.hip_def()

        if self.butt_check_box_query == True:
            self.butt_def()

        # final grp
        self.final_group()

        if self.mirror_check_box_query == True:
            self.mirror_value()

    def leg_sphere_def(self):
        self.sphere_list = []
        self.cluster_list = []
        self.cylinder_list = []
        self.ctrl_list = []
        self.crv_list = []

        # THINE
        self.thine_common = self.prefix_name + "_" + self.leg_side + "_Leg_Thine_Tem_" + str(self.val)
        self.thine_sphere_name = self.thine_common + "_Geo"
        self.thine_sphere_clu_name = self.thine_common + '_Clu'
        self.thine_sphere_clu_handle_name = self.thine_sphere_clu_name + 'Handle'
        self.sphere_list.append(self.thine_sphere_name)
        self.cluster_list.append(self.thine_sphere_clu_handle_name)
        self.helper_class.set_sphere_position(self.thine_sphere_name,
                                              self.thine_pos,
                                              self.thine_sphere_clu_name)

        # SHINE
        self.shine_common = self.prefix_name + "_" + self.leg_side + "_Leg_Shine_Tem_" + str(self.val)
        self.shine_sphere_name = self.shine_common + "_Geo"
        self.shine_sphere_clu_name = self.shine_common + '_Clu'
        self.shine_sphere_clu_handle_name = self.shine_sphere_clu_name + 'Handle'
        self.sphere_list.append(self.shine_sphere_name)
        self.cluster_list.append(self.shine_sphere_clu_handle_name)
        self.helper_class.set_sphere_position(self.shine_sphere_name,
                                              self.shine_pos,
                                              self.shine_sphere_clu_name)

        # FOOT
        self.foot_common = self.prefix_name + "_" + self.leg_side + "_Leg_Foot_Tem_" + str(self.val)
        self.foot_sphere_name = self.foot_common + "_Geo"
        self.foot_sphere_clu_name = self.foot_common + '_Clu'
        self.foot_sphere_clu_handle_name = self.foot_sphere_clu_name + 'Handle'
        self.sphere_list.append(self.foot_sphere_name)
        self.cluster_list.append(self.foot_sphere_clu_handle_name)
        self.helper_class.set_sphere_position(self.foot_sphere_name,
                                              self.foot_pos,
                                              self.foot_sphere_clu_name)

        # BALL
        self.ball_common = self.prefix_name + "_" + self.leg_side + "_Leg_Ball_Tem_" + str(self.val)
        self.ball_sphere_name = self.ball_common + "_Geo"
        self.ball_sphere_clu_name = self.ball_common + '_Clu'
        self.ball_sphere_clu_handle_name = self.ball_sphere_clu_name + 'Handle'
        self.sphere_list.append(self.ball_sphere_name)
        self.cluster_list.append(self.ball_sphere_clu_handle_name)
        self.helper_class.set_sphere_position(self.ball_sphere_name,
                                              self.ball_pos,
                                              self.ball_sphere_clu_name)

        # END
        self.end_common = self.prefix_name + "_" + self.leg_side + "_Leg_End_Tem_" + str(self.val)
        self.end_sphere_name = self.end_common + "_Geo"
        self.end_sphere_clu_name = self.end_common + '_Clu'
        self.end_sphere_clu_handle_name = self.end_sphere_clu_name + 'Handle'
        self.sphere_list.append(self.end_sphere_name)
        self.cluster_list.append(self.end_sphere_clu_handle_name)
        self.helper_class.set_sphere_position(self.end_sphere_name,
                                              self.end_pos,
                                              self.end_sphere_clu_name)

    def leg_cylinder_def(self):
        # THINE TO SHINE
        self.thine_to_shine_common = self.prefix_name + "_" + self.leg_side + "_Leg_Thine_to_Shine_Tem_" + str(self.val)
        self.thine_to_shine_cylinder_name = self.thine_to_shine_common + '_Geo'
        self.thine_to_shine_lower_cylinder_cluster_name = self.prefix_name + "_" + self.leg_side + "_Leg_Thine_to_Shine_Lower_Tem_" + str(
            self.val) + '_Clu'
        self.thine_to_shine_lower_cylinder_cluster_handle_name = self.thine_to_shine_lower_cylinder_cluster_name + 'Handle'
        self.thine_to_shine_upper_cylinder_cluster_name = self.prefix_name + "_" + self.leg_side + "_Leg_Thine_to_Shine_Upper_Tem_" + str(
            self.val) + '_Clu'
        self.thine_to_shine_upper_cylinder_cluster_handle_name = self.thine_to_shine_upper_cylinder_cluster_name + 'Handle'
        self.cylinder_rotate = [0, 0, 0]
        self.cluster_list.append(self.thine_to_shine_lower_cylinder_cluster_handle_name)
        self.cluster_list.append(self.thine_to_shine_upper_cylinder_cluster_handle_name)
        self.cylinder_list.append(self.thine_to_shine_cylinder_name)
        self.helper_class.set_cylinder_position(self.thine_to_shine_cylinder_name,
                                                self.thine_to_shine_lower_cylinder_cluster_name,
                                                self.thine_to_shine_upper_cylinder_cluster_name,
                                                self.shine_sphere_name,
                                                self.thine_sphere_name,
                                                rotate_val=[self.cylinder_rotate[0],
                                                            self.cylinder_rotate[1],
                                                            self.cylinder_rotate[2]])

        # SHINE TO FOOT
        self.shine_to_foot_common = self.prefix_name + "_" + self.leg_side + "_Leg_Shine_to_Foot_Tem_" + str(self.val)
        self.shine_to_foot_cylinder_name = self.shine_to_foot_common + '_Geo'
        self.shine_to_foot_lower_cylinder_cluster_name = self.prefix_name + "_" + self.leg_side + "_Leg_Shine_to_Foot_Lower_Tem_" + str(
            self.val) + '_Clu'
        self.shine_to_foot_lower_cylinder_cluster_handle_name = self.shine_to_foot_lower_cylinder_cluster_name + 'Handle'
        self.shine_to_foot_upper_cylinder_cluster_name = self.prefix_name + "_" + self.leg_side + "_Leg_Shine_to_Foot_Upper_Tem_" + str(
            self.val) + '_Clu'
        self.shine_to_foot_upper_cylinder_cluster_handle_name = self.shine_to_foot_upper_cylinder_cluster_name + 'Handle'
        self.cylinder_rotate = [0, 0, 0]
        self.cluster_list.append(self.shine_to_foot_lower_cylinder_cluster_handle_name)
        self.cluster_list.append(self.shine_to_foot_upper_cylinder_cluster_handle_name)
        self.cylinder_list.append(self.shine_to_foot_cylinder_name)
        self.helper_class.set_cylinder_position(self.shine_to_foot_cylinder_name,
                                                self.shine_to_foot_lower_cylinder_cluster_name,
                                                self.shine_to_foot_upper_cylinder_cluster_name,
                                                self.foot_sphere_name,
                                                self.shine_sphere_name,
                                                rotate_val=[self.cylinder_rotate[0],
                                                            self.cylinder_rotate[1],
                                                            self.cylinder_rotate[2]])

        # FOOT TO BALL
        self.foot_to_ball_common = self.prefix_name + "_" + self.leg_side + "_Leg_Foot_to_Ball_Tem_" + str(self.val)
        self.foot_to_ball_cylinder_name = self.foot_to_ball_common + '_Geo'
        self.foot_to_ball_lower_cylinder_cluster_name = self.prefix_name + "_" + self.leg_side + "_Leg_Foot_to_Ball_Lower_Tem_" + str(
            self.val) + '_Clu'
        self.foot_to_ball_lower_cylinder_cluster_handle_name = self.foot_to_ball_lower_cylinder_cluster_name + 'Handle'
        self.foot_to_ball_upper_cylinder_cluster_name = self.prefix_name + "_" + self.leg_side + "_Leg_Foot_to_Ball_Upper_Tem_" + str(
            self.val) + '_Clu'
        self.foot_to_ball_upper_cylinder_cluster_handle_name = self.foot_to_ball_upper_cylinder_cluster_name + 'Handle'
        self.cylinder_rotate = [90, 0, 0]
        self.cluster_list.append(self.foot_to_ball_lower_cylinder_cluster_handle_name)
        self.cluster_list.append(self.foot_to_ball_upper_cylinder_cluster_handle_name)
        self.cylinder_list.append(self.foot_to_ball_cylinder_name)
        self.helper_class.set_cylinder_position(self.foot_to_ball_cylinder_name,
                                                self.foot_to_ball_lower_cylinder_cluster_name,
                                                self.foot_to_ball_upper_cylinder_cluster_name,
                                                self.foot_sphere_name,
                                                self.ball_sphere_name,
                                                rotate_val=[self.cylinder_rotate[0],
                                                            self.cylinder_rotate[1],
                                                            self.cylinder_rotate[2]])

        # BALL TO END
        self.ball_to_end_common = self.prefix_name + "_" + self.leg_side + "_Leg_Ball_to_End_Tem_" + str(self.val)
        self.ball_to_end_cylinder_name = self.ball_to_end_common + '_Geo'
        self.ball_to_end_lower_cylinder_cluster_name = self.prefix_name + "_" + self.leg_side + "_Leg_Ball_to_End_Lower_Tem_" + str(
            self.val) + '_Clu'
        self.ball_to_end_lower_cylinder_cluster_handle_name = self.ball_to_end_lower_cylinder_cluster_name + 'Handle'
        self.ball_to_end_upper_cylinder_cluster_name = self.prefix_name + "_" + self.leg_side + "_Leg_Ball_to_End_Upper_Tem_" + str(
            self.val) + '_Clu'
        self.ball_to_end_upper_cylinder_cluster_handle_name = self.ball_to_end_upper_cylinder_cluster_name + 'Handle'
        self.cylinder_rotate = [90, 0, 0]
        self.cluster_list.append(self.ball_to_end_lower_cylinder_cluster_handle_name)
        self.cluster_list.append(self.ball_to_end_upper_cylinder_cluster_handle_name)
        self.cylinder_list.append(self.ball_to_end_cylinder_name)
        self.helper_class.set_cylinder_position(self.ball_to_end_cylinder_name,
                                                self.ball_to_end_lower_cylinder_cluster_name,
                                                self.ball_to_end_upper_cylinder_cluster_name,
                                                self.ball_sphere_name,
                                                self.end_sphere_name,
                                                rotate_val=[self.cylinder_rotate[0],
                                                            self.cylinder_rotate[1],
                                                            self.cylinder_rotate[2]])

        # SET THE BUTT

    def controller_def(self):
        # CREATE CONTROLLER
        self.ctrl_lower_size = [0.5, 0.5, 0.5]
        self.ctrl_outer_size = [1.5, 1.5, 1.5]
        self.ctrl_rotate = [0, 0, 0]
        self.base_ctrl_freez_trans = True
        self.base_ctrl_freez_rotate = True
        self.base_ctrl_freez_scale = True

        # THINE CONTROLLER
        self.thine_const_list = [self.thine_sphere_clu_handle_name,
                                 self.thine_to_shine_upper_cylinder_cluster_handle_name]
        self.controller_small_big(base_name=self.thine_common,
                                  parent_list=self.thine_const_list,
                                  pos=self.thine_pos,
                                  ctrl_rotate=self.ctrl_rotate)
        self.thine_inner_ctrl = self.thine_common + '_Inner_Ctrl'
        self.thine_outer_ctrl = self.thine_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.thine_inner_ctrl)
        self.ctrl_list.append(self.thine_outer_ctrl)

        # SHINE CONTROLLER
        self.shine_const_list = [self.shine_sphere_clu_handle_name,
                                 self.thine_to_shine_lower_cylinder_cluster_handle_name,
                                 self.shine_to_foot_upper_cylinder_cluster_handle_name]
        self.controller_small_big(base_name=self.shine_common,
                                  parent_list=self.shine_const_list,
                                  pos=self.shine_pos,
                                  ctrl_rotate=self.ctrl_rotate)
        self.shine_inner_ctrl = self.shine_common + '_Inner_Ctrl'
        self.shine_outer_ctrl = self.shine_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.shine_inner_ctrl)
        self.ctrl_list.append(self.shine_outer_ctrl)
        cmds.select(self.shine_outer_ctrl,
                    self.thine_outer_ctrl)
        cmds.parent()

        # FOOT CONTROLLER
        self.foot_const_list = [self.foot_sphere_clu_handle_name,
                                self.shine_to_foot_lower_cylinder_cluster_handle_name,
                                self.foot_to_ball_lower_cylinder_cluster_handle_name]
        self.controller_small_big(base_name=self.foot_common,
                                  parent_list=self.foot_const_list,
                                  pos=self.foot_pos,
                                  ctrl_rotate=self.ctrl_rotate)
        self.foot_inner_ctrl = self.foot_common + '_Inner_Ctrl'
        self.foot_outer_ctrl = self.foot_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.foot_inner_ctrl)
        self.ctrl_list.append(self.foot_outer_ctrl)
        cmds.select(self.foot_outer_ctrl,
                    self.shine_outer_ctrl)
        cmds.parent()

        # BALL CONTROLLER
        self.ctrl_rotate = [90, 0, 0]
        self.ball_const_list = [self.ball_sphere_clu_handle_name,
                                self.foot_to_ball_upper_cylinder_cluster_handle_name,
                                self.ball_to_end_lower_cylinder_cluster_handle_name]
        self.controller_small_big(base_name=self.ball_common,
                                  parent_list=self.ball_const_list,
                                  pos=self.ball_pos,
                                  ctrl_rotate=self.ctrl_rotate)
        self.ball_inner_ctrl = self.ball_common + '_Inner_Ctrl'
        self.ball_outer_ctrl = self.ball_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.ball_inner_ctrl)
        self.ctrl_list.append(self.ball_outer_ctrl)
        cmds.select(self.ball_outer_ctrl,
                    self.foot_outer_ctrl)
        cmds.parent()

        # END CONTROLLER
        self.end_const_list = [self.end_sphere_clu_handle_name,
                               self.ball_to_end_upper_cylinder_cluster_handle_name]
        self.controller_small_big(base_name=self.end_common,
                                  parent_list=self.end_const_list,
                                  pos=self.end_pos,
                                  ctrl_rotate=self.ctrl_rotate)
        self.end_inner_ctrl = self.end_common + '_Inner_Ctrl'
        self.end_outer_ctrl = self.end_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.end_inner_ctrl)
        self.ctrl_list.append(self.end_outer_ctrl)
        cmds.select(self.end_outer_ctrl,
                    self.ball_outer_ctrl)
        cmds.parent()

        # roll bone
        self.roll_bone('Upper',
                       self.thine_inner_ctrl,
                       self.shine_inner_ctrl,
                       self.thine_to_knee_jnt_line_edit_line_edit_query)
        self.roll_bone('Lower',
                       self.shine_inner_ctrl,
                       self.foot_inner_ctrl,
                       self.knee_to_ball_jnt_line_edit_query)

    def controller_small_big(self, base_name, parent_list, pos, ctrl_rotate):
        self.ctrl_lower_size = [0.5, 0.5, 0.5]
        self.ctrl_outer_size = [0.8, 0.8, 0.8]
        self.base_ctrl_freez_trans = True
        self.base_ctrl_freez_rotate = True
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
        self.base_ctrl_roate = self.ctrl_rotate
        self.base_parent_const_list = []
        self.helper_class.set_controller(self.base_outer_ctrl, pos, self.base_ctrl_size_ctrl,
                                         self.base_ctrl_roate, self.base_parent_const_list, self.base_parent_const_list,
                                         color=self.base_ctrl_color,
                                         freez_trans=self.base_ctrl_freez_trans,
                                         freez_rotate=self.base_ctrl_freez_rotate,
                                         freez_scale=self.base_ctrl_freez_scale)
        cmds.select(self.base_inner_ctrl, self.base_outer_ctrl)
        cmds.parent()

    def butt_def(self):

        # create a sphere
        self.butt_common = self.prefix_name + "_" + self.leg_side + "_Leg_Butt_Tem_" + str(self.val)
        self.butt_sphere_name = self.butt_common + "_Geo"
        self.butt_sphere_clu_name = self.butt_common + '_Clu'
        self.butt_sphere_clu_handle_name = self.butt_sphere_clu_name + 'Handle'
        self.sphere_list.append(self.butt_sphere_name)
        self.cluster_list.append(self.butt_sphere_clu_handle_name)
        self.helper_class.set_sphere_position(self.butt_sphere_name,
                                              self.butt_pos,
                                              self.butt_sphere_clu_name)

        # cylinder
        self.thine_to_butt_common = self.prefix_name + "_" + self.leg_side + "_Leg_Thine_to_Butt_Tem_" + str(self.val)
        self.thine_to_butt_cylinder_name = self.thine_to_butt_common + '_Geo'
        self.thine_to_butt_lower_cylinder_cluster_name = self.prefix_name + "_" + self.leg_side + "_Leg_Thine_to_Butt_Lower_Tem_" + str(
            self.val) + '_Clu'
        self.thine_to_butt_lower_cylinder_cluster_handle_name = self.thine_to_butt_lower_cylinder_cluster_name + 'Handle'
        self.thine_to_butt_upper_cylinder_cluster_name = self.prefix_name + "_" + self.leg_side + "_Leg_Thine_to_Butt_Upper_Tem_" + str(
            self.val) + '_Clu'
        self.thine_to_butt_upper_cylinder_cluster_handle_name = self.thine_to_butt_upper_cylinder_cluster_name + 'Handle'
        self.cylinder_rotate = [90, 0, 0]
        self.cluster_list.append(self.thine_to_butt_lower_cylinder_cluster_handle_name)
        self.cluster_list.append(self.thine_to_butt_upper_cylinder_cluster_handle_name)
        self.cylinder_list.append(self.thine_to_butt_cylinder_name)
        self.helper_class.set_cylinder_position(self.thine_to_butt_cylinder_name,
                                                self.thine_to_butt_lower_cylinder_cluster_name,
                                                self.thine_to_butt_upper_cylinder_cluster_name,
                                                self.butt_sphere_name,
                                                self.thine_sphere_name,
                                                rotate_val=[self.cylinder_rotate[0],
                                                            self.cylinder_rotate[1],
                                                            self.cylinder_rotate[2]])

        self.ctrl_rotate = [90, 0, 0]
        self.butt_const_list = [self.butt_sphere_clu_handle_name,
                                self.thine_to_butt_lower_cylinder_cluster_handle_name]
        self.controller_small_big(base_name=self.butt_common,
                                  parent_list=self.butt_const_list,
                                  pos=self.butt_pos,
                                  ctrl_rotate=self.ctrl_rotate)
        self.butt_inner_ctrl = self.butt_common + '_Inner_Ctrl'
        self.butt_outer_ctrl = self.butt_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.butt_inner_ctrl)
        self.ctrl_list.append(self.butt_outer_ctrl)
        cmds.select(self.butt_outer_ctrl,
                    self.thine_outer_ctrl)
        cmds.parent()
        parent_list = [self.thine_to_butt_upper_cylinder_cluster_handle_name]
        self.helper_class.parent_constrain(self.thine_outer_ctrl, parent_list)

    def roll_bone(self, type, upper_object, lower_object, no_of_bone):
        # create a curve
        self.curve_common = self.prefix_name + "_" + self.leg_side + "_Leg_" + type + "_Tem_" + str(self.val)
        self.curve_name = self.curve_common + '_Crv'
        self.curve_shape_name = self.curve_name + 'Shape'
        self.curve_0_clu_name = self.prefix_name + "_" + self.leg_side + "_Leg_" + type + "_0_Tem_" + str(
            self.val) + '_Clu'
        self.curve_0_clu_handle_name = self.curve_0_clu_name + 'Handle'
        self.curve_1_clu_name = self.prefix_name + "_" + self.leg_side + "_Leg_" + type + "_1_Tem_" + str(
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
        toal_minus = 0
        value = 1.0 - toal_minus
        average_val = value / (no_of_bone + 1.0)
        start_val = average_val

        while a < no_of_bone:
            common_name = self.prefix_name + "_" + self.leg_side + "_Leg_" + type + "_" + str(a) + "_Tem_" + str(
                self.val)
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

            cmds.setAttr((self.poc_name + '.parameter'), start_val)
            start_val += average_val

            # setAttr "Template_L_Arm_Lower_0_Tem_1_POC.parameter" 0.2;

            a += 1

    def finger_def(self):

        a = 0
        self.locator_list = []
        x_val = 0
        while a < self.no_finger_line_edit_query:
            locator_name = 'Finger_' + str(a) + '_Loc'
            self.locator_list.append(locator_name)
            cmds.spaceLocator(n=locator_name, p=(x_val, 0, 0))
            cmds.select(locator_name)
            cmds.CenterPivot()
            x_val += 3
            a += 1
        self.locator_grp_name = 'Finger_Grp'
        cmds.select('Finger_*_Loc')
        cmds.group(n=self.locator_grp_name)
        cmds.select(self.locator_grp_name)
        cmds.CenterPivot()
        cmds.move(0, 0, 0, rpr=True)
        cmds.FreezeTransformations()
        cmds.move(self.finger_default_pos[0],
                  self.finger_default_pos[1],
                  self.finger_default_pos[2])
        if self.leg_side == 'R':
            cmds.setAttr((self.locator_grp_name + '.rz'), 180)
        # now get each positiona dn create a finger

        a = 0
        while a < self.no_finger_line_edit_query:

            new_loc = 'New_Loc_' + str(a)
            cmds.spaceLocator(n=new_loc, p=(0, 0, 0))
            cmds.parentConstraint(self.locator_list[a], new_loc, mo=False)
            self.loc_position = cmds.getAttr(new_loc + '.t')[0]
            cmds.select(new_loc)
            cmds.delete()

            self.finger_query = int(self.leg_finger_line_edit[a].text())
            b = 0
            x_value = self.loc_position[2]
            while b < self.finger_query:
                self.cylinder_rotate = [90, 0, 0]
                self.finger_common = self.prefix_name + "_" + self.leg_side + "_Leg_Finger_" + str(a + 1) + '_' + str(
                    b + 1) + "_Tem_" + str(self.val)
                self.finger_sphere_name = self.finger_common + "_Geo"
                self.finger_sphere_clu_name = self.finger_common + '_Clu'
                self.finger_sphere_clu_handle_name = self.finger_sphere_clu_name + 'Handle'
                # self.finger_default_pos = [61.0,0,]

                self.finger_pos = [self.loc_position[0], 0, x_value]
                self.sphere_list.append(self.finger_sphere_name)
                self.cluster_list.append(self.finger_sphere_clu_handle_name)
                self.helper_class.set_sphere_position(self.finger_sphere_name,
                                                      self.finger_pos,
                                                      self.finger_sphere_clu_name)

                if b == 0:
                    self.cylinder_name = self.prefix_name + '_' + self.leg_side + "_Leg_Finger_Leg_to_" + str(
                        a + 1) + "_" + str(b + 1) + "_Tem_" + str(self.val) + "_Cylinder_Geo"
                    self.cylinder_upper_cluster_name = self.prefix_name + '_' + self.leg_side + "_Leg_Finger_Leg_to_Upper_" + str(
                        a + 1) + "_" + str(b + 1) + "_Tem_" + str(self.val) + "_Clu"
                    self.finger_to_hand_cylinder_upper_cluster_handle_name = self.cylinder_upper_cluster_name + 'Handle'
                    self.cylinder_lower_cluster_name = self.prefix_name + '_' + self.leg_side + "_Leg_Finger_Leg_to_Lower_" + str(
                        a + 1) + "_" + str(b + 1) + "_Tem_" + str(self.val) + "_Clu"
                    self.cylinder_lower_cluster_handle_name = self.cylinder_lower_cluster_name + 'Handle'
                    self.helper_class.set_cylinder_position(self.cylinder_name,
                                                            self.cylinder_lower_cluster_name,
                                                            self.cylinder_upper_cluster_name,
                                                            self.ball_sphere_name,
                                                            self.finger_sphere_name,
                                                            rotate_val=self.cylinder_rotate)
                    self.cluster_list.append(self.finger_to_hand_cylinder_upper_cluster_handle_name)
                    self.cluster_list.append(self.cylinder_lower_cluster_handle_name)
                    self.cylinder_list.append(self.cylinder_name)

                    self.base_parent_const_list = [self.finger_sphere_clu_handle_name,
                                                   self.finger_to_hand_cylinder_upper_cluster_handle_name]
                    cmds.parentConstraint(self.ball_outer_ctrl, self.cylinder_lower_cluster_handle_name, mo=False)
                    ctrl_rotate = (90, 0, 0)
                    self.controller_small_big(base_name=self.finger_common,
                                              parent_list=self.base_parent_const_list,
                                              pos=self.finger_pos,
                                              ctrl_rotate=ctrl_rotate)
                    self.leg_shoulder_inner_ctrl = self.finger_common + '_Inner_Ctrl'
                    self.leg_shoulder_outer_ctrl = self.finger_common + '_Outer_Ctrl'
                    self.ctrl_list.append(self.leg_shoulder_inner_ctrl)
                    self.ctrl_list.append(self.leg_shoulder_outer_ctrl)

                if b + 1 != 1:
                    self.cylinder_name = self.prefix_name + '_' + self.leg_side + "_Leg_Finger_" + str(
                        a + 1) + "_" + str(b + 1) + "_Tem_" + str(self.val) + "_Cylinder_Geo"
                    self.cylinder_upper_cluster_name = self.prefix_name + '_' + self.leg_side + "_Leg_Finger_Upper_" + str(
                        a + 1) + "_" + str(b + 1) + "_Tem_" + str(self.val) + "_Clu"
                    self.cylinder_upper_cluster_handle_name = self.cylinder_upper_cluster_name + 'Handle'
                    self.cylinder_lower_cluster_name = self.prefix_name + '_' + self.leg_side + "_Leg_Finger_Lower_" + str(
                        a + 1) + "_" + str(b + 1) + "_Tem_" + str(self.val) + "_Clu"
                    self.cylinder_lower_cluster_handle_name = self.cylinder_lower_cluster_name + 'Handle'
                    self.current_sphere_name = self.prefix_name + '_' + self.leg_side + "_Leg_Finger_" + str(
                        a + 1) + "_" + str(b) + "_Tem_" + str(self.val) + "_Geo"
                    self.helper_class.set_cylinder_position(self.cylinder_name,
                                                            self.cylinder_lower_cluster_name,
                                                            self.cylinder_upper_cluster_name,
                                                            self.current_sphere_name,
                                                            self.finger_sphere_name,
                                                            rotate_val=self.cylinder_rotate)
                    self.cluster_list.append(self.cylinder_upper_cluster_handle_name)
                    self.cluster_list.append(self.cylinder_lower_cluster_handle_name)
                    self.cylinder_list.append(self.cylinder_name)

                    # create a controller and snap
                    previous_upper_cluster_handle_name = self.prefix_name + "_" + self.leg_side + "_Leg_Finger_Upper_" + str(
                        a + 1) + '_' + str(b + 1) + "_Tem_" + str(self.val) + '_CluHandle'
                    next_lower_cluster_handle_name = self.prefix_name + "_" + self.leg_side + "_Leg_Finger_Lower_" + str(
                        a + 1) + '_' + str(b + 1) + "_Tem_" + str(self.val) + '_CluHandle'
                    self.base_parent_const_list = [self.finger_sphere_clu_handle_name,
                                                   previous_upper_cluster_handle_name]
                    ctrl_rotate = (90, 0, 0)
                    self.controller_small_big(base_name=self.finger_common,
                                              parent_list=self.base_parent_const_list,
                                              pos=self.finger_pos,
                                              ctrl_rotate=ctrl_rotate)
                    self.leg_shoulder_inner_ctrl = self.finger_common + '_Inner_Ctrl'
                    self.leg_shoulder_outer_ctrl = self.finger_common + '_Outer_Ctrl'
                    self.ctrl_list.append(self.leg_shoulder_inner_ctrl)
                    self.ctrl_list.append(self.leg_shoulder_outer_ctrl)

                x_value += 3

                b += 1

            a += 1

        a = 0
        while a < self.no_finger_line_edit_query:
            b = 0
            while b < self.finger_query:

                # Template_L_Leg_Finger_Lower_1_2_Tem_1_CluHandle
                common_ctrl_name = self.prefix_name + "_" + self.leg_side + "_Leg_Finger_" + str(a + 1) + '_' + str(
                    b + 1) + "_Tem_" + str(self.val)
                common_lower_cluster_handle_name = self.prefix_name + "_" + self.leg_side + "_Leg_Finger_Lower_" + str(
                    a + 1) + '_' + str(b + 2) + "_Tem_" + str(self.val)

                inner_ctrl_name = common_ctrl_name + '_Inner_Ctrl'
                outer_ctrl_name = common_ctrl_name + '_Outer_Ctrl'
                lower_cluster_handle = common_lower_cluster_handle_name + '_CluHandle'
                if cmds.objExists(lower_cluster_handle):
                    cmds.parentConstraint(inner_ctrl_name, lower_cluster_handle, mo=False)
                next_common = self.prefix_name + "_" + self.leg_side + "_Leg_Finger_" + str(a + 1) + '_' + str(
                    b + 2) + "_Tem_" + str(self.val)
                if b == 0:
                    cmds.select(outer_ctrl_name, self.ball_outer_ctrl)
                    cmds.parent()

                next_outer_ctrl = next_common + '_Outer_Ctrl'
                if cmds.objExists(next_outer_ctrl):
                    cmds.select(next_outer_ctrl, outer_ctrl_name)
                    cmds.parent()

                b += 1
            a += 1
        cmds.select(self.locator_grp_name)
        cmds.delete()

    def hip_def(self):
        # create a sphere
        self.hip_common = self.prefix_name + "_Leg_Hip_Tem_" + str(self.val)
        self.hip_sphere_name = self.hip_common + "_Geo"
        self.ctrl_rotate = [0, 0, 0]
        if cmds.objExists(self.hip_sphere_name):
            pass
        else:
            self.hip_sphere_clu_name = self.hip_common + '_Clu'
            self.hip_sphere_clu_handle_name = self.hip_sphere_clu_name + 'Handle'
            self.sphere_list.append(self.hip_sphere_name)
            self.cluster_list.append(self.hip_sphere_clu_handle_name)
            self.helper_class.set_sphere_position(self.hip_sphere_name,
                                                  self.hip_pos,
                                                  self.hip_sphere_clu_name)

        # create a cylinder
        self.thine_to_hip_common = self.prefix_name + "_" + self.leg_side + "_Leg_Thine_to_Hip_Tem_" + str(self.val)
        self.thine_to_hip_cylinder_name = self.thine_to_hip_common + '_Geo'
        self.thine_to_hip_lower_cylinder_cluster_name = self.prefix_name + "_" + self.leg_side + "_Leg_Thine_to_Hip_Lower_Tem_" + str(
            self.val) + '_Clu'
        self.thine_to_hip_lower_cylinder_cluster_handle_name = self.thine_to_hip_lower_cylinder_cluster_name + 'Handle'
        self.thine_to_hip_upper_cylinder_cluster_name = self.prefix_name + "_" + self.leg_side + "_Leg_Thine_to_Hip_Upper_Tem_" + str(
            self.val) + '_Clu'
        self.thine_to_hip_upper_cylinder_cluster_handle_name = self.thine_to_hip_upper_cylinder_cluster_name + 'Handle'
        self.cylinder_rotate = [0, 0, 0]
        self.cluster_list.append(self.thine_to_hip_lower_cylinder_cluster_handle_name)
        self.cluster_list.append(self.thine_to_hip_upper_cylinder_cluster_handle_name)
        self.cylinder_list.append(self.thine_to_hip_cylinder_name)
        self.helper_class.set_cylinder_position(self.thine_to_hip_cylinder_name,
                                                self.thine_to_hip_lower_cylinder_cluster_name,
                                                self.thine_to_hip_upper_cylinder_cluster_name,
                                                self.hip_sphere_name,
                                                self.thine_sphere_name,
                                                rotate_val=[self.cylinder_rotate[0],
                                                            self.cylinder_rotate[1],
                                                            self.cylinder_rotate[2]])
        # do parent const
        cmds.parentConstraint(self.thine_inner_ctrl, self.thine_to_hip_upper_cylinder_cluster_handle_name, mo=False)

        if self.mirror_check_box_query == True:
            self.leg_side = 'L'
            # create a cylinder
            self.left_thine_to_hip_common = self.prefix_name + "_" + self.leg_side + "_Leg_Thine_to_Hip_Tem_" + str(
                self.val)
            self.thine_to_hip_cylinder_name = self.left_thine_to_hip_common + '_Geo'
            self.thine_to_hip_lower_cylinder_cluster_name = self.prefix_name + "_" + self.leg_side + "_Leg_Thine_to_Hip_Lower_Tem_" + str(
                self.val) + '_Clu'
            self.left_thine_to_hip_lower_cylinder_cluster_handle_name = self.thine_to_hip_lower_cylinder_cluster_name + 'Handle'
            self.thine_to_hip_upper_cylinder_cluster_name = self.prefix_name + "_" + self.leg_side + "_Leg_Thine_to_Hip_Upper_Tem_" + str(
                self.val) + '_Clu'
            self.thine_to_hip_upper_cylinder_cluster_handle_name = self.thine_to_hip_upper_cylinder_cluster_name + 'Handle'
            self.hip_common = self.prefix_name + "_Leg_Hip_Tem_" + str(self.val)
            self.hip_sphere_name = self.hip_common + "_Geo"
            self.thine_common = self.prefix_name + "_" + self.leg_side + "_Leg_Thine_Tem_" + str(self.val)
            self.thine_sphere_name = self.thine_common + "_Geo"
            self.cylinder_rotate = [0, 0, 0]
            self.cluster_list.append(self.left_thine_to_hip_lower_cylinder_cluster_handle_name)
            self.cluster_list.append(self.thine_to_hip_upper_cylinder_cluster_handle_name)
            self.cylinder_list.append(self.thine_to_hip_cylinder_name)
            self.helper_class.set_cylinder_position(self.thine_to_hip_cylinder_name,
                                                    self.thine_to_hip_lower_cylinder_cluster_name,
                                                    self.thine_to_hip_upper_cylinder_cluster_name,
                                                    self.hip_sphere_name,
                                                    self.thine_sphere_name,
                                                    rotate_val=[self.cylinder_rotate[0],
                                                                self.cylinder_rotate[1],
                                                                self.cylinder_rotate[2]])
            # Template_R_Leg_Thine_Tem_1_Inner_Ctrl
            self.left_thinner_inner_ctrl = self.prefix_name + "_" + self.leg_side + "_Leg_Thine_Tem_" + str(
                self.val) + '_Inner_Ctrl'
            cmds.parentConstraint(self.left_thinner_inner_ctrl, self.thine_to_hip_upper_cylinder_cluster_handle_name,
                                  mo=False)

            # create a controller
            # THINE CONTROLLER
            new_color = self.base_ctrl_color
            self.base_ctrl_color = 'Yellow'
            self.hip_const_list = [self.hip_sphere_clu_handle_name,
                                   self.left_thine_to_hip_lower_cylinder_cluster_handle_name,
                                   self.thine_to_hip_lower_cylinder_cluster_handle_name]
            self.controller_small_big(base_name=self.hip_common,
                                      parent_list=self.hip_const_list,
                                      pos=self.hip_pos,
                                      ctrl_rotate=self.ctrl_rotate)
            self.hip_inner_ctrl = self.hip_common + '_Inner_Ctrl'
            self.hip_outer_ctrl = self.hip_common + '_Outer_Ctrl'

            self.base_ctrl_color = new_color
            # parent the both thine ctrl

            self.leg_side = 'R'

    def final_group(self, hip=True):
        self.sphere_group_name = self.prefix_name + '_' + self.leg_side + "_Leg_Tem_" + str(self.val) + "_Sphere_Grp"
        cmds.select(cl=True)
        for each in self.sphere_list:
            self.helper_class.parent_child_grp(parent=self.sphere_group_name,
                                               child=each)

        self.cluster_group_name = self.prefix_name + '_' + self.leg_side + "_Leg_Tem_" + str(self.val) + "_Cluster_Grp"
        cmds.select(cl=True)
        for each in self.cluster_list:
            self.helper_class.parent_child_grp(parent=self.cluster_group_name,
                                               child=each,
                                               vis=True)

        self.cylinder_group_name = self.prefix_name + '_' + self.leg_side + "_Leg_Tem_" + str(
            self.val) + "_Cylinder_Grp"
        cmds.select(cl=True)
        for each in self.cylinder_list:
            self.helper_class.parent_child_grp(parent=self.cylinder_group_name,
                                               child=each)

        self.curve_group_name = self.prefix_name + '_' + self.leg_side + "_Leg_Tem_" + str(self.val) + "_Crv_Grp"
        cmds.select(cl=True)
        for each in self.crv_list:
            self.helper_class.parent_child_grp(parent=self.curve_group_name,
                                               child=each,
                                               vis=True)

        self_outer = self.prefix_name + '_Leg_Hip_Tem_' + str(self.val) + "_Outer_Ctrl"
        if hip == True:

            if cmds.objExists(self_outer):
                if self.mirror_check_box_query == True:
                    # do this for left and right
                    # RIGHT
                    right_outer_grp_name = self.thine_outer_ctrl + '_Hip_Outer_Grp'

                    # RIGHT
                    left_outer_grp_name = right_outer_grp_name.replace('R', 'L')
                    left_outer_name = self.thine_outer_ctrl.replace('R', 'L')

                    cmds.select(left_outer_name)
                    cmds.group(n=left_outer_grp_name)
                    cmds.CenterPivot()
                    cmds.parentConstraint(self_outer, left_outer_grp_name, mo=True)

                right_outer_grp_name = self.thine_outer_ctrl + '_Hip_Outer_Grp'
                cmds.select(self.thine_outer_ctrl)
                cmds.group(n=right_outer_grp_name)
                cmds.CenterPivot()
                cmds.parentConstraint(self_outer, right_outer_grp_name, mo=True)

                # put everything in one group
                cmds.select(self.sphere_group_name,
                            self.cluster_group_name,
                            self.cylinder_group_name,
                            right_outer_grp_name,
                            self_outer,
                            self.curve_group_name)
                grp_list = [self.sphere_group_name, self.cluster_group_name,
                            self.cylinder_group_name, right_outer_grp_name, self_outer,
                            self.curve_group_name]
                self.main_grp_name = self.prefix_name + '_' + self.leg_side + '_Leg_Tem_' + str(self.val) + '_Main_Grp'
                for each in grp_list:
                    self.helper_class.parent_child_grp(parent=self.main_grp_name,
                                                       child=each)

        grp_list = [self.sphere_group_name, self.cluster_group_name,
                    self.cylinder_group_name, self.thine_outer_ctrl,
                    self.curve_group_name]
        self.main_grp_name = self.prefix_name + '_' + self.leg_side + '_Leg_Tem_' + str(self.val) + '_Main_Grp'
        for each in grp_list:
            self.helper_class.parent_child_grp(parent=self.main_grp_name,
                                               child=each)

        # create a mirror object

        cmds.select(self.main_grp_name)
        self.leg_grp_name = 'Leg_Grp'
        self.helper_class.parent_child_grp(parent=self.leg_grp_name,
                                           child=self.main_grp_name,
                                           trans_rot_scale=False)
        self.helper_class.transform_rotation_scale_visible(self.leg_grp_name,
                                                           v=False)

    def mirror_value(self):
        for each in self.ctrl_list:
            self.right_ctrl = each
            self.left_ctrl = each.replace('R', 'L')
            self.helper_class.mirror_grp(self.left_ctrl,
                                         self.right_ctrl)

    def mirror_status_def(self):
        # get the statu
        if self.mirror_check_box.isChecked():
            self.left_check_box.setChecked(True)
            self.right_check_box.setChecked(True)
        else:
            self.left_check_box.setChecked(False)
            self.right_check_box.setChecked(False)

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
                grid_value = 6 + a + 1

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
            self.leg_create_button.clicked.connect(self.leg_leg_def)
            self.leg_grid_layout.addWidget(self.leg_create_button, grid_value, 0, 1, 4)
            grid_value += 1
            self.leg_grid_layout.addItem(self.spacerItem, grid_value, 0, 1, 1)

        else:
            grid_value += 1
            self.leg_create_button = QtGui.QPushButton(self.widget)
            self.leg_create_button.setObjectName("leg_create_button")
            self.leg_create_button.setText('Create Arm')
            self.leg_create_button.clicked.connect(self.leg_leg_def)
            self.leg_grid_layout.addWidget(self.leg_create_button, grid_value, 0, 1, 4)
            grid_value += 1
            self.leg_grid_layout.addItem(self.spacerItem, grid_value, 0, 1, 1)

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

        # lock the Attr
        self.lock_attr()

    def get_update_radio_button(self):
        self.leg_name_scroll_area = QtGui.QScrollArea(self.head_splitter)
        self.leg_name_scroll_area.setWidgetResizable(True)
        self.leg_name_scroll_area.setObjectName("leg_name_scroll_area")
        self.leg_name_scrollArea_widget_contents = QtGui.QWidget()
        self.leg_name_scrollArea_widget_contents.setGeometry(QtCore.QRect(0, 0, 642, 64))
        self.leg_name_scrollArea_widget_contents.setObjectName("leg_name_scrollArea_widget_contents")
        self.gridLayout_15 = QtGui.QGridLayout(self.leg_name_scrollArea_widget_contents)
        self.gridLayout_15.setObjectName("gridLayout_15")

        self.no_leg = self.helper_class.get_leg()
        a = 0
        value = 0
        grid_value = 0
        while a < len(self.no_leg):
            self.radio_button = QtGui.QRadioButton(self.leg_name_scrollArea_widget_contents)
            self.radio_button.setObjectName(self.no_leg[a])
            self.radio_button.setText(self.no_leg[a])
            self.gridLayout_15.addWidget(self.radio_button, grid_value, value, 1, 1)
            self.radio_button.toggled.connect(partial(self.radio_button_change, a))
            value += 1
            if value == 3:
                value = 0
                grid_value += 1

            a += 1

        self.leg_name_scroll_area.setWidget(self.leg_name_scrollArea_widget_contents)

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
        self.mirror_check_box.stateChanged.connect(self.mirror_status_def)
        self.leg_mirror_grid_layout.addWidget(self.mirror_check_box, 0, 0, 1, 1)

        # LEFT
        self.left_check_box = QtGui.QCheckBox(self.leg_mirror_group_box)
        self.left_check_box.setObjectName("leg_left_check_box")
        self.left_check_box.setText('Left')
        self.leg_mirror_grid_layout.addWidget(self.left_check_box, 1, 0, 1, 1)

        # RIGHT
        self.right_check_box = QtGui.QCheckBox(self.leg_mirror_group_box)
        self.right_check_box.setObjectName("leg_right_check_box")
        self.right_check_box.setText('Right')
        self.leg_mirror_grid_layout.addWidget(self.right_check_box, 1, 1, 1, 1)

        # CLAVICAL
        self.hip_check_box = QtGui.QCheckBox(self.leg_mirror_group_box)
        self.hip_check_box.setObjectName("leg_clavical_check_box")
        self.hip_check_box.setText('Hip')
        self.leg_mirror_grid_layout.addWidget(self.hip_check_box, 2, 0, 1, 1)

        # SCAPULA
        self.butt_check_box = QtGui.QCheckBox(self.leg_mirror_group_box)
        self.butt_check_box.setObjectName("leg_scapula_check_box")
        self.butt_check_box.setText('Butt')
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
        self.leg_bone_grid_layout.addWidget(self.thine_to_knee_jnt_label, 0, 0, 1, 1)
        # UPPER ARM BONE LINE EDIT
        self.thine_to_knee_jnt_line_edit = QtGui.QLineEdit(self.leg_bone_group_box)
        self.thine_to_knee_jnt_line_edit.setObjectName("leg_upper_leg_bone_line_edit")
        self.leg_bone_grid_layout.addWidget(self.thine_to_knee_jnt_line_edit, 0, 1, 1, 1)

        # LOWER ARM BONE
        # LOWER ARM BONE LABEL
        self.knee_to_ball_jnt_label = QtGui.QLabel(self.leg_bone_group_box)
        self.knee_to_ball_jnt_label.setObjectName("Knee_to_Ball_Jnt")
        self.knee_to_ball_jnt_label.setText('Knee to Ball Bone')
        self.leg_bone_grid_layout.addWidget(self.knee_to_ball_jnt_label, 1, 0, 1, 1)
        # LOWER ARM BONE LINE EDIT
        self.knee_to_ball_jnt_line_edit = QtGui.QLineEdit(self.leg_bone_group_box)
        self.knee_to_ball_jnt_line_edit.setObjectName("leg_lower_leg_bone_line_edit")
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
        self.foot_check_box.stateChanged.connect(self.update_foot_check_box_def)
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
        self.gridLayout_26.addWidget(self.leg_name_label, 0, 0, 1, 1)
        # ARM NAME BUTTON
        self.leg_name_button = QtGui.QPushButton(self.leg_name_parent_group_box)
        self.leg_name_button.setMinimumSize(QtCore.QSize(297, 0))
        self.leg_name_button.setObjectName("leg_name_button")
        self.leg_name_button.setText('None)')
        self.leg_name_button.clicked.connect(self.rename)
        self.gridLayout_26.addWidget(self.leg_name_button, 0, 1, 1, 1)

        # ARM PARENT
        # ARM PARENT LABEL
        self.leg_parent_label = QtGui.QLabel(self.leg_name_parent_group_box)
        self.leg_parent_label.setObjectName("leg_parent_label")
        self.leg_parent_label.setText('Parent')
        self.gridLayout_26.addWidget(self.leg_parent_label, 1, 0, 1, 1)
        # ARM PARENT BUTTON
        self.leg_parent_button = QtGui.QPushButton(self.leg_name_parent_group_box)
        self.leg_parent_button.setObjectName("leg_parent_button")
        self.leg_parent_button.setText('None)')
        self.leg_parent_button.clicked.connect(self.parent)
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
        self.leg_update_button.clicked.connect(self.leg_update_button_def)
        self.gridLayout_17.addWidget(self.leg_update_button, 1, 0, 1, 1)

        # DELETE BUTTON
        self.leg_delete_button = QtGui.QPushButton(self.head_update_scrollArea_widget_contents)
        self.leg_delete_button.setObjectName("leg_delete_button")
        self.leg_delete_button.setText('Delete(Leg Name)')
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

    def delete_all(self):
        print('now all Leg is going to delete')

    def radio_button_change(self, b, val):
        if val == True:
            # unlock the val
            self.unlock_attr()

            # get input data
            self.get_input_data(self.no_leg[b])

    def get_input_data(self, leg_name):
        # self.prefix_name + "_" + self.leg_side  + "_Leg_Thine_Tem_" + str(self.val)
        # L_Leg_1
        self.leg_name = leg_name
        self.leg_name_split = self.leg_name.split('_')
        # get the side
        self.leg_side = self.leg_name_split[0]

        # get the val
        self.val = self.leg_name_split[-1]

        # get the prefix
        # Template_L_Leg_Tem_1_Main_Grp
        main_grp_name = '*_' + self.leg_side + '_Leg_Tem_' + str(self.val) + '_Main_Grp'
        cmds.select(main_grp_name)
        sel_main_grp = cmds.ls(sl=True)[0]
        self.prefix_name = sel_main_grp.split('_' + self.leg_side)[0]

        # Template_L_Leg_Thine_Tem_1_Outer_Ctrl_right_to_left_Mirror_Grp
        if self.leg_side == 'L':
            mirror_name = 'right_to_left'
        else:
            mirror_name = 'left_to_right'
        mirror_grp_name = self.prefix_name + '_' + self.leg_side + '_Leg_Thine_Tem_' + str(self.val) + \
                          '_Outer_Ctrl_' + mirror_name + '_Mirror_Grp'
        if cmds.objExists(mirror_grp_name):
            self.mirror_check_box.setChecked(True)
        else:
            self.mirror_check_box.setChecked(False)

        if self.leg_side == 'L':
            if cmds.objExists(mirror_grp_name):
                self.mirror_check_box.setChecked(True)
                self.left_check_box.setChecked(True)
                self.right_check_box.setChecked(True)
            else:
                self.left_check_box.setChecked(True)

        if self.leg_side == 'R':
            if cmds.objExists(mirror_grp_name):
                self.mirror_check_box.setChecked(True)
                self.left_check_box.setChecked(True)
                self.right_check_box.setChecked(True)
            else:
                self.right_check_box.setChecked(True)

        # get the hip controller
        # Template_Leg_Hip_Tem_1_Outer_Ctrl
        hip_ctrl_name = self.prefix_name + '_Leg_Hip_Tem_' + str(self.val) + '_Outer_Ctrl'
        if cmds.objExists(hip_ctrl_name):
            self.hip_check_box.setChecked(True)
        else:
            self.hip_check_box.setChecked(False)

        # Template_L_Leg_Butt_Tem_1_Outer_Ctrl
        butt_ctrl_name = self.prefix_name + '_' + self.leg_side + '_Leg_Butt_Tem_' + str(self.val) + \
                         '_Outer_Ctrl'
        if cmds.objExists(butt_ctrl_name):
            self.butt_check_box.setChecked(True)
        else:
            self.butt_check_box.setChecked(False)

        # get thine to knee geo
        # Template_L_Leg_Upper_0_Tem_1_Geo
        upper_geo = self.prefix_name + '_' + self.leg_side + '_Leg_Upper_*_Tem_' + str(self.val) + \
                    '_Geo'
        cmds.select(upper_geo)
        sel_upper_geo = cmds.ls(sl=True)
        self.thine_to_knee_jnt_line_edit.setText(str(len(sel_upper_geo)))

        # get knee to ball geo
        lower_geo = self.prefix_name + '_' + self.leg_side + '_Leg_Lower_*_Tem_' + str(self.val) + \
                    '_Geo'
        cmds.select(lower_geo)
        sel_lower_geo = cmds.ls(sl=True)
        self.knee_to_ball_jnt_line_edit.setText(str(len(sel_lower_geo)))

        # finger_ctrl
        # Template_L_Leg_Finger_1_1_Tem_1_Outer_Ctrl
        finger_outer = self.prefix_name + '_' + self.leg_side + '_Leg_Finger_1_1_Tem_' + str(self.val) + \
                       '_Outer_Ctrl'
        if cmds.objExists(finger_outer):
            self.foot_check_box.setChecked(True)
        else:
            self.foot_check_box.setChecked(False)

        # set the finger
        # Template_L_Leg_Finger_1_1_Tem_1_Outer_Ctrl
        #
        finger_name = self.prefix_name + '_' + self.leg_side + '_Leg_Finger_*_1_Tem_' + str(self.val) + \
                      '_Outer_Ctrl'

        if cmds.objExists(finger_name):

            cmds.select(finger_name)
            sel_finger = cmds.ls(sl=True)
            self.len_finger = len(sel_finger)

            a = 0

            while a < self.len_finger:
                self.finger_label_list[a] = QtGui.QLabel(self.leg_finger_group_box)
                self.finger_label_list[a].setObjectName(sel_finger[a])
                self.finger_label_list[a].setText('Finger : ' + str(a + 1))
                self.leg_finger_grid_layout.addWidget(self.finger_label_list[a], a, 0, 1, 1)

                self.leg_finger_line_edit[a] = QtGui.QLineEdit(self.leg_finger_group_box)
                self.leg_finger_line_edit[a].setObjectName(sel_finger[a])
                # Template_L_Leg_Finger_1_1_Tem_1_Outer_Ctrl
                outer_ctrl = self.prefix_name + '_' + self.leg_side + '_Leg_Finger_' + str(a + 1) + '_*_Tem_' + str(
                    self.val) + \
                             '_Outer_Ctrl'
                cmds.select(outer_ctrl)
                sel_outer = cmds.ls(sl=True)
                self.leg_finger_line_edit[a].setText(str(len(sel_outer)))
                self.leg_finger_grid_layout.addWidget(self.leg_finger_line_edit[a], a, 1, 1, 1)
                a += 1

        # set the name
        self.leg_name_button.setText(self.prefix_name)

        # get the parent const
        self.leg_parent_button.setText(self.parent_query())

        # delete and update
        name = 'Update (%s)' % self.leg_name
        self.leg_update_button.setText(name)
        name = 'Delete (%s)' % self.leg_name
        self.leg_delete_button.setText(name)

    def parent_query(self):
        # Template_Human_Head_Base_Tem_1_Ctrl
        thine_ctrl_name = self.prefix_name + '_' + self.leg_side + '_Leg_Thine_Tem_' + str(self.val) + \
                          '_Outer_Ctrl'
        hip_ctrl_name = self.prefix_name + '_Leg_Hip_Tem_' + str(self.val) + '_Outer_Ctrl'
        if cmds.objExists(hip_ctrl_name):
            value = cmds.listRelatives(hip_ctrl_name, type='parentConstraint')
        else:
            value = cmds.listRelatives(thine_ctrl_name, type='parentConstraint')
        if value == None:
            parent = 'None'
        else:
            parent = cmds.listConnections((value[0] + '.target[0].targetTranslate'), type='transform')[0]
        return parent

    def lock_attr(self):
        self.mirror_check_box.setDisabled(True)
        self.left_check_box.setDisabled(True)
        self.right_check_box.setDisabled(True)
        self.hip_check_box.setDisabled(True)
        self.butt_check_box.setDisabled(True)
        self.thine_to_knee_jnt_label.setDisabled(True)
        self.thine_to_knee_jnt_line_edit.setDisabled(True)
        self.knee_to_ball_jnt_label.setDisabled(True)
        self.knee_to_ball_jnt_line_edit.setDisabled(True)
        self.foot_check_box.setDisabled(True)
        self.leg_name_label.setDisabled(True)
        self.leg_name_button.setDisabled(True)
        self.leg_parent_label.setDisabled(True)
        self.leg_parent_button.setDisabled(True)
        self.leg_update_button.setDisabled(True)
        self.leg_delete_button.setDisabled(True)

    def unlock_attr(self):
        self.mirror_check_box.setDisabled(False)
        self.left_check_box.setDisabled(False)
        self.right_check_box.setDisabled(False)
        self.hip_check_box.setDisabled(False)
        self.butt_check_box.setDisabled(False)
        self.thine_to_knee_jnt_label.setDisabled(False)
        self.thine_to_knee_jnt_line_edit.setDisabled(False)
        self.knee_to_ball_jnt_label.setDisabled(False)
        self.knee_to_ball_jnt_line_edit.setDisabled(False)
        self.foot_check_box.setDisabled(False)
        self.leg_name_label.setDisabled(False)
        self.leg_name_button.setDisabled(False)
        self.leg_parent_label.setDisabled(False)
        self.leg_parent_button.setDisabled(False)
        self.leg_update_button.setDisabled(False)
        self.leg_delete_button.setDisabled(False)

    def rename(self):
        rename.main('Leg', self.leg_name, self.leg_name_button)

    def parent(self):
        parent.main('Leg', self.leg_name, self.leg_parent_button)

    def get_update_ui(self):
        # MIRROR
        self.mirror_check_box_query = self.mirror_check_box.isChecked()

        # LEFT LEG
        self.left_check_box_query = self.left_check_box.isChecked()

        # RIGHT LEG
        self.right_check_box_query = self.right_check_box.isChecked()

        # HIP
        self.hip_check_box_query = self.hip_check_box.isChecked()

        # BUTT
        self.butt_check_box_query = self.butt_check_box.isChecked()

        # THING TO KNEE JNT
        self.thine_to_knee_jnt_line_edit_line_edit_query = int(self.thine_to_knee_jnt_line_edit.text())

        # KNEE TO FOOT JNT
        self.knee_to_ball_jnt_line_edit_query = int(self.knee_to_ball_jnt_line_edit.text())

        # FOOT
        self.foot_check_box_query = self.foot_check_box.isChecked()

        # NAME BUTTON
        self.leg_name_button_query = self.leg_name_button.text()

        # PARENT PARENT
        self.leg_parent_button_query = self.leg_parent_button.text()

    def leg_update_button_def(self):
        # GET UPDATE UI
        self.get_update_ui()
        # GET GROUP NAME
        self.get_grp_name()

        # HIP
        if self.hip_check_box_query == False:
            # check the hip out controller
            # Template_Leg_Hip_Tem_1_Outer_Ctrl
            # Template_Leg_Hip_Tem_1_Geo
            hip_common = self.prefix_name + '_Leg_Hip_Tem_' + str(self.val)
            hip_ctrl = hip_common + '_Outer_Ctrl'
            clu_handle_name = hip_common + '_CluHandle'
            geo_name = hip_common + '_Geo'
            if cmds.objExists(hip_ctrl):
                # Template_L_Leg_Thine_to_Hip_Tem_1_Geo
                cylinder_name = self.prefix_name + '_' + self.leg_side + '_Leg_Thine_to_Hip_Tem_' + str(
                    self.val) + '_Geo'
                cmds.select(hip_ctrl, clu_handle_name,
                            geo_name, cylinder_name)
                if self.mirror_check_box_query == True:
                    if self.leg_side == 'L':
                        value = 'R'
                    else:
                        value = 'L'
                    new_cylinder_name = self.prefix_name + '_' + value + '_Leg_Thine_to_Hip_Tem_' + str(
                        self.val) + '_Geo'
                    cmds.select(new_cylinder_name, add=True)
                cmds.delete()

        # BUTT
        butt_common = self.prefix_name + '_' + self.leg_side + '_Leg_Butt_Tem_' + str(self.val)
        butt_ctrl = butt_common + '_Outer_Ctrl'
        if self.butt_check_box_query == True:
            # Template_L_Leg_Butt_Tem_1_Outer_Ctrl
            if cmds.objExists(butt_ctrl):
                pass
            else:
                # self.butt_pos = [-8.177, 83.76, -2.319]
                # get the thine pos
                thine_pos = cmds.xform(self.thine_outer_ctrl, q=1, ws=1, rp=1)
                x_minus = thine_pos[2] - 4
                self.butt_pos = [thine_pos[0], thine_pos[1], x_minus]
                if self.leg_side == 'L':
                    self.base_ctrl_color = 'Blue'
                else:
                    self.base_ctrl_color = 'Red'
                self.butt_def()
                self.final_group(hip=False)
                if self.mirror_check_box_query == True:
                    if self.leg_side == 'L':
                        value = 'R'
                    else:
                        value = 'L'

                    self.leg_side = value
                    self.get_grp_name()
                    thine_pos = cmds.xform(self.thine_outer_ctrl, q=1, ws=1, rp=1)
                    value_z = thine_pos[2] - 4
                    self.butt_pos = [thine_pos[0], thine_pos[1], value_z]

                    if self.leg_side == 'L':
                        self.base_ctrl_color = 'Blue'
                    else:
                        self.base_ctrl_color = 'Red'
                    self.butt_def()
                    self.final_group(hip=False)

                    if self.leg_side == 'L':
                        value = 'R'
                    else:
                        value = 'L'
                    self.leg_side = value
                    self.get_grp_name()
        else:
            if cmds.objExists(butt_ctrl):
                # Template_L_Leg_Thine_to_Butt_Tem_1_Geo
                geo_name = butt_common + '_Geo'
                clu_handle_name = butt_common + '_CluHandle'
                cylinder_name = self.prefix_name + '_' + self.leg_side + '_Leg_Thine_to_Butt_Tem_' + str(
                    self.val) + '_Geo'
                # Template_L_Leg_Thine_to_Butt_Lower_Tem_1_CluHandle
                # Template_L_Leg_Thine_to_Butt_Upper_Tem_1_CluHandle
                clu_upper_name = self.prefix_name + '_' + self.leg_side + '_Leg_Thine_to_Butt_Upper_Tem_' + str(
                    self.val) + '_CluHandle'
                clu_lower_name = self.prefix_name + '_' + self.leg_side + '_Leg_Thine_to_Butt_Lower_Tem_' + str(
                    self.val) + '_CluHandle'

                cmds.select(butt_ctrl,
                            geo_name,
                            clu_handle_name,
                            cylinder_name,
                            clu_upper_name,
                            clu_lower_name)
                cmds.delete()
                if self.mirror_check_box_query == True:
                    if self.leg_side == 'L':
                        value = 'R'
                    else:
                        value = 'L'

                    butt_common = self.prefix_name + '_' + value + '_Leg_Butt_Tem_' + str(self.val)
                    butt_ctrl = butt_common + '_Outer_Ctrl'
                    geo_name = butt_common + '_Geo'
                    clu_handle_name = butt_common + '_CluHandle'
                    cylinder_name = self.prefix_name + '_' + value + '_Leg_Thine_to_Butt_Tem_' + str(self.val) + '_Geo'
                    # Template_L_Leg_Thine_to_Butt_Lower_Tem_1_CluHandle
                    # Template_L_Leg_Thine_to_Butt_Upper_Tem_1_CluHandle
                    clu_upper_name = self.prefix_name + '_' + value + '_Leg_Thine_to_Butt_Upper_Tem_' + str(
                        self.val) + '_CluHandle'
                    clu_lower_name = self.prefix_name + '_' + value + '_Leg_Thine_to_Butt_Lower_Tem_' + str(
                        self.val) + '_CluHandle'

                    cmds.select(butt_ctrl,
                                geo_name,
                                clu_handle_name,
                                cylinder_name,
                                clu_upper_name,
                                clu_lower_name)
                    cmds.delete()

        # THINE TO KNEE JNT
        # Template_L_Leg_Upper_0_Tem_1_Geo
        common_name = self.prefix_name + '_' + self.leg_side + '_Leg_Upper_*_Tem_' + str(self.val)
        geo_name = common_name + '_Geo'
        cmds.select(geo_name)
        sel_geo = cmds.ls(sl=True)
        if self.thine_to_knee_jnt_line_edit_line_edit_query != len(sel_geo):
            # delete curve,curve_0_clu_handle_name,curve_1_clu_handle_name,self.poc_name
            # Template_L_Leg_Upper_Tem_1_Crv
            crv_name = self.prefix_name + '_' + self.leg_side + '_Leg_Upper_Tem_' + str(self.val) + '_Crv'
            curve_0_clu_handle_name = self.prefix_name + "_" + self.leg_side + "_Leg_Upper_0_Tem_" + str(
                self.val) + '_CluHandle'
            curve_1_clu_handle_name = self.prefix_name + "_" + self.leg_side + "_Leg_Upper_1_Tem_" + str(
                self.val) + '_CluHandle'
            poc_name = common_name + '_POC'
            cmds.select(geo_name,
                        crv_name,
                        curve_1_clu_handle_name,
                        curve_0_clu_handle_name,
                        poc_name)
            cmds.delete()

            # create a new upper
            self.roll_bone('Upper',
                           self.thine_inner_ctrl,
                           self.shine_inner_ctrl,
                           self.thine_to_knee_jnt_line_edit_line_edit_query)
            self.final_group(hip=False)

            # do if mirror
            if self.mirror_check_box_query == True:
                if self.leg_side == 'L':
                    value = 'R'
                else:
                    value = 'L'

                self.leg_side = value
                self.get_grp_name()

                common_name = self.prefix_name + '_' + self.leg_side + '_Leg_Upper_*_Tem_' + str(self.val)
                geo_name = common_name + '_Geo'
                crv_name = self.prefix_name + '_' + self.leg_side + '_Leg_Upper_Tem_' + str(self.val) + '_Crv'
                curve_0_clu_handle_name = self.prefix_name + "_" + self.leg_side + "_Leg_Upper_0_Tem_" + str(
                    self.val) + '_CluHandle'
                curve_1_clu_handle_name = self.prefix_name + "_" + self.leg_side + "_Leg_Upper_1_Tem_" + str(
                    self.val) + '_CluHandle'
                poc_name = common_name + '_POC'
                cmds.select(geo_name,
                            crv_name,
                            curve_1_clu_handle_name,
                            curve_0_clu_handle_name,
                            poc_name)
                cmds.delete()

                # create a new upper
                self.roll_bone('Upper',
                               self.thine_inner_ctrl,
                               self.shine_inner_ctrl,
                               self.thine_to_knee_jnt_line_edit_line_edit_query)
                self.final_group(hip=False)

                if self.leg_side == 'L':
                    value = 'R'
                else:
                    value = 'L'

                self.leg_side = value
                self.get_grp_name()

        # THINE TO KNEE JNT
        # Template_L_Leg_Upper_0_Tem_1_Geo
        common_name = self.prefix_name + '_' + self.leg_side + '_Leg_Lower_*_Tem_' + str(self.val)
        geo_name = common_name + '_Geo'
        cmds.select(geo_name)
        sel_geo = cmds.ls(sl=True)
        if self.knee_to_ball_jnt_line_edit_query != len(sel_geo):
            # delete curve,curve_0_clu_handle_name,curve_1_clu_handle_name,self.poc_name
            # Template_L_Leg_Upper_Tem_1_Crv
            crv_name = self.prefix_name + '_' + self.leg_side + '_Leg_Lower_Tem_' + str(self.val) + '_Crv'
            curve_0_clu_handle_name = self.prefix_name + "_" + self.leg_side + "_Leg_Lower_0_Tem_" + str(
                self.val) + '_CluHandle'
            curve_1_clu_handle_name = self.prefix_name + "_" + self.leg_side + "_Leg_Lower_1_Tem_" + str(
                self.val) + '_CluHandle'
            poc_name = common_name + '_POC'
            cmds.select(geo_name,
                        crv_name,
                        curve_1_clu_handle_name,
                        curve_0_clu_handle_name,
                        poc_name)
            cmds.delete()

            # create a new upper
            self.roll_bone('Lower',
                           self.shine_inner_ctrl,
                           self.foot_inner_ctrl,
                           self.thine_to_knee_jnt_line_edit_line_edit_query)
            self.final_group(hip=False)

            # do if mirror
            if self.mirror_check_box_query == True:
                if self.leg_side == 'L':
                    value = 'R'
                else:
                    value = 'L'

                self.leg_side = value
                self.get_grp_name()

                common_name = self.prefix_name + '_' + self.leg_side + '_Leg_Lower_*_Tem_' + str(self.val)
                geo_name = common_name + '_Geo'
                crv_name = self.prefix_name + '_' + self.leg_side + '_Leg_Lower_Tem_' + str(self.val) + '_Crv'
                curve_0_clu_handle_name = self.prefix_name + "_" + self.leg_side + "_Leg_Lower_0_Tem_" + str(
                    self.val) + '_CluHandle'
                curve_1_clu_handle_name = self.prefix_name + "_" + self.leg_side + "_Leg_Lower_1_Tem_" + str(
                    self.val) + '_CluHandle'
                poc_name = common_name + '_POC'
                cmds.select(geo_name,
                            crv_name,
                            curve_1_clu_handle_name,
                            curve_0_clu_handle_name,
                            poc_name)
                cmds.delete()

                # create a new upper
                self.roll_bone('Lower',
                               self.shine_inner_ctrl,
                               self.foot_inner_ctrl,
                               self.thine_to_knee_jnt_line_edit_line_edit_query)
                self.final_group(hip=False)

                if self.leg_side == 'L':
                    value = 'R'
                else:
                    value = 'L'

                self.leg_side = value
                self.get_grp_name()

        # LEG
        if self.foot_check_box_query == False:
            # Template_L_Leg_Finger_1_1_Tem_1_Outer_Ctrl
            finger_outer = self.prefix_name + '_' + self.leg_side + '_Leg_Finger_1_1_Tem_' + str(
                self.val) + '_Outer_Ctrl'
            if cmds.objExists(finger_outer):
                # Delete the all the data
                self.delete_finger()
                if self.mirror_check_box_query == True:
                    if self.leg_side == 'L':
                        value = 'R'
                    else:
                        value = 'L'
                    self.leg_side = value
                    self.get_grp_name()

                    self.delete_finger()

                    if self.leg_side == 'L':
                        value = 'R'
                    else:
                        value = 'L'
                    self.leg_side = value
                    self.get_grp_name()

        else:
            a = 0
            while a < len(self.finger_label_list):
                # Template_L_Leg_Finger_1_1_Tem_1_Outer_Ctrl
                outer_ctrl = self.prefix_name + '_' + self.leg_side + '_Leg_Finger_1_*_Tem_' + str(
                    self.val) + '_Outer_Ctrl'
                cmds.select(outer_ctrl)
                sel_outer = cmds.ls(sl=True)
                # get the value
                line_edit_query = int(self.leg_finger_line_edit[a].text())
                if line_edit_query != len(sel_outer):
                    # delete all the controller
                    self.delete_finger()

                    # update the leg
                    self.no_finger_line_edit_query = len(self.finger_label_list)
                    # self.finger_default_pos
                    self.finger_default_pos = cmds.xform(self.ball_outer_ctrl, q=1, ws=1, rp=1)
                    # self.base_ctrl_color = 'Blue'
                    if self.leg_side == 'L':
                        self.base_ctrl_color = 'Blue'
                    else:
                        self.base_ctrl_color = 'Red'
                    self.ctrl_rotate = [90, 0, 0]
                    self.finger_def()
                    self.final_group(hip=False)
                    if self.mirror_check_box_query == True:
                        if self.leg_side == 'L':
                            value = 'R'
                        else:
                            value = 'L'
                        self.leg_side = value
                        self.get_grp_name()

                        self.delete_finger()
                        # update the leg
                        self.no_finger_line_edit_query = len(self.finger_label_list)
                        # self.finger_default_pos
                        self.finger_default_pos = cmds.xform(self.ball_outer_ctrl, q=1, ws=1, rp=1)
                        # self.base_ctrl_color = 'Blue'
                        if self.leg_side == 'L':
                            self.base_ctrl_color = 'Blue'
                        else:
                            self.base_ctrl_color = 'Red'
                        self.ctrl_rotate = [90, 0, 0]
                        self.finger_def()
                        self.final_group(hip=False)

                        if self.leg_side == 'L':
                            value = 'R'
                        else:
                            value = 'L'
                        self.leg_side = value
                        self.get_grp_name()
                    break
                a += 1

    def delete_finger(self):
        # Template_L_Leg_Finger_3_1_Tem_1_Outer_Ctrl_right_to_left_Mirror_Grp
        common_name = self.prefix_name + '_' + self.leg_side + '_Leg_Finger_*_1_Tem_' + str(self.val)
        outer_ctrl_name = common_name + '_Outer_Ctrl'
        if self.leg_side == 'L':
            rev_val = 'right_to_left'
        else:
            rev_val = 'left_to_right'
        mirror_ctrl_grp_name = outer_ctrl_name + '_' + rev_val + '_Mirror_Grp'
        clu_handle_name = common_name + '_CluHandle'
        geo_name = self.prefix_name + '_' + self.leg_side + '_Leg_Finger_*_*_Tem_' + str(self.val) + '_Geo'
        cmds.select(mirror_ctrl_grp_name, clu_handle_name, geo_name)

        a = 0
        while a < len(self.finger_label_list):
            # Template_R_Leg_Finger_1_2_Tem_1_Cylinder_Geo
            cylinder_name = self.prefix_name + "_" + self.leg_side + '_Leg_Finger_' + str(a + 1) + '_*_Tem_' + str(
                self.val) + '_Cylinder_Geo'
            lower_cluster_name = self.prefix_name + '_' + self.leg_side + '_Leg_Finger_Lower_' + str(
                a + 1) + '_*_Tem_' + str(self.val) + '_CluHandle'
            upper_cluster_name = self.prefix_name + '_' + self.leg_side + '_Leg_Finger_Upper_' + str(
                a + 1) + '_*_Tem_' + str(self.val) + '_CluHandle'
            cmds.select(cylinder_name, lower_cluster_name, upper_cluster_name, add=True)
            a += 1
        # Template_R_Leg_Finger_Leg_to_3_1_Tem_1_Cylinder_Geo
        cylinder_base = self.prefix_name + "_" + self.leg_side + "_Leg_Finger_Leg_to_*_1_Tem_" + str(
            self.val) + '_Cylinder_Geo'
        cmds.select(cylinder_base, add=True)
        cmds.delete()

    def get_grp_name(self):
        # THINE
        self.thine_common = self.prefix_name + "_" + self.leg_side + "_Leg_Thine_Tem_" + str(self.val)
        self.thine_sphere_name = self.thine_common + "_Geo"
        self.thine_sphere_clu_name = self.thine_common + '_Clu'
        self.thine_sphere_clu_handle_name = self.thine_sphere_clu_name + 'Handle'
        self.thine_inner_ctrl = self.thine_common + '_Inner_Ctrl'
        self.thine_outer_ctrl = self.thine_common + '_Outer_Ctrl'

        # SHINE
        self.shine_common = self.prefix_name + "_" + self.leg_side + "_Leg_Shine_Tem_" + str(self.val)
        self.shine_sphere_name = self.shine_common + "_Geo"
        self.shine_sphere_clu_name = self.shine_common + '_Clu'
        self.shine_sphere_clu_handle_name = self.shine_sphere_clu_name + 'Handle'
        self.shine_inner_ctrl = self.shine_common + '_Inner_Ctrl'
        self.shine_outer_ctrl = self.shine_common + '_Outer_Ctrl'

        # FOOT
        self.foot_common = self.prefix_name + "_" + self.leg_side + "_Leg_Foot_Tem_" + str(self.val)
        self.foot_sphere_name = self.foot_common + "_Geo"
        self.foot_sphere_clu_name = self.foot_common + '_Clu'
        self.foot_sphere_clu_handle_name = self.foot_sphere_clu_name + 'Handle'
        self.foot_inner_ctrl = self.foot_common + '_Inner_Ctrl'
        self.foot_outer_ctrl = self.foot_common + '_Outer_Ctrl'

        # BALL
        self.ball_common = self.prefix_name + "_" + self.leg_side + "_Leg_Ball_Tem_" + str(self.val)
        self.ball_sphere_name = self.ball_common + "_Geo"
        self.ball_sphere_clu_name = self.ball_common + '_Clu'
        self.ball_sphere_clu_handle_name = self.ball_sphere_clu_name + 'Handle'
        self.ball_inner_ctrl = self.ball_common + '_Inner_Ctrl'
        self.ball_outer_ctrl = self.ball_common + '_Outer_Ctrl'

        # END
        self.end_common = self.prefix_name + "_" + self.leg_side + "_Leg_End_Tem_" + str(self.val)
        self.end_sphere_name = self.end_common + "_Geo"
        self.end_sphere_clu_name = self.end_common + '_Clu'
        self.end_sphere_clu_handle_name = self.end_sphere_clu_name + 'Handle'
        self.end_inner_ctrl = self.end_common + '_Inner_Ctrl'
        self.end_outer_ctrl = self.end_common + '_Outer_Ctrl'

        self.sphere_group_name = self.prefix_name + '_' + self.leg_side + "_Leg_Tem_" + str(self.val) + "_Sphere_Grp"
        self.cluster_group_name = self.prefix_name + '_' + self.leg_side + "_Leg_Tem_" + str(self.val) + "_Cluster_Grp"
        self.cylinder_group_name = self.prefix_name + '_' + self.leg_side + "_Leg_Tem_" + str(
            self.val) + "_Cylinder_Grp"
        self.curve_group_name = self.prefix_name + '_' + self.leg_side + "_Leg_Tem_" + str(self.val) + "_Crv_Grp"

    def update_foot_check_box_def(self):
        self.foot_check_box_query = self.foot_check_box.isChecked()
        # Template_L_Leg_Finger_1_1_Tem_1_Outer_Ctrl
        outer_ctrl = self.prefix_name + '_' + self.leg_side + '_Leg_Finger_*_1_Tem_' + str(self.val) + \
                     '_Outer_Ctrl'
        if cmds.objExists(outer_ctrl):
            cmds.select(outer_ctrl)
            sel_outer = cmds.ls(sl=True)
            if self.foot_check_box_query == True:
                a = 0
                while a < len(sel_outer):
                    self.finger_label_list[a].setDisabled(False)
                    self.leg_finger_line_edit[a].setDisabled(False)
                    a += 1
            else:
                a = 0
                while a < len(sel_outer):
                    self.finger_label_list[a].setDisabled(True)
                    self.leg_finger_line_edit[a].setDisabled(True)
                    a += 1

    def get_data_variable(self, common_name):
        inner_ctrl = common_name + '_Inner_Ctrl'
        tem_remove_name = self.helper_class.remove_tem(common_name)
        if cmds.objExists(inner_ctrl):
            #
            jnt_name = common_name + '_Jnt'
            ik_name = tem_remove_name + '_Ik_Jnt'
            fk_name = tem_remove_name + '_Fk_Jnt'
            result_name = tem_remove_name + '_Result_Jnt'
            ik_pv_name = tem_remove_name + '_Ik_pv_Jnt'
            ik_no_flip_name = tem_remove_name + '_Ik_no_flip_Jnt'

            # GET VAL
            get_trans = cmds.xform(inner_ctrl, q=1, ws=1, rp=1)
            get_rot = cmds.getAttr(inner_ctrl + '.r')

            # APPEND THE VALUE
            self.ctrl_list[inner_ctrl] = {}
            self.ctrl_list[inner_ctrl]['Trans'] = get_trans
            self.ctrl_list[inner_ctrl]['Rot'] = get_rot
            self.common_list.append(common_name)
            return inner_ctrl, jnt_name, fk_name, ik_name, result_name, ik_pv_name, ik_no_flip_name

    def controller_get_data(self, main_grp_name):
        main_grp_split = main_grp_name.split('_')
        self.prefix_name = main_grp_split[0]
        self.leg_side = main_grp_split[1]
        self.val = main_grp_split[4]

        self.ctrl_list = {}
        self.common_list = []

        # THINE
        self.thine_common = self.prefix_name + "_" + self.leg_side + "_Leg_Thine_Tem_" + str(self.val)
        self.thine_inner_ctrl, self.thine_jnt_name, self.thine_fk_jnt, self.thine_ik_jnt, \
        self.thine_result_jnt, self.thine_ik_pv_jnt, self.thine_ik_no_flip_jnt = self.get_data_variable(
            self.thine_common)

        # SHINE
        self.shine_common = self.prefix_name + "_" + self.leg_side + "_Leg_Shine_Tem_" + str(self.val)
        self.shine_inner_ctrl, self.shine_jnt_name, self.shine_fk_jnt, self.shine_ik_jnt, \
        self.shine_result_jnt, self.shine_ik_pv_jnt, self.shine_ik_no_flip_jnt = self.get_data_variable(
            self.shine_common)

        # FOOT
        self.foot_common = self.prefix_name + "_" + self.leg_side + "_Leg_Foot_Tem_" + str(self.val)
        self.foot_inner_ctrl, self.foot_jnt_name, self.foot_fk_jnt, self.foot_ik_jnt, \
        self.foot_result_jnt, self.foot_ik_pv_jnt, self.foot_ik_no_flip_jnt = self.get_data_variable(self.foot_common)

        # BALL
        self.ball_common = self.prefix_name + "_" + self.leg_side + "_Leg_Ball_Tem_" + str(self.val)
        self.ball_inner_ctrl, self.ball_jnt_name, self.ball_fk_jnt, self.ball_ik_jnt, \
        self.ball_result_jnt, self.ball_ik_pv_jnt, self.ball_ik_no_flip_jnt = self.get_data_variable(self.ball_common)

        # END
        self.end_common = self.prefix_name + "_" + self.leg_side + "_Leg_End_Tem_" + str(self.val)
        self.end_inner_ctrl, self.end_jnt_name, self.end_fk_jnt, self.end_ik_jnt, \
        self.end_result_jnt, self.end_ik_pv_jnt, self.end_ik_no_flip_jnt = self.get_data_variable(self.end_common)

        self.butt_common = self.prefix_name + "_" + self.leg_side + "_Leg_Butt_Tem_" + str(self.val)

        '''
        self.butt_common = self.prefix_name + "_" + self.leg_side  + "_Leg_Butt_Tem_" + str(self.val)
        self.inner_butt_ctrl = self.butt_common + '_Inner_Ctrl'
        if cmds.objExists(self.inner_butt_ctrl):
            self.butt_inner_ctrl,self.butt_jnt_name,self.butt_fk_jnt,self.butt_ik_jnt,\
                self.butt_result_jnt,self.butt_ik_pv_jnt,self.butt_ik_no_flip_jnt = self.get_data_variable(self.butt_common)
        '''

        # UPPER ARM GEO
        # Template_L_Leg_Upper_0_Tem_1_Geo
        self.upper_jnt_list = {}
        geo_name = self.prefix_name + "_" + self.leg_side + "_Leg_Upper_*_Tem_" + str(self.val) + '_Geo'
        if cmds.objExists(geo_name):
            cmds.select(geo_name)
            sel_geo = cmds.ls(sl=True)
            a = 0
            while a < len(sel_geo):
                # get the position
                sel_geo_get_trans = cmds.xform(sel_geo[a], q=1, ws=1, rp=1)
                sel_geo_get_rot = cmds.getAttr(sel_geo[a] + '.r')
                split_geo = sel_geo[a].split('_Geo')[0]

                self.upper_jnt_list[sel_geo[a]] = {}
                self.upper_jnt_list[sel_geo[a]]['Trans'] = sel_geo_get_trans
                self.upper_jnt_list[sel_geo[a]]['Rot'] = sel_geo_get_rot
                a += 1

        # LOWER ARM GEO
        self.lower_jnt_list = {}
        geo_name = self.prefix_name + "_" + self.leg_side + "_Leg_Lower_*_Tem_" + str(self.val) + '_Geo'
        if cmds.objExists(geo_name):
            cmds.select(geo_name)
            sel_geo = cmds.ls(sl=True)
            a = 0
            while a < len(sel_geo):
                # get the position
                sel_geo_get_trans = cmds.xform(sel_geo[a], q=1, ws=1, rp=1)
                sel_geo_get_rot = cmds.getAttr(sel_geo[a] + '.r')
                split_geo = sel_geo[a].split('_Geo')[0]

                self.lower_jnt_list[sel_geo[a]] = {}
                self.lower_jnt_list[sel_geo[a]]['Trans'] = sel_geo_get_trans
                self.lower_jnt_list[sel_geo[a]]['Rot'] = sel_geo_get_rot
                a += 1

        # GET THE FINGER
        # Template_L_Leg_Finger_1_1_Tem_1_Inner_Ctrl
        self.finger_list = []
        outer_finger_ctrl = self.prefix_name + "_" + self.leg_side + "_Leg_Finger_*_1_Tem_" + str(
            self.val) + '_Inner_Ctrl'
        if cmds.objExists(outer_finger_ctrl):
            cmds.select(outer_finger_ctrl)
            sel_finger = cmds.ls(sl=True)
            for each_finger in sel_finger:
                self.finger_list.append(each_finger)

    def leg_create(self):
        # get the no of the human main grp
        self.grp_list = ['Leg_Grp']
        for each_grp in self.grp_list:
            # list of the all children
            if cmds.objExists(each_grp):
                children_list = cmds.listRelatives(each_grp, children=True)
                for each_child in children_list:
                    # get all the controller data
                    self.controller_get_data(each_child)

                    # final the head
                    self.final_leg()

    def final_leg(self):
        # create a joint on each position
        ik_jnt_list = []
        fk_jnt_list = []
        result_jnt_list = []
        ik_pv_jnt_list = []
        ik_no_flip_jnt_list = []
        a = 0
        while a < len(self.common_list):
            common_name = self.helper_class.remove_tem(self.common_list[a])
            ik_jnt_name = common_name + '_Ik_Jnt'
            fk_jnt_name = common_name + '_Fk_Jnt'
            result_jnt_name = common_name + '_Result_Jnt'
            ik_pv_jnt_name = common_name + '_Ik_pv_Jnt'
            ik_no_flip_jnt_name = common_name + '_Ik_no_flip_Jnt'
            list = [ik_jnt_name, fk_jnt_name, result_jnt_name, ik_pv_jnt_name, ik_no_flip_jnt_name]
            for each_jnt in list:
                cmds.select(cl=True)
                controller_name = self.common_list[a] + '_Inner_Ctrl'
                cmds.joint(n=each_jnt, p=(self.ctrl_list[controller_name]['Trans'][0],
                                          self.ctrl_list[controller_name]['Trans'][1],
                                          self.ctrl_list[controller_name]['Trans'][2]))
            ik_jnt_list.append(ik_jnt_name)
            fk_jnt_list.append(fk_jnt_name)
            result_jnt_list.append(result_jnt_name)
            ik_pv_jnt_list.append(ik_pv_jnt_name)
            ik_no_flip_jnt_list.append(ik_no_flip_jnt_name)

            a += 1

        # parent the joint
        self.helper_class.maya_parent(self.shine_fk_jnt, self.thine_fk_jnt)
        self.helper_class.maya_parent(self.foot_fk_jnt, self.shine_fk_jnt)
        self.helper_class.maya_parent(self.ball_fk_jnt, self.foot_fk_jnt)
        self.helper_class.maya_parent(self.end_fk_jnt, self.ball_fk_jnt)

        self.helper_class.maya_parent(self.shine_ik_jnt, self.thine_ik_jnt)
        self.helper_class.maya_parent(self.foot_ik_jnt, self.shine_ik_jnt)
        self.helper_class.maya_parent(self.ball_ik_jnt, self.foot_ik_jnt)
        self.helper_class.maya_parent(self.end_ik_jnt, self.ball_ik_jnt)

        self.helper_class.maya_parent(self.shine_result_jnt, self.thine_result_jnt)
        self.helper_class.maya_parent(self.foot_result_jnt, self.shine_result_jnt)
        self.helper_class.maya_parent(self.ball_result_jnt, self.foot_result_jnt)
        self.helper_class.maya_parent(self.end_result_jnt, self.ball_result_jnt)

        self.helper_class.maya_parent(self.shine_ik_pv_jnt, self.thine_ik_pv_jnt)
        self.helper_class.maya_parent(self.foot_ik_pv_jnt, self.shine_ik_pv_jnt)
        self.helper_class.maya_parent(self.ball_ik_pv_jnt, self.foot_ik_pv_jnt)
        self.helper_class.maya_parent(self.end_ik_pv_jnt, self.ball_ik_pv_jnt)

        self.helper_class.maya_parent(self.shine_ik_no_flip_jnt, self.thine_ik_no_flip_jnt)
        self.helper_class.maya_parent(self.foot_ik_no_flip_jnt, self.shine_ik_no_flip_jnt)
        self.helper_class.maya_parent(self.ball_ik_no_flip_jnt, self.foot_ik_no_flip_jnt)
        self.helper_class.maya_parent(self.end_ik_no_flip_jnt, self.ball_ik_no_flip_jnt)

        # create a ik pv and no flip grp
        thine_ik_pv_grp_name = self.thine_ik_pv_jnt + '_Grp'
        cmds.select(self.thine_ik_pv_jnt)
        cmds.group(n=thine_ik_pv_grp_name)

        thine_ik_no_flip_grp_name = self.thine_ik_no_flip_jnt + '_Grp'
        cmds.select(self.thine_ik_no_flip_jnt)
        cmds.group(n=thine_ik_no_flip_grp_name)

        cmds.select(self.thine_ik_jnt, self.thine_fk_jnt, self.thine_result_jnt, self.thine_ik_pv_jnt,
                    self.thine_ik_no_flip_jnt)
        cmds.joint(e=True, oj='xyz', secondaryAxisOrient='xup', ch=True, zso=True)

        # create a ik and fk switch
        self.controller_class.cube_ctrl()
        sel_obj = cmds.ls(sl=True)
        ik_fk_switch_name = self.prefix_name + "_" + self.leg_side + "_Ik_Fk_Switch_" + str(self.val) + '_Ctrl'
        ik_fk_switch_grp_name = ik_fk_switch_name + '_Grp'
        cmds.rename(sel_obj[0], ik_fk_switch_name)
        cmds.move(self.ctrl_list[self.foot_inner_ctrl]['Trans'][0],
                  self.ctrl_list[self.foot_inner_ctrl]['Trans'][1],
                  self.ctrl_list[self.foot_inner_ctrl]['Trans'][2])
        # move -r -os -wd 0 0 -6.664142 ;
        cmds.move(0, 0, -6, r=True)
        cmds.group(n=ik_fk_switch_grp_name)
        self.helper_class.transform_rotation_scale_visible(ik_fk_switch_grp_name)
        cmds.select(ik_fk_switch_name)

        cmds.DeleteHistory()
        cmds.FreezeTransformations()
        cmds.parentConstraint(self.foot_result_jnt, ik_fk_switch_name, mo=True)
        cmds.addAttr(ik_fk_switch_name, ln="IK_FK_Switch", at='double', min=0, max=1)
        cmds.setAttr((ik_fk_switch_name + ".IK_FK_Switch"), e=True, keyable=True)
        # joint -e  -oj xyz -secondaryAxisOrient xup -ch -zso;
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
            a += 1

        cmds.connectAttr((ik_fk_switch_name + '.IK_FK_Switch'), (thine_ik_no_flip_grp_name + '.v'), f=True)
        cmds.connectAttr((ik_fk_switch_name + '.IK_FK_Switch'), (thine_ik_pv_grp_name + '.v'), f=True)

        # CREATE A FK JOINT
        a = 0
        if self.leg_side == 'L':
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

        # STRETCH THE IK THINE AND SHINE
        cmds.addAttr(self.thine_fk_jnt, ln="Stretch", at='double', min=-1, dv=0)
        cmds.setAttr((self.thine_fk_jnt + ".Stretch"), e=True, keyable=True)
        cmds.setDrivenKeyframe((self.shine_fk_jnt + ".tx"), currentDriver=(self.thine_fk_jnt + ".Stretch"))

        cmds.setAttr((self.thine_fk_jnt + ".Stretch"), -1)
        cmds.setAttr((self.shine_fk_jnt + ".tx"), 0)
        cmds.setDrivenKeyframe((self.shine_fk_jnt + ".tx"), currentDriver=(self.thine_fk_jnt + ".Stretch"))
        mel.eval("selectKey -add -k -f -1 -f 0 %s;" % (self.shine_fk_jnt + "_translateX"))
        mel.eval('setInfinity -poi cycleRelative;')
        cmds.setAttr((self.thine_fk_jnt + ".Stretch"), 0)

        cmds.addAttr(self.shine_fk_jnt, ln="Stretch", at='double', min=-1, dv=0)
        cmds.setAttr((self.shine_fk_jnt + ".Stretch"), e=True, keyable=True)
        cmds.setDrivenKeyframe((self.foot_fk_jnt + ".tx"), currentDriver=(self.shine_fk_jnt + ".Stretch"))

        cmds.setAttr((self.shine_fk_jnt + ".Stretch"), -1)
        cmds.setAttr((self.foot_fk_jnt + ".tx"), 0)
        cmds.setDrivenKeyframe((self.foot_fk_jnt + ".tx"), currentDriver=(self.shine_fk_jnt + ".Stretch"))
        mel.eval("selectKey -add -k -f -1 -f 0 %s;" % (self.foot_fk_jnt + "_translateX"))
        mel.eval('setInfinity -poi cycleRelative;')
        cmds.setAttr((self.shine_fk_jnt + ".Stretch"), 0)

        # CREATE A IK
        cmds.setAttr(((ik_fk_switch_name + '.IK_FK_Switch')), 1)
        cmds.select(self.ball_ik_no_flip_jnt, self.ball_ik_pv_jnt)
        cmds.delete()

        # create a the controller ik position
        foot_ctrl_name = self.prefix_name + "_" + self.leg_side + "_Foot_" + str(self.val) + '_Ctrl'
        foot_ctrl_grp_name = foot_ctrl_name + '_Grp'
        self.controller_class.footprint_ctrl()
        sel_obj = cmds.ls(sl=True)
        cmds.rename(sel_obj[0], foot_ctrl_name)
        cmds.select(foot_ctrl_name)
        cmds.move(self.ctrl_list[self.foot_inner_ctrl]['Trans'][0],
                  self.ctrl_list[self.foot_inner_ctrl]['Trans'][1],
                  self.ctrl_list[self.foot_inner_ctrl]['Trans'][2])
        # move -r -os -wd 0 0 -6.664142 ;
        cmds.move(0, -8, 0, r=True)
        cmds.setAttr((foot_ctrl_name + '.sx'), 5)
        cmds.setAttr((foot_ctrl_name + '.sy'), 5)
        cmds.setAttr((foot_ctrl_name + '.sz'), 5)
        if self.leg_side != 'L':
            cmds.setAttr((foot_ctrl_name + '.sx'), -5)
        cmds.DeleteHistory()
        cmds.FreezeTransformations()
        cmds.addAttr(foot_ctrl_name, ln="IK_pv_no_Flip_Switch", at='double', min=0, max=1)
        cmds.setAttr((foot_ctrl_name + ".IK_pv_no_Flip_Switch"), e=True, keyable=True)
        cmds.select(foot_ctrl_name)
        cmds.group(n=foot_ctrl_grp_name)
        cmds.connectAttr((ik_fk_switch_name + '.IK_FK_Switch'), (foot_ctrl_grp_name + '.v'), f=True)
        self.helper_class.color_val(color_name, foot_ctrl_name)

        ik_pv_jnt_list = [self.thine_ik_pv_jnt, self.shine_ik_pv_jnt, self.foot_ik_pv_jnt]
        ik_no_flip_jnt_list = [self.thine_ik_no_flip_jnt, self.shine_ik_no_flip_jnt, self.foot_ik_no_flip_jnt]

        a = 0
        while a < len(ik_pv_jnt_list):
            ik_pv_jnt = ik_pv_jnt_list[a]
            ik_no_flip_jnt = ik_no_flip_jnt_list[a]
            ik_jnt = ik_jnt_list[a]
            trans_blend_name = ik_pv_jnt + '_' + ik_no_flip_jnt + '_Trans_Blend_Color'

            self.connection_class.blend_one_val(blend_color_name=trans_blend_name,
                                                input_1=ik_pv_jnt,
                                                input_2=ik_no_flip_jnt,
                                                output=ik_jnt,
                                                input_1_val='translate',
                                                input_2_val='translate',
                                                output_val='translate')
            rot_blend_name = ik_pv_jnt + '_' + ik_no_flip_jnt + '_Rot_Blend_Color'
            self.connection_class.blend_one_val(blend_color_name=rot_blend_name,
                                                input_1=ik_pv_jnt,
                                                input_2=ik_no_flip_jnt,
                                                output=ik_jnt,
                                                input_1_val='rotate',
                                                input_2_val='rotate',
                                                output_val='rotate')
            cmds.connectAttr((foot_ctrl_name + '.IK_pv_no_Flip_Switch'), (trans_blend_name + '.blender'), f=True)
            cmds.connectAttr((foot_ctrl_name + '.IK_pv_no_Flip_Switch'), (rot_blend_name + '.blender'), f=True)
            cmds.connectAttr((foot_ctrl_name + '.IK_pv_no_Flip_Switch'), (ik_pv_jnt + '.v'), f=True)
            reverse_name = foot_ctrl_name + '_' + ik_no_flip_jnt + '_Reverse'
            self.connection_class.reverse_def(reverse_name=reverse_name,
                                              input=foot_ctrl_name,
                                              output=ik_no_flip_jnt,
                                              input_val='IK_pv_no_Flip_Switch',
                                              output_val='v')
            a += 1

        # PV IK HANDLE NAME
        pv_handle_name = self.prefix_name + "_" + self.leg_side + "_Foot_PV_" + str(self.val) + '_IK_Handle'
        cmds.ikHandle(n=pv_handle_name,
                      sj=self.thine_ik_pv_jnt,
                      ee=self.foot_ik_pv_jnt,
                      sol='ikRPsolver')
        cmds.setAttr((pv_handle_name + '.v'), 0)
        cmds.select(pv_handle_name, foot_ctrl_name)
        cmds.parent()

        # NO FLIP IK HANDLE NAME
        no_flip_handle_name = self.prefix_name + "_" + self.leg_side + "_Foot_No_Flip_" + str(self.val) + '_IK_Handle'
        cmds.ikHandle(n=no_flip_handle_name,
                      sj=self.thine_ik_no_flip_jnt,
                      ee=self.foot_ik_no_flip_jnt,
                      sol='ikRPsolver')
        cmds.setAttr((no_flip_handle_name + '.v'), 0)
        cmds.select(no_flip_handle_name, foot_ctrl_name)
        cmds.parent()

        # BALL HANDLE NAME
        ball_handle_name = self.prefix_name + "_" + self.leg_side + "_Ball_" + str(self.val) + '_IK_Handle'
        cmds.ikHandle(n=ball_handle_name,
                      sj=self.foot_ik_jnt,
                      ee=self.ball_ik_jnt,
                      sol='ikSCsolver')
        cmds.setAttr((ball_handle_name + '.v'), 0)
        cmds.select(ball_handle_name, foot_ctrl_name)
        cmds.parent()

        # END HANDLE NAME
        end_handle_name = self.prefix_name + "_" + self.leg_side + "_End_" + str(self.val) + '_IK_Handle'
        cmds.ikHandle(n=end_handle_name,
                      sj=self.ball_ik_jnt,
                      ee=self.end_ik_jnt,
                      sol='ikSCsolver')
        cmds.setAttr((end_handle_name + '.v'), 0)
        cmds.select(end_handle_name, foot_ctrl_name)
        cmds.parent()

        # create a stretch
        thine_to_foot_start_loc = self.prefix_name + "_" + self.leg_side + "_Thine_to_Foot_" + str(
            self.val) + '_Start_Loc'
        thine_to_foot_end_loc = self.prefix_name + "_" + self.leg_side + "_Thine_to_Foot_" + str(self.val) + '_End_Loc'
        thine_to_foot_dis = self.prefix_name + "_" + self.leg_side + "_Thine_to_Foot_" + str(self.val) + '_Dis'
        thine_to_foot_dis_shape = thine_to_foot_dis + 'Shape'
        cmds.spaceLocator(n=thine_to_foot_start_loc, p=(self.ctrl_list[self.thine_inner_ctrl]['Trans'][0],
                                                        self.ctrl_list[self.thine_inner_ctrl]['Trans'][1],
                                                        self.ctrl_list[self.thine_inner_ctrl]['Trans'][2]))
        cmds.spaceLocator(n=thine_to_foot_end_loc, p=(self.ctrl_list[self.foot_inner_ctrl]['Trans'][0],
                                                      self.ctrl_list[self.foot_inner_ctrl]['Trans'][1],
                                                      self.ctrl_list[self.foot_inner_ctrl]['Trans'][2]))
        cmds.select(thine_to_foot_start_loc, thine_to_foot_end_loc)
        cmds.distanceDimension()
        cmds.rename('distanceDimension1', thine_to_foot_dis)
        cmds.select(thine_to_foot_end_loc, foot_ctrl_name)
        cmds.parent()
        cmds.select(thine_to_foot_start_loc, thine_to_foot_end_loc)
        cmds.CenterPivot()

        driver = thine_to_foot_dis_shape + '.distance'
        thine_length = cmds.getAttr(self.shine_ik_no_flip_jnt + '.tx')
        shine_length = cmds.getAttr(self.foot_ik_no_flip_jnt + '.tx')
        sumlength = thine_length + shine_length
        cmds.setDrivenKeyframe(self.shine_ik_no_flip_jnt, currentDriver=driver, driverValue=sumlength, attribute='tx',
                               value=thine_length)
        cmds.setDrivenKeyframe(self.shine_ik_no_flip_jnt, currentDriver=driver, driverValue=sumlength * 2,
                               attribute='tx', value=thine_length * 2)

        cmds.setDrivenKeyframe(self.foot_ik_no_flip_jnt, currentDriver=driver, driverValue=sumlength, attribute='tx',
                               value=shine_length)
        cmds.setDrivenKeyframe(self.foot_ik_no_flip_jnt, currentDriver=driver, driverValue=sumlength * 2,
                               attribute='tx', value=shine_length * 2)

        driver = thine_to_foot_dis_shape + '.distance'
        thine_length = cmds.getAttr(self.shine_ik_pv_jnt + '.tx')
        shine_length = cmds.getAttr(self.foot_ik_pv_jnt + '.tx')
        sumlength = thine_length + shine_length
        cmds.setDrivenKeyframe(self.shine_ik_pv_jnt, currentDriver=driver, driverValue=sumlength, attribute='tx',
                               value=thine_length)
        cmds.setDrivenKeyframe(self.shine_ik_pv_jnt, currentDriver=driver, driverValue=sumlength * 2, attribute='tx',
                               value=thine_length * 2)

        cmds.setDrivenKeyframe(self.foot_ik_pv_jnt, currentDriver=driver, driverValue=sumlength, attribute='tx',
                               value=shine_length)
        cmds.setDrivenKeyframe(self.foot_ik_pv_jnt, currentDriver=driver, driverValue=sumlength * 2, attribute='tx',
                               value=shine_length * 2)

        mel.eval("selectKey -add -k -f 74.186363 -f 148.372726 %s;" % (self.shine_ik_pv_jnt + "_translateX"))
        mel.eval('keyTangent -e -itt linear -ott linear;')
        mel.eval('setInfinity -poi cycleRelative;')
        mel.eval("selectKey -add -k -f 74.186363 -f 148.372726 %s;" % (self.foot_ik_pv_jnt + "_translateX"))
        mel.eval('keyTangent -e -itt linear -ott linear;')
        mel.eval('setInfinity -poi cycleRelative;')

        mel.eval("selectKey -add -k -f 74.186363 -f 148.372726 %s;" % (self.shine_ik_no_flip_jnt + "_translateX"))
        mel.eval('keyTangent -e -itt linear -ott linear;')
        mel.eval('setInfinity -poi cycleRelative;')
        mel.eval("selectKey -add -k -f 74.186363 -f 148.372726 %s;" % (self.foot_ik_no_flip_jnt + "_translateX"))
        mel.eval('keyTangent -e -itt linear -ott linear;')
        mel.eval('setInfinity -poi cycleRelative;')

        # Create a knee Controller
        knee_pv_loc_name = self.prefix_name + "_" + self.leg_side + "_Knee_Pv_" + str(self.val) + '_Loc'
        knee_pv_loc_grp_name = knee_pv_loc_name + '_Grp'
        cmds.spaceLocator(n=knee_pv_loc_name, p=(self.ctrl_list[self.shine_inner_ctrl]['Trans'][0],
                                                 self.ctrl_list[self.shine_inner_ctrl]['Trans'][1],
                                                 self.ctrl_list[self.shine_inner_ctrl]['Trans'][2]))
        cmds.select(knee_pv_loc_name)
        cmds.CenterPivot()
        cmds.move(0, 0, 5, r=True)
        cmds.DeleteHistory()
        cmds.FreezeTransformations()
        cmds.select(knee_pv_loc_name, pv_handle_name)
        cmds.poleVectorConstraint()
        cmds.parentConstraint(self.foot_result_jnt, knee_pv_loc_name, mo=False)
        cmds.select(knee_pv_loc_name + '_parentConstraint1')
        cmds.delete()
        cmds.select(knee_pv_loc_name)
        cmds.move(13, 0, 0, r=True)
        # setAttr "Template_L_Foot_PV_1_IK_Handle.twist" 90;
        cmds.setAttr((pv_handle_name + '.twist'), 90)
        # make a Group
        cmds.select(knee_pv_loc_name)
        cmds.group(n=knee_pv_loc_grp_name)
        # move -rpr 8.177 9.675004 -0.261 Template_L_Knee_Pv_1_Loc.scalePivot Template_L_Knee_Pv_1_Loc.rotatePivot ;
        cmds.move(self.ctrl_list[self.foot_inner_ctrl]['Trans'][0],
                  self.ctrl_list[self.foot_inner_ctrl]['Trans'][1],
                  self.ctrl_list[self.foot_inner_ctrl]['Trans'][2],
                  (knee_pv_loc_grp_name + '.scalePivot'),
                  (knee_pv_loc_grp_name + '.rotatePivot'))

        cmds.addAttr(foot_ctrl_name, ln="Rv_Knee_Rot", at='double')
        cmds.setAttr((foot_ctrl_name + ".Rv_Knee_Rot"), e=True, keyable=True)
        cmds.connectAttr((foot_ctrl_name + '.Rv_Knee_Rot'), (knee_pv_loc_grp_name + '.ry'))
        cmds.setAttr((knee_pv_loc_grp_name + '.v'), 0)
        cmds.select(knee_pv_loc_grp_name, foot_ctrl_name)
        cmds.parent()

        knee_noflip_loc_name = self.prefix_name + "_" + self.leg_side + "_Knee_noFlip_" + str(self.val) + '_Loc'
        knee_noflip_loc_grp_name = knee_noflip_loc_name + '_Grp'
        cmds.spaceLocator(n=knee_noflip_loc_name, p=(self.ctrl_list[self.shine_inner_ctrl]['Trans'][0],
                                                     self.ctrl_list[self.shine_inner_ctrl]['Trans'][1],
                                                     self.ctrl_list[self.shine_inner_ctrl]['Trans'][2]))
        cmds.select(knee_noflip_loc_name)
        cmds.CenterPivot()
        cmds.move(0, 0, 5, r=True)
        cmds.DeleteHistory()
        cmds.FreezeTransformations()
        cmds.select(knee_noflip_loc_name, no_flip_handle_name)
        cmds.poleVectorConstraint()

        # Create a Handle
        self.controller_class.traiangle_new_ctrl()
        knee_noflip_ctrl_name = self.prefix_name + "_" + self.leg_side + "_Knee_noFlip_" + str(self.val) + '_Ctrl'
        knee_noflip_ctrl_grp_name = knee_noflip_ctrl_name + '_Grp'
        cmds.rename('Triangle_new_ctrl', knee_noflip_ctrl_name)
        cmds.parentConstraint(knee_noflip_loc_name, knee_noflip_ctrl_name, mo=False)
        knee_loc_pos = cmds.getAttr(knee_noflip_ctrl_name + '.t')[0]
        cmds.select(knee_noflip_ctrl_name + '_parentConstraint1')
        cmds.delete()
        cmds.select(knee_noflip_ctrl_name)
        cmds.DeleteHistory()
        cmds.FreezeTransformations()
        cmds.select(knee_noflip_loc_name, knee_noflip_ctrl_name)
        cmds.parent()
        cmds.select(knee_noflip_ctrl_name)
        cmds.group(n=knee_noflip_ctrl_grp_name)

        # knee Stretch
        # THINE TO KNEE DIS
        thine_to_knee_start_loc = self.prefix_name + "_" + self.leg_side + "_Thine_to_Knee_" + str(
            self.val) + '_Start_Loc'
        thine_to_knee_end_loc = self.prefix_name + "_" + self.leg_side + "_Thine_to_Knee_" + str(self.val) + '_End_Loc'
        thine_to_knee_dis = self.prefix_name + "_" + self.leg_side + "_Thine_to_Knee_" + str(self.val) + '_Dis'
        thine_to_knee_dis_shape = thine_to_knee_dis + 'Shape'
        cmds.spaceLocator(n=thine_to_knee_start_loc, p=(self.ctrl_list[self.thine_inner_ctrl]['Trans'][0],
                                                        self.ctrl_list[self.thine_inner_ctrl]['Trans'][1],
                                                        self.ctrl_list[self.thine_inner_ctrl]['Trans'][2]))
        cmds.spaceLocator(n=thine_to_knee_end_loc, p=(knee_loc_pos[0],
                                                      knee_loc_pos[1],
                                                      knee_loc_pos[2]))
        cmds.select(thine_to_knee_start_loc, thine_to_knee_end_loc)
        cmds.distanceDimension()
        cmds.select(thine_to_knee_start_loc, thine_to_knee_end_loc)
        cmds.CenterPivot()
        cmds.rename('distanceDimension1', thine_to_knee_dis)
        cmds.select(thine_to_knee_end_loc, knee_noflip_ctrl_name)
        cmds.parent()

        # KNEE TO FOOT DIS
        knee_to_foot_start_loc = self.prefix_name + "_" + self.leg_side + "_Knee_to_Foot_" + str(
            self.val) + '_Start_Loc'
        knee_to_foot_end_loc = self.prefix_name + "_" + self.leg_side + "_Knee_to_Foot_" + str(self.val) + '_End_Loc'
        knee_to_foot_dis = self.prefix_name + "_" + self.leg_side + "_Knee_to_Foot_" + str(self.val) + '_Dis'
        knee_to_foot_dis_shape = knee_to_foot_dis + 'Shape'
        cmds.spaceLocator(n=knee_to_foot_start_loc, p=(knee_loc_pos[0],
                                                       knee_loc_pos[1],
                                                       knee_loc_pos[2]))
        cmds.spaceLocator(n=knee_to_foot_end_loc, p=(self.ctrl_list[self.foot_inner_ctrl]['Trans'][0],
                                                     self.ctrl_list[self.foot_inner_ctrl]['Trans'][1],
                                                     self.ctrl_list[self.foot_inner_ctrl]['Trans'][2]))
        cmds.select(knee_to_foot_start_loc, knee_to_foot_end_loc)
        cmds.distanceDimension()
        cmds.select(knee_to_foot_start_loc, knee_to_foot_end_loc)
        cmds.CenterPivot()
        cmds.rename('distanceDimension1', knee_to_foot_dis)
        cmds.select(knee_to_foot_start_loc, knee_noflip_ctrl_name)
        cmds.parent()
        cmds.select(knee_to_foot_end_loc, foot_ctrl_name)
        cmds.parent()

        cmds.addAttr(knee_noflip_ctrl_name, ln="Knee_Snap", at='double', min=0, max=1)
        cmds.setAttr((knee_noflip_ctrl_name + ".Knee_Snap"), e=True, keyable=True)

        # connect with the no Flip
        # Create a Blend Color
        blend_color_name = self.prefix_name + "_" + self.leg_side + "_Upper_Leg_Stretch_" + str(self.val) + '_Blend'
        cmds.createNode('blendColors', n=blend_color_name)
        cmds.connectAttr((thine_to_knee_dis_shape + '.distance'), (blend_color_name + '.color1.color1R'), f=True)
        cmds.connectAttr((self.shine_ik_no_flip_jnt + '_translateX.output'), (blend_color_name + '.color2R'), f=True)
        cmds.connectAttr((blend_color_name + '.outputR'), (self.shine_ik_no_flip_jnt + '.tx'), f=True)
        cmds.connectAttr((knee_noflip_ctrl_name + '.Knee_Snap'), (blend_color_name + '.blender'), f=True)

        # Create a Blend Color
        blend_color_name = self.prefix_name + "_" + self.leg_side + "_Lower_Leg_Stretch_" + str(self.val) + '_Blend'
        cmds.createNode('blendColors', n=blend_color_name)
        cmds.connectAttr((knee_to_foot_dis_shape + '.distance'), (blend_color_name + '.color1.color1R'), f=True)
        cmds.connectAttr((self.foot_ik_no_flip_jnt + '_translateX.output'), (blend_color_name + '.color2R'), f=True)
        cmds.connectAttr((blend_color_name + '.outputR'), (self.foot_ik_no_flip_jnt + '.tx'), f=True)
        cmds.connectAttr((knee_noflip_ctrl_name + '.Knee_Snap'), (blend_color_name + '.blender'), f=True)

        # hide the uneanted the object
        list = [thine_to_foot_start_loc, thine_to_foot_dis, thine_to_foot_end_loc, thine_to_knee_start_loc,
                thine_to_knee_end_loc, thine_to_knee_dis,
                knee_to_foot_dis, knee_to_foot_end_loc, knee_to_foot_start_loc, knee_pv_loc_name, knee_noflip_loc_name]
        for each_loc in list: \
                cmds.setAttr((each_loc + '.v'), 0)

        knee_pv_no_flip_reverse = self.prefix_name + "_" + self.leg_side + "_Knee_pv_noFlip_" + str(self.val) + '_Rev'
        self.connection_class.reverse_def(reverse_name=knee_pv_no_flip_reverse,
                                          input=foot_ctrl_name,
                                          output=knee_noflip_ctrl_name,
                                          input_val='IK_pv_no_Flip_Switch',
                                          output_val='v')
        cmds.connectAttr((ik_fk_switch_name + '.IK_FK_Switch'), (knee_noflip_ctrl_grp_name + '.v'))

        cmds.addAttr(foot_ctrl_name, ln="Auto_Knee_Thine_Length", at='double', min=0, dv=1)
        cmds.setAttr((foot_ctrl_name + ".Auto_Knee_Thine_Length"), e=True, keyable=True)

        cmds.addAttr(foot_ctrl_name, ln="Auto_Knee_Shine_Length", at='double', min=0, dv=1)
        cmds.setAttr((foot_ctrl_name + ".Auto_Knee_Shine_Length"), e=True, keyable=True)

        blend_color_name = self.prefix_name + "_" + self.leg_side + "_Upper_Leg_Stretch_" + str(self.val) + '_Blend'
        mult_div_name = self.prefix_name + "_" + self.leg_side + "_auto_knee_thine_length_" + str(self.val) + '_Mult'
        cmds.createNode('multiplyDivide', n=mult_div_name)
        cmds.connectAttr((foot_ctrl_name + '.Auto_Knee_Thine_Length'), (mult_div_name + '.input1.input1X'), f=True)
        cmds.connectAttr((self.shine_ik_no_flip_jnt + '_translateX.output'), (mult_div_name + '.input2.input2X'),
                         f=True)
        cmds.connectAttr((mult_div_name + '.output.outputX'), (blend_color_name + '.color2.color2R'), f=True)

        blend_color_name = self.prefix_name + "_" + self.leg_side + "_Lower_Leg_Stretch_" + str(self.val) + '_Blend'
        mult_div_name = self.prefix_name + "_" + self.leg_side + "_auto_knee_shine_length_" + str(self.val) + '_Mult'
        cmds.createNode('multiplyDivide', n=mult_div_name)
        cmds.connectAttr((foot_ctrl_name + '.Auto_Knee_Shine_Length'), (mult_div_name + '.input1.input1X'), f=True)
        # Template_L_Leg_Foot_1_Ik_no_flip_Jnt_translateX
        cmds.connectAttr((self.foot_ik_no_flip_jnt + '_translateX.output'), (mult_div_name + '.input2.input2X'), f=True)
        cmds.connectAttr((mult_div_name + '.output.outputX'), (blend_color_name + '.color2.color2R'), f=True)

        # Select all the
        cmds.select(self.thine_ik_jnt, self.thine_fk_jnt, self.thine_result_jnt, thine_ik_pv_grp_name,
                    thine_ik_no_flip_grp_name, ik_fk_switch_grp_name, foot_ctrl_grp_name,
                    thine_to_foot_start_loc, thine_to_foot_dis, knee_noflip_ctrl_grp_name, thine_to_knee_start_loc,
                    thine_to_knee_dis, knee_to_foot_dis)
        main_grp_name = self.prefix_name + "_" + self.leg_side + "_Leg_" + str(self.val) + '_Grp'
        cmds.group(n=main_grp_name)
        root_grp_name = "Root_Grp"
        if cmds.objExists(root_grp_name):
            pass
        else:
            cmds.createNode('transform', n=root_grp_name)
        cmds.select(main_grp_name, root_grp_name)
        cmds.parent()

        cmds.select(self.thine_result_jnt, self.thine_ik_jnt, thine_ik_pv_grp_name, thine_ik_no_flip_grp_name,
                    thine_to_foot_start_loc, thine_to_foot_dis,
                    thine_to_knee_start_loc, thine_to_knee_dis, knee_to_foot_dis)
        do_not_touch_grp_name = self.prefix_name + "_" + self.leg_side + "_Leg_" + str(self.val) + '_Do_Not_Touch_Grp'
        cmds.group(n=do_not_touch_grp_name)

        cmds.select(thine_to_foot_start_loc, thine_to_knee_start_loc, self.thine_ik_jnt, thine_ik_pv_grp_name,
                    thine_ik_no_flip_grp_name)
        ik_const_grp = self.prefix_name + "_" + self.leg_side + "_Leg_" + str(self.val) + '_Ik_Const_Grp'
        cmds.group(n=ik_const_grp)
        # move -rpr 9.082711 12.330127 11.057034 Template_Human_Head_Neck_Tem_1_Ctrl.scalePivot Template_Human_Head_Neck_Tem_1_Ctrl.rotatePivot ;
        cmds.move(self.ctrl_list[self.thine_inner_ctrl]['Trans'][0],
                  self.ctrl_list[self.thine_inner_ctrl]['Trans'][1],
                  self.ctrl_list[self.thine_inner_ctrl]['Trans'][2],
                  (ik_const_grp + '.scalePivot'),
                  (ik_const_grp + '.rotatePivot'))

        cmds.select(self.thine_result_jnt)
        result_const_grp = self.prefix_name + "_" + self.leg_side + "_Leg_" + str(self.val) + '_Result_Const_Grp'
        cmds.group(n=result_const_grp)
        cmds.move(self.ctrl_list[self.thine_inner_ctrl]['Trans'][0],
                  self.ctrl_list[self.thine_inner_ctrl]['Trans'][1],
                  self.ctrl_list[self.thine_inner_ctrl]['Trans'][2],
                  (result_const_grp + '.scalePivot'),
                  (result_const_grp + '.rotatePivot'))

        # Create a Fk Grp
        fk_const_grp = self.prefix_name + "_" + self.leg_side + "_Leg_" + str(self.val) + '_Fk_Const_Grp'
        cmds.select(self.thine_fk_jnt)
        cmds.group(n=fk_const_grp)
        cmds.move(self.ctrl_list[self.thine_inner_ctrl]['Trans'][0],
                  self.ctrl_list[self.thine_inner_ctrl]['Trans'][1],
                  self.ctrl_list[self.thine_inner_ctrl]['Trans'][2],
                  (fk_const_grp + '.scalePivot'),
                  (fk_const_grp + '.rotatePivot'))

        # leg_spaceLoc
        leg_hip_space_loc = self.prefix_name + "_" + self.leg_side + "_Leg_Hip_Space_" + str(self.val) + '_Loc'
        cmds.spaceLocator(n=leg_hip_space_loc, p=(self.ctrl_list[self.thine_inner_ctrl]['Trans'][0],
                                                  self.ctrl_list[self.thine_inner_ctrl]['Trans'][1],
                                                  self.ctrl_list[self.thine_inner_ctrl]['Trans'][2]))

        # BODY AND ROOT SPACE LOC
        body_space_loc = self.prefix_name + "_" + self.leg_side + "_Leg_Body_Space_" + str(self.val) + '_Loc'
        cmds.spaceLocator(n=body_space_loc, p=(self.ctrl_list[self.thine_inner_ctrl]['Trans'][0],
                                               self.ctrl_list[self.thine_inner_ctrl]['Trans'][1],
                                               self.ctrl_list[self.thine_inner_ctrl]['Trans'][2]))
        root_space_loc = self.prefix_name + "_" + self.leg_side + "_Leg_Root_Space_" + str(self.val) + '_Loc'
        cmds.spaceLocator(n=root_space_loc, p=(self.ctrl_list[self.thine_inner_ctrl]['Trans'][0],
                                               self.ctrl_list[self.thine_inner_ctrl]['Trans'][1],
                                               self.ctrl_list[self.thine_inner_ctrl]['Trans'][2]))

        cmds.select(leg_hip_space_loc, body_space_loc, root_space_loc)
        cmds.CenterPivot()

        cmds.pointConstraint(leg_hip_space_loc, ik_const_grp, mo=True)
        cmds.pointConstraint(leg_hip_space_loc, result_const_grp, mo=True)
        cmds.pointConstraint(leg_hip_space_loc, fk_const_grp, mo=True)
        cmds.orientConstraint(leg_hip_space_loc, body_space_loc, root_space_loc, ik_const_grp, mo=True)
        cmds.orientConstraint(leg_hip_space_loc, body_space_loc, root_space_loc, result_const_grp, mo=True)
        cmds.orientConstraint(leg_hip_space_loc, body_space_loc, root_space_loc, fk_const_grp, mo=True)

        # add Rotation space loc

        cmds.addAttr(ik_fk_switch_name, ln="FK_Rotation_Space", at='enum', en='Hip:UpperBody:Root')
        cmds.setAttr((ik_fk_switch_name + ".FK_Rotation_Space"), e=True, keyable=True)

        # cmds.setDrivenKeyframe((self.shine_fk_jnt + ".tx"),currentDriver=(self.thine_fk_jnt + ".Stretch"))
        cmds.setAttr((ik_fk_switch_name + ".FK_Rotation_Space"), 0)
        cmds.setAttr((fk_const_grp + "_orientConstraint1." + leg_hip_space_loc + 'W0'), 1)
        cmds.setAttr((fk_const_grp + "_orientConstraint1." + body_space_loc + 'W1'), 0)
        cmds.setAttr((fk_const_grp + "_orientConstraint1." + root_space_loc + 'W2'), 0)
        cmds.setAttr((result_const_grp + "_orientConstraint1." + leg_hip_space_loc + 'W0'), 1)
        cmds.setAttr((result_const_grp + "_orientConstraint1." + body_space_loc + 'W1'), 0)
        cmds.setAttr((result_const_grp + "_orientConstraint1." + root_space_loc + 'W2'), 0)
        cmds.setDrivenKeyframe((fk_const_grp + "_orientConstraint1." + leg_hip_space_loc + 'W0'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))
        cmds.setDrivenKeyframe((fk_const_grp + "_orientConstraint1." + body_space_loc + 'W1'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))
        cmds.setDrivenKeyframe((fk_const_grp + "_orientConstraint1." + root_space_loc + 'W2'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))
        cmds.setDrivenKeyframe((result_const_grp + "_orientConstraint1." + leg_hip_space_loc + 'W0'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))
        cmds.setDrivenKeyframe((result_const_grp + "_orientConstraint1." + body_space_loc + 'W1'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))
        cmds.setDrivenKeyframe((result_const_grp + "_orientConstraint1." + root_space_loc + 'W2'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))

        cmds.setAttr((ik_fk_switch_name + ".FK_Rotation_Space"), 1)
        cmds.setAttr((fk_const_grp + "_orientConstraint1." + leg_hip_space_loc + 'W0'), 0)
        cmds.setAttr((fk_const_grp + "_orientConstraint1." + body_space_loc + 'W1'), 1)
        cmds.setAttr((fk_const_grp + "_orientConstraint1." + root_space_loc + 'W2'), 0)
        cmds.setAttr((result_const_grp + "_orientConstraint1." + leg_hip_space_loc + 'W0'), 0)
        cmds.setAttr((result_const_grp + "_orientConstraint1." + body_space_loc + 'W1'), 1)
        cmds.setAttr((result_const_grp + "_orientConstraint1." + root_space_loc + 'W2'), 0)
        cmds.setDrivenKeyframe((fk_const_grp + "_orientConstraint1." + leg_hip_space_loc + 'W0'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))
        cmds.setDrivenKeyframe((fk_const_grp + "_orientConstraint1." + body_space_loc + 'W1'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))
        cmds.setDrivenKeyframe((fk_const_grp + "_orientConstraint1." + root_space_loc + 'W2'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))
        cmds.setDrivenKeyframe((result_const_grp + "_orientConstraint1." + leg_hip_space_loc + 'W0'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))
        cmds.setDrivenKeyframe((result_const_grp + "_orientConstraint1." + body_space_loc + 'W1'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))
        cmds.setDrivenKeyframe((result_const_grp + "_orientConstraint1." + root_space_loc + 'W2'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))

        cmds.setAttr((ik_fk_switch_name + ".FK_Rotation_Space"), 2)
        cmds.setAttr((fk_const_grp + "_orientConstraint1." + leg_hip_space_loc + 'W0'), 0)
        cmds.setAttr((fk_const_grp + "_orientConstraint1." + body_space_loc + 'W1'), 0)
        cmds.setAttr((fk_const_grp + "_orientConstraint1." + root_space_loc + 'W2'), 1)
        cmds.setAttr((result_const_grp + "_orientConstraint1." + leg_hip_space_loc + 'W0'), 0)
        cmds.setAttr((result_const_grp + "_orientConstraint1." + body_space_loc + 'W1'), 0)
        cmds.setAttr((result_const_grp + "_orientConstraint1." + root_space_loc + 'W2'), 1)
        cmds.setDrivenKeyframe((fk_const_grp + "_orientConstraint1." + leg_hip_space_loc + 'W0'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))
        cmds.setDrivenKeyframe((fk_const_grp + "_orientConstraint1." + body_space_loc + 'W1'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))
        cmds.setDrivenKeyframe((fk_const_grp + "_orientConstraint1." + root_space_loc + 'W2'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))
        cmds.setDrivenKeyframe((result_const_grp + "_orientConstraint1." + leg_hip_space_loc + 'W0'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))
        cmds.setDrivenKeyframe((result_const_grp + "_orientConstraint1." + body_space_loc + 'W1'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))
        cmds.setDrivenKeyframe((result_const_grp + "_orientConstraint1." + root_space_loc + 'W2'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))

        blend_color_name = self.prefix_name + "_" + self.leg_side + "_Leg_Result_Orient_" + str(self.val) + '_Blend'
        cmds.createNode('blendColors', n=blend_color_name)

        # connectAttr -f Template_L_Leg_1_Result_Const_Grp_orientConstraint1.constraintRotate blendColors1.color2;

        cmds.connectAttr((result_const_grp + '_orientConstraint1.constraintRotate'), (blend_color_name + '.color2'),
                         f=True)
        cmds.setAttr((blend_color_name + '.color1R'), 0)
        cmds.connectAttr((ik_fk_switch_name + '.IK_FK_Switch'), (blend_color_name + '.blender'), f=True)
        # connectAttr -f blendColors1.output Template_L_Leg_1_Result_Const_Grp.rotate;
        cmds.connectAttr((blend_color_name + '.output'), (result_const_grp + '.r'), f=True)

        # Hide unwanted object
        transform_object = [self.thine_fk_jnt, self.shine_fk_jnt, self.foot_fk_jnt, self.ball_fk_jnt, ik_fk_switch_name,
                            fk_const_grp, ik_const_grp, result_const_grp]
        for each_obj in transform_object:
            self.helper_class.transform_rotation_scale_visible(each_obj, t=True, r=False, s=False)
        rotate_object = [ik_fk_switch_name, knee_noflip_ctrl_name, fk_const_grp, ik_const_grp, result_const_grp]
        for each_obj in rotate_object:
            self.helper_class.transform_rotation_scale_visible(each_obj, t=False, r=True, s=False)
        scale_object = [self.thine_fk_jnt, self.shine_fk_jnt, self.foot_fk_jnt, self.ball_fk_jnt, ik_fk_switch_name,
                        knee_noflip_ctrl_name, foot_ctrl_name,
                        fk_const_grp, ik_const_grp, result_const_grp]
        for each_obj in scale_object:
            self.helper_class.transform_rotation_scale_visible(each_obj, t=False, r=False, s=True)

        mult_div_name = self.prefix_name + "_" + self.leg_side + "_Global_Scale_Normalize_" + str(self.val) + '_Mult'
        cmds.createNode('multiplyDivide', n=mult_div_name)
        # connectAttr -f Template_L_Thine_to_Foot_1_DisShape.distance multiplyDivide1.input1X;
        cmds.connectAttr((thine_to_foot_dis_shape + '.distance'), (mult_div_name + '.input1X'), f=True)
        cmds.connectAttr((root_grp_name + '.scale.scaleY'), (mult_div_name + '.input2.input2X'), f=True)
        # setAttr "multiplyDivide1.operation" 2;
        cmds.setAttr((mult_div_name + '.operation'), 2)
        cmds.connectAttr((mult_div_name + '.output.outputX'), (self.foot_ik_no_flip_jnt + '_translateX.input'), f=True)
        cmds.connectAttr((mult_div_name + '.output.outputX'), (self.shine_ik_no_flip_jnt + '_translateX.input'), f=True)
        cmds.connectAttr((mult_div_name + '.output.outputX'), (self.foot_ik_pv_jnt + '_translateX.input'), f=True)
        cmds.connectAttr((mult_div_name + '.output.outputX'), (self.shine_ik_pv_jnt + '_translateX.input'), f=True)

        # put the locator in the grp
        cmds.select(leg_hip_space_loc, body_space_loc, root_space_loc, root_grp_name)
        cmds.parent()

        # Create a Reverse Foot
        heel_loc_name = self.prefix_name + "_" + self.leg_side + "_Leg_Heel_" + str(self.val) + '_Loc'
        cmds.spaceLocator(n=heel_loc_name, p=(self.ctrl_list[self.foot_inner_ctrl]['Trans'][0],
                                              self.ctrl_list[self.foot_inner_ctrl]['Trans'][1],
                                              self.ctrl_list[self.foot_inner_ctrl]['Trans'][2]))
        cmds.select(heel_loc_name)
        cmds.move(0, -9, -4, r=True)
        cmds.DeleteHistory()
        cmds.FreezeTransformations()
        cmds.CenterPivot()

        ball_loc_name = self.prefix_name + "_" + self.leg_side + "_Leg_Ball_" + str(self.val) + '_Loc'
        cmds.spaceLocator(n=ball_loc_name, p=(self.ctrl_list[self.ball_inner_ctrl]['Trans'][0],
                                              self.ctrl_list[self.ball_inner_ctrl]['Trans'][1],
                                              self.ctrl_list[self.ball_inner_ctrl]['Trans'][2]))
        cmds.select(ball_loc_name)
        cmds.DeleteHistory()
        cmds.FreezeTransformations()
        cmds.CenterPivot()

        toe_loc_name = self.prefix_name + "_" + self.leg_side + "_Leg_Toe_" + str(self.val) + '_Loc'
        cmds.spaceLocator(n=toe_loc_name, p=(self.ctrl_list[self.end_inner_ctrl]['Trans'][0],
                                             self.ctrl_list[self.end_inner_ctrl]['Trans'][1],
                                             self.ctrl_list[self.end_inner_ctrl]['Trans'][2]))
        cmds.select(toe_loc_name)
        cmds.DeleteHistory()
        cmds.FreezeTransformations()
        cmds.CenterPivot()

        # parent to all the ik controller
        cmds.select(heel_loc_name, ball_loc_name, toe_loc_name, foot_ctrl_name)
        cmds.parent()
        cmds.select(toe_loc_name, ball_loc_name, end_handle_name, ball_handle_name, no_flip_handle_name, pv_handle_name,
                    heel_loc_name)
        cmds.parent()
        cmds.select(no_flip_handle_name, pv_handle_name, ball_handle_name, knee_pv_loc_grp_name, thine_to_foot_end_loc,
                    knee_to_foot_end_loc, ball_loc_name)
        cmds.parent()
        cmds.select(ball_loc_name, toe_loc_name)
        cmds.parent()

        # add Attr
        cmds.addAttr(foot_ctrl_name, ln="Roll", at='double')
        cmds.setAttr((foot_ctrl_name + ".Roll"), e=True, keyable=True)

        cmds.addAttr(foot_ctrl_name, ln="Bend_Limit", at='double', dv=45)
        cmds.setAttr((foot_ctrl_name + ".Bend_Limit"), e=True, keyable=True)

        cmds.addAttr(foot_ctrl_name, ln="Toe_Stright", at='double', dv=70)
        cmds.setAttr((foot_ctrl_name + ".Toe_Stright"), e=True, keyable=True)

        # Create a Node
        heel_rot_clamp = self.prefix_name + "_" + self.leg_side + "_Leg_Heel_Rot_" + str(self.val) + '_Clamp'
        cmds.createNode('clamp', n=heel_rot_clamp)
        cmds.connectAttr((foot_ctrl_name + '.Roll'), (heel_rot_clamp + '.input.inputR'))
        # setAttr "clamp1.minR" -90;
        cmds.setAttr((heel_rot_clamp + '.minR'), -90)
        cmds.connectAttr((heel_rot_clamp + '.output.outputR'), (heel_loc_name + '.rx'))

        ball_rot_clamp = self.prefix_name + "_" + self.leg_side + "_Leg_Ball_Zero_to_Bend_" + str(self.val) + '_Clamp'
        cmds.createNode('clamp', n=ball_rot_clamp)
        cmds.connectAttr((foot_ctrl_name + '.Roll'), (ball_rot_clamp + '.input.inputR'))
        # setAttr "clamp1.minR" -90;
        cmds.setAttr((ball_rot_clamp + '.maxR'), 90)
        # cmds.connectAttr((heel_rot_clamp + '.output.outputR'),(ball_loc_name + '.rx'))

        foot_bend_to_stright_clamp = self.prefix_name + "_" + self.leg_side + "_Leg_Foot_Bend_to_Stright_" + str(
            self.val) + '_Clamp'
        cmds.createNode('clamp', n=foot_bend_to_stright_clamp)
        cmds.connectAttr((foot_ctrl_name + '.Bend_Limit'), (foot_bend_to_stright_clamp + '.min.minR'))
        cmds.connectAttr((foot_ctrl_name + '.Toe_Stright'), (foot_bend_to_stright_clamp + '.max.maxR'))
        cmds.connectAttr((foot_ctrl_name + '.Roll'), (foot_bend_to_stright_clamp + '.input.inputR'))

        foot_bend_to_stright_percent = self.prefix_name + "_" + self.leg_side + "_Leg_Foot_Bend_to_Stright_" + str(
            self.val) + '_Percent'
        cmds.createNode('setRange', n=foot_bend_to_stright_percent)
        cmds.connectAttr((foot_bend_to_stright_clamp + '.min.minR'), (foot_bend_to_stright_percent + '.oldMin.oldMinX'))
        cmds.connectAttr((foot_bend_to_stright_clamp + '.max.maxR'), (foot_bend_to_stright_percent + '.oldMax.oldMaxX'))
        # connectAttr -f clamp1.inputR setRange1.valueX;
        cmds.setAttr((foot_bend_to_stright_percent + '.maxX'), 1)
        cmds.connectAttr((foot_bend_to_stright_clamp + '.inputR'), (foot_bend_to_stright_percent + '.valueX'))

        foot_roll_Mult = self.prefix_name + "_" + self.leg_side + "_Leg_Foot_Roll_" + str(self.val) + '_Mult'
        cmds.createNode('multiplyDivide', n=foot_roll_Mult)
        cmds.connectAttr((foot_bend_to_stright_percent + '.outValue.outValueX'), (foot_roll_Mult + '.input1.input1X'))
        # connectAttr -f clamp1.inputR multiplyDivide1.input2X;
        cmds.connectAttr((foot_bend_to_stright_clamp + '.inputR'), (foot_roll_Mult + '.input2.input2X'))
        cmds.connectAttr((foot_roll_Mult + '.output.outputX'), (toe_loc_name + '.rx'))

        cmds.connectAttr((foot_ctrl_name + '.Bend_Limit'), (ball_rot_clamp + '.max.maxR'))

        ball_zero_to_bend_percent = self.prefix_name + "_" + self.leg_side + "_Leg_Ball_Zero_to_Bend_" + str(
            self.val) + '_Percent'
        cmds.createNode('setRange', n=ball_zero_to_bend_percent)
        cmds.connectAttr((ball_rot_clamp + '.min.minR'), (ball_zero_to_bend_percent + '.oldMin.oldMinX'))
        cmds.connectAttr((ball_rot_clamp + '.max.maxR'), (ball_zero_to_bend_percent + '.oldMax.oldMaxX'))
        cmds.setAttr((ball_zero_to_bend_percent + '.maxX'), 1)
        cmds.connectAttr((ball_rot_clamp + '.inputR'), (ball_zero_to_bend_percent + '.valueX'))

        foot_invert_percent = self.prefix_name + "_" + self.leg_side + "_Leg_Foot_Invert_" + str(self.val) + '_Percent'
        cmds.createNode('plusMinusAverage', n=foot_invert_percent)
        cmds.setAttr((foot_invert_percent + '.input1D[0]'), 1)
        cmds.setAttr((foot_invert_percent + '.input1D[1]'), 1)
        cmds.connectAttr((foot_bend_to_stright_percent + '.outValue.outValueX'), (foot_invert_percent + '.input1D[1]'))
        # setAttr "plusMinusAverage1.operation" 2;
        cmds.setAttr((foot_invert_percent + '.operation'), 2)

        ball_percent_Mult = self.prefix_name + "_" + self.leg_side + "_Leg_Ball_Percent_" + str(self.val) + '_Mult'
        cmds.createNode('multiplyDivide', n=ball_percent_Mult)
        cmds.connectAttr((ball_zero_to_bend_percent + '.outValue.outValueX'), (ball_percent_Mult + '.input1.input1X'))
        cmds.connectAttr((foot_invert_percent + '.output1D'), (ball_percent_Mult + '.input2.input2X'))

        ball_roll_Mult = self.prefix_name + "_" + self.leg_side + "_Leg_Ball_Roll_" + str(self.val) + '_Mult'
        cmds.createNode('multiplyDivide', n=ball_roll_Mult)
        cmds.connectAttr((ball_percent_Mult + '.output.outputX'), (ball_roll_Mult + '.input1.input1X'))
        cmds.connectAttr((foot_ctrl_name + '.Roll'), (ball_roll_Mult + '.input2.input2X'))
        cmds.connectAttr((ball_roll_Mult + '.output.outputX'), (ball_loc_name + '.rx'))

        # Create a Side Rotate
        inner_foot_loc_name = self.prefix_name + "_" + self.leg_side + "_Leg_Inner_Foot_" + str(self.val) + '_Loc'
        cmds.spaceLocator(n=inner_foot_loc_name, p=(self.ctrl_list[self.ball_inner_ctrl]['Trans'][0],
                                                    self.ctrl_list[self.ball_inner_ctrl]['Trans'][1],
                                                    self.ctrl_list[self.ball_inner_ctrl]['Trans'][2]))
        cmds.select(inner_foot_loc_name)
        if self.leg_side == 'L':
            cmds.move(-5, 0, 0, r=True)
        else:
            cmds.move(5, 0, 0, r=True)

        cmds.DeleteHistory()
        cmds.FreezeTransformations()
        cmds.CenterPivot()

        outer_foot_loc_name = self.prefix_name + "_" + self.leg_side + "_Leg_Outer_Foot_" + str(self.val) + '_Loc'
        cmds.spaceLocator(n=outer_foot_loc_name, p=(self.ctrl_list[self.ball_inner_ctrl]['Trans'][0],
                                                    self.ctrl_list[self.ball_inner_ctrl]['Trans'][1],
                                                    self.ctrl_list[self.ball_inner_ctrl]['Trans'][2]))
        cmds.select(outer_foot_loc_name)
        if self.leg_side == 'L':
            cmds.move(5, 0, 0, r=True)
        else:
            cmds.move(-5, 0, 0, r=True)
        cmds.DeleteHistory()
        cmds.FreezeTransformations()
        cmds.CenterPivot()

        cmds.select(inner_foot_loc_name, outer_foot_loc_name)
        cmds.parent()
        cmds.select(outer_foot_loc_name, heel_loc_name)
        cmds.parent()
        cmds.select(toe_loc_name, end_handle_name, inner_foot_loc_name)
        cmds.parent()

        cmds.addAttr(foot_ctrl_name, ln="Tilt", at='double', min=-10, max=10)
        cmds.setAttr((foot_ctrl_name + ".Tilt"), e=True, keyable=True)

        cmds.setAttr((foot_ctrl_name + ".Tilt"), 0)
        cmds.setAttr((inner_foot_loc_name + '.rz'), 0)
        cmds.setAttr((outer_foot_loc_name + '.rz'), 0)
        cmds.setDrivenKeyframe((inner_foot_loc_name + ".rz"), currentDriver=(foot_ctrl_name + ".Tilt"))
        cmds.setDrivenKeyframe((outer_foot_loc_name + ".rz"), currentDriver=(foot_ctrl_name + ".Tilt"))

        if self.leg_side == 'L':
            inner_val = 90
            outer_val = -90
        else:
            inner_val = -90
            outer_val = 90

        cmds.setAttr((foot_ctrl_name + ".Tilt"), -10)
        cmds.setAttr((inner_foot_loc_name + '.rz'), inner_val)
        cmds.setAttr((outer_foot_loc_name + '.rz'), 0)
        cmds.setDrivenKeyframe((inner_foot_loc_name + ".rz"), currentDriver=(foot_ctrl_name + ".Tilt"))
        cmds.setDrivenKeyframe((outer_foot_loc_name + ".rz"), currentDriver=(foot_ctrl_name + ".Tilt"))

        cmds.setAttr((foot_ctrl_name + ".Tilt"), 10)
        cmds.setAttr((inner_foot_loc_name + '.rz'), 0)
        cmds.setAttr((outer_foot_loc_name + '.rz'), outer_val)
        cmds.setDrivenKeyframe((inner_foot_loc_name + ".rz"), currentDriver=(foot_ctrl_name + ".Tilt"))
        cmds.setDrivenKeyframe((outer_foot_loc_name + ".rz"), currentDriver=(foot_ctrl_name + ".Tilt"))
        cmds.setAttr((foot_ctrl_name + ".Tilt"), 0)

        # Create  a Controller for the loc
        # get the attr
        heel_common = self.prefix_name + "_" + self.leg_side + "_Leg_Heel_" + str(self.val)
        heel_ctrl_name = self.foot_side_ctrl_set(heel_common)

        inner_foot_common = self.prefix_name + "_" + self.leg_side + "_Leg_Inner_Foot_" + str(self.val)
        inner_foot_ctrl_name = self.foot_side_ctrl_set(inner_foot_common)

        outer_foot_common = self.prefix_name + "_" + self.leg_side + "_Leg_Outer_Foot_" + str(self.val)
        outer_foot_ctrl_name = self.foot_side_ctrl_set(outer_foot_common)

        foot_side_ctrl_grp_name = self.prefix_name + "_" + self.leg_side + "_Leg_Foot_" + str(self.val) + '_Ctrl_Grp'
        cmds.select(heel_ctrl_name, inner_foot_ctrl_name, outer_foot_ctrl_name)
        cmds.group(n=foot_side_ctrl_grp_name)
        cmds.select(foot_side_ctrl_grp_name, foot_ctrl_name)
        cmds.parent()
        cmds.setAttr((heel_loc_name + '.v'), 0)
        '''
        addAttr -ln "Foot_Side_Ctrl_Vis"  -at "enum" -en "Off:On:"  |Root_Grp|Template_L_Leg_1_Grp|Template_L_Foot_1_Ctrl_Grp|Template_L_Foot_1_Ctrl;
        setAttr -e-keyable true |Root_Grp|Template_L_Leg_1_Grp|Template_L_Foot_1_Ctrl_Grp|Template_L_Foot_1_Ctrl.Foot_Side_Ctrl_Vis;
        '''
        cmds.addAttr(foot_ctrl_name, ln="Foot_Side_Ctrl_Vis", at='enum', en='Off:On')
        cmds.setAttr((foot_ctrl_name + ".Foot_Side_Ctrl_Vis"), e=True, keyable=True)
        cmds.connectAttr((foot_ctrl_name + ".Foot_Side_Ctrl_Vis"), (foot_side_ctrl_grp_name + '.v'))

    def bone_def(self):
        self.grp_list = ['Leg_Grp']
        for each_grp in self.grp_list:
            # list of the all children
            if cmds.objExists(each_grp):
                children_list = cmds.listRelatives(each_grp, children=True)
                for each_child in children_list:
                    # get all the controller data
                    self.controller_get_data(each_child)

                    self.final_bone_leg()

    def final_bone_leg(self):
        grp_namne = self.prefix_name + '_' + self.leg_side + '_Leg_' + str(self.val) + '_Bone_Grp'
        main_grp_name = 'Leg_Bone_Grp'

        list = [self.thine_common, self.shine_common, self.foot_common, self.ball_common]

        for each in list:
            ctrl_name = each + '_Outer_Ctrl'
            bone_name = each + '_Bone'
            get_pos = cmds.xform(ctrl_name, q=1, ws=1, rp=1)
            cmds.select(cl=True)
            cmds.joint(n=bone_name, p=(get_pos[0], get_pos[1], get_pos[2]))

        # Template_L_Leg_Finger_1_1_Tem_1_Outer_Ctrl
        finger_list = self.prefix_name + "_" + self.leg_side + "_Leg_Finger_*_1_Tem_" + str(self.val) + '_Outer_Ctrl'
        if cmds.objExists(finger_list):
            cmds.select(finger_list)
            sel_finger = cmds.ls(sl=True)
            a = 0
            while a < len(sel_finger):
                finger_name_list = self.prefix_name + "_" + self.leg_side + '_Leg_Finger_' + str(
                    a + 1) + '_*_Tem_' + str(self.val) + '_Outer_Ctrl'
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
                        hand_bone_jnt = self.ball_common + '_Bone'
                        cmds.parent(bone_name, hand_bone_jnt)
                    else:
                        split_name = sel_finger_new[b - 1].split('_Outer_Ctrl')[0]
                        previous_jnt = split_name + '_Bone'
                        cmds.parent(bone_name, previous_jnt)

                    b += 1
                a += 1

        thine_jnt = self.thine_common + '_Bone'
        shine_jnt = self.shine_common + '_Bone'
        foot_jnt = self.foot_common + '_Bone'
        ball_jnt = self.ball_common + '_Bone'
        cmds.parent(shine_jnt, thine_jnt)
        cmds.parent(foot_jnt, shine_jnt)
        cmds.parent(ball_jnt, foot_jnt)

        # Template_L_Leg_Butt_Tem_1_Outer_Ctrl
        butt_outer_ctrl = self.butt_common + '_Outer_Ctrl'
        if cmds.objExists(butt_outer_ctrl):
            butt_xform = cmds.xform(butt_outer_ctrl, q=1, ws=1, rp=1)
            jnt_name = self.butt_common + '_Bone'
            cmds.select(cl=True)
            cmds.joint(n=jnt_name, p=(butt_xform[0], butt_xform[1], butt_xform[2]))

            cmds.parent(jnt_name, thine_jnt)

        # put everything in one grp
        self.helper_class.grp_create(object_name=thine_jnt,
                                     grp_name=grp_namne)

        self.helper_class.grp_create(object_name=grp_namne,
                                     grp_name=main_grp_name)

    def controller_twick_def(self):
        self.grp_list = ['Leg_Grp']
        for each_grp in self.grp_list:
            # list of the all children
            if cmds.objExists(each_grp):
                children_list = cmds.listRelatives(each_grp, children=True)
                for each_child in children_list:
                    # get all the controller data
                    self.controller_get_data(each_child)

                    self.final_controller_def()

    def final_controller_def(self):
        grp_name = self.prefix_name + "_" + self.leg_side + "_Leg_" + str(self.val) + '_Outer_Ctrl' + '_Twick_Ctrl_Grp'
        main_grp_name = 'Leg_Twick_Ctrl_Grp'

        if self.leg_side == 'L':
            col = 'Blue'
        else:
            col = 'Red'

        list = [self.thine_common, self.shine_common, self.foot_common, self.ball_common]
        for each in list:
            ctrl_name = each + '_Inner_Ctrl'
            twick_ctrl = each + '_Twick_Ctrl'
            get_pos = cmds.xform(ctrl_name, q=1, ws=1, rp=1)
            self.controller_class.circle_ctrl()
            cmds.rename('circle_ctrl', twick_ctrl)
            cmds.setAttr((twick_ctrl + '.tx'), get_pos[0])
            cmds.setAttr((twick_ctrl + '.ty'), get_pos[1])
            cmds.setAttr((twick_ctrl + '.tz'), get_pos[2])

            self.helper_class.color_val(color=col,
                                        obj_name=twick_ctrl)

            self.helper_class.grp_create(object_name=twick_ctrl,
                                         grp_name=grp_name)

        finger_list = self.prefix_name + "_" + self.leg_side + "_Leg_Finger_*_1_Tem_" + str(self.val) + '_Outer_Ctrl'
        cmds.select(finger_list)
        sel_finger = cmds.ls(sl=True)
        a = 0
        while a < len(sel_finger):
            finger_name_list = self.prefix_name + "_" + self.leg_side + '_Leg_Finger_' + str(a + 1) + '_*_Tem_' + str(
                self.val) + '_Outer_Ctrl'
            cmds.select(finger_name_list)
            sel_finger_new = cmds.ls(sl=True)
            b = 0
            while b < len(sel_finger_new):
                split_name = sel_finger_new[b].split('_Outer_Ctrl')[0]
                get_pos = cmds.xform(sel_finger_new[b], q=1, ws=1, rp=1)
                twick_ctrl_name = split_name + '_Twick_Ctrl'
                self.controller_class.circle_ctrl()
                cmds.rename('circle_ctrl', twick_ctrl_name)
                cmds.setAttr((twick_ctrl_name + '.rx'), 90)

                cmds.setAttr((twick_ctrl_name + '.tx'), get_pos[0])
                cmds.setAttr((twick_ctrl_name + '.ty'), get_pos[1])
                cmds.setAttr((twick_ctrl_name + '.tz'), get_pos[2])

                self.helper_class.grp_create(object_name=twick_ctrl_name,
                                             grp_name=grp_name)

                self.helper_class.color_val(color=col,
                                            obj_name=twick_ctrl_name)

                b += 1
            a += 1

        self.helper_class.grp_create(object_name=grp_name,
                                     grp_name=main_grp_name)

    def foot_side_ctrl_set(self, loc_common):
        loc_name = loc_common + '_Loc'
        ctrl_name = loc_common + '_Ctrl'
        plus_minus_name = loc_common + '_Plus_Minus'
        heel_rpx = cmds.getAttr(loc_name + '.rotatePivotX')
        heel_rpy = cmds.getAttr(loc_name + '.rotatePivotY')
        heel_rpz = cmds.getAttr(loc_name + '.rotatePivotZ')
        self.controller_class.half_circle_ctrl()
        cmds.rename('Half_Circle', ctrl_name)
        cmds.select(ctrl_name)
        cmds.move(heel_rpx, heel_rpy, heel_rpz)
        cmds.DeleteHistory()
        cmds.FreezeTransformations()
        cmds.createNode('plusMinusAverage', n=plus_minus_name)
        mel.eval('AEnewNonNumericMultiAddNewItem("%s","input3D");' % plus_minus_name)
        mel.eval('AEnewNonNumericMultiAddNewItem("%s","input3D");' % plus_minus_name)
        cmds.setAttr((plus_minus_name + '.input3D[1].input3Dx'), heel_rpx)
        cmds.setAttr((plus_minus_name + '.input3D[1].input3Dy'), heel_rpy)
        cmds.setAttr((plus_minus_name + '.input3D[1].input3Dz'), heel_rpz)
        # connectAttr -f plusMinusAverage1.output3D Template_L_Leg_Heel_1_Loc.rotatePivot;
        cmds.connectAttr((ctrl_name + '.translate'), (plus_minus_name + '.input3D[0]'))
        cmds.connectAttr((plus_minus_name + '.output3D'), (loc_name + '.rotatePivot'))
        return ctrl_name

    def get_leg(self):
        list = []
        self.grp_list = ['Leg_Grp']
        for each_grp in self.grp_list:
            # list of the all children
            if cmds.objExists(each_grp):
                children_list = cmds.listRelatives(each_grp, children=True)
                for each_child in children_list:
                    # get all the controller data
                    list.append(each_child)
        return len(list)







