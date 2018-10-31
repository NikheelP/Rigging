
class SPINE:
    def __init__(self):
        self.helper_class = helper.HELPER()
        self.controller_class = controller_rig.controler()

    def new(self ,widget ,layout):
        self.spine_grid_layout = QtGui.QGridLayout()
        self.spine_grid_layout.setObjectName("spine_grid_layout")

        # TYPE
        self.spine_type_combo_box = QtGui.QComboBox(widget)
        self.spine_type_combo_box.setObjectName("spine_type_combo_box")
        self.spine_type_combo_box.addItem("Human")
        self.spine_type_combo_box.addItem("Animal")
        self.spine_type_combo_box.addItem("Bird")
        self.spine_grid_layout.addWidget(self.spine_type_combo_box, 0, 0, 1, 2)

        # LEFT BREAST LABEL
        self.left_breast_label = QtGui.QLabel(widget)
        self.left_breast_label.setObjectName("left_breast_label")
        self.left_breast_label.setText('Left Breast')
        self.spine_grid_layout.addWidget(self.left_breast_label, 1, 0, 1, 1)
        # LEFT BREAST LINE EDIT
        self.left_breast_line_edit = QtGui.QLineEdit(widget)
        self.left_breast_line_edit.setObjectName("left_breast_line_edit")
        self.validator = QtGui.QDoubleValidator()
        self.left_breast_line_edit.setValidator(self.validator)
        self.left_breast_line_edit.setText(str(1))
        self.spine_grid_layout.addWidget(self.left_breast_line_edit, 1, 1, 1, 1)

        # RIGHT BREAST LABEL
        self.right_breast_label = QtGui.QLabel(widget)
        self.right_breast_label.setObjectName("right_breast_label")
        self.right_breast_label.setText('Right Breast')
        self.spine_grid_layout.addWidget(self.right_breast_label, 2, 0, 1, 1)
        # RIGHT BREAST LINE EDIT
        self.right_breast_line_edit = QtGui.QLineEdit(widget)
        self.right_breast_line_edit.setObjectName("right_breast_line_edit")
        self.right_breast_line_edit.setValidator(self.validator)
        self.right_breast_line_edit.setText(str(1))
        self.spine_grid_layout.addWidget(self.right_breast_line_edit, 2, 1, 1, 1)

        # NO OF THE JOINT LABEL
        self.no_of_joint_label = QtGui.QLabel(widget)
        self.no_of_joint_label.setObjectName("no_of_joint_label")
        self.no_of_joint_label.setText('No Of the Joint')
        self.spine_grid_layout.addWidget(self.no_of_joint_label, 3, 0, 1, 1)
        # NO OF THE JOINT LINE EDIT
        self.no_of_joint_line_edit = QtGui.QLineEdit(widget)
        self.no_of_joint_line_edit.setObjectName("no_of_joint_line_edit")
        self.no_of_joint_line_edit.setValidator(self.validator)
        self.no_of_joint_line_edit.setText(str(8))
        self.spine_grid_layout.addWidget(self.no_of_joint_line_edit, 3, 1, 1, 1)

        # SPINE BUTTON
        self.spine_create_button = QtGui.QPushButton(widget)
        self.spine_create_button.setObjectName("spine_create_button")
        self.spine_create_button.setText('Create Spine')
        self.spine_create_button.clicked.connect(self.new_spine_def)
        self.spine_grid_layout.addWidget(self.spine_create_button, 4, 0, 1, 2)

        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.spine_grid_layout.addItem(spacerItem, 5, 0, 1, 1)
        layout.addLayout(self.spine_grid_layout)

        layout.addLayout(self.spine_grid_layout)

    def new_clear(self):
        self.helper_class.clearLayout(self.spine_grid_layout)

    def new_spine_def(self):
        # get the value
        self.left_breast_line_edit_query = int(self.left_breast_line_edit.text())
        self.right_breast_line_edit_query = int(self.right_breast_line_edit.text())
        self.no_of_joint_line_edit_query = int(self.no_of_joint_line_edit.text())
        self.spine_type_combo_box_query = self.spine_type_combo_box.currentText()

        self.prefix_name = 'Template'

        if self.spine_type_combo_box_query == 'Human':
            self.human_spine_def()
        elif self.spine_type_combo_box_query == 'Animal':
            self.animal_spine_def()
        elif self.spine_type_combo_box_query == 'Bird':
            pass

    def human_spine_def(self ,find_val = False ,defaule_val=1):
        self.spine_type = 'Human'
        self.left_brest_pos = [2 ,23 ,3]
        self.right_brest_pos = [-2 ,23 ,3]

        # find the global name
        if cmds.objExists('*_Human_Spine_Tem_*_Main_Grp'):
            # get the val
            cmds.select("*_Human_Spine_Tem_*_Main_Grp")
            sel_spine_list = cmds.ls(sl=True)
            len_sel_spine_list = len(sel_spine_list)
            self.val = len_sel_spine_list + 1
        else:
            self.val = 1


        self.spine_def()
        self.base_spine()
        self.breast_def(self.left_breast_line_edit_query,
                        self.left_brest_pos,
                        'L',
                        'Red')
        self.breast_def(self.right_breast_line_edit_query,
                        self.right_brest_pos,
                        'R',
                        'Blue')

    def animal_spine_def(self ,find_val = False ,defaule_val=1):
        self.spine_type = 'Animal'
        self.left_brest_pos = [3 ,0 ,21.969]
        self.right_brest_pos = [-3 ,0 ,21.969]

        # find the global name

        if cmds.objExists('*_Animal_Spine_Tem_*_Main_Grp'):
            # get the val
            cmds.select("*_Animal_Spine_Tem_*_Main_Grp")
            sel_spine_list = cmds.ls(sl=True)
            len_sel_spine_list = len(sel_spine_list)
            self.val = len_sel_spine_list + 1
        else:
            self.val = 1

        self.spine_def()
        self.base_spine()
        self.breast_def(self.left_breast_line_edit_query,
                        self.left_brest_pos,
                        'L',
                        'Red')
        self.breast_def(self.right_breast_line_edit_query,
                        self.right_brest_pos,
                        'R',
                        'Blue')

    def spine_def(self ,val=0 ,update_val=1 ,def_val = 2):
        a = 0
        default_value = def_val + val
        while a < self.no_of_joint_line_edit_query:
            self.spine_sphere_name =  self.prefix_name + '_' + self.spine_type + '_Spine_' + str \
                (update_val) + '_Tem_' + str(self.val) + "_Geo"
            self.spine_clu_name = self.prefix_name + '_' + self.spine_type + '_Spine_' + str \
                (update_val) + '_Tem_' + str(self.val) + '_Clu'
            self.spine_clu_handle_name = self.spine_clu_name + 'Handle'
            if self.spine_type == 'Human':
                self.spine_pos = [0, default_value, 0]
                self.cylinder_ctrl_roate = [0 ,0 ,0]
                self.cylinder_rotate = [0 ,0 ,0]
            elif self.spine_type == 'Animal':
                self.spine_pos = [0, 3, default_value]
                self.cylinder_ctrl_roate = [90 ,0 ,0]
                self.cylinder_rotate = [90 ,0 ,0]
            elif self.spine_type == 'Bird':
                self.spine_pos = [default_value, 0, 0]
                self.cylinder_ctrl_roate = [0 ,0 ,90]
                self.cylinder_rotate = [0 ,0 ,-90]

            self.helper_class.set_sphere_position(self.spine_sphere_name,
                                                  self.spine_pos,
                                                  self.spine_clu_name)

            # create a controller
            self.cylinder_ctrl_name = self.prefix_name + '_' + self.spine_type + "_Spine_" + str \
                (update_val)  + "_Tem_" + str(self.val) + '_Ctrl'
            self.cylinder_ctrl_size_ctrl = [0.5 ,0.5 ,0.5]
            self.cylinder_parent_const_list = [self.spine_clu_handle_name]
            self.cylinder_ctrl_color = 'Yellow'
            self.cylinder_ctrl_freez_trans = True
            self.cylinder_ctrl_freez_rotate = True
            self.cylinder_ctrl_freez_scale = True
            self.helper_class.set_controller(self.cylinder_ctrl_name ,self.spine_pos ,self.cylinder_ctrl_size_ctrl,
                                             self.cylinder_ctrl_roate ,self.cylinder_parent_const_list
                                             ,self.cylinder_parent_const_list,
                                             color=self.cylinder_ctrl_color,
                                             freez_trans = self.cylinder_ctrl_freez_trans,
                                             freez_rotate = self.cylinder_ctrl_freez_rotate,
                                             freez_scale = self.cylinder_ctrl_freez_scale)

            # create a cylinder
            if a+ 1 != 1:
                self.cylinder_name = self.prefix_name + '_' + self.spine_type + "_Spine_" + str(
                    update_val - 1) + "_" + str(update_val) + "_Tem_" + str(self.val) + "_Geo"
                self.cylinder_upper_cluster_name = self.prefix_name + '_' + self.spine_type + "_Spine_Upper_" + str(
                    update_val - 1) + "_" + str(update_val) + "_Tem_" + str(self.val) + "_Clu"
                self.cylinder_upper_cluster_handle_name = self.cylinder_upper_cluster_name + 'Handle'
                self.cylinder_lower_cluster_name = self.prefix_name + '_' + self.spine_type + "_Spine_Lower_" + str(
                    update_val - 1) + "_" + str(update_val) + "_Tem_" + str(self.val) + "_Clu"
                self.cylinder_lower_cluster_handle_name = self.cylinder_lower_cluster_name + 'Handle'
                self.current_sphere_name = self.prefix_name + '_' + self.spine_type + '_Spine_' + str(
                    update_val) + '_Tem_' + str(self.val) + "_Geo"
                self.helper_class.set_cylinder_position(self.cylinder_name,
                                                        self.cylinder_lower_cluster_name,
                                                        self.cylinder_upper_cluster_name,
                                                        self.current_sphere_name,
                                                        self.spine_sphere_name,
                                                        rotate_val=self.cylinder_rotate)

                self.previous_ctrl = self.prefix_name + '_' + self.spine_type + "_Spine_" + str(
                    update_val - 1) + "_Tem_" + str(self.val) + '_Ctrl'
                self.parent_list = [self.cylinder_lower_cluster_handle_name]
                self.helper_class.parent_constrain(self.previous_ctrl, self.parent_list)
                self.helper_class.scale_constrain(self.previous_ctrl, self.parent_list)

                self.parent_list = [self.cylinder_upper_cluster_handle_name]
                self.helper_class.parent_constrain(self.cylinder_ctrl_name, self.parent_list)
                self.helper_class.scale_constrain(self.cylinder_ctrl_name, self.parent_list)

                # pare the controller
                cmds.select(self.cylinder_ctrl_name, self.previous_ctrl)
                cmds.parent()

                self.cylinder_group_name = self.prefix_name + '_' + self.spine_type + "_Spine_Tem_" + str(
                    self.val) + "_Cylinder_Grp"
                if cmds.objExists(self.cylinder_group_name):
                    cmds.select(self.cylinder_name, self.cylinder_group_name)
                    cmds.parent()
                else:
                    cmds.select(self.cylinder_name)
                    cmds.group(n=self.cylinder_group_name)

                self.cluster_grp_name = self.prefix_name + '_' + self.spine_type + '_Spine_Tem_' + str(
                    self.val) + "_Cluster_Grp"
                if cmds.objExists(self.cluster_grp_name):
                    cmds.select(self.cylinder_upper_cluster_handle_name, self.cylinder_lower_cluster_handle_name,
                                self.cluster_grp_name)
                    cmds.parent()
                else:
                    cmds.select(self.cylinder_upper_cluster_handle_name, self.cylinder_lower_cluster_handle_name)
                    cmds.group(n=self.cluster_grp_name)

            default_value += 4

            self.sphere_grp_name = self.prefix_name + '_' + self.spine_type + '_Spine_Tem_' + str(
                self.val) + "_Sphere_Grp"
            if cmds.objExists(self.sphere_grp_name):
                cmds.select(self.spine_sphere_name, self.sphere_grp_name)
                cmds.parent()
            else:
                cmds.select(self.spine_sphere_name)
                cmds.group(n=self.sphere_grp_name)

            self.cluster_grp_name = self.prefix_name + '_' + self.spine_type + '_Spine_Tem_' + str(
                self.val) + "_Cluster_Grp"
            if cmds.objExists(self.cluster_grp_name):
                cmds.select(self.spine_clu_handle_name, self.cluster_grp_name)
                cmds.parent()
            else:
                cmds.select(self.spine_clu_handle_name)
                cmds.group(n=self.cluster_grp_name)
            update_val += 1
            a += 1

    def cylinder_def(self, common_middle,
                     rotate,
                     first_sphere_name,
                     secound_sphere_name):

        self.common_name = self.prefix_name + "_" + self.spine_type + "_Spine_" + common_middle + "_Tem_" + str(
            self.val)
        self.cylinder_name = self.common_name + '_Geo'
        self.cylinder_lower_cylinder_cluster_name = self.prefix_name + "_" + self.spine_type + "_Spine_" + common_middle + "_Lower_Tem_" + str(
            self.val) + '_Clu'
        self.cylinder_lower_cylinder_cluster_handle_name = self.cylinder_lower_cylinder_cluster_name + 'Handle'
        self.cylinder_upper_cylinder_cluster_name = self.prefix_name + "_" + self.spine_type + "_Spine_" + common_middle + "_Upper_Tem_" + str(
            self.val) + '_Clu'
        self.cylinder_upper_cylinder_cluster_handle_name = self.cylinder_upper_cylinder_cluster_name + 'Handle'
        self.cylinder_rotate = rotate
        self.helper_class.set_cylinder_position(self.cylinder_name,
                                                self.cylinder_lower_cylinder_cluster_name,
                                                self.cylinder_upper_cylinder_cluster_name,
                                                first_sphere_name,
                                                secound_sphere_name,
                                                rotate_val=[self.cylinder_rotate[0],
                                                            self.cylinder_rotate[1],
                                                            self.cylinder_rotate[2]])

        cmds.select(self.cylinder_lower_cylinder_cluster_handle_name,
                    self.cylinder_upper_cylinder_cluster_handle_name, self.cluster_grp_name)
        cmds.parent()
        cmds.select(self.cylinder_name, self.cylinder_group_name)
        cmds.parent()

        self.lower_cluster_handle = self.cylinder_lower_cylinder_cluster_handle_name
        self.upper_cluster_handle = self.cylinder_upper_cylinder_cluster_handle_name

    def base_spine(self):

        self.spine_base_sphere_name = self.prefix_name + '_' + self.spine_type + '_Spine_Base_Tem_' + str(
            self.val) + "_Geo"
        self.spine_base_clu_name = self.prefix_name + '_' + self.spine_type + '_Spine_Base_Tem_' + str(
            self.val) + '_Clu'
        self.spine_base_clu_handle_name = self.spine_base_clu_name + 'Handle'
        self.spine_pos = [0, 0, 0]
        self.helper_class.set_sphere_position(self.spine_base_sphere_name,
                                              self.spine_pos,
                                              self.spine_base_clu_name)

        # create a controller
        self.spine_base_ctrl_name = self.prefix_name + '_' + self.spine_type + "_Spine_Base_Tem_" + str(
            self.val) + '_Ctrl'
        self.spine_ctrl_size_ctrl = [1.0, 1.0, 1.0]
        self.spine_parent_const_list = [self.spine_base_clu_handle_name]
        self.spine_ctrl_color = 'Yellow'
        self.spine_ctrl_freez_trans = True
        self.spine_ctrl_freez_rotate = True
        self.spine_ctrl_freez_scale = True
        self.helper_class.set_controller(self.spine_base_ctrl_name, self.spine_pos, self.spine_ctrl_size_ctrl,
                                         self.cylinder_ctrl_roate, self.spine_parent_const_list,
                                         self.spine_parent_const_list,
                                         color=self.spine_ctrl_color,
                                         freez_trans=self.spine_ctrl_freez_trans,
                                         freez_rotate=self.spine_ctrl_freez_rotate,
                                         freez_scale=self.spine_ctrl_freez_scale)

        self.cylinder_name = self.prefix_name + '_' + self.spine_type + "_Spine_Base_" + str(0) + "_Tem_" + str(
            self.val) + "_Geo"
        self.cylinder_upper_cluster_name = self.prefix_name + '_' + self.spine_type + "_Spine_Upper_Base_" + str(
            0) + "_Tem_" + str(self.val) + "_Clu"
        self.cylinder_upper_cluster_handle_name = self.cylinder_upper_cluster_name + 'Handle'
        self.cylinder_lower_cluster_name = self.prefix_name + '_' + self.spine_type + "_Spine_Lower_Base_" + str(
            0) + "_Tem_" + str(self.val) + "_Clu"
        self.cylinder_lower_cluster_handle_name = self.cylinder_lower_cluster_name + 'Handle'
        self.first_sphere_name = self.prefix_name + '_' + self.spine_type + "_Spine_" + str(1) + "_Tem_" + str(
            self.val) + "_Geo"
        self.first_ctrl_name = self.prefix_name + '_' + self.spine_type + "_Spine_" + str(1) + "_Tem_" + str(
            self.val) + "_Ctrl"
        self.helper_class.set_cylinder_position(self.cylinder_name,
                                                self.cylinder_lower_cluster_name,
                                                self.cylinder_upper_cluster_name,
                                                self.spine_base_sphere_name,
                                                self.first_sphere_name)

        self.parent_list = [self.cylinder_upper_cluster_handle_name]
        self.helper_class.parent_constrain(self.first_ctrl_name, self.parent_list)
        self.helper_class.scale_constrain(self.first_ctrl_name, self.parent_list)

        self.parent_list = [self.cylinder_lower_cluster_handle_name]
        self.helper_class.parent_constrain(self.spine_base_ctrl_name, self.parent_list)
        self.helper_class.scale_constrain(self.spine_base_ctrl_name, self.parent_list)

        cmds.select(self.spine_base_sphere_name, self.sphere_grp_name)
        cmds.parent()
        cmds.select(self.spine_base_clu_handle_name, self.cylinder_upper_cluster_handle_name
                    , self.cylinder_lower_cluster_handle_name, self.cluster_grp_name)
        cmds.parent()
        cmds.select(self.cylinder_name, self.cylinder_group_name)
        cmds.parent()
        cmds.select(self.first_ctrl_name, self.spine_base_ctrl_name)
        cmds.parent()

        cmds.setAttr((self.cluster_grp_name + '.v'), 0)
        cmds.setAttr((self.cluster_grp_name + '.v'), lock=True)
        self.helper_class.transform_rotation_scale_visible(self.cluster_grp_name)

        self.ctrl_grp_name = self.prefix_name + '_' + self.spine_type + '_Spine_Tem_' + str(self.val) + "_Ctrl_Grp"
        if cmds.objExists(self.ctrl_grp_name):
            cmds.select(self.spine_base_ctrl_name, self.ctrl_grp_name)
            cmds.parent()
        else:
            cmds.select(self.spine_base_ctrl_name)
            cmds.group(n=self.ctrl_grp_name)

        # put everything in the one grpup
        cmds.select(self.sphere_grp_name,
                    self.cluster_grp_name,
                    self.cylinder_group_name,
                    self.ctrl_grp_name)
        self.main_group_name = self.prefix_name + '_' + self.spine_type + '_Spine_Tem_' + str(self.val) + '_Main_Grp'
        cmds.group(n=self.main_group_name)

        # put everything in one group
        if self.spine_type == 'Human':
            self.character_spine_grp = 'Human_Spine_Grp'
        elif self.spine_type == 'Animal':
            self.character_spine_grp = 'Animal_Spine_Grp'
        elif self.spine_type == 'Bird':
            self.character_spine_grp = 'Bird_Spine_Grp'

        if cmds.objExists(self.character_spine_grp):
            cmds.select(self.main_group_name, self.character_spine_grp)
            cmds.parent()
        else:
            cmds.select(self.main_group_name)
            cmds.group(n=self.character_spine_grp)
            self.helper_class.transform_rotation_scale_visible(self.character_spine_grp)

        self.spine_grp = 'Spine_Grp'
        if cmds.objExists(self.spine_grp):
            parent_obj = cmds.listRelatives(self.character_spine_grp, p=True)
            if parent_obj == None:
                cmds.select(self.character_spine_grp, self.spine_grp)
                cmds.parent()
        else:
            cmds.select(self.character_spine_grp)
            cmds.group(n=self.spine_grp)
            self.helper_class.transform_rotation_scale_visible(self.spine_grp, v=False)

    def breast_def(self, line_edit_query, pos, side, color):
        # set the left breast
        a = 0
        value = 0
        while a < line_edit_query:
            self.breast_common = self.prefix_name + '_' + self.spine_type + '_' + side + '_Spine_Breast_' + str(
                a + 1) + '_Tem_' + str(self.val)
            self.sphere_name = self.breast_common + "_Geo"
            self.clu_name = self.breast_common + "_Clu"
            self.clu_handle_name = self.clu_name + 'Handle'
            self.new_value = pos[1] + value
            if self.spine_type == 'Human':
                self.new_value = pos[1] + value
                self.pos = [pos[0],
                            self.new_value,
                            pos[2]]
                self.cylinder_ctrl_roate = [0, 0, 0]
            elif self.spine_type == 'Animal':
                self.new_value = pos[2] + value
                self.pos = [pos[0],
                            pos[1],
                            self.new_value]
                self.cylinder_ctrl_roate = [90, 0, 0]
            elif self.spine_type == 'Bird':
                self.new_value = pos[0] + value
                self.pos = [self.new_value,
                            pos[1],
                            pos[2]]
                self.cylinder_ctrl_roate = [0, 0, 90]

            self.helper_class.set_sphere_position(self.sphere_name,
                                                  self.pos,
                                                  self.clu_name)

            # create a controller
            self.spine_breast_ctrl_name = self.breast_common + '_Ctrl'
            self.spine_breast_ctrl_grp_name = self.spine_breast_ctrl_name + '_Grp'
            self.spine_ctrl_size_ctrl = [0.6, 0.6, 0.6]

            self.spine_parent_const_list = [self.clu_handle_name]
            self.spine_ctrl_color = color
            self.spine_ctrl_freez_trans = True
            self.spine_ctrl_freez_rotate = True
            self.spine_ctrl_freez_scale = True
            self.helper_class.set_controller(self.spine_breast_ctrl_name, self.pos, self.spine_ctrl_size_ctrl,
                                             self.cylinder_ctrl_roate, self.spine_parent_const_list,
                                             self.spine_parent_const_list,
                                             color=self.spine_ctrl_color,
                                             freez_trans=self.spine_ctrl_freez_trans,
                                             freez_rotate=self.spine_ctrl_freez_rotate,
                                             freez_scale=self.spine_ctrl_freez_scale)
            cmds.select(self.spine_breast_ctrl_name)
            cmds.group(n=self.spine_breast_ctrl_grp_name)
            cmds.move()
            # Template_Human_Spine_7_8_Tem_1_Ctrl
            self.last_ctrl = self.prefix_name + '_' + self.spine_type + "_Spine_" + str(7) + "_Tem_" + str(
                self.val) + '_Ctrl'
            cmds.parentConstraint(self.last_ctrl, self.spine_breast_ctrl_grp_name, mo=True)
            cmds.select(self.sphere_name, self.sphere_grp_name)
            cmds.parent()
            cmds.select(self.clu_handle_name, self.cluster_grp_name)
            cmds.parent()
            cmds.select(self.spine_breast_ctrl_grp_name, self.ctrl_grp_name)
            cmds.parent()

            value += 2

            a += 1

    def update_gui(self, widget):
        self.update_widget = widget

        self.verticalLayout = QtGui.QVBoxLayout(self.update_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.common_spitter = QtGui.QSplitter(self.update_widget)
        self.common_spitter.setOrientation(QtCore.Qt.Vertical)
        self.common_spitter.setObjectName("common_spitter")

        # get the radio button
        self.get_update_radio_button()
        self.get_detail_update_def()

        # lock the attr
        self.lock_attr()

    def get_update_radio_button(self):
        self.spine_name_scroll_area = QtGui.QScrollArea(self.common_spitter)
        self.spine_name_scroll_area.setWidgetResizable(True)
        self.spine_name_scroll_area.setObjectName("spine_name_scroll_area")
        self.spine_name_scrollArea_widget_contents = QtGui.QWidget()
        self.spine_name_scrollArea_widget_contents.setGeometry(QtCore.QRect(0, 0, 642, 64))
        self.spine_name_scrollArea_widget_contents.setObjectName("spine_name_scrollArea_widget_contents")
        self.gridLayout_15 = QtGui.QGridLayout(self.spine_name_scrollArea_widget_contents)
        self.gridLayout_15.setObjectName("gridLayout_15")

        self.number = self.helper_class.get_spine()
        a = 0
        value = 0
        grid_value = 0
        while a < len(self.number):
            self.radio_button = QtGui.QRadioButton(self.spine_name_scrollArea_widget_contents)
            self.radio_button.setObjectName(self.number[a])
            self.radio_button.setText(self.number[a])
            self.gridLayout_15.addWidget(self.radio_button, grid_value, value, 1, 1)
            self.radio_button.toggled.connect(partial(self.radio_button_change, a))
            value += 1
            if value == 3:
                value = 0
                grid_value += 1

            a += 1

        self.spine_name_scroll_area.setWidget(self.spine_name_scrollArea_widget_contents)

    def get_detail_update_def(self):
        self.head_detail_scroll_area = QtGui.QScrollArea(self.common_spitter)
        self.head_detail_scroll_area.setWidgetResizable(True)
        self.head_detail_scroll_area.setObjectName("head_detail_scroll_area")
        self.head_detail_scrollArea_widget_contents = QtGui.QWidget()
        self.head_detail_scrollArea_widget_contents.setGeometry(QtCore.QRect(0, 0, 489, 350))
        self.head_detail_scrollArea_widget_contents.setObjectName("head_detail_scrollArea_widget_contents")

        # UPDATE
        self.head_detail_2_scroll_area = QtGui.QScrollArea(self.head_detail_scrollArea_widget_contents)
        self.head_detail_2_scroll_area.setMinimumSize(QtCore.QSize(0, 207))
        self.head_detail_2_scroll_area.setWidgetResizable(True)
        self.head_detail_2_scroll_area.setObjectName("head_detail_2_scroll_area")
        self.head_detail_2_scrollArea_widget_contents = QtGui.QWidget()
        self.head_detail_2_scrollArea_widget_contents.setGeometry(QtCore.QRect(0, 0, 469, 275))
        self.head_detail_2_scrollArea_widget_contents.setObjectName("head_detail_2_scrollArea_widget_contents")
        self.gridLayout_16 = QtGui.QGridLayout(self.head_detail_2_scrollArea_widget_contents)
        self.gridLayout_16.setObjectName("gridLayout_16")

        self.gridLayout_23 = QtGui.QGridLayout()
        self.gridLayout_23.setObjectName("gridLayout_23")

        # CHARACTER TYPE
        # CHARACTER LABEL
        self.character_type_label = QtGui.QLabel(self.head_detail_2_scrollArea_widget_contents)
        self.character_type_label.setObjectName("character_type_label")
        self.character_type_label.setText('Character Type : ')
        self.gridLayout_23.addWidget(self.character_type_label, 0, 0, 1, 1)
        # CHARACTER OPTION MENU
        self.character_type_combo_box = QtGui.QComboBox(self.head_detail_2_scrollArea_widget_contents)
        self.character_type_combo_box.setObjectName("character_type_combo_box")
        self.character_type_combo_box.addItem("Human")
        self.character_type_combo_box.addItem("Animal")
        self.character_type_combo_box.addItem("Bird")
        self.character_type_combo_box.setMinimumWidth(363)
        self.gridLayout_23.addWidget(self.character_type_combo_box, 0, 1, 1, 1)

        # SPINE NO
        # SPINE NO LABEL
        self.spine_no_label = QtGui.QLabel(self.head_detail_2_scrollArea_widget_contents)
        self.spine_no_label.setObjectName("Spine_No")
        self.spine_no_label.setText('Spine No : ')
        self.gridLayout_23.addWidget(self.spine_no_label, 1, 0, 1, 1)
        # SPINE NO LINE EDIT
        self.spine_no_line_edit = QtGui.QLineEdit(self.head_detail_2_scrollArea_widget_contents)
        self.spine_no_line_edit.setObjectName("Spine_No_Line")
        self.validator = QtGui.QDoubleValidator()
        self.spine_no_line_edit.setValidator(self.validator)
        self.gridLayout_23.addWidget(self.spine_no_line_edit, 1, 1, 1, 1)

        # LEFT BREAST
        # LEFT BREAST LABEL
        self.left_breast_label = QtGui.QLabel(self.head_detail_2_scrollArea_widget_contents)
        self.left_breast_label.setObjectName("Left_Breast_Label")
        self.left_breast_label.setText('Left Breast : ')
        self.gridLayout_23.addWidget(self.left_breast_label, 2, 0, 1, 1)
        # LEFT EYE LINE EDIT
        self.left_breast_line_edit = QtGui.QLineEdit(self.head_detail_2_scrollArea_widget_contents)
        self.left_breast_line_edit.setObjectName("Left_Breast_LineEdit")
        self.left_breast_line_edit.setValidator(self.validator)
        self.gridLayout_23.addWidget(self.left_breast_line_edit, 2, 1, 1, 1)

        # RIGHT EYE
        # RIGH EYE LABEL
        self.right_breast_label = QtGui.QLabel(self.head_detail_2_scrollArea_widget_contents)
        self.right_breast_label.setObjectName("Right_Breast_Label")
        self.right_breast_label.setText('Right Breast : ')
        self.gridLayout_23.addWidget(self.right_breast_label, 3, 0, 1, 1)
        # LEFT EYE LINE EDIT
        self.right_breast_line_edit = QtGui.QLineEdit(self.head_detail_2_scrollArea_widget_contents)
        self.right_breast_line_edit.setObjectName("Right_Breast_LineEdit")
        self.right_breast_line_edit.setValidator(self.validator)
        self.gridLayout_23.addWidget(self.right_breast_line_edit, 3, 1, 1, 1)

        # NAME
        # NAME LABEL
        self.name_label = QtGui.QLabel(self.head_detail_2_scrollArea_widget_contents)
        self.name_label.setObjectName("name_label")
        self.name_label.setText('Name : ')
        self.gridLayout_23.addWidget(self.name_label, 4, 0, 1, 1)
        # NAME BUTTON
        self.name_button = QtGui.QPushButton(self.head_detail_2_scrollArea_widget_contents)
        self.name_button.setObjectName("name_button")
        self.name_button.clicked.connect(self.rename)
        self.gridLayout_23.addWidget(self.name_button, 4, 1, 1, 1)

        # PARENT
        # PARENT LABEL
        self.parent_label = QtGui.QLabel(self.head_detail_2_scrollArea_widget_contents)
        self.parent_label.setObjectName("parent_label")
        self.parent_label.setText('Parent : ')
        self.gridLayout_23.addWidget(self.parent_label, 5, 0, 1, 1)
        # PARENT BUTTON
        self.parent_button = QtGui.QPushButton(self.head_detail_2_scrollArea_widget_contents)
        self.parent_button.setObjectName("parent_button")
        self.parent_button.clicked.connect(self.parent)
        self.gridLayout_23.addWidget(self.parent_button, 5, 1, 1, 1)

        spacerItem10 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_23.addItem(spacerItem10, 6, 0, 1, 1)

        self.gridLayout_16.addLayout(self.gridLayout_23, 0, 0, 1, 1)
        self.head_detail_2_scroll_area.setWidget(self.head_detail_2_scrollArea_widget_contents)

        # UPDATE AND DELETE BUTTON
        self.gridLayout_18 = QtGui.QGridLayout(self.head_detail_scrollArea_widget_contents)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.head_update_scroll_area = QtGui.QScrollArea(self.head_detail_scrollArea_widget_contents)
        self.head_update_scroll_area.setMaximumSize(QtCore.QSize(16777215, 49))
        self.head_update_scroll_area.setWidgetResizable(True)
        self.head_update_scroll_area.setObjectName("head_update_scroll_area")
        self.head_update_scrollArea_widget_contents = QtGui.QWidget()
        self.head_update_scrollArea_widget_contents.setGeometry(QtCore.QRect(0, 0, 469, 47))
        self.head_update_scrollArea_widget_contents.setObjectName("head_update_scrollArea_widget_contents")
        self.gridLayout_17 = QtGui.QGridLayout(self.head_update_scrollArea_widget_contents)
        self.gridLayout_17.setObjectName("gridLayout_17")

        # UPDATE BUTTON
        self.spine_update_button = QtGui.QPushButton(self.head_update_scrollArea_widget_contents)
        self.spine_update_button.setObjectName("spine_update_button")
        self.spine_update_button.clicked.connect(self.spine_update_button_def)
        self.spine_update_button.setText('Update (Spine name)')

        self.gridLayout_17.addWidget(self.spine_update_button, 1, 0, 1, 1)

        # DELETE BUTTON
        self.spine_delete_button = QtGui.QPushButton(self.head_update_scrollArea_widget_contents)
        self.spine_delete_button.setObjectName("spine_delete_button")
        self.spine_delete_button.setText('Delete(Spine Name)')
        self.gridLayout_17.addWidget(self.spine_delete_button, 1, 1, 1, 1)

        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_17.addItem(spacerItem9, 0, 0, 1, 1)

        self.head_update_scroll_area.setWidget(self.head_update_scrollArea_widget_contents)
        self.gridLayout_18.addWidget(self.head_update_scroll_area, 1, 0, 1, 1)

        self.gridLayout_18.addWidget(self.head_detail_2_scroll_area, 0, 0, 1, 1)
        self.head_detail_scroll_area.setWidget(self.head_detail_scrollArea_widget_contents)
        self.verticalLayout.addWidget(self.common_spitter)

        self.head_detail_scroll_area.setWidget(self.head_detail_scrollArea_widget_contents)
        self.verticalLayout.addWidget(self.common_spitter)

    def delete_all(self):
        print('now all Spine is going to delete')

    def lock_attr(self):
        self.character_type_combo_box.setDisabled(True)
        self.spine_no_label.setDisabled(True)
        self.spine_no_line_edit.setDisabled(True)
        self.left_breast_label.setDisabled(True)
        self.left_breast_line_edit.setDisabled(True)
        self.right_breast_label.setDisabled(True)
        self.right_breast_line_edit.setDisabled(True)
        self.name_label.setDisabled(True)
        self.name_button.setDisabled(True)
        self.parent_label.setDisabled(True)
        self.parent_button.setDisabled(True)
        self.spine_update_button.setDisabled(True)
        self.spine_delete_button.setDisabled(True)

    def unlock_attr(self):
        self.character_type_combo_box.setDisabled(False)
        self.spine_no_label.setDisabled(False)
        self.spine_no_line_edit.setDisabled(False)
        self.left_breast_label.setDisabled(False)
        self.left_breast_line_edit.setDisabled(False)
        self.right_breast_label.setDisabled(False)
        self.right_breast_line_edit.setDisabled(False)
        self.name_label.setDisabled(False)
        self.name_button.setDisabled(False)
        self.parent_label.setDisabled(False)
        self.parent_button.setDisabled(False)
        self.spine_update_button.setDisabled(False)
        self.spine_delete_button.setDisabled(False)

    def radio_button_change(self, b, val):
        if val == True:
            # unlock the val
            self.radio_button_val = b
            self.unlock_attr()

            # get the value
            self.get_input_data(self.number[b])

            # update the ui
            self.character_type_combo_box.setCurrentIndex(self.input_character_option_menu)
            self.spine_no_line_edit.setText(str(self.input_no_spine))
            self.left_breast_line_edit.setText(str(self.input_left_breast))
            self.right_breast_line_edit.setText(str(self.input_right_breast))
            self.name_button.setText(self.prefix_name)
            self.parent_button.setText(self.input_parent)
            self.spine_update_button.setText('Update (%s)' % self.spine_name)
            self.spine_delete_button.setText('Delete(%s)' % self.spine_name)

            cmds.select(cl=True)

    def get_input_data(self, spine_name):
        self.spine_name = spine_name
        self.name = self.spine_name.split('_')
        self.input_main_grp_name = '*_' + self.name[0] + '_Spine_Tem_' + self.name[-1] + '_Main_Grp'
        cmds.select(self.input_main_grp_name)
        self.input_sel_main_grp_name = cmds.ls(sl=True)[0]
        self.input_split_main_grp = self.input_sel_main_grp_name.split('_' + self.name[0])[0]
        # get the characert option menu
        if self.name[0] == 'Human':
            value = 0
        elif self.name[0] == 'Animal':
            value = 1
        elif self.name[0] == 'Bird':
            value = 2

        # get left eye

        self.spine_type = self.name[0]
        self.val = self.name[-1]
        self.prefix_name = self.input_split_main_grp
        self.input_character_option_menu = value
        self.input_no_spine = self.spine_no_query()
        self.input_left_breast = self.left_breast_query()
        self.input_right_breast = self.right_breast_query()
        self.input_parent = self.parent_query()

    def spine_no_query(self):
        # Template_Human_Spine_1_Tem_1_Geo
        self.sphere_name = self.prefix_name + '_' + self.spine_type + '_Spine_*_Tem_' + self.val + '_Ctrl'
        self.base_ctrl_name = self.prefix_name + '_' + self.spine_type + '_Spine_Base_Tem_' + self.val + '_Ctrl'
        cmds.select(self.sphere_name)
        cmds.select(self.base_ctrl_name, d=True)
        sel_ctrl = cmds.ls(sl=True)
        return len(sel_ctrl)

    def left_breast_query(self):
        # Template_Human_L_Spine_Breast_1_Tem_1_Ctrl
        self.ctrl_name = self.prefix_name + '_' + self.spine_type + '_L_Spine_Breast_*_Tem_' + self.val + '_Ctrl'
        cmds.select(self.ctrl_name)
        sel_ctrl = cmds.ls(sl=True)
        return len(sel_ctrl)

    def right_breast_query(self):
        # Template_Human_Head_Left_Eye_1_Tem_3_Ctrl
        self.ctrl_name = self.prefix_name + '_' + self.spine_type + '_R_Spine_Breast_*_Tem_' + self.val + '_Ctrl'
        cmds.select(self.ctrl_name)
        sel_ctrl = cmds.ls(sl=True)
        return len(sel_ctrl)

    def parent_query(self):
        # Template_Human_Spine_Base_Tem_1_Ctrl
        base_ctrl_name = self.prefix_name + '_' + self.spine_type + '_Spine_Base_Tem_' + self.val + '_Ctrl'
        value = cmds.listRelatives(base_ctrl_name, type='parentConstraint')
        if value == None:
            parent = 'None'
        else:
            parent = cmds.listConnections((value[0] + '.target[0].targetTranslate'), type='transform')[0]

        return parent

    def rename(self):
        # rename.main('Head',self.head_name,self.name_button,mirror_val=False,mirror_side='')
        rename.main('Spine', self.spine_name, self.name_button, mirror_val=False, mirror_side='')

    def parent(self):
        parent.main('Spine', self.spine_name, self.parent_button)

    def spine_update_get_data(self):
        self.character_type_combo_box_query = self.character_type_combo_box.currentText()
        self.spine_no_line_edit_query = int(self.spine_no_line_edit.text())
        self.get_left_breast = int(self.left_breast_line_edit.text())
        self.get_right_breast = int(self.right_breast_line_edit.text())
        self.prefix_name = self.name_button.text()
        self.get_parent = self.parent_button.text()

    def spine_update_button_def(self):
        self.spine_update_get_data()
        self.get_grp_def()

        if self.character_type_combo_box_query == self.spine_type:
            # check the spine no
            if self.input_no_spine != self.spine_no_line_edit_query:
                # get the increase the spine
                if self.spine_no_line_edit_query > self.input_no_spine:
                    # get the last controller pos
                    # Test_Human_Spine_7_8_Tem_1_Ctrl
                    ctrl_common = self.prefix_name + '_' + self.spine_type + '_Spine_' + str(
                        self.input_no_spine) + '_Tem_' + str(self.val)
                    ctrl_name = ctrl_common + '_Ctrl'
                    ctrl_pos = cmds.xform(ctrl_name, q=1, ws=1, rp=1)
                    self.no_of_joint_line_edit_query = self.spine_no_line_edit_query - self.input_no_spine
                    if self.spine_type == 'Human' or self.spine_type == 'Animal':
                        if self.spine_type == 'Human':
                            value = ctrl_pos[1]
                            self.cylinder_rotate = [0, 0, 0]
                            self.cylinder_ctrl_roate = [0, 0, 90]
                        elif self.spine_type == 'Animal':
                            value = ctrl_pos[0]
                            self.cylinder_rotate = [0, 0, 0]
                            self.cylinder_ctrl_roate = [0, 0, 90]

                        self.spine_def(val=value,
                                       update_val=self.input_no_spine + 1,
                                       def_val=4)
                        new_ctrl_common = self.prefix_name + '_' + self.spine_type + '_Spine_' + str(
                            self.input_no_spine + 1) + '_Tem_' + str(self.val)
                        new_ctrl = new_ctrl_common + '_Ctrl'
                        cmds.select(new_ctrl, ctrl_name)
                        cmds.parent()
                        # create a cylinder
                        # branch 4 3 to branch 4 4
                        self.current_common = str(self.input_no_spine) + '_' + str(self.input_no_spine + 1)
                        self.previous_common = str(self.input_no_spine - 1) + '_' + str(self.input_no_spine)
                        self.first_sphere_name = self.helper_class.object_name(ctrl_common, geo_name=True)
                        self.secound_sphere_name = self.helper_class.object_name(new_ctrl_common, geo_name=True)
                        self.cylinder_def(self.current_common,
                                          self.cylinder_rotate,
                                          self.secound_sphere_name,
                                          self.first_sphere_name)
                        cmds.parentConstraint(ctrl_name, self.lower_cluster_handle, mo=False)
                        cmds.parentConstraint(new_ctrl, self.upper_cluster_handle, mo=False)
                # decrease the spine
                elif self.spine_no_line_edit_query < self.input_no_spine:
                    val = self.input_no_spine - self.spine_no_line_edit_query
                    a = 0
                    while a < self.input_no_spine:
                        if a >= self.spine_no_line_edit_query:
                            self.common_del_name = self.prefix_name + '_' + self.spine_type + "_Spine_" + str(
                                a + 1) + "_Tem_" + str(self.val)
                            self.sphere_del_name = self.common_del_name + '_Geo'
                            self.sphere_del_clu_handle_name = self.common_del_name + '_CluHandle'
                            self.sphere_del_ctrl_name = self.common_del_name + '_Ctrl'
                            # Template_Human_Spine_8_9_Tem_1_Geo
                            self.cylinder_del_name = self.prefix_name + '_' + self.spine_type + "_Spine_" + str(
                                a) + '_' + str(a + 1) + "_Tem_" + str(self.val) + '_Geo'
                            cmds.select(self.sphere_del_name, self.sphere_del_clu_handle_name, self.cylinder_del_name)
                            if a == self.spine_no_line_edit_query:
                                cmds.select(self.sphere_del_ctrl_name, add=True)
                            cmds.delete()
                        a += 1

                # find_val = False,defaule_val=1

            # left breast
            if self.get_left_breast != self.input_left_breast:
                # self.input_left_breast = self.left_breast_query()
                if self.get_left_breast > self.input_left_breast:
                    # delete all the left breast geo,cluster,ctrl
                    self.side = 'L'
                    ctrl_common = self.prefix_name + '_' + self.spine_type + '_' + self.side + '_Spine_Breast_1_Tem_' + str(
                        self.val)
                    ctrl_name = ctrl_common + '_Ctrl'
                    ctrl_pos = cmds.xform(ctrl_name, q=1, ws=1, rp=1)

                    self.delete_breasr()
                    self.breast_def(self.get_left_breast,
                                    ctrl_pos,
                                    self.side,
                                    'Red')


                elif self.get_left_breast < self.input_left_breast:
                    a = 0
                    while a < self.input_left_breast:
                        if a + 1 > self.get_left_breast:
                            common_name = self.prefix_name + '_' + self.spine_type + '_L_Spine_Breast_' + str(
                                a + 1) + '_Tem_' + str(self.val)
                            ctrl_name = common_name + '_Ctrl'
                            clu_handle_name = common_name + '_CluHandle'
                            geo_name = common_name + '_Geo'
                            ctrl_grp_name = ctrl_name + '_Grp'
                            cmds.select(clu_handle_name, geo_name, ctrl_grp_name)
                            cmds.delete()
                        a += 1

            # right breast
            if self.get_right_breast != self.input_right_breast:
                # self.input_right_breast = self.right_breast_query()
                if self.get_right_breast > self.input_right_breast:
                    # delete all the left breast geo,cluster,ctrl
                    self.side = 'R'
                    ctrl_common = self.prefix_name + '_' + self.spine_type + '_' + self.side + '_Spine_Breast_1_Tem_' + str(
                        self.val)
                    ctrl_name = ctrl_common + '_Ctrl'
                    ctrl_pos = cmds.xform(ctrl_name, q=1, ws=1, rp=1)

                    self.delete_breasr()
                    self.breast_def(self.get_left_breast,
                                    ctrl_pos,
                                    self.side,
                                    'Blue')
                elif self.get_right_breast < self.input_right_breast:
                    a = 0
                    while a < self.input_left_breast:
                        if a + 1 > self.get_left_breast:
                            common_name = self.prefix_name + '_' + self.spine_type + '_R_Spine_Breast_' + str(
                                a + 1) + '_Tem_' + str(self.val)
                            ctrl_name = common_name + '_Ctrl'
                            clu_handle_name = common_name + '_CluHandle'
                            geo_name = common_name + '_Geo'
                            ctrl_grp_name = ctrl_name + '_Grp'
                            cmds.select(clu_handle_name, geo_name, ctrl_grp_name)
                            cmds.delete()
                        a += 1

            cmds.select(cl=True)
            self.get_input_data(self.number[self.radio_button_val])
            self.spine_update_get_data()
        else:
            # Template_Human_Spine_Tem_1_Main_Grp
            # get the old position
            # Template_Animal_Spine_Base_Tem_2_Ctrl
            old_base_ctrl_name = self.prefix_name + '_' + self.spine_type + '_Spine_Base_Tem_' + str(self.val) + '_Ctrl'
            base_ctrl_trans_getAttr = cmds.getAttr(old_base_ctrl_name + '.t')[0]
            base_ctrl_rot_getAttr = cmds.getAttr(old_base_ctrl_name + '.r')[0]

            old_main_grp_name = self.prefix_name + '_' + self.spine_type + '_Spine_Tem_' + str(self.val) + '_Main_Grp'
            cmds.select(old_main_grp_name)
            cmds.delete()
            # get the value
            self.left_breast_line_edit_query = self.get_left_breast
            self.right_breast_line_edit_query = self.get_right_breast
            self.no_of_joint_line_edit_query = self.spine_no_line_edit_query
            self.spine_type_combo_box_query = self.character_type_combo_box_query

            if self.spine_type_combo_box_query == 'Human':
                self.human_spine_def()
                base_ctrl_name = self.prefix_name + '_' + self.spine_type + '_Spine_Base_Tem_' + str(self.val) + '_Ctrl'
                self.helper_class.set_val(ctrl_name=base_ctrl_name,
                                          t=True, t_val=base_ctrl_trans_getAttr,
                                          r=True, r_val=base_ctrl_rot_getAttr)
            elif self.spine_type_combo_box_query == 'Animal':
                self.animal_spine_def()
                base_ctrl_name = self.prefix_name + '_' + self.spine_type + '_Spine_Base_Tem_' + str(self.val) + '_Ctrl'
                self.helper_class.set_val(ctrl_name=base_ctrl_name,
                                          t=True, t_val=base_ctrl_trans_getAttr,
                                          r=True, r_val=base_ctrl_rot_getAttr)
            elif self.spine_type_combo_box_query == 'Bird':
                pass
                print('this is something different')

    def get_grp_def(self):
        self.sphere_grp_name = self.prefix_name + '_' + self.spine_type + '_Spine_Tem_' + str(self.val) + "_Sphere_Grp"
        self.cluster_grp_name = self.prefix_name + '_' + self.spine_type + '_Spine_Tem_' + str(
            self.val) + "_Cluster_Grp"
        self.cylinder_group_name = self.prefix_name + '_' + self.spine_type + "_Spine_Tem_" + str(
            self.val) + "_Cylinder_Grp"
        self.ctrl_grp_name = self.prefix_name + '_' + self.spine_type + '_Spine_Tem_' + str(self.val) + "_Ctrl_Grp"

    def delete_breasr(self):
        # Template_Human_L_Spine_Breast_1_Tem_1_Ctrl
        # Template_Human_L_Spine_Breast_1_Tem_1_CluHandle
        # Template_Human_L_Spine_Breast_1_Tem_1_Geo
        common_name = self.prefix_name + '_' + self.spine_type + '_' + self.side + '_Spine_Breast_*_Tem_' + str(
            self.val)
        ctrl_name = common_name + '_Ctrl'
        clu_handle_name = common_name + '_CluHandle'
        geo_name = common_name + '_Geo'
        ctrl_grp_name = ctrl_name + '_Grp'
        cmds.select(ctrl_name, clu_handle_name, geo_name, ctrl_grp_name)
        cmds.delete()

    def spine_create(self):
        # get the data
        self.get_list_main_grp()
        # get the data
        for each_main_gro in self.total_main_grp:
            self.get_spine_data(each_main_gro)
            if self.spine_type == 'Human':
                self.final_spine()
            elif self.spine_type == 'Animal':
                self.final_spine()

    def get_list_main_grp(self):
        # Human_Spine_Grp
        grp_list = ['Human_Spine_Grp', 'Animal_Spine_Grp']
        self.total_main_grp = []
        for each_list in grp_list:
            if cmds.objExists(each_list):
                main_grp_list = cmds.listRelatives(each_list, c=True)
                if main_grp_list != None:
                    for each_main_grp in main_grp_list:
                        self.total_main_grp.append(each_main_grp)

    def get_spine_data(self, main_grp_name):
        split_main_grp = main_grp_name.split('_')
        self.prefix_name = split_main_grp[0]
        self.spine_type = split_main_grp[1]
        self.val = split_main_grp[4]

    def final_spine(self):
        # Template_Human_Spine_1_Tem_1_Ctrl
        # Template_Human_Spine_Base_Tem_1_Ctrl
        spine_ctrl_name = self.prefix_name + '_' + self.spine_type + '_Spine_*_Tem_' + str(self.val) + '_Ctrl'
        base_ctrl_name = self.prefix_name + '_' + self.spine_type + '_Spine_Base_Tem_' + str(self.val) + '_Ctrl'
        if cmds.objExists(spine_ctrl_name):
            cmds.select(spine_ctrl_name)
            if cmds.objExists(base_ctrl_name):
                cmds.select(base_ctrl_name, d=True)
            sel_spine = cmds.ls(sl=True)
            # CREATE A SPINE IN EACH AND EVERY POSITION
            self.result_jnt_list = []
            self.result_jnt = {}
            self.result_jnt_pos_list = []
            a = 0
            while a < len(sel_spine):
                # get the position
                spine_get_trans = cmds.xform(sel_spine[a], q=1, ws=1, rp=1)
                spine_get_rot = cmds.getAttr(sel_spine[a] + '.r')
                jnt_name = self.prefix_name + '_' + self.spine_type + '_Spine_' + str(a + 1) + '_' + str(
                    self.val) + '_Result_Jnt'
                cmds.select(cl=True)
                cmds.joint(n=jnt_name, p=(spine_get_trans[0],
                                          spine_get_trans[1],
                                          spine_get_trans[2]))
                self.result_jnt_list.append(jnt_name)
                self.result_jnt[jnt_name] = {}
                self.result_jnt[jnt_name]['Trans'] = spine_get_trans
                self.result_jnt[jnt_name]['Rot'] = spine_get_rot
                if a > 0:
                    previous_jnt = self.prefix_name + '_' + self.spine_type + '_Spine_' + str(a) + '_' + str(
                        self.val) + '_Result_Jnt'
                    cmds.select(jnt_name, previous_jnt)
                    cmds.parent()
                a += 1

            # joint -e  -oj xzy -secondaryAxisOrient xup -ch -zso;
            cmds.select(self.result_jnt_list[0])
            cmds.joint(e=True, oj='xzy', secondaryAxisOrient='xup', ch=True, zso=True)

            # create a ik spine
            # Create a Ik Handle
            ik_spine_handle_name = self.prefix_name + "_" + self.spine_type + "_Spine_Result_" + str(
                self.val) + "_Handle"
            crv_name = self.prefix_name + "_" + self.spine_type + "_Spine_" + str(self.val) + "_Crv"
            crv_shape_name = crv_name + "Shape"
            hand_create = cmds.ikHandle(n=ik_spine_handle_name, sj=self.result_jnt_list[0], ee=self.result_jnt_list[-1],
                                        sol='ikSplineSolver')
            cmds.rename(hand_create[2], crv_name)
            cmds.select(cl=True)
            cmds.setAttr((ik_spine_handle_name + ".v"), 0)
            cmds.setAttr((crv_name + ".v"), 0)
            cmds.setAttr((crv_name + ".inheritsTransform"), 0)
            # create a bing jnt
            hip_bind_jnt_name = self.prefix_name + "_" + self.spine_type + "_Spine_Hip_Bind_" + str(self.val) + "_Jnt"
            hip_bind_jnt_grp_name = hip_bind_jnt_name + '_Grp'
            shoulder_bind_jnt_name = self.prefix_name + "_" + self.spine_type + "_Spine_Shoulder_Bind_" + str(
                self.val) + "_Jnt"
            shoulder_bind_jnt_grp_name = shoulder_bind_jnt_name + '_Grp'
            cmds.select(cl=True)
            cmds.joint(n=hip_bind_jnt_name, p=(self.result_jnt[self.result_jnt_list[0]]['Trans'][0],
                                               self.result_jnt[self.result_jnt_list[0]]['Trans'][1],
                                               self.result_jnt[self.result_jnt_list[0]]['Trans'][2]))

            cmds.select(cl=True)
            cmds.joint(n=shoulder_bind_jnt_name, p=(self.result_jnt[self.result_jnt_list[-1]]['Trans'][0],
                                                    self.result_jnt[self.result_jnt_list[-1]]['Trans'][1],
                                                    self.result_jnt[self.result_jnt_list[-1]]['Trans'][2]))

            cmds.select(hip_bind_jnt_name, shoulder_bind_jnt_name, crv_name)
            cmds.SmoothBindSkin()

            shoulder_ctrl_name = self.prefix_name + "_" + self.spine_type + "_Spine_Shoulder_" + str(self.val) + "_Ctrl"
            shoulder_ctrl_grp_name = shoulder_ctrl_name + "_Const_Grp"
            hip_ctrl_name = self.prefix_name + "_" + self.spine_type + "_Spine_Hip_" + str(self.val) + "_Ctrl"
            hip_ctrl_grp_name = hip_ctrl_name + "_Const_Grp"
            self.controller_class.cube_ctrl()
            cmds.rename('cube_ctrl', shoulder_ctrl_name)
            self.controller_class.cube_ctrl()
            cmds.rename('cube_ctrl', hip_ctrl_name)
            cmds.parentConstraint(hip_bind_jnt_name, hip_ctrl_name, mo=False)
            cmds.parentConstraint(shoulder_bind_jnt_name, shoulder_ctrl_name, mo=False)
            cmds.select((shoulder_ctrl_name + "_parentConstraint1"), (hip_ctrl_name + "_parentConstraint1"))
            cmds.delete()
            cmds.select(shoulder_ctrl_name, hip_ctrl_name)
            cmds.DeleteHistory()
            cmds.FreezeTransformations()
            cmds.parentConstraint(hip_ctrl_name, hip_bind_jnt_name, mo=True)
            cmds.parentConstraint(shoulder_ctrl_name, shoulder_bind_jnt_name, mo=True)
            cmds.select(cl=True)
            cmds.select(shoulder_ctrl_name)
            cmds.group(n=shoulder_ctrl_grp_name)
            cmds.select(hip_ctrl_name)
            cmds.group(n=hip_ctrl_grp_name)
            cmds.select(cl=True)

            # setAttr "Template_Human_Spine_Hip_1_Ctrl.rotateOrder" 2;
            list = [hip_bind_jnt_name, shoulder_bind_jnt_name, hip_ctrl_name, shoulder_ctrl_name]
            for each in list:
                cmds.setAttr((each + '.rotateOrder'), 2)
            cmds.setAttr((ik_spine_handle_name + '.dTwistControlEnable'), 1)
            cmds.setAttr((ik_spine_handle_name + '.dWorldUpType'), 4)
            cmds.setAttr((ik_spine_handle_name + '.dWorldUpAxis'), 1)
            cmds.setAttr((ik_spine_handle_name + '.dWorldUpVectorX'), 0)
            cmds.setAttr((ik_spine_handle_name + '.dWorldUpVectorY'), -1)
            cmds.setAttr((ik_spine_handle_name + '.dWorldUpVectorZ'), 0)
            cmds.setAttr((ik_spine_handle_name + '.dWorldUpVectorEndX'), 0)
            cmds.setAttr((ik_spine_handle_name + '.dWorldUpVectorEndY'), 0)
            cmds.setAttr((ik_spine_handle_name + '.dWorldUpVectorEndZ'), -1)

            # create a selection set to set the name
            cmds.select(ik_spine_handle_name, hip_bind_jnt_name, shoulder_bind_jnt_name)
            set_name = self.prefix_name + "_" + self.spine_type + "_Spine_" + str(self.val) + "_Set"
            selection_set = cmds.sets()
            cmds.rename(selection_set, set_name)

            # create a fk control
            hip_fk_jnt_name = self.prefix_name + "_" + self.spine_type + "_Spine_Hip_" + str(self.val) + "_FK_Jnt"
            spine_1_fk_common_name = self.prefix_name + "_" + self.spine_type + "_Spine_1_" + str(self.val) + "_FK"
            spine_1_fk_jnt_name = spine_1_fk_common_name + "_Ctrl"
            spine_2_fk_common_name = self.prefix_name + "_" + self.spine_type + "_Spine_2_" + str(self.val) + "_FK"
            spine_2_fk_jnt_name = spine_2_fk_common_name + "_Ctrl"
            shoulder_fk_jnt_name = self.prefix_name + "_" + self.spine_type + "_Spine_Shoulder_" + str(
                self.val) + "_FK_Jnt"

            fk_name = [hip_fk_jnt_name, spine_1_fk_jnt_name, spine_2_fk_jnt_name, shoulder_fk_jnt_name]
            a = 0
            while a < 4:
                point_position = cmds.pointPosition(crv_name + '.cv[%s]' % a)
                jnt_name = fk_name[a]
                cmds.select(cl=True)
                cmds.joint(n=jnt_name, p=(point_position[0],
                                          point_position[1],
                                          point_position[2]))
                if a > 0:
                    previous_jnt = fk_name[a - 1]
                    cmds.select(jnt_name, previous_jnt)
                    cmds.parent()
                a += 1
            # make a joint orient proper
            cmds.select(hip_fk_jnt_name)
            cmds.joint(e=True, oj='yxz', secondaryAxisOrient='xup', ch=True, zso=True)
            for each in fk_name:
                cmds.setAttr((each + '.rotateOrder'), 1)
            cmds.parentConstraint(shoulder_fk_jnt_name, shoulder_ctrl_grp_name, mo=True)
            cmds.parentConstraint(hip_fk_jnt_name, hip_ctrl_grp_name, mo=True)

            # creeate a fk controller name
            self.controller_class.circle_ctrl()
            spine_1_fk_ctrl_name = spine_1_fk_common_name + '_New_Ctrl'
            spine_1_fk_ctrl_shape_name = spine_1_fk_ctrl_name + 'Shape'
            ctrl = cmds.ls(sl=True)
            cmds.rename(ctrl[0], spine_1_fk_ctrl_name)
            cmds.DeleteHistory()
            cmds.FreezeTransformations()
            cmds.select(spine_1_fk_ctrl_shape_name, spine_1_fk_jnt_name)
            cmds.parent(r=True, s=True)
            cmds.select(spine_1_fk_ctrl_name)
            cmds.delete()

            self.controller_class.circle_ctrl()
            spine_2_fk_ctrl_name = spine_2_fk_common_name + '_New_Ctrl'
            spine_2_fk_ctrl_shape_name = spine_2_fk_ctrl_name + 'Shape'
            ctrl = cmds.ls(sl=True)
            cmds.rename(ctrl[0], spine_2_fk_ctrl_name)
            cmds.DeleteHistory()
            cmds.FreezeTransformations()
            cmds.select(spine_2_fk_ctrl_shape_name, spine_2_fk_jnt_name)
            cmds.parent(r=True, s=True)
            cmds.select(spine_2_fk_ctrl_name)
            cmds.delete()

            # set the color
            ctrl_list = [shoulder_ctrl_name, hip_ctrl_name, spine_1_fk_jnt_name, spine_2_fk_jnt_name]
            for each in ctrl_list:
                self.helper_class.color_val(color='Yellow',
                                            obj_name=each)

            # CREATE A STRETCH AND SQUASH NODE
            # Create a Curve info node
            curve_info_node_name = self.prefix_name + "_" + self.spine_type + "_Spine_" + str(self.val) + "_Info"
            cmds.shadingNode('curveInfo', asUtility=True, n=curve_info_node_name)
            # connectAttr -f curveInfo1.arcLength multiplyDivide1.input1X;
            cmds.connectAttr((crv_shape_name + ".worldSpace[0]"), (curve_info_node_name + ".inputCurve"), f=True)

            spine_multiply_divide_node_name = self.prefix_name + "_" + self.spine_type + "_Spine_Stretch_" + str(
                self.val) + "_Mult_Div"
            cmds.shadingNode('multiplyDivide', asUtility=True, n=spine_multiply_divide_node_name)
            cmds.connectAttr((curve_info_node_name + ".arcLength"), (spine_multiply_divide_node_name + ".input1X"),
                             f=True)
            get_val = cmds.getAttr(curve_info_node_name + ".arcLength")
            # setAttr "multiplyDivide1.input2X" 5;
            cmds.setAttr((spine_multiply_divide_node_name + ".operation"), 2)
            cmds.setAttr((spine_multiply_divide_node_name + ".input2X"), get_val)

            spine_square_multiply_divide_node_name = self.prefix_name + "_" + self.spine_type + "_Spine_Square_Root_" + str(
                self.val) + "_Mult_Div"
            cmds.shadingNode('multiplyDivide', asUtility=True, n=spine_square_multiply_divide_node_name)
            cmds.connectAttr((spine_multiply_divide_node_name + ".outputX"),
                             (spine_square_multiply_divide_node_name + ".input1X"), f=True)
            cmds.setAttr((spine_square_multiply_divide_node_name + ".operation"), 3)
            cmds.setAttr((spine_square_multiply_divide_node_name + ".input2X"), 0.5)

            spine_square_multiply_inverse_divide_node_name = self.prefix_name + "_" + self.spine_type + "_Spine_Square_Root_inverse_" + str(
                self.val) + "_Mult_Div"
            cmds.shadingNode('multiplyDivide', asUtility=True, n=spine_square_multiply_inverse_divide_node_name)
            cmds.connectAttr((spine_square_multiply_divide_node_name + ".outputX"),
                             (spine_square_multiply_inverse_divide_node_name + ".input2X"), f=True)
            cmds.setAttr((spine_square_multiply_inverse_divide_node_name + ".operation"), 2)
            cmds.setAttr((spine_square_multiply_inverse_divide_node_name + ".input1X"), 1)

            a = 0
            while a < len(self.result_jnt_list):
                cmds.connectAttr((spine_multiply_divide_node_name + ".outputX"), (self.result_jnt_list[a] + ".scaleX"),
                                 f=True)
                cmds.connectAttr((spine_square_multiply_inverse_divide_node_name + ".outputX"),
                                 (self.result_jnt_list[a] + ".scaleY"), f=True)
                cmds.connectAttr((spine_square_multiply_inverse_divide_node_name + ".outputX"),
                                 (self.result_jnt_list[a] + ".scaleZ"), f=True)
                a += 1

            # CREATE A A BREAST
            # L BREAST
            # Template_Human_L_Spine_Breast_1_Tem_1_Ctrl
            breast_name = self.prefix_name + "_" + self.spine_type + "_L_Spine_Breast_*_Tem_" + str(self.val) + "_Ctrl"
            cmds.select(breast_name)
            sel_breast = cmds.ls(sl=True)
            cmds.select(cl=True)
            a = 0
            while a < len(sel_breast):
                # Template_Human_Spine_L_Breast_1_Tem_1_Ctrl
                plusOne = a + 1
                # get the position
                jnt_pos = cmds.xform(sel_breast[a], q=1, ws=1, rp=1)
                breast_common = self.prefix_name + "_" + self.spine_type + "_L_Spine_Breast_" + str(
                    plusOne) + "_" + str(self.val)
                spine_jnt_name = breast_common + "_Result_Jnt"
                spine_ctrl_name = breast_common + "_Ctrl"
                cmds.joint(n=spine_jnt_name, p=(jnt_pos[0], jnt_pos[1], jnt_pos[2]))
                self.controller_class.circle_ctrl()
                sel_ctrl = cmds.ls(sl=True)
                cmds.rename(sel_ctrl[0], spine_ctrl_name)
                cmds.move(jnt_pos[0], jnt_pos[1], jnt_pos[2])
                cmds.select(spine_ctrl_name)
                cmds.DeleteHistory()
                cmds.FreezeTransformations()
                self.helper_class.color_val(color='Red',
                                            obj_name=spine_ctrl_name)
                cmds.parentConstraint(spine_ctrl_name, spine_jnt_name, mo=True)
                l_breast_jnt_grp = self.prefix_name + "_" + self.spine_type + "_L_Spine_Breast_" + str(
                    self.val) + "_Jnt_Grp"
                if cmds.objExists(l_breast_jnt_grp):
                    cmds.select(spine_jnt_name, spine_ctrl_name, l_breast_jnt_grp)
                    cmds.parent()
                else:
                    cmds.select(spine_jnt_name, spine_ctrl_name)
                    cmds.group(n=l_breast_jnt_grp)

                self.helper_class.transform_rotation_scale_visible(spine_ctrl_name, t=False, r=True, s=True)
                cmds.select(cl=True)
                a += 1

            # R BREAST
            # Template_Human_L_Spine_Breast_1_Tem_1_Ctrl
            breast_name = self.prefix_name + "_" + self.spine_type + "_R_Spine_Breast_*_Tem_" + str(self.val) + "_Ctrl"
            cmds.select(breast_name)
            sel_breast = cmds.ls(sl=True)
            cmds.select(cl=True)
            a = 0
            while a < len(sel_breast):
                # Template_Human_Spine_L_Breast_1_Tem_1_Ctrl
                plusOne = a + 1
                # get the position
                jnt_pos = cmds.xform(sel_breast[a], q=1, ws=1, rp=1)
                breast_common = self.prefix_name + "_" + self.spine_type + "_R_Spine_Breast_" + str(
                    plusOne) + "_" + str(self.val)
                spine_jnt_name = breast_common + "_Result_Jnt"
                spine_ctrl_name = breast_common + "_Ctrl"
                cmds.joint(n=spine_jnt_name, p=(jnt_pos[0], jnt_pos[1], jnt_pos[2]))
                self.controller_class.circle_ctrl()
                sel_ctrl = cmds.ls(sl=True)
                cmds.rename(sel_ctrl[0], spine_ctrl_name)
                cmds.move(jnt_pos[0], jnt_pos[1], jnt_pos[2])
                cmds.select(spine_ctrl_name)
                cmds.DeleteHistory()
                cmds.FreezeTransformations()
                self.helper_class.color_val(color='Blue',
                                            obj_name=spine_ctrl_name)
                cmds.parentConstraint(spine_ctrl_name, spine_jnt_name, mo=True)
                r_breast_jnt_grp = self.prefix_name + "_" + self.spine_type + "_R_Spine_Breast_" + str(
                    self.val) + "_Jnt_Grp"
                if cmds.objExists(r_breast_jnt_grp):
                    cmds.select(spine_jnt_name, spine_ctrl_name, r_breast_jnt_grp)
                    cmds.parent()
                else:
                    cmds.select(spine_jnt_name, spine_ctrl_name)
                    cmds.group(n=r_breast_jnt_grp)

                self.helper_class.transform_rotation_scale_visible(spine_ctrl_name, t=False, r=True, s=True)
                cmds.select(cl=True)
                a += 1

            cmds.parentConstraint(spine_2_fk_jnt_name, l_breast_jnt_grp, mo=True)
            cmds.parentConstraint(spine_2_fk_jnt_name, r_breast_jnt_grp, mo=True)

            # Create a Body Control
            body_ctrl = self.prefix_name + "_" + self.spine_type + "_Spine_Body_" + str(self.val) + "_Ctrl"
            self.controller_class.square_ctrl()
            cmds.rename('Square_ctrl', body_ctrl)
            cmds.parentConstraint(hip_fk_jnt_name, body_ctrl, mo=False)
            cmds.select(body_ctrl + "_parentConstraint1")
            cmds.delete()
            cmds.setAttr((body_ctrl + ".ry"), 90)
            cmds.select(body_ctrl)
            cmds.DeleteHistory()
            cmds.FreezeTransformations()
            self.helper_class.color_val(color='Yellow',
                                        obj_name=body_ctrl)

            # "Template_Human_Spine_1_Crv.inheritsTransform" 0;

            # Create a Torso Grp
            torso_grp_name = self.prefix_name + "_" + self.spine_type + "_Spine_Torso_" + str(self.val) + "_Grp"

            cmds.select(self.result_jnt_list[0], ik_spine_handle_name, crv_name,
                        hip_bind_jnt_name, shoulder_bind_jnt_name, hip_ctrl_grp_name,
                        shoulder_ctrl_grp_name, hip_fk_jnt_name, l_breast_jnt_grp, r_breast_jnt_grp)
            cmds.group(n=torso_grp_name)
            cmds.parentConstraint(body_ctrl, torso_grp_name, mo=True)

            cmds.select(self.result_jnt_list[0], ik_spine_handle_name, crv_name, hip_bind_jnt_name,
                        shoulder_bind_jnt_name)
            spine_do_not_touch_grp = self.prefix_name + "_" + self.spine_type + "_Spine_DO_NOT_TOUCH_" + str(
                self.val) + "_Grp"
            cmds.group(n=spine_do_not_touch_grp)

            # make a center Grp and add to the list
            root_grp_name = "Root_Grp"
            if cmds.objExists(root_grp_name):
                cmds.select(torso_grp_name, body_ctrl, root_grp_name)
                cmds.parent()
            else:
                cmds.createNode('transform', n=root_grp_name)
                cmds.select(torso_grp_name, body_ctrl, root_grp_name)
                cmds.parent()

            # ADD ATTR TO THE BODY_CONTROLLER
            cmds.addAttr(body_ctrl, ln="Spine_Result_Vis", at='enum', en='Off:On')
            cmds.setAttr((body_ctrl + ".Spine_Result_Vis"), e=True, keyable=True)
            cmds.connectAttr((body_ctrl + '.Spine_Result_Vis'), (self.result_jnt_list[0] + '.v'))

            # create a Multiply dive scale to the crv
            spine_normalise_div = self.prefix_name + "_" + self.spine_type + "_Spine_Global_Scale_Spine_Normalise_" + str(
                self.val) + "_Div"
            cmds.shadingNode('multiplyDivide', asUtility=True, n=spine_normalise_div)
            cmds.connectAttr((curve_info_node_name + ".arcLength"), (spine_normalise_div + ".input1X"), f=True)
            cmds.connectAttr((root_grp_name + ".sy"), (spine_normalise_div + ".input2X"), f=True)
            cmds.setAttr((spine_normalise_div + ".operation"), 2)
            cmds.disconnectAttr((curve_info_node_name + ".arcLength"), (spine_multiply_divide_node_name + ".input1X"))
            cmds.connectAttr((spine_normalise_div + ".outputX"), (spine_multiply_divide_node_name + ".input1X"), f=True)

            lock_and_hid_list = [torso_grp_name, shoulder_bind_jnt_name, hip_ctrl_grp_name, hip_fk_jnt_name,
                                 shoulder_fk_jnt_name,
                                 hip_bind_jnt_name, shoulder_bind_jnt_name, spine_do_not_touch_grp,
                                 ik_spine_handle_name]
            for each in lock_and_hid_list:
                self.helper_class.transform_rotation_scale_visible(each, v=False)

            # lock and hide transform
            list = [spine_1_fk_jnt_name, spine_2_fk_jnt_name]
            for each in list:
                self.helper_class.transform_rotation_scale_visible(each, t=True, r=False, s=False)
            # lock and hide scale
            list = [spine_1_fk_jnt_name, spine_2_fk_jnt_name, body_ctrl, hip_ctrl_name, shoulder_ctrl_name]
            for each in list:
                self.helper_class.transform_rotation_scale_visible(each, t=False, r=False, s=True)

    def bone_def(self):
        # get the data
        self.get_list_main_grp()
        # get the data
        for each_main_gro in self.total_main_grp:
            self.get_spine_data(each_main_gro)

            self.final_bone_spine()

    def controller_twick_def(self):
        # get the data
        self.get_list_main_grp()
        # get the data
        for each_main_gro in self.total_main_grp:
            self.get_spine_data(each_main_gro)

            self.final_controller_def()

    def final_controller_def(self):
        grp_name = self.prefix_name + '_' + self.spine_type + '_Spine_' + str(self.val) + '_Twick_Ctrl_Grp'
        main_grp_name = 'Spine_Twick_Ctrl_Grp'

        spine_ctrl_name = self.prefix_name + '_' + self.spine_type + '_Spine_*_Tem_' + str(self.val) + '_Ctrl'
        base_ctrl_name = self.prefix_name + '_' + self.spine_type + '_Spine_Base_Tem_' + str(self.val) + '_Ctrl'
        if cmds.objExists(spine_ctrl_name):
            cmds.select(spine_ctrl_name)
            if cmds.objExists(base_ctrl_name):
                cmds.select(base_ctrl_name, d=True)
            sel_spine = cmds.ls(sl=True)
            a = 0
            while a < len(sel_spine):
                get_pos = cmds.xform(sel_spine[a], q=1, ws=1, rp=1)
                get_rot = cmds.xform(sel_spine[a], q=1, rotation=1)

                self.controller_class.circle_ctrl()
                ctrl_name = sel_spine[a].split('_Ctrl')[0] + '_Twick_Ctrl'
                cmds.rename('circle_ctrl', ctrl_name)

                cmds.setAttr((ctrl_name + '.tx'), get_pos[0])
                cmds.setAttr((ctrl_name + '.ty'), get_pos[1])
                cmds.setAttr((ctrl_name + '.tz'), get_pos[2])

                cmds.setAttr((ctrl_name + '.rx'), get_rot[0])
                cmds.setAttr((ctrl_name + '.ry'), get_rot[1])
                cmds.setAttr((ctrl_name + '.rz'), get_rot[2])

                self.helper_class.color_val(color='Yellow',
                                            obj_name=ctrl_name)

                self.helper_class.grp_create(object_name=ctrl_name,
                                             grp_name=grp_name)
                a += 1

        # Template_Human_L_Spine_Breast_1_Tem_1_Ctrl
        l_breast_ctrl = self.prefix_name + '_' + self.spine_type + '_L_Spine_Breast_*_Tem_' + str(self.val) + '_Ctrl'
        r_breast_ctrl = self.prefix_name + '_' + self.spine_type + '_R_Spine_Breast_*_Tem_' + str(self.val) + '_Ctrl'
        cmds.select(cl=True)
        if cmds.objExists(l_breast_ctrl):
            cmds.select(l_breast_ctrl)
            sel_ctrl = cmds.ls(sl=True)
            for each in sel_ctrl:
                get_pos = cmds.xform(each, q=1, ws=1, rp=1)
                get_rot = cmds.xform(each, q=1, rotation=1)

                self.controller_class.circle_ctrl()
                ctrl_name = each.split('_Ctrl')[0] + '_Twick_Ctrl'
                cmds.rename('circle_ctrl', ctrl_name)
                cmds.setAttr((ctrl_name + '.tx'), get_pos[0])
                cmds.setAttr((ctrl_name + '.ty'), get_pos[1])
                cmds.setAttr((ctrl_name + '.tz'), get_pos[2])

                cmds.setAttr((ctrl_name + '.rx'), get_rot[0])
                cmds.setAttr((ctrl_name + '.ry'), get_rot[1])
                cmds.setAttr((ctrl_name + '.rz'), get_rot[2])

                self.helper_class.color_val(color='Blue',
                                            obj_name=ctrl_name)

                self.helper_class.grp_create(object_name=ctrl_name,
                                             grp_name=grp_name)

        if cmds.objExists(r_breast_ctrl):
            cmds.select(r_breast_ctrl)
            sel_ctrl = cmds.ls(sl=True)
            for each in sel_ctrl:
                get_pos = cmds.xform(each, q=1, ws=1, rp=1)
                get_rot = cmds.xform(each, q=1, rotation=1)

                self.controller_class.circle_ctrl()
                ctrl_name = each.split('_Ctrl')[0] + '_Twick_Ctrl'
                cmds.rename('circle_ctrl', ctrl_name)
                cmds.setAttr((ctrl_name + '.tx'), get_pos[0])
                cmds.setAttr((ctrl_name + '.ty'), get_pos[1])
                cmds.setAttr((ctrl_name + '.tz'), get_pos[2])

                cmds.setAttr((ctrl_name + '.rx'), get_rot[0])
                cmds.setAttr((ctrl_name + '.ry'), get_rot[1])
                cmds.setAttr((ctrl_name + '.rz'), get_rot[2])

                self.helper_class.color_val(color='Red',
                                            obj_name=ctrl_name)

                self.helper_class.grp_create(object_name=ctrl_name,
                                             grp_name=grp_name)

        self.helper_class.grp_create(object_name=grp_name,
                                     grp_name=main_grp_name)

    def final_bone_spine(self):
        grp_namne = self.prefix_name + '_' + self.spine_type + '_Spine_Bone_' + str(self.val) + '_Grp'
        main_grp_name = 'Spine_Bone_Grp'

        spine_ctrl_name = self.prefix_name + '_' + self.spine_type + '_Spine_*_Tem_' + str(self.val) + '_Ctrl'
        base_ctrl_name = self.prefix_name + '_' + self.spine_type + '_Spine_Base_Tem_' + str(self.val) + '_Ctrl'
        if cmds.objExists(spine_ctrl_name):
            cmds.select(spine_ctrl_name)
            if cmds.objExists(base_ctrl_name):
                cmds.select(base_ctrl_name, d=True)
            sel_spine = cmds.ls(sl=True)
            a = 0
            while a < len(sel_spine):

                common_name = sel_spine[a].split('_Ctrl')[0]
                bone_name = common_name + '_Bone'
                ctrl_pos = cmds.xform(sel_spine[a], q=1, ws=1, rp=1)
                cmds.select(cl=True)
                cmds.joint(n=bone_name, p=(ctrl_pos[0], ctrl_pos[1], ctrl_pos[2]))
                if a > 0:
                    p_commmon = sel_spine[a - 1].split('_Ctrl')[0]
                    previous_bone = p_commmon + '_Bone'
                    cmds.parent(bone_name, previous_bone)
                else:
                    first_jnt_name = bone_name
                a += 1

            self.helper_class.grp_create(object_name=first_jnt_name,
                                         grp_name=grp_namne)

            # Template_Human_L_Spine_Breast_1_Tem_1_Ctrl
            l_breast_ctrl = self.prefix_name + '_' + self.spine_type + '_L_Spine_Breast_*_Tem_' + str(
                self.val) + '_Ctrl'
            if cmds.objExists(l_breast_ctrl):
                cmds.select(l_breast_ctrl)
            r_breast_ctrl = self.prefix_name + '_' + self.spine_type + '_R_Spine_Breast_*_Tem_' + str(
                self.val) + '_Ctrl'
            if cmds.objExists(r_breast_ctrl):
                cmds.select(r_breast_ctrl, add=True)

            sel_breast = cmds.ls(sl=True)
            for each in sel_breast:
                common_name = each.split('_Ctrl')[0]
                bone_name = common_name + '_Bone'
                get_pos = cmds.xform(each, q=1, ws=1, rp=1)
                cmds.select(cl=True)
                cmds.joint(n=bone_name, p=(get_pos[0], get_pos[1], get_pos[2]))

                self.helper_class.grp_create(object_name=bone_name,
                                             grp_name=grp_namne)

            self.helper_class.grp_create(object_name=grp_namne,
                                         grp_name=main_grp_name)

    def get_spine(self):
        list = []
        # Human_Spine_Grp
        grp_list = ['Human_Spine_Grp', 'Animal_Spine_Grp']
        self.total_main_grp = []
        for each_list in grp_list:
            if cmds.objExists(each_list):
                main_grp_list = cmds.listRelatives(each_list, c=True)
                if main_grp_list != None:
                    for each_main_grp in main_grp_list:
                        list.append(each_main_grp)

        return len(list)




