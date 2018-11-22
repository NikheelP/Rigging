class ARM:
    def __init__(self):
        self.helper_class = helper.HELPER()
        self.connection_class = connection.CONNECTION()
        self.controller_class = controller_rig.controler()
        self.arm_finger_label = {}
        self.arm_finger_line_edit = {}
        self.arm_finger_line_edit = {}
        self.finger_label_list = {}

        self.sphere_grp_list = []
        self.cluster_grp_list = []
        self.cylinder_list = []
        self.ctrl_list = []
        self.crv_list = []

    def new(self, widget, layout):
        self.widget = widget
        self.layout = layout

        self.arm_grid_layout = QtGui.QGridLayout()
        self.arm_grid_layout.setObjectName("arm_grid_layout")

        # MIRROR CHECKBOX
        self.mirror_check_box = QtGui.QCheckBox(self.widget)
        self.mirror_check_box.setObjectName("mirror_check_box")
        self.mirror_check_box.setText('Mirror')
        self.mirror_check_box.setChecked(True)
        self.mirror_check_box.stateChanged.connect(self.mirror_status_def)
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

        # CLAVICAL CHECKBOX
        self.clavical_check_box = QtGui.QCheckBox(self.widget)
        self.clavical_check_box.setObjectName("clavical_check_box")
        self.clavical_check_box.setText('Clavical')
        self.arm_grid_layout.addWidget(self.clavical_check_box, 2, 0, 1, 1)

        # SCAPULA CHECKBOX
        self.scapula_check_box = QtGui.QCheckBox(self.widget)
        self.scapula_check_box.setObjectName("scapula_check_box")
        self.scapula_check_box.setText('Scapula')
        self.arm_grid_layout.addWidget(self.scapula_check_box, 2, 1, 1, 1)

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

    def new_clear(self):
        self.helper_class.clearLayout(self.arm_grid_layout)

    def new_arm_def(self):
        # query eveything from the ui
        self.mirror_check_box_query = self.mirror_check_box.isChecked()
        self.left_hand_check_box_query = self.left_hand_check_box.isChecked()
        self.right_hand_check_box_query = self.right_hand_check_box.isChecked()
        self.clavical_check_box_query = self.clavical_check_box.isChecked()
        self.scapula_check_box_query = self.scapula_check_box.isChecked()
        self.upper_arm_roll_bone_line_edit_query = int(self.upper_arm_roll_bone_line_edit.text())
        self.lower_arm_roll_bone_line_edit_query = int(self.lower_arm_roll_bone_line_edit.text())
        self.hand_check_box_query = self.hand_check_box.isChecked()
        if self.hand_check_box_query == True:
            self.no_finger_line_edit_query = int(self.no_finger_line_edit.text())

        if self.left_hand_check_box_query == True:
            self.left_hand_def()
        if self.right_hand_check_box_query == True:
            self.right_hand_def()

    def left_hand_def(self):
        self.sphere_grp_list = []
        self.cluster_grp_list = []
        self.cylinder_list = []
        self.ctrl_list = []
        self.crv_list = []
        # Chck if left val
        if cmds.objExists("*_L_Arm_Tem_*_Main_Grp"):
            cmds.select("*_L_Arm_Tem_*_Main_Grp")
            sel_main_grp = cmds.ls(sl=True)
            len_sel_main_grp = len(sel_main_grp)
            self.val = len_sel_main_grp + 1
        else:
            self.val = 1

        self.arm_side = 'L'
        self.prefix_name = 'Template'
        self.base_ctrl_color = 'Blue'
        self.base_pos = [0, 0, 0]
        self.shoulder_pos = [11, 6, 0]
        self.upper_hand_pos = [16, 3, 0]
        self.lbow_pos = [35, 1, -3]
        self.hand_pos = [54, 1, 0]
        self.hand_end_pos = [73, 0, 0]
        self.double_wrist_pos = [57, 1, 0]
        self.double_lbow_side_1_pos = [32, 1, -3]
        self.double_lbow_side_2_pos = [38, 1, -3]
        self.finger_default_pos = [54.0, 0, 0]

        # create sphere
        self.arm_sphere_def()
        # create a cylinder
        self.arm_cylinder_def()

        # create a  controller
        self.controller_def()

        # create hand
        if self.hand_check_box_query == True:
            self.finger_def()

        # create a final group
        self.final_parent()
        self.final_group()

    def right_hand_def(self):
        self.sphere_grp_list = []
        self.cluster_grp_list = []
        self.cylinder_list = []
        self.ctrl_list = []
        self.crv_list = []
        # Chck if left val
        if cmds.objExists("*_R_Arm_Tem_*_Main_Grp"):
            cmds.select("*_R_Arm_Tem_*_Main_Grp")
            sel_main_grp = cmds.ls(sl=True)
            len_sel_main_grp = len(sel_main_grp)
            self.val = len_sel_main_grp + 1
        else:
            self.val = 1

        self.arm_side = 'R'
        self.prefix_name = 'Template'
        self.base_ctrl_color = 'Red'
        self.base_pos = [0, 0, 0]
        self.shoulder_pos = [-11, 6, 0]
        self.upper_hand_pos = [-16, 3, 0]
        self.lbow_pos = [-35, 1, -3]
        self.hand_pos = [-54, 1, 0]
        self.hand_end_pos = [-73, 0, 0]
        self.double_wrist_pos = [-57, 1, 0]
        self.double_lbow_side_1_pos = [-32, 1, -3]
        self.double_lbow_side_2_pos = [-38, 1, -3]
        self.finger_default_pos = [-54.0, 0, 0]
        self.ctrl_list = []

        # create sphere
        self.arm_sphere_def()

        # create a cylinder
        self.arm_cylinder_def()

        # create a  controller
        self.controller_def()

        # create hand
        if self.hand_check_box_query == True:
            self.finger_def()

        # create a final group
        self.final_parent()
        self.final_group()

        if self.mirror_check_box_query == True:
            self.mirror_value()

    def arm_sphere_def(self):
        # create a sphere on each position

        # Base
        self.base_common = self.prefix_name + "_" + self.arm_side + "_Arm_Base_Tem_" + str(self.val)
        self.base_sphere_name = self.base_common + "_Geo"
        self.base_sphere_clu_name = self.base_common + '_Clu'
        self.base_sphere_clu_handle_name = self.base_sphere_clu_name + 'Handle'
        self.sphere_grp_list.append(self.base_sphere_name)
        self.cluster_grp_list.append(self.base_sphere_clu_handle_name)
        self.helper_class.set_sphere_position(self.base_sphere_name, self.base_pos, self.base_sphere_clu_name)

        # SHOULDER
        self.shoulder_common = self.prefix_name + "_" + self.arm_side + "_Arm_Shoulder_Tem_" + str(self.val)
        self.shoulder_sphere_name = self.shoulder_common + "_Geo"
        self.shoulder_sphere_clu_name = self.shoulder_common + '_Clu'
        self.shoulder_sphere_clu_handle_name = self.shoulder_sphere_clu_name + 'Handle'
        self.sphere_grp_list.append(self.shoulder_sphere_name)
        self.cluster_grp_list.append(self.shoulder_sphere_clu_handle_name)
        self.helper_class.set_sphere_position(self.shoulder_sphere_name, self.shoulder_pos,
                                              self.shoulder_sphere_clu_name)

        # UPPPER HAND
        self.upper_hand_common = self.prefix_name + "_" + self.arm_side + "_Arm_Upper_Hand_Tem_" + str(self.val)
        self.upper_hand_sphere_name = self.upper_hand_common + "_Geo"
        self.upper_hand_sphere_clu_name = self.upper_hand_common + '_Clu'
        self.upper_hand_sphere_clu_handle_name = self.upper_hand_sphere_clu_name + 'Handle'
        self.sphere_grp_list.append(self.upper_hand_sphere_name)
        self.cluster_grp_list.append(self.upper_hand_sphere_clu_handle_name)
        self.helper_class.set_sphere_position(self.upper_hand_sphere_name, self.upper_hand_pos,
                                              self.upper_hand_sphere_clu_name)

        # LBOW
        self.lbow_common = self.prefix_name + "_" + self.arm_side + "_Arm_lBow_Tem_" + str(self.val)
        self.lbow_sphere_name = self.lbow_common + "_Geo"
        self.lbow_sphere_clu_name = self.lbow_common + '_Clu'
        self.lbow_sphere_clu_handle_name = self.lbow_sphere_clu_name + 'Handle'
        self.sphere_grp_list.append(self.lbow_sphere_name)
        self.cluster_grp_list.append(self.lbow_sphere_clu_handle_name)
        self.helper_class.set_sphere_position(self.lbow_sphere_name,
                                              self.lbow_pos,
                                              self.lbow_sphere_clu_name)

        # HAND
        self.hand_common = self.prefix_name + "_" + self.arm_side + "_Arm_Hand_Tem_" + str(self.val)
        self.hand_sphere_name = self.hand_common + "_Geo"
        self.hand_sphere_clu_name = self.hand_common + '_Clu'
        self.hand_sphere_clu_handle_name = self.hand_sphere_clu_name + 'Handle'
        self.sphere_grp_list.append(self.hand_sphere_name)
        self.cluster_grp_list.append(self.hand_sphere_clu_handle_name)
        self.helper_class.set_sphere_position(self.hand_sphere_name,
                                              self.hand_pos,
                                              self.hand_sphere_clu_name)

        # HAND END
        self.hand_end_common = self.prefix_name + "_" + self.arm_side + "_Arm_Hand_End_Tem_" + str(self.val)
        self.hand_end_sphere_name = self.hand_end_common + "_Geo"
        self.hand_end_sphere_clu_name = self.hand_end_common + '_Clu'
        self.hand_end_sphere_clu_handle_name = self.hand_end_sphere_clu_name + 'Handle'
        self.sphere_grp_list.append(self.hand_end_sphere_name)
        self.cluster_grp_list.append(self.hand_end_sphere_clu_handle_name)
        self.helper_class.set_sphere_position(self.hand_end_sphere_name,
                                              self.hand_end_pos,
                                              self.hand_end_sphere_clu_name)

    def arm_cylinder_def(self):
        # SET THE CYLINDER

        # BASE TO SHOULDER CYLINDER
        self.base_to_shoulder_common = self.prefix_name + "_" + self.arm_side + "_Hand_Base_to_Shoulder_Tem_" + str(
            self.val)
        self.base_to_shoulder_cylinder_name = self.base_to_shoulder_common + '_Geo'
        self.base_to_shoulder_lower_cylinder_cluster_name = self.prefix_name + "_" + self.arm_side + "_Hand_Base_to_Shoulder_Lower_Tem_" + str(
            self.val) + '_Clu'
        self.base_to_shoulder_lower_cylinder_cluster_handle_name = self.base_to_shoulder_lower_cylinder_cluster_name + 'Handle'
        self.base_to_shoulder_upper_cylinder_cluster_name = self.prefix_name + "_" + self.arm_side + "_Hand_Base_to_Shoulder_Upper_Tem_" + str(
            self.val) + '_Clu'
        self.base_to_shoulder_upper_cylinder_cluster_handle_name = self.base_to_shoulder_upper_cylinder_cluster_name + 'Handle'
        self.cylinder_rotate = [0, 0, 90]
        self.cluster_grp_list.append(self.base_to_shoulder_lower_cylinder_cluster_handle_name)
        self.cluster_grp_list.append(self.base_to_shoulder_upper_cylinder_cluster_handle_name)
        self.cylinder_list.append(self.base_to_shoulder_cylinder_name)
        self.helper_class.set_cylinder_position(self.base_to_shoulder_cylinder_name,
                                                self.base_to_shoulder_lower_cylinder_cluster_name,
                                                self.base_to_shoulder_upper_cylinder_cluster_name,
                                                self.shoulder_sphere_name,
                                                self.base_sphere_name,
                                                rotate_val=[self.cylinder_rotate[0],
                                                            self.cylinder_rotate[1],
                                                            self.cylinder_rotate[2]])

        # SHOULDER TO UPPER HAND CYLINDER
        self.shouler_to_upper_hand_common = self.prefix_name + "_" + self.arm_side + "_Hand_Shoulder_to_upper_hand_Tem_" + str(
            self.val)
        self.shouler_to_upper_hand_cylinder_name = self.shouler_to_upper_hand_common + '_Geo'
        self.shouler_to_upper_hand_lower_cylinder_cluster_name = self.prefix_name + "_" + self.arm_side + "_Hand_Shoulder_to_upper_hand_Lower_Tem_" + str(
            self.val) + '_Clu'
        self.shouler_to_upper_hand_lower_cylinder_cluster_handle_name = self.shouler_to_upper_hand_lower_cylinder_cluster_name + 'Handle'
        self.shouler_to_upper_hand_upper_cylinder_cluster_name = self.prefix_name + "_" + self.arm_side + "_Hand_Shoulder_to_upper_hand_Upper_Tem_" + str(
            self.val) + '_Clu'
        self.shouler_to_upper_hand_upper_cylinder_cluster_handle_name = self.shouler_to_upper_hand_upper_cylinder_cluster_name + 'Handle'
        self.cylinder_rotate = [0, 0, 90]
        self.cluster_grp_list.append(self.shouler_to_upper_hand_lower_cylinder_cluster_handle_name)
        self.cluster_grp_list.append(self.shouler_to_upper_hand_upper_cylinder_cluster_handle_name)
        self.cylinder_list.append(self.shouler_to_upper_hand_cylinder_name)
        self.helper_class.set_cylinder_position(self.shouler_to_upper_hand_cylinder_name,
                                                self.shouler_to_upper_hand_lower_cylinder_cluster_name,
                                                self.shouler_to_upper_hand_upper_cylinder_cluster_name,
                                                self.upper_hand_sphere_name,
                                                self.shoulder_sphere_name,
                                                rotate_val=[self.cylinder_rotate[0],
                                                            self.cylinder_rotate[1],
                                                            self.cylinder_rotate[2]])

        self.upper_hand_to_lbow_hand_common = self.prefix_name + "_" + self.arm_side + "_Hand_upper_hand_to_lbow_Tem_" + str(
            self.val)
        self.upper_hand_to_lbow_hand_cylinder_name = self.upper_hand_to_lbow_hand_common + '_Geo'
        self.upper_hand_to_lbow_hand_lower_cylinder_cluster_name = self.prefix_name + "_" + self.arm_side + "_Hand_upper_hand_to_lbow_Lower_Tem_" + str(
            self.val) + '_Clu'
        self.upper_hand_to_lbow_hand_lower_cylinder_cluster_handle_name = self.upper_hand_to_lbow_hand_lower_cylinder_cluster_name + 'Handle'
        self.upper_hand_to_lbow_hand_upper_cylinder_cluster_name = self.prefix_name + "_" + self.arm_side + "_Hand_upper_hand_to_lbow_Upper_Tem_" + str(
            self.val) + '_Clu'
        self.upper_hand_to_lbow_hand_upper_cylinder_cluster_handle_name = self.upper_hand_to_lbow_hand_upper_cylinder_cluster_name + 'Handle'
        self.cylinder_rotate = [0, 0, 90]
        self.cluster_grp_list.append(self.upper_hand_to_lbow_hand_lower_cylinder_cluster_handle_name)
        self.cluster_grp_list.append(self.upper_hand_to_lbow_hand_upper_cylinder_cluster_handle_name)
        self.cylinder_list.append(self.upper_hand_to_lbow_hand_cylinder_name)
        self.helper_class.set_cylinder_position(self.upper_hand_to_lbow_hand_cylinder_name,
                                                self.upper_hand_to_lbow_hand_lower_cylinder_cluster_name,
                                                self.upper_hand_to_lbow_hand_upper_cylinder_cluster_name,
                                                self.lbow_sphere_name,
                                                self.upper_hand_sphere_name,
                                                rotate_val=[self.cylinder_rotate[0],
                                                            self.cylinder_rotate[1],
                                                            self.cylinder_rotate[2]])

        self.lbow_to_hand_hand_common = self.prefix_name + "_" + self.arm_side + "_Hand_lbow_to_Hand_Tem_" + str(
            self.val)
        self.lbow_to_hand_hand_cylinder_name = self.lbow_to_hand_hand_common + '_Geo'
        self.lbow_to_hand_hand_lower_cylinder_cluster_name = self.prefix_name + "_" + self.arm_side + "_Hand_lbow_to_hand_Lower_Tem_" + str(
            self.val) + '_Clu'
        self.lbow_to_hand_hand_lower_cylinder_cluster_handle_name = self.lbow_to_hand_hand_lower_cylinder_cluster_name + 'Handle'
        self.lbow_to_hand_hand_upper_cylinder_cluster_name = self.prefix_name + "_" + self.arm_side + "_Hand_lbow_to_hand_Upper_Tem_" + str(
            self.val) + '_Clu'
        self.lbow_to_hand_hand_upper_cylinder_cluster_handle_name = self.lbow_to_hand_hand_upper_cylinder_cluster_name + 'Handle'
        self.cylinder_rotate = [0, 0, 90]
        self.cluster_grp_list.append(self.lbow_to_hand_hand_lower_cylinder_cluster_handle_name)
        self.cluster_grp_list.append(self.lbow_to_hand_hand_upper_cylinder_cluster_handle_name)
        self.cylinder_list.append(self.lbow_to_hand_hand_cylinder_name)
        self.helper_class.set_cylinder_position(self.lbow_to_hand_hand_cylinder_name,
                                                self.lbow_to_hand_hand_lower_cylinder_cluster_name,
                                                self.lbow_to_hand_hand_upper_cylinder_cluster_name,
                                                self.hand_sphere_name,
                                                self.lbow_sphere_name,
                                                rotate_val=[self.cylinder_rotate[0],
                                                            self.cylinder_rotate[1],
                                                            self.cylinder_rotate[2]])

        # hand to hand end
        self.hand_to_hand_end_hand_common = self.prefix_name + "_" + self.arm_side + "_Hand_Hand_to_Hand_End_Tem_" + str(
            self.val)
        self.hand_to_hand_end_hand_cylinder_name = self.hand_to_hand_end_hand_common + '_Geo'
        self.hand_to_hand_end_hand_lower_cylinder_cluster_name = self.prefix_name + "_" + self.arm_side + "_Hand_Hand_to_Hand_End_Lower_Tem_" + str(
            self.val) + '_Clu'
        self.hand_to_hand_end_hand_lower_cylinder_cluster_handle_name = self.hand_to_hand_end_hand_lower_cylinder_cluster_name + 'Handle'
        self.hand_to_hand_end_hand_upper_cylinder_cluster_name = self.prefix_name + "_" + self.arm_side + "_Hand_Hand_to_Hand_End_Upper_Tem_" + str(
            self.val) + '_Clu'
        self.hand_to_hand_end_hand_upper_cylinder_cluster_handle_name = self.hand_to_hand_end_hand_upper_cylinder_cluster_name + 'Handle'
        self.cylinder_rotate = [0, 0, 90]
        self.cluster_grp_list.append(self.hand_to_hand_end_hand_lower_cylinder_cluster_handle_name)
        self.cluster_grp_list.append(self.hand_to_hand_end_hand_upper_cylinder_cluster_handle_name)
        self.cylinder_list.append(self.hand_to_hand_end_hand_cylinder_name)
        self.helper_class.set_cylinder_position(self.hand_to_hand_end_hand_cylinder_name,
                                                self.hand_to_hand_end_hand_lower_cylinder_cluster_name,
                                                self.hand_to_hand_end_hand_upper_cylinder_cluster_name,
                                                self.hand_end_sphere_name,
                                                self.hand_sphere_name,
                                                rotate_val=[self.cylinder_rotate[0],
                                                            self.cylinder_rotate[1],
                                                            self.cylinder_rotate[2]])

    def controller_def(self):
        # CREATE CONTROLLER
        self.ctrl_lower_size = [0.5, 0.5, 0.5]
        self.ctrl_outer_size = [1.5, 1.5, 1.5]
        self.ctrl_rotate = [0, 0, 90]
        self.base_ctrl_freez_trans = True
        self.base_ctrl_freez_rotate = True
        self.base_ctrl_freez_scale = True

        # BASE CONTROLLER
        self.base_parent_const_list = [self.base_sphere_clu_handle_name,
                                       self.base_to_shoulder_upper_cylinder_cluster_handle_name]
        self.controller_small_big(base_name=self.base_common,
                                  parent_list=self.base_parent_const_list,
                                  pos=self.base_pos)
        self.arm_base_inner_ctrl = self.base_common + '_Inner_Ctrl'
        self.arm_base_outer_ctrl = self.base_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.arm_base_inner_ctrl)
        self.ctrl_list.append(self.arm_base_outer_ctrl)

        # SHOULDER CONTROLLER
        self.base_parent_const_list = [self.shoulder_sphere_clu_handle_name,
                                       self.base_to_shoulder_lower_cylinder_cluster_handle_name,
                                       self.shouler_to_upper_hand_upper_cylinder_cluster_handle_name]
        self.controller_small_big(base_name=self.shoulder_common,
                                  parent_list=self.base_parent_const_list,
                                  pos=self.shoulder_pos)
        self.arm_shoulder_inner_ctrl = self.shoulder_common + '_Inner_Ctrl'
        self.arm_shoulder_outer_ctrl = self.shoulder_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.arm_shoulder_inner_ctrl)
        self.ctrl_list.append(self.arm_shoulder_outer_ctrl)

        # UPPER ARM
        self.base_parent_const_list = [self.upper_hand_sphere_clu_handle_name,
                                       self.shouler_to_upper_hand_lower_cylinder_cluster_handle_name,
                                       self.upper_hand_to_lbow_hand_upper_cylinder_cluster_handle_name]
        self.controller_small_big(base_name=self.upper_hand_common,
                                  parent_list=self.base_parent_const_list,
                                  pos=self.upper_hand_pos)
        self.arm_upper_hand_inner_ctrl = self.upper_hand_common + '_Inner_Ctrl'
        self.arm_upper_hand_outer_ctrl = self.upper_hand_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.arm_upper_hand_inner_ctrl)
        self.ctrl_list.append(self.arm_upper_hand_outer_ctrl)

        # LBOW
        self.base_parent_const_list = [self.lbow_sphere_clu_handle_name,
                                       self.upper_hand_to_lbow_hand_lower_cylinder_cluster_handle_name,
                                       self.lbow_to_hand_hand_upper_cylinder_cluster_handle_name]
        self.controller_small_big(base_name=self.lbow_common,
                                  parent_list=self.base_parent_const_list,
                                  pos=self.lbow_pos)
        self.arm_lbow_inner_ctrl = self.lbow_common + '_Inner_Ctrl'
        self.arm_lbow_outer_ctrl = self.lbow_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.arm_lbow_inner_ctrl)
        self.ctrl_list.append(self.arm_lbow_outer_ctrl)

        # HAND
        self.base_parent_const_list = [self.hand_sphere_clu_handle_name,
                                       self.lbow_to_hand_hand_lower_cylinder_cluster_handle_name,
                                       self.hand_to_hand_end_hand_upper_cylinder_cluster_handle_name]
        self.controller_small_big(base_name=self.hand_common,
                                  parent_list=self.base_parent_const_list,
                                  pos=self.hand_pos)
        self.arm_hand_inner_ctrl = self.hand_common + '_Inner_Ctrl'
        self.arm_hand_outer_ctrl = self.hand_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.arm_hand_inner_ctrl)
        self.ctrl_list.append(self.arm_hand_outer_ctrl)

        # HAND END
        self.base_parent_const_list = [self.hand_end_sphere_clu_handle_name,
                                       self.hand_to_hand_end_hand_lower_cylinder_cluster_handle_name]
        self.controller_small_big(base_name=self.hand_end_common,
                                  parent_list=self.base_parent_const_list,
                                  pos=self.hand_end_pos)
        self.arm_hand_end_inner_ctrl = self.hand_end_common + '_Inner_Ctrl'
        self.arm_hand_end_outer_ctrl = self.hand_end_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.arm_hand_end_inner_ctrl)
        self.ctrl_list.append(self.arm_hand_end_outer_ctrl)

        # roll bone
        self.roll_bone('Upper',
                       self.arm_upper_hand_inner_ctrl,
                       self.arm_lbow_inner_ctrl,
                       self.upper_arm_roll_bone_line_edit_query)
        self.roll_bone('Lower',
                       self.arm_lbow_inner_ctrl,
                       self.arm_hand_inner_ctrl,
                       self.lower_arm_roll_bone_line_edit_query)

    def controller_small_big(self, base_name, parent_list, pos):
        self.ctrl_lower_size = [0.5, 0.5, 0.5]
        self.ctrl_outer_size = [0.8, 0.8, 0.8]
        self.ctrl_rotate = [0, 0, 90]
        self.base_ctrl_freez_trans = True
        self.base_ctrl_freez_rotate = True
        self.base_ctrl_freez_scale = True

        # SMALL CONTROLLER
        self.base_inner_ctrl = base_name + '_Inner_Ctrl'
        self.base_ctrl_size_ctrl = self.ctrl_lower_size
        self.base_ctrl_roate = self.ctrl_rotate
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

    def finger_def(self):
        # get the rotation value
        get_attr = cmds.getAttr(self.arm_hand_outer_ctrl + '.r')[0]
        cmds.setAttr((self.arm_hand_outer_ctrl + '.rx'), 0)
        cmds.setAttr((self.arm_hand_outer_ctrl + '.ry'), 0)
        cmds.setAttr((self.arm_hand_outer_ctrl + '.rz'), 0)

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
        self.locator_grp_name = 'Finger_first_Grp'
        cmds.select('Finger_*_Loc')
        cmds.group(n=self.locator_grp_name)
        cmds.select(self.locator_grp_name)
        cmds.CenterPivot()
        cmds.move(0, 0, 0, rpr=True)
        cmds.FreezeTransformations()
        if self.arm_side == 'L':
            x_val_new = self.finger_default_pos[0] + 7
        else:
            x_val_new = self.finger_default_pos[0] - 7

        cmds.move(x_val_new,
                  self.finger_default_pos[1],
                  self.finger_default_pos[2])
        cmds.setAttr((self.locator_grp_name + '.rotateY'), 90)

        # new_grp
        self.locator_new_grp_name = 'Finger_Grp'
        cmds.select(self.locator_grp_name)
        cmds.group(n=self.locator_new_grp_name)
        cmds.select(self.locator_new_grp_name)
        cmds.CenterPivot()
        # get hand xform
        hand_xform = cmds.xform(self.arm_hand_outer_ctrl, q=1, ws=1, rp=1)
        # move -rpr 61 -0.293893 1.095491 Finger_Grp.scalePivot Finger_Grp.rotatePivot ;
        cmds.move(hand_xform[0],
                  hand_xform[1],
                  hand_xform[2],
                  (self.locator_new_grp_name + '.scalePivot'),
                  (self.locator_new_grp_name + '.rotatePivot'))
        cmds.orientConstraint(self.arm_hand_outer_ctrl, self.locator_new_grp_name, mo=False)

        a = 0
        while a < self.no_finger_line_edit_query:
            loc_name = 'Finger_' + str(a) + '_Loc'
            self.finger_query = int(self.arm_finger_line_edit[a].text())
            b = 0
            x_value = 0
            while b < self.finger_query:
                cmds.select(loc_name)
                cmds.Duplicate()
                sel_new_loc = cmds.ls(sl=True)[0]
                new_loc_name = 'Finger_' + str(a) + '_' + str(b) + '_Loc'
                cmds.rename(sel_new_loc, new_loc_name)
                cmds.select(new_loc_name)
                cmds.setAttr((new_loc_name + '.tz'), x_value)

                if self.arm_side == 'L':
                    x_value += 3
                else:
                    x_value -= 3
                b += 1
            a += 1

        # now get each positiona dn create a finger
        a = 0
        while a < self.no_finger_line_edit_query:
            self.finger_query = int(self.arm_finger_line_edit[a].text())
            self.finger_indi_def(finger_query=self.finger_query,
                                 value=a)
            a+=1

        a = 0
        while a < self.no_finger_line_edit_query:
            self.loc_position = cmds.xform(self.locator_list[a], q=1, ws=1, rp=1)
            self.finger_query = int(self.arm_finger_line_edit[a].text())
            self.finger_indi_parent_def(finger_query=self.finger_query,
                                        value=a)
            a+=1

        cmds.select(self.locator_new_grp_name)
        cmds.delete()

        cmds.setAttr((self.arm_hand_outer_ctrl + '.rx'), get_attr[0])
        cmds.setAttr((self.arm_hand_outer_ctrl + '.ry'), get_attr[1])
        cmds.setAttr((self.arm_hand_outer_ctrl + '.rz'), get_attr[2])

    def finger_indi_def(self, finger_query, value):
        b = 0
        while b < finger_query:
            self.cylinder_rotate = [0, 0, -90]
            self.finger_common = self.prefix_name + "_" + self.arm_side + "_Arm_Finger_" + str(value + 1) + '_' + str(
                b + 1) + "_Tem_" + str(self.val)
            self.finger_sphere_name = self.finger_common + "_Geo"
            self.finger_sphere_clu_name = self.finger_common + '_Clu'
            self.finger_sphere_clu_handle_name = self.finger_sphere_clu_name + 'Handle'
            # self.finger_default_pos = [61.0,0,]
            # Finger_0_0_Loc
            loc_name = 'Finger_' + str(value) + '_' + str(b) + '_Loc'

            self.finger_pos = cmds.xform(loc_name, q=1, ws=1, rp=1)

            self.sphere_grp_list.append(self.finger_sphere_name)
            self.cluster_grp_list.append(self.finger_sphere_clu_handle_name)
            self.helper_class.set_sphere_position(self.finger_sphere_name,
                                                  self.finger_pos,
                                                  self.finger_sphere_clu_name)

            if b == 0:
                self.cylinder_name = self.prefix_name + '_' + self.arm_side + "_Arm_Finger_Hand_to_" + str(
                    value + 1) + "_" + str(b + 1) + "_Tem_" + str(self.val) + "_Cylinder_Geo"
                self.cylinder_upper_cluster_name = self.prefix_name + '_' + self.arm_side + "_Arm_Finger_Hand_to_Upper_" + str(
                    value + 1) + "_" + str(b + 1) + "_Tem_" + str(self.val) + "_Clu"
                self.finger_to_hand_cylinder_upper_cluster_handle_name = self.cylinder_upper_cluster_name + 'Handle'
                self.cylinder_lower_cluster_name = self.prefix_name + '_' + self.arm_side + "_Arm_Finger_Hand_to_Lower_" + str(
                    value + 1) + "_" + str(b + 1) + "_Tem_" + str(self.val) + "_Clu"
                self.cylinder_lower_cluster_handle_name = self.cylinder_lower_cluster_name + 'Handle'
                self.helper_class.set_cylinder_position(self.cylinder_name,
                                                        self.cylinder_lower_cluster_name,
                                                        self.cylinder_upper_cluster_name,
                                                        self.hand_sphere_name,
                                                        self.finger_sphere_name,
                                                        rotate_val=self.cylinder_rotate)
                self.cluster_grp_list.append(self.finger_to_hand_cylinder_upper_cluster_handle_name)
                self.cluster_grp_list.append(self.cylinder_lower_cluster_handle_name)
                self.cylinder_list.append(self.cylinder_name)

            if b+1 != 1:
                self.cylinder_name = self.prefix_name + '_' + self.arm_side + "_Arm_Finger_" + str(
                    value + 1) + "_" + str(b + 1) + "_Tem_" + str(self.val) + "_Cylinder_Geo"
                self.cylinder_upper_cluster_name = self.prefix_name + '_' + self.arm_side + "_Arm_Finger_Upper_" + str(
                    value + 1) + "_" + str(b + 1) + "_Tem_" + str(self.val) + "_Clu"
                self.cylinder_upper_cluster_handle_name = self.cylinder_upper_cluster_name + 'Handle'
                self.cylinder_lower_cluster_name = self.prefix_name + '_' + self.arm_side + "_Arm_Finger_Lower_" + str(
                    value + 1) + "_" + str(b + 1) + "_Tem_" + str(self.val) + "_Clu"
                self.cylinder_lower_cluster_handle_name = self.cylinder_lower_cluster_name + 'Handle'
                self.current_sphere_name = self.prefix_name + '_' + self.arm_side + "_Arm_Finger_" + str(
                    value + 1) + "_" + str(b) + "_Tem_" + str(self.val) + "_Geo"
                self.helper_class.set_cylinder_position(self.cylinder_name,
                                                        self.cylinder_lower_cluster_name,
                                                        self.cylinder_upper_cluster_name,
                                                        self.current_sphere_name,
                                                        self.finger_sphere_name,
                                                        rotate_val=self.cylinder_rotate)
                self.cluster_grp_list.append(self.cylinder_upper_cluster_handle_name)
                self.cluster_grp_list.append(self.cylinder_lower_cluster_handle_name)
                self.cylinder_list.append(self.cylinder_name)

                # create a controller and snap
                previous_upper_cluster_handle_name = self.prefix_name + "_" + self.arm_side + "_Arm_Finger_Upper_" + str(
                    value + 1) + '_' + str(b + 1) + "_Tem_" + str(self.val) + '_CluHandle'
                next_lower_cluster_handle_name = self.prefix_name + "_" + self.arm_side + "_Arm_Finger_Lower_" + str(
                    value + 1) + '_' + str(b + 2) + "_Tem_" + str(self.val) + '_CluHandle'
                self.base_parent_const_list = [self.finger_sphere_clu_handle_name,
                                               previous_upper_cluster_handle_name]
                self.controller_small_big(base_name=self.finger_common,
                                          parent_list=self.base_parent_const_list,
                                          pos=self.finger_pos)
                self.arm_shoulder_inner_ctrl = self.finger_common + '_Inner_Ctrl'
                self.arm_shoulder_outer_ctrl = self.finger_common + '_Outer_Ctrl'
                self.ctrl_list.append(self.arm_shoulder_inner_ctrl)
                self.ctrl_list.append(self.arm_shoulder_outer_ctrl)
            b+=1

    def finger_indi_parent_def(self, finger_query, value):
        b = 0
        while b < finger_query:
            self.finger_common = self.prefix_name + "_" + self.arm_side + "_Arm_Finger_" + str(value + 1) + '_' + str(
                b + 1) + "_Tem_" + str(self.val)
            self.finger_sphere_name = self.finger_common + "_Geo"
            self.finger_sphere_clu_name = self.finger_common + '_Clu'
            self.finger_sphere_clu_handle_name = self.finger_sphere_clu_name + 'Handle'
            loc_name = 'Finger_' + str(value) + '_' + str(b) + '_Loc'

            self.finger_pos = cmds.xform(loc_name, q=1, ws=1, rp=1)
            if b==0:
                # create a controller and snap
                previous_upper_cluster_handle_name = self.prefix_name + "_" + self.arm_side + "_Arm_Finger_Hand_to_Upper_" + str(
                    value + 1) + '_' + str(b + 1) + "_Tem_" + str(self.val) + '_CluHandle'
                previous_lower_cluster_handle_name = self.prefix_name + "_" + self.arm_side + "_Arm_Finger_Hand_to_Lower_" + str(
                    value + 1) + '_' + str(b + 1) + "_Tem_" + str(self.val) + '_CluHandle'
                next_lower = self.prefix_name + "_" + self.arm_side + "_Arm_Finger_Lower_" + str(value + 1) + '_' + str(
                    b + 2) + "_Tem_" + str(self.val) + '_CluHandle'
                self.base_parent_const_list = [self.finger_sphere_clu_handle_name,
                                               previous_upper_cluster_handle_name,
                                               next_lower]
                self.controller_small_big(base_name=self.finger_common,
                                          parent_list=self.base_parent_const_list,
                                          pos=self.finger_pos)
                self.arm_shoulder_inner_ctrl = self.finger_common + '_Inner_Ctrl'
                self.first_finger_outer = self.finger_common + '_Outer_Ctrl'
                self.ctrl_list.append(self.arm_shoulder_inner_ctrl)
                self.ctrl_list.append(self.first_finger_outer)

                cmds.parentConstraint(self.arm_hand_inner_ctrl, previous_lower_cluster_handle_name, mo=False)

                # parent hand controller to the finger each one controller
                cmds.select(self.first_finger_outer, self.arm_hand_outer_ctrl)
                cmds.parent()

            self.arm_shoulder_inner_ctrl = self.finger_common + '_Inner_Ctrl'
            self.arm_shoulder_outer_ctrl = self.finger_common + '_Outer_Ctrl'
            next_cluster_lower_cluster_handle_name = self.prefix_name + '_' + self.arm_side + "_Arm_Finger_Lower_" + str(
                value + 1) + "_" + str(b + 2) + "_Tem_" + str(self.val) + "_CluHandle"
            next_ctrl_outer_name = self.prefix_name + "_" + self.arm_side + "_Arm_Finger_" + str(value + 1) + '_' + str(
                b + 2) + "_Tem_" + str(self.val) + '_Outer_Ctrl'
            if cmds.objExists(next_ctrl_outer_name):
                cmds.select(next_ctrl_outer_name, self.arm_shoulder_outer_ctrl)
                cmds.parent()
                cmds.parentConstraint(self.arm_shoulder_inner_ctrl, next_cluster_lower_cluster_handle_name, mo=False)
            b+=1

    def roll_bone(self, type, upper_object, lower_object, no_of_bone):
        # create a curve
        self.curve_common = self.prefix_name + "_" + self.arm_side + "_Arm_" + type + "_Tem_" + str(self.val)
        self.curve_name = self.curve_common + '_Crv'
        self.curve_shape_name = self.curve_name + 'Shape'
        self.curve_0_clu_name = self.prefix_name + "_" + self.arm_side + "_Arm_" + type + "_0_Tem_" + str(
            self.val) + '_Clu'
        self.curve_0_clu_handle_name = self.curve_0_clu_name + 'Handle'
        self.curve_1_clu_name = self.prefix_name + "_" + self.arm_side + "_Arm_" + type + "_1_Tem_" + str(
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
        self.cluster_grp_list.append(self.curve_0_clu_handle_name)
        self.cluster_grp_list.append(self.curve_1_clu_handle_name)

        # create a point on curve
        a = 0
        toal_minus = 0
        value = 1.0 - toal_minus
        average_val = value / (no_of_bone + 1.0)
        start_val = average_val
        while a < no_of_bone:
            common_name = self.prefix_name + "_" + self.arm_side + "_Arm_" + type + "_" + str(a) + "_Tem_" + str(
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
            self.sphere_grp_list.append(self.sphere_name)

            cmds.setAttr((self.poc_name + '.parameter'), start_val)
            start_val += average_val

            # setAttr "Template_L_Arm_Lower_0_Tem_1_POC.parameter" 0.2;
            a += 1

    def final_parent(self):
        # now do parenting inddvidual
        cmds.select(self.arm_hand_end_outer_ctrl, self.arm_hand_outer_ctrl)
        cmds.parent()

        cmds.select(self.arm_hand_outer_ctrl, self.arm_lbow_outer_ctrl)
        cmds.parent()
        cmds.select(self.arm_lbow_outer_ctrl, self.arm_upper_hand_outer_ctrl)
        cmds.parent()
        self.arm_shoulder_outer_ctrl = self.prefix_name + '_' + self.arm_side + "_Arm_Shoulder_Tem_" + str(
            self.val) + "_Outer_Ctrl"
        cmds.select(self.arm_upper_hand_outer_ctrl, self.arm_shoulder_outer_ctrl)
        cmds.parent()
        cmds.select(self.arm_shoulder_outer_ctrl, self.arm_base_outer_ctrl)
        cmds.parent()

    def final_group(self):

        self.sphere_group_name = self.prefix_name + '_' + self.arm_side + "_Arm_Tem_" + str(self.val) + "_Sphere_Grp"
        cmds.select(cl=True)
        for each in self.sphere_grp_list:
            self.helper_class.parent_child_grp(parent=self.sphere_group_name,
                                               child=each)
        self.cluster_group_name = self.prefix_name + '_' + self.arm_side + "_Arm_Tem_" + str(self.val) + "_Cluster_Grp"
        cmds.select(cl=True)
        for each in self.cluster_grp_list:
            self.helper_class.parent_child_grp(parent=self.cluster_group_name,
                                               child=each,
                                               vis=True)
        self.curve_group_name = self.prefix_name + '_' + self.arm_side + "_Arm_Tem_" + str(self.val) + "_Crv_Grp"
        cmds.select(cl=True)
        for each in self.crv_list:
            self.helper_class.parent_child_grp(parent=self.curve_group_name,
                                               child=each,
                                               vis=True)

        self.cylinder_group_name = self.prefix_name + '_' + self.arm_side + "_Arm_Tem_" + str(
            self.val) + "_Cylinder_Grp"
        cmds.select(cl=True)
        for each in self.cylinder_list:
            self.helper_class.parent_child_grp(parent=self.cylinder_group_name,
                                               child=each)

        # all grp_list
        grp_list = [self.sphere_group_name, self.cluster_group_name,
                    self.cylinder_group_name, self.arm_base_outer_ctrl,
                    self.curve_group_name]
        self.main_grp_name = self.prefix_name + '_' + self.arm_side + '_Arm_Tem_' + str(self.val) + '_Main_Grp'
        for each in grp_list:
            self.helper_class.parent_child_grp(parent=self.main_grp_name,
                                               child=each)

        cmds.select(self.main_grp_name)
        self.arm_grp_name = 'Arm_Grp'
        self.helper_class.parent_child_grp(parent=self.arm_grp_name,
                                           child=self.main_grp_name,
                                           trans_rot_scale=False)
        self.helper_class.transform_rotation_scale_visible(self.arm_grp_name, v=False)

    def mirror_value(self):
        for each in self.ctrl_list:
            self.right_ctrl = each
            if self.arm_side == 'L':
                old_val = 'L'
                new_val = 'R'
            elif self.arm_side == 'R':
                old_val = 'R'
                new_val = 'L'
            self.left_ctrl = each.replace(old_val, new_val)
            self.helper_class.mirror_grp(self.left_ctrl,
                                         self.right_ctrl)

    def mirror_status_def(self):
        # get the statu
        if self.mirror_check_box.isChecked():
            self.left_hand_check_box.setChecked(True)
            self.right_hand_check_box.setChecked(True)
        else:
            self.left_hand_check_box.setChecked(False)
            self.right_hand_check_box.setChecked(False)

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

        self.no_head = self.helper_class.get_arm()
        a = 0
        value = 0
        self.finger_list = {}
        grid_value = 0
        while a < len(self.no_head):
            self.finger_list[a] = QtGui.QRadioButton(self.head_name_scrollArea_widget_contents)
            self.finger_list[a].setObjectName(self.no_head[a])
            self.finger_list[a].setText(self.no_head[a])
            self.gridLayout_15.addWidget(self.finger_list[a], grid_value, value, 1, 1)
            self.finger_list[a].toggled.connect(partial(self.radio_button_change, a))
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
        self.mirror_check_box = QtGui.QCheckBox(self.arm_mirror_group_box)
        self.mirror_check_box.setObjectName("arm_mirror_check_box")
        self.mirror_check_box.setText('Mirror')
        self.mirror_check_box.stateChanged.connect(self.mirror_status_def)
        self.arm_mirror_grid_layout.addWidget(self.mirror_check_box, 0, 0, 1, 1)

        # LEFT
        self.left_hand_check_box = QtGui.QCheckBox(self.arm_mirror_group_box)
        self.left_hand_check_box.setObjectName("arm_left_check_box")
        self.left_hand_check_box.setText('Left')
        self.arm_mirror_grid_layout.addWidget(self.left_hand_check_box, 1, 0, 1, 1)

        # RIGHT
        self.right_hand_check_box = QtGui.QCheckBox(self.arm_mirror_group_box)
        self.right_hand_check_box.setObjectName("arm_right_check_box")
        self.right_hand_check_box.setText('Right')
        self.arm_mirror_grid_layout.addWidget(self.right_hand_check_box, 1, 1, 1, 1)

        # CLAVICAL
        self.clavical_check_box = QtGui.QCheckBox(self.arm_mirror_group_box)
        self.clavical_check_box.setObjectName("arm_clavical_check_box")
        self.clavical_check_box.setText('Clavical')
        self.arm_mirror_grid_layout.addWidget(self.clavical_check_box, 2, 0, 1, 1)

        # SCAPULA
        self.scapula_check_box = QtGui.QCheckBox(self.arm_mirror_group_box)
        self.scapula_check_box.setObjectName("arm_scapula_check_box")
        self.scapula_check_box.setText('Scapula')
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
        self.arm_bone_grid_layout.addWidget(self.upper_arm_roll_bone_label, 0, 0, 1, 1)
        # UPPER ARM BONE LINE EDIT
        self.upper_arm_roll_bone_line_edit = QtGui.QLineEdit(self.arm_bone_group_box)
        self.validator = QtGui.QDoubleValidator()
        self.upper_arm_roll_bone_line_edit.setObjectName("arm_upper_arm_bone_line_edit")
        self.upper_arm_roll_bone_line_edit.setValidator(self.validator)
        self.arm_bone_grid_layout.addWidget(self.upper_arm_roll_bone_line_edit, 0, 1, 1, 1)

        # LOWER ARM BONE
        # LOWER ARM BONE LABEL
        self.lower_arm_roll_bone = QtGui.QLabel(self.arm_bone_group_box)
        self.lower_arm_roll_bone.setObjectName("arm_lower_arm_bone_label")
        self.lower_arm_roll_bone.setText('Lower Arm Bone')
        self.arm_bone_grid_layout.addWidget(self.lower_arm_roll_bone, 1, 0, 1, 1)
        # LOWER ARM BONE LINE EDIT
        self.lower_arm_roll_bone_line_edit = QtGui.QLineEdit(self.arm_bone_group_box)
        self.lower_arm_roll_bone_line_edit.setObjectName("arm_lower_arm_bone_line_edit")
        self.lower_arm_roll_bone_line_edit.setValidator(self.validator)
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
        self.hand_check_box.stateChanged.connect(self.update_hand_check_box_def)
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
        self.gridLayout_26.addWidget(self.arm_name_label, 0, 0, 1, 1)
        # ARM NAME BUTTON
        self.arm_name_button = QtGui.QPushButton(self.arm_name_parent_group_box)
        self.arm_name_button.setMinimumSize(QtCore.QSize(297, 0))
        self.arm_name_button.setObjectName("arm_name_button")
        self.arm_name_button.clicked.connect(self.rename)

        self.gridLayout_26.addWidget(self.arm_name_button, 0, 1, 1, 1)

        # ARM PARENT
        # ARM PARENT LABEL
        self.arm_parent_label = QtGui.QLabel(self.arm_name_parent_group_box)
        self.arm_parent_label.setObjectName("arm_parent_label")
        self.arm_parent_label.setText('Parent')
        self.gridLayout_26.addWidget(self.arm_parent_label, 1, 0, 1, 1)
        # ARM PARENT BUTTON
        self.arm_parent_button = QtGui.QPushButton(self.arm_name_parent_group_box)
        self.arm_parent_button.setObjectName("arm_parent_button")
        self.arm_parent_button.clicked.connect(self.parent)

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
        self.arm_update_button.clicked.connect(self.arm_update_button_def)
        self.gridLayout_17.addWidget(self.arm_update_button, 1, 0, 1, 1)

        # DELETE BUTTON
        self.arm_delete_button = QtGui.QPushButton(self.head_update_scrollArea_widget_contents)
        self.arm_delete_button.setObjectName("arm_delete_button")
        self.arm_delete_button.setText('Delete(Arm Name)')
        self.arm_delete_button.clicked.connect(self.arm_delete_button_def)
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

    def update_hand_check_box_def(self):
        self.get_hand_checkbox = self.hand_check_box.isChecked()
        if self.get_hand_checkbox == True:
            a = 0
            while a < len(self.new_finger_label_list):
                self.new_finger_label_list[a].setDisabled(False)
                self.new_finger_line_edit_list[a].setDisabled(False)
                a += 1
        else:
            a = 0
            while a < len(self.new_finger_label_list):
                self.new_finger_label_list[a].setDisabled(True)
                self.new_finger_line_edit_list[a].setDisabled(True)
                a += 1

    def delete_all(self):
        print('now all hand is going to delete')

    def lock_attr(self):
        self.mirror_check_box.setDisabled(True)
        self.left_hand_check_box.setDisabled(True)
        self.right_hand_check_box.setDisabled(True)
        self.clavical_check_box.setDisabled(True)
        self.scapula_check_box.setDisabled(True)
        self.upper_arm_roll_bone_label.setDisabled(True)
        self.upper_arm_roll_bone_line_edit.setDisabled(True)
        self.lower_arm_roll_bone.setDisabled(True)
        self.lower_arm_roll_bone_line_edit.setDisabled(True)
        self.hand_check_box.setDisabled(True)
        self.arm_name_label.setDisabled(True)
        self.arm_name_button.setDisabled(True)
        self.arm_parent_label.setDisabled(True)
        self.arm_parent_button.setDisabled(True)
        self.arm_update_button.setDisabled(True)
        self.arm_delete_button.setDisabled(True)

    def unlock_attr(self):
        self.mirror_check_box.setDisabled(False)
        self.left_hand_check_box.setDisabled(False)
        self.right_hand_check_box.setDisabled(False)
        self.clavical_check_box.setDisabled(False)
        self.scapula_check_box.setDisabled(False)
        self.upper_arm_roll_bone_label.setDisabled(False)
        self.upper_arm_roll_bone_line_edit.setDisabled(False)
        self.lower_arm_roll_bone.setDisabled(False)
        self.lower_arm_roll_bone_line_edit.setDisabled(False)
        self.hand_check_box.setDisabled(False)
        self.arm_name_label.setDisabled(False)
        self.arm_name_button.setDisabled(False)
        self.arm_parent_label.setDisabled(False)
        self.arm_parent_button.setDisabled(False)
        self.arm_update_button.setDisabled(False)
        self.arm_delete_button.setDisabled(False)

    def radio_button_change(self, b, val):
        if val == True:
            # unlock the val
            self.unlock_attr()

            # get the value
            self.get_input_data(self.no_head[b])

            # get the value
            self.get_update_ui_def()

    def get_input_data(self, arm_name):
        # split the name
        self.arm_name = arm_name
        self.name = self.arm_name.split('_')
        self.arm_side = self.name[0]
        self.input_character_type = self.name[1]
        self.val = self.name[-1]

        # main grp name
        # Template_L_Arm_Tem_1_Main_Grp
        main_grp_name = '*_' + self.arm_side + '_Arm_Tem_' + self.val + '_Main_Grp'
        cmds.select(main_grp_name)
        sel_main_grp = cmds.ls(sl=True)[0]
        self.prefix_name = sel_main_grp.split('_' + self.arm_side + '_Arm_Tem_')[0]

        # Template_L_Arm_Base_Tem_1_Outer_Ctrl_right_to_left_Mirror_Grp
        # get the mirror
        mirror_grp_name = self.prefix_name + '_' + self.arm_side + '_Arm_Base_Tem_' + self.val + \
                          '_Outer_Ctrl_right_to_left_Mirror_Grp'
        if cmds.objExists(mirror_grp_name):
            self.mirror_check_box.setChecked(True)
        else:
            self.mirror_check_box.setChecked(False)

        # side
        if self.arm_side == 'L':
            mirror_grp_name = self.prefix_name + '_' + self.arm_side + '_Arm_Base_Tem_' + self.val + \
                              '_Outer_Ctrl_right_to_left_Mirror_Grp'
            if cmds.objExists(mirror_grp_name):
                self.mirror_check_box.setChecked(True)
                self.left_hand_check_box.setChecked(True)
                self.right_hand_check_box.setChecked(True)
            else:
                self.mirror_check_box.setChecked(False)
                self.left_hand_check_box.setChecked(False)
                self.right_hand_check_box.setChecked(False)

            self.left_hand_check_box.setChecked(True)
        elif self.arm_side == 'R':
            mirror_grp_name = self.prefix_name + '_' + self.arm_side + '_Arm_Base_Tem_' + self.val + \
                              '_Outer_Ctrl_left_to_right_Mirror_Grp'
            if cmds.objExists(mirror_grp_name):
                self.mirror_check_box.setChecked(True)
                self.left_hand_check_box.setChecked(True)
                self.right_hand_check_box.setChecked(True)
            else:
                self.mirror_check_box.setChecked(False)
                self.left_hand_check_box.setChecked(False)
                self.right_hand_check_box.setChecked(False)

            self.right_hand_check_box.setChecked(True)

        # get clavical
        # upper bone
        # Template_L_Arm_Upper_0_Tem_1Geo
        self.upper_bone_name = self.prefix_name + '_' + self.arm_side + '_Arm_Upper_*_Tem_' \
                                                                        '' + self.val + '_Geo'
        # Template_L_Arm_Upper_Hand_Tem_1_Geo
        self.upper_hand_name = self.prefix_name + '_' + self.arm_side + '_Arm_Upper_Hand_Tem_' \
                                                                        '' + self.val + '_Geo'
        cmds.select(self.upper_bone_name)
        self.sel_upper_bone = cmds.ls(sl=True)
        if cmds.objExists(self.upper_hand_name):
            self.sel_upper_bone.remove(self.upper_hand_name)
        self.upper_arm_roll_bone_line_edit.setText(str(len(self.sel_upper_bone)))

        # lower bone
        # Template_L_Arm_Upper_0_Tem_1Geo
        self.lower_bone_name = self.prefix_name + '_' + self.arm_side + '_Arm_Lower_*_Tem_' \
                                                                        '' + self.val + '_Geo'
        cmds.select(self.lower_bone_name)
        self.sel_lower_bone = cmds.ls(sl=True)
        self.lower_arm_roll_bone_line_edit.setText(str(len(self.sel_lower_bone)))

        # get the one ourter ctrl
        # Template_L_Arm_Finger_1_1_Tem_2_Outer_Ctrl
        self.outer_one_ctrl_name = self.prefix_name + '_' + self.arm_side + '_Arm_Finger_1_1_Tem_' \
                                                                            '' + self.val + '_Outer_Ctrl'

        self.new_finger_label_list = self.arm_finger_label
        self.new_finger_line_edit_list = self.arm_finger_line_edit

        if cmds.objExists(self.outer_one_ctrl_name):
            self.hand_check_box.setChecked(True)
            # delete if exist#
            if self.arm_finger_line_edit != {}:
                a = 0
                while a < len(self.no_finger):
                    self.finger_label_list[a].deleteLater()
                    self.arm_finger_line_edit[a].deleteLater()
                    a += 1

            # Template_L_Arm_Finger_1_1_Tem_2_Outer_Ctrl
            self.hand_ctrl = self.prefix_name + '_' + self.arm_side + '_Arm_Finger_*_1_Tem_' \
                                                                      '' + self.val + '_Outer_Ctrl'
            cmds.select(self.hand_ctrl)
            self.no_finger = cmds.ls(sl=True)
            # get the finger

            a = 0
            while a < len(self.no_finger):
                self.finger_label_list[a] = QtGui.QLabel(self.arm_finger_group_box)
                finger_name = "Finger : " + str(a + 1)
                self.finger_label_list[a].setObjectName(finger_name)
                self.finger_label_list[a].setText(finger_name)
                self.arm_finger_grid_layout.addWidget(self.finger_label_list[a], a, 0, 1, 1)

                self.arm_finger_line_edit[a] = QtGui.QLineEdit(self.arm_finger_group_box)
                self.arm_finger_line_edit[a].setObjectName("arm_finger_1_lineEdit")
                self.arm_finger_line_edit[a].setValidator(self.validator)
                # Template_R_Arm_Finger_1_1_Tem_1_Outer_Ctrl
                outer_ctrl = self.prefix_name + '_' + self.arm_side + '_Arm_Finger_' + str(a + 1) + '_*_Tem_' \
                                                                                                    '' + self.val + '_Outer_Ctrl'
                no_finger = self.get_finger_no(outer_ctrl)
                self.arm_finger_line_edit[a].setText(str(no_finger))
                self.arm_finger_grid_layout.addWidget(self.arm_finger_line_edit[a], a, 1, 1, 1)

                a += 1
        else:
            self.hand_check_box.setChecked(False)
            if self.arm_finger_line_edit != {}:
                a = 0
                while a < len(self.no_finger):
                    self.finger_label_list[a].deleteLater()
                    self.arm_finger_line_edit[a].deleteLater()
                    a += 1
                self.arm_finger_line_edit = {}
                self.finger_label_list = {}

        self.new_finger_label_list = self.finger_label_list
        self.new_finger_line_edit_list = self.arm_finger_line_edit
        # set the name
        self.arm_name_button.setText(self.prefix_name)

        # parent button
        # Template_L_Arm_Base_Tem_1_Outer_Ctrl
        base_ctrl_name = self.prefix_name + '_' + self.arm_side + '_Arm_Base_Tem_' + self.val + '_Outer_Ctrl'
        value = cmds.listRelatives(base_ctrl_name, type='parentConstraint')
        if value == None:
            parent = 'None'
        else:
            parent = value[0]

        self.arm_parent_button.setText(parent)

        # update the button
        self.arm_update_button.setText('Update (%s)' % self.arm_name)
        self.arm_delete_button.setText('Delete(%s)' % self.arm_name)

    def get_update_ui_def(self):
        # GET MIRROR
        self.get_mirror_checkbox = self.mirror_check_box.isChecked()

        # GET LEFT
        self.get_left_checkbox = self.left_hand_check_box.isChecked()

        # GET RIGHT
        self.get_right_checkbox = self.right_hand_check_box.isChecked()

        # GET CLAVICAL
        self.get_clavical_checkbox = self.clavical_check_box.isChecked()

        # GET SCAPULA
        self.get_scapula_checkbox = self.scapula_check_box.isChecked()

        # GET UPPER ARM BONE
        self.get_upper_arm_roll_lineedit = int(self.upper_arm_roll_bone_line_edit.text())

        # GET LOWER ARM BONE
        self.get_lower_arm_roll_lineedit = int(self.lower_arm_roll_bone_line_edit.text())

        # GET HAND CHECKBOX
        self.get_hand_checkbox = self.hand_check_box.isChecked()

        # NO OF THE FINGER
        self.get_finger = self.arm_finger_line_edit

    def get_finger_no(self, outer_no):
        cmds.select(outer_no)
        # Template_R_Arm_Finger_1_1_Tem_1_Outer_Ctrl
        sel_ctrl = cmds.ls(sl=True)
        return len(sel_ctrl)

    def remove_roll(self, side):
        # ssssss_L_Arm_Upper_Tem_1_Crv
        common_name = self.prefix_name + '_' + self.arm_side + '_Arm_' + side + '_Tem_' + self.val
        crv_name = common_name + '_Crv'
        # ssssss_L_Arm_Upper_0_Tem_1_Geo
        new_common = self.prefix_name + '_' + self.arm_side + '_Arm_' + side + '_*_Tem_' + self.val
        geo_name = new_common + '_Geo'
        clu_handle_name = new_common + '_CluHandle'
        cmds.select(crv_name, geo_name, clu_handle_name)
        cmds.delete()

    def arm_update_button_def(self):
        # get the ui data
        self.get_update_ui_def()
        # get the variable
        self.controller_variable()

        # check the upper bone
        if len(self.sel_upper_bone) != self.get_upper_arm_roll_lineedit:
            # delete the roll
            self.remove_roll('Upper')
            self.roll_bone('Upper',
                           self.arm_upper_hand_inner_ctrl,
                           self.arm_lbow_inner_ctrl,
                           self.get_upper_arm_roll_lineedit)
            self.final_group()
            # if mirror is on
            if self.get_mirror_checkbox == True:
                if self.arm_side == 'R':
                    value = 'L'
                elif self.arm_side == 'L':
                    value = 'R'
                self.arm_side = value
                self.controller_variable()
                self.remove_roll('Upper')
                self.roll_bone('Upper',
                               self.arm_upper_hand_inner_ctrl,
                               self.arm_lbow_inner_ctrl,
                               self.get_upper_arm_roll_lineedit)
                self.final_group()

        # check the lower bone
        if len(self.sel_lower_bone) != self.get_lower_arm_roll_lineedit:
            # delete the roll
            self.remove_roll('Lower')
            self.roll_bone('Lower',
                           self.arm_lbow_inner_ctrl,
                           self.arm_hand_inner_ctrl,
                           self.get_lower_arm_roll_lineedit)
            self.final_group()
            # if mirror is on
            if self.get_mirror_checkbox == True:
                if self.arm_side == 'R':
                    value = 'L'
                elif self.arm_side == 'L':
                    value = 'R'
                self.arm_side = value
                self.controller_variable()
                self.remove_roll('Lower')
                self.roll_bone('Lower',
                               self.arm_lbow_inner_ctrl,
                               self.arm_hand_inner_ctrl,
                               self.get_lower_arm_roll_lineedit)
                self.final_group()

        if self.get_hand_checkbox == True:
            # get each finger value
            a = 0
            while a < len(self.arm_finger_line_edit):
                # get the query
                # Template_L_Arm_Finger_2_1_Tem_1_Outer_Ctrl
                # get the query
                self.finger_query = int(self.arm_finger_line_edit[a].text())
                outer_ctrl = self.prefix_name + '_' + self.arm_side + '_Arm_Finger_' + str(
                    a + 1) + '_*_Tem_' + self.val + \
                             '_Outer_Ctrl'

                cmds.select(outer_ctrl)
                sel_outer = cmds.ls(sl=True)
                if self.finger_query != len(sel_outer):
                    self.new_finger_def()
                    break

                a += 1

            pass
            '''
            self.no_finger_line_edit_query = len(self.new_finger_label_list)
            self.finger_default_pos = [61.0,0,0]
            self.finger_def()
            self.final_group()
            if self.get_mirror_checkbox == True:
                if self.arm_side == 'R':
                    value = 'L'
                elif self.arm_side == 'L':
                    value = 'R'
                self.arm_side = value
                self.controller_variable()
                self.no_finger_line_edit_query = len(self.new_finger_label_list)
                self.finger_default_pos = [-61.0,0,0]
                self.finger_def()
                #mirror the controller
                #self.mirror_value()
                self.final_group()
                if self.arm_side == 'R':
                    value = 'L'
                elif self.arm_side == 'L':
                    value = 'R'
                self.arm_side = value
            '''
        else:
            # Template_L_Arm_Finger_1_1_Tem_1_Outer_Ctrl_right_to_left_Mirror_Grp
            finger_common = self.prefix_name + "_" + self.arm_side + "_Arm_Finger_*_*_Tem_" + str(self.val)
            finger_outer_ctrl = finger_common + '_*'
            if cmds.objExists(finger_outer_ctrl):
                cmds.select(finger_outer_ctrl)
                cmds.delete()
                if self.get_mirror_checkbox == True:
                    if self.arm_side == 'R':
                        value = 'L'
                    elif self.arm_side == 'L':
                        value = 'R'
                    self.arm_side = value
                    finger_common = self.prefix_name + "_" + self.arm_side + "_Arm_Finger_*_*_Tem_" + str(self.val)
                    finger_outer_ctrl = finger_common + '_*'
                    cmds.select(finger_outer_ctrl)
                    cmds.delete()

                    if self.arm_side == 'R':
                        value = 'L'
                    elif self.arm_side == 'L':
                        value = 'R'
                    self.arm_side = value

    def arm_delete_button_def(self):
        # Template_Human_Head_Tem_1_Main_Grp
        main_new_grp_name = self.prefix_name + '_' + self.arm_side + '_Head_Tem_' + self.val + '_Main_Grp'
        cmds.select(main_new_grp_name)
        cmds.delete()

    def rename(self):
        self.get_mirror_checkbox = self.mirror_check_box.isChecked()
        if self.get_mirror_checkbox == True:
            if self.arm_side == 'L':
                value = 'R'
            elif self.arm_side == 'R':
                value = 'L'
            rename.main('Arm', self.arm_name, self.arm_name_button,
                        mirror_val=True,
                        mirror_side=value)
        else:
            rename.main('Arm', self.arm_name, self.arm_name_button)

    def parent(self):
        parent.main('Arm', self.arm_name, self.arm_parent_button)

    def controller_variable(self):
        if self.arm_side == 'L':
            self.base_ctrl_color = 'Blue'
        else:
            self.base_ctrl_color = 'Red'

        self.base_common = self.prefix_name + "_" + self.arm_side + "_Arm_Base_Tem_" + str(self.val)
        self.base_sphere_name = self.base_common + "_Geo"
        self.arm_base_inner_ctrl = self.base_common + '_Inner_Ctrl'
        self.arm_base_outer_ctrl = self.base_common + '_Outer_Ctrl'

        # SHOULDER
        self.shoulder_common = self.prefix_name + "_" + self.arm_side + "_Arm_Shoulder_Tem_" + str(self.val)
        self.shoulder_sphere_name = self.shoulder_common + "_Geo"
        self.arm_shoulder_inner_ctrl = self.shoulder_common + '_Inner_Ctrl'
        self.arm_shoulder_outer_ctrl = self.shoulder_common + '_Outer_Ctrl'

        # UPPPER HAND
        self.upper_hand_common = self.prefix_name + "_" + self.arm_side + "_Arm_Upper_Hand_Tem_" + str(self.val)
        self.upper_hand_sphere_name = self.upper_hand_common + "_Geo"
        self.arm_upper_hand_inner_ctrl = self.upper_hand_common + '_Inner_Ctrl'
        self.arm_upper_hand_outer_ctrl = self.upper_hand_common + '_Outer_Ctrl'

        # LBOW
        self.lbow_common = self.prefix_name + "_" + self.arm_side + "_Arm_lBow_Tem_" + str(self.val)
        self.lbow_sphere_name = self.lbow_common + "_Geo"
        self.arm_lbow_inner_ctrl = self.lbow_common + '_Inner_Ctrl'
        self.arm_lbow_outer_ctrl = self.lbow_common + '_Outer_Ctrl'

        # HAND
        self.hand_common = self.prefix_name + "_" + self.arm_side + "_Arm_Hand_Tem_" + str(self.val)
        self.hand_sphere_name = self.hand_common + "_Geo"
        self.arm_hand_inner_ctrl = self.hand_common + '_Inner_Ctrl'
        self.arm_hand_outer_ctrl = self.hand_common + '_Outer_Ctrl'

        # HAND END
        self.hand_end_common = self.prefix_name + "_" + self.arm_side + "_Arm_Hand_End_Tem_" + str(self.val)
        self.hand_end_sphere_name = self.hand_end_common + "_Geo"
        self.arm_hand_end_inner_ctrl = self.hand_end_common + '_Inner_Ctrl'
        self.arm_hand_end_outer_ctrl = self.hand_end_common + '_Outer_Ctrl'

    def new_finger_def(self):
        self.finger_change_def()

        # check if mirror is there
        if self.get_mirror_checkbox == True:
            if self.arm_side == 'L':
                value = 'R'
            else:
                value = 'L'
            self.arm_side = value
            # new reverse variable
            self.controller_variable()
            self.finger_change_def()
            # self.mirror_value()

            if self.arm_side == 'L':
                value = 'R'
            else:
                value = 'L'
            self.arm_side = value

    def finger_change_def(self):
        # get the no of the finger

        # get the first controller
        outer_ctrl = self.prefix_name + '_' + self.arm_side + '_Arm_Finger_*_*_Tem_' + self.val + \
                     '_Outer_Ctrl'
        # get the ctrl pos

        if self.arm_side == 'L':
            mirror_name = 'right_to_left'
        else:
            mirror_name = 'left_to_right'

        mirror_grp_name = outer_ctrl + '_' + mirror_name + '_Mirror_Grp'
        cmds.select(outer_ctrl)
        # ssss_R_Arm_Finger_4_1_Tem_1_CluHandle
        common_name = self.prefix_name + '_' + self.arm_side + '_Arm_Finger_*_*_Tem_' + self.val
        clu_sphere_name = common_name + '_CluHandle'
        sphere_name = common_name + '_Geo'
        # ssss_R_Arm_Finger_4_2_Tem_1_Cylinder_Geo
        cylinder_name = self.prefix_name + '_' + self.arm_side + '_Arm_Finger_*_*_Tem_' + self.val + '_Cylinder_Geo'
        # ssss_R_Arm_Finger_Hand_to_Upper_4_1_Tem_1_CluHandle
        # ssss_R_Arm_Finger_Hand_to_Lower_4_1_Tem_1_CluHandle
        # ssss_R_Arm_Finger_Upper_4_2_Tem_1_CluHandle
        # ssss_R_Arm_Finger_Lower_4_2_Tem_1_CluHandle

        clu_hand_to_upper_name = self.prefix_name + '_' + self.arm_side + '_Arm_Finger_Hand_to_Upper_*_*_Tem_' + self.val + \
                                 '_CluHandle'
        clu_hand_to_lower_name = self.prefix_name + '_' + self.arm_side + '_Arm_Finger_Hand_to_Lower_*_*_Tem_' + self.val + \
                                 '_CluHandle'
        clu_upper_name = self.prefix_name + '_' + self.arm_side + '_Arm_Finger_Upper_*_*_Tem_' + self.val + \
                         '_CluHandle'
        clu_lower_name = self.prefix_name + '_' + self.arm_side + '_Arm_Finger_Lower_*_*_Tem_' + self.val + \
                         '_CluHandle'

        cmds.select(clu_sphere_name,
                    sphere_name,
                    cylinder_name,
                    clu_hand_to_upper_name,
                    clu_hand_to_lower_name,
                    clu_upper_name,
                    clu_lower_name,
                    outer_ctrl)
        cmds.delete()

        self.no_finger_line_edit_query = len(self.arm_finger_line_edit)
        self.finger_default_pos = cmds.xform(self.arm_hand_outer_ctrl, q=1, ws=1, rp=1)
        print('----------', self.finger_default_pos)
        self.finger_def()

        # create a final grp
        self.final_group()

    def controller_get_data(self, main_grp_name):
        # Template_L_Arm_Tem_1_Main_Grp
        main_grp_split = main_grp_name.split('_')
        self.prefix_name = main_grp_split[0]
        self.arm_side = main_grp_split[1]
        self.val = main_grp_split[4]

        self.ctrl_list = {}

        # SHOULDER
        self.shoulder_common = self.prefix_name + "_" + self.arm_side + "_Arm_Shoulder_Tem_" + str(self.val)
        self.shoulder_ctrl_name = self.shoulder_common + '_Inner_Ctrl'
        self.shoulder_jnt_name = self.shoulder_common + '_Jnt'
        self.shoulder_ctrl_get_trans = cmds.xform(self.shoulder_ctrl_name, q=1, ws=1, rp=1)
        self.shoulder_ctrl_get_rot = cmds.getAttr(self.shoulder_ctrl_name + '.r')
        self.ctrl_list[self.shoulder_ctrl_name] = {}
        self.ctrl_list[self.shoulder_ctrl_name]['Trans'] = self.shoulder_ctrl_get_trans
        self.ctrl_list[self.shoulder_ctrl_name]['Rot'] = self.shoulder_ctrl_get_rot

        # UPPPER HAND
        self.upper_hand_common = self.prefix_name + "_" + self.arm_side + "_Arm_Upper_Hand_Tem_" + str(self.val)
        self.upper_hand_ctrl_name = self.upper_hand_common + '_Inner_Ctrl'
        self.upper_hand_jnt_name = self.upper_hand_common + '_Jnt'
        self.upper_hand_ctrl_get_trans = cmds.xform(self.upper_hand_ctrl_name, q=1, ws=1, rp=1)
        self.upper_hand_ctrl_get_rot = cmds.getAttr(self.upper_hand_ctrl_name + '.r')
        self.ctrl_list[self.upper_hand_ctrl_name] = {}
        self.ctrl_list[self.upper_hand_ctrl_name]['Trans'] = self.upper_hand_ctrl_get_trans
        self.ctrl_list[self.upper_hand_ctrl_name]['Rot'] = self.upper_hand_ctrl_get_rot

        # LBOW
        self.lbow_common = self.prefix_name + "_" + self.arm_side + "_Arm_lBow_Tem_" + str(self.val)
        self.lbow_ctrl_name = self.lbow_common + '_Inner_Ctrl'
        self.lbow_jnt_name = self.lbow_common + '_Jnt'
        self.lbow_ctrl_get_trans = cmds.xform(self.lbow_ctrl_name, q=1, ws=1, rp=1)
        self.lbow_ctrl_get_rot = cmds.getAttr(self.lbow_ctrl_name + '.r')
        self.ctrl_list[self.lbow_ctrl_name] = {}
        self.ctrl_list[self.lbow_ctrl_name]['Trans'] = self.lbow_ctrl_get_trans
        self.ctrl_list[self.lbow_ctrl_name]['Rot'] = self.lbow_ctrl_get_rot

        # HAND
        self.hand_common = self.prefix_name + "_" + self.arm_side + "_Arm_Hand_Tem_" + str(self.val)
        self.hand_ctrl_name = self.hand_common + '_Inner_Ctrl'
        self.hand_jnt_name = self.hand_common + '_Jnt'
        self.hand_ctrl_get_trans = cmds.xform(self.hand_ctrl_name, q=1, ws=1, rp=1)
        self.hand_ctrl_get_rot = cmds.getAttr(self.hand_ctrl_name + '.r')
        self.ctrl_list[self.hand_ctrl_name] = {}
        self.ctrl_list[self.hand_ctrl_name]['Trans'] = self.hand_ctrl_get_trans
        self.ctrl_list[self.hand_ctrl_name]['Rot'] = self.hand_ctrl_get_rot

        # HAND END
        self.hand_end_common = self.prefix_name + "_" + self.arm_side + "_Arm_Hand_End_Tem_" + str(self.val)
        self.hand_end_ctrl_name = self.hand_end_common + '_Inner_Ctrl'
        self.hand_end_jnt_name = self.hand_end_common + '_Jnt'
        self.hand_end_ctrl_get_trans = cmds.xform(self.hand_end_ctrl_name, q=1, ws=1, rp=1)
        self.hand_end_ctrl_get_rot = cmds.getAttr(self.hand_end_ctrl_name + '.r')
        self.ctrl_list[self.hand_end_ctrl_name] = {}
        self.ctrl_list[self.hand_end_ctrl_name]['Trans'] = self.hand_end_ctrl_get_trans
        self.ctrl_list[self.hand_end_ctrl_name]['Rot'] = self.hand_end_ctrl_get_rot

        # UPPER ARM GEO
        # Template_L_Arm_Upper_0_Tem_1_Geo
        self.upper_arm_jnt_list = {}
        geo_name = self.prefix_name + "_" + self.arm_side + "_Arm_Upper_*_Tem_" + str(self.val) + '_Geo'
        # Template_L_Arm_Upper_Hand_Tem_1_Jnt
        upper_hand_common = self.prefix_name + "_" + self.arm_side + "_Arm_Upper_Hand_Tem_" + str(self.val)
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
        geo_name = self.prefix_name + "_" + self.arm_side + "_Arm_Lower_*_Tem_" + str(self.val) + '_Geo'
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
        # Template_L_Arm_Finger_1_1_Tem_1_Outer_Ctrl
        self.finger_list = []
        outer_finger_ctrl = self.prefix_name + "_" + self.arm_side + "_Arm_Finger_*_1_Tem_" + str(
            self.val) + '_Inner_Ctrl'
        if cmds.objExists(outer_finger_ctrl):
            cmds.select(outer_finger_ctrl)
            sel_finger = cmds.ls(sl=True)
            for each_finger in sel_finger:
                self.finger_list.append(each_finger)

    def arm_create(self):
        # get the no of the human main grp
        self.grp_list = ['Arm_Grp']
        for each_grp in self.grp_list:
            # list of the all children
            if cmds.objExists(each_grp):
                children_list = cmds.listRelatives(each_grp, children=True)
                for each_child in children_list:
                    # get all the controller data
                    self.arm_data(each_child)

                    # FINAL THE ARM
                    self.final_arm_def()

    def arm_data(self, main_grp_name):
        split_name = main_grp_name.split('_')
        # Template_Animal_Head_Tem_1_Main_Grp
        main_grp = main_grp_name.split('_Arm_Tem_')[1]
        self.prefix_name = split_name[0]
        self.side = split_name[1]
        self.type = split_name[1]
        self.val = main_grp.split('_Main_Grp')[0]

        # get each ctrl position data
        self.get_each_pos_data(main_grp_name)

    def get_each_pos_data(self, main_grp_name):
        self.ctrl_list = {}
        self.common_list = []

        # UPPER HAND
        # Template_L_Arm_Upper_Hand_Tem_1_Inner_Ctrl
        self.upper_hand_common = self.prefix_name + "_" + self.side + "_Arm_Upper_Hand_Tem_" + str(self.val)
        self.upper_hand_inner_ctrl, self.upper_hand_jnt_name, self.upper_hand_fk_jnt_name, self.upper_hand_ik_jnt_name, \
        self.upper_hand_result_jnt_name = self.get_data_variable(self.upper_hand_common)

        # LBOW
        # Template_L_Arm_lBow_Tem_1_Inner_Ctrl
        self.lbow_common = self.prefix_name + "_" + self.side + "_Arm_lBow_Tem_" + str(self.val)
        self.lbow_inner_ctrl, self.lbow_jnt_name, self.lbow_fk_jnt_name, self.lbow_ik_jnt_name, \
        self.lbow_result_jnt_name = self.get_data_variable(self.lbow_common)

        # HAND HAND
        # Template_L_Arm_Hand_Tem_1_Inner_Ctrl
        self.hand_common = self.prefix_name + "_" + self.side + "_Arm_Hand_Tem_" + str(self.val)
        self.hand_inner_ctrl, self.hand_jnt_name, self.hand_fk_jnt_name, self.hand_ik_jnt_name, \
        self.hand_result_jnt_name = self.get_data_variable(self.hand_common)

        self.shoulder_common = self.prefix_name + "_" + self.side + "_Arm_Shoulder_Tem_" + str(self.val)

        # UPPER ARM GEO
        # Template_L_Arm_Upper_0_Tem_1_Geo
        self.upper_jnt_list = {}
        geo_name = self.prefix_name + "_" + self.side + "_Arm_Upper_*_Tem_" + str(self.val) + '_Geo'
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
        # Template_L_Arm_Lower_0_Tem_1_Geo
        self.lower_jnt_list = {}
        geo_name = self.prefix_name + "_" + self.side + "_Arm_Lower_*_Tem_" + str(self.val) + '_Geo'
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
        # Template_L_Arm_Finger_1_1_Tem_1_Inner_Ctrl
        self.finger_list = []
        outer_finger_ctrl = self.prefix_name + "_" + self.side + "_Arm_Finger_*_1_Tem_" + str(self.val) + '_Inner_Ctrl'
        if cmds.objExists(outer_finger_ctrl):
            cmds.select(outer_finger_ctrl)
            sel_finger = cmds.ls(sl=True)
            for each_finger in sel_finger:
                self.finger_list.append(each_finger)

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
            return inner_ctrl, jnt_name, fk_name, ik_name, result_name

    def final_arm_def(self):
        ik_jnt_list = []
        fk_jnt_list = []
        result_jnt_list = []

        root_grp_name = "Root_Grp"
        self.root_grp_name = root_grp_name
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

        # parent the joint
        # self.helper_class.maya_parent(self.upper_hand_fk_jnt_name,self.shoulder_fk_jnt_name)
        self.helper_class.maya_parent(self.lbow_fk_jnt_name, self.upper_hand_fk_jnt_name)
        self.helper_class.maya_parent(self.hand_fk_jnt_name, self.lbow_fk_jnt_name)

        # self.helper_class.maya_parent(self.upper_hand_ik_jnt_name,self.shoulder_ik_jnt_name)
        self.helper_class.maya_parent(self.lbow_ik_jnt_name, self.upper_hand_ik_jnt_name)
        self.helper_class.maya_parent(self.hand_ik_jnt_name, self.lbow_ik_jnt_name)

        # self.helper_class.maya_parent(self.upper_hand_result_jnt_name,self.shoulder_result_jnt_name)
        self.helper_class.maya_parent(self.lbow_result_jnt_name, self.upper_hand_result_jnt_name)
        self.helper_class.maya_parent(self.hand_result_jnt_name, self.lbow_result_jnt_name)

        # make a group
        fk_jnt_grp_name = self.upper_hand_fk_jnt_name + '_Grp'
        cmds.select(self.upper_hand_fk_jnt_name)
        cmds.group(n=fk_jnt_grp_name)

        ik_jnt_grp_name = self.upper_hand_ik_jnt_name + '_Grp'
        cmds.select(self.upper_hand_ik_jnt_name)
        cmds.group(n=ik_jnt_grp_name)

        result_jnt_grp_name = self.upper_hand_result_jnt_name + '_Grp'
        cmds.select(self.upper_hand_result_jnt_name)
        cmds.group(n=result_jnt_grp_name)

        cmds.select(self.upper_hand_fk_jnt_name, self.upper_hand_ik_jnt_name, self.upper_hand_result_jnt_name)
        cmds.joint(e=True, oj='xyz', secondaryAxisOrient='xup', ch=True, zso=True)

        # create a ik and fk switch
        self.controller_class.cube_ctrl()
        sel_obj = cmds.ls(sl=True)
        ik_fk_switch_name = self.prefix_name + "_" + self.side + "_Hand_Ik_Fk_Switch_" + str(self.val) + '_Ctrl'
        ik_fk_switch_grp_name = ik_fk_switch_name + '_Grp'
        cmds.rename(sel_obj[0], ik_fk_switch_name)
        cmds.move(self.ctrl_list[self.hand_inner_ctrl]['Trans'][0],
                  self.ctrl_list[self.hand_inner_ctrl]['Trans'][1],
                  self.ctrl_list[self.hand_inner_ctrl]['Trans'][2])
        # move -r -os -wd 0 0 -6.664142 ;
        cmds.move(0, 0, -6, r=True)
        cmds.group(n=ik_fk_switch_grp_name)
        self.helper_class.transform_rotation_scale_visible(ik_fk_switch_grp_name)
        cmds.select(ik_fk_switch_name)

        cmds.DeleteHistory()
        cmds.FreezeTransformations()
        cmds.parentConstraint(self.hand_result_jnt_name, ik_fk_switch_name, mo=True)
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
            a += 1

        # CREATE A FK JOINT
        a = 0
        if self.side == 'L':
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
        cmds.setAttr((ik_fk_switch_name + '.IK_FK_Switch'), 1)
        cmds.addAttr(self.upper_hand_fk_jnt_name, ln="Stretch", at='double', min=-1, dv=0)
        cmds.setAttr((self.upper_hand_fk_jnt_name + ".Stretch"), e=True, keyable=True)
        cmds.setDrivenKeyframe((self.lbow_fk_jnt_name + ".tx"),
                               currentDriver=(self.upper_hand_fk_jnt_name + ".Stretch"))

        cmds.setAttr((self.upper_hand_fk_jnt_name + ".Stretch"), -1)
        cmds.setAttr((self.lbow_fk_jnt_name + ".tx"), 0)
        cmds.setDrivenKeyframe((self.lbow_fk_jnt_name + ".tx"),
                               currentDriver=(self.upper_hand_fk_jnt_name + ".Stretch"))
        mel.eval("selectKey -add -k -f -1 -f 0 %s;" % (self.lbow_fk_jnt_name + "_translateX"))
        mel.eval('setInfinity -poi cycleRelative;')
        cmds.setAttr((self.upper_hand_fk_jnt_name + ".Stretch"), 0)

        cmds.addAttr(self.lbow_fk_jnt_name, ln="Stretch", at='double', min=-1, dv=0)
        cmds.setAttr((self.lbow_fk_jnt_name + ".Stretch"), e=True, keyable=True)
        cmds.setDrivenKeyframe((self.hand_fk_jnt_name + ".tx"), currentDriver=(self.lbow_fk_jnt_name + ".Stretch"))
        cmds.setAttr((self.lbow_fk_jnt_name + ".Stretch"), -1)
        cmds.setAttr((self.hand_fk_jnt_name + ".tx"), 0)
        cmds.setDrivenKeyframe((self.hand_fk_jnt_name + ".tx"), currentDriver=(self.lbow_fk_jnt_name + ".Stretch"))
        mel.eval("selectKey -add -k -f -1 -f 0 %s;" % (self.hand_fk_jnt_name + "_translateX"))
        mel.eval('setInfinity -poi cycleRelative;')
        cmds.setAttr((self.lbow_fk_jnt_name + ".Stretch"), 0)

        # create a the controller ik position
        hand_ctrl_name = self.prefix_name + "_" + self.side + "_Hand_" + str(self.val) + '_Ctrl'
        hand_ctrl_grp_name = hand_ctrl_name + '_Grp'
        self.controller_class.hand_ctrl()
        cmds.select('hand_ctrl')
        sel_obj = cmds.ls(sl=True)
        cmds.rename(sel_obj[0], hand_ctrl_name)
        cmds.select(hand_ctrl_name)
        cmds.move(self.ctrl_list[self.hand_inner_ctrl]['Trans'][0],
                  self.ctrl_list[self.hand_inner_ctrl]['Trans'][1],
                  self.ctrl_list[self.hand_inner_ctrl]['Trans'][2])
        # move -r -os -wd 0 0 -6.664142 ;

        cmds.setAttr((hand_ctrl_name + '.sx'), 5)
        cmds.setAttr((hand_ctrl_name + '.sy'), 5)
        cmds.setAttr((hand_ctrl_name + '.sz'), 5)
        cmds.DeleteHistory()
        cmds.FreezeTransformations()
        cmds.addAttr(hand_ctrl_name, ln="IK_pv_no_Flip_Switch", at='double', min=0, max=1)
        cmds.setAttr((hand_ctrl_name + ".IK_pv_no_Flip_Switch"), e=True, keyable=True)
        cmds.select(hand_ctrl_name)
        cmds.group(n=hand_ctrl_grp_name)
        cmds.connectAttr((ik_fk_switch_name + '.IK_FK_Switch'), (hand_ctrl_grp_name + '.v'), f=True)
        self.helper_class.color_val(color_name, hand_ctrl_name)

        ik_handle_name = self.prefix_name + "_" + self.side + "_Hand_" + str(self.val) + '_IK_Handle'
        cmds.ikHandle(n=ik_handle_name,
                      sj=self.upper_hand_ik_jnt_name,
                      ee=self.hand_ik_jnt_name,
                      sol='ikRPsolver')
        cmds.setAttr((ik_handle_name + '.v'), 0)
        cmds.select(ik_handle_name, hand_ctrl_name)
        cmds.parent()

        # create a distance between the shoulder and hand
        dimention = cmds.distanceDimension(sp=(self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][0],
                                               self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][1],
                                               self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][2]),
                                           ep=(self.ctrl_list[self.hand_inner_ctrl]['Trans'][0],
                                               self.ctrl_list[self.hand_inner_ctrl]['Trans'][1],
                                               self.ctrl_list[self.hand_inner_ctrl]['Trans'][2]))
        get_loc = cmds.listConnections(dimention)
        upper_hand_to_hand_start_loc = self.prefix_name + "_" + self.side + "_Upper_Hand_to_Hand_" + str(
            self.val) + '_Start_Loc'
        upper_hand_to_hand_end_loc = self.prefix_name + "_" + self.side + "_Upper_Hand_to_Hand_" + str(
            self.val) + '_End_Loc'
        dimention_name = self.prefix_name + "_" + self.side + "_Upper_Hand_to_Hand_" + str(self.val) + '_Dis'
        dimention_shape_name = dimention_name + 'Shape'
        cmds.rename(get_loc[0], upper_hand_to_hand_start_loc)
        cmds.rename(get_loc[1], upper_hand_to_hand_end_loc)
        cmds.select(upper_hand_to_hand_end_loc, hand_ctrl_name)
        cmds.parent()
        dimention_parent = cmds.listRelatives(dimention, parent=True)
        cmds.rename(dimention_parent, dimention_name)

        # make a stretch
        driver = dimention_shape_name + '.distance'
        thine_length = cmds.getAttr(self.lbow_ik_jnt_name + '.tx')
        shine_length = cmds.getAttr(self.hand_ik_jnt_name + '.tx')
        sumlength = thine_length + shine_length
        cmds.setDrivenKeyframe(self.lbow_ik_jnt_name, currentDriver=driver, driverValue=sumlength, attribute='tx',
                               value=thine_length)
        cmds.setDrivenKeyframe(self.lbow_ik_jnt_name, currentDriver=driver, driverValue=sumlength * 2, attribute='tx',
                               value=thine_length * 2)

        cmds.setDrivenKeyframe(self.hand_ik_jnt_name, currentDriver=driver, driverValue=sumlength, attribute='tx',
                               value=shine_length)
        cmds.setDrivenKeyframe(self.hand_ik_jnt_name, currentDriver=driver, driverValue=sumlength * 2, attribute='tx',
                               value=shine_length * 2)

        mel.eval("selectKey -add -k -f -38.574463 -f 77.148926 %s;" % (self.lbow_ik_jnt_name + "_translateX"))
        mel.eval('keyTangent -e -itt linear -ott linear;')
        mel.eval('setInfinity -poi cycleRelative;')
        mel.eval("selectKey -add -k -f -38.574463 -f 77.148926 %s;" % (self.hand_ik_jnt_name + "_translateX"))
        mel.eval('keyTangent -e -itt linear -ott linear;')
        mel.eval('setInfinity -poi cycleRelative;')

        # Create a Lbow Ctrl
        lbow_loc_name = self.prefix_name + "_" + self.side + "_lBow_" + str(self.val) + '_Loc'
        cmds.spaceLocator(n=lbow_loc_name, p=(self.ctrl_list[self.lbow_inner_ctrl]['Trans'][0],
                                              self.ctrl_list[self.lbow_inner_ctrl]['Trans'][1],
                                              self.ctrl_list[self.lbow_inner_ctrl]['Trans'][2]))
        # move -r -os -wd 0 0 -2.411616 ;
        cmds.move(0, 0, -3, r=True)
        cmds.select(lbow_loc_name)
        cmds.CenterPivot()
        cmds.select(lbow_loc_name)
        cmds.DeleteHistory()
        cmds.FreezeTransformations()

        cmds.select(lbow_loc_name, ik_handle_name)
        cmds.poleVectorConstraint()
        # setAttr "Template_L_lBow_1_Loc.translateY" -0.999;
        cmds.setAttr((lbow_loc_name + '.ty'), -0.999)
        self.controller_class.traiangle_new_ctrl()
        lbow_ctrl_name = self.prefix_name + "_" + self.side + "_lBow_" + str(self.val) + '_Ctrl'
        lbow_ctrl_grp_name = lbow_ctrl_name + '_Grp'
        cmds.rename('Triangle_new_ctrl', lbow_ctrl_name)
        cmds.select(lbow_ctrl_name)
        cmds.parentConstraint(lbow_loc_name, lbow_ctrl_name, mo=False)
        cmds.select(lbow_ctrl_name + '_parentConstraint1')
        cmds.delete()
        lbow_world_pos = cmds.getAttr(lbow_ctrl_name + '.t')[0]
        cmds.select(lbow_ctrl_name)
        cmds.DeleteHistory()
        cmds.FreezeTransformations()
        cmds.select(lbow_loc_name, lbow_ctrl_name)
        cmds.parent()
        cmds.select(lbow_ctrl_name)
        cmds.group(n=lbow_ctrl_grp_name)
        cmds.connectAttr((ik_fk_switch_name + '.IK_FK_Switch'), (lbow_ctrl_grp_name + '.v'))

        # CREATE A DIS BETWEEN THE SHOULDER AND THE HAND CONTROLLER
        upper_hand_to_hand_start_loc = self.prefix_name + "_" + self.side + "_Upper_Hand_to_lBow_" + str(
            self.val) + '_Start_Loc'
        upper_hand_to_hand_end_loc = self.prefix_name + "_" + self.side + "_Upper_Hand_to_lBow_" + str(
            self.val) + '_End_Loc'
        dimention_name = self.prefix_name + "_" + self.side + "_Upper_Hand_to_lBow_" + str(self.val) + '_Dis'
        upper_hand_to_lbow_dis_shape = dimention_name + 'Shape'
        cmds.spaceLocator(n=upper_hand_to_hand_start_loc, p=(self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][0],
                                                             self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][1],
                                                             self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][2]))
        cmds.spaceLocator(n=upper_hand_to_hand_end_loc, p=(lbow_world_pos[0],
                                                           lbow_world_pos[1],
                                                           lbow_world_pos[2]))
        cmds.select(upper_hand_to_hand_start_loc, upper_hand_to_hand_end_loc)
        cmds.distanceDimension()
        cmds.rename('distanceDimension1', dimention_name)
        cmds.select(upper_hand_to_hand_end_loc, lbow_ctrl_name)
        cmds.parent()

        upper_hand_to_hand_start_loc = self.prefix_name + "_" + self.side + "_lBow_to_Hand_" + str(
            self.val) + '_Start_Loc'
        upper_hand_to_hand_end_loc = self.prefix_name + "_" + self.side + "_lBow_to_Hand_" + str(self.val) + '_End_Loc'
        dimention_name = self.prefix_name + "_" + self.side + "_lBow_to_Hand_" + str(self.val) + '_Dis'
        lbow_to_hand_dis_shape = dimention_name + 'Shape'
        cmds.spaceLocator(n=upper_hand_to_hand_start_loc, p=(lbow_world_pos[0],
                                                             lbow_world_pos[1],
                                                             lbow_world_pos[2]))
        cmds.spaceLocator(n=upper_hand_to_hand_end_loc, p=(self.ctrl_list[self.hand_inner_ctrl]['Trans'][0],
                                                           self.ctrl_list[self.hand_inner_ctrl]['Trans'][1],
                                                           self.ctrl_list[self.hand_inner_ctrl]['Trans'][2]))
        cmds.select(upper_hand_to_hand_start_loc, upper_hand_to_hand_end_loc)
        cmds.distanceDimension()
        cmds.rename('distanceDimension1', dimention_name)
        cmds.select(upper_hand_to_hand_start_loc, lbow_ctrl_name)
        cmds.parent()
        cmds.select(upper_hand_to_hand_end_loc, hand_ctrl_name)
        cmds.parent()

        cmds.addAttr(lbow_ctrl_name, ln="lBow_Snap", at='double', min=0, max=1)
        cmds.setAttr((lbow_ctrl_name + ".lBow_Snap"), e=True, keyable=True)

        # blend witht he orignal and the snap
        blend_color_name = self.prefix_name + "_" + self.side + "_Upper_arm_Stretch_" + str(self.val) + '_Blend'
        cmds.createNode('blendColors', n=blend_color_name)
        cmds.connectAttr((upper_hand_to_lbow_dis_shape + '.distance'), (blend_color_name + '.color1.color1R'), f=True)
        cmds.connectAttr((self.lbow_ik_jnt_name + '_translateX.output'), (blend_color_name + '.color2R'), f=True)
        cmds.connectAttr((blend_color_name + '.outputR'), (self.lbow_ik_jnt_name + '.tx'), f=True)
        cmds.connectAttr((lbow_ctrl_name + '.lBow_Snap'), (blend_color_name + '.blender'), f=True)

        blend_color_name = self.prefix_name + "_" + self.side + "_lBow_Stretch_" + str(self.val) + '_Blend'
        cmds.createNode('blendColors', n=blend_color_name)
        cmds.connectAttr((lbow_to_hand_dis_shape + '.distance'), (blend_color_name + '.color1.color1R'), f=True)
        cmds.connectAttr((self.hand_ik_jnt_name + '_translateX.output'), (blend_color_name + '.color2R'), f=True)
        # Template_L_Arm_Hand_1_Ik_Jnt_translateX
        cmds.connectAttr((blend_color_name + '.outputR'), (self.hand_ik_jnt_name + '.tx'), f=True)
        cmds.connectAttr((lbow_ctrl_name + '.lBow_Snap'), (blend_color_name + '.blender'), f=True)

        # create a hybrid fk
        self.hybrid_lbow_common = self.prefix_name + "_" + self.side + "_Arm_lBow_HyBrid_Tem_" + str(self.val)
        self.hybrid_lbow_jnt = self.hybrid_lbow_common + '_Jnt'
        self.hybrid_hand_common = self.prefix_name + "_" + self.side + "_Arm_Hand_HyBrid_Tem_" + str(self.val)
        self.hybrid_hand_jnt = self.hybrid_hand_common + '_Jnt'

        cmds.joint(n=self.hybrid_lbow_jnt, p=(self.ctrl_list[self.lbow_inner_ctrl]['Trans'][0],
                                              self.ctrl_list[self.lbow_inner_ctrl]['Trans'][1],
                                              self.ctrl_list[self.lbow_inner_ctrl]['Trans'][2]))

        cmds.joint(n=self.hybrid_hand_jnt, p=(self.ctrl_list[self.hand_inner_ctrl]['Trans'][0],
                                              self.ctrl_list[self.hand_inner_ctrl]['Trans'][1],
                                              self.ctrl_list[self.hand_inner_ctrl]['Trans'][2]))

        cmds.select(self.hybrid_lbow_jnt)
        cmds.joint(e=True, oj='xyz', secondaryAxisOrient='xup', ch=True, zso=True)
        hybrid_list = [self.hybrid_lbow_jnt]
        for each in hybrid_list:
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
        cmds.select(self.hybrid_lbow_jnt)
        cmds.move(lbow_world_pos[0],
                  lbow_world_pos[1],
                  lbow_world_pos[2])

        cmds.select(self.hybrid_lbow_jnt, lbow_ctrl_name)
        cmds.parent()

        # get the children of the hand ctrl
        hand_children = cmds.listRelatives(hand_ctrl_name, children=True)
        hand_hybrid_grp_name = self.prefix_name + "_" + self.side + "_Hand_Hybrid_" + str(self.val) + '_Ctrl_Grp'

        hand_children.remove(hand_ctrl_name + 'Shape')
        hand_children.remove(hand_ctrl_name + 'Shape1')
        hand_children.remove(hand_ctrl_name + 'Shape2')
        hand_children.remove(hand_ctrl_name + 'Shape3')
        hand_children.remove(hand_ctrl_name + 'Shape4')
        hand_children.remove(hand_ctrl_name + 'Shape5')
        cmds.select(hand_children)
        cmds.group(n=hand_hybrid_grp_name)
        cmds.select(hand_hybrid_grp_name)
        mel.eval('parent -w;')

        # make a parent const to the object
        cmds.parentConstraint(hand_ctrl_name, hand_hybrid_grp_name, mo=True)
        cmds.parentConstraint(self.hybrid_hand_jnt, hand_hybrid_grp_name, mo=False)

        # set driven key
        cmds.setAttr((lbow_ctrl_name + '.lBow_Snap'), 0)
        cmds.setAttr((hand_hybrid_grp_name + '_parentConstraint1.' + self.hybrid_hand_jnt + 'W1'), 0)
        cmds.setAttr((hand_hybrid_grp_name + '_parentConstraint1.' + hand_ctrl_name + 'W0'), 1)
        cmds.setAttr((hand_ctrl_name + '.v'), 1)
        cmds.setAttr((self.hybrid_lbow_jnt + '.v'), 0)
        cmds.setDrivenKeyframe((hand_hybrid_grp_name + '_parentConstraint1.' + self.hybrid_hand_jnt + 'W1'),
                               currentDriver=(lbow_ctrl_name + '.lBow_Snap'))
        cmds.setDrivenKeyframe((hand_hybrid_grp_name + '_parentConstraint1.' + hand_ctrl_name + 'W0'),
                               currentDriver=(lbow_ctrl_name + '.lBow_Snap'))
        cmds.setDrivenKeyframe((hand_ctrl_name + '.v'), currentDriver=(lbow_ctrl_name + '.lBow_Snap'))
        cmds.setDrivenKeyframe((self.hybrid_lbow_jnt + '.v'), currentDriver=(lbow_ctrl_name + '.lBow_Snap'))

        cmds.setAttr((lbow_ctrl_name + '.lBow_Snap'), 1)
        cmds.setAttr((hand_hybrid_grp_name + '_parentConstraint1.' + self.hybrid_hand_jnt + 'W1'), 1)
        cmds.setAttr((hand_hybrid_grp_name + '_parentConstraint1.' + hand_ctrl_name + 'W0'), 0)
        cmds.setAttr((hand_ctrl_name + '.v'), 0)
        cmds.setAttr((self.hybrid_lbow_jnt + '.v'), 1)
        cmds.setDrivenKeyframe((hand_hybrid_grp_name + '_parentConstraint1.' + self.hybrid_hand_jnt + 'W1'),
                               currentDriver=(lbow_ctrl_name + '.lBow_Snap'))
        cmds.setDrivenKeyframe((hand_hybrid_grp_name + '_parentConstraint1.' + hand_ctrl_name + 'W0'),
                               currentDriver=(lbow_ctrl_name + '.lBow_Snap'))
        cmds.setDrivenKeyframe((hand_ctrl_name + '.v'), currentDriver=(lbow_ctrl_name + '.lBow_Snap'))
        cmds.setDrivenKeyframe((self.hybrid_lbow_jnt + '.v'), currentDriver=(lbow_ctrl_name + '.lBow_Snap'))
        cmds.setAttr((lbow_ctrl_name + '.lBow_Snap'), 0)

        # hide the unwanted object
        # list = [upper_hand_to_hand_start_loc,upper_hand_to_hand_end_loc]

        upper_hand_to_hand_start_loc = self.prefix_name + "_" + self.side + "_Upper_Hand_to_Hand_" + str(
            self.val) + '_Start_Loc'
        upper_hand_to_hand_end_loc = self.prefix_name + "_" + self.side + "_Upper_Hand_to_Hand_" + str(
            self.val) + '_End_Loc'
        upper_hand_to_hand_dis = self.prefix_name + "_" + self.side + "_Upper_Hand_to_Hand_" + str(self.val) + '_Dis'
        upper_hand_to_lbow_start_loc = self.prefix_name + "_" + self.side + "_Upper_Hand_to_lBow_" + str(
            self.val) + '_Start_Loc'
        upper_hand_to_lbow_end_loc = self.prefix_name + "_" + self.side + "_Upper_Hand_to_lBow_" + str(
            self.val) + '_End_Loc'
        upper_hand_to_lbow_dis = self.prefix_name + "_" + self.side + "_Upper_Hand_to_lBow_" + str(self.val) + '_Dis'
        lbow_to_hand_start_loc = self.prefix_name + "_" + self.side + "_lBow_to_Hand_" + str(self.val) + '_Start_Loc'
        lbow_to_hand_end_loc = self.prefix_name + "_" + self.side + "_lBow_to_Hand_" + str(self.val) + '_End_Loc'
        lbow_to_hand_dis = self.prefix_name + "_" + self.side + "_lBow_to_Hand_" + str(self.val) + '_Dis'
        list = [upper_hand_to_hand_start_loc, upper_hand_to_hand_end_loc, upper_hand_to_hand_dis,
                upper_hand_to_lbow_start_loc, upper_hand_to_lbow_end_loc,
                upper_hand_to_lbow_dis, lbow_to_hand_start_loc, lbow_to_hand_end_loc, lbow_to_hand_dis, lbow_loc_name]
        for each_obj in list:
            cmds.setAttr((each_obj + '.v'), 0)

        # put everything is in one group
        cmds.select(fk_jnt_grp_name, ik_jnt_grp_name, result_jnt_grp_name, ik_fk_switch_grp_name, hand_ctrl_grp_name,
                    upper_hand_to_hand_start_loc, upper_hand_to_hand_dis, lbow_ctrl_grp_name,
                    upper_hand_to_lbow_start_loc,
                    upper_hand_to_lbow_dis, lbow_to_hand_dis, hand_hybrid_grp_name)
        arm_grp_name = self.prefix_name + "_" + self.side + "_Arm_" + str(self.val) + '_Grp'
        cmds.group(n=arm_grp_name)
        cmds.select(arm_grp_name, root_grp_name)
        cmds.parent()

        arm_do_not_touch_grp_name = self.prefix_name + "_" + self.side + "_Arm_DO_NOT_TOUCH_" + str(self.val) + '_Grp'
        cmds.select(result_jnt_grp_name, ik_jnt_grp_name, upper_hand_to_hand_start_loc, upper_hand_to_hand_dis,
                    upper_hand_to_lbow_start_loc,
                    upper_hand_to_lbow_dis, lbow_to_hand_dis)
        cmds.group(n=arm_do_not_touch_grp_name)

        result_const_grp_name = self.upper_hand_result_jnt_name + '_Const_Grp'
        cmds.select(result_jnt_grp_name)
        cmds.group(n=result_const_grp_name)
        cmds.move(self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][0],
                  self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][1],
                  self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][2],
                  (result_const_grp_name + '.scalePivot'),
                  (result_const_grp_name + '.rotatePivot'))

        ik_const_grp_name = self.hand_ik_jnt_name + '_Const_Grp'
        cmds.select(ik_jnt_grp_name)
        cmds.group(n=ik_const_grp_name)
        cmds.move(self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][0],
                  self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][1],
                  self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][2],
                  (ik_const_grp_name + '.scalePivot'),
                  (ik_const_grp_name + '.rotatePivot'))

        fk_const_grp_name = self.hand_fk_jnt_name + '_Const_Grp'
        cmds.select(fk_jnt_grp_name)
        cmds.group(n=fk_const_grp_name)
        cmds.move(self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][0],
                  self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][1],
                  self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][2],
                  (fk_const_grp_name + '.scalePivot'),
                  (fk_const_grp_name + '.rotatePivot'))

        # Shoulder space Loc
        shoulder_arm_space_loc = self.prefix_name + "_" + self.side + "_Arm_Shoulder_Space_" + str(self.val) + '_Loc'
        cmds.spaceLocator(n=shoulder_arm_space_loc, p=(self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][0],
                                                       self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][1],
                                                       self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][2]))
        cmds.select(shoulder_arm_space_loc)
        cmds.CenterPivot()

        body_arm_space_loc = self.prefix_name + "_" + self.side + "_Arm_Body_Space_" + str(self.val) + '_Loc'
        cmds.spaceLocator(n=body_arm_space_loc, p=(self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][0],
                                                   self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][1],
                                                   self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][2]))
        cmds.select(body_arm_space_loc)
        cmds.CenterPivot()

        root_arm_space_loc = self.prefix_name + "_" + self.side + "_Arm_Root_Space_" + str(self.val) + '_Loc'
        cmds.spaceLocator(n=root_arm_space_loc, p=(self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][0],
                                                   self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][1],
                                                   self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][2]))
        cmds.select(root_arm_space_loc)
        cmds.CenterPivot()

        cmds.select(shoulder_arm_space_loc, body_arm_space_loc, root_arm_space_loc, root_grp_name)
        cmds.parent()
        cmds.pointConstraint(shoulder_arm_space_loc, result_const_grp_name, mo=True)
        cmds.pointConstraint(shoulder_arm_space_loc, ik_const_grp_name, mo=True)
        cmds.pointConstraint(shoulder_arm_space_loc, fk_const_grp_name, mo=True)

        # Create a Gimble controller
        test_circle_1_name = 'Test_1'
        cmds.circle(c=(0, 0, 0), nr=(0, 1, 0), sw=360, r=3, d=3, ut=0, tol=0.01, s=8, ch=0, n=test_circle_1_name)
        test_circle_2_name = 'Test_2'
        test_circle_2_shape_name = test_circle_2_name + 'Shape'
        cmds.circle(c=(0, 0, 0), nr=(0, 1, 0), sw=360, r=1, d=3, ut=0, tol=0.01, s=8, ch=0, n=test_circle_2_name)
        cmds.select(test_circle_2_name)
        cmds.move(0, 0, -3, r=True)
        cmds.select(test_circle_1_name, test_circle_2_name)
        cmds.DeleteHistory()
        mel.eval('makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;')

        cmds.select(test_circle_2_shape_name, test_circle_1_name)
        cmds.parent(r=True, s=True)
        cmds.select(test_circle_2_name)
        cmds.delete()

        gimble_name = self.prefix_name + "_" + self.side + "_Arm_Gimble_" + str(self.val) + '_Ctrl'
        cmds.rename(test_circle_1_name, gimble_name)
        cmds.select(gimble_name)
        cmds.move(self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][0],
                  self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][1],
                  self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][2])
        cmds.setAttr((gimble_name + '.rx'), 90)
        cmds.setAttr((gimble_name + '.ry'), 90)
        cmds.DeleteHistory()
        mel.eval('makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;')

        cmds.select(gimble_name, fk_jnt_grp_name)
        cmds.parent()
        cmds.select(self.upper_hand_fk_jnt_name, gimble_name)
        cmds.parent()
        cmds.select(self.upper_hand_result_jnt_name)

        reverse_name = ik_fk_switch_name + '_' + fk_jnt_list[0] + '_Reverse'
        cmds.connectAttr((reverse_name + '.outputX'), (gimble_name + '.v'), f=True)

        mel.eval('doGroup 0 0 1;')
        sel_obj = cmds.ls(sl=True)
        result_gimble_grp_name = self.prefix_name + "_" + self.side + "_Arm_Result_Gimble_" + str(self.val) + '_Grp'
        cmds.rename(sel_obj[0], result_gimble_grp_name)
        cmds.move(self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][0],
                  self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][1],
                  self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][2],
                  (result_gimble_grp_name + '.scalePivot'),
                  (result_gimble_grp_name + '.rotatePivot'))

        # Create a Blend Color name
        blend_color_name = self.prefix_name + "_" + self.side + "_Arm_Gimble_" + str(self.val) + '_Blend'
        cmds.createNode('blendColors', n=blend_color_name)
        cmds.connectAttr((gimble_name + '.r'), (blend_color_name + '.color2'), f=True)
        cmds.setAttr((blend_color_name + '.color1R'), 0)
        cmds.connectAttr((blend_color_name + '.output'), (result_gimble_grp_name + '.r'), f=True)
        cmds.connectAttr((ik_fk_switch_name + '.IK_FK_Switch'), (blend_color_name + '.blender'), f=True)

        # make a Rotate Const
        cmds.orientConstraint(shoulder_arm_space_loc, fk_const_grp_name)
        cmds.orientConstraint(body_arm_space_loc, fk_const_grp_name)
        cmds.orientConstraint(root_arm_space_loc, fk_const_grp_name)

        cmds.orientConstraint(shoulder_arm_space_loc, result_const_grp_name)
        cmds.orientConstraint(body_arm_space_loc, result_const_grp_name)
        cmds.orientConstraint(root_arm_space_loc, result_const_grp_name)

        cmds.addAttr(ik_fk_switch_name, ln="FK_Rotation_Space", at='enum', en='Shoulder:UpperBody:Root')
        cmds.setAttr((ik_fk_switch_name + ".FK_Rotation_Space"), e=True, keyable=True)

        cmds.setAttr((ik_fk_switch_name + ".FK_Rotation_Space"), 0)
        cmds.setAttr((fk_const_grp_name + "_orientConstraint1." + shoulder_arm_space_loc + 'W0'), 1)
        cmds.setAttr((fk_const_grp_name + "_orientConstraint1." + body_arm_space_loc + 'W1'), 0)
        cmds.setAttr((fk_const_grp_name + "_orientConstraint1." + root_arm_space_loc + 'W2'), 0)
        cmds.setAttr((result_const_grp_name + "_orientConstraint1." + shoulder_arm_space_loc + 'W0'), 1)
        cmds.setAttr((result_const_grp_name + "_orientConstraint1." + body_arm_space_loc + 'W1'), 0)
        cmds.setAttr((result_const_grp_name + "_orientConstraint1." + root_arm_space_loc + 'W2'), 0)
        cmds.setDrivenKeyframe((fk_const_grp_name + "_orientConstraint1." + shoulder_arm_space_loc + 'W0'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))
        cmds.setDrivenKeyframe((fk_const_grp_name + "_orientConstraint1." + body_arm_space_loc + 'W1'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))
        cmds.setDrivenKeyframe((fk_const_grp_name + "_orientConstraint1." + root_arm_space_loc + 'W2'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))
        cmds.setDrivenKeyframe((result_const_grp_name + "_orientConstraint1." + shoulder_arm_space_loc + 'W0'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))
        cmds.setDrivenKeyframe((result_const_grp_name + "_orientConstraint1." + body_arm_space_loc + 'W1'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))
        cmds.setDrivenKeyframe((result_const_grp_name + "_orientConstraint1." + root_arm_space_loc + 'W2'),
                               currentDriver=(ik_fk_switch_name + ".FK_Rotation_Space"))

        blend_color_name = self.prefix_name + "_" + self.side + "_Arm_Result_Orient_" + str(self.val) + '_Blend'
        cmds.createNode('blendColors', n=blend_color_name)
        cmds.connectAttr((result_const_grp_name + '_orientConstraint1.constraintRotate'),
                         (blend_color_name + '.color2'), f=True)
        cmds.setAttr((blend_color_name + '.color1R'), 0)
        cmds.connectAttr((ik_fk_switch_name + '.IK_FK_Switch'), (blend_color_name + '.blender'), f=True)
        cmds.connectAttr((blend_color_name + '.output'), (result_const_grp_name + '.r'), f=True)

        #######################################################SHOULDER
        cmds.select(cl=True)
        # CREATE A SHOULDER
        # Template_L_Arm_Shoulder_Tem_1_Inner_Ctrl
        self.shoulder_common = self.prefix_name + "_" + self.side + "_Arm_Shoulder_Tem_" + str(self.val)
        self.shoulder_inner_ctrl, self.shoulder_jnt_name, self.shoulder_fk_jnt_name, self.shoulder_ik_jnt_name, \
        self.shoulder_result_jnt_name = self.get_data_variable(self.shoulder_common)

        # Create a joint
        cmds.joint(n=self.shoulder_jnt_name, p=(self.ctrl_list[self.shoulder_inner_ctrl]['Trans'][0],
                                                self.ctrl_list[self.shoulder_inner_ctrl]['Trans'][1],
                                                self.ctrl_list[self.shoulder_inner_ctrl]['Trans'][2]))
        shoulder_end_jnt_name = self.upper_hand_jnt_name.replace('Upper_Hand', 'Shoulder_End_Jnt')
        cmds.joint(n=shoulder_end_jnt_name, p=(self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][0],
                                               self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][1],
                                               self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][2]))
        cmds.select(self.shoulder_jnt_name)
        cmds.joint(e=True, oj='xyz', secondaryAxisOrient='xup', ch=True, zso=True)
        shoulder_ik_handle = self.prefix_name + "_" + self.side + "_Shoulder_" + str(self.val) + '_IK_Handle'
        cmds.ikHandle(n=shoulder_ik_handle,
                      sj=self.shoulder_jnt_name,
                      ee=shoulder_end_jnt_name,
                      sol='ikSCsolver')
        shoulder_loc_name = self.prefix_name + "_" + self.side + "_Shoulder_" + str(self.val) + '_Loc'
        cmds.spaceLocator(n=shoulder_loc_name, p=(self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][0],
                                                  self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][1],
                                                  self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][2]))
        cmds.select(shoulder_loc_name)
        cmds.CenterPivot()
        cmds.select(shoulder_ik_handle, shoulder_loc_name)
        cmds.parent()

        shoulder_dis_start_loc = self.prefix_name + "_" + self.side + "_Shoulder_" + str(self.val) + '_Start_Loc'
        shoulder_dis_end_loc = self.prefix_name + "_" + self.side + "_Shoulder_" + str(self.val) + '_End_Loc'
        shoulder_dis = self.prefix_name + "_" + self.side + "_Shoulder_" + str(self.val) + '_Dis'
        shoulder_dis_shape = shoulder_dis + 'Shape'
        cmds.spaceLocator(n=shoulder_dis_start_loc, p=(self.ctrl_list[self.shoulder_inner_ctrl]['Trans'][0],
                                                       self.ctrl_list[self.shoulder_inner_ctrl]['Trans'][1],
                                                       self.ctrl_list[self.shoulder_inner_ctrl]['Trans'][2]))
        cmds.spaceLocator(n=shoulder_dis_end_loc, p=(self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][0],
                                                     self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][1],
                                                     self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][2]))
        cmds.select(shoulder_dis_start_loc, shoulder_dis_end_loc)
        cmds.distanceDimension()
        cmds.rename('distanceDimension1', shoulder_dis)
        cmds.select(shoulder_dis_end_loc, shoulder_loc_name)
        cmds.parent()

        # Stretch
        driver = shoulder_dis_shape + '.distance'
        length = cmds.getAttr(shoulder_end_jnt_name + '.tx')
        cmds.setDrivenKeyframe(shoulder_end_jnt_name, currentDriver=driver, driverValue=length, attribute='tx',
                               value=length)
        cmds.setDrivenKeyframe(shoulder_end_jnt_name, currentDriver=driver, driverValue=length * 2, attribute='tx',
                               value=length * 2)

        # selectKey -add -k -f 5.830952 -f 11.661903 Template_L_Arm_Shoulder_End_Jnt_Tem_1_Jnt_translateX ;
        mel.eval("selectKey -add -k -f 5.830952 -f 11.661903 %s;" % (shoulder_end_jnt_name + "_translateX"))
        mel.eval('keyTangent -e -itt linear -ott linear;')
        mel.eval('setInfinity -poi cycleRelative;')

        # Create a shoulder ctrl
        self.controller_class.traiangle_new_ctrl()
        shoulder_ctrl_name = self.prefix_name + "_" + self.side + "_Shoulder_" + str(self.val) + '_Ctrl'
        shoulder_ctrl_grp_name = shoulder_ctrl_name + '_Grp'
        cmds.rename('Triangle_new_ctrl', shoulder_ctrl_name)
        cmds.select(shoulder_ctrl_name)
        cmds.move(self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][0],
                  self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][1],
                  self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][2])
        # move -r -os -wd 0 6.748391 0 ;
        cmds.move(0, 6, 0, r=True)
        cmds.select(shoulder_ctrl_name)
        cmds.DeleteHistory()
        cmds.FreezeTransformations()
        cmds.select(shoulder_loc_name, shoulder_ctrl_name)
        cmds.parent()
        cmds.move(self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][0],
                  self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][1],
                  self.ctrl_list[self.upper_hand_inner_ctrl]['Trans'][2],
                  (shoulder_ctrl_name + '.scalePivot'),
                  (shoulder_ctrl_name + '.rotatePivot'))

        # Create a Shoulder Vis
        cmds.addAttr(ik_fk_switch_name, ln="Shoulder_Vis", at='enum', en='Off:On')
        cmds.setAttr((ik_fk_switch_name + ".Shoulder_Vis"), e=True, keyable=True)
        cmds.connectAttr((ik_fk_switch_name + '.Shoulder_Vis'), (shoulder_ctrl_name + '.v'))

        # Hide all the unwanted
        list = [shoulder_dis_start_loc, shoulder_dis, shoulder_dis_end_loc, shoulder_ik_handle, shoulder_loc_name]
        for object in list:
            cmds.setAttr((object + '.v'), 0)

        # make a shoulder Grp
        cmds.select(self.shoulder_jnt_name, shoulder_dis_start_loc, shoulder_dis, shoulder_ctrl_name)
        shoulder_grp_name = self.prefix_name + "_" + self.side + "_Shoulder_" + str(self.val) + '_Grp'
        cmds.group(n=shoulder_grp_name)

        cmds.select(shoulder_grp_name, root_grp_name)
        cmds.parent()

        shoulder_do_not_touch_grp = self.prefix_name + "_" + self.side + "_Shoulder_Do_NOT_TOUCH_" + str(
            self.val) + '_Grp'
        cmds.select(shoulder_dis, shoulder_dis_start_loc, self.shoulder_jnt_name)
        cmds.group(n=shoulder_do_not_touch_grp)

        # Connecth the loc
        shoulder_main_loc = self.prefix_name + "_" + self.side + "_Shoulder_to_Body_" + str(self.val) + '_Loc'
        cmds.spaceLocator(n=shoulder_main_loc, p=(self.ctrl_list[self.shoulder_inner_ctrl]['Trans'][0],
                                                  self.ctrl_list[self.shoulder_inner_ctrl]['Trans'][1],
                                                  self.ctrl_list[self.shoulder_inner_ctrl]['Trans'][2]))
        cmds.select(shoulder_main_loc)
        cmds.CenterPivot()
        cmds.select(shoulder_main_loc, root_grp_name)
        cmds.parent()
        cmds.parentConstraint(shoulder_main_loc, shoulder_grp_name, mo=True)

        # Hide unwanted object
        transform_object = [gimble_name, self.upper_hand_fk_jnt_name, self.lbow_fk_jnt_name, self.hand_fk_jnt_name,
                            ik_fk_switch_name, self.hybrid_lbow_jnt,
                            self.hybrid_hand_jnt]
        for each_obj in transform_object:
            self.helper_class.transform_rotation_scale_visible(each_obj, t=True, r=False, s=False)
        rotate_object = [ik_fk_switch_name, shoulder_ctrl_name, lbow_ctrl_name, hand_ctrl_name]
        for each_obj in rotate_object:
            self.helper_class.transform_rotation_scale_visible(each_obj, t=False, r=True, s=False)
        scale_object = [gimble_name, self.upper_hand_fk_jnt_name, self.lbow_fk_jnt_name, self.hand_fk_jnt_name,
                        shoulder_ctrl_name,
                        lbow_ctrl_name, hand_ctrl_name]
        for each_obj in scale_object:
            self.helper_class.transform_rotation_scale_visible(each_obj, t=False, r=False, s=True)

        # Create a Mult and Div
        mult_div_name = self.prefix_name + "_" + self.side + "_Arm_Root_" + str(self.val) + '_Mult'
        arm_upper_hand_to_hand_dis = self.prefix_name + "_" + self.side + "_Upper_Hand_to_Hand_" + str(
            self.val) + '_Dis'
        arm_upper_hand_to_hand_dis_shape = arm_upper_hand_to_hand_dis + 'Shape'
        cmds.createNode('multiplyDivide', n=mult_div_name)
        cmds.connectAttr((arm_upper_hand_to_hand_dis_shape + '.distance'), (mult_div_name + '.input1X'), f=True)
        cmds.connectAttr((root_grp_name + '.sx'), (mult_div_name + '.input2X'), f=True)
        # setAttr "Template_L_Arm_Root_1_Mult.operation" 2;
        cmds.setAttr((mult_div_name + '.operation'), 2)
        cmds.connectAttr((mult_div_name + '.output.outputX'), (self.hand_ik_jnt_name + '_translateX.input'), f=True)
        cmds.connectAttr((mult_div_name + '.output.outputX'), (self.lbow_ik_jnt_name + '_translateX.input'), f=True)

        # Create a Finger
        self.create_finger()

    def create_finger(self):
        # Create a hand joint
        # Character_L_Hand_Base_Ctrl
        hand_jnt_name = self.prefix_name + "_" + self.side + "_Hand_Base_Tem_" + str(self.val) + '_Result_Jnt'
        cmds.select(cl=True)
        cmds.joint(n=hand_jnt_name, p=(self.ctrl_list[self.hand_inner_ctrl]['Trans'][0],
                                       self.ctrl_list[self.hand_inner_ctrl]['Trans'][1],
                                       self.ctrl_list[self.hand_inner_ctrl]['Trans'][2]))

        hand_new_jnt_name = self.prefix_name + "_" + self.side + "_Hand_Base_Tem_" + str(self.val) + '_Ctrl_Jnt'
        cmds.select(cl=True)
        cmds.joint(n=hand_new_jnt_name, p=(self.ctrl_list[self.hand_inner_ctrl]['Trans'][0],
                                           self.ctrl_list[self.hand_inner_ctrl]['Trans'][1],
                                           self.ctrl_list[self.hand_inner_ctrl]['Trans'][2]))

        # Template_L_Arm_Finger_1_1_Tem_1_Inner_Ctrl
        finger_innner_ctrl = self.prefix_name + "_" + self.side + "_Arm_Finger_*_1_Tem_" + str(self.val) + '_Inner_Ctrl'
        cmds.select(finger_innner_ctrl)
        sel_obj = cmds.ls(sl=True)
        finger_list = []
        result_jnt_list = []
        ctrl_jnt_list = []
        a = 1
        for each in sel_obj:
            finger_list_name = self.prefix_name + "_" + self.side + '_Arm_Finger_' + str(a) + '_*_Tem_' + str(
                self.val) + '_Inner_Ctrl'
            cmds.select(finger_list_name)
            sel_finger = cmds.ls(sl=True)
            b = 0
            for each_finger in sel_finger:
                # get the position of the finger
                pos_finger = cmds.xform(each_finger, q=1, ws=1, rp=1)
                split_name = each_finger.split('_Inner_Ctrl')[0]
                result_jnt_name = split_name + '_Result_Jnt'
                result_jnt_list.append(result_jnt_name)
                ctrl_name = split_name + '_Ctrl'
                ctrl_shape_name = ctrl_name + 'Shape'
                component_jnt_name = split_name + '_Componente_Jnt'
                result_jnt_list.append(component_jnt_name)
                cmds.select(cl=True)
                cmds.joint(n=component_jnt_name, p=(pos_finger[0],
                                                    pos_finger[1],
                                                    pos_finger[2]))
                cmds.setAttr((component_jnt_name + '.rotateOrder'), 5)

                cmds.joint(n=result_jnt_name, p=(pos_finger[0],
                                                 pos_finger[1],
                                                 pos_finger[2]))
                cmds.setAttr((result_jnt_name + '.rotateOrder'), 5)

                #####
                fk_jnt_name = split_name + '_FK_Jnt'
                ctrl_jnt_list.append(fk_jnt_name)
                orient_jnt_name = split_name + '_Orient_Jnt'
                ctrl_jnt_list.append(orient_jnt_name)

                cmds.select(cl=True)
                cmds.joint(n=orient_jnt_name, p=(pos_finger[0],
                                                 pos_finger[1],
                                                 pos_finger[2]))
                cmds.setAttr((orient_jnt_name + '.rotateOrder'), 5)

                cmds.joint(n=fk_jnt_name, p=(pos_finger[0],
                                             pos_finger[1],
                                             pos_finger[2]))
                cmds.setAttr((fk_jnt_name + '.rotateOrder'), 5)

                # Create a Controller and snap to the result jnt
                self.controller_class.circle_ctrl()
                cmds.rename('circle_ctrl', ctrl_name)
                cmds.select(ctrl_shape_name, fk_jnt_name)
                cmds.parent(r=True, s=True)
                cmds.select(ctrl_name)
                cmds.delete()

                if b > 0:
                    previous_split_name = sel_finger[b - 1].split('_Inner_Ctrl')[0]
                    previous_jnt_name = previous_split_name + '_Result_Jnt'
                    cmds.select(component_jnt_name, previous_jnt_name)
                    cmds.parent()

                    previous_jnt_name = previous_split_name + '_FK_Jnt'
                    cmds.select(orient_jnt_name, previous_jnt_name)
                    cmds.parent()

                if b == 0:
                    cmds.select(component_jnt_name, hand_jnt_name)
                    cmds.parent()

                    cmds.select(orient_jnt_name, hand_new_jnt_name)
                    cmds.parent()

                    # create a Ik Joint
                    component_start_jnt_name = split_name + '_Componente_Start_Jnt'
                    cmds.select(cl=True)
                    cmds.joint(n=component_start_jnt_name, p=(pos_finger[0], pos_finger[1], pos_finger[2]))

                    cmds.select(component_start_jnt_name, hand_new_jnt_name)
                    cmds.parent()

                # Create a Finger  cointroller and set the position
                if a == 2 and b == 1:
                    middle_pos = pos_finger

                if b + 1 == len(sel_finger):
                    # Create a Finger  cointroller and set the position
                    finger_ctrl_name = split_name + '_Finger_Ctrl'
                    finger_list.append(finger_ctrl_name)
                    self.controller_class.finger_indi_ctrl()
                    cmds.rename('Finger_Indi', finger_ctrl_name)
                    cmds.move(pos_finger[0], pos_finger[1], pos_finger[2])
                    if self.side == 'L':
                        cmds.move(14, 0, 0, r=True)
                    else:
                        cmds.move(-14, 0, 0, r=True)
                    cmds.move(self.ctrl_list[self.hand_inner_ctrl]['Trans'][0],
                              self.ctrl_list[self.hand_inner_ctrl]['Trans'][1],
                              self.ctrl_list[self.hand_inner_ctrl]['Trans'][2],
                              (finger_ctrl_name + '.scalePivot'),
                              (finger_ctrl_name + '.rotatePivot'))

                    cmds.select(finger_ctrl_name)
                    cmds.DeleteHistory()
                    cmds.FreezeTransformations()

                    # lock and hide transform rotate scale attr
                    self.helper_class.transform_rotation_scale_visible(finger_ctrl_name, t=True,
                                                                       r=True,
                                                                       s=True)

                    attr_list = ['Length', 'Curl', 'Scrunch', 'Lean', 'Relax']
                    for each in attr_list:
                        cmds.addAttr(finger_ctrl_name, ln=each, at='double', min=-10, max=10)
                        cmds.setAttr((finger_ctrl_name + "." + each), e=True, keyable=True)
                    if a == 1:
                        first_pos = pos_finger

                    if a == len(sel_obj):
                        last_pos = pos_finger

                    # create a Ik Joint
                    component_end_jnt_name = split_name + '_Componente_End_Jnt'
                    cmds.select(cl=True)
                    cmds.joint(n=component_end_jnt_name, p=(pos_finger[0], pos_finger[1], pos_finger[2]))
                    cmds.select(component_end_jnt_name, component_start_jnt_name)
                    cmds.parent()
                    cmds.select(component_start_jnt_name)
                    mel.eval('makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1 -jointOrient;')

                b += 1

            a += 1

        cmds.select(hand_jnt_name, hand_new_jnt_name)
        mel.eval('joint -e  -oj xyz -secondaryAxisOrient ydown -ch -zso;')
        cmds.setAttr((hand_jnt_name + '.v'), 0)

        a = 1
        for each in sel_obj:
            # Template_L_Arm_Finger_1_1_Tem_1_Componente_Start_Jnt
            # Template_L_Arm_Finger_1_5_Tem_1_Componente_End_Jnt
            common = self.prefix_name + "_" + self.side + '_Arm_Finger_' + str(a) + '_1_Tem_' + str(self.val)
            component_start_jnt_name = self.prefix_name + "_" + self.side + '_Arm_Finger_' + str(a) + '_1_Tem_' + str(
                self.val) + '_Componente_Start_Jnt'
            component_end_jnt_name = self.prefix_name + "_" + self.side + '_Arm_Finger_' + str(a) + '_5_Tem_' + str(
                self.val) + '_Componente_End_Jnt'
            component_ik_handle_name = common + '_Ik_Handle'
            cmds.ikHandle(n=component_ik_handle_name,
                          sj=component_start_jnt_name,
                          ee=component_end_jnt_name,
                          sol='ikSCsolver')

            handle_name = self.prefix_name + "_" + self.side + "_Arm_Component_Tem_" + str(self.val) + '_Handle_Grp'
            if cmds.objExists(handle_name):
                cmds.select(component_ik_handle_name, handle_name)
                cmds.parent()
            else:
                cmds.select(component_ik_handle_name)
                cmds.group(n=handle_name)

            # Template_L_Arm_Finger_1_1_Tem_1_Orient_Jnt
            orient_jnt = self.prefix_name + "_" + self.side + '_Arm_Finger_' + str(a) + '_1_Tem_' + str(
                self.val) + '_Orient_Jnt'
            cmds.select(orient_jnt, component_start_jnt_name)
            cmds.parent()

            a += 1

        a = 0
        while a < len(result_jnt_list):
            cmds.connectAttr((ctrl_jnt_list[a] + '.t'), (result_jnt_list[a] + '.t'))
            cmds.connectAttr((ctrl_jnt_list[a] + '.r'), (result_jnt_list[a] + '.r'))
            cmds.connectAttr((ctrl_jnt_list[a] + '.s'), (result_jnt_list[a] + '.s'))
            a += 1

        # Create a Hand Controller
        self.controller_class.hand_center_ctrl()
        hand_ctrl_name = self.prefix_name + "_" + self.side + '_Arm_Hand_Tem_' + str(self.val) + '_Center_Ctrl'
        cmds.rename('Hand_Center', hand_ctrl_name)
        cmds.move(pos_finger[0], pos_finger[1], self.ctrl_list[self.hand_inner_ctrl]['Trans'][2])
        if self.side == 'L':
            cmds.move(7, 0, 0, r=True)
        else:
            cmds.setAttr((hand_ctrl_name + '.sx'), -1)
            cmds.move(-7, 0, 0, r=True)
        cmds.move(self.ctrl_list[self.hand_inner_ctrl]['Trans'][0],
                  self.ctrl_list[self.hand_inner_ctrl]['Trans'][1],
                  self.ctrl_list[self.hand_inner_ctrl]['Trans'][2],
                  (hand_ctrl_name + '.scalePivot'),
                  (hand_ctrl_name + '.rotatePivot'))
        # move -rpr 54 1 2.8122e-008 Template_L_Arm_Hand_Tem_1_Center_Ctrl.scalePivot Template_L_Arm_Hand_Tem_1_Center_Ctrl.rotatePivot ;
        # addAttr
        attr_list = ['Curl', 'Scrunch', 'Lean', 'Relax', 'Spread', 'fist', 'PalmRaise', 'SideRoll']
        for each in attr_list:
            cmds.addAttr(hand_ctrl_name, ln=each, at='double', min=-10, max=10)
            cmds.setAttr((hand_ctrl_name + "." + each), e=True, keyable=True)

        cmds.select(hand_ctrl_name)
        cmds.DeleteHistory()
        cmds.FreezeTransformations()

        for each in finger_list:
            cmds.select(each, hand_ctrl_name)
            cmds.parent()

        cmds.connectAttr((hand_new_jnt_name + '.t'), (hand_jnt_name + '.t'))
        cmds.connectAttr((hand_new_jnt_name + '.r'), (hand_jnt_name + '.r'))
        self.helper_class.transform_rotation_scale_visible(hand_ctrl_name, t=True, r=True, s=True)

        # Create Inside Outside Middle pivot
        inner_loc_name = self.prefix_name + "_" + self.side + '_Arm_Inner_Tem_' + str(self.val) + '_Loc'
        outer_loc_name = self.prefix_name + "_" + self.side + '_Arm_Outer_Tem_' + str(self.val) + '_Loc'
        middle_loc_name = self.prefix_name + "_" + self.side + '_Arm_Middle_Tem_' + str(self.val) + '_Loc'

        cmds.spaceLocator(n=inner_loc_name, p=(first_pos[0], first_pos[1], first_pos[2]))
        cmds.select(inner_loc_name)
        cmds.CenterPivot()
        cmds.DeleteHistory()
        cmds.FreezeTransformations()

        cmds.spaceLocator(n=outer_loc_name, p=(last_pos[0], last_pos[1], last_pos[2]))
        cmds.select(outer_loc_name)
        cmds.CenterPivot()
        cmds.DeleteHistory()
        cmds.FreezeTransformations()

        cmds.spaceLocator(n=middle_loc_name, p=(middle_pos[0], middle_pos[1], middle_pos[2]))
        cmds.select(middle_loc_name)
        cmds.CenterPivot()
        cmds.DeleteHistory()
        cmds.FreezeTransformations()

        cmds.select(outer_loc_name, inner_loc_name)
        cmds.parent()
        cmds.select(middle_loc_name, outer_loc_name)
        cmds.parent()

        middle_const_jnt = self.prefix_name + "_" + self.side + "_Hand_Middle_Const_Tem_" + str(self.val) + '_Jnt'
        cmds.select(cl=True)
        cmds.joint(n=middle_const_jnt, p=(self.ctrl_list[self.hand_inner_ctrl]['Trans'][0],
                                          self.ctrl_list[self.hand_inner_ctrl]['Trans'][1],
                                          self.ctrl_list[self.hand_inner_ctrl]['Trans'][2]))
        cmds.select(middle_const_jnt, middle_loc_name)
        cmds.parent()

        cmds.parentConstraint(middle_const_jnt, hand_new_jnt_name, mo=True)
        cmds.setAttr((inner_loc_name + '.v'), 0)
        cmds.setAttr((handle_name + '.v'), 0)

        # Group all the object
        cmds.select(inner_loc_name, handle_name, hand_jnt_name, hand_new_jnt_name, hand_ctrl_name)
        hand_grp_name = self.prefix_name + "_" + self.side + "_Hand_Tem_" + str(self.val) + '_Grp'
        cmds.group(n=hand_grp_name)

        cmds.select(hand_grp_name, self.root_grp_name)
        cmds.parent()

        do_not_touch_grp = self.prefix_name + "_" + self.side + "_Hand_DO_NOT_TOUCH_Tem_" + str(self.val) + '_Grp'
        cmds.select(handle_name, inner_loc_name, hand_jnt_name, hand_ctrl_name)
        cmds.group(n=do_not_touch_grp)

        hand_const_grp_name = self.prefix_name + "_" + self.side + "_Hand_Const_Tem_" + str(self.val) + '_Grp'
        cmds.select(inner_loc_name, handle_name, hand_ctrl_name)
        cmds.group(n=hand_const_grp_name)
        cmds.move(self.ctrl_list[self.hand_inner_ctrl]['Trans'][0],
                  self.ctrl_list[self.hand_inner_ctrl]['Trans'][1],
                  self.ctrl_list[self.hand_inner_ctrl]['Trans'][2],
                  (hand_const_grp_name + '.scalePivot'),
                  (hand_const_grp_name + '.rotatePivot'))

        # now Create a Loc and parent const
        hand_const_loc = self.prefix_name + "_" + self.side + "_Hand_Const_" + str(self.val) + '_Loc'
        cmds.spaceLocator(n=hand_const_loc, p=(self.ctrl_list[self.hand_inner_ctrl]['Trans'][0],
                                               self.ctrl_list[self.hand_inner_ctrl]['Trans'][1],
                                               self.ctrl_list[self.hand_inner_ctrl]['Trans'][2]))
        cmds.CenterPivot()
        cmds.parentConstraint(hand_const_loc, hand_const_grp_name, mo=True)
        cmds.select(hand_const_loc, self.root_grp_name)
        cmds.parent()

    def arm_testing_def(self):
        print('This is arm testing Def')

    def bone_def(self):
        # get the no of the human main grp
        self.grp_list = ['Arm_Grp']
        for each_grp in self.grp_list:
            # list of the all children
            if cmds.objExists(each_grp):
                children_list = cmds.listRelatives(each_grp, children=True)
                for each_child in children_list:
                    # get all the controller data
                    self.arm_data(each_child)

                    self.final_bone_arm()

    def final_bone_arm(self):
        grp_namne = self.prefix_name + '_' + self.side + '_Arm_' + str(self.val) + '_Bone_Grp'
        main_grp_name = 'Arm_Bone_Grp'

        list = [self.upper_hand_common, self.lbow_common, self.hand_common, self.shoulder_common]
        for each in list:
            ctrl_name = each + '_Outer_Ctrl'
            bone_name = each + '_Bone'
            get_pos = cmds.xform(ctrl_name, q=1, ws=1, rp=1)
            cmds.select(cl=True)
            cmds.joint(n=bone_name, p=(get_pos[0], get_pos[1], get_pos[2]))

        # Template_L_Arm_Finger_1_1_Tem_1_Outer_Ctrl
        finger_list = self.prefix_name + "_" + self.side + "_Arm_Finger_*_1_Tem_" + str(self.val) + '_Outer_Ctrl'
        cmds.select(finger_list)
        sel_finger = cmds.ls(sl=True)
        a = 0
        while a < len(sel_finger):
            finger_name_list = self.prefix_name + "_" + self.side + '_Arm_Finger_' + str(a + 1) + '_*_Tem_' + str(
                self.val) + '_Outer_Ctrl'
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
                    hand_bone_jnt = self.hand_common + '_Bone'
                    cmds.parent(bone_name, hand_bone_jnt)
                else:
                    split_name = sel_finger_new[b - 1].split('_Outer_Ctrl')[0]
                    previous_jnt = split_name + '_Bone'
                    cmds.parent(bone_name, previous_jnt)

                b += 1
            a += 1

        shoulder_jnt = self.shoulder_common + '_Bone'
        upper_jnt = self.upper_hand_common + '_Bone'
        lbow_jnt = self.lbow_common + '_Bone'
        hand_jnt = self.hand_common + '_Bone'

        cmds.parent(hand_jnt, lbow_jnt)
        cmds.parent(lbow_jnt, upper_jnt)
        cmds.parent(upper_jnt, shoulder_jnt)

        # put everything in one grp
        self.helper_class.grp_create(object_name=shoulder_jnt,
                                     grp_name=grp_namne)

        self.helper_class.grp_create(object_name=grp_namne,
                                     grp_name=main_grp_name)

    def controller_twick_def(self):
        # get the no of the human main grp
        self.grp_list = ['Arm_Grp']
        for each_grp in self.grp_list:
            # list of the all children
            if cmds.objExists(each_grp):
                children_list = cmds.listRelatives(each_grp, children=True)
                for each_child in children_list:
                    # get all the controller data
                    self.arm_data(each_child)

                    self.final_controller_def()

    def final_controller_def(self):
        # Create a Fk Controller
        grp_name = self.prefix_name + "_" + self.side + "_Arm_" + str(self.val) + '_Twick_Ctrl_Grp'
        main_grp_name = 'Arm_Twick_Ctrl_Grp'

        list = [self.upper_hand_common, self.shoulder_common, self.lbow_common, self.hand_common]
        for each in list:
            ctrl_name = each + '_Outer_Ctrl'
            twick_ctrl = each + '_Twick_Ctrl'

            get_pos = cmds.xform(ctrl_name, q=1, ws=1, rp=1)
            get_rot = cmds.xform(ctrl_name, q=1, rotation=1)
            self.controller_class.circle_ctrl()
            cmds.rename('circle_ctrl', twick_ctrl)
            cmds.setAttr((twick_ctrl + '.rz'), 90)
            cmds.DeleteHistory()
            cmds.FreezeTransformations()

            cmds.setAttr((twick_ctrl + '.tx'), get_pos[0])
            cmds.setAttr((twick_ctrl + '.ty'), get_pos[1])
            cmds.setAttr((twick_ctrl + '.tz'), get_pos[2])

            cmds.setAttr((twick_ctrl + '.rx'), get_rot[0])
            cmds.setAttr((twick_ctrl + '.ry'), get_rot[1])
            cmds.setAttr((twick_ctrl + '.rz'), get_rot[2])

            if self.side == 'L':
                col = 'Blue'
            else:
                col = 'Red'

            self.helper_class.color_val(color=col,
                                        obj_name=twick_ctrl)

            self.helper_class.grp_create(object_name=twick_ctrl,
                                         grp_name=grp_name)

        hand_ctrl_name = self.hand_common + '_Inner_Ctrl'
        get_pos = cmds.xform(hand_ctrl_name, q=1, ws=1, rp=1)
        get_rot = cmds.xform(hand_ctrl_name, q=1, rotation=1)

        self.controller_class.hand_ctrl()
        hand_twick_ik_ctrl = self.hand_common + '_Ik_Twick_Ctrl'
        cmds.select('hand_ctrl')
        sel_obj = cmds.ls(sl=True)
        cmds.rename(sel_obj[0], hand_twick_ik_ctrl)

        cmds.move(get_pos[0], get_pos[1], get_pos[2])
        self.helper_class.color_val(color=col,
                                    obj_name=hand_twick_ik_ctrl)
        self.helper_class.grp_create(object_name=hand_twick_ik_ctrl,
                                     grp_name=grp_name)

        finger_list = self.prefix_name + "_" + self.side + "_Arm_Finger_*_1_Tem_" + str(self.val) + '_Outer_Ctrl'
        cmds.select(finger_list)
        sel_finger = cmds.ls(sl=True)
        a = 0
        while a < len(sel_finger):
            finger_name_list = self.prefix_name + "_" + self.side + '_Arm_Finger_' + str(a + 1) + '_*_Tem_' + str(
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

        pass

    def get_arm(self):
        list = []
        # get the no of the human main grp
        self.grp_list = ['Arm_Grp']
        for each_grp in self.grp_list:
            # list of the all children
            if cmds.objExists(each_grp):
                children_list = cmds.listRelatives(each_grp, children=True)
                for each_child in children_list:
                    # get all the controller data
                    list.append(each_child)

        return len(list)




















