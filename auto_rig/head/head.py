



class HEAD:
    def __init__(self):
        self.helper_class = helper.HELPER()
        self.controller_class = controller_rig.controler()

        self.head_attr_data = {}

    # NEW WINDOW UI
    def new(self, widget, layout):
        self.head_grid_layout = QtGui.QGridLayout()
        self.head_grid_layout.setObjectName("head_grid_layout")

        # LEFT EYE LABEL
        self.left_eye_label = QtGui.QLabel(widget)
        self.left_eye_label.setObjectName("left_eye_label")
        self.left_eye_label.setText('Left Eye')
        self.head_grid_layout.addWidget(self.left_eye_label, 0, 0, 1, 1)
        # LEFT EYE LINE EDIT
        self.left_eye_line_edit = QtGui.QLineEdit(widget)
        self.left_eye_line_edit.setObjectName("left_eye_line_edit")
        self.validator = QtGui.QDoubleValidator()
        self.left_eye_line_edit.setValidator(self.validator)
        self.left_eye_line_edit.setText(str(1))
        self.head_grid_layout.addWidget(self.left_eye_line_edit, 0, 1, 1, 1)

        # RIGHT EYE LABEL
        self.right_eye_label = QtGui.QLabel(widget)
        self.right_eye_label.setObjectName("right_eye_label")
        self.right_eye_label.setText('Right Eye')
        self.head_grid_layout.addWidget(self.right_eye_label, 1, 0, 1, 1)
        # RIGHT EYE LINE EDIT
        self.right_eye_line_edit = QtGui.QLineEdit(widget)
        self.right_eye_line_edit.setObjectName("right_eye_line_edit")
        self.right_eye_line_edit.setValidator(self.validator)
        self.right_eye_line_edit.setText(str(1))
        self.head_grid_layout.addWidget(self.right_eye_line_edit, 1, 1, 1, 1)

        # TYPE COMBO BOX
        self.type_combo_box = QtGui.QComboBox(widget)
        self.type_combo_box.setObjectName("type_combo_box")
        self.type_combo_box.addItem("Human")
        self.type_combo_box.addItem("Animal")
        self.type_combo_box.addItem("Bird")
        self.head_grid_layout.addWidget(self.type_combo_box, 2, 0, 1, 2)

        # HEAD CREATE BUTTON
        self.head_create_button = QtGui.QPushButton(widget)
        self.head_create_button.setObjectName("head_create_button")
        self.head_create_button.setText('Create Head')
        self.head_create_button.clicked.connect(self.new_create_def)
        self.head_grid_layout.addWidget(self.head_create_button, 3, 0, 1, 2)

        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.head_grid_layout.addItem(spacerItem, 4, 0, 1, 1)

        layout.addLayout(self.head_grid_layout)

    def new_create_def(self):
        # GET THE VALUE
        self.left_eye_query = int(self.left_eye_line_edit.text())
        self.right_eye_query = int(self.right_eye_line_edit.text())
        self.combo_box_value = self.type_combo_box.currentText()

        self.prefix_name = 'Template'

        if self.combo_box_value == 'Human':
            self.human_head_def()
        elif self.combo_box_value == 'Animal':
            self.animal_head_def()
        elif self.combo_box_value == 'Bird':
            self.animal_head_def()

    def human_head_def(self):
        self.type = 'Human'
        self.main_group_name = '*_' + self.type + '_Head_Tem_*_Main_Grp'
        if cmds.objExists(self.main_group_name):
            cmds.select(self.main_group_name)
            sel_main_grp = cmds.ls(sl=True)
            self.val = len(sel_main_grp) + 1
        else:
            self.val = 1

        # set the defalult position
        self.base_pos = [0, 0, 0]
        self.neck_pos = [0, 0, 0]
        self.head_pos = [0, 9.958, 2.056]
        self.head_top_pos = [0, 31.339, 3.198]
        self.lower_mouth_pos = [0, 4.665, 13.597]
        self.upper_mouth_pos = [0, 9.328, 15.108]
        self.left_ear_pos = [9.42, 14.506, -0.042]
        self.right_ear_pos = [-8.42, 14.506, -0.042]
        self.left_eye_pos = [4.999, 15.786, 10.84]
        self.right_eye_pos = [-5.449, 15.786, 10.84]

        # create a sphere
        self.head_sphere_def()

        # create a cylinder
        self.head_cylinder_def()

        # CREATE CONTROLLER
        # BASE
        self.base_ctrl_size = [0.5, 0.5, 0.5]
        self.base_ctrl_rotate = [0, 0, 0]
        self.base_ctrl_color = 'Yellow'
        self.base_ctrl_freez_trans = True
        self.base_ctrl_freez_rotate = True
        self.base_ctrl_freez_scale = True

        # NECK
        self.neck_ctrl_size = [1.5, 1.5, 1.5]
        self.neck_ctrl_rotate = [0, 0, 0]
        self.neck_ctrl_color = 'Yellow'
        self.neck_ctrl_freez_trans = True
        self.neck_ctrl_freez_rotate = True
        self.neck_ctrl_freez_scale = True

        # HEAD
        self.head_ctrl_size = [1.5, 1.5, 1.5]
        self.head_ctrl_rotate = [0, 0, 0]
        self.head_ctrl_color = 'Yellow'
        self.head_ctrl_freez_trans = True
        self.head_ctrl_freez_rotate = True
        self.head_ctrl_freez_scale = True

        # LOERT MOUTH
        self.lower_mouth_ctrl_size = [0.5, 0.5, 0.5]
        self.lower_mouth_ctrl_rotate = [90, 0, 0]
        self.lower_mouth_ctrl_color = 'Yellow'
        self.lower_mouth_ctrl_freez_trans = True
        self.lower_mouth_ctrl_freez_rotate = True
        self.lower_mouth_ctrl_freez_scale = True

        # UPPER MPUTH
        self.upper_mouth_ctrl_size = [0.5, 0.5, 0.5]
        self.upper_mouth_ctrl_rotate = [90, 0, 0]
        self.upper_mouth_ctrl_color = 'Yellow'
        self.upper_mouth_ctrl_freez_trans = True
        self.upper_mouth_ctrl_freez_rotate = True
        self.upper_mouth_ctrl_freez_scale = True

        # HEAD TOP
        self.head_top_ctrl_size = [1.5, 1.5, 1.5]
        self.head_top_ctrl_rotate = [0, 0, 0]
        self.head_top_ctrl_color = 'Yellow'
        self.head_top_ctrl_freez_trans = True
        self.head_top_ctrl_freez_rotate = True
        self.head_top_ctrl_freez_scale = True

        # LEFT EAR
        self.left_ear_ctrl_size = [0.5, 0.5, 0.5]
        self.left_ear_ctrl_rotate = [0, 0, 90]
        self.left_ear_ctrl_color = 'Red'
        self.left_ear_ctrl_freez_trans = True
        self.left_ear_ctrl_freez_rotate = True
        self.left_ear_ctrl_freez_scale = True

        # RIGHT EAR
        self.right_ear_ctrl_size = [0.5, 0.5, 0.5]
        self.right_ear_ctrl_rotate = [0, 0, 90]
        self.right_ear_ctrl_color = 'Blue'
        self.right_ear_ctrl_freez_trans = True
        self.right_ear_ctrl_freez_rotate = True
        self.right_ear_ctrl_freez_scale = True

        self.controller_def()

        # left_eye

        self.eye(self.left_eye_pos, 'Left', 'Red', self.left_eye_query)
        self.eye(self.right_eye_pos, 'Right', 'Blue', self.right_eye_query)

        # put everything in one group
        self.human_head_grp = 'Human_Head_Grp'
        if cmds.objExists(self.human_head_grp):
            cmds.select(self.main_group_name, self.human_head_grp)
            cmds.parent()
        else:
            cmds.select(self.main_group_name)
            cmds.group(n=self.human_head_grp)
            self.helper_class.transform_rotation_scale_visible(self.human_head_grp)

        self.head_grp = 'Head_Grp'
        if cmds.objExists(self.head_grp):
            parent_obj = cmds.listRelatives(self.human_head_grp, p=True)
            if parent_obj == None:
                cmds.select(self.human_head_grp, self.head_grp)
                cmds.parent()
        else:
            cmds.select(self.human_head_grp)
            cmds.group(n=self.head_grp)
            self.helper_class.transform_rotation_scale_visible(self.head_grp, v=False)

    def animal_head_def(self):
        self.type = 'Animal'
        self.main_group_name = '*_' + self.type + '_Head_Tem_*_Main_Grp'
        if cmds.objExists(self.main_group_name):
            cmds.select(self.main_group_name)
            sel_main_grp = cmds.ls(sl=True)
            self.val = len(sel_main_grp) + 1
        else:
            self.val = 1

        # set the defalult position
        self.base_pos = [0, 0, 0]
        self.neck_pos = [0, 0, 0]
        self.head_pos = [0, 5.769, 5.631]
        self.head_top_pos = [0, 12.851, 6.136]
        self.lower_mouth_pos = [0, 1.386, 15.772]
        self.upper_mouth_pos = [0, 4.179, 18.565]
        self.left_ear_pos = [4.022, 10.3, 5.064]
        self.right_ear_pos = [-3.642, 10.3, 5.064]
        self.left_eye_pos = [2.026, 8.391, 11.297]
        self.right_eye_pos = [-2.095, 8.391, 11.297]

        # create a sphere
        self.head_sphere_def()

        # create a cylinder
        self.head_cylinder_def()

        # CREATE CONTROLLER
        # BASE
        self.base_ctrl_size = [0.5, 0.5, 0.5]
        self.base_ctrl_rotate = [0, 0, 0]
        self.base_ctrl_color = 'Yellow'
        self.base_ctrl_freez_trans = True
        self.base_ctrl_freez_rotate = True
        self.base_ctrl_freez_scale = True

        # NECK
        self.neck_ctrl_size = [1.5, 1.5, 1.5]
        self.neck_ctrl_rotate = [70, 0, 0]
        self.neck_ctrl_color = 'Yellow'
        self.neck_ctrl_freez_trans = True
        self.neck_ctrl_freez_rotate = False
        self.neck_ctrl_freez_scale = True

        # HEAD
        self.head_ctrl_size = [1.5, 1.5, 1.5]
        self.head_ctrl_rotate = [45, 0, 0]
        self.head_ctrl_color = 'Yellow'
        self.head_ctrl_freez_trans = True
        self.head_ctrl_freez_rotate = False
        self.head_ctrl_freez_scale = True

        # LOWER MOUTH
        self.lower_mouth_ctrl_size = [0.5, 0.5, 0.5]
        self.lower_mouth_ctrl_rotate = [90, 0, 0]
        self.lower_mouth_ctrl_color = 'Yellow'
        self.lower_mouth_ctrl_freez_trans = True
        self.lower_mouth_ctrl_freez_rotate = True
        self.lower_mouth_ctrl_freez_scale = True

        # UPPER MOUTH
        self.upper_mouth_ctrl_size = [0.5, 0.5, 0.5]
        self.upper_mouth_ctrl_rotate = [90, 0, 0]
        self.upper_mouth_ctrl_color = 'Yellow'
        self.upper_mouth_ctrl_freez_trans = True
        self.upper_mouth_ctrl_freez_rotate = True
        self.upper_mouth_ctrl_freez_scale = True

        # HEAD TOP
        self.head_top_ctrl_size = [1.5, 1.5, 1.5]
        self.head_top_ctrl_rotate = [0, 0, 0]
        self.head_top_ctrl_color = 'Yellow'
        self.head_top_ctrl_freez_trans = True
        self.head_top_ctrl_freez_rotate = True
        self.head_top_ctrl_freez_scale = True

        # LEFT EAR
        self.left_ear_ctrl_size = [0.5, 0.5, 0.5]
        self.left_ear_ctrl_rotate = [0, 0, 90]
        self.left_ear_ctrl_color = 'Red'
        self.left_ear_ctrl_freez_trans = True
        self.left_ear_ctrl_freez_rotate = True
        self.left_ear_ctrl_freez_scale = True

        # RIGHT EAR
        self.right_ear_ctrl_size = [0.5, 0.5, 0.5]
        self.right_ear_ctrl_rotate = [0, 0, 90]
        self.right_ear_ctrl_color = 'Blue'
        self.right_ear_ctrl_freez_trans = True
        self.right_ear_ctrl_freez_rotate = True
        self.right_ear_ctrl_freez_scale = True

        self.controller_def()

        # left_eye
        self.eye(self.left_eye_pos, 'Left', 'Red', self.left_eye_query)
        self.eye(self.right_eye_pos, 'Right', 'Blue', self.right_eye_query)

        # put everything in one group
        self.animal_head_grp = 'Animal_Head_Grp'
        if cmds.objExists(self.animal_head_grp):
            cmds.select(self.main_group_name, self.animal_head_grp)
            cmds.parent()
        else:
            cmds.select(self.main_group_name)
            cmds.group(n=self.animal_head_grp)
            self.helper_class.transform_rotation_scale_visible(self.animal_head_grp)

        self.head_grp = 'Head_Grp'
        if cmds.objExists(self.head_grp):
            # get the parent
            parent_obj = cmds.listRelatives(self.animal_head_grp, p=True)
            if parent_obj == None:
                cmds.select(self.animal_head_grp, self.head_grp)
                cmds.parent()
        else:
            cmds.select(self.animal_head_grp)
            cmds.group(n=self.head_grp)
            self.helper_class.transform_rotation_scale_visible(self.head_grp)

    def head_sphere_def(self):

        # create a sphere on each position
        # Base
        self.base_sphere_name = self.prefix_name + '_' + self.type + '_Head_Base_Tem_' + str(self.val) + '_Geo'
        self.base_sphere_clu_name = self.prefix_name + '_' + self.type + '_Head_Base_Tem_' + str(self.val) + '_Clu'
        self.base_sphere_clu_handle_name = self.base_sphere_clu_name + 'Handle'
        self.helper_class.set_sphere_position(self.base_sphere_name, self.base_pos, self.base_sphere_clu_name)

        # Neck
        self.neck_sphere_name = self.prefix_name + '_' + self.type + '_Head_Neck_Tem_' + str(self.val) + '_Geo'
        self.neck_sphere_clu_name = self.prefix_name + '_' + self.type + '_Head_Neck_Tem_' + str(self.val) + '_Clu'
        self.neck_sphere_clu_handle_name = self.neck_sphere_clu_name + 'Handle'
        self.helper_class.set_sphere_position(self.neck_sphere_name, self.neck_pos, self.neck_sphere_clu_name)

        # Head
        self.head_sphere_name = self.prefix_name + '_' + self.type + '_Head_Head_Tem_' + str(self.val) + '_Geo'
        self.head_sphere_clu_name = self.prefix_name + '_' + self.type + '_Head_Head_Tem_' + str(self.val) + '_Clu'
        self.head_sphere_clu_handle_name = self.head_sphere_clu_name + 'Handle'
        self.helper_class.set_sphere_position(self.head_sphere_name, self.head_pos, self.head_sphere_clu_name)

        # HEAD TOP
        self.head_top_sphere_name = self.prefix_name + '_' + self.type + '_Head_Head_Top_Tem_' + str(self.val) + '_Geo'
        self.head_top_sphere_clu_name = self.prefix_name + '_' + self.type + '_Head_Head_Top_Tem_' + str(
            self.val) + '_Clu'
        self.head_top_sphere_clu_handle_name = self.head_top_sphere_clu_name + 'Handle'
        self.helper_class.set_sphere_position(self.head_top_sphere_name, self.head_top_pos,
                                              self.head_top_sphere_clu_name)

        # LOWER MOUTH
        self.lower_mouth_sphere_name = self.prefix_name + '_' + self.type + '_Head_Lower_Mouth_Tem_' + str(
            self.val) + '_Geo'
        self.lower_mouth_sphere_clu_name = self.prefix_name + '_' + self.type + '_Head_Lower_Mouth_Tem_' + str(
            self.val) + '_Clu'
        self.lower_mouth_sphere_clu_handle_name = self.lower_mouth_sphere_clu_name + 'Handle'
        self.helper_class.set_sphere_position(self.lower_mouth_sphere_name, self.lower_mouth_pos,
                                              self.lower_mouth_sphere_clu_name)

        # UPPER MOUTH
        self.upper_mouth_sphere_name = self.prefix_name + '_' + self.type + '_Head_Upper_Mouth_Tem_' + str(
            self.val) + '_Geo'
        self.upper_mouth_sphere_clu_name = self.prefix_name + '_' + self.type + '_Head_Upper_Mouth_Tem_' + str(
            self.val) + '_Clu'
        self.upper_mouth_sphere_clu_handle_name = self.upper_mouth_sphere_clu_name + 'Handle'
        self.helper_class.set_sphere_position(self.upper_mouth_sphere_name, self.upper_mouth_pos,
                                              self.upper_mouth_sphere_clu_name)

        # LEFT EAR
        self.left_ear_sphere_name = self.prefix_name + '_' + self.type + '_Head_Left_Ear_Tem_' + str(self.val) + '_Geo'
        self.left_ear_sphere_clu_name = self.prefix_name + '_' + self.type + '_Head_Left_Ear_Tem_' + str(
            self.val) + '_Clu'
        self.left_ear_sphere_clu_handle_name = self.left_ear_sphere_clu_name + 'Handle'
        self.helper_class.set_sphere_position(self.left_ear_sphere_name, self.left_ear_pos,
                                              self.left_ear_sphere_clu_name)

        # RIGHT EAR
        self.right_ear_sphere_name = self.prefix_name + '_' + self.type + '_Head_Right_Ear_Tem_' + str(
            self.val) + '_Geo'
        self.right_ear_sphere_clu_name = self.prefix_name + '_' + self.type + '_Head_Right_Ear_Tem_' + str(
            self.val) + '_Clu'
        self.right_ear_sphere_clu_handle_name = self.right_ear_sphere_clu_name + 'Handle'
        self.helper_class.set_sphere_position(self.right_ear_sphere_name, self.right_ear_pos,
                                              self.right_ear_sphere_clu_name)

        # put the sphere in the group
        cmds.select(self.base_sphere_name, self.neck_sphere_name, self.head_sphere_name,
                    self.head_top_sphere_name, self.lower_mouth_sphere_name, self.upper_mouth_sphere_name,
                    self.left_ear_sphere_name, self.right_ear_sphere_name)
        self.sphere_group_name = self.prefix_name + '_' + self.type + "_Head_Face_Tem_" + str(self.val) + "_Sphere_Grp"
        cmds.group(n=self.sphere_group_name)
        self.helper_class.transform_rotation_scale_visible(self.sphere_group_name)

    def head_cylinder_def(self):

        # SET THE CYLINDER
        # NECK TO FACE CYLINDER
        self.base_to_neck_cylinder_name = self.prefix_name + '_' + self.type + '_Head_Base_to_Neck_Tem_' + str(
            self.val) + '_Geo'
        self.base_to_neck_lower_cylinder_cluster_name = self.prefix_name + '_' + self.type + '_Head_Base_to_Neck_Lower_Tem_' + str(
            self.val) + '_Clu'
        self.base_to_neck_lower_cylinder_cluster_handle_name = self.base_to_neck_lower_cylinder_cluster_name + 'Handle'
        self.base_to_neck_upper_cylinder_cluster_name = self.prefix_name + '_' + self.type + '_Head_Base_to_Neck_Upper_Tem_' + str(
            self.val) + '_Clu'
        self.base_to_neck_upper_cylinder_cluster_handle_name = self.base_to_neck_upper_cylinder_cluster_name + 'Handle'

        self.helper_class.set_cylinder_position(self.base_to_neck_cylinder_name,
                                                self.base_to_neck_lower_cylinder_cluster_name,
                                                self.base_to_neck_upper_cylinder_cluster_name,
                                                self.neck_sphere_name,
                                                self.base_sphere_name)
        # NECK TO FACE CYLINDER
        self.neck_to_face_cylinder_name = self.prefix_name + '_' + self.type + '_Head_Neck_to_Face_Tem_' + str(
            self.val) + '_Geo'
        self.neck_to_face_lower_cylinder_cluster_name = self.prefix_name + '_' + self.type + '_Head_Neck_to_Face_Lower_Tem_' + str(
            self.val) + '_Clu'
        self.neck_to_face_lower_cylinder_cluster_handle_name = self.neck_to_face_lower_cylinder_cluster_name + 'Handle'
        self.neck_to_face_upper_cylinder_cluster_name = self.prefix_name + '_' + self.type + '_Head_Neck_to_Face_Upper_Tem_' + str(
            self.val) + '_Clu'
        self.neck_to_face_upper_cylinder_cluster_handle_name = self.neck_to_face_upper_cylinder_cluster_name + 'Handle'
        self.helper_class.set_cylinder_position(self.neck_to_face_cylinder_name,
                                                self.neck_to_face_lower_cylinder_cluster_name,
                                                self.neck_to_face_upper_cylinder_cluster_name,
                                                self.neck_sphere_name,
                                                self.head_sphere_name)

        # FACE TO LOWER MOUTH CYLINDER
        self.face_to_lower_mouth_cylinder_name = self.prefix_name + '_' + self.type + '_Head_Face_to_Lower_Mouth_Tem_' + str(
            self.val) + '_Geo'
        self.face_to_lower_mouth_lower_cylinder_cluster_name = self.prefix_name + '_' + self.type + '_Head_Face_to_Lower_Mouth_Lower_Tem_' + str(
            self.val) + '_Clu'
        self.face_to_lower_mouth_lower_cylinder_cluster_handle_name = self.face_to_lower_mouth_lower_cylinder_cluster_name + 'Handle'
        self.face_to_lower_mouth_upper_cylinder_cluster_name = self.prefix_name + '_' + self.type + '_Head_Face_to_Lower_Mouth_Upper_Tem_' + str(
            self.val) + '_Clu'
        self.face_to_lower_mouth_upper_cylinder_cluster_handle_name = self.face_to_lower_mouth_upper_cylinder_cluster_name + 'Handle'
        self.helper_class.set_cylinder_position(self.face_to_lower_mouth_cylinder_name,
                                                self.face_to_lower_mouth_lower_cylinder_cluster_name,
                                                self.face_to_lower_mouth_upper_cylinder_cluster_name,
                                                self.lower_mouth_sphere_name,
                                                self.head_sphere_name)

        # FACE TO UPPER MOUTH CYLINDER
        self.face_to_upper_mouth_cylinder_name = self.prefix_name + '_' + self.type + '_Head_Face_to_Upper_Mouth_Tem_' + str(
            self.val) + '_Geo'
        self.face_to_upper_mouth_lower_cylinder_cluster_name = self.prefix_name + '_' + self.type + '_Head_Face_to_Upper_Mouth_Lower_Tem_' + str(
            self.val) + '_Clu'
        self.face_to_upper_mouth_lower_cylinder_cluster_handle_name = self.face_to_upper_mouth_lower_cylinder_cluster_name + 'Handle'
        self.face_to_upper_mouth_upper_cylinder_cluster_name = self.prefix_name + '_' + self.type + '_Head_Face_to_Upper_Mouth_Upper_Tem_' + str(
            self.val) + '_Clu'
        self.face_to_upper_mouth_upper_cylinder_cluster_handle_name = self.face_to_upper_mouth_upper_cylinder_cluster_name + 'Handle'
        self.helper_class.set_cylinder_position(self.face_to_upper_mouth_cylinder_name,
                                                self.face_to_upper_mouth_lower_cylinder_cluster_name,
                                                self.face_to_upper_mouth_upper_cylinder_cluster_name,
                                                self.upper_mouth_sphere_name,
                                                self.head_sphere_name)

        # FACE TO HEAD TOP CYLINDER
        self.face_to_head_top_cylinder_name = self.prefix_name + '_' + self.type + '_Head_Face_to_Head_Top_Tem_' + str(
            self.val) + '_Geo'
        self.face_to_head_top_lower_cylinder_cluster_name = self.prefix_name + '_' + self.type + '_Head_Face_to_Head_Top_Lower_Tem_' + str(
            self.val) + '_Clu'
        self.face_to_head_top_lower_cylinder_cluster_handle_name = self.face_to_head_top_lower_cylinder_cluster_name + 'Handle'
        self.face_to_head_top_upper_cylinder_cluster_name = self.prefix_name + '_' + self.type + '_Head_Face_to_Head_Top_Upper_Tem_' + str(
            self.val) + '_Clu'
        self.face_to_head_top_upper_cylinder_cluster_handle_name = self.face_to_head_top_upper_cylinder_cluster_name + 'Handle'
        self.helper_class.set_cylinder_position(self.face_to_head_top_cylinder_name,
                                                self.face_to_head_top_lower_cylinder_cluster_name,
                                                self.face_to_head_top_upper_cylinder_cluster_name,
                                                self.head_sphere_name,
                                                self.head_top_sphere_name)

        # FACE TO LEFT EAR CYLINDER
        self.face_to_left_ear_cylinder_name = self.prefix_name + '_' + self.type + '_Head_Face_to_Left_Ear_Tem_' + str(
            self.val) + '_Geo'
        self.face_to_left_ear_lower_cylinder_cluster_name = self.prefix_name + '_' + self.type + '_Head_Face_to_Left_Ear_Lower_Tem_' + str(
            self.val) + '_Clu'
        self.face_to_left_ear_lower_cylinder_cluster_handle_name = self.face_to_left_ear_lower_cylinder_cluster_name + 'Handle'
        self.face_to_left_ear_upper_cylinder_cluster_name = self.prefix_name + '_' + self.type + '_Head_Face_to_Left_Ear_Upper_Tem_' + str(
            self.val) + '_Clu'
        self.face_to_left_ear_upper_cylinder_cluster_handle_name = self.face_to_left_ear_upper_cylinder_cluster_name + 'Handle'
        self.helper_class.set_cylinder_position(self.face_to_left_ear_cylinder_name,
                                                self.face_to_left_ear_lower_cylinder_cluster_name,
                                                self.face_to_left_ear_upper_cylinder_cluster_name,
                                                self.head_sphere_name,
                                                self.left_ear_sphere_name)

        # FACE TO RIGHT EAR CYLINDER
        self.face_to_right_ear_cylinder_name = self.prefix_name + '_' + self.type + '_Head_Face_to_Right_Ear_Tem_' + str(
            self.val) + '_Geo'
        self.face_to_right_ear_lower_cylinder_cluster_name = self.prefix_name + '_' + self.type + '_Head_Face_to_Right_Ear_Lower_Tem_' + str(
            self.val) + '_Clu'
        self.face_to_right_ear_lower_cylinder_cluster_handle_name = self.face_to_right_ear_lower_cylinder_cluster_name + 'Handle'
        self.face_to_right_ear_upper_cylinder_cluster_name = self.prefix_name + '_' + self.type + '_Head_Face_to_Right_Ear_Upper_Tem_' + str(
            self.val) + '_Clu'
        self.face_to_right_ear_upper_cylinder_cluster_handle_name = self.face_to_right_ear_upper_cylinder_cluster_name + 'Handle'
        self.helper_class.set_cylinder_position(self.face_to_right_ear_cylinder_name,
                                                self.face_to_right_ear_lower_cylinder_cluster_name,
                                                self.face_to_right_ear_upper_cylinder_cluster_name,
                                                self.head_sphere_name,
                                                self.right_ear_sphere_name)

        # put the cluster on one group
        cmds.select(self.base_to_neck_lower_cylinder_cluster_handle_name,
                    self.base_to_neck_upper_cylinder_cluster_handle_name,
                    self.neck_to_face_lower_cylinder_cluster_handle_name,
                    self.neck_to_face_upper_cylinder_cluster_handle_name,
                    self.face_to_lower_mouth_lower_cylinder_cluster_handle_name,
                    self.face_to_lower_mouth_upper_cylinder_cluster_handle_name,
                    self.face_to_upper_mouth_lower_cylinder_cluster_handle_name,
                    self.face_to_upper_mouth_upper_cylinder_cluster_handle_name,
                    self.face_to_head_top_lower_cylinder_cluster_handle_name,
                    self.face_to_head_top_upper_cylinder_cluster_handle_name,
                    self.face_to_left_ear_lower_cylinder_cluster_handle_name,
                    self.face_to_left_ear_upper_cylinder_cluster_handle_name,
                    self.face_to_right_ear_lower_cylinder_cluster_handle_name,
                    self.face_to_right_ear_upper_cylinder_cluster_handle_name,
                    self.base_sphere_clu_handle_name, self.neck_sphere_clu_handle_name,
                    self.head_sphere_clu_handle_name,
                    self.head_top_sphere_clu_handle_name, self.lower_mouth_sphere_clu_handle_name,
                    self.upper_mouth_sphere_clu_handle_name, self.left_ear_sphere_clu_handle_name,
                    self.right_ear_sphere_clu_handle_name)

        self.cluster_group_name = self.prefix_name + '_' + self.type + "_Head_Face_Tem_" + str(
            self.val) + "_Cluster_Grp"
        cmds.group(n=self.cluster_group_name)
        cmds.setAttr((self.cluster_group_name + '.v'), 0)
        cmds.setAttr((self.cluster_group_name + '.v'), lock=True)
        self.helper_class.transform_rotation_scale_visible(self.cluster_group_name)

        cmds.select(self.base_to_neck_cylinder_name, self.neck_to_face_cylinder_name,
                    self.face_to_lower_mouth_cylinder_name,
                    self.face_to_upper_mouth_cylinder_name, self.face_to_head_top_cylinder_name,
                    self.face_to_left_ear_cylinder_name, self.face_to_right_ear_cylinder_name)
        self.cylinder_group_name = self.prefix_name + '_' + self.type + "_Head_Face_Tem_" + str(
            self.val) + "_Cylinder_Grp"
        cmds.group(n=self.cylinder_group_name)
        self.helper_class.transform_rotation_scale_visible(self.cylinder_group_name)

    def eye(self, eye_position, eye_side, ctrl_color, eye_query):
        # left eye

        self.eye_query = eye_query
        self.default_value = eye_position
        self.eye_side = eye_side
        self.ctrl_color = ctrl_color

        a = 0
        add_value = 0
        while a < self.eye_query:
            self.new_value = [self.default_value[0], (self.default_value[1] + add_value), self.default_value[2]]
            # create a sphere
            self.eye_sphere_name = self.prefix_name + '_' + self.type + '_Head_' + self.eye_side + '_Eye_' + str(
                a + 1) + '_Tem_' + str(self.val) + '_Geo'
            self.eye_sphere_clu_name = self.prefix_name + '_' + self.type + '_Head_' + self.eye_side + '_Eye_' + str(
                a + 1) + '_Tem_' + str(self.val) + '_Clu'
            self.eye_sphere_clu_handle_name = self.eye_sphere_clu_name + 'Handle'
            self.helper_class.set_sphere_position(self.eye_sphere_name, self.new_value, self.eye_sphere_clu_name)

            # put the sphere and cluster in the group
            cmds.select(self.eye_sphere_name, self.sphere_group_name)
            cmds.parent()
            cmds.select(self.eye_sphere_clu_handle_name, self.cluster_group_name)
            cmds.parent()

            # LOWER MOUTH
            self.eye_ctrl_name = self.prefix_name + '_' + self.type + '_Head_' + self.eye_side + '_Eye_' + str(
                a + 1) + '_Tem_' + str(self.val) + '_Ctrl'
            self.eye_ctrl_size_ctrl = [0.5, 0.5, 0.5]
            self.eye_ctrl_roate = [0, 0, 0]
            self.eye_parent_const_list = [self.eye_sphere_clu_handle_name]
            self.helper_class.set_controller(self.eye_ctrl_name, self.new_value, self.eye_ctrl_size_ctrl,
                                             self.eye_ctrl_roate, self.eye_parent_const_list,
                                             self.eye_parent_const_list,
                                             color=self.ctrl_color)
            cmds.select(self.eye_ctrl_name, self.head_ctrl_name)
            cmds.parent()

            add_value += 2
            a += 1

    def controller_def(self):

        # CREATE CONTROLLER
        # BASE CONTROLLER
        self.base_ctrl_name = self.prefix_name + '_' + self.type + '_Head_Base_Tem_' + str(self.val) + '_Ctrl'
        self.base_ctrl_size_ctrl = self.base_ctrl_size
        self.base_ctrl_roate = self.base_ctrl_rotate
        self.base_parent_const_list = [self.base_sphere_clu_handle_name,
                                       self.base_to_neck_lower_cylinder_cluster_handle_name]
        self.helper_class.set_controller(self.base_ctrl_name, self.base_pos, self.base_ctrl_size_ctrl,
                                         self.base_ctrl_roate, self.base_parent_const_list, self.base_parent_const_list,
                                         color=self.base_ctrl_color,
                                         freez_trans=self.base_ctrl_freez_trans,
                                         freez_rotate=self.base_ctrl_freez_rotate,
                                         freez_scale=self.base_ctrl_freez_scale)

        # NECK CONTROLLER
        self.neck_ctrl_name = self.prefix_name + '_' + self.type + '_Head_Neck_Tem_' + str(self.val) + '_Ctrl'
        self.neck_ctrl_size_ctrl = self.neck_ctrl_size
        self.neck_ctrl_roate = self.neck_ctrl_rotate
        self.neck_parent_const_list = [self.neck_sphere_clu_handle_name,
                                       self.base_to_neck_upper_cylinder_cluster_handle_name,
                                       self.neck_to_face_lower_cylinder_cluster_handle_name]
        self.helper_class.set_controller(self.neck_ctrl_name, self.neck_pos, self.neck_ctrl_size_ctrl,
                                         self.neck_ctrl_roate, self.neck_parent_const_list, self.neck_parent_const_list,
                                         color=self.neck_ctrl_color,
                                         freez_trans=self.neck_ctrl_freez_trans,
                                         freez_rotate=self.neck_ctrl_freez_rotate,
                                         freez_scale=self.neck_ctrl_freez_scale)

        # HEAD CONTROLLER
        self.head_ctrl_name = self.prefix_name + '_' + self.type + '_Head_Head_Tem_' + str(self.val) + '_Ctrl'
        self.head_ctrl_size_ctrl = self.head_ctrl_size
        self.head_ctrl_roate = self.head_ctrl_rotate
        self.head_parent_const_list = [self.face_to_right_ear_lower_cylinder_cluster_handle_name,
                                       self.face_to_head_top_lower_cylinder_cluster_handle_name,
                                       self.face_to_left_ear_lower_cylinder_cluster_handle_name,
                                       self.head_sphere_clu_handle_name,
                                       self.neck_to_face_upper_cylinder_cluster_handle_name,
                                       self.face_to_lower_mouth_upper_cylinder_cluster_handle_name,
                                       self.face_to_upper_mouth_upper_cylinder_cluster_handle_name]
        self.helper_class.set_controller(self.head_ctrl_name, self.head_pos, self.head_ctrl_size_ctrl,
                                         self.head_ctrl_roate, self.head_parent_const_list, self.head_parent_const_list,
                                         color=self.head_ctrl_color,
                                         freez_trans=self.head_ctrl_freez_trans,
                                         freez_rotate=self.head_ctrl_freez_rotate,
                                         freez_scale=self.head_ctrl_freez_scale)

        # HEAD TOP
        self.head_top_ctrl_name = self.prefix_name + '_' + self.type + '_Head_Head_Top_Tem_' + str(self.val) + '_Ctrl'
        self.head_top_ctrl_size_ctrl = self.head_top_ctrl_size
        self.head_top_ctrl_roate = self.head_top_ctrl_rotate
        self.head_top_parent_const_list = [self.face_to_head_top_upper_cylinder_cluster_handle_name,
                                           self.head_top_sphere_clu_handle_name]
        self.helper_class.set_controller(self.head_top_ctrl_name, self.head_top_pos, self.head_top_ctrl_size_ctrl,
                                         self.head_top_ctrl_roate, self.head_top_parent_const_list,
                                         self.head_top_parent_const_list,
                                         color=self.head_top_ctrl_color,
                                         freez_trans=self.head_top_ctrl_freez_trans,
                                         freez_rotate=self.head_top_ctrl_freez_rotate,
                                         freez_scale=self.head_top_ctrl_freez_scale)

        # LOWER MOUTH
        self.lower_mouth_ctrl_name = self.prefix_name + '_' + self.type + '_Head_Lower_Mouth_Tem_' + str(
            self.val) + '_Ctrl'
        self.lower_mouth_ctrl_size_ctrl = self.lower_mouth_ctrl_size
        self.lower_mouth_ctrl_roate = self.lower_mouth_ctrl_rotate
        self.lower_mouth_parent_const_list = [self.face_to_lower_mouth_lower_cylinder_cluster_handle_name,
                                              self.lower_mouth_sphere_clu_handle_name]
        self.helper_class.set_controller(self.lower_mouth_ctrl_name, self.lower_mouth_pos,
                                         self.lower_mouth_ctrl_size_ctrl,
                                         self.lower_mouth_ctrl_roate, self.lower_mouth_parent_const_list,
                                         self.lower_mouth_parent_const_list,
                                         color=self.lower_mouth_ctrl_color,
                                         freez_trans=self.lower_mouth_ctrl_freez_trans,
                                         freez_rotate=self.lower_mouth_ctrl_freez_rotate,
                                         freez_scale=self.lower_mouth_ctrl_freez_scale)

        # UPPER MOUTH
        self.upper_mouth_ctrl_name = self.prefix_name + '_' + self.type + '_Head_Upper_Mouth_Tem_' + str(
            self.val) + '_Ctrl'
        self.upper_mouth_ctrl_size_ctrl = self.upper_mouth_ctrl_size
        self.upper_mouth_ctrl_roate = self.upper_mouth_ctrl_rotate
        self.upper_mouth_parent_const_list = [self.face_to_upper_mouth_lower_cylinder_cluster_handle_name,
                                              self.upper_mouth_sphere_clu_handle_name]
        self.helper_class.set_controller(self.upper_mouth_ctrl_name, self.upper_mouth_pos,
                                         self.upper_mouth_ctrl_size_ctrl,
                                         self.upper_mouth_ctrl_roate, self.upper_mouth_parent_const_list,
                                         self.upper_mouth_parent_const_list,
                                         color=self.upper_mouth_ctrl_color,
                                         freez_trans=self.upper_mouth_ctrl_freez_trans,
                                         freez_rotate=self.upper_mouth_ctrl_freez_rotate,
                                         freez_scale=self.upper_mouth_ctrl_freez_scale)

        # LEFT EAR
        self.left_ear_ctrl_name = self.prefix_name + '_' + self.type + '_Head_Left_Ear_Tem_' + str(self.val) + '_Ctrl'
        self.left_ear_ctrl_size_ctrl = self.left_ear_ctrl_size
        self.left_ear_ctrl_roate = self.left_ear_ctrl_rotate
        self.left_ear_parent_const_list = [self.face_to_left_ear_upper_cylinder_cluster_handle_name,
                                           self.left_ear_sphere_clu_handle_name]
        self.helper_class.set_controller(self.left_ear_ctrl_name, self.left_ear_pos, self.left_ear_ctrl_size_ctrl,
                                         self.left_ear_ctrl_roate, self.left_ear_parent_const_list,
                                         self.left_ear_parent_const_list,
                                         color=self.left_ear_ctrl_color,
                                         freez_trans=self.left_ear_ctrl_freez_trans,
                                         freez_rotate=self.left_ear_ctrl_freez_rotate,
                                         freez_scale=self.left_ear_ctrl_freez_scale)

        # RIGHT EAR
        self.right_ear_ctrl_name = self.prefix_name + '_' + self.type + '_Head_Right_Ear_Tem_' + str(self.val) + '_Ctrl'
        self.right_ear_ctrl_size_ctrl = self.right_ear_ctrl_size
        self.right_ear_ctrl_roate = self.right_ear_ctrl_rotate
        self.right_ear_parent_const_list = [self.face_to_right_ear_upper_cylinder_cluster_handle_name,
                                            self.right_ear_sphere_clu_handle_name]
        self.helper_class.set_controller(self.right_ear_ctrl_name, self.right_ear_pos, self.right_ear_ctrl_size_ctrl,
                                         self.right_ear_ctrl_roate, self.right_ear_parent_const_list,
                                         self.right_ear_parent_const_list,
                                         color=self.right_ear_ctrl_color,
                                         freez_trans=self.right_ear_ctrl_freez_trans,
                                         freez_rotate=self.right_ear_ctrl_freez_rotate,
                                         freez_scale=self.right_ear_ctrl_freez_scale)

        cmds.select(self.base_ctrl_name,
                    self.neck_ctrl_name,
                    self.head_ctrl_name,
                    self.lower_mouth_ctrl_name,
                    self.upper_mouth_ctrl_name,
                    self.head_top_ctrl_name,
                    self.left_ear_ctrl_name,
                    self.right_ear_ctrl_name)
        self.ctrl_group_name = self.prefix_name + '_' + self.type + "_Head_Face_Tem_" + str(self.val) + "_Ctrl_Grp"
        cmds.group(n=self.ctrl_group_name)
        self.helper_class.transform_rotation_scale_visible(self.ctrl_group_name)

        # make a parent
        cmds.select(self.lower_mouth_ctrl_name,
                    self.upper_mouth_ctrl_name,
                    self.head_top_ctrl_name,
                    self.left_ear_ctrl_name,
                    self.right_ear_ctrl_name,
                    self.head_ctrl_name)
        cmds.parent()
        cmds.select(self.head_ctrl_name,
                    self.neck_ctrl_name)
        cmds.parent()
        cmds.select(self.neck_ctrl_name,
                    self.base_ctrl_name)
        cmds.parent()

        # put everything in the one grpup
        cmds.select(self.sphere_group_name,
                    self.cluster_group_name,
                    self.cylinder_group_name,
                    self.ctrl_group_name)
        self.main_group_name = self.prefix_name + '_' + self.type + '_Head_Tem_' + str(self.val) + '_Main_Grp'
        cmds.group(n=self.main_group_name)
        self.helper_class.transform_rotation_scale_visible(self.main_group_name, v=False)

        # create mirror ear
        self.helper_class.mirror_grp(self.left_ear_ctrl_name,
                                     self.right_ear_ctrl_name)

    def eye_side(self):
        pass

    def set_left_eye(self):
        pass

    def update_gui(self, widget):
        self.update_widget = widget
        self.default_box_layout(self.update_widget)
        # get the radio button
        self.get_update_radio_button()
        self.get_detail_update_def()

        # lock the attr
        self.lock_attr()

    def default_box_layout(self, widget):
        self.head_verticalLayout = QtGui.QVBoxLayout(widget)
        self.head_verticalLayout.setObjectName("head_verticalLayout")
        self.head_splitter = QtGui.QSplitter(widget)
        self.head_splitter.setOrientation(QtCore.Qt.Vertical)
        self.head_splitter.setObjectName("head_splitter")

    def get_update_radio_button(self):
        self.head_name_scroll_area = QtGui.QScrollArea(self.head_splitter)
        self.head_name_scroll_area.setWidgetResizable(True)
        self.head_name_scroll_area.setObjectName("head_name_scroll_area")
        self.head_name_scrollArea_widget_contents = QtGui.QWidget()
        self.head_name_scrollArea_widget_contents.setGeometry(QtCore.QRect(0, 0, 642, 64))
        self.head_name_scrollArea_widget_contents.setObjectName("head_name_scrollArea_widget_contents")
        self.gridLayout_15 = QtGui.QGridLayout(self.head_name_scrollArea_widget_contents)
        self.gridLayout_15.setObjectName("gridLayout_15")

        self.no_head = self.helper_class.get_head()

        a = 0
        value = 0
        grid_value = 0
        self.radio_button = {}
        while a < len(self.no_head):
            self.radio_button[a] = QtGui.QRadioButton(self.head_name_scrollArea_widget_contents)
            self.radio_button[a].setObjectName(self.no_head[a])
            self.radio_button[a].setText(self.no_head[a])
            self.radio_button[a].toggled.connect(partial(self.radio_button_change, a))
            self.gridLayout_15.addWidget(self.radio_button[a], grid_value, value, 1, 1)
            value += 1
            if value == 3:
                value = 0
                grid_value += 1

            a += 1

        self.head_name_scroll_area.setWidget(self.head_name_scrollArea_widget_contents)

    def get_detail_update_def(self):
        self.head_detail_scroll_area = QtGui.QScrollArea(self.head_splitter)
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

        # LEFT EYE
        # LEFT EYE LABEL
        self.left_eye_label = QtGui.QLabel(self.head_detail_2_scrollArea_widget_contents)
        self.left_eye_label.setObjectName("left_eye_label")
        self.left_eye_label.setText('Left Eye : ')
        self.gridLayout_23.addWidget(self.left_eye_label, 1, 0, 1, 1)
        # LEFT EYE LINE EDIT
        self.left_eye_line_edit = QtGui.QLineEdit(self.head_detail_2_scrollArea_widget_contents)
        self.left_eye_line_edit.setObjectName("left_eye_line_edit")
        self.gridLayout_23.addWidget(self.left_eye_line_edit, 1, 1, 1, 1)

        # RIGHT EYE
        # RIGH EYE LABEL
        self.right_eye_label = QtGui.QLabel(self.head_detail_2_scrollArea_widget_contents)
        self.right_eye_label.setObjectName("right_eye_label")
        self.right_eye_label.setText('Right Eye : ')
        self.gridLayout_23.addWidget(self.right_eye_label, 2, 0, 1, 1)
        # RIGHT EYE LINE EDIT
        self.right_eye_line_edit = QtGui.QLineEdit(self.head_detail_2_scrollArea_widget_contents)
        self.right_eye_line_edit.setObjectName("right_eye_line_dit")
        self.gridLayout_23.addWidget(self.right_eye_line_edit, 2, 1, 1, 1)

        # NAME
        # NAME LABEL
        self.name_label = QtGui.QLabel(self.head_detail_2_scrollArea_widget_contents)
        self.name_label.setObjectName("name_label")
        self.name_label.setText('Name : ')
        self.gridLayout_23.addWidget(self.name_label, 3, 0, 1, 1)
        # NAME BUTTON
        self.name_button = QtGui.QPushButton(self.head_detail_2_scrollArea_widget_contents)
        self.name_button.setObjectName("name_button")
        self.name_button.clicked.connect(self.rename)
        self.gridLayout_23.addWidget(self.name_button, 3, 1, 1, 1)

        # PARENT
        # PARENT LABEL
        self.parent_label = QtGui.QLabel(self.head_detail_2_scrollArea_widget_contents)
        self.parent_label.setObjectName("parent_label")
        self.parent_label.setText('Parent : ')
        self.gridLayout_23.addWidget(self.parent_label, 4, 0, 1, 1)
        # PARENT BUTTON
        self.parent_button = QtGui.QPushButton(self.head_detail_2_scrollArea_widget_contents)
        self.parent_button.setObjectName("parent_button")
        self.parent_button.clicked.connect(self.parent)
        self.gridLayout_23.addWidget(self.parent_button, 4, 1, 1, 1)

        spacerItem10 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_23.addItem(spacerItem10, 5, 0, 1, 1)

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
        self.head_update_button = QtGui.QPushButton(self.head_update_scrollArea_widget_contents)
        self.head_update_button.setObjectName("head_update_button")
        self.head_update_button.setText('Update (Head name)')
        self.head_update_button.clicked.connect(self.head_update_button_def)
        self.gridLayout_17.addWidget(self.head_update_button, 1, 0, 1, 1)

        # DELETE BUTTON
        self.head_delete_button = QtGui.QPushButton(self.head_update_scrollArea_widget_contents)
        self.head_delete_button.setObjectName("head_delete_button")
        self.head_delete_button.setText('Delete(Head Name)')
        self.head_delete_button.clicked.connect(self.head_delete_button_def)
        self.gridLayout_17.addWidget(self.head_delete_button, 1, 1, 1, 1)

        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_17.addItem(spacerItem9, 0, 0, 1, 1)

        self.head_update_scroll_area.setWidget(self.head_update_scrollArea_widget_contents)
        self.gridLayout_18.addWidget(self.head_update_scroll_area, 1, 0, 1, 1)

        self.gridLayout_18.addWidget(self.head_detail_2_scroll_area, 0, 0, 1, 1)
        self.head_detail_scroll_area.setWidget(self.head_detail_scrollArea_widget_contents)
        self.head_verticalLayout.addWidget(self.head_splitter)

        self.head_detail_scroll_area.setWidget(self.head_detail_scrollArea_widget_contents)
        self.head_verticalLayout.addWidget(self.head_splitter)

    def delete_all(self):
        # get the children
        head_name = 'Head_Grp'
        if cmds.objExists(head_name):
            children = cmds.listRelatives(head_name)
            for each in children:
                cmds.select(each)
                cmds.delete()

    def radio_button_change(self, b, val):
        if val == True:
            # unlock the val
            self.unlock_attr()

            # get the value
            self.get_input_data(self.no_head[b])

            # update the ui
            self.character_type_combo_box.setCurrentIndex(self.input_character_option_menu)
            self.left_eye_line_edit.setText(str(self.input_left_eye))
            self.right_eye_line_edit.setText(str(self.input_right_eye))
            self.name_button.setText(self.prefix_name)
            self.parent_button.setText(self.input_parent)
            self.head_update_button.setText('Update (%s)' % self.head_name)
            self.head_delete_button.setText('Delete(%s)' % self.head_name)

    def get_input_data(self, head_name):
        self.head_name = head_name
        self.name = self.head_name.split('_')
        self.input_main_grp_name = '*_' + self.name[0] + '_Head_Tem_' + self.name[-1] + '_Main_Grp'
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
        self.type = self.name[0]
        self.val = self.name[-1]
        self.prefix_name = self.input_split_main_grp
        self.input_character_option_menu = value
        self.input_left_eye = self.left_eye_query()
        self.input_right_eye = self.right_eye_query()
        self.input_parent = self.parent_query()

        # get the grpup name
        self.get_grp_name()

    def get_data(self):
        # split the name
        self.name = self.head_name.split('_')
        # Template_Human_Head_Tem_1_Main_Grp
        main_grp_name = '*_' + self.name[0] + '_Head_Tem_' + self.name[-1] + '_Main_Grp'
        cmds.select(main_grp_name)
        sel_main_grp_name = cmds.ls(sl=True)[0]
        split_main_grp = sel_main_grp_name.split('_' + self.name[0])[0]
        # get the characert option menu
        if self.name[0] == 'Human':
            value = 0
        elif self.name[0] == 'Animal':
            value = 1
        elif self.name[0] == 'Bird':
            value = 2

        return self.name[0], self.name[-1], split_main_grp, value

    def left_eye_query(self):
        # Template_Human_Head_Left_Eye_1_Tem_3_Ctrl
        # New_Human_Human_Head_Left_Eye_1_Tem_1_Ctrl
        # New_Human_Head_Left_Eye_*_Tem_1_Ctrl
        self.left_ctrl_common_name = self.prefix_name + '_' + self.type + '_Head_Left_Eye_*_Tem_' + self.val
        self.left_ctrl_name = self.left_ctrl_common_name + '_Ctrl'

        cmds.select(self.left_ctrl_name)
        sel_ctrl = cmds.ls(sl=True)
        return len(sel_ctrl)

    def right_eye_query(self):
        # Template_Human_Head_Left_Eye_1_Tem_3_Ctrl
        self.right_ctrl_common_name = self.prefix_name + '_' + self.type + '_Head_Right_Eye_*_Tem_' + self.val
        self.right_ctrl_name = self.right_ctrl_common_name + '_Ctrl'

        cmds.select(self.right_ctrl_name)
        sel_ctrl = cmds.ls(sl=True)
        return len(sel_ctrl)

    def parent_query(self):
        # Template_Human_Head_Base_Tem_1_Ctrl
        base_ctrl_name = self.prefix_name + '_' + self.type + '_Head_Base_Tem_' + self.val + '_Ctrl'
        value = cmds.listRelatives(base_ctrl_name, type='parentConstraint')
        if value == None:
            parent = 'None'
        else:
            parent = cmds.listConnections((value[0] + '.target[0].targetTranslate'), type='transform')[0]
        return parent

    def head_update_get_data(self):
        self.get_character_type = self.character_type_combo_box.currentText()
        self.get_left_eye = int(self.left_eye_line_edit.text())
        self.get_right_eye = int(self.right_eye_line_edit.text())
        self.get_name = self.name_button.text()
        self.get_parent = self.parent_button.text()

    def head_update_button_def(self):
        self.head_update_get_data()

        if self.type == self.get_character_type:
            # get the current pos
            base_val = cmds.xform(self.base_ctrl_name, q=1, rotation=1)
            neck_val = cmds.xform(self.neck_ctrl_name, q=1, rotation=1)
            head_val = cmds.xform(self.head_ctrl_name, q=1, rotation=1)
            list = [self.base_ctrl_name, self.neck_ctrl_name, self.head_ctrl_name]
            list_val = [base_val, neck_val, head_val]
            for each in list:
                if self.type == 'Animal':
                    if each == self.neck_ctrl_name:
                        self.helper_class.set_val(ctrl_name=each,
                                                  r=True,
                                                  r_val=[70, 0, 0])
                    elif each == self.head_ctrl_name:
                        self.helper_class.set_val(ctrl_name=each,
                                                  r=True,
                                                  r_val=[-25, 0, 0])
                else:
                    self.helper_class.set_val(ctrl_name=each,
                                              r=True,
                                              r_val=[0, 0, 0])

            # get each pos data

            # set the left eye
            def eye_create(ctrl_name,
                           common_name):
                # eye_position,eye_side,ctrl_color,eye_query
                cmds.select(ctrl_name)
                sel_ctrl = cmds.ls(sl=True)
                # get the position
                ctrl_pos = cmds.xform(sel_ctrl[0], q=1, ws=1, rp=1)
                # delete all the ctrl,cluster,sphere
                geo_name = common_name + '_Geo'
                clu_handle_name = common_name + '_CluHandle'
                cmds.select(geo_name, clu_handle_name, ctrl_name)
                cmds.delete()

                return ctrl_pos

            if self.input_left_eye != self.get_left_eye:
                # get the
                # set the rotation zero

                self.ctrl_pos = eye_create(self.left_ctrl_name,
                                           self.left_ctrl_common_name)

                # now create a new controller with new position and parent to the grp
                self.eye(self.ctrl_pos, 'Left', 'Red', self.get_left_eye)

            if self.input_right_eye != self.get_right_eye:
                # get the
                self.ctrl_pos = eye_create(self.right_ctrl_name,
                                           self.right_ctrl_common_name)

                # now create a new controller with new position and parent to the grp
                self.eye(self.ctrl_pos, 'Right', 'Blue', self.get_right_eye)

            a = 0
            for each in list:
                self.helper_class.set_val(ctrl_name=each,
                                          r=True,
                                          r_val=list_val[a])
                a += 1
        else:
            # delete the old one
            # get the base and neck pos
            # Template_Animal_Head_Neck_Tem_2_Ctrl
            default_base_ctrl_name = self.prefix_name + '_' + self.type + "_Head_Base_Tem_" + str(self.val) + "_Ctrl"
            base_ctrl_trans_getAttr = cmds.getAttr(default_base_ctrl_name + '.t')[0]
            base_ctrl_rot_getAttr = cmds.getAttr(default_base_ctrl_name + '.r')[0]
            default_neck_ctrl_name = self.prefix_name + '_' + self.type + "_Head_Neck_Tem_" + str(self.val) + "_Ctrl"
            neck_ctrl_trans_getAttr = cmds.getAttr(default_neck_ctrl_name + '.t')[0]
            neck_ctrl_rot_getAttr = cmds.getAttr(default_neck_ctrl_name + '.r')[0]

            self.old_main_grp = self.prefix_name + '_' + self.type + "_Head_Tem_" + str(self.val) + "_Main_Grp"
            cmds.select(self.old_main_grp)
            cmds.delete()
            self.left_eye_query = self.get_left_eye
            self.right_eye_query = self.get_right_eye
            self.combo_box_value = self.get_character_type

            self.prefix_name = 'Template'

            if self.get_character_type == 'Human':
                self.human_head_def()
                base_ctrl_name = self.prefix_name + '_' + self.type + "_Head_Base_Tem_" + str(self.val) + "_Ctrl"
                self.helper_class.set_val(ctrl_name=base_ctrl_name,
                                          t=True, t_val=base_ctrl_trans_getAttr)
                neck_ctrl_name = self.prefix_name + '_' + self.type + "_Head_Neck_Tem_" + str(self.val) + "_Ctrl"
                self.helper_class.set_val(ctrl_name=neck_ctrl_name,
                                          t=True, t_val=neck_ctrl_trans_getAttr)
            elif self.get_character_type == 'Animal':
                self.animal_head_def()
                base_ctrl_name = self.prefix_name + '_' + self.type + "_Head_Base_Tem_" + str(self.val) + "_Ctrl"
                self.helper_class.set_val(ctrl_name=base_ctrl_name,
                                          t=True, t_val=base_ctrl_trans_getAttr)
                neck_ctrl_name = self.prefix_name + '_' + self.type + "_Head_Neck_Tem_" + str(self.val) + "_Ctrl"
                self.helper_class.set_val(ctrl_name=neck_ctrl_name,
                                          t=True, t_val=neck_ctrl_trans_getAttr)
            elif self.get_character_type == 'Bird':
                self.animal_head_def()
                base_ctrl_name = self.prefix_name + '_' + self.type + "_Head_Base_Tem_" + str(self.val) + "_Ctrl"
                self.helper_class.set_val(ctrl_name=base_ctrl_name,
                                          t=True, t_val=base_ctrl_trans_getAttr)
                neck_ctrl_name = self.prefix_name + '_' + self.type + "_Head_Neck_Tem_" + str(self.val) + "_Ctrl"
                self.helper_class.set_val(ctrl_name=neck_ctrl_name,
                                          t=True, t_val=neck_ctrl_trans_getAttr)

            if self.get_parent != 'None':
                cmds.parentConstraint(self.get_parent, self.base_ctrl_name, mo=False)

    def head_delete_button_def(self):
        # Template_Human_Head_Tem_1_Main_Grp
        # get the name of the object in the button
        self.name_button_query = self.name_button.text()
        main_new_grp_name = self.name_button_query + '_' + self.type + '_Head_Tem_' + self.val + '_Main_Grp'
        if cmds.objExists(main_new_grp_name):
            cmds.select(main_new_grp_name)
            cmds.delete()
        else:
            print(main_new_grp_name, ' is not there in the file please check the file if exist')

    def lock_attr(self):
        self.character_type_label.setDisabled(True)
        self.character_type_combo_box.setDisabled(True)
        self.left_eye_label.setDisabled(True)
        self.left_eye_line_edit.setDisabled(True)
        self.right_eye_label.setDisabled(True)
        self.right_eye_line_edit.setDisabled(True)
        self.name_label.setDisabled(True)
        self.name_button.setDisabled(True)
        self.parent_label.setDisabled(True)
        self.parent_button.setDisabled(True)
        self.head_update_button.setDisabled(True)
        self.head_delete_button.setDisabled(True)

    def unlock_attr(self):
        self.character_type_label.setDisabled(False)
        self.character_type_combo_box.setDisabled(False)
        self.left_eye_label.setDisabled(False)
        self.left_eye_line_edit.setDisabled(False)
        self.right_eye_label.setDisabled(False)
        self.right_eye_line_edit.setDisabled(False)
        self.name_label.setDisabled(False)
        self.name_button.setDisabled(False)
        self.parent_label.setDisabled(False)
        self.parent_button.setDisabled(False)
        self.head_update_button.setDisabled(False)
        self.head_delete_button.setDisabled(False)

    def update_ui(self, widget):
        self.default_box_layout(widget)
        self.get_update_radio_button()
        # self.head_verticalLayout.deleteLater()

    def rename(self):
        rename.main('Head', self.head_name, self.name_button, mirror_val=False, mirror_side='')

    def parent(self):
        parent.main('Head', self.head_name, self.parent_button)

    def new_clear(self):
        self.helper_class.clearLayout(self.head_grid_layout)

    def head_create(self):
        # get the no of the human main grp
        self.head_grp_list = ['Human_Head_Grp', 'Animal_Head_Grp']
        for each_grp in self.head_grp_list:
            # list of the all children
            if cmds.objExists(each_grp):
                children_list = cmds.listRelatives(each_grp, children=True)
                if children_list != None:
                    for each_child in children_list:
                        # get all the controller data
                        self.head_data(each_child)

                        # final the head
                        self.final_head()

    def head_data(self, main_grp_name):
        split_name = main_grp_name.split('_')
        # Template_Animal_Head_Tem_1_Main_Grp
        main_grp = main_grp_name.split('_Head_Tem_')[1]
        self.prefix_name = split_name[0]
        self.type = split_name[1]
        self.val = main_grp.split('_Main_Grp')[0]

        # get each ctrl position data
        self.get_each_pos_data()

    def final_head(self):
        # create a joint on each controller pos

        # create a neck joint
        # create a neck controller
        # create a neck and head bind jnt

        self.final_neck_bind_jnt = self.final_neck_common + '_Neck_Bind_Jnt'
        cmds.select(cl=True)
        cmds.joint(n=self.final_neck_bind_jnt, p=(self.final_ctrl_list[self.final_neck_common]['t_pos'][0],
                                                  self.final_ctrl_list[self.final_neck_common]['t_pos'][1],
                                                  self.final_ctrl_list[self.final_neck_common]['t_pos'][2]))

        self.final_head_head_bind_jnt = self.final_head_head_common + '_Neck_Bind_Jnt'
        cmds.select(cl=True)
        cmds.joint(n=self.final_head_head_bind_jnt, p=(self.final_ctrl_list[self.final_head_head_common]['t_pos'][0],
                                                       self.final_ctrl_list[self.final_head_head_common]['t_pos'][1],
                                                       self.final_ctrl_list[self.final_head_head_common]['t_pos'][2]))

        self.roll_bone(type='Neck',
                       upper_object=self.final_neck_ctrl,
                       lower_object=self.final_head_head_ctrl,
                       no_of_bone=3)

        # create a joint
        a = 0
        bind_jnt_list = []
        for each_sphere in self.neck_sphere_list:
            jnt_name = each_sphere + '_Neck_Bind_Jnt'
            bind_jnt_list.append(jnt_name)
            cmds.select(cl=True)
            cmds.joint(n=jnt_name, p=(self.neck_sphere_list[each_sphere][0],
                                      self.neck_sphere_list[each_sphere][1],
                                      self.neck_sphere_list[each_sphere][2]))
            a += 1

        neck_bind_0_jnt = self.prefix_name + "_" + self.type + '_Neck_Neck_0_Tem_' + str(self.val) + '_Neck_Bind_Jnt'
        neck_bind_1_jnt = self.prefix_name + "_" + self.type + '_Neck_Neck_1_Tem_' + str(self.val) + '_Neck_Bind_Jnt'
        neck_bind_2_jnt = self.prefix_name + "_" + self.type + '_Neck_Neck_2_Tem_' + str(self.val) + '_Neck_Bind_Jnt'
        cmds.select(neck_bind_0_jnt, self.final_neck_bind_jnt)
        cmds.parent()
        cmds.select(neck_bind_1_jnt, neck_bind_0_jnt)
        cmds.parent()
        cmds.select(neck_bind_2_jnt, neck_bind_1_jnt)
        cmds.parent()
        cmds.select(self.final_head_head_bind_jnt, neck_bind_2_jnt)
        cmds.parent()

        # make a freez transform the joint
        cmds.select(self.final_neck_bind_jnt)
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1, jointOrient=True)
        cmds.joint(e=True, oj='xzy', secondaryAxisOrient='xup', ch=True, zso=True)

        # Create ik spine jnt
        self.ik_spine = self.final_neck_common + "_HDL"
        self.ik_curve_name = self.final_neck_common + "_CRV"
        self.ik_curve_shape_name = self.ik_curve_name + "Shape"
        self.ik_eff_name = self.final_neck_common + "_Eff"
        self.handle = cmds.ikHandle(n=self.ik_spine, sj=self.final_neck_bind_jnt, ee=self.final_head_head_bind_jnt,
                                    sol='ikSplineSolver')
        cmds.setAttr((self.ik_spine + ".v"), 0)
        cmds.rename(self.handle[1], self.ik_eff_name)
        cmds.rename(self.handle[2], self.ik_curve_name)
        # setAttr "Template_Human_Head_Neck_Tem_1_CRV.inheritsTransform" 0;
        cmds.setAttr((self.ik_curve_name + ".inheritsTransform"), 0)

        # Create  a Bind Jnt
        self.neck_bind_jnt_name = self.final_neck_common + "_Bind_Jnt"
        self.neck_bind_jnt_grp_name = self.neck_bind_jnt_name + "_Grp"
        cmds.select(cl=True)
        cmds.joint(n=self.neck_bind_jnt_name, p=(self.final_ctrl_list[self.final_neck_common]['t_pos'][0],
                                                 self.final_ctrl_list[self.final_neck_common]['t_pos'][1],
                                                 self.final_ctrl_list[self.final_neck_common]['t_pos'][2]))
        cmds.select(self.neck_bind_jnt_name)
        cmds.group(n=self.neck_bind_jnt_grp_name)

        self.head_bind_jnt_name = self.final_head_head_common + "_Bind_Jnt"
        self.head_bind_jnt_grp_name = self.head_bind_jnt_name + "_Grp"
        cmds.select(cl=True)
        cmds.joint(n=self.head_bind_jnt_name, p=(self.final_ctrl_list[self.final_head_head_common]['t_pos'][0],
                                                 self.final_ctrl_list[self.final_head_head_common]['t_pos'][1],
                                                 self.final_ctrl_list[self.final_head_head_common]['t_pos'][2]))
        cmds.select(self.head_bind_jnt_name)
        cmds.group(n=self.head_bind_jnt_grp_name)

        cmds.select(self.neck_bind_jnt_name,
                    self.head_bind_jnt_name,
                    self.ik_curve_name)
        cmds.SmoothBindSkin()

        # Create advanced Twsit control
        cmds.setAttr((self.ik_spine + ".dTwistControlEnable"), 1)
        cmds.setAttr((self.ik_spine + ".dWorldUpType"), 4)
        cmds.setAttr((self.ik_spine + ".dWorldUpVectorX"), 0)
        cmds.setAttr((self.ik_spine + ".dWorldUpVectorY"), -1)
        cmds.setAttr((self.ik_spine + ".dWorldUpVectorZ"), 1)
        cmds.setAttr((self.ik_spine + ".dWorldUpVectorEndX"), 0)
        cmds.setAttr((self.ik_spine + ".dWorldUpVectorEndY"), 1)
        cmds.setAttr((self.ik_spine + ".dWorldUpVectorEndZ"), -1)
        cmds.setAttr((self.ik_spine + ".dWorldUpAxis"), 1)

        for each_ctrl in self.final_ctrl_list:
            split_ctrl = each_ctrl.split('_Ctrl')[0]
            jnt_name = split_ctrl + '_Result_Jnt'
            cmds.select(cl=True)
            cmds.joint(n=jnt_name, p=(self.final_ctrl_list[each_ctrl]['t_pos'][0],
                                      self.final_ctrl_list[each_ctrl]['t_pos'][1],
                                      self.final_ctrl_list[each_ctrl]['t_pos'][2]))
            cmds.select(cl=True)

        cmds.select(self.final_head_head_jnt, self.final_neck_jnt)
        cmds.parent()

        # make a freez transform the joint
        cmds.select(self.final_neck_jnt)
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1, jointOrient=True)
        cmds.joint(e=True, oj='xzy', secondaryAxisOrient='xup', ch=True, zso=True)

        # self.prefix_name + "_" + self.type  + '_Neck_Neck_0_Tem_' + str(self.val) + '_Neck_Bind_Jnt'

        # CREATE A A NECK CONTROLLER
        neck_ctrl_name = self.prefix_name + '_' + self.type + '_Head_Neck_' + str(self.val) + '_Ctrl'
        neck_ctrl_shape_name = neck_ctrl_name + 'Shape'
        self.controller_class.circle_ctrl()
        sel_obj = cmds.ls(sl=True)
        cmds.rename(sel_obj[0], neck_ctrl_name)
        cmds.select(neck_ctrl_shape_name, self.final_neck_jnt)
        cmds.parent(r=True, s=True)
        cmds.select(neck_ctrl_name)
        cmds.delete()
        cmds.parentConstraint(self.final_neck_jnt, self.neck_bind_jnt_grp_name, mo=True)

        # create a head controller
        head_ctrl_name = self.prefix_name + '_' + self.type + '_Head_Head_' + str(self.val) + '_Ctrl'
        head_ctrl_shape_name = head_ctrl_name + 'Shape'  #
        head_ctrl_grp_name = head_ctrl_name + '_Grp'
        self.controller_class.circle_ctrl()
        sel_obj = cmds.ls(sl=True)
        cmds.rename(sel_obj[0], head_ctrl_name)
        cmds.select(head_ctrl_name)
        cmds.move(self.final_ctrl_list[self.final_head_head_common]['t_pos'][0],
                  self.final_ctrl_list[self.final_head_head_common]['t_pos'][1],
                  self.final_ctrl_list[self.final_head_head_common]['t_pos'][2])
        cmds.DeleteHistory()
        cmds.FreezeTransformations()
        cmds.parentConstraint(head_ctrl_name, self.head_bind_jnt_grp_name, mo=True)
        cmds.select(head_ctrl_name)
        cmds.group(n=head_ctrl_grp_name)
        cmds.parentConstraint(self.final_head_head_jnt, head_ctrl_grp_name, mo=True)

        # Now Stretch the neck
        curve_info_name = self.prefix_name + '_' + self.type + "_Head_Neck_Tem_" + str(self.val) + "_Info"
        cmds.createNode('curveInfo', n=curve_info_name)
        cmds.connectAttr((self.ik_curve_shape_name + ".worldSpace[0]"), (curve_info_name + ".inputCurve"), f=True)

        multipy_info_name = self.prefix_name + '_' + self.type + "_Head_Neck_Tem_" + str(self.val) + "_Div"
        cmds.createNode('multiplyDivide', n=multipy_info_name)
        cmds.setAttr((multipy_info_name + ".operation"), 2)

        root_grp_name = "Root_Grp"
        if cmds.objExists(root_grp_name):
            pass
        else:
            cmds.createNode('transform', n=root_grp_name)

        multipy_global_info_name = self.prefix_name + '_' + self.type + "_Head_Neck_Global_Tem_" + str(
            self.val) + "_Div"
        cmds.createNode('multiplyDivide', n=multipy_global_info_name)
        cmds.connectAttr((curve_info_name + ".arcLength"), (multipy_global_info_name + ".input1X"), f=True)
        cmds.connectAttr((root_grp_name + ".sy"), (multipy_global_info_name + ".input2X"), f=True)
        cmds.connectAttr((multipy_global_info_name + ".outputX"), (multipy_info_name + ".input1X"), f=True)
        input_cruve_getAttr = cmds.getAttr(curve_info_name + ".arcLength")
        cmds.setAttr((multipy_info_name + ".input2X"), input_cruve_getAttr)
        cmds.setAttr((multipy_global_info_name + ".operation"), 2)

        # now add the connec to the result jnt
        a = 0
        while a < len(bind_jnt_list):
            cmds.connectAttr((multipy_info_name + ".outputX"), (bind_jnt_list[a] + ".sx"), f=True)
            a += 1

        # LOWER MOUTH
        final_base_common = self.prefix_name + '_' + self.type + '_Head_Lower_Mouth_Base_Tem_' + str(self.val)
        jnt_name = final_base_common + '_Jnt'
        cmds.select(cl=True)
        cmds.joint(n=jnt_name, p=(self.final_ctrl_list[self.final_head_head_common]['t_pos'][0],
                                  self.final_ctrl_list[self.final_head_head_common]['t_pos'][1],
                                  self.final_ctrl_list[self.final_head_head_common]['t_pos'][2]))
        cmds.select(self.final_lower_mouth_jnt, jnt_name)
        cmds.parent()
        # create a controller
        self.controller_class.circle_ctrl()
        sel_ctrl = cmds.ls(sl=True)
        cmds.rename(sel_ctrl[0], self.lower_mouth_ctrl)
        mouth_ctrl_shape_name = self.lower_mouth_ctrl + 'Shape'
        mouth_ctrl_grp_name = self.lower_mouth_ctrl + '_Grp'
        lowe_mouth_base_jnt_grp = mouth_ctrl_grp_name
        cmds.select(mouth_ctrl_shape_name, jnt_name)
        cmds.parent(r=True, s=True)
        cmds.select(jnt_name)
        cmds.group(n=mouth_ctrl_grp_name)
        cmds.parentConstraint(head_ctrl_name, mouth_ctrl_grp_name, mo=True)
        cmds.select(self.lower_mouth_ctrl)
        cmds.delete()

        # UPPER MOUTH
        final_base_common = self.prefix_name + '_' + self.type + '_Head_Upper_Mouth_Base_Tem_' + str(self.val)
        jnt_name = final_base_common + '_Jnt'
        cmds.select(cl=True)
        cmds.joint(n=jnt_name, p=(self.final_ctrl_list[self.final_head_head_common]['t_pos'][0],
                                  self.final_ctrl_list[self.final_head_head_common]['t_pos'][1],
                                  self.final_ctrl_list[self.final_head_head_common]['t_pos'][2]))
        cmds.select(self.final_upper_mouth_jnt, jnt_name)
        cmds.parent()
        # create a controller
        self.controller_class.circle_ctrl()
        sel_ctrl = cmds.ls(sl=True)
        cmds.rename(sel_ctrl[0], self.upper_mouth_ctrl)
        mouth_ctrl_shape_name = self.upper_mouth_ctrl + 'Shape'
        mouth_ctrl_grp_name = self.upper_mouth_ctrl + '_Grp'
        upper_mouth_base_jnt_grp = mouth_ctrl_grp_name
        cmds.select(mouth_ctrl_shape_name, jnt_name)
        cmds.parent(r=True, s=True)
        cmds.select(jnt_name)
        cmds.group(n=mouth_ctrl_grp_name)
        cmds.parentConstraint(head_ctrl_name, mouth_ctrl_grp_name, mo=True)
        cmds.select(self.upper_mouth_ctrl)
        cmds.delete()

        # L EAR
        final_base_common = self.prefix_name + '_' + self.type + '_Head_L_Ear_Base_Tem_' + str(self.val)
        jnt_name = final_base_common + '_Jnt'
        cmds.select(cl=True)
        cmds.joint(n=jnt_name, p=(self.final_ctrl_list[self.final_head_head_common]['t_pos'][0],
                                  self.final_ctrl_list[self.final_head_head_common]['t_pos'][1],
                                  self.final_ctrl_list[self.final_head_head_common]['t_pos'][2]))
        cmds.select(self.final_l_ear_jnt, jnt_name)
        cmds.parent()
        # create a controller
        self.controller_class.circle_ctrl()
        sel_ctrl = cmds.ls(sl=True)
        cmds.rename(sel_ctrl[0], self.l_ear_ctrl)
        mouth_ctrl_shape_name = self.l_ear_ctrl + 'Shape'
        mouth_ctrl_grp_name = self.l_ear_ctrl + '_Grp'
        left_ear_grp = mouth_ctrl_grp_name
        cmds.select(mouth_ctrl_shape_name, jnt_name)
        cmds.parent(r=True, s=True)
        cmds.select(jnt_name)
        cmds.group(n=mouth_ctrl_grp_name)
        cmds.parentConstraint(head_ctrl_name, mouth_ctrl_grp_name, mo=True)
        cmds.select(self.l_ear_ctrl)
        cmds.delete()

        # R EAR
        final_base_common = self.prefix_name + '_' + self.type + '_Head_R_Ear_Base_Tem_' + str(self.val)
        jnt_name = final_base_common + '_Jnt'
        cmds.select(cl=True)
        cmds.joint(n=jnt_name, p=(self.final_ctrl_list[self.final_head_head_common]['t_pos'][0],
                                  self.final_ctrl_list[self.final_head_head_common]['t_pos'][1],
                                  self.final_ctrl_list[self.final_head_head_common]['t_pos'][2]))
        cmds.select(self.final_r_ear_jnt, jnt_name)
        cmds.parent()
        # create a controller
        self.controller_class.circle_ctrl()
        sel_ctrl = cmds.ls(sl=True)
        cmds.rename(sel_ctrl[0], self.r_ear_ctrl)
        mouth_ctrl_shape_name = self.r_ear_ctrl + 'Shape'
        mouth_ctrl_grp_name = self.r_ear_ctrl + '_Grp'
        right_ear_grp = mouth_ctrl_grp_name
        cmds.select(mouth_ctrl_shape_name, jnt_name)
        cmds.parent(r=True, s=True)
        cmds.select(jnt_name)
        cmds.group(n=mouth_ctrl_grp_name)
        cmds.parentConstraint(head_ctrl_name, mouth_ctrl_grp_name, mo=True)
        cmds.select(self.r_ear_ctrl)
        cmds.delete()

        # L EYE
        # Template_Human_Head_Left_Eye_1_Tem_1_Ctrl
        eye_name = self.prefix_name + '_' + self.type + '_Head_Left_Eye_*_Tem_' + str(self.val) + "_Ctrl"
        l_eye_ctrl = self.prefix_name + '_' + self.type + '_Head_Left_Eye_1_Tem_' + str(self.val) + "_Ctrl"
        cmds.select(eye_name)
        sel_eye = cmds.ls(sl=True)
        cmds.select(cl=True)
        a = 0
        while a < len(sel_eye):
            # Template_Human_Spine_L_Breast_1_Tem_1_Ctrl
            plusOne = a + 1
            # get the position
            jnt_pos = cmds.xform(sel_eye[a], q=1, ws=1, rp=1)
            common = self.prefix_name + "_" + self.type + "_Head_Left_Eye_" + str(plusOne) + "_" + str(self.val)
            jnt_name = common + "_Result_Jnt"
            ctrl_name = common + "_Ctrl"
            ctrl_grp_name = ctrl_name + '_Grp'
            cmds.joint(n=jnt_name, p=(jnt_pos[0], jnt_pos[1], jnt_pos[2]))
            self.controller_class.circle_ctrl()
            sel_ctrl = cmds.ls(sl=True)
            cmds.rename(sel_ctrl[0], ctrl_name)
            cmds.move(jnt_pos[0], jnt_pos[1], jnt_pos[2])
            cmds.select(ctrl_name)
            cmds.DeleteHistory()
            cmds.FreezeTransformations()
            cmds.group(n=ctrl_grp_name)
            self.helper_class.color_val(color='Red',
                                        obj_name=ctrl_name)
            cmds.parentConstraint(ctrl_name, jnt_name, mo=True)
            jnt_grp_name = self.prefix_name + "_" + self.type + "_Head_Left_Eye_" + str(self.val) + "_Jnt_Grp"
            left_eye_grp = jnt_grp_name
            cmds.parentConstraint(head_ctrl_name, ctrl_grp_name, mo=True)
            if cmds.objExists(jnt_grp_name):
                cmds.select(jnt_name, ctrl_grp_name, jnt_grp_name)
                cmds.parent()
            else:
                cmds.select(jnt_name, ctrl_grp_name)
                cmds.group(n=jnt_grp_name)

            cmds.select(cl=True)
            a += 1

        # R EYE
        # Template_Human_Head_Right_Eye_1_Tem_1_Ctrl
        eye_name = self.prefix_name + '_' + self.type + '_Head_Right_Eye_*_Tem_' + str(self.val) + "_Ctrl"
        r_eye_ctrl = self.prefix_name + '_' + self.type + '_Head_Right_Eye_1_Tem_' + str(self.val) + "_Ctrl"
        cmds.select(eye_name)
        sel_eye = cmds.ls(sl=True)
        cmds.select(cl=True)
        a = 0
        while a < len(sel_eye):
            # Template_Human_Spine_L_Breast_1_Tem_1_Ctrl
            plusOne = a + 1
            # get the position
            jnt_pos = cmds.xform(sel_eye[a], q=1, ws=1, rp=1)
            common = self.prefix_name + "_" + self.type + "_Head_Right_Eye_" + str(plusOne) + "_" + str(self.val)
            jnt_name = common + "_Result_Jnt"
            ctrl_name = common + "_Ctrl"
            ctrl_grp_name = ctrl_name + '_Grp'
            cmds.joint(n=jnt_name, p=(jnt_pos[0], jnt_pos[1], jnt_pos[2]))
            self.controller_class.circle_ctrl()
            sel_ctrl = cmds.ls(sl=True)
            cmds.rename(sel_ctrl[0], ctrl_name)
            cmds.move(jnt_pos[0], jnt_pos[1], jnt_pos[2])
            cmds.select(ctrl_name)
            cmds.DeleteHistory()
            cmds.FreezeTransformations()
            cmds.group(n=ctrl_grp_name)
            self.helper_class.color_val(color='Blue',
                                        obj_name=ctrl_name)
            cmds.parentConstraint(ctrl_name, jnt_name, mo=True)
            jnt_grp_name = self.prefix_name + "_" + self.type + "_Head_Right_Eye_" + str(self.val) + "_Jnt_Grp"
            right_eye_grp = jnt_grp_name
            cmds.parentConstraint(head_ctrl_name, ctrl_grp_name, mo=True)
            if cmds.objExists(jnt_grp_name):
                cmds.select(jnt_name, ctrl_grp_name, jnt_grp_name)
                cmds.parent()
            else:
                cmds.select(jnt_name, ctrl_grp_name)
                cmds.group(n=jnt_grp_name)

            cmds.select(cl=True)
            a += 1

        cmds.select(self.final_neck_jnt, self.ik_spine, self.ik_curve_name, self.neck_bind_jnt_grp_name,
                    self.head_bind_jnt_grp_name, upper_mouth_base_jnt_grp,
                    lowe_mouth_base_jnt_grp, self.final_neck_jnt,
                    left_ear_grp, right_ear_grp, head_ctrl_grp_name, self.final_neck_bind_jnt)
        if cmds.objExists(l_eye_ctrl):
            cmds.select(left_eye_grp, add=True)
        if cmds.objExists(r_eye_ctrl):
            cmds.select(right_eye_grp, add=True)

        head_grp_name = self.prefix_name + "_" + self.type + "_Head_Tem_" + str(self.val) + "_Grp"
        cmds.group(n=head_grp_name)

        cmds.select(head_grp_name, root_grp_name)
        cmds.parent()

        # Create a Connection
        neck_shoulder_loc_name = self.prefix_name + "_" + self.type + "_Head_Neck_Shoulder_Tem_" + str(
            self.val) + "_LOC"
        cmds.spaceLocator(n=neck_shoulder_loc_name, p=(0, 0, 0))
        cmds.parentConstraint(self.final_neck_jnt, neck_shoulder_loc_name, mo=False)
        cmds.select(neck_shoulder_loc_name + "_parentConstraint1")
        cmds.delete()
        cmds.select(neck_shoulder_loc_name)
        cmds.DeleteHistory()
        cmds.FreezeTransformations()
        cmds.select(neck_shoulder_loc_name, root_grp_name)
        cmds.parent()

        # make a fk grp
        fk_grp_name = self.final_neck_jnt + "_Grp"
        cmds.select(self.final_neck_jnt)
        cmds.group(n=fk_grp_name)
        print('this is the : ', neck_shoulder_loc_name)
        cmds.parentConstraint(neck_shoulder_loc_name, fk_grp_name, mo=True)

        '''

        cmds.select(neck_jnt_name,ik_spine,ik_curve_name,neck_bind_jnt_grp_name,
                    head_bind_jnt_grp_name,upper_head_base_jnt_name,
                    lower_head_base_jnt_name,upper_head_ctrl_grp_name,lower_head_ctrl_grp_name,fk_1_jnt_name,
                    l_ear_grp_name,r_ear_grp_name)
        if cmds.objExists(l_eyes):
            cmds.select(l_eye_grp_name,add=True)
        if cmds.objExists(r_eyes):
            cmds.select(r_eye_grp_name,add=True)

        head_grp_name = prefix_name  + type + "_Head_Tem_" + str(no) + "_Grp"
        cmds.group(n=head_grp_name)

        cmds.select(head_grp_name,root_grp_name)
        cmds.parent()

        #Create a Connection
        neck_shoulder_loc_name = prefix_name  + type + "_Head_Neck_Shoulder_Tem_" + str(no) + "_LOC"
        cmds.spaceLocator(n=neck_shoulder_loc_name,p=(0,0,0))
        cmds.parentConstraint(neck_ctrl_name,neck_shoulder_loc_name,mo=False)
        cmds.select(neck_shoulder_loc_name + "_parentConstraint1")
        cmds.delete()
        cmds.select(neck_shoulder_loc_name)
        cmds.DeleteHistory()
        cmds.FreezeTransformations()
        cmds.select(neck_shoulder_loc_name,root_grp_name)
        cmds.parent()

        #make a fk grp
        fk_grp_name = fk_1_jnt_name + "_Grp"
        cmds.select(fk_1_jnt_name)
        cmds.group(n=fk_grp_name)
        cmds.parentConstraint(neck_shoulder_loc_name,fk_grp_name,mo=True)
        '''

    def get_each_pos_data(self):
        # new_base
        # Template_Animal_Head_Base_Tem_1_Ctrl
        # Template_Human_Head_Base_Tem_1_Ctrl
        # final base ctrl
        self.final_ctrl_list = {}
        ctrl_name = '_Ctrl'
        self.final_base_common = self.prefix_name + '_' + self.type + '_Head_Base_Tem_' + str(self.val)
        self.final_base_ctrl = self.final_base_common + ctrl_name
        self.final_base_jnt = self.final_base_common + '_Result_Jnt'
        self.final_base_ctrl_t_pos = cmds.xform(self.final_base_ctrl, q=1, ws=1, rp=1)
        self.final_base_ctrl_r_pos = cmds.xform(self.final_base_ctrl, q=1, rotation=1)

        # Template_Human_Head_Neck_Tem_1_Ctrl
        # final neck ctrl
        self.final_neck_common = self.prefix_name + '_' + self.type + '_Head_Neck_Tem_' + str(self.val)
        self.final_neck_ctrl = self.final_neck_common + ctrl_name
        self.final_neck_jnt = self.final_neck_common + '_Result_Jnt'
        self.final_neck_ctrl_t_pos = cmds.xform(self.final_neck_ctrl, q=1, ws=1, rp=1)
        self.final_neck_ctrl_r_pos = cmds.xform(self.final_neck_ctrl, q=1, rotation=1)
        self.final_ctrl_list[self.final_neck_common] = {}
        self.final_ctrl_list[self.final_neck_common]['t_pos'] = self.final_neck_ctrl_t_pos
        self.final_ctrl_list[self.final_neck_common]['r_pos'] = self.final_neck_ctrl_r_pos

        # Template_Human_Head_Head_Tem_1_Ctrl
        # final head face ctrl
        self.final_head_head_common = self.prefix_name + '_' + self.type + '_Head_Head_Tem_' + str(self.val)
        self.final_head_head_ctrl = self.final_head_head_common + ctrl_name
        self.final_head_head_jnt = self.final_head_head_common + '_Result_Jnt'
        self.final_head_head_ctrl_t_pos = cmds.xform(self.final_head_head_ctrl, q=1, ws=1, rp=1)
        self.final_head_head_ctrl_r_pos = cmds.xform(self.final_head_head_ctrl, q=1, rotation=1)
        self.final_ctrl_list[self.final_head_head_common] = {}
        self.final_ctrl_list[self.final_head_head_common]['t_pos'] = self.final_head_head_ctrl_t_pos
        self.final_ctrl_list[self.final_head_head_common]['r_pos'] = self.final_head_head_ctrl_r_pos

        # Template_Human_Head_Lower_Mouth_Tem_1_Ctrl
        # final lower face
        self.final_lower_mouth_common = self.prefix_name + '_' + self.type + '_Head_Lower_Mouth_Tem_' + str(self.val)
        lower_mouth_common = self.prefix_name + '_' + self.type + '_Head_Lower_Mouth_' + str(self.val)
        self.final_lower_mouth_ctrl = self.final_lower_mouth_common + ctrl_name
        self.lower_mouth_ctrl = lower_mouth_common + ctrl_name
        self.final_lower_mouth_jnt = self.final_lower_mouth_common + '_Result_Jnt'
        self.final_lower_mouth_ctrl_t_pos = cmds.xform(self.final_lower_mouth_ctrl, q=1, ws=1, rp=1)
        self.final_lower_mouth_ctrl_r_pos = cmds.xform(self.final_lower_mouth_ctrl, q=1, rotation=1)
        self.final_ctrl_list[self.final_lower_mouth_common] = {}
        self.final_ctrl_list[self.final_lower_mouth_common]['t_pos'] = self.final_lower_mouth_ctrl_t_pos
        self.final_ctrl_list[self.final_lower_mouth_common]['r_pos'] = self.final_lower_mouth_ctrl_r_pos

        # Template_Human_Head_Lower_Mouth_Tem_1_Ctrl
        # final upper face
        self.final_upper_mouth_common = self.prefix_name + '_' + self.type + '_Head_Upper_Mouth_Tem_' + str(self.val)
        upper_mouth_common = self.prefix_name + '_' + self.type + '_Head_Upper_Mouth_' + str(self.val)
        self.final_upper_mouth_ctrl = self.final_upper_mouth_common + ctrl_name
        self.upper_mouth_ctrl = upper_mouth_common + ctrl_name
        self.final_upper_mouth_jnt = self.final_upper_mouth_common + '_Result_Jnt'
        self.final_upper_mouth_ctrl_t_pos = cmds.xform(self.final_upper_mouth_ctrl, q=1, ws=1, rp=1)
        self.final_upper_mouth_ctrl_r_pos = cmds.xform(self.final_upper_mouth_ctrl, q=1, rotation=1)
        self.final_ctrl_list[self.final_upper_mouth_common] = {}
        self.final_ctrl_list[self.final_upper_mouth_common]['t_pos'] = self.final_upper_mouth_ctrl_t_pos
        self.final_ctrl_list[self.final_upper_mouth_common]['r_pos'] = self.final_upper_mouth_ctrl_r_pos

        # Template_Human_Head_Left_Ear_Tem_1_Ctrl
        # final_l_ear
        self.final_l_ear_common = self.prefix_name + '_' + self.type + '_Head_Left_Ear_Tem_' + str(self.val)
        l_ear_common = self.prefix_name + '_' + self.type + '_Head_Left_Ear_' + str(self.val)
        self.final_l_ear_ctrl = self.final_l_ear_common + ctrl_name
        self.l_ear_ctrl = l_ear_common + ctrl_name
        self.final_l_ear_jnt = self.final_l_ear_common + '_Result_Jnt'
        self.final_l_ear_ctrl_t_pos = cmds.xform(self.final_l_ear_ctrl, q=1, ws=1, rp=1)
        self.final_l_ear_ctrl_r_pos = cmds.xform(self.final_l_ear_ctrl, q=1, rotation=1)
        self.final_ctrl_list[self.final_l_ear_common] = {}
        self.final_ctrl_list[self.final_l_ear_common]['t_pos'] = self.final_l_ear_ctrl_t_pos
        self.final_ctrl_list[self.final_l_ear_common]['r_pos'] = self.final_l_ear_ctrl_r_pos

        # Template_Human_Head_Right_Ear_Tem_1_Ctrl
        # final r ear
        self.final_r_ear_common = self.prefix_name + '_' + self.type + '_Head_Right_Ear_Tem_' + str(self.val)
        r_ear_common = self.prefix_name + '_' + self.type + '_Head_Right_Ear_' + str(self.val)
        self.final_r_ear_ctrl = self.final_r_ear_common + ctrl_name
        self.r_ear_ctrl = r_ear_common + ctrl_name
        self.final_r_ear_jnt = self.final_r_ear_common + '_Result_Jnt'
        self.final_r_ear_ctrl_t_pos = cmds.xform(self.final_r_ear_ctrl, q=1, ws=1, rp=1)
        self.final_r_ear_ctrl_r_pos = cmds.xform(self.final_r_ear_ctrl, q=1, rotation=1)
        self.final_ctrl_list[self.final_r_ear_common] = {}
        self.final_ctrl_list[self.final_r_ear_common]['t_pos'] = self.final_r_ear_ctrl_t_pos
        self.final_ctrl_list[self.final_r_ear_common]['r_pos'] = self.final_r_ear_ctrl_r_pos

        # Template_Human_Head_Head_Top_Tem_1_Ctrl
        # final upper face

        # list l eye
        # list r eye

    def get_grp_name(self):
        self.sphere_group_name = self.prefix_name + '_' + self.type + "_Head_Face_Tem_" + str(self.val) + "_Sphere_Grp"
        self.cluster_group_name = self.prefix_name + '_' + self.type + "_Head_Face_Tem_" + str(
            self.val) + "_Cluster_Grp"
        self.cylinder_group_name = self.prefix_name + '_' + self.type + "_Head_Face_Tem_" + str(
            self.val) + "_Cylinder_Grp"
        self.ctrl_group_name = self.prefix_name + '_' + self.type + "_Head_Face_Tem_" + str(self.val) + "_Ctrl_Grp"
        self.head_ctrl_name = self.prefix_name + '_' + self.type + '_Head_Head_Tem_' + str(self.val) + '_Ctrl'
        self.base_ctrl_name = self.prefix_name + '_' + self.type + '_Head_Base_Tem_' + str(self.val) + '_Ctrl'
        self.neck_ctrl_name = self.prefix_name + '_' + self.type + '_Head_Neck_Tem_' + str(self.val) + '_Ctrl'

        # self.eye_sphere_name = self.prefix_name + '_' + self.type + '_Head_' + self.eye_side + '_Eye_' + str(a+1) + '_Tem_' + str(self.val) + '_Geo'

    def roll_bone(self, type, upper_object, lower_object, no_of_bone):
        # create a curve
        self.curve_common = self.prefix_name + "_" + self.type + "_Neck_" + type + "_Tem_" + str(self.val)
        self.curve_name = self.curve_common + '_Crv'
        self.curve_shape_name = self.curve_name + 'Shape'
        self.curve_0_clu_name = self.prefix_name + "_" + self.type + "_Neck_" + type + "_0_Tem_" + str(
            self.val) + '_Clu'
        self.curve_0_clu_handle_name = self.curve_0_clu_name + 'Handle'
        self.curve_1_clu_name = self.prefix_name + "_" + self.type + "_Neck_" + type + "_1_Tem_" + str(
            self.val) + '_Clu'
        self.curve_1_clu_handle_name = self.curve_1_clu_name + 'Handle'
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
        self.neck_sphere_list = {}
        # create a point on curve
        a = 0
        toal_minus = 0.5
        value = 1 - toal_minus
        average_val = value / (no_of_bone - 1)
        start_val = 0.25
        while a < no_of_bone:
            common_name = self.prefix_name + "_" + self.type + "_Neck_" + type + "_" + str(a) + "_Tem_" + str(self.val)
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

            cmds.setAttr((self.poc_name + '.parameter'), start_val)
            start_val += average_val

            xform_val = cmds.xform(self.sphere_name, q=1, ws=1, rp=1)
            self.neck_sphere_list[common_name] = xform_val
            # delete the sphere
            cmds.select(self.sphere_name, self.poc_name)
            cmds.delete()
            # setAttr "Template_L_Arm_Lower_0_Tem_1_POC.parameter" 0.2;
            a += 1
        # delete the curve
        cmds.select(self.curve_name, self.curve_0_clu_handle_name, self.curve_1_clu_handle_name)
        cmds.delete()

    def controller_twick_def(self):
        self.head_grp_list = ['Human_Head_Grp', 'Animal_Head_Grp']
        for each_grp in self.head_grp_list:
            # list of the all children
            if cmds.objExists(each_grp):
                children_list = cmds.listRelatives(each_grp, children=True)
                if children_list != None:
                    for each_child in children_list:
                        # get all the controller data
                        self.head_data(each_child)

                        self.final_controller_def()

    def final_controller_def(self):
        grp_name = self.prefix_name + '_' + self.type + '_Head_' + str(self.val) + '_Twick_Ctrl_Grp'
        main_grp_name = 'Head_Twick_Ctrl_Grp'

        ctrl_list = []
        # neck controller
        self.controller_class.circle_ctrl()
        ctrl_name = self.final_neck_common + '_Twick_Ctrl'
        cmds.rename('circle_ctrl', ctrl_name)
        self.controller_pos(ctrl_name,
                            self.final_neck_common)
        ctrl_list.append(ctrl_name)
        self.helper_class.color_val(color='Yellow',
                                    obj_name=ctrl_name)

        # head controlle
        self.controller_class.circle_ctrl()
        ctrl_name = self.final_head_head_common + '_Twick_Ctrl'
        cmds.rename('circle_ctrl', ctrl_name)
        self.controller_pos(ctrl_name,
                            self.final_head_head_common)
        self.helper_class.color_val(color='Yellow',
                                    obj_name=ctrl_name)
        ctrl_list.append(ctrl_name)

        # lower mouth
        self.controller_class.circle_ctrl()
        ctrl_name = self.final_lower_mouth_common + '_Twick_Ctrl'
        cmds.rename('circle_ctrl', ctrl_name)
        self.controller_pos(ctrl_name,
                            self.final_lower_mouth_common)
        self.helper_class.color_val(color='Yellow',
                                    obj_name=ctrl_name)
        ctrl_list.append(ctrl_name)

        # upper mouth
        self.controller_class.circle_ctrl()
        ctrl_name = self.final_upper_mouth_common + '_Twick_Ctrl'
        cmds.rename('circle_ctrl', ctrl_name)
        self.controller_pos(ctrl_name,
                            self.final_upper_mouth_common)
        self.helper_class.color_val(color='Yellow',
                                    obj_name=ctrl_name)
        ctrl_list.append(ctrl_name)

        # l ear
        self.controller_class.circle_ctrl()
        ctrl_name = self.final_l_ear_common + '_Twick_Ctrl'
        cmds.rename('circle_ctrl', ctrl_name)
        self.controller_pos(ctrl_name,
                            self.final_l_ear_common)
        self.helper_class.color_val(color='Blue',
                                    obj_name=ctrl_name)
        ctrl_list.append(ctrl_name)

        # r Ear
        self.controller_class.circle_ctrl()
        ctrl_name = self.final_r_ear_common + '_Twick_Ctrl'
        cmds.rename('circle_ctrl', ctrl_name)
        self.controller_pos(ctrl_name,
                            self.final_r_ear_common)
        self.helper_class.color_val(color='Red',
                                    obj_name=ctrl_name)
        ctrl_list.append(ctrl_name)

        # Create L Eye
        # Template_Human_Head_Left_Eye_1_Tem_1_Ctrl
        l_eye_ctrl = self.prefix_name + '_' + self.type + '_Head_Left_Eye_*_Tem_' + str(self.val) + '_Ctrl'
        r_eye_ctrl = self.prefix_name + '_' + self.type + '_Head_Right_Eye_*_Tem_' + str(self.val) + '_Ctrl'
        cmds.select(cl=True)
        if cmds.objExists(l_eye_ctrl):
            cmds.select(l_eye_ctrl)
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
                ctrl_list.append(ctrl_name)

                self.helper_class.color_val(color='Blue',
                                            obj_name=ctrl_name)

        if cmds.objExists(r_eye_ctrl):
            cmds.select(r_eye_ctrl)
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
                ctrl_list.append(ctrl_name)

                self.helper_class.color_val(color='Red',
                                            obj_name=ctrl_name)

        for each in ctrl_list:
            self.helper_class.grp_create(object_name=each,
                                         grp_name=grp_name)

        self.helper_class.grp_create(object_name=grp_name,
                                     grp_name=main_grp_name)

    def controller_pos(self, ctrl_name, common_name):
        cmds.setAttr((ctrl_name + '.tx'), self.final_ctrl_list[common_name]['t_pos'][0])
        cmds.setAttr((ctrl_name + '.ty'), self.final_ctrl_list[common_name]['t_pos'][1])
        cmds.setAttr((ctrl_name + '.tz'), self.final_ctrl_list[common_name]['t_pos'][2])

        cmds.setAttr((ctrl_name + '.rx'), self.final_ctrl_list[common_name]['r_pos'][0])
        cmds.setAttr((ctrl_name + '.ry'), self.final_ctrl_list[common_name]['r_pos'][1])
        cmds.setAttr((ctrl_name + '.rz'), self.final_ctrl_list[common_name]['r_pos'][2])

        pass

        '''
        for each_main_grp in total_main_grp:
            self.controller_get_data(each_main_grp)
            #create a joint in each pos
            for each_ctrl in self.ctrl_list:
                split_each_ctrl = each_ctrl.split('_Ctrl')[0]
                jnt_name = split_each_ctrl + '_Jnt'
                cmds.select(cl=True)
                cmds.joint(n=jnt_name,p=(self.ctrl_list[each_ctrl]['Trans'][0],
                                         self.ctrl_list[each_ctrl]['Trans'][1],
                                         self.ctrl_list[each_ctrl]['Trans'][2]))

            #parent the object
            cmds.select(self.head_jnt_name,
                        self.neck_jnt_name)
            cmds.parent()
            cmds.select(self.head_top_jnt_name,self.lower_mouth_jnt_name,self.upper_mouth_jnt_name,
                        self.left_ear_jnt_name,self.right_ear_jnt_name,
                        self.head_jnt_name)
            cmds.parent()

            #Template_Human_Head_Tem_1_Main_Ctrl_Grp
            ctrl_grp_name = self.prefix_name + '_' + self.type + '_Head_Tem_' + str(self.val) + '_Main_Ctrl_Grp'
            cmds.select(self.neck_jnt_name,self.eye_jnt_list)
            cmds.group(n=ctrl_grp_name)

            head_grp_name = 'Head_Ctrl_Grp'
            self.helper_class.parent_child_grp(parent=head_grp_name,
                                               child=ctrl_grp_name)
            main_grp = 'Controller_Grp'
            self.helper_class.parent_child_grp(parent=main_grp,
                                               child=head_grp_name)
        '''

    def controller_get_data(self, main_grp_name):
        # Template_Human_Head_Tem_1_Main_Grp
        main_grp_split = main_grp_name.split('_')
        self.prefix_name = main_grp_split[0]
        self.type = main_grp_split[1]
        self.val = main_grp_split[4]

        self.ctrl_list = {}

        # BASE CONTROLLER
        self.base_common = self.prefix_name + '_' + self.type + '_Head_Base_Tem_' + str(self.val)
        self.base_ctrl_name = self.base_common + '_Ctrl'
        self.base_jnt_name = self.base_common + '_Jnt'
        self.base_ctrl_get_trans = cmds.xform(self.base_ctrl_name, q=1, ws=1, rp=1)
        self.base_ctrl_get_rot = cmds.getAttr(self.base_ctrl_name + '.r')

        # NECK CONTROLLER
        self.neck_common = self.prefix_name + '_' + self.type + '_Head_Neck_Tem_' + str(self.val)
        self.neck_ctrl_name = self.neck_common + '_Ctrl'
        self.neck_jnt_name = self.neck_common + '_Jnt'
        self.neck_ctrl_get_trans = cmds.xform(self.neck_ctrl_name, q=1, ws=1, rp=1)
        self.neck_ctrl_get_rot = cmds.getAttr(self.neck_ctrl_name + '.r')
        self.ctrl_list[self.neck_ctrl_name] = {}
        self.ctrl_list[self.neck_ctrl_name]['Trans'] = self.neck_ctrl_get_trans
        self.ctrl_list[self.neck_ctrl_name]['Rot'] = self.neck_ctrl_get_rot

        # HEAD CONTROLLER
        self.head_common = self.prefix_name + '_' + self.type + '_Head_Head_Tem_' + str(self.val)
        self.head_ctrl_name = self.head_common + '_Ctrl'
        self.head_jnt_name = self.head_common + '_Jnt'
        self.head_ctrl_get_trans = cmds.xform(self.head_ctrl_name, q=1, ws=1, rp=1)
        self.head_ctrl_get_rot = cmds.getAttr(self.head_ctrl_name + '.r')
        self.ctrl_list[self.head_ctrl_name] = {}
        self.ctrl_list[self.head_ctrl_name]['Trans'] = self.head_ctrl_get_trans
        self.ctrl_list[self.head_ctrl_name]['Rot'] = self.head_ctrl_get_rot

        # HEAD TOP
        self.head_top_common = self.prefix_name + '_' + self.type + '_Head_Head_Top_Tem_' + str(self.val)
        self.head_top_ctrl_name = self.head_top_common + '_Ctrl'
        self.head_top_jnt_name = self.head_top_common + '_Jnt'
        self.head_top_ctrl_get_trans = cmds.xform(self.head_top_ctrl_name, q=1, ws=1, rp=1)
        self.head_top_ctrl_get_rot = cmds.getAttr(self.head_top_ctrl_name + '.r')
        self.ctrl_list[self.head_top_ctrl_name] = {}
        self.ctrl_list[self.head_top_ctrl_name]['Trans'] = self.head_top_ctrl_get_trans
        self.ctrl_list[self.head_top_ctrl_name]['Rot'] = self.head_top_ctrl_get_rot

        # LOWER MOUTH
        self.lower_mouth_common = self.prefix_name + '_' + self.type + '_Head_Lower_Mouth_Tem_' + str(self.val)
        self.lower_mouth_ctrl_name = self.lower_mouth_common + '_Ctrl'
        self.lower_mouth_jnt_name = self.lower_mouth_common + '_Jnt'
        self.lower_mouth_ctrl_get_trans = cmds.xform(self.lower_mouth_ctrl_name, q=1, ws=1, rp=1)
        self.lower_mouth_ctrl_get_rot = cmds.getAttr(self.lower_mouth_ctrl_name + '.r')
        self.ctrl_list[self.lower_mouth_ctrl_name] = {}
        self.ctrl_list[self.lower_mouth_ctrl_name]['Trans'] = self.lower_mouth_ctrl_get_trans
        self.ctrl_list[self.lower_mouth_ctrl_name]['Rot'] = self.lower_mouth_ctrl_get_rot

        # UPPER MOUTH
        self.upper_mouth_common = self.prefix_name + '_' + self.type + '_Head_Upper_Mouth_Tem_' + str(self.val)
        self.upper_mouth_ctrl_name = self.upper_mouth_common + '_Ctrl'
        self.upper_mouth_jnt_name = self.upper_mouth_common + '_Jnt'
        self.upper_mouth_ctrl_get_trans = cmds.xform(self.upper_mouth_ctrl_name, q=1, ws=1, rp=1)
        self.upper_mouth_ctrl_get_rot = cmds.getAttr(self.upper_mouth_ctrl_name + '.r')
        self.ctrl_list[self.upper_mouth_ctrl_name] = {}
        self.ctrl_list[self.upper_mouth_ctrl_name]['Trans'] = self.upper_mouth_ctrl_get_trans
        self.ctrl_list[self.upper_mouth_ctrl_name]['Rot'] = self.upper_mouth_ctrl_get_rot

        # LEFT EAR
        self.left_ear_common = self.prefix_name + '_' + self.type + '_Head_Left_Ear_Tem_' + str(self.val)
        self.left_ear_ctrl_name = self.left_ear_common + '_Ctrl'
        self.left_ear_jnt_name = self.left_ear_common + '_Jnt'
        self.left_ear_ctrl_get_trans = cmds.xform(self.left_ear_ctrl_name, q=1, ws=1, rp=1)
        self.left_ear_ctrl_get_rot = cmds.getAttr(self.left_ear_ctrl_name + '.r')
        self.ctrl_list[self.left_ear_ctrl_name] = {}
        self.ctrl_list[self.left_ear_ctrl_name]['Trans'] = self.left_ear_ctrl_get_trans
        self.ctrl_list[self.left_ear_ctrl_name]['Rot'] = self.left_ear_ctrl_get_rot

        # RIGHT EAR
        self.right_ear_common = self.prefix_name + '_' + self.type + '_Head_Right_Ear_Tem_' + str(self.val)
        self.right_ear_ctrl_name = self.right_ear_common + '_Ctrl'
        self.right_ear_jnt_name = self.right_ear_common + '_Jnt'
        self.right_ear_ctrl_get_trans = cmds.xform(self.right_ear_ctrl_name, q=1, ws=1, rp=1)
        self.right_ear_ctrl_get_rot = cmds.getAttr(self.right_ear_ctrl_name + '.r')
        self.ctrl_list[self.right_ear_ctrl_name] = {}
        self.ctrl_list[self.right_ear_ctrl_name]['Trans'] = self.right_ear_ctrl_get_trans
        self.ctrl_list[self.right_ear_ctrl_name]['Rot'] = self.right_ear_ctrl_get_rot

        # GET THE L EYE
        # Template_Human_Head_Left_Eye_1_Tem_1_Ctrl
        self.eye_jnt_list = []
        l_ctrl_name = self.prefix_name + '_' + self.type + '_Head_Left_Eye_*_Tem_' + str(self.val) + '_Ctrl'
        if cmds.objExists(l_ctrl_name):
            cmds.select(l_ctrl_name)
            sel_l_ctrl = cmds.ls(sl=True)
            a = 0
            while a < len(sel_l_ctrl):
                ctrl_common = sel_l_ctrl[a].split('_Ctrl')[0]
                ctrl_name = ctrl_common + '_Ctrl'
                jnt_name = ctrl_common + '_Jnt'
                self.ctrl_get_trans = cmds.xform(ctrl_name, q=1, ws=1, rp=1)
                self.ctrl_get_rot = cmds.getAttr(ctrl_name + '.r')
                self.ctrl_list[ctrl_name] = {}
                self.ctrl_list[ctrl_name]['Trans'] = self.ctrl_get_trans
                self.ctrl_list[ctrl_name]['Rot'] = self.ctrl_get_rot
                self.eye_jnt_list.append(jnt_name)
                a += 1

        r_ctrl_name = self.prefix_name + '_' + self.type + '_Head_Right_Eye_*_Tem_' + str(self.val) + '_Ctrl'
        if cmds.objExists(r_ctrl_name):
            cmds.select(r_ctrl_name)
            sel_r_ctrl = cmds.ls(sl=True)
            a = 0
            while a < len(sel_r_ctrl):
                ctrl_common = sel_r_ctrl[a].split('_Ctrl')[0]
                ctrl_name = ctrl_common + '_Ctrl'
                jnt_name = ctrl_common + '_Jnt'
                self.ctrl_get_trans = cmds.xform(ctrl_name, q=1, ws=1, rp=1)
                self.ctrl_get_rot = cmds.getAttr(ctrl_name + '.r')
                self.ctrl_list[ctrl_name] = {}
                self.ctrl_list[ctrl_name]['Trans'] = self.ctrl_get_trans
                self.ctrl_list[ctrl_name]['Rot'] = self.ctrl_get_rot
                self.eye_jnt_list.append(jnt_name)
                a += 1

    def bone_def(self):
        self.head_grp_list = ['Human_Head_Grp', 'Animal_Head_Grp']
        for each_grp in self.head_grp_list:
            # list of the all children
            if cmds.objExists(each_grp):
                children_list = cmds.listRelatives(each_grp, children=True)
                if children_list != None:
                    for each_child in children_list:
                        # get all the controller data
                        self.head_data(each_child)

                        # final the head
                        self.final_bone_head()

    def final_bone_head(self):
        self.final_head_top_common = self.prefix_name + '_' + self.type + '_Head_Head_Top_Tem_' + str(self.val)
        self.final_head_top_ctrl = self.final_head_top_common + '_Ctrl'
        self.final_head_top_jnt = self.final_head_top_common + '_Result_Jnt'
        self.final_head_top_ctrl_t_pos = cmds.xform(self.final_head_top_ctrl, q=1, ws=1, rp=1)
        self.final_head_top_ctrl_r_pos = cmds.xform(self.final_head_top_ctrl, q=1, rotation=1)
        self.final_ctrl_list[self.final_head_top_common] = {}
        self.final_ctrl_list[self.final_head_top_common]['t_pos'] = self.final_head_top_ctrl_t_pos
        self.final_ctrl_list[self.final_head_top_common]['r_pos'] = self.final_head_top_ctrl_r_pos

        jnt_all_list = []
        grp_name = self.prefix_name + '_' + self.type + '_Head_Bone_' + str(self.val) + '_Grp'
        main_grp_name = 'Head_Bone_Grp'
        # Now Create a bone on each position
        list = [self.final_neck_common, self.final_head_head_common, self.final_lower_mouth_common,
                self.final_upper_mouth_common,
                self.final_l_ear_common, self.final_r_ear_common, self.final_head_top_common]
        for each in list:
            common_name = each
            ctrl_name = common_name + '_Ctrl'
            jnt_name = common_name + '_Bone'
            cmds.select(cl=True)
            cmds.joint(n=jnt_name, p=(self.final_ctrl_list[common_name]['t_pos'][0],
                                      self.final_ctrl_list[common_name]['t_pos'][1],
                                      self.final_ctrl_list[common_name]['t_pos'][2]))

            self.helper_class.grp_create(object_name=jnt_name,
                                         grp_name=grp_name)

        # Check with left and right eye
        # Template_Human_Head_Left_Eye_1_Tem_1_Ctrl Template_Human_Head_Right_Eye_1_Tem_1_Ctrl
        l_eye_ctrl = self.prefix_name + '_' + self.type + '_Head_Left_Eye_*_Tem_' + str(self.val) + '_Ctrl'
        r_eye_ctrl = self.prefix_name + '_' + self.type + '_Head_Right_Eye_*_Tem_' + str(self.val) + '_Ctrl'
        cmds.select(l_eye_ctrl)
        cmds.select(r_eye_ctrl, add=True)
        sel_ctrl = cmds.ls(sl=True)
        for each in sel_ctrl:
            split_name = each.split('_Ctrl')[0]
            jnt_name = split_name + '_Bone'
            cmds.select(cl=True)
            # get the position
            get_pos = cmds.xform(each, q=1, ws=1, rp=1)
            cmds.joint(n=jnt_name, p=(get_pos[0], get_pos[1], get_pos[2]))
            jnt_all_list.append(jnt_name)
            self.helper_class.grp_create(object_name=jnt_name,
                                         grp_name=grp_name)

        neck_bone_name = self.final_neck_common + '_Bone'
        head_bone_name = self.final_head_head_common + '_Bone'
        lower_mouth_bone_name = self.final_lower_mouth_common + '_Bone'
        upper_mouth_bone_name = self.final_upper_mouth_common + '_Bone'
        l_ear_bone_name = self.final_l_ear_common + '_Bone'
        r_ear_bone_name = self.final_r_ear_common + '_Bone'
        head_top_bone_name = self.final_head_top_common + '_Bone'

        cmds.parent(head_bone_name, neck_bone_name)
        cmds.parent(lower_mouth_bone_name, upper_mouth_bone_name, l_ear_bone_name, r_ear_bone_name, head_top_bone_name,
                    head_bone_name)
        jnt_all_list.append(neck_bone_name)

        self.helper_class.grp_create(object_name=grp_name,
                                     grp_name=main_grp_name)

    def get_head(self):

        get_list = self.get_head_list()
        return len(get_list)

    def get_head_list(self):
        list = []
        self.head_grp_list = ['Human_Head_Grp', 'Animal_Head_Grp']
        for each_grp in self.head_grp_list:
            # list of the all children
            if cmds.objExists(each_grp):
                children_list = cmds.listRelatives(each_grp, children=True)
                if children_list != None:
                    for each_child in children_list:
                        list.append(each_child)
                        self.head_data(each_child)

        return list

    #################################################################CONTROLLER START
    def get_twick_ctrl_list(self, grp_name):
        self.head_data(grp_name)
        neck_twick_ctrl = self.final_neck_common + '_Twick_Ctrl'
        head_twick_ctrl = self.final_head_head_common + '_Twick_Ctrl'
        lower_mouth_twick_ctrl = self.final_lower_mouth_common + '_Twick_Ctrl'
        upper_mouth_twick_ctrl = self.final_upper_mouth_common + '_Twick_Ctrl'
        l_ear_twick_ctrl = self.final_l_ear_common + '_Twick_Ctrl'
        r_ear_twick_ctrl = self.final_r_ear_common + '_Twick_Ctrl'
        list = [neck_twick_ctrl, head_twick_ctrl, lower_mouth_twick_ctrl, upper_mouth_twick_ctrl, l_ear_twick_ctrl,
                r_ear_twick_ctrl]

        # Template_Human_Head_Left_Eye_1_Tem_1_Ctrl
        l_eye = self.prefix_name + '_' + self.type + '_Head_Left_Eye_*_Tem_' + str(self.val) + '_Ctrl'
        r_eye = self.prefix_name + '_' + self.type + '_Head_Right_Eye_*_Tem_' + str(self.val) + '_Ctrl'
        cmds.select(cl=True)
        if cmds.objExists(l_eye):
            cmds.select(l_eye)
        if cmds.objExists(r_eye):
            cmds.select(r_eye, add=True)
        sel_eye = cmds.ls(sl=True)
        for each in sel_eye:
            split_word = each.split('_Ctrl')[0]
            twick_ctrl_name = split_word + '_Twick_Ctrl'
            list.append(twick_ctrl_name)

        shape_name = neck_twick_ctrl + 'Shape'
        color_no = cmds.getAttr(shape_name + '.overrideColor')
        print('this is the color no : ', color_no)

        return list

        pass

    def _controller_def(self, widget):
        controller_list = {}
        # Head_Twick_Ctrl_Grp
        if cmds.objExists('Head_Twick_Ctrl_Grp'):
            self.horizontalLayout_22 = QtGui.QHBoxLayout(widget)
            self.horizontalLayout_22.setObjectName("horizontalLayout_22")
            self.controller_head_tab = QtGui.QTabWidget(widget)
            self.controller_head_tab.setObjectName("controller_head_tab")

            # get the head

            total_head = self.get_head_list()
            a = 0
            while a < len(total_head):
                self.controller_head_1_tab = QtGui.QWidget()
                self.controller_head_1_tab.setObjectName("controller_head_1_tab")
                self._controller_head_1_ui(total_head[a])
                self.head_data(total_head[a])
                name = self.type + '_Head ' + str(self.val)
                self.controller_head_tab.addTab(self.controller_head_1_tab, name)
                a += 1

            '''
            self.controller_head_1_tab = QtGui.QWidget()
            self.controller_head_1_tab.setObjectName("controller_head_1_tab")
            self._controller_head_1_ui()
            self.controller_head_tab.addTab(self.controller_head_1_tab, 'Head 1')

            self.controller_head_2_tab = QtGui.QWidget()
            self.controller_head_2_tab.setObjectName("controller_head_2_tab")
            self.controller_head_tab.addTab(self.controller_head_2_tab, 'Head 2')
            '''
            self.horizontalLayout_22.addWidget(self.controller_head_tab)

    def _controller_head_1_ui(self, grp_name):
        list = self.get_twick_ctrl_list(grp_name=grp_name)

        print(grp_name)

        self.gridLayout_30 = QtGui.QGridLayout(self.controller_head_1_tab)
        self.gridLayout_30.setObjectName("gridLayout_30")

        # for each in list

        # CONTROLLER NAME
        self.controller_name_label = QtGui.QLabel(self.controller_head_1_tab)
        self.controller_name_label.setObjectName("controller_name_label")
        self.controller_name_label.setText('Controller Name')
        self.gridLayout_30.addWidget(self.controller_name_label, 0, 1, 1, 5)

        # get the toatal controller name

        # CONTROLLER COLOR BUTTON
        self.controller_name_button = QtGui.QPushButton(self.controller_head_1_tab)
        self.controller_name_button.setEnabled(True)
        self.controller_name_button.setText("")
        self.controller_name_button.setObjectName("controller_name_button")
        self.controller_name_button.clicked.connect(self.controller_name_button_def)
        self.gridLayout_30.addWidget(self.controller_name_button, 1, 1, 1, 1)

        # CONTROLLER COLOR SLIDER
        self.controller_name_color_horizontalSlider = QtGui.QSlider(self.controller_head_1_tab)
        self.controller_name_color_horizontalSlider.setMinimumSize(QtCore.QSize(217, 0))
        self.controller_name_color_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.controller_name_color_horizontalSlider.setMinimum(0)
        self.controller_name_color_horizontalSlider.setMaximum(20)
        self.controller_name_color_horizontalSlider.setTickInterval(5)
        self.controller_name_color_horizontalSlider.valueChanged.connect(
            self.controller_name_color_horizontalSlider_def)
        self.controller_name_color_horizontalSlider.setObjectName("controller_name_color_horizontalSlider")

        self.gridLayout_30.addWidget(self.controller_name_color_horizontalSlider, 1, 2, 1, 1)

        # CONTROLER SEL BUTTON
        self.controller_name_select_tool_button = QtGui.QToolButton(self.controller_head_1_tab)
        self.controller_name_select_tool_button.setObjectName("controller_name_select_tool_button")
        self.controller_name_select_tool_button.setText('S')
        self.controller_name_select_tool_button.clicked.connect(self.controller_name_select_tool_button_def)
        self.gridLayout_30.addWidget(self.controller_name_select_tool_button, 1, 5, 1, 1)

        # SPACE ITEM
        self.space_item = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_30.addItem(self.space_item, 2, 0, 1, 5)

    def controller_name_button_def(self):
        color = QtGui.QColorDialog.getColor()
        rgb = (color.red(), color.green(), color.blue())
        self.controller_name_button.setStyleSheet(
            "background-color:rgb(%s,%s,%s)" % (color.red(), color.green(), color.blue()))

    def controller_name_color_horizontalSlider_def(self):
        value = self.controller_name_color_horizontalSlider.value()
        self.helper_class.slider_color(value, self.controller_name_button)

    def controller_name_select_tool_button_def(self):
        print('now object is going to select')
    ##
    #################################################################CONTROLLER END

