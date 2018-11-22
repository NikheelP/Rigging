class FACE:
    def __init__(self):
        self.helper_class = helper.HELPER()
        self.controller_class = controller_rig.controler()
        self.connection_class = connection.CONNECTION()

        self.crv_list = []
        self.loc_list = []
        self.sphere_list = []
        self.clu_list = []
        self.loc_center_list = []
        self.loc_grp_list = []
        self.mirror_loc = []

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

        # LEFT CHECKBOX
        self.left_check_box = QtGui.QCheckBox(self.widget)
        self.left_check_box.setObjectName("left_check_box")
        self.left_check_box.setText('Left Face')
        self.left_check_box.setChecked(True)
        self.leg_grid_layout.addWidget(self.left_check_box, 1, 0, 1, 1)

        # RIGHT CHECKBOX
        self.right_check_box = QtGui.QCheckBox(self.widget)
        self.right_check_box.setObjectName("right_check_box")
        self.right_check_box.setText('Right Face')
        self.right_check_box.setChecked(True)
        self.leg_grid_layout.addWidget(self.right_check_box, 1, 1, 1, 1)

        # EYE LABEL
        self.eye_label = QtGui.QLabel(self.widget)
        self.eye_label.setObjectName("eye_label")
        self.eye_label.setText('Eye : ')
        self.leg_grid_layout.addWidget(self.eye_label, 2, 0, 1, 1)
        # EYE CHECKBOX
        self.eye_check_box = QtGui.QCheckBox(self.widget)
        self.eye_check_box.setObjectName("eye_check_box")
        self.eye_check_box.setText('Eye')
        self.eye_check_box.stateChanged.connect(partial(self.face_checkbox_change, 0))
        self.leg_grid_layout.addWidget(self.eye_check_box, 3, 0, 1, 1)

        # EYE SIDE CHECKBOX
        self.eye_side_check_box = QtGui.QCheckBox(self.widget)
        self.eye_side_check_box.setObjectName("eye_side_check_box")
        self.eye_side_check_box.setText('Eye Side')
        self.eye_side_check_box.stateChanged.connect(partial(self.face_checkbox_change, 1))
        self.leg_grid_layout.addWidget(self.eye_side_check_box, 3, 1, 1, 1)

        # EYE SIDE 2 CHECKBOX
        self.eye_side_2_check_box = QtGui.QCheckBox(self.widget)
        self.eye_side_2_check_box.setObjectName("eye_side_2_check_box")
        self.eye_side_2_check_box.setText('Eye Side 2')
        self.eye_side_2_check_box.stateChanged.connect(partial(self.face_checkbox_change, 2))
        self.leg_grid_layout.addWidget(self.eye_side_2_check_box, 3, 2, 1, 1)

        # EYE LABEL
        self.no_eye_label = QtGui.QLabel(self.widget)
        self.no_eye_label.setObjectName("no_eye_eye_label")
        self.no_eye_label.setText('No Eye : ')
        self.no_eye_label.hide()
        self.leg_grid_layout.addWidget(self.no_eye_label, 4, 0, 1, 1)

        # EYE LINE EIDT
        self.no_eye_line_edit = QtGui.QLineEdit(self.widget)
        self.no_eye_line_edit.setObjectName("no_eye_eye_line_edit")
        self.validator = QtGui.QDoubleValidator()
        self.no_eye_line_edit.setValidator(self.validator)
        self.no_eye_line_edit.setText(str(15))
        self.no_eye_line_edit.hide()
        self.leg_grid_layout.addWidget(self.no_eye_line_edit, 4, 1, 1, 3)

        # EYE SIDE LABEL
        self.eye_side_label = QtGui.QLabel(self.widget)
        self.eye_side_label.setObjectName("eye_side_label")
        self.eye_side_label.setText('Eye Side : ')
        self.eye_side_label.hide()
        self.leg_grid_layout.addWidget(self.eye_side_label, 5, 0, 1, 1)

        # EYE SIDE LINE EIDT
        self.eye_side_line_edit = QtGui.QLineEdit(self.widget)
        self.eye_side_line_edit.setObjectName("eye_side_line_edit")
        self.eye_side_line_edit.setValidator(self.validator)
        self.eye_side_line_edit.setText(str(12))
        self.eye_side_line_edit.hide()
        self.leg_grid_layout.addWidget(self.eye_side_line_edit, 5, 1, 1, 3)

        # EYE SIDE 2 LABEL
        self.eye_side_2_label = QtGui.QLabel(self.widget)
        self.eye_side_2_label.setObjectName("eye_side_2_label")
        self.eye_side_2_label.setText('Eye Side 2 : ')
        self.eye_side_2_label.hide()
        self.leg_grid_layout.addWidget(self.eye_side_2_label, 6, 0, 1, 1)

        # EYE SIDE 2 LINE EIDT
        self.eye_side_2_line_edit = QtGui.QLineEdit(self.widget)
        self.eye_side_2_line_edit.setObjectName("eye_side_2_line_edit")
        self.eye_side_2_line_edit.setValidator(self.validator)
        self.eye_side_2_line_edit.setText(str(16))
        self.eye_side_2_line_edit.hide()
        self.leg_grid_layout.addWidget(self.eye_side_2_line_edit, 6, 1, 1, 3)

        # NOSE LABEL
        self.nose_label = QtGui.QLabel(self.widget)
        self.nose_label.setObjectName("nose_label")
        self.nose_label.setText('Nose : ')
        self.leg_grid_layout.addWidget(self.nose_label, 7, 0, 1, 1)

        # NOSE CHECKBOX
        self.nose_check_box = QtGui.QCheckBox(self.widget)
        self.nose_check_box.setObjectName("nose_check_box")
        self.nose_check_box.setText('Nose')
        self.leg_grid_layout.addWidget(self.nose_check_box, 8, 0, 1, 1)

        # NOSE SIDE CHECKBOX
        self.nose_side_check_box = QtGui.QCheckBox(self.widget)
        self.nose_side_check_box.setObjectName("nose_side_check_box")
        self.nose_side_check_box.setText('Nose Side')
        self.nose_side_check_box.stateChanged.connect(partial(self.face_checkbox_change, 3))
        self.leg_grid_layout.addWidget(self.nose_side_check_box, 8, 1, 1, 1)

        # NOSE SIDE LABEL
        self.nose_side_label = QtGui.QLabel(self.widget)
        self.nose_side_label.setObjectName("nose_side_label")
        self.nose_side_label.setText('Nose Side : ')
        self.nose_side_label.hide()
        self.leg_grid_layout.addWidget(self.nose_side_label, 9, 0, 1, 1)

        # EYE SIDE LINE EIDT
        self.nose_side_line_edit = QtGui.QLineEdit(self.widget)
        self.nose_side_line_edit.setObjectName("nose_side_line_edit")
        self.nose_side_line_edit.setValidator(self.validator)
        self.nose_side_line_edit.setText(str(3))
        self.nose_side_line_edit.hide()
        self.leg_grid_layout.addWidget(self.nose_side_line_edit, 9, 1, 1, 3)

        # COMMON LABEL
        self.common_label = QtGui.QLabel(self.widget)
        self.common_label.setObjectName("common_label")
        self.common_label.setText('Common : ')
        self.leg_grid_layout.addWidget(self.common_label, 10, 0, 1, 1)

        # FOR HEAD CHCKBOX
        self.for_head_check_box = QtGui.QCheckBox(self.widget)
        self.for_head_check_box.setObjectName("for_head_check_box")
        self.for_head_check_box.setText('ForHead')
        self.for_head_check_box.stateChanged.connect(partial(self.face_checkbox_change, 4))
        self.leg_grid_layout.addWidget(self.for_head_check_box, 11, 0, 1, 1)

        # NOSE SIDE LABEL
        self.for_head_label = QtGui.QLabel(self.widget)
        self.for_head_label.setObjectName("for_head_label")
        self.for_head_label.setText('ForHead : ')
        self.for_head_label.hide()
        self.leg_grid_layout.addWidget(self.for_head_label, 12, 0, 1, 1)

        # EYE SIDE LINE EIDT
        self.for_head_line_edit = QtGui.QLineEdit(self.widget)
        self.for_head_line_edit.setObjectName("for_head_line_edit")
        self.for_head_line_edit.setValidator(self.validator)
        self.for_head_line_edit.setText(str(9))
        self.for_head_line_edit.hide()
        self.leg_grid_layout.addWidget(self.for_head_line_edit, 12, 1, 1, 3)

        # MOUTH CHECKBOX
        self.mouth_check_box = QtGui.QCheckBox(self.widget)
        self.mouth_check_box.setObjectName("mouth_check_box")
        self.mouth_check_box.setText('Mouth')
        self.mouth_check_box.stateChanged.connect(partial(self.face_checkbox_change, 5))
        self.leg_grid_layout.addWidget(self.mouth_check_box, 13, 0, 1, 1)

        # MOUTH SIDE CHECKBOX
        self.mouth_side_check_box = QtGui.QCheckBox(self.widget)
        self.mouth_side_check_box.setObjectName("mouth_side_check_box")
        self.mouth_side_check_box.setText('Mouth Side')
        self.mouth_side_check_box.stateChanged.connect(partial(self.face_checkbox_change, 6))
        self.leg_grid_layout.addWidget(self.mouth_side_check_box, 13, 1, 1, 1)

        # MOUTH SIDE 2 CHECKBOX
        self.mouth_side_2_check_box = QtGui.QCheckBox(self.widget)
        self.mouth_side_2_check_box.setObjectName("mouth_side_2_check_box")
        self.mouth_side_2_check_box.setText('Mouth Side 2')
        self.mouth_side_2_check_box.stateChanged.connect(partial(self.face_checkbox_change, 7))
        self.leg_grid_layout.addWidget(self.mouth_side_2_check_box, 13, 2, 1, 1)

        # MOUTH LABEL
        self.mouth_label = QtGui.QLabel(self.widget)
        self.mouth_label.setObjectName("no_eye_eye_label")
        self.mouth_label.setText('Mouth : ')
        self.mouth_label.hide()
        self.leg_grid_layout.addWidget(self.mouth_label, 14, 0, 1, 1)

        # MOUTH LINE EIDT
        self.mouth_line_edit = QtGui.QLineEdit(self.widget)
        self.mouth_line_edit.setObjectName("mouth_line_edit")
        self.validator = QtGui.QDoubleValidator()
        self.mouth_line_edit.setValidator(self.validator)
        self.mouth_line_edit.setText(str(22))
        self.mouth_line_edit.hide()
        self.leg_grid_layout.addWidget(self.mouth_line_edit, 14, 1, 1, 3)

        # MOUTH SIDE LABEL
        self.mouth_side_label = QtGui.QLabel(self.widget)
        self.mouth_side_label.setObjectName("mouth_side_label")
        self.mouth_side_label.setText('Mouth Side : ')
        self.mouth_side_label.hide()
        self.leg_grid_layout.addWidget(self.mouth_side_label, 15, 0, 1, 1)

        # MOUTH SIDE LINE EIDT
        self.mouth_side_line_edit = QtGui.QLineEdit(self.widget)
        self.mouth_side_line_edit.setObjectName("mouth_side_line_edit")
        self.mouth_side_line_edit.setValidator(self.validator)
        self.mouth_side_line_edit.setText(str(20))
        self.mouth_side_line_edit.hide()
        self.leg_grid_layout.addWidget(self.mouth_side_line_edit, 15, 1, 1, 3)

        # MOUTH SIDE 2 LABEL
        self.mouth_side_2_label = QtGui.QLabel(self.widget)
        self.mouth_side_2_label.setObjectName("mouth_side_2_label")
        self.mouth_side_2_label.setText('Mouth Side 2 : ')
        self.mouth_side_2_label.hide()
        self.leg_grid_layout.addWidget(self.mouth_side_2_label, 16, 0, 1, 1)

        # MOUTH SIDE 2 LINE EIDT
        self.mouth_side_2_line_edit = QtGui.QLineEdit(self.widget)
        self.mouth_side_2_line_edit.setObjectName("mouth_side_2_line_edit")
        self.mouth_side_2_line_edit.setValidator(self.validator)
        self.mouth_side_2_line_edit.setText(str(5))
        self.mouth_side_2_line_edit.hide()
        self.leg_grid_layout.addWidget(self.mouth_side_2_line_edit, 16, 1, 1, 3)

        # FACE CENTER CHECKBOX
        self.face_center_check_box = QtGui.QCheckBox(self.widget)
        self.face_center_check_box.setObjectName("face_center_check_box")
        self.face_center_check_box.setText('Face Center')
        self.face_center_check_box.stateChanged.connect(partial(self.face_checkbox_change, 8))
        self.leg_grid_layout.addWidget(self.face_center_check_box, 17, 0, 1, 1)

        # FACE CENTER LABEL
        self.face_center_label = QtGui.QLabel(self.widget)
        self.face_center_label.setObjectName("face_center_label")
        self.face_center_label.setText('Face Center : ')
        self.face_center_label.hide()
        self.leg_grid_layout.addWidget(self.face_center_label, 18, 0, 1, 1)

        # FACE CENTER LINE EIDT
        self.face_center_line_edit = QtGui.QLineEdit(self.widget)
        self.face_center_line_edit.setObjectName("face_center_line_edit")
        self.face_center_line_edit.setValidator(self.validator)
        self.face_center_line_edit.setText(str(6))
        self.face_center_line_edit.hide()
        self.leg_grid_layout.addWidget(self.face_center_line_edit, 18, 1, 1, 3)

        # FACE BUTTON
        self.face_create_button = QtGui.QPushButton(self.widget)
        self.face_create_button.setObjectName("face_create_button")
        self.face_create_button.setText('Create Face')
        self.face_create_button.clicked.connect(self.new_face_def)
        self.leg_grid_layout.addWidget(self.face_create_button, 19, 0, 1, 4)

        self.spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.leg_grid_layout.addItem(self.spacerItem, 20, 0, 1, 1)
        self.layout.addLayout(self.leg_grid_layout)

    def mirror_status_def(self):
        # get the statu
        if self.mirror_check_box.isChecked():
            self.left_check_box.setChecked(True)
            self.right_check_box.setChecked(True)
        else:
            self.left_check_box.setChecked(False)
            self.right_check_box.setChecked(False)

    def new_face_def(self):
        # get the value
        # Template_Face_Tem_1_Main_Ctrl
        # Chck if left val
        self.prefix_name = 'Template'

        # get the new ui
        self.get_new_ui_def()

        if cmds.objExists("*_Face_Tem_*_Main_Grp"):
            cmds.select("*_Face_Tem_*_Main_Grp")
            sel_main_grp = cmds.ls(sl=True)
            len_sel_main_grp = len(sel_main_grp)
            self.val = len_sel_main_grp + 1
        else:
            self.val = 1

        self.crv_list = []
        self.loc_list = []
        self.sphere_list = []
        self.clu_list = []
        self.loc_center_list = []
        self.loc_grp_list = []
        self.mirror_loc = []

        if self.left_check_box_query == True:
            self.face_side = 'L'

            # EYE
            if self.eye_check_box_query == True:
                self.eye_def()

            # EYE SIDE
            if self.eye_side_check_box_query == True:
                self.eye_side_def()

            # EYE SIDE 2
            if self.eye_side_2_check_box_query == True:
                self.eye_side_2_def()

            # NOSE
            if self.nose_check_box_query == True:
                self.nose_def()

            # NOSE SIDE
            if self.nose_side_check_box_query == True:
                self.nose_side_def()

            # MOUTH SIDE
            if self.mouth_side_2_check_box_query == True:
                self.mouth_side_2_def()

        if self.right_check_box_query == True:

            self.face_side = 'R'

            # EYE
            if self.eye_check_box_query == True:
                self.eye_def()

            # EYE SIDE
            if self.eye_side_check_box_query == True:
                self.eye_side_def()

            # EYE SIDE 2
            if self.eye_side_2_check_box_query == True:
                self.eye_side_2_def()

            # NOSE
            if self.nose_check_box_query == True:
                self.nose_def()

            # NOSE SIDE
            if self.nose_side_check_box_query == True:
                self.nose_side_def()

            # MOUTH SIDE
            if self.mouth_side_2_check_box_query == True:
                self.mouth_side_2_def()

            if self.mirror_check_box_query == True:
                self.mirror_value()

        # FOR HEAD
        if self.for_head_check_box_query == True:
            self.for_head_def()

        # MOUTH
        if self.mouth_check_box_query == True:
            self.mouth_def()

        # MOUTH SIDE
        if self.mouth_side_check_box_query == True:
            self.mouth_side_def()

        # FACE CENTER
        if self.face_center_check_box_query == True:
            self.face_center_def()

        self.final_group()

        # create a center controller
        # circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0.01 -s 8 -ch 0;
        self.main_ctrl_name = self.prefix_name + '_Main_Tem_' + str(self.val) + '_Ctrl'
        cmds.circle(nr=(0, 1, 0), c=(0, 0, 0), sw=360, r=10, n=self.main_ctrl_name)
        # move -rpr 4.938595 2.441233 8.891526 Template_R_Eye_Tem_2_Loc_Center_Grp.scalePivot Template_R_Eye_Tem_2_Loc_Center_Grp.rotatePivot ;
        cmds.select(self.loc_center_group_name)
        cmds.move(0, 0, 0,
                  (self.loc_center_group_name + '.scalePivot'),
                  (self.loc_center_group_name + '.rotatePivot'))
        cmds.select(self.loc_main_group_name)
        cmds.move(0, 0, 0,
                  (self.loc_main_group_name + '.scalePivot'),
                  (self.loc_main_group_name + '.rotatePivot'))

        cmds.parentConstraint((self.main_ctrl_name), (self.loc_center_group_name), mo=True)
        cmds.parentConstraint((self.main_ctrl_name), (self.loc_main_group_name), mo=True)
        cmds.scaleConstraint((self.main_ctrl_name), (self.loc_center_group_name), mo=True)
        cmds.scaleConstraint((self.main_ctrl_name), (self.loc_main_group_name), mo=True)

        # Template_Face_Tem_2_Main_Grp
        main_grp = self.prefix_name + '_Face_Tem_' + str(self.val) + '_Main_Grp'
        cmds.select(self.main_ctrl_name,
                    main_grp)
        cmds.parent()

    def eye_def(self):
        if self.face_side == 'L':
            self.loc_pos = {}
            self.loc_pos[0] = [2.4237557873701157, 10.26417024199597, 8.436801198766686]
            self.loc_pos[1] = [2.63367571687451, 11.517145705863157, 8.700258497045494]
            self.loc_pos[2] = [3.527619980332762, 12.775843215628782, 8.935631040380455]
            self.loc_pos[3] = [4.664785288331419, 13.370768142386595, 8.932724241064049]
            self.loc_pos[4] = [5.9194406495069565, 13.598932815238157, 8.672170881078697]
            self.loc_pos[5] = [7.207328222749144, 13.431269241019407, 8.13992238406942]
            self.loc_pos[6] = [8.135233782288939, 12.651651931449095, 7.220290426061608]
            self.loc_pos[7] = [8.642078302857787, 11.654337478324095, 6.522227052495934]
            self.loc_pos[8] = [8.497332476136595, 11.22706086699597, 6.779950860784508]
            self.loc_pos[9] = [7.676333330628783, 10.540567947074095, 7.670774701879479]
            self.loc_pos[10] = [6.552756689546019, 9.979609084769407, 8.296170476720787]
            self.loc_pos[11] = [5.208461187837035, 9.702570510550657, 8.649672750280358]
            self.loc_pos[12] = [4.005923651215941, 9.718256545706907, 8.69976067905233]
            self.loc_pos[13] = [3.100969694611937, 9.75104768340222, 8.589694265172936]
            self.eye_ball_pos = [6, 11, 4]
        else:
            self.loc_pos = {}
            self.loc_pos[0] = [-2.4237557873701157, 10.26417024199597, 8.436801198766686]
            self.loc_pos[1] = [-2.63367571687451, 11.517145705863157, 8.700258497045494]
            self.loc_pos[2] = [-3.527619980332762, 12.775843215628782, 8.935631040380455]
            self.loc_pos[3] = [-4.664785288331419, 13.370768142386595, 8.932724241064049]
            self.loc_pos[4] = [-5.9194406495069565, 13.598932815238157, 8.672170881078697]
            self.loc_pos[5] = [-7.207328222749144, 13.431269241019407, 8.13992238406942]
            self.loc_pos[6] = [-8.135233782288939, 12.651651931449095, 7.220290426061608]
            self.loc_pos[7] = [-8.642078302857787, 11.654337478324095, 6.522227052495934]
            self.loc_pos[8] = [-8.497332476136595, 11.22706086699597, 6.779950860784508]
            self.loc_pos[9] = [-7.676333330628783, 10.540567947074095, 7.670774701879479]
            self.loc_pos[10] = [-6.552756689546019, 9.979609084769407, 8.296170476720787]
            self.loc_pos[11] = [-5.208461187837035, 9.702570510550657, 8.649672750280358]
            self.loc_pos[12] = [-4.005923651215941, 9.718256545706907, 8.69976067905233]
            self.loc_pos[13] = [-3.100969694611937, 9.75104768340222, 8.589694265172936]
            self.eye_ball_pos = [-6, 11, 4]

        # get the difault pos
        # create basic loc position
        self.eye_curve_name = self.prefix_name + '_' + self.face_side + '_Eye_Tem_' + str(self.val) + '_Crv'
        self.eye_curve_shape_name = self.eye_curve_name + 'Shape'
        self.crv_list.append(self.eye_curve_name)
        cmds.curve(n=self.eye_curve_name, d=0, p=[(self.loc_pos[0][0], self.loc_pos[0][1], self.loc_pos[0][2]),
                                                  (self.loc_pos[1][0], self.loc_pos[1][1], self.loc_pos[1][2]),
                                                  (self.loc_pos[2][0], self.loc_pos[2][1], self.loc_pos[2][2]),
                                                  (self.loc_pos[3][0], self.loc_pos[3][1], self.loc_pos[3][2]),
                                                  (self.loc_pos[4][0], self.loc_pos[4][1], self.loc_pos[4][2]),
                                                  (self.loc_pos[5][0], self.loc_pos[5][1], self.loc_pos[5][2]),
                                                  (self.loc_pos[6][0], self.loc_pos[6][1], self.loc_pos[6][2]),
                                                  (self.loc_pos[7][0], self.loc_pos[7][1], self.loc_pos[7][2]),
                                                  (self.loc_pos[8][0], self.loc_pos[8][1], self.loc_pos[8][2]),
                                                  (self.loc_pos[9][0], self.loc_pos[9][1], self.loc_pos[9][2]),
                                                  (self.loc_pos[10][0], self.loc_pos[10][1], self.loc_pos[10][2]),
                                                  (self.loc_pos[11][0], self.loc_pos[11][1], self.loc_pos[11][2]),
                                                  (self.loc_pos[12][0], self.loc_pos[12][1], self.loc_pos[12][2]),
                                                  (self.loc_pos[13][0], self.loc_pos[13][1], self.loc_pos[13][2]),
                                                  (self.loc_pos[0][0], self.loc_pos[0][1], self.loc_pos[0][2])],
                   k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
        cmds.CenterPivot()
        # get th epos
        crv_pos = cmds.xform(self.eye_curve_name, q=1, ws=1, rp=1)
        shape_name = cmds.listRelatives(self.eye_curve_name, s=True)[0]
        cmds.rename(shape_name, self.eye_curve_shape_name)
        # rebuild the curve
        self.make_refernce(self.eye_curve_name)
        '''
        cmds.rebuildCurve( self.eye_curve_name,ch=0,
                           rpo=1,rt=0,end=1,kr=0,kcp=0,kep=1,kt=0,d=1,tol=0.01, s=self.no_eye_line_edit_query )

        '''
        self.center_loc_name = self.prefix_name + '_' + self.face_side + '_Eye_Tem_' + str(self.val) + "_Main_LOC"
        cmds.spaceLocator(n=self.center_loc_name, p=(crv_pos[0],
                                                     crv_pos[1],
                                                     crv_pos[2]))
        cmds.CenterPivot()
        self.loc_center_list.append(self.center_loc_name)

        self.center_loc_ball_name = self.prefix_name + '_' + self.face_side + '_Eye_Ball_Tem_' + str(
            self.val) + "_Main_LOC"
        cmds.spaceLocator(n=self.center_loc_ball_name, p=(self.eye_ball_pos[0],
                                                          self.eye_ball_pos[1],
                                                          self.eye_ball_pos[2]))
        cmds.select(self.center_loc_ball_name)
        cmds.CenterPivot()
        self.loc_center_list.append(self.center_loc_ball_name)

        # eye Close curve
        if self.face_side == 'L':
            self.eye_upper_curve_smooth_name = self.prefix_name + '_' + self.face_side + '_Eye_Tem_' + str(
                self.val) + '_Upper_Close_Crv'
            cmds.curve(n=self.eye_upper_curve_smooth_name, d=2, p=[(2.423756, 10.264171, 8.436801),
                                                                   (3.714209, 10.334795, 9.783671),
                                                                   (6.266183, 11.042989, 9.271085),
                                                                   (7.980102, 11.258657, 8.188),
                                                                   (8.642078, 11.654338, 6.522227)],
                       k=[0, 0, 1, 2, 3, 3])
            self.crv_list.append(self.eye_upper_curve_smooth_name)

            self.eye_lower_curve_smooth_name = self.prefix_name + '_' + self.face_side + '_Eye_Tem_' + str(
                self.val) + '_Lower_Close_Crv'
            cmds.curve(n=self.eye_lower_curve_smooth_name, d=2, p=[(2.423756, 10.264171, 8.436801),
                                                                   (3.714209, 9.985803, 9.366231),
                                                                   (6.266182, 10.435225, 9.027925),
                                                                   (7.980102, 10.965312, 7.509478),
                                                                   (8.642078, 11.654338, 6.522227)],
                       k=[0, 0, 1, 2, 3, 3])
            self.crv_list.append(self.eye_lower_curve_smooth_name)
            self.create_loc_curve('Eye')

        if self.face_side == 'R':
            self.eye_upper_curve_smooth_name = self.prefix_name + '_' + self.face_side + '_Eye_Tem_' + str(
                self.val) + '_Upper_Close_Crv'
            cmds.curve(n=self.eye_upper_curve_smooth_name, d=2, p=[(-2.423756, 10.264171, 8.436801),
                                                                   (-3.714209, 10.334795, 9.783671),
                                                                   (-6.266183, 11.042989, 9.271085),
                                                                   (-7.980102, 11.258657, 8.188),
                                                                   (-8.642078, 11.654338, 6.522227)],
                       k=[0, 0, 1, 2, 3, 3])
            self.crv_list.append(self.eye_upper_curve_smooth_name)

            self.eye_lower_curve_smooth_name = self.prefix_name + '_' + self.face_side + '_Eye_Tem_' + str(
                self.val) + '_Lower_Close_Crv'
            cmds.curve(n=self.eye_lower_curve_smooth_name, d=2, p=[(-2.423756, 10.264171, 8.436801),
                                                                   (-3.714209, 9.985803, 9.366231),
                                                                   (-6.266182, 10.435225, 9.027925),
                                                                   (-7.980102, 10.965312, 7.509478),
                                                                   (-8.642078, 11.654338, 6.522227)],
                       k=[0, 0, 1, 2, 3, 3])
            self.crv_list.append(self.eye_lower_curve_smooth_name)
            self.create_loc_curve('Eye')

    def eye_side_def(self):
        if self.face_side == 'L':
            self.loc_pos = {}
            self.loc_pos[0] = [2.4820000000000007, 9.705000000000013, 8.919999999999998]
            self.loc_pos[1] = [2.1750000000000007, 10.483000000000004, 8.844]
            self.loc_pos[2] = [2.2770000000000006, 11.72399999999999, 9.036999999999999]
            self.loc_pos[3] = [3.1520000000000006, 13.355999999999995, 9.509999999999998]
            self.loc_pos[4] = [5.545000000000001, 14.289000000000016, 9.427]
            self.loc_pos[5] = [7.525, 14.094999999999999, 8.443999999999999]
            self.loc_pos[6] = [8.693000000000001, 13.257000000000005, 7.167999999999999]
            self.loc_pos[7] = [8.977, 11.698000000000008, 6.193999999999999]
            self.loc_pos[8] = [8.533000000000001, 10.425000000000011, 7.1019999999999985]
            self.loc_pos[9] = [7.260000000000001, 9.533000000000015, 8.299999999999999]
            self.loc_pos[10] = [5.146000000000001, 9.230999999999995, 8.957999999999998]
            self.loc_pos[11] = [3.4030000000000005, 9.420999999999992, 8.940999999999999]
        else:
            self.loc_pos = {}
            self.loc_pos[0] = [-2.4820000000000007, 9.705000000000013, 8.919999999999998]
            self.loc_pos[1] = [-2.1750000000000007, 10.483000000000004, 8.844]
            self.loc_pos[2] = [-2.2770000000000006, 11.72399999999999, 9.036999999999999]
            self.loc_pos[3] = [-3.1520000000000006, 13.355999999999995, 9.509999999999998]
            self.loc_pos[4] = [-5.545000000000001, 14.289000000000016, 9.427]
            self.loc_pos[5] = [-7.525, 14.094999999999999, 8.443999999999999]
            self.loc_pos[6] = [-8.693000000000001, 13.257000000000005, 7.167999999999999]
            self.loc_pos[7] = [-8.977, 11.698000000000008, 6.193999999999999]
            self.loc_pos[8] = [-8.533000000000001, 10.425000000000011, 7.1019999999999985]
            self.loc_pos[9] = [-7.260000000000001, 9.533000000000015, 8.299999999999999]
            self.loc_pos[10] = [-5.146000000000001, 9.230999999999995, 8.957999999999998]
            self.loc_pos[11] = [-3.4030000000000005, 9.420999999999992, 8.940999999999999]

        # get the difault pos
        # create basic loc position
        self.eye_curve_name = self.prefix_name + '_' + self.face_side + '_Eye_Side_Tem_' + str(self.val) + '_Crv'
        self.eye_curve_shape_name = self.eye_curve_name + 'Shape'
        self.crv_list.append(self.eye_curve_name)
        cmds.curve(n=self.eye_curve_name, d=0, p=[(self.loc_pos[0][0], self.loc_pos[0][1], self.loc_pos[0][2]),
                                                  (self.loc_pos[1][0], self.loc_pos[1][1], self.loc_pos[1][2]),
                                                  (self.loc_pos[2][0], self.loc_pos[2][1], self.loc_pos[2][2]),
                                                  (self.loc_pos[3][0], self.loc_pos[3][1], self.loc_pos[3][2]),
                                                  (self.loc_pos[4][0], self.loc_pos[4][1], self.loc_pos[4][2]),
                                                  (self.loc_pos[5][0], self.loc_pos[5][1], self.loc_pos[5][2]),
                                                  (self.loc_pos[6][0], self.loc_pos[6][1], self.loc_pos[6][2]),
                                                  (self.loc_pos[7][0], self.loc_pos[7][1], self.loc_pos[7][2]),
                                                  (self.loc_pos[8][0], self.loc_pos[8][1], self.loc_pos[8][2]),
                                                  (self.loc_pos[9][0], self.loc_pos[9][1], self.loc_pos[9][2]),
                                                  (self.loc_pos[10][0], self.loc_pos[10][1], self.loc_pos[10][2]),
                                                  (self.loc_pos[11][0], self.loc_pos[11][1], self.loc_pos[11][2]),
                                                  (self.loc_pos[0][0], self.loc_pos[0][1], self.loc_pos[0][2])],
                   k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        cmds.CenterPivot()
        # get th epos
        crv_pos = cmds.xform(self.eye_curve_name, q=1, ws=1, rp=1)
        shape_name = cmds.listRelatives(self.eye_curve_name, s=True)[0]
        cmds.rename(shape_name, self.eye_curve_shape_name)
        # rebuild the curve
        self.make_refernce(self.eye_curve_name)
        '''
        cmds.rebuildCurve( self.eye_curve_name,ch=0,
                           rpo=1,rt=0,end=1,kr=0,kcp=0,kep=1,kt=0,d=1,tol=0.01, s=self.eye_side_line_edit_query )

        '''
        self.center_loc_name = self.prefix_name + '_' + self.face_side + '_Eye_Side_Tem_' + str(self.val) + "_Main_LOC"
        cmds.spaceLocator(n=self.center_loc_name, p=(crv_pos[0],
                                                     crv_pos[1],
                                                     crv_pos[2]))
        cmds.CenterPivot()
        self.loc_center_list.append(self.center_loc_name)

        self.create_loc_curve('Eye_Side')

    def eye_side_2_def(self):
        if self.face_side == 'L':
            self.loc_pos = {}
            self.loc_pos[0] = [2.5640000000000005, 15.454000000000008, 10.514]
            self.loc_pos[1] = [4.631, 15.635999999999996, 10.152]
            self.loc_pos[2] = [6.522, 15.700999999999993, 9.415999999999999]
            self.loc_pos[3] = [8.194000000000003, 15.495000000000005, 8.210999999999999]
            self.loc_pos[4] = [9.272, 14.893, 6.845999999999999]
            self.loc_pos[5] = [9.732000000000001, 13.947000000000003, 5.656999999999999]
            self.loc_pos[6] = [9.937000000000001, 12.010999999999996, 4.636999999999999]
            self.loc_pos[7] = [9.441, 10.486999999999995, 6.039999999999999]
            self.loc_pos[8] = [9.017000000000001, 9.141999999999996, 7.199999999999998]
            self.loc_pos[9] = [7.777000000000001, 8.490000000000009, 8.508]
            self.loc_pos[10] = [5.925000000000001, 8.344999999999999, 9.421]
            self.loc_pos[11] = [4.1450000000000005, 8.560000000000002, 9.691999999999998]
            self.loc_pos[12] = [2.468000000000001, 8.99600000000001, 9.838]
            self.loc_pos[13] = [1.3850000000000007, 10.289999999999992, 9.652999999999999]
            self.loc_pos[14] = [1.4490000000000007, 12.238, 9.832999999999998]
            self.loc_pos[15] = [2.1160000000000005, 14.439999999999998, 10.376999999999999]

        else:
            self.loc_pos = {}
            self.loc_pos[0] = [-2.5640000000000005, 15.454000000000008, 10.514]
            self.loc_pos[1] = [-4.631, 15.635999999999996, 10.152]
            self.loc_pos[2] = [-6.522, 15.700999999999993, 9.415999999999999]
            self.loc_pos[3] = [-8.194000000000003, 15.495000000000005, 8.210999999999999]
            self.loc_pos[4] = [-9.272, 14.893, 6.845999999999999]
            self.loc_pos[5] = [-9.732000000000001, 13.947000000000003, 5.656999999999999]
            self.loc_pos[6] = [-9.937000000000001, 12.010999999999996, 4.636999999999999]
            self.loc_pos[7] = [-9.441, 10.486999999999995, 6.039999999999999]
            self.loc_pos[8] = [-9.017000000000001, 9.141999999999996, 7.199999999999998]
            self.loc_pos[9] = [-7.777000000000001, 8.490000000000009, 8.508]
            self.loc_pos[10] = [-5.925000000000001, 8.344999999999999, 9.421]
            self.loc_pos[11] = [-4.1450000000000005, 8.560000000000002, 9.691999999999998]
            self.loc_pos[12] = [-2.468000000000001, 8.99600000000001, 9.838]
            self.loc_pos[13] = [-1.3850000000000007, 10.289999999999992, 9.652999999999999]
            self.loc_pos[14] = [-1.4490000000000007, 12.238, 9.832999999999998]
            self.loc_pos[15] = [-2.1160000000000005, 14.439999999999998, 10.376999999999999]

        # get the difault pos
        # create basic loc position
        self.eye_curve_name = self.prefix_name + '_' + self.face_side + '_Eye_Side_2_Tem_' + str(self.val) + '_Crv'
        self.eye_curve_shape_name = self.eye_curve_name + 'Shape'
        self.crv_list.append(self.eye_curve_name)
        cmds.curve(n=self.eye_curve_name, d=0, p=[(self.loc_pos[0][0], self.loc_pos[0][1], self.loc_pos[0][2]),
                                                  (self.loc_pos[1][0], self.loc_pos[1][1], self.loc_pos[1][2]),
                                                  (self.loc_pos[2][0], self.loc_pos[2][1], self.loc_pos[2][2]),
                                                  (self.loc_pos[3][0], self.loc_pos[3][1], self.loc_pos[3][2]),
                                                  (self.loc_pos[4][0], self.loc_pos[4][1], self.loc_pos[4][2]),
                                                  (self.loc_pos[5][0], self.loc_pos[5][1], self.loc_pos[5][2]),
                                                  (self.loc_pos[6][0], self.loc_pos[6][1], self.loc_pos[6][2]),
                                                  (self.loc_pos[7][0], self.loc_pos[7][1], self.loc_pos[7][2]),
                                                  (self.loc_pos[8][0], self.loc_pos[8][1], self.loc_pos[8][2]),
                                                  (self.loc_pos[9][0], self.loc_pos[9][1], self.loc_pos[9][2]),
                                                  (self.loc_pos[10][0], self.loc_pos[10][1], self.loc_pos[10][2]),
                                                  (self.loc_pos[11][0], self.loc_pos[11][1], self.loc_pos[11][2]),
                                                  (self.loc_pos[12][0], self.loc_pos[12][1], self.loc_pos[12][2]),
                                                  (self.loc_pos[13][0], self.loc_pos[13][1], self.loc_pos[13][2]),
                                                  (self.loc_pos[14][0], self.loc_pos[14][1], self.loc_pos[14][2]),
                                                  (self.loc_pos[15][0], self.loc_pos[15][1], self.loc_pos[15][2]),
                                                  (self.loc_pos[0][0], self.loc_pos[0][1], self.loc_pos[0][2])],
                   k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
        cmds.CenterPivot()
        # get th epos
        crv_pos = cmds.xform(self.eye_curve_name, q=1, ws=1, rp=1)
        shape_name = cmds.listRelatives(self.eye_curve_name, s=True)[0]
        cmds.rename(shape_name, self.eye_curve_shape_name)
        # rebuild the curve
        self.make_refernce(self.eye_curve_name)
        '''
        cmds.rebuildCurve( self.eye_curve_name,ch=0,
                           rpo=1,rt=0,end=1,kr=0,kcp=0,kep=1,kt=0,d=1,tol=0.01, s=self.eye_side_2_line_edit_query)

        '''
        self.center_loc_name = self.prefix_name + '_' + self.face_side + '_Eye_Side_2_Tem_' + str(
            self.val) + "_Main_LOC"
        cmds.spaceLocator(n=self.center_loc_name, p=(crv_pos[0],
                                                     crv_pos[1],
                                                     crv_pos[2]))
        cmds.CenterPivot()
        self.loc_center_list.append(self.center_loc_name)

        self.create_loc_curve('Eye_Side_2')

    def nose_def(self):
        if self.face_side == 'L':
            self.loc_pos = {}
            self.loc_pos[0] = [1.1630000000000007, 6.372000000000014, 12.604]
            self.loc_pos[1] = [1.4740000000000006, 6.39500000000001, 12.229]
            self.loc_pos[2] = [1.1240000000000006, 6.236999999999995, 11.927999999999999]
            self.loc_pos[3] = [0.8120000000000006, 6.213999999999999, 12.303999999999998]
        else:
            self.loc_pos = {}
            self.loc_pos[0] = [-1.1630000000000007, 6.372000000000014, 12.604]
            self.loc_pos[1] = [-1.4740000000000006, 6.39500000000001, 12.229]
            self.loc_pos[2] = [-1.1240000000000006, 6.236999999999995, 11.927999999999999]
            self.loc_pos[3] = [-0.8120000000000006, 6.213999999999999, 12.303999999999998]

        # get the difault pos
        # create basic loc position
        self.eye_curve_name = self.prefix_name + '_' + self.face_side + '_Nose_Tem_' + str(self.val) + '_Crv'
        self.eye_curve_shape_name = self.eye_curve_name + 'Shape'
        self.crv_list.append(self.eye_curve_name)
        cmds.curve(n=self.eye_curve_name, d=0, p=[(self.loc_pos[0][0], self.loc_pos[0][1], self.loc_pos[0][2]),
                                                  (self.loc_pos[1][0], self.loc_pos[1][1], self.loc_pos[1][2]),
                                                  (self.loc_pos[2][0], self.loc_pos[2][1], self.loc_pos[2][2]),
                                                  (self.loc_pos[3][0], self.loc_pos[3][1], self.loc_pos[3][2]),
                                                  (self.loc_pos[0][0], self.loc_pos[0][1], self.loc_pos[0][2])],
                   k=[0, 1, 2, 3, 4])
        cmds.CenterPivot()
        # get th epos
        crv_pos = cmds.xform(self.eye_curve_name, q=1, ws=1, rp=1)
        shape_name = cmds.listRelatives(self.eye_curve_name, s=True)[0]
        cmds.rename(shape_name, self.eye_curve_shape_name)
        # rebuild the curve
        self.make_refernce(self.eye_curve_name)
        cmds.rebuildCurve(self.eye_curve_name, ch=0,
                          rpo=1, rt=0, end=1, kr=0, kcp=0, kep=1, kt=0, d=1, tol=0.01, s=4)

        self.center_loc_name = self.prefix_name + '_' + self.face_side + '_Nose_Tem_' + str(self.val) + "_Main_LOC"
        cmds.spaceLocator(n=self.center_loc_name, p=(crv_pos[0],
                                                     crv_pos[1],
                                                     crv_pos[2]))
        cmds.CenterPivot()
        self.loc_center_list.append(self.center_loc_name)

        self.create_loc_curve('Nose')

    def nose_side_def(self):
        if self.face_side == 'L':
            self.loc_pos = {}
            self.loc_pos[0] = [2.4740000000000006, 7.834000000000003, 10.822999999999999]
            self.loc_pos[1] = [2.650000000000001, 6.653999999999996, 11.245999999999999]
            self.loc_pos[2] = [3.0910000000000006, 5.912000000000006, 11.020999999999999]


        else:
            self.loc_pos = {}
            self.loc_pos[0] = [-2.4740000000000006, 7.834000000000003, 10.822999999999999]
            self.loc_pos[1] = [-2.650000000000001, 6.653999999999996, 11.245999999999999]
            self.loc_pos[2] = [-3.0910000000000006, 5.912000000000006, 11.020999999999999]

        # get the difault pos
        # create basic loc position
        self.eye_curve_name = self.prefix_name + '_' + self.face_side + '_Nose_Side_Tem_' + str(self.val) + '_Crv'
        self.eye_curve_shape_name = self.eye_curve_name + 'Shape'
        self.crv_list.append(self.eye_curve_name)
        cmds.curve(n=self.eye_curve_name, d=0, p=[(self.loc_pos[0][0], self.loc_pos[0][1], self.loc_pos[0][2]),
                                                  (self.loc_pos[1][0], self.loc_pos[1][1], self.loc_pos[1][2]),
                                                  (self.loc_pos[2][0], self.loc_pos[2][1], self.loc_pos[2][2])],
                   k=[0, 1, 2])
        cmds.CenterPivot()
        # get th epos
        crv_pos = cmds.xform(self.eye_curve_name, q=1, ws=1, rp=1)
        shape_name = cmds.listRelatives(self.eye_curve_name, s=True)[0]
        cmds.rename(shape_name, self.eye_curve_shape_name)
        # rebuild the curve
        self.make_refernce(self.eye_curve_name)
        cmds.rebuildCurve(self.eye_curve_name, ch=0,
                          rpo=1, rt=0, end=1, kr=0, kcp=0, kep=1, kt=0, d=1, tol=0.01, s=self.nose_side_line_edit_query)

        self.center_loc_name = self.prefix_name + '_' + self.face_side + '_Nose_Side_Tem_' + str(self.val) + "_Main_LOC"
        cmds.spaceLocator(n=self.center_loc_name, p=(crv_pos[0],
                                                     crv_pos[1],
                                                     crv_pos[2]))
        cmds.CenterPivot()
        self.loc_center_list.append(self.center_loc_name)

        self.new_create_loc_curve('Nose_Side', nose_side=True)

    def for_head_def(self):
        self.loc_pos = {}
        self.loc_pos[0] = [-7.9879999999999995, 17.191000000000003, 6.837999999999999]
        self.loc_pos[1] = [-6.337, 17.927999999999997, 8.245]
        self.loc_pos[2] = [-4.382, 18.232, 9.270999999999999]
        self.loc_pos[3] = [-2.5229999999999992, 18.40100000000001, 9.815999999999999]
        self.loc_pos[4] = [0.22000000000000064, 18.63300000000001, 10.053999999999998]
        self.loc_pos[5] = [2.9630000000000005, 18.40100000000001, 9.815999999999999]
        self.loc_pos[6] = [4.822000000000001, 18.232, 9.270999999999999]
        self.loc_pos[7] = [6.777000000000001, 17.927999999999997, 8.245]
        self.loc_pos[8] = [8.428, 17.191000000000003, 6.837999999999999]

        # get the difault pos
        # create basic loc position
        self.eye_curve_name = self.prefix_name + '_For_Head_Tem_' + str(self.val) + '_Crv'
        self.eye_curve_shape_name = self.eye_curve_name + 'Shape'
        self.crv_list.append(self.eye_curve_name)
        cmds.curve(n=self.eye_curve_name, d=0, p=[(self.loc_pos[0][0], self.loc_pos[0][1], self.loc_pos[0][2]),
                                                  (self.loc_pos[1][0], self.loc_pos[1][1], self.loc_pos[1][2]),
                                                  (self.loc_pos[2][0], self.loc_pos[2][1], self.loc_pos[2][2]),
                                                  (self.loc_pos[3][0], self.loc_pos[3][1], self.loc_pos[3][2]),
                                                  (self.loc_pos[4][0], self.loc_pos[4][1], self.loc_pos[4][2]),
                                                  (self.loc_pos[5][0], self.loc_pos[5][1], self.loc_pos[5][2]),
                                                  (self.loc_pos[6][0], self.loc_pos[6][1], self.loc_pos[6][2]),
                                                  (self.loc_pos[7][0], self.loc_pos[7][1], self.loc_pos[7][2]),
                                                  (self.loc_pos[8][0], self.loc_pos[8][1], self.loc_pos[8][2])],
                   k=[0, 1, 2, 3, 4, 5, 6, 7, 8])
        cmds.CenterPivot()
        # get th epos
        crv_pos = cmds.xform(self.eye_curve_name, q=1, ws=1, rp=1)
        shape_name = cmds.listRelatives(self.eye_curve_name, s=True)[0]
        cmds.rename(shape_name, self.eye_curve_shape_name)
        # rebuild the curve
        self.make_refernce(self.eye_curve_name)
        cmds.rebuildCurve(self.eye_curve_name, ch=0,
                          rpo=1, rt=0, end=1, kr=0, kcp=0, kep=1, kt=0, d=1, tol=0.01, s=self.for_head_line_edit_query)

        self.center_loc_name = self.prefix_name + '_For_Head_Tem_' + str(self.val) + "_Main_LOC"
        cmds.spaceLocator(n=self.center_loc_name, p=(crv_pos[0],
                                                     crv_pos[1],
                                                     crv_pos[2]))
        cmds.CenterPivot()
        self.loc_center_list.append(self.center_loc_name)

        self.new_create_loc_curve('For_Head')

    def mouth_def(self):
        self.loc_pos = {}
        self.loc_pos[0] = [-3.1409999999999996, 3.9739999999999895, 9.94]
        self.loc_pos[1] = [-2.5619999999999994, 3.7560000000000002, 10.259999999999998]
        self.loc_pos[2] = [-2.196999999999999, 3.6680000000000064, 10.616]
        self.loc_pos[3] = [-1.7439999999999993, 3.569999999999993, 10.928999999999998]
        self.loc_pos[4] = [-1.2229999999999994, 3.4569999999999936, 11.213]
        self.loc_pos[5] = [-0.7079999999999994, 3.3729999999999905, 11.386999999999999]
        self.loc_pos[6] = [0.22000000000000064, 3.3189999999999884, 11.499999999999998]
        self.loc_pos[7] = [1.1480000000000006, 3.3729999999999905, 11.386999999999999]
        self.loc_pos[8] = [1.6630000000000007, 3.4569999999999936, 11.213]
        self.loc_pos[9] = [2.184, 3.569999999999993, 10.928999999999998]
        self.loc_pos[10] = [2.6370000000000005, 3.6680000000000064, 10.616]
        self.loc_pos[11] = [3.0020000000000007, 3.7560000000000002, 10.259999999999998]
        self.loc_pos[12] = [3.5280000000000005, 3.9170000000000016, 9.831]
        self.loc_pos[13] = [3.037000000000001, 4.024000000000001, 10.496999999999998]
        self.loc_pos[14] = [2.6770000000000005, 4.1270000000000095, 10.900999999999998]
        self.loc_pos[15] = [2.2440000000000007, 4.244, 11.28]
        self.loc_pos[16] = [1.7230000000000005, 4.347000000000008, 11.624999999999998]
        self.loc_pos[17] = [1.0880000000000005, 4.462999999999994, 11.908]
        self.loc_pos[18] = [0.22000000000000064, 4.304000000000002, 11.959]
        self.loc_pos[19] = [-0.6479999999999994, 4.462999999999994, 11.908]
        self.loc_pos[20] = [-1.2829999999999993, 4.347000000000008, 11.624999999999998]
        self.loc_pos[21] = [-1.8039999999999994, 4.244, 11.28]
        self.loc_pos[22] = [-2.236999999999999, 4.1270000000000095, 10.900999999999998]
        self.loc_pos[23] = [-2.5969999999999995, 4.024000000000001, 10.496999999999998]

        # get the difault pos
        # create basic loc position
        self.eye_curve_name = self.prefix_name + '_Mouth_Tem_' + str(self.val) + '_Crv'
        self.eye_curve_shape_name = self.eye_curve_name + 'Shape'
        self.crv_list.append(self.eye_curve_name)
        cmds.curve(n=self.eye_curve_name, d=0, p=[(self.loc_pos[0][0], self.loc_pos[0][1], self.loc_pos[0][2]),
                                                  (self.loc_pos[1][0], self.loc_pos[1][1], self.loc_pos[1][2]),
                                                  (self.loc_pos[2][0], self.loc_pos[2][1], self.loc_pos[2][2]),
                                                  (self.loc_pos[3][0], self.loc_pos[3][1], self.loc_pos[3][2]),
                                                  (self.loc_pos[4][0], self.loc_pos[4][1], self.loc_pos[4][2]),
                                                  (self.loc_pos[5][0], self.loc_pos[5][1], self.loc_pos[5][2]),
                                                  (self.loc_pos[6][0], self.loc_pos[6][1], self.loc_pos[6][2]),
                                                  (self.loc_pos[7][0], self.loc_pos[7][1], self.loc_pos[7][2]),
                                                  (self.loc_pos[8][0], self.loc_pos[8][1], self.loc_pos[8][2]),
                                                  (self.loc_pos[9][0], self.loc_pos[9][1], self.loc_pos[9][2]),
                                                  (self.loc_pos[10][0], self.loc_pos[10][1], self.loc_pos[10][2]),
                                                  (self.loc_pos[11][0], self.loc_pos[11][1], self.loc_pos[11][2]),
                                                  (self.loc_pos[12][0], self.loc_pos[12][1], self.loc_pos[12][2]),
                                                  (self.loc_pos[13][0], self.loc_pos[13][1], self.loc_pos[13][2]),
                                                  (self.loc_pos[14][0], self.loc_pos[14][1], self.loc_pos[14][2]),
                                                  (self.loc_pos[15][0], self.loc_pos[15][1], self.loc_pos[15][2]),
                                                  (self.loc_pos[16][0], self.loc_pos[16][1], self.loc_pos[16][2]),
                                                  (self.loc_pos[17][0], self.loc_pos[17][1], self.loc_pos[17][2]),
                                                  (self.loc_pos[18][0], self.loc_pos[18][1], self.loc_pos[18][2]),
                                                  (self.loc_pos[19][0], self.loc_pos[19][1], self.loc_pos[19][2]),
                                                  (self.loc_pos[20][0], self.loc_pos[20][1], self.loc_pos[20][2]),
                                                  (self.loc_pos[21][0], self.loc_pos[21][1], self.loc_pos[21][2]),
                                                  (self.loc_pos[22][0], self.loc_pos[22][1], self.loc_pos[22][2]),
                                                  (self.loc_pos[23][0], self.loc_pos[23][1], self.loc_pos[23][2]),
                                                  (self.loc_pos[0][0], self.loc_pos[0][1], self.loc_pos[0][2])],
                   k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])
        cmds.CenterPivot()
        # get th epos
        crv_pos = cmds.xform(self.eye_curve_name, q=1, ws=1, rp=1)
        shape_name = cmds.listRelatives(self.eye_curve_name, s=True)[0]
        cmds.rename(shape_name, self.eye_curve_shape_name)
        # rebuild the curve
        self.make_refernce(self.eye_curve_name)
        cmds.rebuildCurve(self.eye_curve_name, ch=0,
                          rpo=1, rt=0, end=1, kr=0, kcp=0, kep=1, kt=0, d=1, tol=0.01, s=self.mouth_line_edit_query)

        self.center_loc_name = self.prefix_name + '_Mouth_Tem_' + str(self.val) + "_Main_LOC"
        cmds.spaceLocator(n=self.center_loc_name, p=(crv_pos[0],
                                                     crv_pos[1],
                                                     crv_pos[2]))
        cmds.CenterPivot()
        self.loc_center_list.append(self.center_loc_name)

        self.new_create_loc_curve('Mouth')

    def mouth_side_def(self):
        self.loc_pos = {}
        self.loc_pos[0] = [-3.494999999999999, 4.5800000000000125, 10.328999999999999]
        self.loc_pos[1] = [-2.9609999999999994, 4.830999999999989, 10.700999999999999]
        self.loc_pos[2] = [-2.2679999999999993, 5.093999999999994, 11.11]
        self.loc_pos[3] = [-1.3859999999999995, 5.251000000000005, 11.662999999999998]
        self.loc_pos[4] = [-0.5429999999999994, 5.186000000000007, 11.943]
        self.loc_pos[5] = [0.22000000000000064, 5.141999999999996, 11.948999999999998]
        self.loc_pos[6] = [0.9830000000000007, 5.186000000000007, 11.943]
        self.loc_pos[7] = [1.8260000000000007, 5.251000000000005, 11.662999999999998]
        self.loc_pos[8] = [2.7080000000000006, 5.093999999999994, 11.11]
        self.loc_pos[9] = [3.4010000000000007, 4.830999999999989, 10.700999999999999]
        self.loc_pos[10] = [3.9350000000000005, 4.5800000000000125, 10.328999999999999]
        self.loc_pos[11] = [3.8560000000000008, 3.655000000000001, 10.001]
        self.loc_pos[12] = [3.3130000000000006, 2.968999999999994, 10.084]
        self.loc_pos[13] = [2.4140000000000006, 2.469999999999999, 10.438999999999998]
        self.loc_pos[14] = [1.3230000000000006, 2.1049999999999898, 10.783]
        self.loc_pos[15] = [0.22000000000000064, 1.9629999999999939, 10.921999999999999]
        self.loc_pos[16] = [-0.8829999999999993, 2.1049999999999898, 10.783]
        self.loc_pos[17] = [-1.9739999999999993, 2.469999999999999, 10.438999999999998]
        self.loc_pos[18] = [-2.8729999999999993, 2.968999999999994, 10.084]
        self.loc_pos[19] = [-3.4159999999999995, 3.655000000000001, 10.001]

        # get the difault pos
        # create basic loc position
        self.eye_curve_name = self.prefix_name + '_Mouth_Side_Tem_' + str(self.val) + '_Crv'
        self.eye_curve_shape_name = self.eye_curve_name + 'Shape'
        self.crv_list.append(self.eye_curve_name)
        cmds.curve(n=self.eye_curve_name, d=0, p=[(self.loc_pos[0][0], self.loc_pos[0][1], self.loc_pos[0][2]),
                                                  (self.loc_pos[1][0], self.loc_pos[1][1], self.loc_pos[1][2]),
                                                  (self.loc_pos[2][0], self.loc_pos[2][1], self.loc_pos[2][2]),
                                                  (self.loc_pos[3][0], self.loc_pos[3][1], self.loc_pos[3][2]),
                                                  (self.loc_pos[4][0], self.loc_pos[4][1], self.loc_pos[4][2]),
                                                  (self.loc_pos[5][0], self.loc_pos[5][1], self.loc_pos[5][2]),
                                                  (self.loc_pos[6][0], self.loc_pos[6][1], self.loc_pos[6][2]),
                                                  (self.loc_pos[7][0], self.loc_pos[7][1], self.loc_pos[7][2]),
                                                  (self.loc_pos[8][0], self.loc_pos[8][1], self.loc_pos[8][2]),
                                                  (self.loc_pos[9][0], self.loc_pos[9][1], self.loc_pos[9][2]),
                                                  (self.loc_pos[10][0], self.loc_pos[10][1], self.loc_pos[10][2]),
                                                  (self.loc_pos[11][0], self.loc_pos[11][1], self.loc_pos[11][2]),
                                                  (self.loc_pos[12][0], self.loc_pos[12][1], self.loc_pos[12][2]),
                                                  (self.loc_pos[13][0], self.loc_pos[13][1], self.loc_pos[13][2]),
                                                  (self.loc_pos[14][0], self.loc_pos[14][1], self.loc_pos[14][2]),
                                                  (self.loc_pos[15][0], self.loc_pos[15][1], self.loc_pos[15][2]),
                                                  (self.loc_pos[16][0], self.loc_pos[16][1], self.loc_pos[16][2]),
                                                  (self.loc_pos[17][0], self.loc_pos[17][1], self.loc_pos[17][2]),
                                                  (self.loc_pos[18][0], self.loc_pos[18][1], self.loc_pos[18][2]),
                                                  (self.loc_pos[19][0], self.loc_pos[19][1], self.loc_pos[19][2]),
                                                  (self.loc_pos[0][0], self.loc_pos[0][1], self.loc_pos[0][2])],
                   k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
        cmds.CenterPivot()
        # get th epos
        crv_pos = cmds.xform(self.eye_curve_name, q=1, ws=1, rp=1)
        shape_name = cmds.listRelatives(self.eye_curve_name, s=True)[0]
        cmds.rename(shape_name, self.eye_curve_shape_name)
        # rebuild the curve
        self.make_refernce(self.eye_curve_name)
        cmds.rebuildCurve(self.eye_curve_name, ch=0,
                          rpo=1, rt=0, end=1, kr=0, kcp=0, kep=1, kt=0, d=1, tol=0.01,
                          s=self.mouth_side_line_edit_query)

        self.center_loc_name = self.prefix_name + '_Mouth_Side_Tem_' + str(self.val) + "_Main_LOC"
        cmds.spaceLocator(n=self.center_loc_name, p=(crv_pos[0],
                                                     crv_pos[1],
                                                     crv_pos[2]))
        cmds.CenterPivot()
        self.loc_center_list.append(self.center_loc_name)

        self.new_create_loc_curve('Mouth_Side')

    def mouth_side_2_def(self):
        if self.face_side == 'L':
            self.loc_pos = {}
            self.loc_pos[0] = [5.434000000000001, 6.282000000000011, 10.113999999999999]
            self.loc_pos[1] = [5.636000000000001, 4.707999999999998, 9.682999999999998]
            self.loc_pos[2] = [5.2250000000000005, 3.2789999999999964, 9.243999999999998]
            self.loc_pos[3] = [4.290000000000001, 1.9370000000000118, 9.11]
            self.loc_pos[4] = [2.9230000000000005, 0.9029999999999916, 9.701999999999998]

        else:
            self.loc_pos = {}
            self.loc_pos[0] = [-5.434000000000001, 6.282000000000011, 10.113999999999999]
            self.loc_pos[1] = [-5.636000000000001, 4.707999999999998, 9.682999999999998]
            self.loc_pos[2] = [-5.2250000000000005, 3.2789999999999964, 9.243999999999998]
            self.loc_pos[3] = [-4.290000000000001, 1.9370000000000118, 9.11]
            self.loc_pos[4] = [-2.9230000000000005, 0.9029999999999916, 9.701999999999998]

        # get the difault pos
        # create basic loc position
        self.eye_curve_name = self.prefix_name + '_' + self.face_side + '_Mouth_Side_2_Tem_' + str(self.val) + '_Crv'
        self.eye_curve_shape_name = self.eye_curve_name + 'Shape'
        self.crv_list.append(self.eye_curve_name)
        cmds.curve(n=self.eye_curve_name, d=0, p=[(self.loc_pos[0][0], self.loc_pos[0][1], self.loc_pos[0][2]),
                                                  (self.loc_pos[1][0], self.loc_pos[1][1], self.loc_pos[1][2]),
                                                  (self.loc_pos[2][0], self.loc_pos[2][1], self.loc_pos[2][2]),
                                                  (self.loc_pos[3][0], self.loc_pos[3][1], self.loc_pos[3][2]),
                                                  (self.loc_pos[4][0], self.loc_pos[4][1], self.loc_pos[4][2])],
                   k=[0, 1, 2, 3, 4])
        cmds.CenterPivot()
        # get th epos
        crv_pos = cmds.xform(self.eye_curve_name, q=1, ws=1, rp=1)
        shape_name = cmds.listRelatives(self.eye_curve_name, s=True)[0]
        cmds.rename(shape_name, self.eye_curve_shape_name)
        # rebuild the curve
        self.make_refernce(self.eye_curve_name)
        cmds.rebuildCurve(self.eye_curve_name, ch=0,
                          rpo=1, rt=0, end=1, kr=0, kcp=0, kep=1, kt=0, d=1, tol=0.01,
                          s=self.mouth_side_2_line_edit_query)

        self.center_loc_name = self.prefix_name + '_' + self.face_side + '_Mouth_Side_2_Tem_' + str(
            self.val) + "_Main_LOC"
        cmds.spaceLocator(n=self.center_loc_name, p=(crv_pos[0],
                                                     crv_pos[1],
                                                     crv_pos[2]))
        cmds.CenterPivot()
        self.loc_center_list.append(self.center_loc_name)

        self.new_create_loc_curve('Mouth_Side_2', nose_side=True)

    def face_center_def(self):
        self.loc_pos = {}
        self.loc_pos[0] = [0.22000000000000064, 15.786000000000001, 10.627999999999998]
        self.loc_pos[1] = [0.22000000000000064, 13.955999999999989, 10.501999999999999]
        self.loc_pos[2] = [0.22000000000000064, 11.897999999999996, 10.139]
        self.loc_pos[3] = [0.22000000000000064, 10.128000000000014, 10.187]
        self.loc_pos[4] = [0.22000000000000064, 8.359000000000009, 11.553999999999998]
        self.loc_pos[5] = [0.22000000000000064, 7.354000000000013, 13.578]

        # get the difault pos
        # create basic loc position
        self.eye_curve_name = self.prefix_name + '_Face_Center_Tem_' + str(self.val) + '_Crv'
        self.eye_curve_shape_name = self.eye_curve_name + 'Shape'
        self.crv_list.append(self.eye_curve_name)
        cmds.curve(n=self.eye_curve_name, d=0, p=[(self.loc_pos[0][0], self.loc_pos[0][1], self.loc_pos[0][2]),
                                                  (self.loc_pos[1][0], self.loc_pos[1][1], self.loc_pos[1][2]),
                                                  (self.loc_pos[2][0], self.loc_pos[2][1], self.loc_pos[2][2]),
                                                  (self.loc_pos[3][0], self.loc_pos[3][1], self.loc_pos[3][2]),
                                                  (self.loc_pos[4][0], self.loc_pos[4][1], self.loc_pos[4][2])],
                   k=[0, 1, 2, 3, 4])
        cmds.CenterPivot()
        # get th epos
        crv_pos = cmds.xform(self.eye_curve_name, q=1, ws=1, rp=1)
        shape_name = cmds.listRelatives(self.eye_curve_name, s=True)[0]
        cmds.rename(shape_name, self.eye_curve_shape_name)
        # rebuild the curve
        self.make_refernce(self.eye_curve_name)
        cmds.rebuildCurve(self.eye_curve_name, ch=0,
                          rpo=1, rt=0, end=1, kr=0, kcp=0, kep=1, kt=0, d=1, tol=0.01,
                          s=self.face_center_line_edit_query)

        self.center_loc_name = self.prefix_name + '_Face_Center_Tem_' + str(self.val) + "_Main_LOC"
        cmds.spaceLocator(n=self.center_loc_name, p=(crv_pos[0],
                                                     crv_pos[1],
                                                     crv_pos[2]))
        cmds.CenterPivot()
        self.loc_center_list.append(self.center_loc_name)

        self.new_create_loc_curve('Face_Center')

    def create_loc_curve(self, type):
        value = cmds.getAttr(self.eye_curve_name + '.cv[*]')
        main_cv = len(value) - 1.0
        indi_val = 1 / main_cv
        new_val = indi_val
        a = 0
        while a < main_cv:
            common_name = self.prefix_name + '_' + self.face_side + '_' + type + '_' + str(a + 1) + '_Tem_' + str(
                self.val)
            loc_name = common_name + '_LOC'
            poc_name = common_name + '_POC'
            clu_name = common_name + '_Clu'
            if self.face_side == 'R':
                self.mirror_loc.append(loc_name)

            clu_handle_name = clu_name + 'Handle'
            sphere_name = common_name + '_Geo'
            self.loc_list.append(loc_name)
            self.sphere_list.append(sphere_name)
            self.clu_list.append(clu_handle_name)

            cmds.createNode('pointOnCurveInfo', n=poc_name)
            cmds.connectAttr((self.eye_curve_shape_name + '.worldSpace[0]'),
                             (poc_name + '.inputCurve'),
                             f=True)
            cmds.polySphere(r=0.3, sx=6, sy=6, ax=(0, 1, 0), cuv=2, ch=1, n=sphere_name)
            cmds.connectAttr((poc_name + '.position'),
                             (sphere_name + '.translate'),
                             f=True)
            cmds.setAttr((poc_name + ".parameter"), a)

            # select the cv
            if a == 0:
                cmds.select((self.eye_curve_name + '.cv[0]'), (self.eye_curve_name + '.cv[%s]' % main_cv))
                cmds.cluster(n=clu_name)
            else:
                cmds.select(self.eye_curve_name + '.cv[%s]' % a)
                cmds.cluster(n=clu_name)

            # create locator and parent to cluster
            clu_pos = cmds.xform(clu_handle_name, q=1, ws=1, rp=1)
            cmds.spaceLocator(n=loc_name, p=(clu_pos[0],
                                             clu_pos[1],
                                             clu_pos[2]))
            cmds.CenterPivot()
            cmds.parentConstraint(loc_name, clu_handle_name, mo=True)
            cmds.scaleConstraint(loc_name, clu_handle_name, mo=True)
            self.loc_group_name = self.prefix_name + '_' + self.face_side + '_' + type + '_Tem_' + str(
                self.val) + "_Loc_Grp"
            self.helper_class.parent_child_grp(parent=self.loc_group_name,
                                               child=loc_name,
                                               trans_rot_scale=False)
            self.loc_grp_list.append(self.loc_group_name)
            cmds.select(self.loc_group_name)
            cmds.CenterPivot()

            cmds.scaleConstraint(self.center_loc_name, sphere_name, mo=True)
            self.helper_class.transform_rotation_scale_visible(sphere_name, v=False)
            cmds.setAttr((sphere_name + '.overrideEnabled'), 1)
            cmds.setAttr((sphere_name + '.overrideDisplayType'), 2)

            new_val += indi_val

            a += 1

        # create a cluster in crv

        cmds.connectAttr((self.center_loc_name + '.t'), (self.loc_group_name + '.t'))
        cmds.connectAttr((self.center_loc_name + '.r'), (self.loc_group_name + '.r'))
        cmds.connectAttr((self.center_loc_name + '.s'), (self.loc_group_name + '.s'))

    def new_create_loc_curve(self, type, nose_side=False):

        value = cmds.getAttr(self.eye_curve_name + '.cv[*]')
        main_cv = len(value) - 1.0
        indi_val = 0.999999999 / main_cv
        new_val = 0
        a = 0
        while a < len(value):
            if nose_side == True:
                common_name = self.prefix_name + '_' + self.face_side + '_' + type + '_' + str(a + 1) + '_Tem_' + str(
                    self.val)
                self.loc_group_name = self.prefix_name + '_' + self.face_side + '_' + type + '_Tem_' + str(
                    self.val) + "_Loc_Grp"
            else:
                common_name = self.prefix_name + '_' + type + '_' + str(a + 1) + '_Tem_' + str(self.val)
                self.loc_group_name = self.prefix_name + '_' + type + '_Tem_' + str(self.val) + "_Loc_Grp"

            loc_name = common_name + '_LOC'
            poc_name = common_name + '_POC'
            clu_name = common_name + '_Clu'
            clu_handle_name = clu_name + 'Handle'
            sphere_name = common_name + '_Geo'
            self.loc_list.append(loc_name)
            self.sphere_list.append(sphere_name)
            self.clu_list.append(clu_handle_name)

            cmds.createNode('pointOnCurveInfo', n=poc_name)
            cmds.connectAttr((self.eye_curve_shape_name + '.worldSpace[0]'),
                             (poc_name + '.inputCurve'),
                             f=True)
            cmds.polySphere(r=0.3, sx=6, sy=6, ax=(0, 1, 0), cuv=2, ch=1, n=sphere_name)
            cmds.connectAttr((poc_name + '.position'),
                             (sphere_name + '.translate'),
                             f=True)
            cmds.setAttr((poc_name + ".parameter"), new_val)

            # select the cv

            cmds.select(self.eye_curve_name + '.cv[%s]' % a)
            cmds.cluster(n=clu_name)

            # create locator and parent to cluster
            clu_pos = cmds.xform(clu_handle_name, q=1, ws=1, rp=1)
            cmds.spaceLocator(n=loc_name, p=(clu_pos[0],
                                             clu_pos[1],
                                             clu_pos[2]))
            cmds.CenterPivot()
            cmds.parentConstraint(loc_name, clu_handle_name, mo=True)
            cmds.scaleConstraint(loc_name, clu_handle_name, mo=True)

            self.helper_class.parent_child_grp(parent=self.loc_group_name,
                                               child=loc_name,
                                               trans_rot_scale=False)
            self.loc_grp_list.append(self.loc_group_name)
            cmds.select(self.loc_group_name)
            cmds.CenterPivot()

            cmds.scaleConstraint(self.center_loc_name, sphere_name, mo=True)
            self.helper_class.transform_rotation_scale_visible(sphere_name, v=False)
            cmds.setAttr((sphere_name + '.overrideEnabled'), 1)
            cmds.setAttr((sphere_name + '.overrideDisplayType'), 2)

            new_val += indi_val
            a += 1

        cmds.connectAttr((self.center_loc_name + '.t'), (self.loc_group_name + '.t'))
        cmds.connectAttr((self.center_loc_name + '.r'), (self.loc_group_name + '.r'))
        cmds.connectAttr((self.center_loc_name + '.s'), (self.loc_group_name + '.s'))

    def final_group(self):
        self.sphere_group_name = self.prefix_name + '_Eye_Tem_' + str(self.val) + "_Sphere_Grp"
        cmds.select(cl=True)
        for each in self.sphere_list:
            self.helper_class.parent_child_grp(parent=self.sphere_group_name,
                                               child=each)

        self.loc_center_group_name = self.prefix_name + '_Eye_Tem_' + str(self.val) + "_Loc_Center_Grp"
        cmds.select(cl=True)
        for each in self.loc_center_list:
            self.helper_class.parent_child_grp(parent=self.loc_center_group_name,
                                               child=each,
                                               trans_rot_scale=False)

        self.loc_main_group_name = self.prefix_name + '_Eye_Tem_' + str(self.val) + "_Loc_Main_Grp"
        cmds.select(cl=True)
        for each in self.loc_grp_list:
            self.helper_class.parent_child_grp(parent=self.loc_main_group_name,
                                               child=each,
                                               trans_rot_scale=False)

        # self.loc_grp_list

        self.cluster_group_name = self.prefix_name + '_Eye_Tem_' + str(self.val) + "_Cluster_Grp"
        cmds.select(cl=True)
        for each in self.clu_list:
            self.helper_class.parent_child_grp(parent=self.cluster_group_name,
                                               child=each,
                                               vis=True)

        self.curve_group_name = self.prefix_name + '_Eye_Tem_' + str(self.val) + "_Crv_Grp"
        cmds.select(cl=True)
        for each in self.crv_list:
            self.helper_class.parent_child_grp(parent=self.curve_group_name,
                                               child=each)

        grp_list = [self.sphere_group_name, self.cluster_group_name,
                    self.curve_group_name, self.loc_main_group_name,
                    self.loc_center_group_name]
        # "*_Face_Tem_*_Main_Ctrl"
        self.main_grp_name = self.prefix_name + '_Face_Tem_' + str(self.val) + '_Main_Grp'
        for each in grp_list:
            self.helper_class.parent_child_grp(parent=self.main_grp_name,
                                               child=each)

        self.helper_class.parent_child_grp(parent=self.main_grp_name,
                                           child=self.center_loc_name)

        # create a mirror object
        cmds.select(self.main_grp_name)
        self.leg_grp_name = 'Face_Grp'
        self.helper_class.parent_child_grp(parent=self.leg_grp_name,
                                           child=self.main_grp_name)

    def get_new_ui_def(self):
        # MIRROR CHECKBOX
        self.mirror_check_box_query = self.mirror_check_box.isChecked()

        # LEFT LEG CHECKBOX
        self.left_check_box_query = self.left_check_box.isChecked()

        # RIGHT LEG CHECKBOX
        self.right_check_box_query = self.right_check_box.isChecked()

        # EYE CHECKBOX
        self.eye_check_box_query = self.eye_check_box.isChecked()
        if self.eye_check_box_query == True:
            self.no_eye_line_edit_query = int(self.no_eye_line_edit.text())

        # EYE SIDE CHECKBOX
        self.eye_side_check_box_query = self.eye_side_check_box.isChecked()
        if self.eye_side_check_box_query == True:
            self.eye_side_line_edit_query = int(self.eye_side_line_edit.text())

        # EYE SIDE 2 CHECKBOX
        self.eye_side_2_check_box_query = self.eye_side_2_check_box.isChecked()
        if self.eye_side_2_check_box_query == True:
            self.eye_side_2_line_edit_query = int(self.eye_side_2_line_edit.text())

        # NOSE CHECKBOX
        self.nose_check_box_query = self.nose_check_box.isChecked()

        # NOSE SIDE CHECKBOX
        self.nose_side_check_box_query = self.nose_side_check_box.isChecked()
        if self.nose_side_check_box_query == True:
            self.nose_side_line_edit_query = int(self.nose_side_line_edit.text())

        # FOR HEAD CHCKBOX
        self.for_head_check_box_query = self.for_head_check_box.isChecked()
        if self.for_head_check_box_query == True:
            self.for_head_line_edit_query = int(self.for_head_line_edit.text())

        # MOUTH CHECKBOX
        self.mouth_check_box_query = self.mouth_check_box.isChecked()
        if self.mouth_check_box_query == True:
            self.mouth_line_edit_query = int(self.mouth_line_edit.text())

        # MOUTH SIDE CHECKBOX
        self.mouth_side_check_box_query = self.mouth_side_check_box.isChecked()
        if self.mouth_side_check_box_query == True:
            self.mouth_side_line_edit_query = int(self.mouth_side_line_edit.text())

        # MOUTH SIDE 2 CHECKBOX
        self.mouth_side_2_check_box_query = self.mouth_side_2_check_box.isChecked()
        if self.mouth_side_2_check_box_query == True:
            self.mouth_side_2_line_edit_query = int(self.mouth_side_2_line_edit.text())

        # FACE CENTER CHECKBOX
        self.face_center_check_box_query = self.face_center_check_box.isChecked()
        if self.face_center_check_box_query == True:
            self.face_center_line_edit_query = int(self.face_center_line_edit.text())

    def new_clear(self):
        self.helper_class.clearLayout(self.leg_grid_layout)

    def delete_all(self):
        print('delete all the face')

    def face_checkbox_change(self, b, val):
        if b == 0:
            self.eye_check_box_query = self.eye_check_box.isChecked()
            if self.eye_check_box_query == True:
                self.no_eye_label.show()
                self.no_eye_line_edit.show()
            else:
                self.no_eye_label.hide()
                self.no_eye_line_edit.hide()
        if b == 1:
            self.eye_side_check_box_query = self.eye_side_check_box.isChecked()
            if self.eye_side_check_box_query == True:
                self.eye_side_label.show()
                self.eye_side_line_edit.show()
            else:
                self.eye_side_label.hide()
                self.eye_side_line_edit.hide()

        if b == 2:
            self.eye_side_2_check_box_query = self.eye_side_2_check_box.isChecked()
            if self.eye_side_2_check_box_query == True:
                self.eye_side_2_label.show()
                self.eye_side_2_line_edit.show()
            else:
                self.eye_side_2_label.hide()
                self.eye_side_2_line_edit.hide()

        if b == 3:
            self.nose_side_check_box_query = self.nose_side_check_box.isChecked()
            if self.nose_side_check_box_query == True:
                self.nose_side_label.show()
                self.nose_side_line_edit.show()
            else:
                self.nose_side_label.hide()
                self.nose_side_line_edit.hide()

        if b == 4:
            self.for_head_check_box_query = self.for_head_check_box.isChecked()
            if self.for_head_check_box_query == True:
                self.for_head_label.show()
                self.for_head_line_edit.show()
            else:
                self.for_head_label.hide()
                self.for_head_line_edit.hide()

        if b == 5:
            self.mouth_check_box_query = self.mouth_check_box.isChecked()
            if self.mouth_check_box_query == True:
                self.mouth_label.show()
                self.mouth_line_edit.show()
            else:
                self.mouth_label.hide()
                self.mouth_line_edit.hide()

        if b == 6:
            self.mouth_side_check_box_query = self.mouth_side_check_box.isChecked()
            if self.mouth_side_check_box_query == True:
                self.mouth_side_label.show()
                self.mouth_side_line_edit.show()
            else:
                self.mouth_side_label.hide()
                self.mouth_side_line_edit.hide()

        if b == 7:
            self.mouth_side_2_check_box_query = self.mouth_side_2_check_box.isChecked()
            if self.mouth_side_2_check_box_query == True:
                self.mouth_side_2_label.show()
                self.mouth_side_2_line_edit.show()
            else:
                self.mouth_side_2_label.hide()
                self.mouth_side_2_line_edit.hide()

        if b == 8:
            self.face_center_check_box_query = self.face_center_check_box.isChecked()
            if self.face_center_check_box_query == True:
                self.face_center_label.show()
                self.face_center_line_edit.show()
            else:
                self.face_center_label.hide()
                self.face_center_line_edit.hide()

    def mirror_value(self):
        for each in self.mirror_loc:
            self.right_ctrl = each
            self.left_ctrl = each.replace('R', 'L')
            self.helper_class.mirror_grp(self.left_ctrl,
                                         self.right_ctrl)

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

        self.no_face = self.helper_class.get_face()

        a = 0
        value = 0
        grid_value = 0
        self.radio_button = {}
        while a < len(self.no_face):
            self.radio_button[a] = QtGui.QRadioButton(self.head_name_scrollArea_widget_contents)
            self.radio_button[a].setObjectName(self.no_face[a])
            self.radio_button[a].setText(self.no_face[a])
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
        self.face_detail_scroll_area_widget_contents = QtGui.QWidget()
        self.face_detail_scroll_area_widget_contents.setGeometry(QtCore.QRect(0, 0, 469, 275))
        self.face_detail_scroll_area_widget_contents.setObjectName("head_detail_2_scrollArea_widget_contents")
        self.gridLayout_16 = QtGui.QGridLayout(self.face_detail_scroll_area_widget_contents)
        self.gridLayout_16.setObjectName("gridLayout_16")

        self.face_detail_tool_box = QtGui.QToolBox(self.face_detail_scroll_area_widget_contents)
        self.face_detail_tool_box.setObjectName("face_detail_tool_box")

        self.eye_page = QtGui.QWidget()
        self.eye_page.setGeometry(QtCore.QRect(0, 0, 463, 147))
        self.eye_page.setObjectName("eye_page")
        self.eye_page_def()
        self.face_detail_tool_box.addItem(self.eye_page, 'Eye')

        self.nose_page = QtGui.QWidget()
        self.nose_page.setGeometry(QtCore.QRect(0, 0, 463, 147))
        self.nose_page.setObjectName("nose_page")
        self.nose_page_def()
        self.face_detail_tool_box.addItem(self.nose_page, 'Nose')

        self.common_page = QtGui.QWidget()
        self.common_page.setGeometry(QtCore.QRect(0, 0, 463, 147))
        self.common_page.setObjectName("common_page")
        self.common_page_def()
        self.face_detail_tool_box.addItem(self.common_page, 'Common')

        '''
        self.gridLayout_23 = QtGui.QGridLayout()
        self.gridLayout_23.setObjectName("gridLayout_23")

        #MIRROR CHECKBOX
        self.mirror_check_box = QtGui.QCheckBox(self.face_detail_scroll_area_widget_contents)
        self.mirror_check_box.setObjectName("mirror_check_box")
        self.mirror_check_box.setText('Mirror')
        self.mirror_check_box.setChecked(True)
        self.gridLayout_23.addWidget(self.mirror_check_box, 0, 0, 1, 1)

        #LEFT CHECKBOX
        self.left_check_box = QtGui.QCheckBox(self.face_detail_scroll_area_widget_contents)
        self.left_check_box.setObjectName("left_check_box")
        self.left_check_box.setText('Left Face')
        self.left_check_box.setChecked(True)
        self.gridLayout_23.addWidget(self.left_check_box, 1, 0, 1, 1)

        #RIGHT CHECKBOX
        self.right_check_box = QtGui.QCheckBox(self.face_detail_scroll_area_widget_contents)
        self.right_check_box.setObjectName("right_check_box")
        self.right_check_box.setText('Right Face')
        self.right_check_box.setChecked(True)
        self.gridLayout_23.addWidget(self.right_check_box, 1, 1, 1, 1)

        #EYE LABEL
        self.eye_label = QtGui.QLabel(self.face_detail_scroll_area_widget_contents)
        self.eye_label.setObjectName("eye_label")
        self.eye_label.setText('Eye : ')
        self.gridLayout_23.addWidget(self.eye_label, 2, 0, 1, 1)
        #EYE CHECKBOX
        self.eye_check_box = QtGui.QCheckBox(self.face_detail_scroll_area_widget_contents)
        self.eye_check_box.setObjectName("eye_check_box")
        self.eye_check_box.setText('Eye')
        self.eye_check_box.stateChanged.connect(partial(self.face_checkbox_change, 0))
        self.gridLayout_23.addWidget(self.eye_check_box, 3, 0, 1, 1)

        #EYE SIDE CHECKBOX
        self.eye_side_check_box = QtGui.QCheckBox(self.face_detail_scroll_area_widget_contents)
        self.eye_side_check_box.setObjectName("eye_side_check_box")
        self.eye_side_check_box.setText('Eye Side')
        self.eye_side_check_box.stateChanged.connect(partial(self.face_checkbox_change, 1))
        self.gridLayout_23.addWidget(self.eye_side_check_box, 3, 1, 1, 1)

        #EYE SIDE 2 CHECKBOX
        self.eye_side_2_check_box = QtGui.QCheckBox(self.face_detail_scroll_area_widget_contents)
        self.eye_side_2_check_box.setObjectName("eye_side_2_check_box")
        self.eye_side_2_check_box.setText('Eye Side 2')
        self.eye_side_2_check_box.stateChanged.connect(partial(self.face_checkbox_change, 2))
        self.gridLayout_23.addWidget(self.eye_side_2_check_box, 3, 2, 1, 1)

        #EYE LABEL
        self.no_eye_label = QtGui.QLabel(self.face_detail_scroll_area_widget_contents)
        self.no_eye_label.setObjectName("no_eye_eye_label")
        self.no_eye_label.setText('No Eye : ')
        self.no_eye_label.hide()
        self.gridLayout_23.addWidget(self.no_eye_label, 4, 0, 1, 1)

        #EYE LINE EIDT
        self.no_eye_line_edit = QtGui.QLineEdit(self.face_detail_scroll_area_widget_contents)
        self.no_eye_line_edit.setObjectName("no_eye_eye_line_edit")
        self.validator = QtGui.QDoubleValidator()
        self.no_eye_line_edit.setValidator(self.validator)
        self.no_eye_line_edit.setText(str(12))
        self.no_eye_line_edit.hide()
        self.gridLayout_23.addWidget(self.no_eye_line_edit, 4, 1, 1, 3)

        #EYE SIDE LABEL
        self.eye_side_label = QtGui.QLabel(self.face_detail_scroll_area_widget_contents)
        self.eye_side_label.setObjectName("eye_side_label")
        self.eye_side_label.setText('Eye Side : ')
        self.eye_side_label.hide()
        self.gridLayout_23.addWidget(self.eye_side_label, 5, 0, 1, 1)

        #EYE SIDE LINE EIDT
        self.eye_side_line_edit = QtGui.QLineEdit(self.face_detail_scroll_area_widget_contents)
        self.eye_side_line_edit.setObjectName("eye_side_line_edit")
        self.eye_side_line_edit.setValidator(self.validator)
        self.eye_side_line_edit.setText(str(12))
        self.eye_side_line_edit.hide()
        self.gridLayout_23.addWidget(self.eye_side_line_edit, 5, 1, 1, 3)

        #EYE SIDE 2 LABEL
        self.eye_side_2_label = QtGui.QLabel(self.face_detail_scroll_area_widget_contents)
        self.eye_side_2_label.setObjectName("eye_side_2_label")
        self.eye_side_2_label.setText('Eye Side 2 : ')
        self.eye_side_2_label.hide()
        self.gridLayout_23.addWidget(self.eye_side_2_label, 6, 0, 1, 1)

        #EYE SIDE 2 LINE EIDT
        self.eye_side_2_line_edit = QtGui.QLineEdit(self.face_detail_scroll_area_widget_contents)
        self.eye_side_2_line_edit.setObjectName("eye_side_2_line_edit")
        self.eye_side_2_line_edit.setValidator(self.validator)
        self.eye_side_2_line_edit.setText(str(16))
        self.eye_side_2_line_edit.hide()
        self.gridLayout_23.addWidget(self.eye_side_2_line_edit, 6, 1, 1, 3)

        #NOSE LABEL
        self.nose_label = QtGui.QLabel(self.face_detail_scroll_area_widget_contents)
        self.nose_label.setObjectName("nose_label")
        self.nose_label.setText('Nose : ')
        self.gridLayout_23.addWidget(self.nose_label, 7, 0, 1, 1)

        #NOSE CHECKBOX
        self.nose_check_box = QtGui.QCheckBox(self.face_detail_scroll_area_widget_contents)
        self.nose_check_box.setObjectName("nose_check_box")
        self.nose_check_box.setText('Nose')
        self.gridLayout_23.addWidget(self.nose_check_box, 8, 0, 1, 1)

        #NOSE SIDE CHECKBOX
        self.nose_side_check_box = QtGui.QCheckBox(self.face_detail_scroll_area_widget_contents)
        self.nose_side_check_box.setObjectName("nose_side_check_box")
        self.nose_side_check_box.setText('Nose Side')
        self.nose_side_check_box.stateChanged.connect(partial(self.face_checkbox_change, 3))
        self.gridLayout_23.addWidget(self.nose_side_check_box, 8, 1, 1, 1)

        #NOSE SIDE LABEL
        self.nose_side_label = QtGui.QLabel(self.face_detail_scroll_area_widget_contents)
        self.nose_side_label.setObjectName("nose_side_label")
        self.nose_side_label.setText('Nose Side : ')
        self.nose_side_label.hide()
        self.gridLayout_23.addWidget(self.nose_side_label, 9, 0, 1, 1)

        #EYE SIDE LINE EIDT
        self.nose_side_line_edit = QtGui.QLineEdit(self.face_detail_scroll_area_widget_contents)
        self.nose_side_line_edit.setObjectName("nose_side_line_edit")
        self.nose_side_line_edit.setValidator(self.validator)
        self.nose_side_line_edit.setText(str(3))
        self.nose_side_line_edit.hide()
        self.gridLayout_23.addWidget(self.nose_side_line_edit, 9, 1, 1, 3)


        #COMMON LABEL
        self.common_label = QtGui.QLabel(self.face_detail_scroll_area_widget_contents)
        self.common_label.setObjectName("common_label")
        self.common_label.setText('Common : ')
        self.gridLayout_23.addWidget(self.common_label, 10, 0, 1, 1)

        #FOR HEAD CHCKBOX
        self.for_head_check_box = QtGui.QCheckBox(self.face_detail_scroll_area_widget_contents)
        self.for_head_check_box.setObjectName("for_head_check_box")
        self.for_head_check_box.setText('ForHead')
        self.for_head_check_box.stateChanged.connect(partial(self.face_checkbox_change, 4))
        self.gridLayout_23.addWidget(self.for_head_check_box, 11, 0, 1, 1)

        #NOSE SIDE LABEL
        self.for_head_label = QtGui.QLabel(self.face_detail_scroll_area_widget_contents)
        self.for_head_label.setObjectName("for_head_label")
        self.for_head_label.setText('ForHead : ')
        self.for_head_label.hide()
        self.gridLayout_23.addWidget(self.for_head_label, 12, 0, 1, 1)

        #EYE SIDE LINE EIDT
        self.for_head_line_edit = QtGui.QLineEdit(self.face_detail_scroll_area_widget_contents)
        self.for_head_line_edit.setObjectName("for_head_line_edit")
        self.for_head_line_edit.setValidator(self.validator)
        self.for_head_line_edit.setText(str(9))
        self.for_head_line_edit.hide()
        self.gridLayout_23.addWidget(self.for_head_line_edit, 12, 1, 1, 3)


        #MOUTH CHECKBOX
        self.mouth_check_box = QtGui.QCheckBox(self.face_detail_scroll_area_widget_contents)
        self.mouth_check_box.setObjectName("mouth_check_box")
        self.mouth_check_box.setText('Mouth')
        self.mouth_check_box.stateChanged.connect(partial(self.face_checkbox_change, 5))
        self.gridLayout_23.addWidget(self.mouth_check_box, 13, 0, 1, 1)

        #MOUTH SIDE CHECKBOX
        self.mouth_side_check_box = QtGui.QCheckBox(self.face_detail_scroll_area_widget_contents)
        self.mouth_side_check_box.setObjectName("mouth_side_check_box")
        self.mouth_side_check_box.setText('Mouth Side')
        self.mouth_side_check_box.stateChanged.connect(partial(self.face_checkbox_change, 6))
        self.gridLayout_23.addWidget(self.mouth_side_check_box, 13, 1, 1, 1)

        #MOUTH SIDE 2 CHECKBOX
        self.mouth_side_2_check_box = QtGui.QCheckBox(self.face_detail_scroll_area_widget_contents)
        self.mouth_side_2_check_box.setObjectName("mouth_side_2_check_box")
        self.mouth_side_2_check_box.setText('Mouth Side 2')
        self.mouth_side_2_check_box.stateChanged.connect(partial(self.face_checkbox_change, 7))
        self.gridLayout_23.addWidget(self.mouth_side_2_check_box, 13, 2, 1, 1)

        #MOUTH LABEL
        self.mouth_label = QtGui.QLabel(self.face_detail_scroll_area_widget_contents)
        self.mouth_label.setObjectName("no_eye_eye_label")
        self.mouth_label.setText('Mouth : ')
        self.mouth_label.hide()
        self.gridLayout_23.addWidget(self.mouth_label, 14, 0, 1, 1)

        #MOUTH LINE EIDT
        self.mouth_line_edit = QtGui.QLineEdit(self.face_detail_scroll_area_widget_contents)
        self.mouth_line_edit.setObjectName("mouth_line_edit")
        self.validator = QtGui.QDoubleValidator()
        self.mouth_line_edit.setValidator(self.validator)
        self.mouth_line_edit.setText(str(22))
        self.mouth_line_edit.hide()
        self.gridLayout_23.addWidget(self.mouth_line_edit, 14, 1, 1, 3)

        #MOUTH SIDE LABEL
        self.mouth_side_label = QtGui.QLabel(self.face_detail_scroll_area_widget_contents)
        self.mouth_side_label.setObjectName("mouth_side_label")
        self.mouth_side_label.setText('Mouth Side : ')
        self.mouth_side_label.hide()
        self.gridLayout_23.addWidget(self.mouth_side_label, 15, 0, 1, 1)

        #MOUTH SIDE LINE EIDT
        self.mouth_side_line_edit = QtGui.QLineEdit(self.face_detail_scroll_area_widget_contents)
        self.mouth_side_line_edit.setObjectName("mouth_side_line_edit")
        self.mouth_side_line_edit.setValidator(self.validator)
        self.mouth_side_line_edit.setText(str(20))
        self.mouth_side_line_edit.hide()
        self.gridLayout_23.addWidget(self.mouth_side_line_edit, 15, 1, 1, 3)

        #MOUTH SIDE 2 LABEL
        self.mouth_side_2_label = QtGui.QLabel(self.face_detail_scroll_area_widget_contents)
        self.mouth_side_2_label.setObjectName("mouth_side_2_label")
        self.mouth_side_2_label.setText('Mouth Side 2 : ')
        self.mouth_side_2_label.hide()
        self.gridLayout_23.addWidget(self.mouth_side_2_label, 16, 0, 1, 1)

        #MOUTH SIDE 2 LINE EIDT
        self.mouth_side_2_line_edit = QtGui.QLineEdit(self.face_detail_scroll_area_widget_contents)
        self.mouth_side_2_line_edit.setObjectName("mouth_side_2_line_edit")
        self.mouth_side_2_line_edit.setValidator(self.validator)
        self.mouth_side_2_line_edit.setText(str(5))
        self.mouth_side_2_line_edit.hide()
        self.gridLayout_23.addWidget(self.mouth_side_2_line_edit, 16, 1, 1, 3)


        #FACE CENTER CHECKBOX
        self.face_center_check_box = QtGui.QCheckBox(self.face_detail_scroll_area_widget_contents)
        self.face_center_check_box.setObjectName("face_center_check_box")
        self.face_center_check_box.setText('Face Center')
        self.face_center_check_box.stateChanged.connect(partial(self.face_checkbox_change, 8))
        self.gridLayout_23.addWidget(self.face_center_check_box, 17, 0, 1, 1)

        #FACE CENTER LABEL
        self.face_center_label = QtGui.QLabel(self.face_detail_scroll_area_widget_contents)
        self.face_center_label.setObjectName("face_center_label")
        self.face_center_label.setText('Face Center : ')
        self.face_center_label.hide()
        self.gridLayout_23.addWidget(self.face_center_label, 18, 0, 1, 1)

        #FACE CENTER LINE EIDT
        self.face_center_line_edit = QtGui.QLineEdit(self.face_detail_scroll_area_widget_contents)
        self.face_center_line_edit.setObjectName("face_center_line_edit")
        self.face_center_line_edit.setValidator(self.validator)
        self.face_center_line_edit.setText(str(6))
        self.face_center_line_edit.hide()
        self.gridLayout_23.addWidget(self.face_center_line_edit, 18, 1, 1, 3)


        self.spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_23.addItem(self.spacerItem, 20, 0, 1, 1)

        self.gridLayout_16.addLayout(self.gridLayout_23, 0, 0, 1, 1)
        '''
        self.head_detail_2_scroll_area.setWidget(self.face_detail_scroll_area_widget_contents)
        self.gridLayout_16.addWidget(self.face_detail_tool_box, 3, 0, 1, 1)

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
        self.face_update_button = QtGui.QPushButton(self.head_update_scrollArea_widget_contents)
        self.face_update_button.setObjectName("head_update_button")
        self.face_update_button.setText('Update (Face name)')
        self.face_update_button.clicked.connect(self.face_update_button_def)
        self.gridLayout_17.addWidget(self.face_update_button, 1, 0, 1, 1)

        # DELETE BUTTON
        self.face_delete_button = QtGui.QPushButton(self.head_update_scrollArea_widget_contents)
        self.face_delete_button.setObjectName("head_delete_button")
        self.face_delete_button.setText('Delete(Face Name)')
        # self.face_delete_button.clicked.connect(self.face_delete_button_def)
        self.gridLayout_17.addWidget(self.face_delete_button, 1, 1, 1, 1)

        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_17.addItem(spacerItem9, 0, 0, 1, 1)

        self.head_update_scroll_area.setWidget(self.head_update_scrollArea_widget_contents)
        self.gridLayout_18.addWidget(self.head_update_scroll_area, 1, 0, 1, 1)

        self.gridLayout_18.addWidget(self.head_detail_2_scroll_area, 0, 0, 1, 1)
        self.head_detail_scroll_area.setWidget(self.head_detail_scrollArea_widget_contents)
        self.head_verticalLayout.addWidget(self.head_splitter)

        self.head_detail_scroll_area.setWidget(self.head_detail_scrollArea_widget_contents)
        self.head_verticalLayout.addWidget(self.head_splitter)

    def eye_page_def(self):
        self.gridLayout_33 = QtGui.QGridLayout(self.eye_page)
        self.gridLayout_33.setObjectName("gridLayout_33")

        # EYE RADIO BUTTON
        self.eye_radio_button = QtGui.QRadioButton(self.eye_page)
        self.eye_radio_button.setObjectName("eye_radio_button")
        self.eye_radio_button.setText('Eye')
        self.eye_radio_button.toggled.connect(partial(self.eye_radio_def, 0))
        self.gridLayout_33.addWidget(self.eye_radio_button, 0, 0, 1, 1)

        # EYE SIDE RADIO BUTTON
        self.eye_side_radio_button = QtGui.QRadioButton(self.eye_page)
        self.eye_side_radio_button.setObjectName("eye_side_radio_button")
        self.eye_side_radio_button.setText('Eye Side')
        self.eye_side_radio_button.toggled.connect(partial(self.eye_radio_def, 1))
        self.gridLayout_33.addWidget(self.eye_side_radio_button, 0, 1, 1, 1)

        # EYE SIDE 2 RADIO BUTTON
        self.eye_side_2_radio_button = QtGui.QRadioButton(self.eye_page)
        self.eye_side_2_radio_button.setObjectName("eye_side_2_radio_button")
        self.eye_side_2_radio_button.setText('Eye Side 2')
        self.eye_side_2_radio_button.toggled.connect(partial(self.eye_radio_def, 2))
        self.gridLayout_33.addWidget(self.eye_side_2_radio_button, 0, 2, 1, 1)

        # MIRROR CHECK BOX
        self.eye_mirror_check_box = QtGui.QCheckBox(self.eye_page)
        self.eye_mirror_check_box.setObjectName("eye_mirror_check_box")
        self.eye_mirror_check_box.setText('Mirror')
        self.gridLayout_33.addWidget(self.eye_mirror_check_box, 1, 0, 1, 1)

        # LEFT CHECK BOX
        self.eye_left_check_box = QtGui.QCheckBox(self.eye_page)
        self.eye_left_check_box.setObjectName("eye_left_check_box")
        self.eye_left_check_box.setText('Left')
        self.gridLayout_33.addWidget(self.eye_left_check_box, 2, 0, 1, 1)

        # RIGHT CHECK BOX
        self.eye_right_check_box = QtGui.QCheckBox(self.eye_page)
        self.eye_right_check_box.setObjectName("eye_right_check_box")
        self.eye_right_check_box.setText('Right')
        self.gridLayout_33.addWidget(self.eye_right_check_box, 2, 1, 1, 1)

        # NAME LABEL
        self.eye_name_label = QtGui.QLabel(self.eye_page)
        self.eye_name_label.setObjectName("eye_name_label")
        self.eye_name_label.setText('Eye : ')
        self.gridLayout_33.addWidget(self.eye_name_label, 3, 0, 1, 1)

        # NAME LINE EDIT
        self.eye_line_edit = QtGui.QLineEdit(self.eye_page)
        self.eye_line_edit.setText("")
        self.eye_line_edit.setObjectName("eye_line_edit")
        self.gridLayout_33.addWidget(self.eye_line_edit, 3, 1, 1, 1)

        self.eye_vis_button = QtGui.QPushButton(self.eye_page)
        self.eye_vis_button.setObjectName("eye_vis_button")
        self.eye_vis_button.setText('V')
        self.eye_vis_button.setMaximumWidth(40)
        # self.eye_vis_button.setStyleSheet("background-color:rgb(0,255,0)")
        self.eye_vis_button.clicked.connect(self.eye_vis_def)
        self.gridLayout_33.addWidget(self.eye_vis_button, 3, 2, 1, 1)

        spacerItem20 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_33.addItem(spacerItem20, 4, 0, 1, 1)
        #

    def nose_page_def(self):
        self.gridLayout_33 = QtGui.QGridLayout(self.nose_page)
        self.gridLayout_33.setObjectName("gridLayout_33")

        # EYE RADIO BUTTON
        self.nose_radio_button = QtGui.QRadioButton(self.nose_page)
        self.nose_radio_button.setObjectName("nose_radio_button")
        self.nose_radio_button.setText('Nose')
        self.nose_radio_button.toggled.connect(partial(self.nose_radio_def, 0))
        self.gridLayout_33.addWidget(self.nose_radio_button, 0, 0, 1, 1)

        # EYE SIDE RADIO BUTTON
        self.nose_side_radio_button = QtGui.QRadioButton(self.nose_page)
        self.nose_side_radio_button.setObjectName("nose_side_radio_button")
        self.nose_side_radio_button.setText('Nose Side')
        self.nose_side_radio_button.toggled.connect(partial(self.nose_radio_def, 1))
        self.gridLayout_33.addWidget(self.nose_side_radio_button, 0, 1, 1, 1)

        # MIRROR CHECK BOX
        self.nose_mirror_check_box = QtGui.QCheckBox(self.nose_page)
        self.nose_mirror_check_box.setObjectName("nose_mirror_check_box")
        self.nose_mirror_check_box.setText('Mirror')
        self.gridLayout_33.addWidget(self.nose_mirror_check_box, 1, 0, 1, 1)

        # LEFT CHECK BOX
        self.nose_left_check_box = QtGui.QCheckBox(self.nose_page)
        self.nose_left_check_box.setObjectName("nose_left_check_box")
        self.nose_left_check_box.setText('Left')
        self.gridLayout_33.addWidget(self.nose_left_check_box, 2, 0, 1, 1)

        # RIGHT CHECK BOX
        self.nose_right_check_box = QtGui.QCheckBox(self.nose_page)
        self.nose_right_check_box.setObjectName("nose_right_check_box")
        self.nose_right_check_box.setText('Right')
        self.gridLayout_33.addWidget(self.nose_right_check_box, 2, 1, 1, 1)

        # NAME LABEL
        self.nose_name_label = QtGui.QLabel(self.nose_page)
        self.nose_name_label.setObjectName("nose_name_label")
        self.nose_name_label.setText('Nose : ')
        self.gridLayout_33.addWidget(self.nose_name_label, 3, 0, 1, 1)

        # NAME LINE EDIT
        self.nose_line_edit = QtGui.QLineEdit(self.nose_page)
        self.nose_line_edit.setText("")
        self.nose_line_edit.setObjectName("nose_line_edit")
        self.gridLayout_33.addWidget(self.nose_line_edit, 3, 1, 1, 1)

        self.nose_vis_button = QtGui.QPushButton(self.nose_page)
        self.nose_vis_button.setObjectName("eye_vis_button")
        self.nose_vis_button.setText('V')
        self.nose_vis_button.setMaximumWidth(40)
        self.nose_vis_button.setStyleSheet("background-color:rgb(0,255,0)")
        self.nose_vis_button.clicked.connect(self.nose_vis_def)
        self.gridLayout_33.addWidget(self.nose_vis_button, 3, 2, 1, 1)

        spacerItem20 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_33.addItem(spacerItem20, 4, 0, 1, 1)
        #

    def common_page_def(self):

        self.gridLayout_33 = QtGui.QGridLayout(self.common_page)
        self.gridLayout_33.setObjectName("gridLayout_33")

        # FORHEAD CHECKBOX
        self.for_head_check_box = QtGui.QCheckBox(self.common_page)
        self.for_head_check_box.setObjectName("for_head_check_box")
        self.for_head_check_box.setText('ForHead')
        self.for_head_check_box.stateChanged.connect(self.for_head_check_box_def)
        self.gridLayout_33.addWidget(self.for_head_check_box, 0, 0, 1, 1)

        # FORHEAD LABEL
        self.for_head_label = QtGui.QLabel(self.common_page)
        self.for_head_label.setObjectName("for_head_label")
        self.for_head_label.setText('For Head : ')
        self.for_head_label.hide()
        self.gridLayout_33.addWidget(self.for_head_label, 2, 0, 1, 1)

        # FORHEAD LINEEDIT
        self.for_head_line_edit = QtGui.QLineEdit(self.common_page)
        self.for_head_line_edit.setText("")
        self.for_head_line_edit.setObjectName("for_head_line_edit")
        self.for_head_line_edit.hide()
        self.gridLayout_33.addWidget(self.for_head_line_edit, 2, 1, 1, 1)

        # visible
        self.for_head_vis_button = QtGui.QPushButton(self.common_page)
        self.for_head_vis_button.setObjectName("for_head_vis_button")
        self.for_head_vis_button.setText('V')
        self.for_head_vis_button.setMaximumWidth(40)
        self.for_head_vis_button.setStyleSheet("background-color:rgb(0,255,0)")
        self.for_head_vis_button.hide()
        self.for_head_vis_button.clicked.connect(self.for_head_vis_def)
        self.gridLayout_33.addWidget(self.for_head_vis_button, 2, 2, 1, 1)

        # MOUTH CHECK BOX
        self.mouth_check_box = QtGui.QCheckBox(self.common_page)
        self.mouth_check_box.setObjectName("mouth_check_box")
        self.mouth_check_box.setText('Mouth')
        self.mouth_check_box.stateChanged.connect(self.mouth_check_box_def)
        self.gridLayout_33.addWidget(self.mouth_check_box, 3, 0, 1, 1)

        # MOUTH SIDE CHECK BOX
        self.mouth_side_check_box = QtGui.QCheckBox(self.common_page)
        self.mouth_side_check_box.setObjectName("mouth_side_check_box")
        self.mouth_side_check_box.setText('Mouth Side')
        self.mouth_side_check_box.stateChanged.connect(self.mouth_side_check_box_def)
        self.gridLayout_33.addWidget(self.mouth_side_check_box, 3, 1, 1, 1)

        # MOUTH SIDE 2 CHECK BOX
        self.mouth_side_2_check_box = QtGui.QCheckBox(self.common_page)
        self.mouth_side_2_check_box.setObjectName("mouth_side_2_check_box")
        self.mouth_side_2_check_box.setText('Mouth Side 2')
        self.mouth_side_2_check_box.stateChanged.connect(self.mouth_side_2_check_box_def)
        self.gridLayout_33.addWidget(self.mouth_side_2_check_box, 3, 2, 1, 1)

        # MOUTH LABEL
        self.mouth_label = QtGui.QLabel(self.common_page)
        self.mouth_label.setObjectName("mouth_label")
        self.mouth_label.setText('Mouth : ')
        self.mouth_label.hide()
        self.gridLayout_33.addWidget(self.mouth_label, 4, 0, 1, 1)

        # MOUTH LINE EDIT
        self.mouth_line_edit = QtGui.QLineEdit(self.common_page)
        self.mouth_line_edit.setText("")
        self.mouth_line_edit.setObjectName("mouth_line_edit")
        self.mouth_line_edit.hide()
        self.gridLayout_33.addWidget(self.mouth_line_edit, 4, 1, 1, 1)

        # visible
        self.mouth_vis_button = QtGui.QPushButton(self.common_page)
        self.mouth_vis_button.setObjectName("mouth_vis_button")
        self.mouth_vis_button.setText('V')
        self.mouth_vis_button.setMaximumWidth(40)
        self.mouth_vis_button.setStyleSheet("background-color:rgb(0,255,0)")
        self.mouth_vis_button.hide()
        self.mouth_vis_button.clicked.connect(self.mouth_vis_def)
        self.gridLayout_33.addWidget(self.mouth_vis_button, 4, 2, 1, 1)

        # MOUTH SIDE LABEL
        self.mouth_side_label = QtGui.QLabel(self.common_page)
        self.mouth_side_label.setObjectName("mouth_side_label")
        self.mouth_side_label.setText('Mouth Side : ')
        self.mouth_side_label.hide()
        self.gridLayout_33.addWidget(self.mouth_side_label, 5, 0, 1, 1)

        # MOUTH SIDE LINE EDIT
        self.mouth_side_line_edit = QtGui.QLineEdit(self.common_page)
        self.mouth_side_line_edit.setText("")
        self.mouth_side_line_edit.setObjectName("mouth_side_line_edit")
        self.mouth_side_line_edit.hide()
        self.gridLayout_33.addWidget(self.mouth_side_line_edit, 5, 1, 1, 1)

        # visible
        self.mouth_side_vis_button = QtGui.QPushButton(self.common_page)
        self.mouth_side_vis_button.setObjectName("mouth_side_vis_button")
        self.mouth_side_vis_button.setText('V')
        self.mouth_side_vis_button.setMaximumWidth(40)
        self.mouth_side_vis_button.setStyleSheet("background-color:rgb(0,255,0)")
        self.mouth_side_vis_button.hide()
        self.mouth_side_vis_button.clicked.connect(self.mouth_side_vis_def)
        self.gridLayout_33.addWidget(self.mouth_side_vis_button, 5, 2, 1, 1)

        # MOUTH SIDE 2 MIRROR CHECK BOX
        self.mouth_side_2_mirror_check_box = QtGui.QCheckBox(self.common_page)
        self.mouth_side_2_mirror_check_box.setObjectName("mouth_side_2_mirror_check_box")
        self.mouth_side_2_mirror_check_box.setText('Mirror')
        self.mouth_side_2_mirror_check_box.hide()
        self.gridLayout_33.addWidget(self.mouth_side_2_mirror_check_box, 6, 0, 1, 1)

        # MOUTH SIDE 2 MIRROR LEFT CHECK BOX
        self.mouth_side_2_left_check_box = QtGui.QCheckBox(self.common_page)
        self.mouth_side_2_left_check_box.setObjectName("mouth_side_2_left_check_box")
        self.mouth_side_2_left_check_box.setText('Left')
        self.mouth_side_2_left_check_box.hide()
        self.gridLayout_33.addWidget(self.mouth_side_2_left_check_box, 7, 0, 1, 1)

        # MOUTH SIDE 2 MIRROR RIGHT CHECK BOX
        self.mouth_side_2_right_check_box = QtGui.QCheckBox(self.common_page)
        self.mouth_side_2_right_check_box.setObjectName("mouth_side_2_right_check_box")
        self.mouth_side_2_right_check_box.setText('Right')
        self.mouth_side_2_right_check_box.hide()
        self.gridLayout_33.addWidget(self.mouth_side_2_right_check_box, 7, 1, 1, 1)

        # MOUTH SIDE 2 LABEL
        self.mouth_side_2_label = QtGui.QLabel(self.common_page)
        self.mouth_side_2_label.setObjectName("mouth_side_2_label")
        self.mouth_side_2_label.setText('Mouth Side 2 : ')
        self.mouth_side_2_label.hide()
        self.gridLayout_33.addWidget(self.mouth_side_2_label, 8, 0, 1, 1)

        # MOUTH SIDE 2 LINE EDIT
        self.mouth_side_2_line_edit = QtGui.QLineEdit(self.common_page)
        self.mouth_side_2_line_edit.setText("")
        self.mouth_side_2_line_edit.setObjectName("mouth_side_2_line_edit")
        self.mouth_side_2_line_edit.hide()
        self.gridLayout_33.addWidget(self.mouth_side_2_line_edit, 8, 1, 1, 1)

        # visible
        self.mouth_side_2_vis_button = QtGui.QPushButton(self.common_page)
        self.mouth_side_2_vis_button.setObjectName("mouth_side_2_vis_button")
        self.mouth_side_2_vis_button.setText('V')
        self.mouth_side_2_vis_button.setMaximumWidth(40)
        self.mouth_side_2_vis_button.setStyleSheet("background-color:rgb(0,255,0)")
        self.mouth_side_2_vis_button.hide()
        self.mouth_side_2_vis_button.clicked.connect(self.mouth_side_2_vis_def)

        self.gridLayout_33.addWidget(self.mouth_side_2_vis_button, 8, 2, 1, 1)

        # FACE CENTER CHECK BOX
        self.face_center_check_box = QtGui.QCheckBox(self.common_page)
        self.face_center_check_box.setObjectName("face_center_check_box")
        self.face_center_check_box.setText('Face Center')
        self.face_center_check_box.stateChanged.connect(self.face_center_check_box_def)
        self.gridLayout_33.addWidget(self.face_center_check_box, 9, 0, 1, 1)

        # FACE CEBTER LABEL
        self.face_center_label = QtGui.QLabel(self.common_page)
        self.face_center_label.setObjectName("face_center_label")
        self.face_center_label.setText('Face Center : ')
        self.face_center_label.hide()
        self.gridLayout_33.addWidget(self.face_center_label, 10, 0, 1, 1)

        # FACE CENTER LINE EDIT
        self.face_center_line_edit = QtGui.QLineEdit(self.common_page)
        self.face_center_line_edit.setText("")
        self.face_center_line_edit.setObjectName("face_center_line_edit")
        self.face_center_line_edit.hide()
        self.gridLayout_33.addWidget(self.face_center_line_edit, 10, 1, 1, 1)

        # visible
        self.face_center_vis_button = QtGui.QPushButton(self.common_page)
        self.face_center_vis_button.setObjectName("face_center_vis_button")
        self.face_center_vis_button.setText('V')
        self.face_center_vis_button.setMaximumWidth(40)
        self.face_center_vis_button.setStyleSheet("background-color:rgb(0,255,0)")
        self.face_center_vis_button.hide()
        self.face_center_vis_button.clicked.connect(self.face_center_vis_def)
        self.gridLayout_33.addWidget(self.face_center_vis_button, 10, 2, 1, 1)

        spacerItem20 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_33.addItem(spacerItem20, 11, 0, 1, 1)

        pass

    def lock_attr(self):
        self.eye_radio_button.setDisabled(True)
        self.eye_side_radio_button.setDisabled(True)
        self.eye_side_2_radio_button.setDisabled(True)
        self.eye_mirror_check_box.setDisabled(True)
        self.eye_left_check_box.setDisabled(True)
        self.eye_right_check_box.setDisabled(True)
        self.eye_name_label.setDisabled(True)
        self.eye_line_edit.setDisabled(True)
        self.eye_vis_button.setDisabled(True)
        self.nose_radio_button.setDisabled(True)
        self.nose_side_radio_button.setDisabled(True)
        self.nose_mirror_check_box.setDisabled(True)
        self.nose_left_check_box.setDisabled(True)
        self.nose_right_check_box.setDisabled(True)
        self.nose_name_label.setDisabled(True)
        self.nose_line_edit.setDisabled(True)
        self.nose_vis_button.setDisabled(True)
        self.for_head_check_box.setDisabled(True)
        self.for_head_label.setDisabled(True)
        self.for_head_line_edit.setDisabled(True)
        self.for_head_vis_button.setDisabled(True)
        self.mouth_check_box.setDisabled(True)
        self.mouth_label.setDisabled(True)
        self.mouth_line_edit.setDisabled(True)
        self.mouth_vis_button.setDisabled(True)
        self.mouth_side_check_box.setDisabled(True)
        self.mouth_side_label.setDisabled(True)
        self.mouth_side_line_edit.setDisabled(True)
        self.mouth_side_vis_button.setDisabled(True)
        self.mouth_side_2_check_box.setDisabled(True)
        self.mouth_side_2_label.setDisabled(True)
        self.mouth_side_2_line_edit.setDisabled(True)
        self.mouth_side_2_vis_button.setDisabled(True)
        self.face_center_check_box.setDisabled(True)
        self.face_center_label.setDisabled(True)
        self.face_center_line_edit.setDisabled(True)
        self.face_center_vis_button.setDisabled(True)
        self.face_update_button.setDisabled(True)
        self.face_delete_button.setDisabled(True)

    def unlock_attr(self, common_vis=True, eye=False, nose=False):
        if common_vis == True:
            self.eye_radio_button.setDisabled(False)
            self.eye_side_radio_button.setDisabled(False)
            self.eye_side_2_radio_button.setDisabled(False)
            self.nose_radio_button.setDisabled(False)
            self.nose_side_radio_button.setDisabled(False)
            self.for_head_check_box.setDisabled(False)
            self.for_head_label.setDisabled(False)
            self.for_head_line_edit.setDisabled(False)
            self.for_head_vis_button.setDisabled(False)
            self.mouth_check_box.setDisabled(False)
            self.mouth_label.setDisabled(False)
            self.mouth_line_edit.setDisabled(False)
            self.mouth_vis_button.setDisabled(False)
            self.mouth_side_check_box.setDisabled(False)
            self.mouth_side_label.setDisabled(False)
            self.mouth_side_line_edit.setDisabled(False)
            self.mouth_side_vis_button.setDisabled(False)
            self.mouth_side_2_check_box.setDisabled(False)
            self.mouth_side_2_label.setDisabled(False)
            self.mouth_side_2_line_edit.setDisabled(False)
            self.mouth_side_2_vis_button.setDisabled(False)
            self.face_center_check_box.setDisabled(False)
            self.face_center_label.setDisabled(False)
            self.face_center_line_edit.setDisabled(False)
            self.face_center_vis_button.setDisabled(False)
            self.face_update_button.setDisabled(False)
            self.face_delete_button.setDisabled(False)
        if eye == True:
            self.eye_mirror_check_box.setDisabled(False)
            self.eye_left_check_box.setDisabled(False)
            self.eye_right_check_box.setDisabled(False)
            self.eye_name_label.setDisabled(False)
            self.eye_line_edit.setDisabled(False)
            self.eye_vis_button.setDisabled(False)

        if nose == True:
            self.nose_mirror_check_box.setDisabled(False)
            self.nose_left_check_box.setDisabled(False)
            self.nose_right_check_box.setDisabled(False)
            self.nose_name_label.setDisabled(False)
            self.nose_line_edit.setDisabled(False)
            self.nose_vis_button.setDisabled(False)

    def radio_button_change(self, b, val):

        if val == True:
            # unlock the val
            self.unlock_attr()

            # get the value
            self.get_input_data(self.no_face[b])

            self.eye_side_radio_button.setChecked(True)
            self.eye_radio_button.setChecked(True)

    def eye_radio_def(self, b, val):
        if val == True:
            # unlock the eye
            self.unlock_attr(eye=True)

            # get eye data and input
            self.get_eye_data(b)

    def get_eye_data(self, value):
        if value == 0:
            # GET THE LEFT EYE
            l_eye_geo_name = self.prefix_name + '_L_Eye_1_Tem_' + str(self.val) + '_LOC'
            if cmds.objExists(l_eye_geo_name):
                self.eye_left_check_box.setChecked(True)
            else:
                self.eye_left_check_box.setDisabled(True)

            # CHECK IF MIRROR IS ON
            # Template_L_Eye_1_Tem_1_LOC
            loc_mirror_name = l_eye_geo_name + '_right_to_left_Mirror_Grp'
            if cmds.objExists(loc_mirror_name):
                self.eye_mirror_check_box.setChecked(True)

            # GET THE RIGHT EYE
            r_eye_geo_name = self.prefix_name + '_R_Eye_1_Tem_' + str(self.val) + '_Geo'
            if cmds.objExists(r_eye_geo_name):
                self.eye_right_check_box.setChecked(True)
            else:
                self.eye_right_check_box.setDisabled(True)

            # GET THE NO OF THE EYE
            if cmds.objExists(l_eye_geo_name) or cmds.objExists(r_eye_geo_name):
                if cmds.objExists(l_eye_geo_name):
                    eye_geo_all_name = self.prefix_name + '_L_Eye_*_Tem_' + str(self.val) + '_Geo'
                    eye_side_geo = self.prefix_name + '_L_Eye_Side_*_Tem_' + str(self.val) + '_Geo'
                    eye_side_2_geo = self.prefix_name + '_L_Eye_Side_2_*_Tem_' + str(self.val) + '_Geo'
                else:
                    eye_geo_all_name = self.prefix_name + '_R_Eye_*_Tem_' + str(self.val) + '_Geo'
                    eye_side_geo = self.prefix_name + '_R_Eye_Side_*_Tem_' + str(self.val) + '_Geo'
                    eye_side_2_geo = self.prefix_name + '_R_Eye_Side_2_*_Tem_' + str(self.val) + '_Geo'

                cmds.select(eye_geo_all_name)
                if cmds.objExists(eye_side_geo):
                    cmds.select(eye_side_geo, d=True)
                if cmds.objExists(eye_side_2_geo):
                    cmds.select(eye_side_2_geo, d=True)
                sel_geo = cmds.ls(sl=True)
                self.eye_line_edit.setText(str(len(sel_geo)))

                # check the vis
                vis = cmds.getAttr(sel_geo[0] + '.v')
                if vis == True:
                    self.eye_vis_button.setStyleSheet("background-color:rgb(0,255,0)")
                else:
                    self.eye_vis_button.setStyleSheet("background-color:rgb(255,0,0)")
            else:
                self.eye_name_label.setDisabled(True)
                self.eye_line_edit.setDisabled(True)
                self.eye_vis_button.setDisabled(True)

        if value == 1:
            # GET THE LEFT EYE
            l_eye_geo_name = self.prefix_name + '_L_Eye_Side_1_Tem_' + str(self.val) + '_LOC'
            if cmds.objExists(l_eye_geo_name):
                self.eye_left_check_box.setChecked(True)
            else:
                self.eye_left_check_box.setChecked(False)
                self.eye_left_check_box.setDisabled(True)

            loc_mirror_name = l_eye_geo_name + '_right_to_left_Mirror_Grp'
            print(loc_mirror_name)
            if cmds.objExists(loc_mirror_name):
                self.eye_mirror_check_box.setChecked(True)

            # GET THE RIGHT EYE
            r_eye_geo_name = self.prefix_name + '_R_Eye_Side_1_Tem_' + str(self.val) + '_Geo'
            if cmds.objExists(r_eye_geo_name):
                self.eye_right_check_box.setChecked(True)
            else:
                self.eye_right_check_box.setChecked(False)
                self.eye_right_check_box.setDisabled(True)

            # GET THE NO OF THE EYE
            if cmds.objExists(l_eye_geo_name) or cmds.objExists(r_eye_geo_name):
                if cmds.objExists(l_eye_geo_name):
                    eye_side_geo = self.prefix_name + '_L_Eye_Side_*_Tem_' + str(self.val) + '_Geo'
                    eye_side_2_geo = self.prefix_name + '_L_Eye_Side_2_*_Tem_' + str(self.val) + '_Geo'
                else:
                    eye_side_geo = self.prefix_name + '_R_Eye_Side_*_Tem_' + str(self.val) + '_Geo'
                    eye_side_2_geo = self.prefix_name + '_R_Eye_Side_2_*_Tem_' + str(self.val) + '_Geo'

                cmds.select(eye_side_geo)
                if cmds.objExists(eye_side_2_geo):
                    cmds.select(eye_side_2_geo, d=True)
                sel_geo = cmds.ls(sl=True)
                self.eye_line_edit.setText(str(len(sel_geo)))

                # check the vis
                vis = cmds.getAttr(sel_geo[0] + '.v')
                if vis == True:
                    self.eye_vis_button.setStyleSheet("background-color:rgb(0,255,0)")
                else:
                    self.eye_vis_button.setStyleSheet("background-color:rgb(255,0,0)")
            else:
                self.eye_name_label.setDisabled(True)
                self.eye_line_edit.setDisabled(True)
                self.eye_vis_button.setDisabled(True)

        if value == 2:
            # GET THE LEFT EYE
            # Template_L_Eye_Side_2_1_Tem_3_LOC
            l_eye_geo_name = self.prefix_name + '_L_Eye_Side_2_1_Tem_' + str(self.val) + '_LOC'
            if cmds.objExists(l_eye_geo_name):
                self.eye_left_check_box.setChecked(True)
            else:
                self.eye_left_check_box.setChecked(False)
                self.eye_left_check_box.setDisabled(True)

            loc_mirror_name = l_eye_geo_name + '_right_to_left_Mirror_Grp'
            if cmds.objExists(loc_mirror_name):
                self.eye_mirror_check_box.setChecked(True)

            # GET THE RIGHT EYE
            r_eye_geo_name = self.prefix_name + '_R_Eye_Side_2_1_Tem_' + str(self.val) + '_Geo'
            if cmds.objExists(r_eye_geo_name):
                self.eye_right_check_box.setChecked(True)
            else:
                self.eye_right_check_box.setChecked(False)
                self.eye_right_check_box.setDisabled(True)

            # GET THE NO OF THE EYE
            if cmds.objExists(l_eye_geo_name) or cmds.objExists(r_eye_geo_name):
                if cmds.objExists(l_eye_geo_name):
                    eye_side_2_geo = self.prefix_name + '_L_Eye_Side_2_*_Tem_' + str(self.val) + '_Geo'
                else:
                    eye_side_2_geo = self.prefix_name + '_R_Eye_Side_2_*_Tem_' + str(self.val) + '_Geo'

                cmds.select(eye_side_2_geo)
                sel_geo = cmds.ls(sl=True)
                self.eye_line_edit.setText(str(len(sel_geo)))

                # check the vis
                vis = cmds.getAttr(sel_geo[0] + '.v')
                if vis == True:
                    self.eye_vis_button.setStyleSheet("background-color:rgb(0,255,0)")
                else:
                    self.eye_vis_button.setStyleSheet("background-color:rgb(255,0,0)")
            else:
                self.eye_name_label.setDisabled(True)
                self.eye_line_edit.setDisabled(True)
                self.eye_vis_button.setDisabled(True)

    def eye_vis_def(self):
        # get which one is on
        if self.eye_radio_button.isChecked():
            value = 0
        elif self.eye_side_radio_button.isChecked():
            value = 1
        elif self.eye_side_2_radio_button.isChecked():
            value = 2

        # check which is on
        left_check_box_query = self.eye_left_check_box.isChecked()
        right_check_box_query = self.eye_right_check_box.isChecked()
        if value == 0:
            cmds.select(cl=True)
            if left_check_box_query == True:
                # Template_L_Eye_Tem_1_Crv
                eye_common = self.prefix_name + '_L_Eye_Tem_' + str(self.val)
                eye_all_common = self.prefix_name + '_L_Eye_*_Tem_' + str(self.val)
                eye_side_common = self.prefix_name + '_L_Eye_Side_*_Tem_' + str(self.val)
                eye_side_2_common = self.prefix_name + '_L_Eye_Side_2_*_Tem_' + str(self.val)

                eye_geo_name = eye_all_common + '_Geo'
                eye_loc_name = eye_all_common + '_LOC'
                main_loc_name = eye_common + '_Main_LOC'
                crv_name = eye_common + '_Crv'

                eye_side_geo = eye_side_common + '_Geo'
                eye_side_loc = eye_side_common + '_LOC'

                eye_side_2_geo = eye_side_2_common + '_Geo'
                eye_side_2_loc = eye_side_2_common + '_LOC'

                cmds.select(eye_geo_name, eye_loc_name, main_loc_name, crv_name, add=True)

                if cmds.objExists(eye_side_geo):
                    cmds.select(eye_side_geo, eye_side_loc, d=True)
                if cmds.objExists(eye_side_2_geo):
                    cmds.select(eye_side_2_geo, eye_side_2_loc, d=True)

            if right_check_box_query == True:
                eye_common = self.prefix_name + '_R_Eye_Tem_' + str(self.val)
                eye_all_common = self.prefix_name + '_R_Eye_*_Tem_' + str(self.val)
                eye_side_common = self.prefix_name + '_R_Eye_Side_*_Tem_' + str(self.val)
                eye_side_2_common = self.prefix_name + '_R_Eye_Side_2_*_Tem_' + str(self.val)

                eye_geo_name = eye_all_common + '_Geo'
                eye_loc_name = eye_all_common + '_LOC'
                main_loc_name = eye_common + '_Main_LOC'
                crv_name = eye_common + '_Crv'

                eye_side_geo = eye_side_common + '_Geo'
                eye_side_loc = eye_side_common + '_LOC'

                eye_side_2_geo = eye_side_2_common + '_Geo'
                eye_side_2_loc = eye_side_2_common + '_LOC'
                cmds.select(eye_geo_name, eye_loc_name, main_loc_name, crv_name, add=True)

                if cmds.objExists(eye_side_geo):
                    cmds.select(eye_side_geo, eye_side_loc, d=True)
                if cmds.objExists(eye_side_2_geo):
                    cmds.select(eye_side_2_geo, eye_side_2_loc, d=True)

            sel_geo = cmds.ls(sl=True)

        if value == 1:
            cmds.select(cl=True)
            if left_check_box_query == True:
                # Template_L_Eye_Tem_1_Crv
                eye_common = self.prefix_name + '_L_Eye_Side_Tem_' + str(self.val)
                eye_side_common = self.prefix_name + '_L_Eye_Side_*_Tem_' + str(self.val)
                eye_side_2_common = self.prefix_name + '_L_Eye_Side_2_*_Tem_' + str(self.val)

                # Template_L_Eye_Side_Tem_2_Main_LOC
                main_loc_name = eye_common + '_Main_LOC'
                crv_name = eye_common + '_Crv'

                eye_side_geo = eye_side_common + '_Geo'
                eye_side_loc = eye_side_common + '_LOC'

                eye_side_2_geo = eye_side_2_common + '_Geo'
                eye_side_2_loc = eye_side_2_common + '_LOC'

                cmds.select(eye_side_geo, eye_side_loc, main_loc_name, crv_name, add=True)
                if cmds.objExists(eye_side_2_geo):
                    cmds.select(eye_side_2_geo, eye_side_2_loc, d=True)

            if right_check_box_query == True:
                eye_common = self.prefix_name + '_R_Eye_Side_Tem_' + str(self.val)
                eye_side_common = self.prefix_name + '_R_Eye_Side_*_Tem_' + str(self.val)
                eye_side_2_common = self.prefix_name + '_R_Eye_Side_2_*_Tem_' + str(self.val)

                main_loc_name = eye_common + '_Main_LOC'
                crv_name = eye_common + '_Crv'

                eye_side_geo = eye_side_common + '_Geo'
                eye_side_loc = eye_side_common + '_LOC'

                eye_side_2_geo = eye_side_2_common + '_Geo'
                eye_side_2_loc = eye_side_2_common + '_LOC'

                cmds.select(eye_side_geo, eye_side_loc, main_loc_name, crv_name, add=True)
                if cmds.objExists(eye_side_2_geo):
                    cmds.select(eye_side_2_geo, eye_side_2_loc, d=True)

            sel_geo = cmds.ls(sl=True)

        if value == 2:
            cmds.select(cl=True)
            if left_check_box_query == True:
                # Template_L_Eye_Tem_1_Crv
                eye_common = self.prefix_name + '_L_Eye_Side_2_Tem_' + str(self.val)
                eye_side_2_common = self.prefix_name + '_L_Eye_Side_2_*_Tem_' + str(self.val)

                # Template_L_Eye_Side_Tem_2_Main_LOC
                main_loc_name = eye_common + '_Main_LOC'
                crv_name = eye_common + '_Crv'

                eye_side_2_geo = eye_side_2_common + '_Geo'
                eye_side_2_loc = eye_side_2_common + '_LOC'

                cmds.select(eye_side_2_geo, eye_side_2_loc, main_loc_name, crv_name, add=True)

            if right_check_box_query == True:
                # Template_L_Eye_Side_2_Tem_3_Crv
                eye_common = self.prefix_name + '_R_Eye_Side_2_Tem_' + str(self.val)
                eye_side_2_common = self.prefix_name + '_R_Eye_Side_2_*_Tem_' + str(self.val)

                # Template_L_Eye_Side_Tem_2_Main_LOC
                main_loc_name = eye_common + '_Main_LOC'
                crv_name = eye_common + '_Crv'

                eye_side_2_geo = eye_side_2_common + '_Geo'
                eye_side_2_loc = eye_side_2_common + '_LOC'

                cmds.select(eye_side_2_geo, eye_side_2_loc, main_loc_name, crv_name, add=True)

            sel_geo = cmds.ls(sl=True)

        vis = cmds.getAttr(sel_geo[0] + '.v')
        if vis == True:
            a = 0
            while a < len(sel_geo):
                cmds.setAttr((sel_geo[a] + '.v'), 0)
                a += 1
            self.eye_vis_button.setStyleSheet("background-color:rgb(255,0,0)")
        else:
            a = 0
            while a < len(sel_geo):
                cmds.setAttr((sel_geo[a] + '.v'), 1)
                a += 1
            self.eye_vis_button.setStyleSheet("background-color:rgb(0,255,0)")

        cmds.select(cl=True)

    def get_input_data(self, face_name):
        self.face_name = face_name
        self.name = self.face_name.split('_')
        # Template_Face_Tem_2_Main_Grp
        self.input_main_grp_name = '*_Face_Tem_' + self.name[-1] + '_Main_Grp'
        cmds.select(self.input_main_grp_name)
        self.input_sel_main_grp_name = cmds.ls(sl=True)[0]
        self.input_split_main_grp = self.input_sel_main_grp_name.split('_Face_Tem_')[0]

        # get left eye
        self.val = self.name[-1]
        self.prefix_name = self.input_split_main_grp

        # COMMON CHANGE
        # FOR HEAD
        for_head_loc = self.prefix_name + '_For_Head_1_Tem_' + str(self.val) + "_LOC"
        if cmds.objExists(for_head_loc):
            self.for_head_check_box.setChecked(True)

            for_head_all_loc = self.prefix_name + '_For_Head_*_Tem_' + str(self.val) + "_LOC"
            cmds.select(for_head_all_loc)
            sel_for_head_loc = cmds.ls(sl=True)
            self.for_head_line_edit.setText(str(len(sel_for_head_loc)))

            vis = cmds.getAttr(for_head_loc + '.v')
            if vis == True:
                self.for_head_vis_button.setStyleSheet("background-color:rgb(0,255,0)")
            else:
                self.for_head_vis_button.setStyleSheet("background-color:rgb(255,0,0)")



        else:
            self.for_head_label.setDisabled(True)
            self.for_head_line_edit.setDisabled(True)
            self.for_head_vis_button.setDisabled(True)

        # MOUTH
        # Template_Mouth_1_Tem_1_LOC
        mouth_loc = self.prefix_name + '_Mouth_1_Tem_' + str(self.val) + "_LOC"
        if cmds.objExists(mouth_loc):
            self.mouth_check_box.setChecked(True)

            mouth_all_loc = self.prefix_name + '_Mouth_*_Tem_' + str(self.val) + "_LOC"
            cmds.select(mouth_all_loc)
            sel_mouth = cmds.ls(sl=True)
            self.mouth_line_edit.setText(str(len(sel_mouth)))

            # change the button
            vis = cmds.getAttr(mouth_loc + '.v')
            if vis == True:
                self.mouth_vis_button.setStyleSheet("background-color:rgb(0,255,0)")
            else:
                self.mouth_vis_button.setStyleSheet("background-color:rgb(255,0,0)")
        else:
            self.mouth_check_box.setDisabled(True)
            self.mouth_label.setDisabled(True)
            self.mouth_line_edit.setDisabled(True)
            self.mouth_vis_button.setDisabled(True)

        # MOUTH SIDE
        # Template_Mouth_Side_1_Tem_1_LOC
        mouth_side_loc = self.prefix_name + '_Mouth_Side_1_Tem_' + str(self.val) + "_LOC"
        if cmds.objExists(mouth_side_loc):
            self.mouth_side_check_box.setChecked(True)

            mouth_side_all_loc = self.prefix_name + '_Mouth_Side_*_Tem_' + str(self.val) + "_LOC"
            cmds.select(mouth_side_all_loc)
            sel_side_mouth = cmds.ls(sl=True)
            self.mouth_side_line_edit.setText(str(len(sel_side_mouth)))

            vis = cmds.getAttr(mouth_side_loc + '.v')
            if vis == True:
                self.mouth_side_vis_button.setStyleSheet("background-color:rgb(0,255,0)")
            else:
                self.mouth_side_vis_button.setStyleSheet("background-color:rgb(255,0,0)")

        else:
            self.mouth_side_check_box.setDisabled(True)
            self.mouth_side_label.setDisabled(True)
            self.mouth_side_line_edit.setDisabled(True)
            self.mouth_side_vis_button.setDisabled(True)

        # MOUTH SIDE 2
        # Template_L_Mouth_Side_2_1_Tem_1_LOC
        l_side_2_loc = self.prefix_name + '_L_Mouth_Side_2_1_Tem_' + str(self.val) + "_LOC"
        r_side_2_loc = self.prefix_name + '_R_Mouth_Side_2_1_Tem_' + str(self.val) + "_LOC"
        if cmds.objExists(l_side_2_loc) or cmds.objExists(r_side_2_loc):

            if cmds.objExists(l_side_2_loc):
                self.mouth_side_2_check_box.setChecked(True)
                self.mouth_side_2_left_check_box.setChecked(True)

                vis = cmds.getAttr(l_side_2_loc + '.v')
                if vis == True:
                    self.mouth_side_2_vis_button.setStyleSheet("background-color:rgb(0,255,0)")
                else:
                    self.mouth_side_2_vis_button.setStyleSheet("background-color:rgb(255,0,0)")

            r_side_2_loc = self.prefix_name + '_R_Mouth_Side_2_1_Tem_' + str(self.val) + "_LOC"
            if cmds.objExists(r_side_2_loc):
                self.mouth_side_2_check_box.setChecked(True)
                self.mouth_side_2_right_check_box.setChecked(True)

                vis = cmds.getAttr(r_side_2_loc + '.v')
                if vis == True:
                    self.mouth_side_2_vis_button.setStyleSheet("background-color:rgb(0,255,0)")
                else:
                    self.mouth_side_2_vis_button.setStyleSheet("background-color:rgb(255,0,0)")

            if cmds.objExists(l_side_2_loc):
                l_side_2_all_loc = self.prefix_name + '_L_Mouth_Side_2_*_Tem_' + str(self.val) + "_LOC"
                cmds.select(l_side_2_all_loc)

            if cmds.objExists(r_side_2_loc):
                r_side_2_all_loc = self.prefix_name + '_R_Mouth_Side_2_*_Tem_' + str(self.val) + "_LOC"
                cmds.select(r_side_2_all_loc)

            sel_loc = cmds.ls(sl=True)
            self.mouth_side_2_line_edit.setText(str(len(sel_loc)))
        else:
            self.mouth_side_2_check_box.setDisabled(True)
            self.mouth_side_2_label.setDisabled(True)
            self.mouth_side_2_line_edit.setDisabled(True)
            self.mouth_side_2_vis_button.setDisabled(True)

        # FACE CENTER
        # Template_Face_Center_1_Tem_1_LOC
        face_center_loc = self.prefix_name + '_Face_Center_1_Tem_' + str(self.val) + "_LOC"
        if cmds.objExists(face_center_loc):
            self.face_center_check_box.setChecked(True)

            face_center_all_loc = self.prefix_name + '_Face_Center_*_Tem_' + str(self.val) + "_LOC"
            cmds.select(face_center_all_loc)
            sel_face_center = cmds.ls(sl=True)
            self.face_center_line_edit.setText(str(len(sel_face_center)))

            vis = cmds.getAttr(face_center_loc + '.v')
            if vis == True:
                self.face_center_vis_button.setStyleSheet("background-color:rgb(0,255,0)")
            else:
                self.face_center_vis_button.setStyleSheet("background-color:rgb(255,0,0)")

        else:
            self.face_center_check_box.setDisabled(True)
            self.face_center_label.setDisabled(True)
            self.face_center_line_edit.setDisabled(True)
            self.face_center_vis_button.setDisabled(True)

        # get the grpup name
        self.get_grp_name()

    def get_grp_name(self):
        self.sphere_group_name = self.prefix_name + '_Eye_Tem_' + str(self.val) + "_Sphere_Grp"
        self.loc_center_group_name = self.prefix_name + '_Eye_Tem_' + str(self.val) + "_Loc_Center_Grp"
        self.loc_main_group_name = self.prefix_name + '_Eye_Tem_' + str(self.val) + "_Loc_Main_Grp"
        self.cluster_group_name = self.prefix_name + '_Eye_Tem_' + str(self.val) + "_Cluster_Grp"
        self.curve_group_name = self.prefix_name + '_Eye_Tem_' + str(self.val) + "_Crv_Grp"
        self.main_grp_name = self.prefix_name + '_Face_Tem_' + str(self.val) + '_Main_Grp'

    def nose_radio_def(self, b, val):
        if val == True:
            # unlock the nose
            self.unlock_attr(nose=True)

            # get nose data and input
            self.get_nose_data(b)

    def get_nose_data(self, value):
        if value == 0:
            self.nose_left_check_box.setChecked(False)
            self.nose_right_check_box.setChecked(False)
            self.nose_mirror_check_box.setDisabled(True)
            self.nose_left_check_box.setDisabled(True)
            self.nose_right_check_box.setDisabled(True)
            self.nose_name_label.setDisabled(True)
            self.nose_line_edit.setDisabled(True)
            self.nose_vis_button.setDisabled(False)
        if value == 1:
            # check the nose side value
            # Template_L_Nose_Side_1_Tem_1_LOC
            # Template_R_Nose_Side_1_Tem_1_LOC
            # get the no of the object

            # GET THE LEFT EYE
            l_nose_geo_name = self.prefix_name + '_L_Nose_Side_1_Tem_' + str(self.val) + '_Geo'
            if cmds.objExists(l_nose_geo_name):
                self.nose_left_check_box.setChecked(True)
            else:
                self.nose_left_check_box.setDisabled(True)

            # GET THE RIGHT EYE
            r_nose_geo_name = self.prefix_name + '_R_Nose_Side_1_Tem_' + str(self.val) + '_Geo'
            if cmds.objExists(r_nose_geo_name):
                self.nose_right_check_box.setChecked(True)
            else:
                self.nose_right_check_box.setDisabled(True)

            # GET THE NO OF THE EYE
            if cmds.objExists(l_nose_geo_name) or cmds.objExists(r_nose_geo_name):
                if cmds.objExists(l_nose_geo_name):
                    eye_geo_all_name = self.prefix_name + '_L_Nose_Side_*_Tem_' + str(self.val) + '_Geo'

                else:
                    eye_geo_all_name = self.prefix_name + '_R_Nose_Side_*_Tem_' + str(self.val) + '_Geo'

                cmds.select(eye_geo_all_name)
                sel_geo = cmds.ls(sl=True)
                self.nose_line_edit.setText(str(len(sel_geo)))

                # check the vis
                vis = cmds.getAttr(sel_geo[0] + '.v')
                if vis == True:
                    self.nose_vis_button.setStyleSheet("background-color:rgb(0,255,0)")
                else:
                    self.nose_vis_button.setStyleSheet("background-color:rgb(255,0,0)")
            else:
                self.nose_name_label.setDisabled(True)
                self.nose_line_edit.setDisabled(True)
                self.nose_vis_button.setDisabled(True)

    def nose_vis_def(self):
        # get which one is on
        if self.nose_radio_button.isChecked():
            value = 0
        elif self.nose_side_radio_button.isChecked():
            value = 1
        # check which is on
        nose_left_check_box_query = self.nose_left_check_box.isChecked()
        nose_right_check_box_query = self.nose_right_check_box.isChecked()
        if value == 1:
            cmds.select(cl=True)
            if nose_left_check_box_query == True:
                eye_common = self.prefix_name + '_L_Nose_Side_Tem_' + str(self.val)
                eye_all_common = self.prefix_name + '_L_Nose_Side_*_Tem_' + str(self.val)

                eye_geo_name = eye_all_common + '_Geo'
                eye_loc_name = eye_all_common + '_LOC'
                main_loc_name = eye_common + '_Main_LOC'
                crv_name = eye_common + '_Crv'

                cmds.select(eye_geo_name, eye_loc_name, main_loc_name, crv_name, add=True)

            if nose_right_check_box_query == True:
                eye_common = self.prefix_name + '_R_Nose_Side_Tem_' + str(self.val)
                eye_all_common = self.prefix_name + '_R_Nose_Side_*_Tem_' + str(self.val)

                eye_geo_name = eye_all_common + '_Geo'
                eye_loc_name = eye_all_common + '_LOC'
                main_loc_name = eye_common + '_Main_LOC'
                crv_name = eye_common + '_Crv'

                cmds.select(eye_geo_name, eye_loc_name, main_loc_name, crv_name, add=True)

            sel_geo = cmds.ls(sl=True)

        if value == 0:
            cmds.select(cl=True)

            eye_common = self.prefix_name + '_L_Nose_Tem_' + str(self.val)
            eye_all_common = self.prefix_name + '_L_Nose_*_Tem_' + str(self.val)
            nose_side_all_common = self.prefix_name + '_L_Nose_Side_*_Tem_' + str(self.val)

            eye_geo_name = eye_all_common + '_Geo'
            eye_loc_name = eye_all_common + '_LOC'
            main_loc_name = eye_common + '_Main_LOC'
            crv_name = eye_common + '_Crv'

            nose_side_geo_name = nose_side_all_common + '_Geo'
            nose_side_loc_name = nose_side_all_common + '_LOC'

            cmds.select(eye_geo_name, eye_loc_name, main_loc_name, crv_name, add=True)
            if cmds.objExists(nose_side_geo_name):
                cmds.select(nose_side_geo_name, nose_side_loc_name, d=True)

            eye_common = self.prefix_name + '_R_Nose_Tem_' + str(self.val)
            eye_all_common = self.prefix_name + '_R_Nose_*_Tem_' + str(self.val)
            nose_side_all_common = self.prefix_name + '_R_Nose_Side_*_Tem_' + str(self.val)

            eye_geo_name = eye_all_common + '_Geo'
            eye_loc_name = eye_all_common + '_LOC'
            main_loc_name = eye_common + '_Main_LOC'
            crv_name = eye_common + '_Crv'

            nose_side_geo_name = nose_side_all_common + '_Geo'
            nose_side_loc_name = nose_side_all_common + '_LOC'

            cmds.select(eye_geo_name, eye_loc_name, main_loc_name, crv_name, add=True)
            if cmds.objExists(nose_side_geo_name):
                cmds.select(nose_side_geo_name, nose_side_loc_name, d=True)

            sel_geo = cmds.ls(sl=True)

        vis = cmds.getAttr(sel_geo[0] + '.v')
        if vis == True:
            a = 0
            while a < len(sel_geo):
                cmds.setAttr((sel_geo[a] + '.v'), 0)
                a += 1
            self.nose_vis_button.setStyleSheet("background-color:rgb(255,0,0)")
        else:
            a = 0
            while a < len(sel_geo):
                cmds.setAttr((sel_geo[a] + '.v'), 1)
                a += 1
            self.nose_vis_button.setStyleSheet("background-color:rgb(0,255,0)")

        cmds.select(cl=True)

    def for_head_check_box_def(self):
        # get the value
        self.for_head_check_box_query = self.for_head_check_box.isChecked()
        if self.for_head_check_box_query == True:
            self.for_head_label.show()
            self.for_head_line_edit.show()
            self.for_head_vis_button.show()
        else:
            self.for_head_label.hide()
            self.for_head_line_edit.hide()
            self.for_head_vis_button.hide()

    def mouth_check_box_def(self):
        # get the value
        self.mouth_check_box_query = self.mouth_check_box.isChecked()
        if self.mouth_check_box_query == True:
            self.mouth_label.show()
            self.mouth_line_edit.show()
            self.mouth_vis_button.show()
        else:
            self.mouth_label.hide()
            self.mouth_line_edit.hide()
            self.mouth_vis_button.hide()

    def mouth_side_check_box_def(self):
        # get the value
        self.mouth_side_check_box_query = self.mouth_side_check_box.isChecked()
        if self.mouth_side_check_box_query == True:
            self.mouth_side_label.show()
            self.mouth_side_line_edit.show()
            self.mouth_side_vis_button.show()
        else:
            self.mouth_side_label.hide()
            self.mouth_side_line_edit.hide()
            self.mouth_side_vis_button.hide()

    def mouth_side_2_check_box_def(self):
        self.mouth_side_2_check_box_query = self.mouth_side_2_check_box.isChecked()
        if self.mouth_side_2_check_box_query == True:
            self.mouth_side_2_label.show()
            self.mouth_side_2_line_edit.show()
            self.mouth_side_2_vis_button.show()
            self.mouth_side_2_mirror_check_box.show()
            self.mouth_side_2_left_check_box.show()
            self.mouth_side_2_right_check_box.show()
        else:
            self.mouth_side_2_label.hide()
            self.mouth_side_2_line_edit.hide()
            self.mouth_side_2_vis_button.hide()
            self.mouth_side_2_mirror_check_box.hide()
            self.mouth_side_2_left_check_box.hide()
            self.mouth_side_2_right_check_box.hide()

    def face_center_check_box_def(self):
        self.face_center_check_box_query = self.face_center_check_box.isChecked()
        if self.face_center_check_box_query == True:
            self.face_center_label.show()
            self.face_center_line_edit.show()
            self.face_center_vis_button.show()
        else:
            self.face_center_label.hide()
            self.face_center_line_edit.hide()
            self.face_center_vis_button.hide()

    def for_head_vis_def(self):
        for_head_common = self.prefix_name + '_For_Head_*_Tem_' + str(self.val)
        for_head_geo = for_head_common + '_Geo'
        for_head_loc = for_head_common + '_LOC'
        crv_name = self.prefix_name + '_For_Head_Tem_' + str(self.val) + '_Crv'
        main_loc_name = self.prefix_name + '_For_Head_Tem_' + str(self.val) + '_Main_LOC'

        cmds.select(for_head_geo, for_head_loc, crv_name, main_loc_name)
        sel_geo = cmds.ls(sl=True)

        vis = cmds.getAttr(sel_geo[0] + '.v')
        if vis == True:
            a = 0
            while a < len(sel_geo):
                cmds.setAttr((sel_geo[a] + '.v'), 0)
                a += 1
            self.for_head_vis_button.setStyleSheet("background-color:rgb(255,0,0)")
        else:
            a = 0
            while a < len(sel_geo):
                cmds.setAttr((sel_geo[a] + '.v'), 1)
                a += 1
            self.for_head_vis_button.setStyleSheet("background-color:rgb(0,255,0)")

        cmds.select(cl=True)

    def mouth_vis_def(self):
        mouth_common = self.prefix_name + '_Mouth_*_Tem_' + str(self.val)
        mouth_side_common = self.prefix_name + '_Mouth_Side_*_Tem_' + str(self.val)

        mouth_geo = mouth_common + '_Geo'
        mouth_loc = mouth_common + '_LOC'

        mouth_side_geo = mouth_side_common + '_Geo'
        mouth_side_loc = mouth_side_common + '_LOC'

        crv_name = self.prefix_name + '_Mouth_Tem_' + str(self.val) + '_Crv'
        main_loc_name = self.prefix_name + '_Mouth_Tem_' + str(self.val) + '_Main_LOC'

        cmds.select(mouth_geo, mouth_loc, crv_name, main_loc_name)
        if cmds.objExists(mouth_side_geo):
            cmds.select(mouth_side_geo, mouth_side_loc, d=True)
        sel_geo = cmds.ls(sl=True)

        vis = cmds.getAttr(sel_geo[0] + '.v')
        if vis == True:
            a = 0
            while a < len(sel_geo):
                cmds.setAttr((sel_geo[a] + '.v'), 0)
                a += 1
            self.mouth_vis_button.setStyleSheet("background-color:rgb(255,0,0)")
        else:
            a = 0
            while a < len(sel_geo):
                cmds.setAttr((sel_geo[a] + '.v'), 1)
                a += 1
            self.mouth_vis_button.setStyleSheet("background-color:rgb(0,255,0)")

        cmds.select(cl=True)

    def mouth_side_vis_def(self):
        mouth_side_common = self.prefix_name + '_Mouth_Side_*_Tem_' + str(self.val)

        mouth_geo = mouth_side_common + '_Geo'
        mouth_loc = mouth_side_common + '_LOC'

        crv_name = self.prefix_name + '_Mouth_Side_Tem_' + str(self.val) + '_Crv'
        main_loc_name = self.prefix_name + '_Mouth_Side_Tem_' + str(self.val) + '_Main_LOC'

        cmds.select(mouth_geo, mouth_loc, crv_name, main_loc_name)

        sel_geo = cmds.ls(sl=True)

        vis = cmds.getAttr(sel_geo[0] + '.v')
        if vis == True:
            a = 0
            while a < len(sel_geo):
                cmds.setAttr((sel_geo[a] + '.v'), 0)
                a += 1
            self.mouth_side_vis_button.setStyleSheet("background-color:rgb(255,0,0)")
        else:
            a = 0
            while a < len(sel_geo):
                cmds.setAttr((sel_geo[a] + '.v'), 1)
                a += 1
            self.mouth_side_vis_button.setStyleSheet("background-color:rgb(0,255,0)")

        cmds.select(cl=True)

    def mouth_side_2_vis_def(self):
        l_side_2_loc = self.prefix_name + '_L_Mouth_Side_2_1_Tem_' + str(self.val) + "_LOC"
        r_side_2_loc = self.prefix_name + '_R_Mouth_Side_2_1_Tem_' + str(self.val) + "_LOC"

        if cmds.objExists(l_side_2_loc):
            l_side_2_all_common = self.prefix_name + '_L_Mouth_Side_2_*_Tem_' + str(self.val)
            l_side_2_geo_all = l_side_2_all_common + '_Geo'
            l_side_2_all_loc = l_side_2_all_common + '_LOC'
            main_common = self.prefix_name + '_L_Mouth_Side_2_Tem_' + str(self.val)
            main_loc = main_common + '_Main_LOC'
            crv_name = main_common + '_Crv'
            cmds.select(l_side_2_geo_all, l_side_2_all_loc, main_loc, crv_name)

        if cmds.objExists(r_side_2_loc):
            r_side_2_all_common = self.prefix_name + '_R_Mouth_Side_2_*_Tem_' + str(self.val)
            r_side_2_geo_all = r_side_2_all_common + '_Geo'
            r_side_2_all_loc = r_side_2_all_common + '_LOC'
            main_common = self.prefix_name + '_R_Mouth_Side_2_Tem_' + str(self.val)
            main_loc = main_common + '_Main_LOC'
            crv_name = main_common + '_Crv'
            cmds.select(r_side_2_geo_all, r_side_2_all_loc, main_loc, crv_name, add=True)

        sel_obj = cmds.ls(sl=True)
        vis = cmds.getAttr(sel_obj[0] + '.v')
        if vis == True:
            a = 0
            while a < len(sel_obj):
                cmds.setAttr((sel_obj[a] + '.v'), 0)
                a += 1
            self.mouth_side_2_vis_button.setStyleSheet("background-color:rgb(255,0,0)")
        else:
            a = 0
            while a < len(sel_obj):
                cmds.setAttr((sel_obj[a] + '.v'), 1)
                a += 1
            self.mouth_side_2_vis_button.setStyleSheet("background-color:rgb(0,255,0)")

        cmds.select(cl=True)

    def face_center_vis_def(self):
        # Template_Face_Center_1_Tem_1_LOC
        face_center_common = self.prefix_name + '_Face_Center_*_Tem_' + str(self.val)

        face_center_geo = face_center_common + '_Geo'
        face_center_loc = face_center_common + '_LOC'

        crv_name = self.prefix_name + '_Face_Center_Tem_' + str(self.val) + '_Crv'
        main_loc_name = self.prefix_name + '_Face_Center_Tem_' + str(self.val) + '_Main_LOC'

        cmds.select(face_center_geo, face_center_loc, crv_name, main_loc_name)

        sel_geo = cmds.ls(sl=True)

        vis = cmds.getAttr(sel_geo[0] + '.v')
        if vis == True:
            a = 0
            while a < len(sel_geo):
                cmds.setAttr((sel_geo[a] + '.v'), 0)
                a += 1
            self.face_center_vis_button.setStyleSheet("background-color:rgb(255,0,0)")
        else:
            a = 0
            while a < len(sel_geo):
                cmds.setAttr((sel_geo[a] + '.v'), 1)
                a += 1
            self.face_center_vis_button.setStyleSheet("background-color:rgb(0,255,0)")

        cmds.select(cl=True)

    def face_update_button_def(self):
        # now check the eye radio button
        # EYE
        if self.eye_radio_button.isChecked():
            value = 0
        elif self.eye_side_radio_button.isChecked():
            value = 1
        elif self.eye_side_2_radio_button.isChecked():
            value = 2

        # GET THE LINE EDIT
        self.eyes = int(self.eye_line_edit.text())
        if value == 0:
            left_check_box_query = self.eye_left_check_box.isChecked()
            right_check_box_query = self.eye_right_check_box.isChecked()
            if left_check_box_query == True:
                self.eye_update('L')
                # CHECK IF MIRRR IS ON
                mirror_checkbox = self.eye_mirror_check_box.isChecked()
                if mirror_checkbox == True:
                    self.eye_update('R')
                    self.mirror_value()
            elif right_check_box_query == True:
                self.eye_update('R')

        elif value == 1:
            left_check_box_query = self.eye_left_check_box.isChecked()
            right_check_box_query = self.eye_right_check_box.isChecked()
            if left_check_box_query == True:
                self.eye_side_update('L')
                # CHECK IF MIRRR IS ON
                mirror_checkbox = self.eye_mirror_check_box.isChecked()
                if mirror_checkbox == True:
                    self.eye_side_update('R')
                    self.mirror_value()
            elif right_check_box_query == True:
                self.eye_side_update('R')

        elif value == 2:
            left_check_box_query = self.eye_left_check_box.isChecked()
            right_check_box_query = self.eye_right_check_box.isChecked()
            if left_check_box_query == True:
                self.eye_side_2_update('L')
                # CHECK IF MIRRR IS ON
                mirror_checkbox = self.eye_mirror_check_box.isChecked()
                if mirror_checkbox == True:
                    self.eye_side_2_update('R')
                    self.mirror_value()
            elif right_check_box_query == True:
                self.eye_side_2_update('R')

        # FOR HEAD
        if self.for_head_check_box_query == True:
            for_head_value = int(self.for_head_line_edit.text())
            for_head_common = self.prefix_name + '_For_Head_*_Tem_' + str(self.val)
            for_head_geo = for_head_common + '_Geo'
            for_head_loc = for_head_common + '_LOC'
            crv_name = self.prefix_name + '_For_Head_Tem_' + str(self.val) + '_Crv'
            main_loc_name = self.prefix_name + '_For_Head_Tem_' + str(self.val) + '_Main_LOC'

            cmds.select(for_head_geo)
            sel_geo = cmds.ls(sl=True)

            if for_head_value != len(sel_geo):
                # create a new forhead
                cmds.select(for_head_geo, for_head_loc, crv_name, main_loc_name)
                cmds.delete()

                self.for_head_line_edit_query = for_head_value
                # self.for_head_def()
                # self.final_group()

                pass

        pass

    def eye_update(self, side):
        eye_common = self.prefix_name + '_' + side + '_Eye_Tem_' + str(self.val)
        eye_all_common = self.prefix_name + '_' + side + '_Eye_*_Tem_' + str(self.val)
        eye_side_common = self.prefix_name + '_' + side + '_Eye_Side_*_Tem_' + str(self.val)
        eye_side_2_common = self.prefix_name + '_' + side + '_Eye_Side_2_*_Tem_' + str(self.val)

        # get the mirror grp common name
        if side == 'L':
            name = 'right_to_left'
        else:
            name = 'left_to_right'

        eye_geo_name = eye_all_common + '_Geo'
        eye_loc_name = eye_all_common + '_LOC'
        eye_loc_mirror = eye_loc_name + '_' + name + '_Mirror_Grp'
        eye_clu_name = eye_all_common + '_CluHandle'
        main_loc_name = eye_common + '_Main_LOC'
        crv_name = eye_common + '_Crv'

        eye_side_geo = eye_side_common + '_Geo'
        eye_side_loc = eye_side_common + '_LOC'
        eye_side_mirror_loc = eye_side_loc + '_' + name + '_Mirror_Grp'
        eye_side_clu_name = eye_side_common + '_CluHandle'

        eye_side_2_geo = eye_side_2_common + '_Geo'
        eye_side_2_loc = eye_side_2_common + '_LOC'
        eye_side_2_mirror_loc = eye_side_2_loc + '_' + name + '_Mirror_Grp'
        eye_side_2_clu_name = eye_side_2_common + '_CluHandle'

        cmds.select(eye_geo_name)

        if cmds.objExists(eye_side_geo):
            cmds.select(eye_side_geo, d=True)
        if cmds.objExists(eye_side_2_geo):
            cmds.select(eye_side_2_geo, d=True)

        sel_geo = cmds.ls(sl=True)
        if len(sel_geo) != self.eyes:
            # get the position
            get_trans = cmds.xform(main_loc_name, q=1, ws=1, rp=1)

            cmds.select(eye_geo_name, main_loc_name, crv_name, eye_clu_name, add=True)
            if cmds.objExists(eye_loc_mirror):
                cmds.select(eye_loc_mirror, add=True)
            else:
                cmds.select(eye_loc_name, add=True)

            # DESELECT THE EYE SIDE
            if cmds.objExists(eye_side_geo):
                cmds.select(eye_side_geo, eye_side_clu_name, d=True)
                if cmds.objExists(eye_side_mirror_loc):
                    cmds.select(eye_side_mirror_loc, d=True)
                else:
                    cmds.select(eye_side_loc, d=True)

            # DESELECT THE EYE SIDE 2
            if cmds.objExists(eye_side_2_geo):
                cmds.select(eye_side_2_geo, eye_side_2_clu_name, d=True)
                if cmds.objExists(eye_side_2_mirror_loc):
                    cmds.select(eye_side_2_mirror_loc, d=True)
                else:
                    cmds.select(eye_side_2_loc, d=True)

            cmds.delete()

            # create a eye
            self.face_side = side
            self.no_eye_line_edit_query = self.eyes

            self.eye_def()
            self.final_group()

    def eye_side_update(self, side):
        eye_common = self.prefix_name + '_' + side + '_Eye_Side_Tem_' + str(self.val)
        eye_side_common = self.prefix_name + '_' + side + '_Eye_Side_*_Tem_' + str(self.val)
        eye_side_2_common = self.prefix_name + '_' + side + '_Eye_Side_2_*_Tem_' + str(self.val)

        # get the mirror grp common name
        if side == 'L':
            name = 'right_to_left'
        else:
            name = 'left_to_right'

        # Template_L_Eye_Side_Tem_2_Main_LOC
        main_loc_name = eye_common + '_Main_LOC'
        crv_name = eye_common + '_Crv'

        eye_side_geo = eye_side_common + '_Geo'
        eye_side_loc = eye_side_common + '_LOC'
        eye_side_mirror_loc = eye_side_loc + '_' + name + '_Mirror_Grp'
        eye_side_clu_name = eye_side_common + '_CluHandle'

        eye_side_2_geo = eye_side_2_common + '_Geo'
        eye_side_2_loc = eye_side_2_common + '_LOC'
        eye_side_2_mirror_loc = eye_side_2_loc + '_' + name + '_Mirror_Grp'
        eye_side_2_clu_name = eye_side_2_common + '_CluHandle'

        cmds.select(eye_side_geo)

        if cmds.objExists(eye_side_2_geo):
            cmds.select(eye_side_2_geo, d=True)

        sel_geo = cmds.ls(sl=True)
        if len(sel_geo) != self.eyes:
            # get the position
            get_trans = cmds.xform(main_loc_name, q=1, ws=1, rp=1)

            cmds.select(eye_side_geo, main_loc_name, crv_name, eye_side_clu_name, add=True)
            if cmds.objExists(eye_side_mirror_loc):
                cmds.select(eye_side_mirror_loc, add=True)
            else:
                cmds.select(eye_side_loc, add=True)

            # DESELECT THE EYE SIDE 2
            if cmds.objExists(eye_side_2_geo):
                cmds.select(eye_side_2_geo, eye_side_2_clu_name, d=True)
                if cmds.objExists(eye_side_2_mirror_loc):
                    cmds.select(eye_side_2_mirror_loc, d=True)
                else:
                    cmds.select(eye_side_2_loc, d=True)

            cmds.delete()

            # create a eye
            self.face_side = side
            self.eye_side_line_edit_query = self.eyes

            self.eye_side_def()
            self.final_group()

    def eye_side_2_update(self, side):
        # Template_L_Eye_Side_2_1_Tem_1_LOC
        eye_common = self.prefix_name + '_' + side + '_Eye_Side_2_Tem_' + str(self.val)
        eye_all_common = self.prefix_name + '_' + side + '_Eye_Side_2_*_Tem_' + str(self.val)

        # get the mirror grp common name
        if side == 'L':
            name = 'right_to_left'
        else:
            name = 'left_to_right'

        # Template_L_Eye_Side_Tem_2_Main_LOC
        eye_geo_name = eye_all_common + '_Geo'
        eye_loc_name = eye_all_common + '_LOC'
        eye_loc_mirror = eye_loc_name + '_' + name + '_Mirror_Grp'
        eye_clu_name = eye_all_common + '_CluHandle'
        main_loc_name = eye_common + '_Main_LOC'
        crv_name = eye_common + '_Crv'

        cmds.select(eye_geo_name)

        sel_geo = cmds.ls(sl=True)
        if len(sel_geo) != self.eyes:
            # get the position
            get_trans = cmds.xform(main_loc_name, q=1, ws=1, rp=1)

            cmds.select(eye_geo_name, main_loc_name, crv_name, eye_clu_name, add=True)
            if cmds.objExists(eye_loc_mirror):
                cmds.select(eye_loc_mirror, add=True)
            else:
                cmds.select(eye_loc_name, add=True)

            cmds.delete()

            # create a eye
            self.face_side = side
            self.eye_side_2_line_edit_query = self.eyes

            self.eye_side_2_def()
            self.final_group()

    def make_refernce(self, curve_name):
        cmds.setAttr((curve_name + '.overrideEnabled'), 1)
        cmds.setAttr((curve_name + '.overrideDisplayType'), 2)

    def face_create(self):
        # get the no of the human main grp
        self.grp_list = ['Face_Grp']
        for each_grp in self.grp_list:
            # list of the all children
            if cmds.objExists(each_grp):
                children_list = cmds.listRelatives(each_grp, children=True)
                for each_child in children_list:
                    # get all the controller data
                    self.face_data(each_child)

                    # FINAL THE ARM
                    self.final_face_def()

    def face_data(self, main_grp_name):
        split_name = main_grp_name.split('_')
        # Template_Animal_Head_Tem_1_Main_Grp
        self.prefix_name = split_name[0]
        self.val = split_name[3]

        # get each ctrl position data
        self.get_each_pos_data(main_grp_name)

    def get_each_pos_data(self, main_grp_name):
        self.face_list = []
        ###########################################CHECK THE EYE
        # L EYE
        eye_main_loc = self.prefix_name + '_*_Eye_Tem_' + str(self.val) + '_Main_LOC'
        if cmds.objExists(eye_main_loc):
            cmds.select(eye_main_loc)
            sel_eye = cmds.ls(sl=True)
            for each in sel_eye:
                # find left
                find_l = each.find('L_')
                if find_l > 0:
                    l_eye_loc_name = self.prefix_name + '_L_Eye_Tem_' + str(self.val) + '_Loc_Grp'
                    # get the children of the object
                    self.l_eye_loc_list = cmds.listRelatives(l_eye_loc_name, c=True)
                    # Template_L_Eye_Ball_Tem_1_Main_LOC
                    self.l_eye_ball_name = self.prefix_name + '_L_Eye_Ball_Tem_' + str(self.val) + '_Main_LOC'
                    # Template_L_Eye_Tem_1_Upper_Close_Crv
                    self.l_eye_upper_close_crv_name = self.prefix_name + '_L_Eye_Tem_' + str(
                        self.val) + '_Upper_Close_Crv'
                    self.l_eye_lower_close_crv_name = self.prefix_name + '_L_Eye_Tem_' + str(
                        self.val) + '_Lower_Close_Crv'
                    self.face_list.append('L_Eye')
                find_r = each.find('R_')
                if find_r > 0:
                    r_eye_loc_name = self.prefix_name + '_R_Eye_Tem_' + str(self.val) + '_Loc_Grp'
                    # get the children of the object
                    self.r_eye_loc_list = cmds.listRelatives(r_eye_loc_name, c=True)
                    self.face_list.append('R_Eye')
                    eye_ball_name = self.prefix_name + '_L_Eye_Ball_Tem_' + str(self.val) + '_Main_LOC'
                    self.r_eye_ball_name = self.prefix_name + '_R_Eye_Ball_Tem_' + str(self.val) + '_Main_LOC'
                    self.r_eye_upper_close_crv_name = self.prefix_name + '_R_Eye_Tem_' + str(
                        self.val) + '_Upper_Close_Crv'
                    self.r_eye_lower_close_crv_name = self.prefix_name + '_R_Eye_Tem_' + str(
                        self.val) + '_Lower_Close_Crv'
                    self.r_eye_ball_pos, self.r_eye_ball_rot = self.helper_class.get_trans_rot(eye_ball_name)

        # L EYE SIDE
        eye_main_loc = self.prefix_name + '_*_Eye_Side_Tem_' + str(self.val) + '_Main_LOC'
        if cmds.objExists(eye_main_loc):
            cmds.select(eye_main_loc)
            sel_eye = cmds.ls(sl=True)
            for each in sel_eye:
                # find left
                find_l = each.find('L_')
                if find_l > 0:
                    # Template_L_Eye_Side_Tem_1_Loc_Grp
                    l_eye_loc_name = self.prefix_name + '_L_Eye_Side_Tem_' + str(self.val) + '_Loc_Grp'
                    # get the children of the object
                    self.l_eye_side_loc_list = cmds.listRelatives(l_eye_loc_name, c=True)
                    self.face_list.append('L_Eye_Side')
                find_r = each.find('R_')
                if find_r > 0:
                    r_eye_loc_name = self.prefix_name + '_R_Eye_Side_Tem_' + str(self.val) + '_Loc_Grp'
                    # get the children of the object
                    self.r_eye_side_loc_list = cmds.listRelatives(r_eye_loc_name, c=True)
                    self.face_list.append('R_Eye_Side')

        # L EYE SIDE 2
        eye_main_loc = self.prefix_name + '_*_Eye_Side_2_Tem_' + str(self.val) + '_Main_LOC'
        if cmds.objExists(eye_main_loc):
            cmds.select(eye_main_loc)
            sel_eye = cmds.ls(sl=True)
            for each in sel_eye:
                # find left
                find_l = each.find('L_')
                if find_l > 0:
                    # Template_L_Eye_Side_Tem_1_Loc_Grp
                    l_eye_loc_name = self.prefix_name + '_L_Eye_Side_2_Tem_' + str(self.val) + '_Loc_Grp'
                    # get the children of the object
                    self.l_eye_side_2_loc_list = cmds.listRelatives(l_eye_loc_name, c=True)
                    self.face_list.append('L_Eye_Side_2')
                find_r = each.find('R_')
                if find_r > 0:
                    r_eye_loc_name = self.prefix_name + '_R_Eye_Side_2_Tem_' + str(self.val) + '_Loc_Grp'
                    # get the children of the object
                    self.r_eye_side_2_loc_list = cmds.listRelatives(r_eye_loc_name, c=True)
                    self.face_list.append('R_Eye_Side_2')

        # NOSE
        # Template_L_Nose_Tem_1_Main_LOC
        main_loc = self.prefix_name + '_*_Nose_Tem_' + str(self.val) + '_Main_LOC'
        if cmds.objExists(main_loc):
            cmds.select(main_loc)
            sel_eye = cmds.ls(sl=True)
            for each in sel_eye:
                # find left
                find_l = each.find('L_')
                if find_l > 0:
                    # Template_L_Eye_Side_Tem_1_Loc_Grp
                    l_loc_name = self.prefix_name + '_L_Nose_Tem_' + str(self.val) + '_Loc_Grp'
                    # get the children of the object
                    self.l_nose_loc_list = cmds.listRelatives(l_loc_name, c=True)
                    self.face_list.append('L_Nose')
                find_r = each.find('R_')
                if find_r > 0:
                    r_loc_name = self.prefix_name + '_R_Nose_Tem_' + str(self.val) + '_Loc_Grp'
                    # get the children of the object
                    self.r_nose_loc_list = cmds.listRelatives(r_loc_name, c=True)
                    self.face_list.append('R_Nose')

        # NOSE SIDE
        # Template_L_Nose_Side_Tem_1_Main_LOC
        main_loc = self.prefix_name + '_*_Nose_Side_Tem_' + str(self.val) + '_Main_LOC'
        if cmds.objExists(main_loc):
            cmds.select(main_loc)
            sel_eye = cmds.ls(sl=True)
            for each in sel_eye:
                # find left
                find_l = each.find('L_')
                if find_l > 0:
                    # Template_L_Nose_Side_Tem_1_Loc_Grp
                    l_loc_name = self.prefix_name + '_L_Nose_Side_Tem_' + str(self.val) + '_Loc_Grp'
                    # get the children of the object
                    self.l_nose_side_loc_list = cmds.listRelatives(l_loc_name, c=True)
                    self.face_list.append('L_Nose_Side')
                find_r = each.find('R_')
                if find_r > 0:
                    r_loc_name = self.prefix_name + '_R_Nose_Side_Tem_' + str(self.val) + '_Loc_Grp'
                    # get the children of the object
                    self.r_nose_side_loc_list = cmds.listRelatives(r_loc_name, c=True)
                    self.face_list.append('R_Nose_Side')

        # FOREHEAD
        # Template_For_Head_Tem_1_Main_LOC
        main_loc = self.prefix_name + '_For_Head_Tem_' + str(self.val) + '_Main_LOC'
        if cmds.objExists(main_loc):
            # Template_For_Head_Tem_1_Loc_Grp
            loc_grp_name = self.prefix_name + '_For_Head_Tem_' + str(self.val) + '_Loc_Grp'
            self.for_head_loc_list = cmds.listRelatives(loc_grp_name, c=True)
            self.face_list.append('For_Head')

        # MOUTH
        # Template_Mouth_Tem_1_Main_LOC
        main_loc = self.prefix_name + '_Mouth_Tem_' + str(self.val) + '_Main_LOC'
        if cmds.objExists(main_loc):
            # Template_Mouth_Tem_1_Loc_Grp
            loc_grp_name = self.prefix_name + '_Mouth_Tem_' + str(self.val) + '_Loc_Grp'
            self.mouth_loc_list = cmds.listRelatives(loc_grp_name, c=True)
            self.face_list.append('Mouth')

        # MOUTH SIDE
        # Template_Mouth_Side_Tem_1_Main_LOC
        main_loc = self.prefix_name + '_Mouth_Side_Tem_' + str(self.val) + '_Main_LOC'
        if cmds.objExists(main_loc):
            # Template_Mouth_Side_Tem_1_Loc_Grp
            loc_grp_name = self.prefix_name + '_Mouth_Side_Tem_' + str(self.val) + '_Loc_Grp'
            self.mouth_side_loc_list = cmds.listRelatives(loc_grp_name, c=True)
            self.face_list.append('Mouth_Side')

        # MOUTH SIDE 2
        # Template_L_Mouth_Side_2_Tem_1_Main_LOC
        main_loc = self.prefix_name + '_*_Mouth_Side_2_Tem_' + str(self.val) + '_Main_LOC'
        if cmds.objExists(main_loc):
            cmds.select(main_loc)
            sel_eye = cmds.ls(sl=True)
            for each in sel_eye:
                # find left
                find_l = each.find('L_')
                if find_l > 0:
                    # Template_L_Nose_Side_Tem_1_Loc_Grp
                    l_loc_name = self.prefix_name + '_L_Mouth_Side_2_Tem_' + str(self.val) + '_Loc_Grp'
                    # get the children of the object
                    self.l_mouth_side_2_loc_list = cmds.listRelatives(l_loc_name, c=True)
                    self.face_list.append('L_Mouth_Side_2')
                find_r = each.find('R_')
                if find_r > 0:
                    r_loc_name = self.prefix_name + '_R_Mouth_Side_2_Tem_' + str(self.val) + '_Loc_Grp'
                    # get the children of the object
                    self.r_mouth_side_2_loc_list = cmds.listRelatives(r_loc_name, c=True)
                    self.face_list.append('R_Mouth_Side_2')

        # FACE CENTER
        # Template_Face_Center_Tem_1_Main_LOC
        main_loc = self.prefix_name + '_Face_Center_Tem_' + str(self.val) + '_Main_LOC'
        if cmds.objExists(main_loc):
            # Template_Face_Center_Tem_1_Loc_Grp
            loc_grp_name = self.prefix_name + '_Face_Center_Tem_' + str(self.val) + '_Loc_Grp'
            self.face_center_list = cmds.listRelatives(loc_grp_name, c=True)
            self.face_list.append('Face_Center')

    def final_face_def(self):
        # ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        for each in self.face_list:
            if each == 'L_Eye':
                self.eye_side = 'L'
                self.eye_create(self.eye_side, self.l_eye_loc_list, self.l_eye_ball_name,
                                self.l_eye_upper_close_crv_name, self.l_eye_lower_close_crv_name)
                pass

            if each == 'R_Eye':
                self.eye_side = 'R'
                self.eye_create(self.eye_side, self.r_eye_loc_list, self.r_eye_ball_name,
                                self.r_eye_upper_close_crv_name, self.r_eye_lower_close_crv_name)

            if each == 'L_Eye_Side':
                self.eye_side = 'L'
                self.side_create(self.eye_side, self.l_eye_side_loc_list, 'Eye_Side')

            if each == 'R_Eye_Side':
                self.eye_side = 'R'
                self.side_create(self.eye_side, self.r_eye_side_loc_list, 'Eye_Side')

            if each == 'L_Eye_Side_2':
                self.eye_side = 'L'
                self.side_create(self.eye_side, self.l_eye_side_2_loc_list, 'Eye_Side_2')

            if each == 'R_Eye_Side_2':
                self.eye_side = 'R'
                self.side_create(self.eye_side, self.r_eye_side_2_loc_list, 'Eye_Side_2')

            if each == 'L_Nose':
                self.nose_side = 'L'
                self.nose_create(self.nose_side)

            if each == 'R_Nose':
                self.nose_side = 'R'
                self.nose_create(self.nose_side)

            if each == 'L_Nose_Side':
                self.nose_side = 'L'
                self.nose_side_final(self.nose_side)

            if each == 'R_Nose_Side':
                self.nose_side = 'R'
                self.nose_side_final(self.nose_side)

            if each == 'For_Head':
                print('this is the for Head')
                self.for_head_final_def()

            if each == 'Mouth':
                self.mouth_final_def()

            if each == 'Mouth_Side':
                self.mouth_side_final_def()

            if each == 'L_Mouth_Side_2':
                self.mouth_side = 'L'
                self.mouth_side_2_final(self.mouth_side)

            if each == 'R_Mouth_Side_2':
                self.mouth_side = 'R'
                self.mouth_side_2_final(self.mouth_side)

            if each == 'Face_Center':
                self.face_center_final()

    def eye_create(self, eye_side, loc_list, eye_ball_name, upper_curve_close_name, lower_curve_close_name):
        # Create a Curve
        # curve -d 1 -p 2.328 10.155 8.545 -p 2.450194 11.594288 8.809421 -p 3.275888 12.803976 9.002793 -p 4.621617 13.41431 8.994136 -p 6.000889 13.6422 8.711704 -p 7.281418 13.317525 8.043427 -p 8.201923 12.501901 7.150285 -p 8.604954 11.392094 6.599563 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;
        self.upper_eye_pos_list = {}

        a = 0
        while a < len(loc_list):
            loc_common = self.prefix_name + '_' + eye_side + '_Eye_' + str(a + 1) + '_Tem_' + str(self.val)
            loc_name = loc_common + '_LOC'
            get_trans, get_rot = self.helper_class.get_trans_rot(loc_name)
            self.upper_eye_pos_list[loc_name] = get_trans
            a += 1
        loc_common = self.prefix_name + '_' + eye_side + '_Eye_' + str(len(loc_list) + 1) + '_Tem_' + str(self.val)
        loc_name = loc_common + '_LOC'
        first_loc_common = self.prefix_name + '_' + eye_side + '_Eye_1_Tem_' + str(self.val)
        first_loc_name = first_loc_common + '_LOC'
        get_trans, get_rot = self.helper_class.get_trans_rot(first_loc_name)
        self.upper_eye_pos_list[loc_name] = get_trans

        # get the no of the loc
        total_loc = len(loc_list)
        minus_two = total_loc - 2
        divide_by_two = minus_two / 2
        last_upper_no = divide_by_two + 1
        upper_list = 1 + last_upper_no
        a = 0
        upper_curve_pos_list = []
        upper_curve_k_val = []
        while a < upper_list:
            loc_common = self.prefix_name + '_' + eye_side + '_Eye_' + str(a + 1) + '_Tem_' + str(self.val)
            loc_name = loc_common + '_LOC'
            pos_val = self.upper_eye_pos_list[loc_name]
            upper_curve_pos_list.append(pos_val)
            number = a
            upper_curve_k_val.append(number)
            a += 1

        upper_curve_name = self.prefix_name + '_' + eye_side + '_Eye_Upper_Tem_' + str(self.val) + '_Crv'
        upper_curve_shape_name = upper_curve_name + 'Shape'
        cmds.curve(n=upper_curve_name, d=0, p=upper_curve_pos_list,
                   k=upper_curve_k_val)
        shape_name = cmds.listRelatives(upper_curve_name, s=True)
        cmds.rename(shape_name[0], upper_curve_shape_name)

        a = 0
        lower_curve_pos_list = []
        lower_curve_k_val = []
        while a < upper_list:
            loc_common = self.prefix_name + '_' + eye_side + '_Eye_' + str(a + 1 + last_upper_no) + '_Tem_' + str(
                self.val)
            loc_name = loc_common + '_LOC'

            pos_val = self.upper_eye_pos_list[loc_name]
            lower_curve_pos_list.append(pos_val)
            number = a
            lower_curve_k_val.append(number)

            a += 1
        lower_curve_name = self.prefix_name + '_' + eye_side + '_Eye_Lower_Tem_' + str(self.val) + '_Crv'
        lower_curve_shape_name = lower_curve_name + 'Shape'
        cmds.curve(n=lower_curve_name, d=0, p=lower_curve_pos_list,
                   k=lower_curve_k_val)
        shape_name = cmds.listRelatives(lower_curve_name, s=True)
        cmds.rename(shape_name[0], lower_curve_shape_name)
        # make a Curve Group
        crv_grp_name = self.prefix_name + '_' + eye_side + '_Eye_Tem_' + str(self.val) + '_Crv_Grp'
        cmds.select(upper_curve_name, lower_curve_name)
        cmds.group(n=crv_grp_name)

        new_val = 0
        a = 0
        ctrl_list = []
        while a < len(loc_list):
            # Template_L_Eye_3_Tem_1_LOC
            loc_common = self.prefix_name + '_' + eye_side + '_Eye_' + str(a + 1) + '_Tem_' + str(self.val)
            loc_name = loc_common + '_LOC'
            get_trans, get_rot = self.helper_class.get_trans_rot(loc_name)
            get_eye_ball_trans, get_eye_ball_rot = self.helper_class.get_trans_rot(eye_ball_name)

            tem_remove_name = self.helper_class.remove_tem(loc_common)

            # Create a Locator and set the position
            new_loc_name = tem_remove_name + '_Loc'
            cmds.spaceLocator(n=new_loc_name, p=(0, 0, 0))
            cmds.move(get_trans[0], get_trans[1], get_trans[2])
            cmds.select(new_loc_name)
            cmds.CenterPivot()

            # Create a Joint on the each loc and center position

            jnt_start_name = tem_remove_name + '_Start_Jnt'
            jnt_end_name = tem_remove_name + '_End_Jnt'
            cmds.select(cl=True)
            cmds.joint(n=jnt_start_name, p=(get_trans[0],
                                            get_trans[1],
                                            get_trans[2]))
            cmds.select(cl=True)
            cmds.joint(n=jnt_end_name, p=(get_eye_ball_trans[0],
                                          get_eye_ball_trans[1],
                                          get_eye_ball_trans[2]))

            cmds.select(jnt_start_name, jnt_end_name)
            cmds.parent()

            # Create a Sphere
            sphere_name = tem_remove_name + '_Secondary_Ctrl'
            ctrl_list.append(sphere_name)
            sphere_grp = sphere_name + '_Grp'
            cmds.polySphere(r=0.3, sx=6, sy=6, ax=(0, 1, 0), cuv=2, ch=1, n=sphere_name)
            cmds.move(get_trans[0], get_trans[1], get_trans[2])
            cmds.DeleteHistory()
            cmds.FreezeTransformations()
            cmds.select(sphere_name)
            cmds.group(n=sphere_grp)
            cmds.aimConstraint(sphere_name, jnt_end_name, mo=True)
            # Create a Plus Minus
            plus_minus_name = tem_remove_name + '_Plus_Minus'
            cmds.createNode('plusMinusAverage', n=plus_minus_name)
            mel.eval('AEnewNonNumericMultiAddNewItem("%s","input3D");' % plus_minus_name)
            mel.eval('AEnewNonNumericMultiAddNewItem("%s","input3D");' % plus_minus_name)
            cmds.connectAttr((new_loc_name + '.translate'), (plus_minus_name + '.input3D[0]'))
            cmds.setAttr((plus_minus_name + '.operation'), 2)
            cmds.setAttr((plus_minus_name + '.input3D[1].input3Dx'), get_trans[0])
            cmds.setAttr((plus_minus_name + '.input3D[1].input3Dy'), get_trans[1])
            cmds.setAttr((plus_minus_name + '.input3D[1].input3Dz'), get_trans[2])
            cmds.connectAttr((plus_minus_name + '.output3D'), (sphere_grp + '.translate'))

            ##Create a point on Curve
            poc_name = tem_remove_name + '_POC'
            cmds.createNode('pointOnCurveInfo', n=poc_name)
            cmds.connectAttr((poc_name + '.position'),
                             (new_loc_name + '.translate'),
                             f=True)

            # add the curve in the poc and set the value
            if a <= 6:
                cmds.connectAttr((upper_curve_shape_name + '.worldSpace[0]'), (poc_name + '.inputCurve'))
                # setAttr "Template_L_Eye_3_1_POC.parameter" 2;
                cmds.setAttr((poc_name + '.parameter'), a)
            else:
                cmds.connectAttr((lower_curve_shape_name + '.worldSpace[0]'), (poc_name + '.inputCurve'))
                cmds.setAttr((poc_name + '.parameter'), new_val)
                new_val += 1

            grp_common = self.prefix_name + '_' + eye_side + '_Eye_' + str(self.val)
            loc_grp_name = grp_common + '_Loc_Grp'
            if cmds.objExists(loc_grp_name):
                cmds.select(new_loc_name, loc_grp_name)
                cmds.parent()
            else:
                cmds.select(new_loc_name)
                cmds.group(n=loc_grp_name)

            jnt_grp_name = grp_common + '_Jnt_Grp'
            if cmds.objExists(jnt_grp_name):
                cmds.select(jnt_end_name, jnt_grp_name)
                cmds.parent()
            else:
                cmds.select(jnt_end_name)
                cmds.group(n=jnt_grp_name)

            sphere_grp_name = grp_common + '_Secondary_Ctrl_Grp'
            if cmds.objExists(sphere_grp_name):
                cmds.select(sphere_grp, sphere_grp_name)
                cmds.parent()
            else:
                cmds.select(sphere_grp)
                cmds.group(n=sphere_grp_name)

            a += 1

        # now make a smooth curve
        # rebuildCurve -ch 1 -rpo 1 -rt 0 -end 1 -kr 0 -kcp 0 -kep 1 -kt 0 -s 3 -d 2 -tol 0.01 "Template_L_Eye_Upper_Tem_1_Crv1";
        upper_curve_smooth_name = self.prefix_name + '_' + eye_side + '_Eye_Upper_Tem_' + str(self.val) + '_Smooth_Crv'
        upper_curve_smooth_shape_name = upper_curve_smooth_name + 'Shape'
        upper_curve_wire_name = self.prefix_name + '_' + eye_side + '_Eye_Upper_Tem_' + str(self.val) + '_Wire'
        cmds.select(upper_curve_name)
        cmds.duplicate(n=upper_curve_smooth_name)
        cmds.rebuildCurve(upper_curve_smooth_name, ch=0,
                          rpo=1, rt=0, end=1, kr=0, kcp=0, kep=1, kt=0, d=2, tol=0.01, s=3)
        # Create a Wire Const
        cmds.select(upper_curve_name, upper_curve_smooth_name)
        mel.eval('wire -gw false -en 1.000000 -ce 0.000000 -li 0.000000 -w %s %s;' % (
        upper_curve_smooth_name, upper_curve_name))
        list = cmds.listConnections(upper_curve_smooth_shape_name, type='wire')
        cmds.rename(list[0], upper_curve_wire_name)

        lower_curve_smooth_name = self.prefix_name + '_' + eye_side + '_Eye_Lower_Tem_' + str(self.val) + '_Smooth_Crv'
        lower_curve_smooth_shape_name = lower_curve_smooth_name + 'Shape'
        lower_curve_wire_name = self.prefix_name + '_' + eye_side + '_Eye_Lower_Tem_' + str(self.val) + '_Wire'
        cmds.select(lower_curve_name)
        cmds.duplicate(n=lower_curve_smooth_name)
        cmds.rebuildCurve(lower_curve_smooth_name, ch=0,
                          rpo=1, rt=0, end=1, kr=0, kcp=0, kep=1, kt=0, d=2, tol=0.01, s=3)
        # Create a Wire Const
        cmds.select(lower_curve_name, lower_curve_smooth_name)
        mel.eval('wire -gw false -en 1.000000 -ce 0.000000 -li 0.000000 -w %s %s;' % (
        lower_curve_smooth_name, lower_curve_name))
        list = cmds.listConnections(lower_curve_smooth_shape_name, type='wire')
        cmds.rename(list[0], lower_curve_wire_name)

        # Select all the smooth cv
        cmds.select(upper_curve_close_name + '.cv[0:]')
        upper_curve_close_cv_list = cmds.ls(sl=True, fl=True)
        pos_list = []
        for each_cv in upper_curve_close_cv_list:
            pos_val = cmds.pointPosition(each_cv)
            pos_list.append(pos_val)

        upper_smooth_close_name = self.prefix_name + '_' + eye_side + '_Eye_Upper_' + str(
            self.val) + '_Smooth_Close_Crv'
        upper_smooth_close_shape_name = upper_smooth_close_name + 'Shape'
        cmds.curve(n=upper_smooth_close_name, d=2, p=pos_list,
                   k=[0, 0, 1, 2, 3, 3])
        shape_name = cmds.listRelatives(upper_smooth_close_name, s=True)
        cmds.rename(shape_name[0], upper_smooth_close_shape_name)
        cmds.setAttr((upper_smooth_close_name + '.v'), 0)

        cmds.select(lower_curve_close_name + '.cv[0:]')
        lower_curve_close_cv_list = cmds.ls(sl=True, fl=True)
        pos_list = []
        a = 0
        value = -1
        while a < len(lower_curve_close_cv_list):
            pos_val = cmds.pointPosition(lower_curve_close_cv_list[value])
            pos_list.append(pos_val)
            value -= 1
            a += 1

        lower_smooth_close_name = self.prefix_name + '_' + eye_side + '_Eye_Lower_' + str(
            self.val) + '_Smooth_Close_Crv'
        lower_smooth_close_shape_name = lower_smooth_close_name + 'Shape'
        cmds.curve(n=lower_smooth_close_name, d=2, p=pos_list,
                   k=[0, 0, 1, 2, 3, 3])
        shape_name = cmds.listRelatives(lower_smooth_close_name, s=True)
        cmds.rename(shape_name[0], lower_smooth_close_shape_name)
        cmds.setAttr((lower_smooth_close_name + '.v'), 0)

        # Create a Blendshape
        cmds.select(upper_smooth_close_name, upper_curve_smooth_name)
        upper_curve_smooth_Blend = self.prefix_name + '_' + eye_side + '_Eye_Upper_' + str(self.val) + '_Blend'
        cmds.blendShape(n=upper_curve_smooth_Blend)

        cmds.select(lower_smooth_close_name, lower_curve_smooth_name)
        lower_curve_smooth_Blend = self.prefix_name + '_' + eye_side + '_Eye_Lower_' + str(self.val) + '_Blend'
        cmds.blendShape(n=lower_curve_smooth_Blend)

        self.controller_class.eye_rig_ctrl(eye_side)
        # snap to the ball and move towards side
        if eye_side == 'L':
            cmds.select(eye_side + '_Eye_Main_Ctrl')
            cmds.move(get_eye_ball_trans[0],
                      get_eye_ball_trans[1],
                      get_eye_ball_trans[2], r=True)
            cmds.move(6, 0, 0, r=True)
        else:
            cmds.select(eye_side + '_Eye_Main_Ctrl')
            cmds.move(get_eye_ball_trans[0],
                      get_eye_ball_trans[1],
                      get_eye_ball_trans[2], r=True)
            cmds.move(-6, 0, 0, r=True)

        cmds.select(upper_smooth_close_name, lower_smooth_close_name, crv_grp_name)
        cmds.parent()

        eye_blink_name = eye_side + '_Eye_Blink_Ctrl'
        cmds.setAttr((eye_blink_name + '.ty'), 1)
        cmds.setAttr((upper_curve_smooth_Blend + '.' + upper_smooth_close_name), 0)
        cmds.setAttr((lower_curve_smooth_Blend + '.' + lower_smooth_close_name), 0)
        cmds.setDrivenKeyframe((upper_curve_smooth_Blend + '.' + upper_smooth_close_name),
                               currentDriver=(eye_blink_name + '.ty'))
        cmds.setDrivenKeyframe((lower_curve_smooth_Blend + '.' + lower_smooth_close_name),
                               currentDriver=(eye_blink_name + '.ty'))

        cmds.setAttr((eye_blink_name + '.ty'), 0)
        cmds.setAttr((upper_curve_smooth_Blend + '.' + upper_smooth_close_name), 1)
        cmds.setAttr((lower_curve_smooth_Blend + '.' + lower_smooth_close_name), 1)
        cmds.setDrivenKeyframe((upper_curve_smooth_Blend + '.' + upper_smooth_close_name),
                               currentDriver=(eye_blink_name + '.ty'))
        cmds.setDrivenKeyframe((lower_curve_smooth_Blend + '.' + lower_smooth_close_name),
                               currentDriver=(eye_blink_name + '.ty'))
        cmds.setAttr((eye_blink_name + '.ty'), 1)

        # EYE side Crv
        upper_curve_eye_side_smooth_name = self.prefix_name + '_' + eye_side + '_Eye_Upper_Side_1_Tem_' + str(
            self.val) + '_Smooth_Crv'
        upper_curve_eye_slide_smooth_shape_name = upper_curve_eye_side_smooth_name + 'Shape'
        cmds.select(upper_curve_smooth_name)
        cmds.duplicate(n=upper_curve_eye_side_smooth_name)
        # select the cv and move to the relative value
        cmds.select(upper_curve_eye_side_smooth_name + '.cv[1]')
        cmds.move(0, -0.8, 0, r=True)
        cmds.select(upper_curve_eye_side_smooth_name + '.cv[2]')
        cmds.move(0, -0.3, 0, r=True)
        # blendShape -e  -t Template_L_Eye_Lower_Tem_1_Smooth_Crv 1 Template_L_Eye_Lower_Tem_1_Smooth_Crv1 1 Template_L_Eye_Lower_1_Blend;
        mel.eval('blendShape -e  -t %s 2 %s 1 %s;' % (
        upper_curve_smooth_name, upper_curve_eye_side_smooth_name, upper_curve_smooth_Blend))
        cmds.setAttr((upper_curve_eye_side_smooth_name + '.v'), 0)

        upper_curve_eye_side_2_smooth_name = self.prefix_name + '_' + eye_side + '_Eye_Upper_Side_2_Tem_' + str(
            self.val) + '_Smooth_Crv'
        upper_curve_eye_slide_2_smooth_shape_name = upper_curve_eye_side_2_smooth_name + 'Shape'
        cmds.select(upper_curve_smooth_name)
        cmds.duplicate(n=upper_curve_eye_side_2_smooth_name)
        # select the cv and move to the relative value
        cmds.select(upper_curve_eye_side_2_smooth_name + '.cv[3]')
        cmds.move(0, -0.8, 0, r=True)
        cmds.select(upper_curve_eye_side_2_smooth_name + '.cv[2]')
        cmds.move(0, -0.3, 0, r=True)
        # blendShape -e  -t Template_L_Eye_Lower_Tem_1_Smooth_Crv 1 Template_L_Eye_Lower_Tem_1_Smooth_Crv1 1 Template_L_Eye_Lower_1_Blend;
        mel.eval('blendShape -e  -t %s 3 %s 1 %s;' % (
        upper_curve_smooth_name, upper_curve_eye_side_2_smooth_name, upper_curve_smooth_Blend))
        cmds.setAttr((upper_curve_eye_side_2_smooth_name + '.v'), 0)

        eye_side_name = eye_side + '_Eye_Side_Ctrl'
        cmds.setAttr((eye_side_name + '.tx'), 0)
        cmds.setAttr((upper_curve_smooth_Blend + '.' + upper_curve_eye_side_smooth_name), 0)
        cmds.setAttr((upper_curve_smooth_Blend + '.' + upper_curve_eye_side_2_smooth_name), 0)
        cmds.setDrivenKeyframe((upper_curve_smooth_Blend + '.' + upper_curve_eye_side_smooth_name),
                               currentDriver=(eye_side_name + '.tx'))
        cmds.setDrivenKeyframe((upper_curve_smooth_Blend + '.' + upper_curve_eye_side_2_smooth_name),
                               currentDriver=(eye_side_name + '.tx'))

        cmds.setAttr((eye_side_name + '.tx'), 1)
        cmds.setAttr((upper_curve_smooth_Blend + '.' + upper_curve_eye_side_smooth_name), 1)
        cmds.setAttr((upper_curve_smooth_Blend + '.' + upper_curve_eye_side_2_smooth_name), 0)
        cmds.setDrivenKeyframe((upper_curve_smooth_Blend + '.' + upper_curve_eye_side_smooth_name),
                               currentDriver=(eye_side_name + '.tx'))
        cmds.setDrivenKeyframe((upper_curve_smooth_Blend + '.' + upper_curve_eye_side_2_smooth_name),
                               currentDriver=(eye_side_name + '.tx'))

        cmds.setAttr((eye_side_name + '.tx'), -1)
        cmds.setAttr((upper_curve_smooth_Blend + '.' + upper_curve_eye_side_smooth_name), 0)
        cmds.setAttr((upper_curve_smooth_Blend + '.' + upper_curve_eye_side_2_smooth_name), 1)
        cmds.setDrivenKeyframe((upper_curve_smooth_Blend + '.' + upper_curve_eye_side_smooth_name),
                               currentDriver=(eye_side_name + '.tx'))
        cmds.setDrivenKeyframe((upper_curve_smooth_Blend + '.' + upper_curve_eye_side_2_smooth_name),
                               currentDriver=(eye_side_name + '.tx'))
        cmds.setAttr((eye_side_name + '.tx'), 0)

        lower_curve_eye_side_smooth_name = self.prefix_name + '_' + eye_side + '_Eye_Lower_Side_1_Tem_' + str(
            self.val) + '_Smooth_Crv'
        lower_curve_eye_slide_smooth_shape_name = lower_curve_eye_side_smooth_name + 'Shape'
        cmds.select(lower_curve_smooth_name)
        cmds.duplicate(n=lower_curve_eye_side_smooth_name)
        # select the cv and move to the relative value
        cmds.select(lower_curve_eye_side_smooth_name + '.cv[1]')
        cmds.move(0, 0.8, 0, r=True)
        cmds.select(lower_curve_eye_side_smooth_name + '.cv[2]')
        cmds.move(0, 0.3, 0, r=True)
        mel.eval('blendShape -e  -t %s 2 %s 1 %s;' % (
        lower_curve_smooth_name, lower_curve_eye_side_smooth_name, lower_curve_smooth_Blend))
        cmds.setAttr((lower_curve_eye_side_smooth_name + '.v'), 0)

        lower_curve_eye_side_2_smooth_name = self.prefix_name + '_' + eye_side + '_Eye_Lower_Side_2_Tem_' + str(
            self.val) + '_Smooth_Crv'
        lower_curve_eye_slide_2_smooth_shape_name = lower_curve_eye_side_2_smooth_name + 'Shape'
        cmds.select(lower_curve_smooth_name)
        cmds.duplicate(n=lower_curve_eye_side_2_smooth_name)
        # select the cv and move to the relative value
        cmds.select(lower_curve_eye_side_2_smooth_name + '.cv[3]')
        cmds.move(0, 0.8, 0, r=True)
        cmds.select(lower_curve_eye_side_2_smooth_name + '.cv[2]')
        cmds.move(0, 0.3, 0, r=True)
        # blendShape -e  -t Template_L_Eye_Lower_Tem_1_Smooth_Crv 1 Template_L_Eye_Lower_Tem_1_Smooth_Crv1 1 Template_L_Eye_Lower_1_Blend;
        mel.eval('blendShape -e  -t %s 3 %s 1 %s;' % (
        lower_curve_smooth_name, lower_curve_eye_side_2_smooth_name, lower_curve_smooth_Blend))
        cmds.setAttr((lower_curve_eye_side_2_smooth_name + '.v'), 0)
        eye_side_name = eye_side + '_Eye_Side_Ctrl'

        cmds.setAttr((eye_side_name + '.tx'), 0)
        cmds.setAttr((lower_curve_smooth_Blend + '.' + lower_curve_eye_side_smooth_name), 0)
        cmds.setAttr((lower_curve_smooth_Blend + '.' + lower_curve_eye_side_2_smooth_name), 0)
        cmds.setDrivenKeyframe((lower_curve_smooth_Blend + '.' + lower_curve_eye_side_smooth_name),
                               currentDriver=(eye_side_name + '.tx'))
        cmds.setDrivenKeyframe((lower_curve_smooth_Blend + '.' + lower_curve_eye_side_2_smooth_name),
                               currentDriver=(eye_side_name + '.tx'))

        cmds.setAttr((eye_side_name + '.tx'), 1)
        cmds.setAttr((lower_curve_smooth_Blend + '.' + lower_curve_eye_side_smooth_name), 1)
        cmds.setAttr((lower_curve_smooth_Blend + '.' + lower_curve_eye_side_2_smooth_name), 0)
        cmds.setDrivenKeyframe((lower_curve_smooth_Blend + '.' + lower_curve_eye_side_smooth_name),
                               currentDriver=(eye_side_name + '.tx'))
        cmds.setDrivenKeyframe((lower_curve_smooth_Blend + '.' + lower_curve_eye_side_2_smooth_name),
                               currentDriver=(eye_side_name + '.tx'))

        cmds.setAttr((eye_side_name + '.tx'), -1)
        cmds.setAttr((lower_curve_smooth_Blend + '.' + lower_curve_eye_side_smooth_name), 0)
        cmds.setAttr((lower_curve_smooth_Blend + '.' + lower_curve_eye_side_2_smooth_name), 1)
        cmds.setDrivenKeyframe((lower_curve_smooth_Blend + '.' + lower_curve_eye_side_smooth_name),
                               currentDriver=(eye_side_name + '.tx'))
        cmds.setDrivenKeyframe((lower_curve_smooth_Blend + '.' + lower_curve_eye_side_2_smooth_name),
                               currentDriver=(eye_side_name + '.tx'))
        cmds.setAttr((eye_side_name + '.tx'), 0)

        pos_val = cmds.pointPosition((upper_curve_close_name + '.cv[1]'))
        upper_loc_1 = 'Upper_Loc_1'
        cmds.spaceLocator(n=upper_loc_1, p=(pos_val[0], pos_val[1], pos_val[2]))
        cmds.CenterPivot()
        pos_val = cmds.pointPosition((upper_curve_close_name + '.cv[2]'))
        upper_loc_2 = 'Upper_Loc_2'
        cmds.spaceLocator(n=upper_loc_2, p=(pos_val[0], pos_val[1], pos_val[2]))
        cmds.CenterPivot()
        pos_val = cmds.pointPosition((upper_curve_close_name + '.cv[3]'))
        upper_loc_3 = 'Upper_Loc_3'
        cmds.spaceLocator(n=upper_loc_3, p=(pos_val[0], pos_val[1], pos_val[2]))
        cmds.CenterPivot()

        pos_val = cmds.pointPosition((lower_curve_close_name + '.cv[1]'))
        lower_loc_1 = 'Lower_Loc_1'
        cmds.spaceLocator(n=lower_loc_1, p=(pos_val[0], pos_val[1], pos_val[2]))
        cmds.CenterPivot()
        pos_val = cmds.pointPosition((lower_curve_close_name + '.cv[2]'))
        lower_loc_2 = 'Lower_Loc_2'
        cmds.spaceLocator(n=lower_loc_2, p=(pos_val[0], pos_val[1], pos_val[2]))
        cmds.CenterPivot()
        pos_val = cmds.pointPosition((lower_curve_close_name + '.cv[3]'))
        lower_loc_3 = 'Lower_Loc_3'
        cmds.spaceLocator(n=lower_loc_3, p=(pos_val[0], pos_val[1], pos_val[2]))
        cmds.CenterPivot()

        middle_1_loc = 'Middle_Loc_1'
        cmds.spaceLocator(n=middle_1_loc, p=(0, 0, 0))
        cmds.parentConstraint(upper_loc_1, lower_loc_1, middle_1_loc, mo=False)
        middle_2_loc = 'Middle_Loc_2'
        cmds.spaceLocator(n=middle_2_loc, p=(0, 0, 0))
        cmds.parentConstraint(upper_loc_2, lower_loc_2, middle_2_loc, mo=False)
        middle_3_loc = 'Middle_Loc_3'
        cmds.spaceLocator(n=middle_3_loc, p=(0, 0, 0))
        cmds.parentConstraint(upper_loc_3, lower_loc_3, middle_3_loc, mo=False)

        # get the pos
        middle_loc_1_pos = cmds.getAttr(middle_1_loc + '.t')[0]
        middle_loc_2_pos = cmds.getAttr(middle_2_loc + '.t')[0]
        middle_loc_3_pos = cmds.getAttr(middle_3_loc + '.t')[0]

        loc_start_point_pos = cmds.pointPosition(upper_curve_smooth_name + '.cv[0]')
        loc_end_point_pos = cmds.pointPosition(upper_curve_smooth_name + '.cv[4]')

        # Delete all the loc
        cmds.select(upper_loc_1, upper_loc_2, upper_loc_3, lower_loc_1, lower_loc_2, lower_loc_3, middle_1_loc,
                    middle_2_loc, middle_3_loc)
        cmds.delete()

        eye_blink_close_wire_crv_name = self.prefix_name + '_' + eye_side + '_Eye_Close_Wire_Tem_' + str(
            self.val) + '_Crv'
        cmds.curve(n=eye_blink_close_wire_crv_name, d=2,
                   p=[(loc_start_point_pos[0], loc_start_point_pos[1], loc_start_point_pos[2]),
                      (middle_loc_1_pos[0], middle_loc_1_pos[1], middle_loc_1_pos[2]),
                      (middle_loc_2_pos[0], middle_loc_2_pos[1], middle_loc_2_pos[2]),
                      (middle_loc_3_pos[0], middle_loc_3_pos[1], middle_loc_3_pos[2]),
                      (loc_end_point_pos[0], loc_end_point_pos[1], loc_end_point_pos[2])],
                   k=[0, 0, 1, 2, 3, 3])
        cmds.select(eye_blink_close_wire_crv_name, crv_grp_name)
        cmds.parent()
        cmds.setAttr((eye_blink_close_wire_crv_name + '.v'), 0)

        eye_blink_open_wire_crv_name = self.prefix_name + '_' + eye_side + '_Eye_Open_Wire_Tem_' + str(
            self.val) + '_Crv'
        cmds.select(upper_curve_smooth_name)
        cmds.duplicate(n=eye_blink_open_wire_crv_name)
        cmds.setAttr((eye_blink_open_wire_crv_name + '.v'), 0)
        cmds.setAttr((eye_blink_name + '.ty'), 0)
        mel.eval('wire -gw false -en 1.000000 -ce 0.000000 -li 0.000000 -w %s %s;' % (
        eye_blink_close_wire_crv_name, upper_curve_name))
        mel.eval('wire -gw false -en 1.000000 -ce 0.000000 -li 0.000000 -w %s %s;' % (
        eye_blink_close_wire_crv_name, lower_curve_name))
        # Create a Wire deformer

        # Create a Blendshape
        eye_open_blend = self.prefix_name + '_' + eye_side + '_Eye_Open_Tem_' + str(self.val) + '_Blend'
        cmds.select(eye_blink_open_wire_crv_name, eye_blink_close_wire_crv_name)
        cmds.blendShape(n=eye_open_blend)

        cmds.setAttr((eye_blink_name + '.tx'), 0)
        cmds.setAttr((eye_open_blend + '.' + eye_blink_open_wire_crv_name), 0)
        cmds.setDrivenKeyframe((eye_open_blend + '.' + eye_blink_open_wire_crv_name),
                               currentDriver=(eye_blink_name + '.tx'))

        cmds.setAttr((eye_blink_name + '.tx'), -1)
        cmds.setAttr((eye_open_blend + '.' + eye_blink_open_wire_crv_name), 1)
        cmds.setDrivenKeyframe((eye_open_blend + '.' + eye_blink_open_wire_crv_name),
                               currentDriver=(eye_blink_name + '.tx'))
        cmds.setAttr((eye_blink_name + '.tx'), 0)

        # make all in the one grp
        # setAttr "Template_L_Eye_Tem_1_Crv_Grp.inheritsTransform" 0;
        eye_grp_name = self.prefix_name + '_' + eye_side + '_Eye_Tem_' + str(self.val) + '_Grp'
        eye_main_ctrl_name = eye_side + '_Eye_Main_Ctrl'
        cmds.select(crv_grp_name, loc_grp_name, jnt_grp_name, sphere_grp_name, eye_main_ctrl_name)
        cmds.group(n=eye_grp_name)

        cmds.move(get_trans[0], get_trans[1], get_trans[2],
                  (eye_grp_name + '.scalePivot'),
                  (eye_grp_name + '.scalePivot'))
        cmds.setAttr((eye_blink_name + '.ty'), 1)
        cmds.setAttr((crv_grp_name + '.inheritsTransform'), 0)

        # Create a primary cluster
        vtx_no = upper_curve_smooth_name + '.cv[1]'
        primary_1_common = self.prefix_name + '_' + eye_side + '_Eye_Upper_Primary_01_Tem_' + str(self.val)
        upper_curve_primary_1_clu_handle_name, upper_curve_primary_1_ctrl_name = self.primary_ctrl_create(vtx_no,
                                                                                                          primary_1_common)
        ctrl_list.append(upper_curve_primary_1_ctrl_name)

        vtx_no = upper_curve_smooth_name + '.cv[2]'
        primary_2_common = self.prefix_name + '_' + eye_side + '_Eye_Upper_Primary_02_Tem_' + str(self.val)
        upper_curve_primary_2_clu_handle_name, upper_curve_primary_2_ctrl_name = self.primary_ctrl_create(vtx_no,
                                                                                                          primary_2_common)
        ctrl_list.append(upper_curve_primary_2_ctrl_name)

        vtx_no = upper_curve_smooth_name + '.cv[3]'
        primary_3_common = self.prefix_name + '_' + eye_side + '_Eye_Upper_Primary_03_Tem_' + str(self.val)
        upper_curve_primary_3_clu_handle_name, upper_curve_primary_3_ctrl_name = self.primary_ctrl_create(vtx_no,
                                                                                                          primary_3_common)
        ctrl_list.append(upper_curve_primary_3_ctrl_name)

        upper_primary_clu_handle_grp_name = self.prefix_name + '_' + eye_side + '_Eye_Upper_Primary_Tem_' + str(
            self.val) + '_Clu_Grp'
        cmds.select(upper_curve_primary_1_clu_handle_name, upper_curve_primary_2_clu_handle_name,
                    upper_curve_primary_3_clu_handle_name)
        cmds.group(n=upper_primary_clu_handle_grp_name)

        upper_primary_ctrl_grp_name = self.prefix_name + '_' + eye_side + '_Eye_Upper_Primary_Tem_' + str(
            self.val) + '_Ctrl_Grp'
        cmds.select(upper_curve_primary_1_ctrl_name, upper_curve_primary_2_ctrl_name, upper_curve_primary_3_ctrl_name)
        cmds.group(n=upper_primary_ctrl_grp_name)

        vtx_no = lower_curve_smooth_name + '.cv[1]'
        primary_1_common = self.prefix_name + '_' + eye_side + '_Eye_Lower_Primary_01_Tem_' + str(self.val)
        lower_curve_primary_1_clu_handle_name, lower_curve_primary_1_ctrl_name = self.primary_ctrl_create(vtx_no,
                                                                                                          primary_1_common)
        ctrl_list.append(lower_curve_primary_1_ctrl_name)

        vtx_no = lower_curve_smooth_name + '.cv[2]'
        primary_2_common = self.prefix_name + '_' + eye_side + '_Eye_Lower_Primary_02_Tem_' + str(self.val)
        lower_curve_primary_2_clu_handle_name, lower_curve_primary_2_ctrl_name = self.primary_ctrl_create(vtx_no,
                                                                                                          primary_2_common)
        ctrl_list.append(lower_curve_primary_2_ctrl_name)

        vtx_no = lower_curve_smooth_name + '.cv[3]'
        primary_3_common = self.prefix_name + '_' + eye_side + '_Eye_Lower_Primary_03_Tem_' + str(self.val)
        lower_curve_primary_3_clu_handle_name, lower_curve_primary_3_ctrl_name = self.primary_ctrl_create(vtx_no,
                                                                                                          primary_3_common)
        ctrl_list.append(lower_curve_primary_3_ctrl_name)

        lower_primary_clu_handle_grp_name = self.prefix_name + '_' + eye_side + '_Eye_Lower_Primary_Tem_' + str(
            self.val) + '_Clu_Grp'
        cmds.select(lower_curve_primary_1_clu_handle_name, lower_curve_primary_2_clu_handle_name,
                    lower_curve_primary_3_clu_handle_name)
        cmds.group(n=lower_primary_clu_handle_grp_name)

        lower_primary_ctrl_grp_name = self.prefix_name + '_' + eye_side + '_Eye_Lower_Primary_Tem_' + str(
            self.val) + '_Ctrl_Grp'
        cmds.select(lower_curve_primary_1_ctrl_name, lower_curve_primary_2_ctrl_name, lower_curve_primary_3_ctrl_name)
        cmds.group(n=lower_primary_ctrl_grp_name)

        # select -r Template_L_Eye_Upper_Tem_1_Smooth_Crv.cv[0] Template_L_Eye_Lower_Tem_1_Smooth_Crv.cv[4] ;

        vtx_no = [upper_curve_smooth_name + '.cv[0]', lower_curve_smooth_name + '.cv[4]']
        side_1_common = self.prefix_name + '_' + eye_side + '_Eye_Upper_Side_01_Tem_' + str(self.val)
        curve_side_1_clu_handle_name, curve_side_1_ctrl_name = self.primary_ctrl_create(vtx_no, side_1_common)
        ctrl_list.append(curve_side_1_ctrl_name)

        vtx_no = [upper_curve_smooth_name + '.cv[4]', lower_curve_smooth_name + '.cv[0]']
        side_2_common = self.prefix_name + '_' + eye_side + '_Eye_Upper_Side_02_Tem_' + str(self.val)
        curve_side_2_clu_handle_name, curve_side_2_ctrl_name = self.primary_ctrl_create(vtx_no, side_2_common)
        ctrl_list.append(curve_side_2_ctrl_name)

        side_primary_clu_handle_grp_name = self.prefix_name + '_' + eye_side + '_Eye_Side_Primary_Tem_' + str(
            self.val) + '_Clu_Grp'
        cmds.select(curve_side_1_clu_handle_name, curve_side_2_clu_handle_name)
        cmds.group(n=side_primary_clu_handle_grp_name)

        primary_clu_grp_name = self.prefix_name + '_' + eye_side + '_Eye_Primary_Tem_' + str(self.val) + '_Clu_Grp'
        cmds.select(upper_primary_clu_handle_grp_name, lower_primary_clu_handle_grp_name,
                    side_primary_clu_handle_grp_name)
        cmds.group(n=primary_clu_grp_name)
        cmds.setAttr((primary_clu_grp_name + '.v'), 0)

        side_primary_ctrl_grp_name = self.prefix_name + '_' + eye_side + '_Eye_Side_Primary_Tem_' + str(
            self.val) + '_Ctrl_Grp'
        cmds.select(curve_side_1_ctrl_name, curve_side_2_ctrl_name)
        cmds.group(n=side_primary_ctrl_grp_name)

        primary_ctrl_grp_name = self.prefix_name + '_' + eye_side + '_Eye_Primary_Tem_' + str(self.val) + '_Ctrl_Grp'
        cmds.select(upper_primary_ctrl_grp_name, lower_primary_ctrl_grp_name, side_primary_ctrl_grp_name)
        cmds.group(n=primary_ctrl_grp_name)
        self.ctrl_list = ctrl_list

        # get the list of the controller
        slide_1_common_name = self.prefix_name + '_' + eye_side + '_Eye_Slide_1_Tem_' + str(self.val)
        # upper_curve_primary_2_clu_handle_name
        get_pos = cmds.xform(upper_curve_primary_2_clu_handle_name, q=1, ws=1, rp=1)
        slide_1_ctrl_name = self.slide_ctrl_create(slide_1_common_name, get_pos, value=1)

        slide_2_common_name = self.prefix_name + '_' + eye_side + '_Eye_Slide_2_Tem_' + str(self.val)
        # upper_curve_primary_2_clu_handle_name
        get_pos = cmds.xform(lower_curve_primary_2_clu_handle_name, q=1, ws=1, rp=1)
        slide_2_ctrl_name = self.slide_ctrl_create(slide_2_common_name, get_pos, value=2)

        slide_3_common_name = self.prefix_name + '_' + eye_side + '_Eye_Slide_3_Tem_' + str(self.val)
        # upper_curve_primary_2_clu_handle_name
        get_pos = cmds.xform(curve_side_1_clu_handle_name, q=1, ws=1, rp=1)
        slide_3_ctrl_name = self.slide_ctrl_create(slide_3_common_name, get_pos, value=3)

        slide_4_common_name = self.prefix_name + '_' + eye_side + '_Eye_Slide_4_Tem_' + str(self.val)
        # upper_curve_primary_2_clu_handle_name
        get_pos = cmds.xform(curve_side_2_clu_handle_name, q=1, ws=1, rp=1)
        slide_4_ctrl_name = self.slide_ctrl_create(slide_4_common_name, get_pos, value=4)

        # Create a Group
        slide_Grp = self.prefix_name + '_' + eye_side + '_Eye_Slide_Tem_' + str(self.val) + '_Ctrl_Grp'
        cmds.select(slide_1_ctrl_name, slide_2_ctrl_name, slide_3_ctrl_name, slide_4_ctrl_name)
        cmds.group(n=slide_Grp)

        # Overall Stretch and Squash Controller
        squeez_1_common_name = self.prefix_name + '_' + eye_side + '_Eye_Squeez_1_Tem_' + str(self.val)
        # upper_curve_primary_2_clu_handle_name
        get_pos = cmds.xform(upper_curve_primary_2_clu_handle_name, q=1, ws=1, rp=1)
        squeez_1_ctrl_name = self.squeez_ctrl_create(squeez_1_common_name, get_pos, value=1)

        squeez_2_common_name = self.prefix_name + '_' + eye_side + '_Eye_Squeez_2_Tem_' + str(self.val)
        # upper_curve_primary_2_clu_handle_name
        get_pos = cmds.xform(lower_curve_primary_2_clu_handle_name, q=1, ws=1, rp=1)
        squeez_2_ctrl_name = self.squeez_ctrl_create(squeez_2_common_name, get_pos, value=2)

        squeez_3_common_name = self.prefix_name + '_' + eye_side + '_Eye_Squeez_3_Tem_' + str(self.val)
        # upper_curve_primary_2_clu_handle_name
        get_pos = cmds.xform(curve_side_1_clu_handle_name, q=1, ws=1, rp=1)
        squeez_3_ctrl_name = self.squeez_ctrl_create(squeez_3_common_name, get_pos, value=3)

        squeez_4_common_name = self.prefix_name + '_' + eye_side + '_Eye_Squeez_4_Tem_' + str(self.val)
        # upper_curve_primary_2_clu_handle_name
        get_pos = cmds.xform(curve_side_2_clu_handle_name, q=1, ws=1, rp=1)
        squeez_4_ctrl_name = self.squeez_ctrl_create(squeez_4_common_name, get_pos, value=4)

        squeez_Grp = self.prefix_name + '_' + eye_side + '_Eye_Squeez_Tem_' + str(self.val) + '_Ctrl_Grp'
        cmds.select(squeez_1_ctrl_name, squeez_2_ctrl_name, squeez_3_ctrl_name, squeez_4_ctrl_name)
        cmds.group(n=squeez_Grp)

        # make a single group
        cmds.select(sphere_grp_name, primary_ctrl_grp_name, slide_Grp, squeez_Grp)
        ctrl_grp_name = self.prefix_name + '_' + eye_side + '_Eye_' + str(self.val) + '_Ctrl_Grp'
        cmds.group(n=ctrl_grp_name)
        cmds.select(ctrl_grp_name, primary_clu_grp_name, eye_grp_name)
        cmds.parent()

        cmds.setAttr((crv_grp_name + '.v'), 0)
        cmds.setAttr((loc_grp_name + '.v'), 0)

        # Create a Controller in each position

        self.final_grp(eye_grp_name)

    def primary_ctrl_create(self, vtx_no, common_name):
        common_clu_name = common_name + 'Clu'
        common_clu_handle_name = common_clu_name + 'Handle'
        cmds.select(vtx_no)
        cmds.cluster(n=common_clu_name)
        cmds.setAttr((common_clu_name + '.relative'), 1)
        ctrl_name = common_name + '_Primary_Ctrl'
        self.controller_class.cube_ctrl()
        cmds.rename('cube_ctrl', ctrl_name)
        get_pos = cmds.xform(common_clu_handle_name, q=1, ws=1, rp=1)
        cmds.select(ctrl_name)
        cmds.move(get_pos[0], get_pos[1], get_pos[2])
        cmds.DeleteHistory()
        cmds.FreezeTransformations()
        # do the connection editor
        list = ['t', 'r', 's', 'v']
        for each in list:
            cmds.connectAttr((ctrl_name + '.' + each), (common_clu_handle_name + '.' + each))

        return common_clu_handle_name, ctrl_name

    def slide_ctrl_create(self, slide_common_name, pos_list, value):
        self.controller_class.square_ctrl()
        ctrl_name = slide_common_name + '_Ctrl'
        ctrl_shape_name = ctrl_name + 'Shape'
        cmds.rename('Square_ctrl', ctrl_name)
        cmds.move(pos_list[0], pos_list[1], pos_list[2])
        cmds.setAttr((ctrl_name + '.rx'), 90)
        if value == 1 or value == 2:
            cmds.setAttr((ctrl_name + '.sz'), 0.3)
            cmds.setAttr((ctrl_name + '.sx'), 2)
        elif value == 3 or value == 4:
            cmds.setAttr((ctrl_name + '.sx'), 0.3)

        cmds.select(ctrl_name)
        cmds.DeleteHistory()
        cmds.FreezeTransformations()
        # Create a each ctrl grp with side
        self.grp_all_controller_def('Slide', value, ctrl_name)

        return ctrl_name

    def grp_all_controller_def(self, type, value, ctrl_name):
        ctrl_shape_name = ctrl_name + 'Shape'
        for each in self.ctrl_list:
            split_word = each.split('_Ctrl')[0]
            grp_name = split_word + '_' + type + '_' + str(value) + '_Grp'
            cmds.select(each)
            cmds.group(n=grp_name)
            mult_name = split_word + '_' + type + '_' + str(value) + '_Mult'
            cmds.createNode('multiplyDivide', n=mult_name)
            cmds.connectAttr((ctrl_name + '.t'), (mult_name + '.input1'))
            # add Attr to the controller
            cmds.addAttr(ctrl_shape_name, ln=each, at='double', dv=1)
            cmds.setAttr((ctrl_shape_name + "." + each), e=True, keyable=True)
            cmds.connectAttr((ctrl_shape_name + "." + each), (mult_name + '.input2.input2X'))
            cmds.connectAttr((ctrl_shape_name + "." + each), (mult_name + '.input2.input2Y'))
            cmds.connectAttr((ctrl_shape_name + "." + each), (mult_name + '.input2.input2Z'))
            cmds.connectAttr((mult_name + '.output'), (grp_name + '.t'))

    def squeez_ctrl_create(self, common_name, pos_list, value):

        ctrl_name = common_name + '_Ctrl'
        ctrl_shape_name = ctrl_name + 'Shape'
        cmds.polySphere(r=0.3, sx=6, sy=6, ax=(0, 1, 0), cuv=2, ch=1, n=ctrl_name)
        cmds.move(pos_list[0], pos_list[1], pos_list[2])
        if value == 1:
            cmds.move(0, 0.5, 0, r=True)
        elif value == 2:
            cmds.move(0, -0.5, 0, r=True)
        elif value == 3:
            cmds.move(-0.5, 0, 0, r=True)
        elif value == 4:
            cmds.move(0.5, 0, 0, r=True)

        cmds.select(ctrl_name)
        cmds.DeleteHistory()
        cmds.FreezeTransformations()
        # Create a each ctrl grp with side
        self.grp_all_controller_def('Squeez', value, ctrl_name)

        return ctrl_name

    def final_grp(self, grp_name):
        root_grp_name = 'Root_Grp'
        if cmds.objExists(root_grp_name):
            cmds.select(grp_name, root_grp_name)
            cmds.parent()
        else:
            cmds.createNode('transform', n=root_grp_name)
            cmds.select(grp_name, root_grp_name)
            cmds.parent()

    def side_create(self, eye_side, loc_list, name):

        if eye_side == 'L':
            color_name = 'Blue'
        else:
            color_name = 'Red'

        a = 0
        curve_pos_list = []
        curve_k_val = []
        main_grp_list = []
        while a < len(loc_list):
            # Template_L_Eye_Side_3_Tem_1_LOC

            loc_common = self.prefix_name + '_' + eye_side + '_' + name + '_' + str(a + 1) + '_Tem_' + str(self.val)
            loc_name = loc_common + '_LOC'
            get_trans, get_rot = self.helper_class.get_trans_rot(loc_name)
            curve_pos_list.append(get_trans)
            curve_k_val.append(a)
            a += 1
        curve_pos_list.append(curve_pos_list[0])
        curve_k_val.append(a + 1)

        side_crv_name = self.prefix_name + '_' + eye_side + '_' + name + '_' + str(self.val) + '_Crv'
        side_curve_shape_name = side_crv_name + 'Shape'
        cmds.curve(n=side_crv_name, d=0, p=curve_pos_list,
                   k=curve_k_val)
        shape_name = cmds.listRelatives(side_crv_name, s=True)
        cmds.rename(shape_name[0], side_curve_shape_name)

        crv_grp_name = self.prefix_name + '_' + eye_side + '_' + name + '_' + str(self.val) + '_Crv_Grp'
        cmds.select(side_crv_name)
        cmds.group(n=crv_grp_name)
        cmds.setAttr((side_crv_name + '.inheritsTransform'), 0)
        cmds.setAttr((side_crv_name + '.v'), 0)
        main_grp_list.append(crv_grp_name)

        x_pos = []
        y_pos = []
        z_pos = []
        total_ctrl_list = []
        a = 0
        while a < len(loc_list):
            # Template_L_Eye_3_Tem_1_LOC
            loc_common = self.prefix_name + '_' + eye_side + '_' + name + '_' + str(a + 1) + '_Tem_' + str(self.val)
            loc_name = loc_common + '_LOC'
            get_trans, get_rot = self.helper_class.get_trans_rot(loc_name)

            tem_remove_name = self.helper_class.remove_tem(loc_common)

            # Create a Locator and set the position
            new_loc_name = tem_remove_name + '_Loc'
            cmds.spaceLocator(n=new_loc_name, p=(0, 0, 0))
            cmds.move(get_trans[0], get_trans[1], get_trans[2])
            cmds.select(new_loc_name)
            cmds.CenterPivot()

            # Create a Sphere
            sphere_name = tem_remove_name + '_Secondary_Ctrl'
            sphere_grp = sphere_name + '_Grp'
            cmds.polySphere(r=0.3, sx=6, sy=6, ax=(0, 1, 0), cuv=2, ch=1, n=sphere_name)
            cmds.move(get_trans[0], get_trans[1], get_trans[2])
            cmds.DeleteHistory()
            cmds.FreezeTransformations()
            cmds.select(sphere_name)
            cmds.group(n=sphere_grp)
            total_ctrl_list.append(sphere_name)

            # Create a Plus Minus
            plus_minus_name = tem_remove_name + '_Plus_Minus'
            cmds.createNode('plusMinusAverage', n=plus_minus_name)
            mel.eval('AEnewNonNumericMultiAddNewItem("%s","input3D");' % plus_minus_name)
            mel.eval('AEnewNonNumericMultiAddNewItem("%s","input3D");' % plus_minus_name)
            cmds.connectAttr((new_loc_name + '.translate'), (plus_minus_name + '.input3D[0]'))
            cmds.setAttr((plus_minus_name + '.operation'), 2)
            cmds.setAttr((plus_minus_name + '.input3D[1].input3Dx'), get_trans[0])
            cmds.setAttr((plus_minus_name + '.input3D[1].input3Dy'), get_trans[1])
            cmds.setAttr((plus_minus_name + '.input3D[1].input3Dz'), get_trans[2])
            cmds.connectAttr((plus_minus_name + '.output3D'), (sphere_grp + '.translate'))

            ##Create a point on Curve
            poc_name = tem_remove_name + '_POC'
            cmds.createNode('pointOnCurveInfo', n=poc_name)
            cmds.connectAttr((poc_name + '.position'),
                             (new_loc_name + '.translate'),
                             f=True)

            cmds.connectAttr((side_curve_shape_name + '.worldSpace[0]'), (poc_name + '.inputCurve'))
            # setAttr "Template_L_Eye_3_1_POC.parameter" 2;
            cmds.setAttr((poc_name + '.parameter'), a)

            grp_common = self.prefix_name + '_' + eye_side + '_' + name + '_' + str(self.val)
            loc_grp_name = grp_common + '_Loc_Grp'
            if cmds.objExists(loc_grp_name):
                cmds.select(new_loc_name, loc_grp_name)
                cmds.parent()
            else:
                cmds.select(new_loc_name)
                cmds.group(n=loc_grp_name)

            sphere_grp_name = grp_common + '_Secondary_Ctrl_Grp'
            if cmds.objExists(sphere_grp_name):
                cmds.select(sphere_grp, sphere_grp_name)
                cmds.parent()
            else:
                cmds.select(sphere_grp)
                cmds.group(n=sphere_grp_name)

            cmds.setAttr((sphere_grp_name + '.inheritsTransform'), 0)

            # get the loc high position
            get_trans = cmds.xform(new_loc_name, q=1, ws=1, rp=1)
            x_pos.append(get_trans[0])
            y_pos.append(get_trans[1])
            z_pos.append(get_trans[2])

            a += 1

        main_grp_list.append(sphere_grp_name)
        main_grp_list.append(loc_grp_name)
        cmds.setAttr((loc_grp_name + '.v'), 0)

        side_crv_smooth_name = self.prefix_name + '_' + eye_side + '_' + name + '_' + str(self.val) + '_Smooth_Crv'
        side_curve_smooth_shape_name = side_crv_smooth_name + 'Shape'
        side_crv_smooth_wire_name = self.prefix_name + '_' + eye_side + '_' + name + '_' + str(self.val) + '_Wire'
        cmds.select(side_crv_name)
        cmds.duplicate(n=side_crv_smooth_name)
        cmds.rebuildCurve(side_crv_smooth_name, ch=0,
                          rpo=1, rt=0, end=1, kr=0, kcp=0, kep=1, kt=0, d=2, tol=0.01, s=6)

        mel.eval(
            'wire -gw false -en 1.000000 -ce 0.000000 -li 0.000000 -w %s %s;' % (side_crv_smooth_name, side_crv_name))
        list = cmds.listConnections(side_curve_smooth_shape_name, type='wire')
        cmds.rename(list[0], side_crv_smooth_wire_name)

        # Create a Cube on each smooth cv
        cmds.select(side_crv_smooth_name + '.cv[0:]')
        smooth_cv = cmds.ls(sl=True, fl=True)
        a = 0
        while a < len(smooth_cv) - 1:
            common_name = self.prefix_name + '_' + eye_side + '_' + name + '_' + str(a + 1) + '_' + str(
                self.val) + '_Smooth'
            clu_name = common_name + '_Clu'
            clu_handle_name = clu_name + 'Handle'
            if a == 0:
                cmds.select(side_crv_smooth_name + '.cv[%s]' % str(len(smooth_cv) - 1))
                cmds.select(side_crv_smooth_name + '.cv[0]', add=True)
                cmds.cluster(n=clu_name)
            else:
                cmds.select((side_crv_smooth_name + '.cv[%s]' % str(a)))
                cmds.cluster(n=clu_name)

            cmds.setAttr((clu_handle_name + '.v'), 0)

            # Now Create Controller on each position
            self.controller_class.cube_ctrl()
            ctrl_name = common_name + '_Primary_Ctrl'
            get_trans = cmds.xform(clu_handle_name, q=1, ws=1, rp=1)
            cmds.rename('cube_ctrl', ctrl_name)
            cmds.move(get_trans[0], get_trans[1], get_trans[2])
            cmds.DeleteHistory()
            cmds.FreezeTransformations()
            cmds.connectAttr((ctrl_name + '.t'), (clu_handle_name + '.t'))
            total_ctrl_list.append(ctrl_name)
            self.helper_class.color_val(color_name, ctrl_name)

            # put the cluster in one group
            clu_grp_name = self.prefix_name + '_' + eye_side + '_' + name + '_' + str(self.val) + '_Smooth_Clu_Grp'
            if cmds.objExists(clu_grp_name):
                cmds.select(clu_handle_name, clu_grp_name)
                cmds.parent()
            else:
                cmds.select(clu_handle_name)
                cmds.group(n=clu_grp_name)
            # setAttr "Template_L_Eye_Side_2_1_Smooth_Clu_Grp.inheritsTransform" 1;

            ctrl_grp_name = self.prefix_name + '_' + eye_side + '_' + name + '_' + str(self.val) + '_Smooth_Ctrl_Grp'
            if cmds.objExists(ctrl_grp_name):
                cmds.select(ctrl_name, ctrl_grp_name)
                cmds.parent()
            else:
                cmds.select(ctrl_name)
                cmds.group(n=ctrl_grp_name)

            a += 1

        main_grp_list.append(clu_grp_name)
        main_grp_list.append(ctrl_grp_name)

        # make a
        min_x_val = min(x_pos)
        max_x_val = max(x_pos)

        min_y_val = min(y_pos)
        max_y_val = max(y_pos)
        a = 0
        while a < len(x_pos):
            # check the min x vak
            if min_x_val == x_pos[a]:
                min_x_pos = [x_pos[a], y_pos[a], z_pos[a]]

            # Check the max x val
            if max_x_val == x_pos[a]:
                max_x_pos = [x_pos[a], y_pos[a], z_pos[a]]

            # check the min y val
            if min_y_val == y_pos[a]:
                min_y_pos = [x_pos[a], y_pos[a], z_pos[a]]

            # check the max y val
            if max_y_val == y_pos[a]:
                max_y_pos = [x_pos[a], y_pos[a], z_pos[a]]
            a += 1

        list = ['Upper', 'Lower', 'Side_1', 'Side_2']
        pos_list = [max_y_pos, min_y_pos, min_x_pos, max_x_pos]

        a = 0
        while a < len(list):
            # Create a Controller and pos the val
            self.controller_class.square_ctrl()
            ctrl_common = self.prefix_name + '_' + eye_side + '_' + name + '_' + str(a + 1) + '_Main_' + list[
                a] + '_' + str(self.val)
            ctrl_name = ctrl_common + '_Ctrl'
            ctrl_shape_name = ctrl_name + 'Shape'
            cmds.rename('Square_ctrl', ctrl_name)
            cmds.move(pos_list[a][0], pos_list[a][1], pos_list[a][2])
            self.helper_class.color_val(color_name, ctrl_name)
            if list[a] == 'Upper' or list[a] == 'Lower':
                cmds.setAttr((ctrl_name + '.rx'), 90)
                cmds.setAttr((ctrl_name + '.sx'), 3)
                cmds.setAttr((ctrl_name + '.sz'), 0.3)
                if list[a] == 'Upper':
                    cmds.move(0, 1, 0, r=True)
                else:
                    cmds.move(0, -1, 0, r=True)
            if list[a] == 'Side_1' or list[a] == 'Side_2':
                cmds.setAttr((ctrl_name + '.rx'), 90)
                cmds.setAttr((ctrl_name + '.sx'), 0.3)
                cmds.setAttr((ctrl_name + '.sz'), 2.5)
                if list[a] == 'Side_1':
                    cmds.move(-1, 0, 0, r=True)
                else:
                    cmds.move(1, 0, 0, r=True)
            cmds.select(ctrl_name)
            cmds.DeleteHistory()
            cmds.FreezeTransformations()

            # Createa a Blend Controller to all the controller
            for each in total_ctrl_list:
                grp_name = each + '_' + list[a] + '_Grp'
                cmds.select(each)
                cmds.group(n=grp_name)
                mult_div_name = grp_name + '_' + ctrl_name + '_Mult'
                cmds.createNode('multiplyDivide', n=mult_div_name)
                # connectAttr -f Template_L_Thine_to_Foot_1_DisShape.distance multiplyDivide1.input1X;
                cmds.connectAttr((ctrl_name + '.t'), (mult_div_name + '.input1'), f=True)
                cmds.connectAttr((mult_div_name + '.output'), (grp_name + '.t'), f=True)
                # add Attr
                cmds.addAttr(ctrl_shape_name, ln=each, at='double')
                cmds.setAttr((ctrl_shape_name + "." + each), e=True, keyable=True)
                cmds.connectAttr(((ctrl_shape_name + "." + each)), (mult_div_name + '.input2.input2X'))
                cmds.connectAttr(((ctrl_shape_name + "." + each)), (mult_div_name + '.input2.input2Y'))
                cmds.connectAttr(((ctrl_shape_name + "." + each)), (mult_div_name + '.input2.input2Z'))

            main_ctrl_grp_name = self.prefix_name + '_' + eye_side + '_' + name + '_Main_' + str(self.val) + '_Ctrl_Grp'
            if cmds.objExists(main_ctrl_grp_name):
                cmds.select(ctrl_name, main_ctrl_grp_name)
                cmds.parent()
            else:
                cmds.select(ctrl_name)
                cmds.group(n=main_ctrl_grp_name)

            a += 1
        # put everything in one group
        main_grp_list.append(main_ctrl_grp_name)
        cmds.select(cl=True)
        for each in main_grp_list:
            cmds.select(each, add=True)

        final_grp_name = self.prefix_name + '_' + eye_side + '_' + name + '_Final_' + str(self.val) + '_Grp'
        cmds.group(n=final_grp_name)

        self.final_grp(final_grp_name)

    def nose_create(self, nose_side):
        # Template_L_Nose_1_Tem_1_LOC
        loc_name = self.prefix_name + '_' + nose_side + '_Nose_*_Tem_' + str(self.val) + '_LOC'
        # Template_L_Nose_4_Tem_1_LOC
        loc_1 = self.prefix_name + '_' + nose_side + '_Nose_1_Tem_' + str(self.val) + '_LOC'
        loc_2 = self.prefix_name + '_' + nose_side + '_Nose_2_Tem_' + str(self.val) + '_LOC'
        loc_3 = self.prefix_name + '_' + nose_side + '_Nose_3_Tem_' + str(self.val) + '_LOC'
        loc_4 = self.prefix_name + '_' + nose_side + '_Nose_4_Tem_' + str(self.val) + '_LOC'

        cmds.select(loc_name)
        sel_loc_name = [loc_1, loc_2, loc_3, loc_4]
        print(sel_loc_name)
        a = 1
        for each in sel_loc_name:
            loc_common = self.prefix_name + '_' + nose_side + '_Nose_' + str(a) + '_Tem_' + str(self.val)
            loc_new_name = loc_common + '_LOC'
            get_trans = cmds.xform(loc_new_name, q=1, ws=1, rp=1)
            sphere_name = loc_common + '_Secondary_Ctrl'
            sphere_grp_name = sphere_name + '_Grp'
            cmds.polySphere(r=0.3, sx=6, sy=6, ax=(0, 1, 0), cuv=2, ch=1, n=sphere_name)
            cmds.move(get_trans[0], get_trans[1], get_trans[2])
            cmds.DeleteHistory()
            cmds.FreezeTransformations()
            cmds.select(sphere_name)
            cmds.group(n=sphere_grp_name)
            # Template_L_Nose_Tem_1_Main_LOC
            main_loc_name = self.prefix_name + '_' + nose_side + '_Nose_Tem_' + str(self.val) + '_Main_LOC'
            main_loc_pos = cmds.xform(main_loc_name, q=1, ws=1, rp=1)
            cmds.move(main_loc_pos[0], main_loc_pos[1], main_loc_pos[2],
                      (sphere_grp_name + '.scalePivot'),
                      (sphere_grp_name + '.rotatePivot'))

            secondary_ctrl_grp_name = self.prefix_name + '_' + nose_side + '_Nose_Tem_' + str(
                self.val) + '_Secondary_Ctrl_Grp'
            if cmds.objExists(secondary_ctrl_grp_name):
                cmds.select(sphere_grp_name, secondary_ctrl_grp_name)
                cmds.parent()
            else:
                cmds.select(sphere_grp_name)
                cmds.group(n=secondary_ctrl_grp_name)

            # lock and hide all
            self.helper_class.transform_rotation_scale_visible(sphere_name, t=False, r=True, s=True, v=True)

            a += 1

        # Creete a Center controller and and connect the spheer
        center_ctrl_name = self.prefix_name + '_' + nose_side + '_Nose_Center_Tem_' + str(self.val) + '_Ctrl'
        center_ctrl_grp_name = center_ctrl_name + '_Grp'
        center_ctrl_shape_name = center_ctrl_name + 'Shape'
        self.controller_class.cube_ctrl()
        cmds.rename('cube_ctrl', center_ctrl_name)
        loc_1_name = self.prefix_name + '_' + nose_side + '_Nose_1_Tem_' + str(self.val) + '_LOC'
        loc_2_name = self.prefix_name + '_' + nose_side + '_Nose_2_Tem_' + str(self.val) + '_LOC'
        loc_3_name = self.prefix_name + '_' + nose_side + '_Nose_3_Tem_' + str(self.val) + '_LOC'
        loc_4_name = self.prefix_name + '_' + nose_side + '_Nose_4_Tem_' + str(self.val) + '_LOC'
        cmds.parentConstraint(loc_1_name, loc_2_name, loc_3_name, loc_4_name, center_ctrl_name, mo=False)
        cmds.select(center_ctrl_name + '_parentConstraint1')
        cmds.delete()
        cmds.select(center_ctrl_name)
        cmds.setAttr((center_ctrl_name + '.sx'), 0.3)
        cmds.setAttr((center_ctrl_name + '.sy'), 0.3)
        cmds.setAttr((center_ctrl_name + '.sz'), 0.3)
        cmds.move(0, -0.5, 0, r=True)
        cmds.DeleteHistory()
        cmds.FreezeTransformations()
        cmds.group(n=center_ctrl_grp_name)
        self.helper_class.transform_rotation_scale_visible(center_ctrl_name, t=False, r=True, s=True, v=True)
        cmds.setAttr((center_ctrl_name + '.tx'), lock=True, keyable=False)
        cmds.setAttr((center_ctrl_name + '.tz'), lock=True, keyable=False)

        # make a blend connection to all the controller grp
        a = 1
        for each in sel_loc_name:
            loc_common = self.prefix_name + '_' + nose_side + '_Nose_' + str(a) + '_Tem_' + str(self.val)
            sphere_name = loc_common + '_Secondary_Ctrl'
            sphere_grp_name = sphere_name + '_Grp'
            mult_name = loc_common + '_Mult'
            cmds.createNode('multiplyDivide', n=mult_name)
            cmds.connectAttr((center_ctrl_name + '.ty'), (mult_name + '.input1.input1X'))
            # add Attr to the controller
            cmds.addAttr(center_ctrl_shape_name, ln=each, at='double', dv=1)
            cmds.setAttr((center_ctrl_shape_name + "." + each), e=True, keyable=True)
            cmds.connectAttr((center_ctrl_shape_name + "." + each), (mult_name + '.input2.input2X'))
            cmds.connectAttr((center_ctrl_shape_name + "." + each), (mult_name + '.input2.input2Y'))
            cmds.connectAttr((center_ctrl_shape_name + "." + each), (mult_name + '.input2.input2Z'))

            # Create a reverse
            rev_name = loc_common + '_Rev'
            cmds.createNode('reverse', n=rev_name)
            cmds.connectAttr((mult_name + ".output.outputX"), (rev_name + '.inputX'))

            cmds.connectAttr((rev_name + ".outputX"), (sphere_grp_name + '.scaleX'))
            cmds.connectAttr((rev_name + ".outputX"), (sphere_grp_name + '.scaleY'))
            cmds.connectAttr((rev_name + ".outputX"), (sphere_grp_name + '.scaleZ'))

            a += 1
        nose_grp_name = self.prefix_name + '_' + nose_side + '_Nose_Tem_' + str(self.val) + '_Grp'
        cmds.select(secondary_ctrl_grp_name, center_ctrl_grp_name)
        cmds.group(n=nose_grp_name)

        self.final_grp(nose_grp_name)
        # connect with the all the loc

    def for_head_final_def(self):
        # Template_For_Head_1_Tem_1_LOC
        loc_name = self.prefix_name + '_For_Head_*_Tem_' + str(self.val) + '_LOC'
        cmds.select(loc_name)
        sel_loc = cmds.ls(sl=True)

        a = 0
        curve_pos_list = []
        curve_k_val = []
        while a < len(sel_loc):

            loc_common = self.prefix_name + '_For_Head_' + str(a + 1) + '_Tem_' + str(self.val)
            loc_name = loc_common + '_LOC'
            pos_val = cmds.xform(loc_name, q=1, ws=1, rp=1)
            curve_pos_list.append(pos_val)
            number = a + 1
            curve_k_val.append(number)

            # Create a Loc
            common_name = self.prefix_name + '_For_Head_' + str(a + 1) + '_' + str(self.val)
            loc_new_name = common_name + '_Loc'
            cmds.spaceLocator(n=loc_new_name, p=(0, 0, 0))
            cmds.move(pos_val[0], pos_val[1], pos_val[2])

            # Create a Sphere
            sphere_name = common_name + '_Secondary_Ctrl'
            sphere_grp_name = sphere_name + '_Grp'
            cmds.polySphere(r=0.3, sx=6, sy=6, ax=(0, 1, 0), cuv=2, ch=1, n=sphere_name)
            cmds.move(pos_val[0], pos_val[1], pos_val[2])
            cmds.DeleteHistory()
            cmds.FreezeTransformations()
            cmds.select(sphere_name)
            cmds.group(n=sphere_grp_name)

            # put all the loc in one group
            grp_common_name = self.prefix_name + '_For_Head_' + str(self.val)
            loc_grp_name = grp_common_name + '_Loc_Grp'
            secondary_grp_name = grp_common_name + '_Secondary_Ctrl_Grp'
            if cmds.objExists(loc_grp_name):
                cmds.select(loc_new_name, loc_grp_name)
                cmds.parent()
            else:
                cmds.select(loc_new_name)
                cmds.group(n=loc_grp_name)

            if cmds.objExists(secondary_grp_name):
                cmds.select(sphere_grp_name, secondary_grp_name)
                cmds.parent()
            else:
                cmds.select(sphere_grp_name)
                cmds.group(n=secondary_grp_name)

            a += 1

        curve_name = self.prefix_name + '_For_Head_Tem_' + str(self.val) + '_no_Smooth_Crv'
        curve_shape_name = curve_name + 'Shape'
        cmds.curve(n=curve_name, d=0, p=curve_pos_list,
                   k=curve_k_val)
        shape_name = cmds.listRelatives(curve_name, s=True)
        cmds.rename(shape_name[0], curve_shape_name)
        crv_grp_name = self.prefix_name + '_For_Head_' + str(self.val) + '_Crv_Grp'
        cmds.select(curve_name)
        cmds.group(n=crv_grp_name)

        # Create a poc and get connect
        a = 0
        self.ctrl_list = []
        while a < len(sel_loc):
            common_name = self.prefix_name + '_For_Head_' + str(a + 1) + '_' + str(self.val)
            sphere_name = common_name + '_Secondary_Ctrl'
            self.ctrl_list.append(sphere_name)
            sphere_grp_name = sphere_name + '_Grp'
            loc_new_name = common_name + '_Loc'
            poc_name = common_name + '_Poc'
            plus_minus_name = common_name + '_Plus_Minus'

            cmds.createNode('pointOnCurveInfo', n=poc_name)
            cmds.connectAttr((curve_shape_name + '.worldSpace[0]'),
                             (poc_name + '.inputCurve'),
                             f=True)
            cmds.setAttr((poc_name + '.parameter'), a + 1)
            cmds.connectAttr((poc_name + '.result.position'), (loc_new_name + '.t'))

            # get the loc val
            loc_value = cmds.getAttr(loc_new_name + '.t')[0]

            cmds.createNode('plusMinusAverage', n=plus_minus_name)
            mel.eval('AEnewNonNumericMultiAddNewItem("%s","input3D");' % plus_minus_name)
            mel.eval('AEnewNonNumericMultiAddNewItem("%s","input3D");' % plus_minus_name)
            cmds.connectAttr((loc_new_name + '.t'), (plus_minus_name + '.input3D[0]'))
            cmds.setAttr((plus_minus_name + '.input3D[1].input3Dx'), loc_value[0])
            cmds.setAttr((plus_minus_name + '.input3D[1].input3Dy'), loc_value[1])
            cmds.setAttr((plus_minus_name + '.input3D[1].input3Dz'), loc_value[2])
            cmds.setAttr((plus_minus_name + '.operation'), 2)

            cmds.connectAttr((plus_minus_name + '.output3D'), (sphere_grp_name + '.t'))
            a += 1

        # Now Duplicate the curve and
        for_head_smooth_crv_name = self.prefix_name + '_For_Head_Tem_' + str(self.val) + '_Smooth_Crv'
        for_head_wire_name = self.prefix_name + '_For_Head_Tem_' + str(self.val) + '_Wire'
        cmds.select(curve_name)
        cmds.duplicate(n=for_head_smooth_crv_name)
        cmds.rebuildCurve(for_head_smooth_crv_name, ch=0,
                          rpo=1, rt=0, end=1, kr=0, kcp=0, kep=1, kt=0, d=2, tol=0.01, s=3)
        cmds.select(curve_name, for_head_smooth_crv_name)
        mel.eval('SmoothCurve;')
        mel.eval('SmoothCurve;')
        mel.eval('SmoothCurve;')
        mel.eval(
            'wire -gw false -en 1.000000 -ce 0.000000 -li 0.000000 -w %s %s;' % (for_head_smooth_crv_name, curve_name))
        list = cmds.listConnections(curve_shape_name, type='wire')
        cmds.rename(list[0], for_head_wire_name)

        # select the cv
        cmds.select(for_head_smooth_crv_name + '.cv[0:]')
        sel_cv = cmds.ls(sl=True, fl=True)
        a = 1
        for each in sel_cv:
            # get the point position
            point_position = cmds.pointPosition(each)
            common_name = self.prefix_name + '_For_Head_' + str(a + 1) + '_' + str(self.val)
            ctrl_name = common_name + '_Primary_Ctrl'
            self.ctrl_list.append(ctrl_name)
            self.controller_class.cube_ctrl()
            cmds.rename('cube_ctrl', ctrl_name)
            cmds.move(point_position[0], point_position[1], point_position[2])
            cmds.DeleteHistory()
            cmds.FreezeTransformations()

            # create a Cluster on the position
            cmds.select(each)
            clu_name = common_name + '_Clu'
            clu_handle_name = clu_name + 'Handle'
            cmds.cluster(n=clu_name)

            cmds.connectAttr((ctrl_name + '.t'), (clu_handle_name + '.t'))
            cmds.connectAttr((ctrl_name + '.r'), (clu_handle_name + '.r'))
            cmds.connectAttr((ctrl_name + '.s'), (clu_handle_name + '.s'))

            clu_grp_name = self.prefix_name + '_For_Head_' + str(self.val) + '_Clu_Grp'
            if cmds.objExists(clu_grp_name):
                cmds.select(clu_handle_name, clu_grp_name)
                cmds.parent()
            else:
                cmds.select(clu_handle_name)
                cmds.group(n=clu_grp_name)

            primary_ctrl_grp_name = self.prefix_name + '_For_Head_' + str(self.val) + '_Primary_Ctrl_Grp'
            if cmds.objExists(primary_ctrl_grp_name):
                cmds.select(ctrl_name, primary_ctrl_grp_name)
                cmds.parent()
            else:
                cmds.select(ctrl_name)
                cmds.group(n=primary_ctrl_grp_name)

            a += 1

        # put two controller in one grp
        ctrl_grp_name = self.prefix_name + '_For_Head_' + str(self.val) + '_Ctrl_Grp'
        cmds.select(secondary_grp_name, primary_ctrl_grp_name)
        cmds.group(n=ctrl_grp_name)

        for_head_grp = self.prefix_name + '_For_Head_' + str(self.val) + '_Grp'
        cmds.select(clu_grp_name, crv_grp_name, loc_grp_name, ctrl_grp_name)
        cmds.group(n=for_head_grp)
        for_head_grp_pos = cmds.xform(for_head_grp, q=1, ws=1, rp=1)

        list = [clu_grp_name, crv_grp_name, loc_grp_name]
        for each in list:
            # setAttr "Template_For_Head_1_Clu_Grp.inheritsTransform" 0;
            cmds.setAttr((each + '.inheritsTransform'), 0)
            cmds.setAttr((each + '.v'), 0)

        # Create a overall controller
        for_head_main_ctrl = self.prefix_name + '_For_Head_' + str(self.val) + '_Main_Ctrl'
        for_head_main_shape_name = for_head_main_ctrl + 'Shape'
        mel.eval(
            'curve -d 1 -p -2.2346 0 -0.439213 -p -0.598042 0 0.439213 -p 0.598042 0 0.439213 -p 2.2346 0 -0.439213 -p -2.2346 0 -0.439213 -k 0 -k 1 -k 2 -k 3 -k 4 -n %s;' % for_head_main_ctrl)
        shape_name = cmds.listRelatives(for_head_main_ctrl, s=True)[0]
        cmds.rename(shape_name, for_head_main_shape_name)

        cmds.move(for_head_grp_pos[0], for_head_grp_pos[1], for_head_grp_pos[2])
        cmds.move(0, 0, 3, r=True)
        cmds.setAttr((for_head_main_ctrl + '.rx'), -90)
        cmds.DeleteHistory()
        cmds.FreezeTransformations()

        # create a blend node with the controller
        for each in self.ctrl_list:
            split_word = each.split('_Ctrl')[0]
            grp_name = split_word + '_For_Head_' + str(self.val) + '_Grp'
            cmds.select(each)
            cmds.group(n=grp_name)
            mult_name = split_word + '_For_Head_' + str(self.val) + '_Mult'
            cmds.createNode('multiplyDivide', n=mult_name)
            cmds.connectAttr((for_head_main_ctrl + '.t'), (mult_name + '.input1'))
            # add Attr to the controller
            cmds.addAttr(for_head_main_shape_name, ln=each, at='double', dv=1)
            cmds.setAttr((for_head_main_shape_name + "." + each), e=True, keyable=True)
            cmds.connectAttr((for_head_main_shape_name + "." + each), (mult_name + '.input2.input2X'))
            cmds.connectAttr((for_head_main_shape_name + "." + each), (mult_name + '.input2.input2Y'))
            cmds.connectAttr((for_head_main_shape_name + "." + each), (mult_name + '.input2.input2Z'))
            cmds.connectAttr((mult_name + '.output'), (grp_name + '.t'))

        cmds.select(for_head_main_ctrl, ctrl_grp_name)
        cmds.parent()

        self.final_grp(for_head_grp)

    def mouth_final_def(self):
        self.ctrl_list = []

        # Lower
        a = 0
        curve_pos_list = []
        curve_k_val = []
        while a < 12:
            # Template_Mouth_1_Tem_1_LOC
            loc_name = self.prefix_name + '_Mouth_' + str(a + 1) + '_Tem_' + str(self.val) + '_LOC'
            pos_val = cmds.xform(loc_name, q=1, ws=1, rp=1)
            curve_pos_list.append(pos_val)
            number = a + 1
            curve_k_val.append(number)

            common_name = self.prefix_name + '_Lower_Mouth_' + str(a + 1) + '_' + str(self.val)
            new_loc_name = common_name + '_Loc'
            sphere_name = common_name + '_Secondary_Ctrl'
            sphere_grp_name = sphere_name + '_Grp'
            self.ctrl_list.append(sphere_name)

            cmds.spaceLocator(n=new_loc_name, p=(0, 0, 0))
            cmds.move(pos_val[0], pos_val[1], pos_val[2])
            cmds.polySphere(r=0.3, sx=6, sy=6, ax=(0, 1, 0), cuv=2, ch=1, n=sphere_name)
            cmds.move(pos_val[0], pos_val[1], pos_val[2])
            cmds.DeleteHistory()
            cmds.FreezeTransformations()
            cmds.select(sphere_name)
            cmds.group(n=sphere_grp_name)

            # keep that in one gr[
            grp_common_name = self.prefix_name + '_Mouth_' + str(self.val)
            loc_grp_name = grp_common_name + '_Loc_Grp'
            if cmds.objExists(loc_grp_name):
                cmds.select(new_loc_name, loc_grp_name)
                cmds.parent()
            else:
                cmds.select(new_loc_name)
                cmds.group(n=loc_grp_name)

            secondary_ctrl_grp_name = grp_common_name + '_Secondary_Ctrl_Grp'
            if cmds.objExists(secondary_ctrl_grp_name):
                cmds.select(sphere_grp_name, secondary_ctrl_grp_name)
                cmds.parent()
            else:
                cmds.select(sphere_grp_name)
                cmds.group(n=secondary_ctrl_grp_name)
            a += 1

        # Create a Curve
        curve_name = self.prefix_name + '_Lower_Mouth_Tem_' + str(self.val) + '_no_Smooth_Crv'
        curve_shape_name = curve_name + 'Shape'
        cmds.curve(n=curve_name, d=0, p=curve_pos_list,
                   k=curve_k_val)
        shape_name = cmds.listRelatives(curve_name, s=True)
        cmds.rename(shape_name[0], curve_shape_name)
        crv_grp_name = self.prefix_name + '_Mouth_' + str(self.val) + '_Crv_Grp'
        cmds.select(curve_name)
        cmds.group(n=crv_grp_name)
        # Create a Each curve ane make a smooth
        lower_mouth_smooth_crv_name = self.prefix_name + '_Lower_Mouth_Tem_' + str(self.val) + '_Smooth_Crv'
        wire_name = self.prefix_name + '_Lower_Mouth_Tem_' + str(self.val) + '_Wire'
        cmds.select(curve_name)
        cmds.duplicate(n=lower_mouth_smooth_crv_name)
        cmds.rebuildCurve(lower_mouth_smooth_crv_name, ch=0,
                          rpo=1, rt=0, end=1, kr=0, kcp=0, kep=1, kt=0, d=2, tol=0.01, s=5)
        cmds.select(lower_mouth_smooth_crv_name)
        mel.eval('SmoothCurve;')
        mel.eval('wire -gw false -en 1.000000 -ce 0.000000 -li 0.000000 -w %s %s;' % (
        lower_mouth_smooth_crv_name, curve_name))
        list = cmds.listConnections(curve_shape_name, type='wire')
        cmds.rename(list[0], wire_name)

        a = 0
        while a < 12:
            common_name = self.prefix_name + '_Lower_Mouth_' + str(a + 1) + '_' + str(self.val)
            loc_new_name = common_name + '_Loc'
            sphere_name = common_name + '_Secondary_Ctrl'
            sphere_grp_name = sphere_name + '_Grp'
            poc_name = common_name + '_Poc'
            plus_minus_name = common_name + '_Plus_Minus'

            cmds.createNode('pointOnCurveInfo', n=poc_name)
            cmds.connectAttr((curve_shape_name + '.worldSpace[0]'),
                             (poc_name + '.inputCurve'),
                             f=True)
            cmds.setAttr((poc_name + '.parameter'), a + 1)
            cmds.connectAttr((poc_name + '.result.position'), (loc_new_name + '.t'))

            # get the loc val
            loc_value = cmds.getAttr(loc_new_name + '.t')[0]

            cmds.createNode('plusMinusAverage', n=plus_minus_name)
            mel.eval('AEnewNonNumericMultiAddNewItem("%s","input3D");' % plus_minus_name)
            mel.eval('AEnewNonNumericMultiAddNewItem("%s","input3D");' % plus_minus_name)
            cmds.connectAttr((loc_new_name + '.t'), (plus_minus_name + '.input3D[0]'))
            cmds.setAttr((plus_minus_name + '.input3D[1].input3Dx'), loc_value[0])
            cmds.setAttr((plus_minus_name + '.input3D[1].input3Dy'), loc_value[1])
            cmds.setAttr((plus_minus_name + '.input3D[1].input3Dz'), loc_value[2])
            cmds.setAttr((plus_minus_name + '.operation'), 2)

            cmds.connectAttr((plus_minus_name + '.output3D'), (sphere_grp_name + '.t'))

            a += 1

        curve_pos_list = []
        curve_k_val = []
        a = 0
        while a < 12:
            if a == 0:
                # Template_Mouth_1_Tem_1_LOC
                loc_name = self.prefix_name + '_Mouth_' + str(a + 1) + '_Tem_' + str(self.val) + '_LOC'
            else:
                # Template_Mouth_22_Tem_1_LOC
                loc_name = self.prefix_name + '_Mouth_' + str(23 - a) + '_Tem_' + str(self.val) + '_LOC'

            pos_val = cmds.xform(loc_name, q=1, ws=1, rp=1)
            curve_pos_list.append(pos_val)
            number = a + 1
            curve_k_val.append(number)

            common_name = self.prefix_name + '_Upper_Mouth_' + str(a + 1) + '_' + str(self.val)
            new_loc_name = common_name + '_Loc'
            sphere_name = common_name + '_Secondary_Ctrl'
            sphere_grp_name = sphere_name + '_Grp'
            self.ctrl_list.append(sphere_name)

            cmds.spaceLocator(n=new_loc_name, p=(0, 0, 0))
            cmds.move(pos_val[0], pos_val[1], pos_val[2])
            cmds.polySphere(r=0.3, sx=6, sy=6, ax=(0, 1, 0), cuv=2, ch=1, n=sphere_name)
            cmds.move(pos_val[0], pos_val[1], pos_val[2])
            cmds.DeleteHistory()
            cmds.FreezeTransformations()
            cmds.select(sphere_name)
            cmds.group(n=sphere_grp_name)

            # keep that in one gr[
            grp_common_name = self.prefix_name + '_Mouth_' + str(self.val)
            loc_grp_name = grp_common_name + '_Loc_Grp'
            if cmds.objExists(loc_grp_name):
                cmds.select(new_loc_name, loc_grp_name)
                cmds.parent()
            else:
                cmds.select(new_loc_name)
                cmds.group(n=loc_grp_name)

            secondary_ctrl_grp_name = grp_common_name + '_Secondary_Ctrl_Grp'
            if cmds.objExists(secondary_ctrl_grp_name):
                cmds.select(sphere_grp_name, secondary_ctrl_grp_name)
                cmds.parent()
            else:
                cmds.select(sphere_grp_name)
                cmds.group(n=secondary_ctrl_grp_name)
            a += 1
        # Create a Curve
        curve_name = self.prefix_name + '_Upper_Mouth_Tem_' + str(self.val) + '_no_Smooth_Crv'
        curve_shape_name = curve_name + 'Shape'
        cmds.curve(n=curve_name, d=0, p=curve_pos_list,
                   k=curve_k_val)
        shape_name = cmds.listRelatives(curve_name, s=True)
        cmds.rename(shape_name[0], curve_shape_name)
        cmds.select(curve_name, crv_grp_name)
        cmds.parent()

        upper_mouth_smooth_crv_name = self.prefix_name + '_Upper_Mouth_Tem_' + str(self.val) + '_Smooth_Crv'
        wire_name = self.prefix_name + '_Upper_Mouth_Tem_' + str(self.val) + '_Wire'
        cmds.select(curve_name)
        cmds.duplicate(n=upper_mouth_smooth_crv_name)
        cmds.rebuildCurve(upper_mouth_smooth_crv_name, ch=0,
                          rpo=1, rt=0, end=1, kr=0, kcp=0, kep=1, kt=0, d=2, tol=0.01, s=5)
        cmds.select(upper_mouth_smooth_crv_name)
        mel.eval('SmoothCurve;')
        mel.eval('SmoothCurve;')
        mel.eval('SmoothCurve;')
        mel.eval('wire -gw false -en 1.000000 -ce 0.000000 -li 0.000000 -w %s %s;' % (
        upper_mouth_smooth_crv_name, curve_name))
        list = cmds.listConnections(curve_shape_name, type='wire')
        cmds.rename(list[0], wire_name)

        a = 0
        while a < 12:
            common_name = self.prefix_name + '_Upper_Mouth_' + str(a + 1) + '_' + str(self.val)
            loc_new_name = common_name + '_Loc'
            sphere_name = common_name + '_Secondary_Ctrl'
            sphere_grp_name = sphere_name + '_Grp'
            poc_name = common_name + '_Poc'
            plus_minus_name = common_name + '_Plus_Minus'

            cmds.createNode('pointOnCurveInfo', n=poc_name)
            cmds.connectAttr((curve_shape_name + '.worldSpace[0]'),
                             (poc_name + '.inputCurve'),
                             f=True)
            cmds.setAttr((poc_name + '.parameter'), a + 1)
            cmds.connectAttr((poc_name + '.result.position'), (loc_new_name + '.t'))

            # get the loc val
            loc_value = cmds.getAttr(loc_new_name + '.t')[0]

            cmds.createNode('plusMinusAverage', n=plus_minus_name)
            mel.eval('AEnewNonNumericMultiAddNewItem("%s","input3D");' % plus_minus_name)
            mel.eval('AEnewNonNumericMultiAddNewItem("%s","input3D");' % plus_minus_name)
            cmds.connectAttr((loc_new_name + '.t'), (plus_minus_name + '.input3D[0]'))
            cmds.setAttr((plus_minus_name + '.input3D[1].input3Dx'), loc_value[0])
            cmds.setAttr((plus_minus_name + '.input3D[1].input3Dy'), loc_value[1])
            cmds.setAttr((plus_minus_name + '.input3D[1].input3Dz'), loc_value[2])
            cmds.setAttr((plus_minus_name + '.operation'), 2)

            cmds.connectAttr((plus_minus_name + '.output3D'), (sphere_grp_name + '.t'))

            a += 1

        # Create a Primary Controller
        # upper curve
        vtx_no = [upper_mouth_smooth_crv_name + '.cv[1]']
        upper_1_common = self.prefix_name + '_Upper_Mouth_Side_1_' + str(self.val)
        mouth_upper_1_primary_clu_handle, mouth_upper_1_primary_ctrl = self.primary_ctrl_create(vtx_no, upper_1_common)
        self.ctrl_list.append(mouth_upper_1_primary_ctrl)

        vtx_no = [upper_mouth_smooth_crv_name + '.cv[2]']
        upper_2_common = self.prefix_name + '_Upper_Mouth_Side_2_' + str(self.val)
        mouth_upper_2_primary_clu_handle, mouth_upper_2_primary_ctrl = self.primary_ctrl_create(vtx_no, upper_2_common)
        self.ctrl_list.append(mouth_upper_2_primary_ctrl)

        vtx_no = [upper_mouth_smooth_crv_name + '.cv[3]']
        upper_3_common = self.prefix_name + '_Upper_Mouth_Side_3_' + str(self.val)
        mouth_upper_3_primary_clu_handle, mouth_upper_3_primary_ctrl = self.primary_ctrl_create(vtx_no, upper_3_common)
        self.ctrl_list.append(mouth_upper_3_primary_ctrl)

        vtx_no = [upper_mouth_smooth_crv_name + '.cv[4]']
        upper_4_common = self.prefix_name + '_Upper_Mouth_Side_4_' + str(self.val)
        mouth_upper_4_primary_clu_handle, mouth_upper_4_primary_ctrl = self.primary_ctrl_create(vtx_no, upper_4_common)
        self.ctrl_list.append(mouth_upper_4_primary_ctrl)

        vtx_no = [upper_mouth_smooth_crv_name + '.cv[5]']
        upper_5_common = self.prefix_name + '_Upper_Mouth_Side_5_' + str(self.val)
        mouth_upper_5_primary_clu_handle, mouth_upper_5_primary_ctrl = self.primary_ctrl_create(vtx_no, upper_5_common)
        self.ctrl_list.append(mouth_upper_5_primary_ctrl)

        vtx_no = [lower_mouth_smooth_crv_name + '.cv[1]']
        lower_1_common = self.prefix_name + '_Lower_Mouth_Side_1_' + str(self.val)
        mouth_lower_1_primary_clu_handle, mouth_lower_1_primary_ctrl = self.primary_ctrl_create(vtx_no, lower_1_common)
        self.ctrl_list.append(mouth_lower_1_primary_ctrl)

        vtx_no = [lower_mouth_smooth_crv_name + '.cv[2]']
        lower_2_common = self.prefix_name + '_Lower_Mouth_Side_2_' + str(self.val)
        mouth_lower_2_primary_clu_handle, mouth_lower_2_primary_ctrl = self.primary_ctrl_create(vtx_no, lower_2_common)
        self.ctrl_list.append(mouth_lower_2_primary_ctrl)

        vtx_no = [lower_mouth_smooth_crv_name + '.cv[3]']
        lower_3_common = self.prefix_name + '_Lower_Mouth_Side_3_' + str(self.val)
        mouth_lower_3_primary_clu_handle, mouth_lower_3_primary_ctrl = self.primary_ctrl_create(vtx_no, lower_3_common)
        self.ctrl_list.append(mouth_lower_3_primary_ctrl)

        vtx_no = [lower_mouth_smooth_crv_name + '.cv[4]']
        lower_4_common = self.prefix_name + '_Lower_Mouth_Side_4_' + str(self.val)
        mouth_lower_4_primary_clu_handle, mouth_lower_4_primary_ctrl = self.primary_ctrl_create(vtx_no, lower_4_common)
        self.ctrl_list.append(mouth_lower_4_primary_ctrl)

        vtx_no = [lower_mouth_smooth_crv_name + '.cv[5]']
        lower_5_common = self.prefix_name + '_Lower_Mouth_Side_5_' + str(self.val)
        mouth_lower_5_primary_clu_handle, mouth_lower_5_primary_ctrl = self.primary_ctrl_create(vtx_no, lower_5_common)
        self.ctrl_list.append(mouth_lower_5_primary_ctrl)

        vtx_no = [lower_mouth_smooth_crv_name + '.cv[0]', upper_mouth_smooth_crv_name + '.cv[0]']
        side_1_common = self.prefix_name + '_Side_Mouth_Side_1_' + str(self.val)
        mouth_side_1_primary_clu_handle, mouth_side_1_primary_ctrl = self.primary_ctrl_create(vtx_no, side_1_common)
        self.ctrl_list.append(mouth_side_1_primary_ctrl)

        vtx_no = [lower_mouth_smooth_crv_name + '.cv[6]', upper_mouth_smooth_crv_name + '.cv[6]']
        side_2_common = self.prefix_name + '_Side_Mouth_Side_2_' + str(self.val)
        mouth_side_2_primary_clu_handle, mouth_side_2_primary_ctrl = self.primary_ctrl_create(vtx_no, side_2_common)
        self.ctrl_list.append(mouth_side_2_primary_ctrl)

        # save cluster and primary controller in one grp
        cmds.select(mouth_upper_1_primary_clu_handle, mouth_upper_2_primary_clu_handle,
                    mouth_upper_3_primary_clu_handle, mouth_upper_4_primary_clu_handle,
                    mouth_upper_5_primary_clu_handle,
                    mouth_lower_1_primary_clu_handle, mouth_lower_2_primary_clu_handle,
                    mouth_lower_3_primary_clu_handle, mouth_lower_4_primary_clu_handle,
                    mouth_lower_5_primary_clu_handle,
                    mouth_side_1_primary_clu_handle, mouth_side_2_primary_clu_handle)
        clu_grp_name = self.prefix_name + '_Mouth_' + str(self.val) + '_Clu_Grp'
        cmds.group(n=clu_grp_name)

        cmds.select(mouth_upper_1_primary_ctrl, mouth_upper_2_primary_ctrl, mouth_upper_3_primary_ctrl,
                    mouth_upper_4_primary_ctrl, mouth_upper_5_primary_ctrl,
                    mouth_lower_1_primary_ctrl, mouth_lower_2_primary_ctrl, mouth_lower_3_primary_ctrl,
                    mouth_lower_4_primary_ctrl, mouth_lower_5_primary_ctrl,
                    mouth_side_1_primary_ctrl, mouth_side_2_primary_ctrl)
        primary_ctrl_grp_name = self.prefix_name + '_Mouth_' + str(self.val) + '_Primary_Ctrl_Grp'
        cmds.group(n=primary_ctrl_grp_name)

        ctrl_grp_name = self.prefix_name + '_Mouth_' + str(self.val) + '_Ctrl_Grp'
        cmds.select(secondary_ctrl_grp_name, primary_ctrl_grp_name)
        cmds.group(n=ctrl_grp_name)

        mouth_grp_name = self.prefix_name + '_Mouth_' + str(self.val) + '_Grp'
        cmds.select(loc_grp_name, crv_grp_name, clu_grp_name, ctrl_grp_name)
        cmds.group(n=mouth_grp_name)

        list = [loc_grp_name, crv_grp_name, clu_grp_name]
        for each in list:
            cmds.setAttr((each + '.inheritsTransform'), 0)
            cmds.setAttr((each + '.v'), 0)

        # Create a Upper Lower and Middle Ctrl
        upper_main_ctrl = self.prefix_name + '_Upper_Mouth_' + str(self.val) + '_Main_Ctrl'
        upper_main_shape_name = upper_main_ctrl + 'Shape'
        mel.eval(
            'curve -d 1 -p -2.2346 0 -0.439213 -p -0.598042 0 0.439213 -p 0.598042 0 0.439213 -p 2.2346 0 -0.439213 -p -2.2346 0 -0.439213 -k 0 -k 1 -k 2 -k 3 -k 4 -n %s;' % upper_main_ctrl)
        shape_name = cmds.listRelatives(upper_main_ctrl, s=True)[0]
        cmds.rename(shape_name, upper_main_shape_name)
        # Template_Mouth_Tem_1_Main_LOC
        mouth_main_loc_name = self.prefix_name + '_Mouth_Tem_' + str(self.val) + '_Main_LOC'
        mouth_main_loc_get_attr_name = cmds.xform(mouth_main_loc_name, q=1, ws=1, rp=1)
        print(mouth_main_loc_get_attr_name)
        cmds.move(mouth_main_loc_get_attr_name[0], mouth_main_loc_get_attr_name[1], mouth_main_loc_get_attr_name[2])
        cmds.move(0, 0.5, 2, r=True)
        cmds.setAttr((upper_main_ctrl + '.rx'), 90)
        cmds.DeleteHistory()
        cmds.FreezeTransformations()
        self.grp_all_controller_def('Upper', value=1,
                                    ctrl_name=upper_main_ctrl)

        lower_main_ctrl = self.prefix_name + '_Lower_Mouth_' + str(self.val) + '_Main_Ctrl'
        upper_main_shape_name = lower_main_ctrl + 'Shape'
        mel.eval(
            'curve -d 1 -p -2.2346 0 -0.439213 -p -0.598042 0 0.439213 -p 0.598042 0 0.439213 -p 2.2346 0 -0.439213 -p -2.2346 0 -0.439213 -k 0 -k 1 -k 2 -k 3 -k 4 -n %s;' % lower_main_ctrl)
        shape_name = cmds.listRelatives(lower_main_ctrl, s=True)[0]
        cmds.rename(shape_name, upper_main_shape_name)
        # Template_Mouth_Tem_1_Main_LOC
        mouth_main_loc_name = self.prefix_name + '_Mouth_Tem_' + str(self.val) + '_Main_LOC'
        mouth_main_loc_get_attr_name = cmds.xform(mouth_main_loc_name, q=1, ws=1, rp=1)
        print(mouth_main_loc_get_attr_name)
        cmds.move(mouth_main_loc_get_attr_name[0], mouth_main_loc_get_attr_name[1], mouth_main_loc_get_attr_name[2])
        cmds.move(0, -0.5, 2, r=True)
        cmds.setAttr((lower_main_ctrl + '.rx'), -90)
        cmds.DeleteHistory()
        cmds.FreezeTransformations()
        self.grp_all_controller_def('Lower', value=1,
                                    ctrl_name=lower_main_ctrl)

        # Create a Square controller

        center_main_ctrl = self.prefix_name + '_Center_Mouth_' + str(self.val) + '_Main_Ctrl'
        upper_main_shape_name = center_main_ctrl + 'Shape'
        self.controller_class.square_ctrl()
        cmds.rename('Square_ctrl', center_main_ctrl)
        # Template_Mouth_Tem_1_Main_LOC
        mouth_main_loc_name = self.prefix_name + '_Mouth_Tem_' + str(self.val) + '_Main_LOC'
        mouth_main_loc_get_attr_name = cmds.xform(mouth_main_loc_name, q=1, ws=1, rp=1)
        print(mouth_main_loc_get_attr_name)
        cmds.move(mouth_main_loc_get_attr_name[0], mouth_main_loc_get_attr_name[1], mouth_main_loc_get_attr_name[2])
        cmds.move(0, 0, 2, r=True)
        cmds.setAttr((center_main_ctrl + '.sz'), 0.2)
        cmds.setAttr((center_main_ctrl + '.rx'), -90)
        cmds.DeleteHistory()
        cmds.FreezeTransformations()
        self.grp_all_controller_def('Center', value=1,
                                    ctrl_name=center_main_ctrl)

        cmds.select(upper_main_ctrl, lower_main_ctrl, center_main_ctrl)
        cmds.parent()
        cmds.select(center_main_ctrl, ctrl_grp_name)
        cmds.parent()

        self.final_grp(mouth_grp_name)

    def mouth_side_final_def(self):

        self.ctrl_list = []
        # Template_Mouth_Side_21_Tem_1_LOC
        loc_name = self.prefix_name + '_Mouth_Side_*_Tem_' + str(self.val) + '_LOC'
        cmds.select(loc_name)
        sel_loc = cmds.ls(sl=True)
        curve_pos_list = []
        curve_k_val = []
        a = 0
        while a < len(sel_loc):
            loc_name = self.prefix_name + '_Mouth_Side_' + str(a + 1) + '_Tem_' + str(self.val) + '_LOC'
            pos_val = cmds.xform(loc_name, q=1, ws=1, rp=1)

            curve_pos_list.append(pos_val)
            number = a + 1
            curve_k_val.append(number)

            common_name = self.prefix_name + '_Mouth_Side_' + str(a + 1) + '_' + str(self.val)
            new_loc_name = common_name + '_Loc'
            sphere_name = common_name + '_Secondary_Ctrl'
            sphere_grp_name = sphere_name + '_Grp'
            self.ctrl_list.append(sphere_name)

            cmds.spaceLocator(n=new_loc_name, p=(0, 0, 0))
            cmds.move(pos_val[0], pos_val[1], pos_val[2])

            cmds.polySphere(r=0.3, sx=6, sy=6, ax=(0, 1, 0), cuv=2, ch=1, n=sphere_name)
            cmds.move(pos_val[0], pos_val[1], pos_val[2])
            cmds.DeleteHistory()
            cmds.FreezeTransformations()
            cmds.select(sphere_name)
            cmds.group(n=sphere_grp_name)

            grp_common_name = self.prefix_name + '_Mouth_Side_' + str(self.val)
            loc_grp_name = grp_common_name + '_Loc_Grp'
            if cmds.objExists(loc_grp_name):
                cmds.select(new_loc_name, loc_grp_name)
                cmds.parent()
            else:
                cmds.select(new_loc_name)
                cmds.group(n=loc_grp_name)

            secondary_ctrl_grp_name = grp_common_name + '_Secondary_Ctrl_Grp'
            if cmds.objExists(secondary_ctrl_grp_name):
                cmds.select(sphere_grp_name, secondary_ctrl_grp_name)
                cmds.parent()
            else:
                cmds.select(sphere_grp_name)
                cmds.group(n=secondary_ctrl_grp_name)

            a += 1
        curve_name = self.prefix_name + '_Mouth_Side_Tem_' + str(self.val) + '_no_Smooth_Crv'
        curve_shape_name = curve_name + 'Shape'
        cmds.curve(n=curve_name, d=0, p=curve_pos_list,
                   k=curve_k_val)
        shape_name = cmds.listRelatives(curve_name, s=True)
        cmds.rename(shape_name[0], curve_shape_name)
        crv_grp_name = self.prefix_name + '_Mouth_Side_' + str(self.val) + '_Crv_Grp'
        cmds.select(curve_name)
        cmds.group(n=crv_grp_name)
        # Create a Each curve ane make a smooth
        mouth_side_smooth_crv_name = self.prefix_name + '_Mouth_Side_Tem_' + str(self.val) + '_Smooth_Crv'
        wire_name = self.prefix_name + '_Mouth_Side_Tem_' + str(self.val) + '_Wire'
        cmds.select(curve_name)
        cmds.duplicate(n=mouth_side_smooth_crv_name)
        cmds.rebuildCurve(mouth_side_smooth_crv_name, ch=0,
                          rpo=1, rt=0, end=1, kr=0, kcp=0, kep=1, kt=0, d=2, tol=0.01, s=9)
        cmds.select(mouth_side_smooth_crv_name)
        mel.eval('wire -gw false -en 1.000000 -ce 0.000000 -li 0.000000 -w %s %s;' % (
        mouth_side_smooth_crv_name, curve_name))
        list = cmds.listConnections(curve_shape_name, type='wire')
        cmds.rename(list[0], wire_name)

        a = 0
        while a < len(sel_loc):
            common_name = self.prefix_name + '_Mouth_Side_' + str(a + 1) + '_' + str(self.val)
            loc_new_name = common_name + '_Loc'
            sphere_name = common_name + '_Secondary_Ctrl'
            sphere_grp_name = sphere_name + '_Grp'

            poc_name = common_name + '_Poc'
            plus_minus_name = common_name + '_Plus_Minus'

            cmds.createNode('pointOnCurveInfo', n=poc_name)
            cmds.connectAttr((curve_shape_name + '.worldSpace[0]'),
                             (poc_name + '.inputCurve'),
                             f=True)
            cmds.setAttr((poc_name + '.parameter'), a + 1)
            cmds.connectAttr((poc_name + '.result.position'), (loc_new_name + '.t'))

            # get the loc val
            loc_value = cmds.getAttr(loc_new_name + '.t')[0]

            cmds.createNode('plusMinusAverage', n=plus_minus_name)
            mel.eval('AEnewNonNumericMultiAddNewItem("%s","input3D");' % plus_minus_name)
            mel.eval('AEnewNonNumericMultiAddNewItem("%s","input3D");' % plus_minus_name)
            cmds.connectAttr((loc_new_name + '.t'), (plus_minus_name + '.input3D[0]'))
            cmds.setAttr((plus_minus_name + '.input3D[1].input3Dx'), loc_value[0])
            cmds.setAttr((plus_minus_name + '.input3D[1].input3Dy'), loc_value[1])
            cmds.setAttr((plus_minus_name + '.input3D[1].input3Dz'), loc_value[2])
            cmds.setAttr((plus_minus_name + '.operation'), 2)

            cmds.connectAttr((plus_minus_name + '.output3D'), (sphere_grp_name + '.t'))

            a += 1

        vtx_no = [mouth_side_smooth_crv_name + '.cv[0]', mouth_side_smooth_crv_name + '.cv[10]']
        common = self.prefix_name + '_Mouth_Side_1_' + str(self.val)
        mouth_side_1_clu_handle, mouth_side_1_primary_ctrl = self.primary_ctrl_create(vtx_no, common)
        self.ctrl_list.append(mouth_side_1_primary_ctrl)

        vtx_no = [mouth_side_smooth_crv_name + '.cv[1]']
        common = self.prefix_name + '_Mouth_Side_2_' + str(self.val)
        mouth_side_2_clu_handle, mouth_side_2_primary_ctrl = self.primary_ctrl_create(vtx_no, common)
        self.ctrl_list.append(mouth_side_2_primary_ctrl)

        vtx_no = [mouth_side_smooth_crv_name + '.cv[2]']
        common = self.prefix_name + '_Mouth_Side_3_' + str(self.val)
        mouth_side_3_clu_handle, mouth_side_3_primary_ctrl = self.primary_ctrl_create(vtx_no, common)
        self.ctrl_list.append(mouth_side_3_primary_ctrl)

        vtx_no = [mouth_side_smooth_crv_name + '.cv[3]']
        common = self.prefix_name + '_Mouth_Side_4_' + str(self.val)
        mouth_side_4_clu_handle, mouth_side_4_primary_ctrl = self.primary_ctrl_create(vtx_no, common)
        self.ctrl_list.append(mouth_side_4_primary_ctrl)

        vtx_no = [mouth_side_smooth_crv_name + '.cv[4]']
        common = self.prefix_name + '_Mouth_Side_5_' + str(self.val)
        mouth_side_5_clu_handle, mouth_side_5_primary_ctrl = self.primary_ctrl_create(vtx_no, common)
        self.ctrl_list.append(mouth_side_5_primary_ctrl)

        vtx_no = [mouth_side_smooth_crv_name + '.cv[5]']
        common = self.prefix_name + '_Mouth_Side_6_' + str(self.val)
        mouth_side_6_clu_handle, mouth_side_6_primary_ctrl = self.primary_ctrl_create(vtx_no, common)
        self.ctrl_list.append(mouth_side_6_primary_ctrl)

        vtx_no = [mouth_side_smooth_crv_name + '.cv[6]']
        common = self.prefix_name + '_Mouth_Side_7_' + str(self.val)
        mouth_side_7_clu_handle, mouth_side_7_primary_ctrl = self.primary_ctrl_create(vtx_no, common)
        self.ctrl_list.append(mouth_side_7_primary_ctrl)

        vtx_no = [mouth_side_smooth_crv_name + '.cv[7]']
        common = self.prefix_name + '_Mouth_Side_8_' + str(self.val)
        mouth_side_8_clu_handle, mouth_side_8_primary_ctrl = self.primary_ctrl_create(vtx_no, common)
        self.ctrl_list.append(mouth_side_8_primary_ctrl)

        vtx_no = [mouth_side_smooth_crv_name + '.cv[8]']
        common = self.prefix_name + '_Mouth_Side_9_' + str(self.val)
        mouth_side_9_clu_handle, mouth_side_9_primary_ctrl = self.primary_ctrl_create(vtx_no, common)
        self.ctrl_list.append(mouth_side_9_primary_ctrl)

        vtx_no = [mouth_side_smooth_crv_name + '.cv[9]']
        common = self.prefix_name + '_Mouth_Side_10_' + str(self.val)
        mouth_side_10_clu_handle, mouth_side_10_primary_ctrl = self.primary_ctrl_create(vtx_no, common)
        self.ctrl_list.append(mouth_side_10_primary_ctrl)

        # Create cluster in one grp

        clu_grp_name = grp_common_name + '_Clu_Grp'
        cmds.select(mouth_side_1_clu_handle, mouth_side_2_clu_handle, mouth_side_3_clu_handle, mouth_side_4_clu_handle,
                    mouth_side_5_clu_handle,
                    mouth_side_6_clu_handle, mouth_side_7_clu_handle, mouth_side_8_clu_handle, mouth_side_9_clu_handle,
                    mouth_side_10_clu_handle)
        cmds.group(n=clu_grp_name)

        primary_ctrl_grp_name = grp_common_name + '_Primary_Ctrl_Grp'
        cmds.select(mouth_side_1_primary_ctrl, mouth_side_2_primary_ctrl, mouth_side_3_primary_ctrl,
                    mouth_side_4_primary_ctrl, mouth_side_5_primary_ctrl,
                    mouth_side_6_primary_ctrl, mouth_side_7_primary_ctrl, mouth_side_8_primary_ctrl,
                    mouth_side_9_primary_ctrl, mouth_side_10_primary_ctrl)
        cmds.group(n=primary_ctrl_grp_name)

        ctrl_grp_name = grp_common_name + '_Ctrl_Grp'
        cmds.select(primary_ctrl_grp_name, secondary_ctrl_grp_name)
        cmds.group(n=ctrl_grp_name)

        # put everything in one grp
        cmds.select(loc_grp_name, crv_grp_name, clu_grp_name, ctrl_grp_name)
        mouth_side_grp_name = self.prefix_name + '_Mouth_Side_' + str(self.val) + '_Grp'
        cmds.group(n=mouth_side_grp_name)

        list = [loc_grp_name, crv_grp_name, clu_grp_name]
        for each in list:
            cmds.setAttr((each + '.inheritsTransform'), 0)
            cmds.setAttr((each + '.v'), 0)

        # Upper Lower Side Ctrl
        # get the list of the controller
        slide_1_ctrl_name = self.prefix_name + '_Mouth_Side_1_' + str(self.val) + '_Ctrl'
        # upper_curve_primary_2_clu_handle_name
        get_pos = cmds.xform(mouth_side_4_clu_handle, q=1, ws=1, rp=1)
        self.controller_class.square_ctrl()
        cmds.rename('Square_ctrl', slide_1_ctrl_name)
        cmds.select(slide_1_ctrl_name)
        cmds.move(get_pos[0], get_pos[1], get_pos[2])
        cmds.setAttr((slide_1_ctrl_name + '.rx'), 90)
        cmds.setAttr((slide_1_ctrl_name + '.sx'), 2.5)
        cmds.setAttr((slide_1_ctrl_name + '.sz'), 0.5)
        cmds.move(0, 0, 0.5, r=True)
        cmds.DeleteHistory()
        cmds.FreezeTransformations()

        self.grp_all_controller_def('Upper', value=1,
                                    ctrl_name=slide_1_ctrl_name)

        slide_2_ctrl_name = self.prefix_name + '_Mouth_Side_2_' + str(self.val) + '_Ctrl'
        # upper_curve_primary_2_clu_handle_name
        get_pos = cmds.xform(mouth_side_8_clu_handle, q=1, ws=1, rp=1)
        self.controller_class.square_ctrl()
        cmds.rename('Square_ctrl', slide_2_ctrl_name)
        cmds.select(slide_2_ctrl_name)
        cmds.move(get_pos[0], get_pos[1], get_pos[2])
        cmds.setAttr((slide_2_ctrl_name + '.rx'), 90)
        cmds.setAttr((slide_2_ctrl_name + '.sx'), 2.5)
        cmds.setAttr((slide_2_ctrl_name + '.sz'), 0.5)
        cmds.move(0, 0, 0.5, r=True)
        cmds.DeleteHistory()
        cmds.FreezeTransformations()

        self.grp_all_controller_def('Lower', value=1,
                                    ctrl_name=slide_2_ctrl_name)

        slide_3_ctrl_name = self.prefix_name + '_Mouth_Side_3_' + str(self.val) + '_Ctrl'
        # upper_curve_primary_2_clu_handle_name
        get_pos = cmds.xform(mouth_side_1_clu_handle, q=1, ws=1, rp=1)
        self.controller_class.square_ctrl()
        cmds.rename('Square_ctrl', slide_3_ctrl_name)
        cmds.select(slide_3_ctrl_name)
        cmds.move(get_pos[0], get_pos[1], get_pos[2])
        cmds.setAttr((slide_3_ctrl_name + '.rx'), 90)
        cmds.setAttr((slide_3_ctrl_name + '.sx'), 0.2)
        cmds.setAttr((slide_3_ctrl_name + '.sz'), 2)
        cmds.move(0, 0, 0.5, r=True)
        cmds.DeleteHistory()
        cmds.FreezeTransformations()

        self.grp_all_controller_def('Side_1', value=1,
                                    ctrl_name=slide_3_ctrl_name)

        slide_4_ctrl_name = self.prefix_name + '_Mouth_Side_4_' + str(self.val) + '_Ctrl'
        # upper_curve_primary_2_clu_handle_name
        get_pos = cmds.xform(mouth_side_6_clu_handle, q=1, ws=1, rp=1)
        self.controller_class.square_ctrl()
        cmds.rename('Square_ctrl', slide_4_ctrl_name)
        cmds.select(slide_4_ctrl_name)
        cmds.move(get_pos[0], get_pos[1], get_pos[2])
        cmds.setAttr((slide_4_ctrl_name + '.rx'), 90)
        cmds.setAttr((slide_4_ctrl_name + '.sx'), 0.2)
        cmds.setAttr((slide_4_ctrl_name + '.sz'), 2)
        cmds.move(0, 0, 0.5, r=True)
        cmds.DeleteHistory()
        cmds.FreezeTransformations()

        self.grp_all_controller_def('Side_2', value=1,
                                    ctrl_name=slide_4_ctrl_name)

        slide_ctrl_grp_name = self.prefix_name + '_Mouth_Slide_' + str(self.val) + '_Ctrl_Grp'
        cmds.select(slide_1_ctrl_name, slide_2_ctrl_name, slide_3_ctrl_name, slide_4_ctrl_name)
        cmds.group(n=slide_ctrl_grp_name)

        cmds.select(slide_ctrl_grp_name, ctrl_grp_name)
        cmds.parent()

        self.final_grp(mouth_side_grp_name)

    def mouth_side_2_final(self, side):
        self.ctrl_list = []
        curve_pos_list = []
        curve_k_val = []
        loc_name = self.prefix_name + '_' + side + '_Mouth_Side_2_*_Tem_' + str(self.val) + '_LOC'
        cmds.select(loc_name)
        sel_loc = cmds.ls(sl=True)
        a = 0
        for each in sel_loc:
            loc_name = self.prefix_name + '_' + side + '_Mouth_Side_2_' + str(a + 1) + '_Tem_' + str(self.val) + '_LOC'
            loc_pos = cmds.xform(loc_name, q=1, ws=1, rp=1)

            curve_pos_list.append(loc_pos)
            number = a + 1
            curve_k_val.append(number)

            common_name = self.prefix_name + '_' + side + '_Mouth_Side_2_' + str(a + 1) + '_' + str(self.val)
            loc_new_name = common_name + '_Loc'
            sphere_name = common_name + '_Secondary_Ctrl'
            sphere_grp_name = sphere_name + '_Grp'

            cmds.spaceLocator(n=loc_new_name, p=(0, 0, 0))
            cmds.move(loc_pos[0], loc_pos[1], loc_pos[2])

            cmds.polySphere(r=0.3, sx=6, sy=6, ax=(0, 1, 0), cuv=2, ch=1, n=sphere_name)
            cmds.move(loc_pos[0], loc_pos[1], loc_pos[2])
            cmds.DeleteHistory()
            cmds.FreezeTransformations()
            cmds.select(sphere_name)
            cmds.group(n=sphere_grp_name)

            grp_common_name = self.prefix_name + '_' + side + '_Mouth_Side_2_' + str(self.val)
            loc_grp_name = grp_common_name + '_Loc_Grp'
            if cmds.objExists(loc_grp_name):
                cmds.select(loc_new_name, loc_grp_name)
                cmds.parent()
            else:
                cmds.select(loc_new_name)
                cmds.group(n=loc_grp_name)

            secondary_ctrl_grp_name = grp_common_name + '_Secondary_Ctrl_Grp'
            if cmds.objExists(secondary_ctrl_grp_name):
                cmds.select(sphere_grp_name, secondary_ctrl_grp_name)
                cmds.parent()
            else:
                cmds.select(sphere_grp_name)
                cmds.group(n=secondary_ctrl_grp_name)

            a += 1

        curve_name = self.prefix_name + '_' + side + '_Mouth_Side_2_' + str(self.val) + '_no_Smooth_Crv'
        curve_shape_name = curve_name + 'Shape'
        cmds.curve(n=curve_name, d=0, p=curve_pos_list,
                   k=curve_k_val)
        shape_name = cmds.listRelatives(curve_name, s=True)
        cmds.rename(shape_name[0], curve_shape_name)
        crv_grp_name = self.prefix_name + '_' + side + '_Mouth_Side_2_' + str(self.val) + '_Crv_Grp'
        cmds.select(curve_name)
        cmds.group(n=crv_grp_name)
        # Create a Each curve ane make a smooth
        mouth_side_smooth_crv_name = self.prefix_name + '_' + side + '_Mouth_Side_2_' + str(self.val) + '_Smooth_Crv'
        wire_name = self.prefix_name + '_' + side + '_Mouth_Side_2_' + str(self.val) + '_Wire'
        cmds.select(curve_name)
        cmds.duplicate(n=mouth_side_smooth_crv_name)
        cmds.rebuildCurve(mouth_side_smooth_crv_name, ch=0,
                          rpo=1, rt=0, end=1, kr=0, kcp=0, kep=1, kt=0, d=2, tol=0.01, s=1)
        cmds.select(mouth_side_smooth_crv_name)
        mel.eval('wire -gw false -en 1.000000 -ce 0.000000 -li 0.000000 -w %s %s;' % (
        mouth_side_smooth_crv_name, curve_name))
        list = cmds.listConnections(curve_shape_name, type='wire')
        cmds.rename(list[0], wire_name)

        a = 0
        while a < len(sel_loc):
            common_name = self.prefix_name + '_' + side + '_Mouth_Side_2_' + str(a + 1) + '_' + str(self.val)
            loc_new_name = common_name + '_Loc'
            sphere_name = common_name + '_Secondary_Ctrl'
            sphere_grp_name = sphere_name + '_Grp'

            poc_name = common_name + '_Poc'
            plus_minus_name = common_name + '_Plus_Minus'

            cmds.createNode('pointOnCurveInfo', n=poc_name)
            cmds.connectAttr((curve_shape_name + '.worldSpace[0]'),
                             (poc_name + '.inputCurve'),
                             f=True)
            cmds.setAttr((poc_name + '.parameter'), a + 1)
            cmds.connectAttr((poc_name + '.result.position'), (loc_new_name + '.t'))

            # get the loc val
            loc_value = cmds.getAttr(loc_new_name + '.t')[0]

            cmds.createNode('plusMinusAverage', n=plus_minus_name)
            mel.eval('AEnewNonNumericMultiAddNewItem("%s","input3D");' % plus_minus_name)
            mel.eval('AEnewNonNumericMultiAddNewItem("%s","input3D");' % plus_minus_name)
            cmds.connectAttr((loc_new_name + '.t'), (plus_minus_name + '.input3D[0]'))
            cmds.setAttr((plus_minus_name + '.input3D[1].input3Dx'), loc_value[0])
            cmds.setAttr((plus_minus_name + '.input3D[1].input3Dy'), loc_value[1])
            cmds.setAttr((plus_minus_name + '.input3D[1].input3Dz'), loc_value[2])
            cmds.setAttr((plus_minus_name + '.operation'), 2)

            cmds.connectAttr((plus_minus_name + '.output3D'), (sphere_grp_name + '.t'))

            a += 1

        vtx_no = [mouth_side_smooth_crv_name + '.cv[0]']
        common = self.prefix_name + '_' + side + '_Mouth_Side_2_1_' + str(self.val)
        mouth_side_2_1_clu_handle, mouth_side_2_1_primary_ctrl = self.primary_ctrl_create(vtx_no, common)
        self.ctrl_list.append(mouth_side_2_1_primary_ctrl)

        vtx_no = [mouth_side_smooth_crv_name + '.cv[1]']
        common = self.prefix_name + '_' + side + '_Mouth_Side_2_2_' + str(self.val)
        mouth_side_2_2_clu_handle, mouth_side_2_2_primary_ctrl = self.primary_ctrl_create(vtx_no, common)
        self.ctrl_list.append(mouth_side_2_2_primary_ctrl)

        vtx_no = [mouth_side_smooth_crv_name + '.cv[2]']
        common = self.prefix_name + '_' + side + '_Mouth_Side_2_3_' + str(self.val)
        mouth_side_2_3_clu_handle, mouth_side_2_3_primary_ctrl = self.primary_ctrl_create(vtx_no, common)
        self.ctrl_list.append(mouth_side_2_3_primary_ctrl)

        vtx_no = [mouth_side_smooth_crv_name + '.cv[3]']
        common = self.prefix_name + '_' + side + '_Mouth_Side_2_4_' + str(self.val)
        mouth_side_2_4_clu_handle, mouth_side_2_4_primary_ctrl = self.primary_ctrl_create(vtx_no, common)
        self.ctrl_list.append(mouth_side_2_4_primary_ctrl)

        clu_grp_name = grp_common_name + '_Clu_Grp'
        cmds.select(mouth_side_2_1_clu_handle, mouth_side_2_2_clu_handle, mouth_side_2_3_clu_handle,
                    mouth_side_2_4_clu_handle)
        cmds.group(n=clu_grp_name)

        primary_ctrl_grp_name = grp_common_name + '_Primary_Ctrl_Grp'
        cmds.select(mouth_side_2_1_primary_ctrl, mouth_side_2_2_primary_ctrl, mouth_side_2_3_primary_ctrl,
                    mouth_side_2_4_primary_ctrl)
        cmds.group(n=primary_ctrl_grp_name)

        ctrl_grp_name = grp_common_name + '_Ctrl_Grp'
        cmds.select(secondary_ctrl_grp_name, primary_ctrl_grp_name)
        cmds.group(n=ctrl_grp_name)

        mouth_side_2_grp = grp_common_name + '_Grp'
        cmds.select(loc_grp_name, clu_grp_name, ctrl_grp_name, crv_grp_name)
        cmds.group(n=mouth_side_2_grp)

        list = [loc_grp_name, clu_grp_name, crv_grp_name]
        for each in list:
            cmds.setAttr((each + '.inheritsTransform'), 0)
            cmds.setAttr((each + '.v'), 0)

        self.final_grp(mouth_side_2_grp)

    def face_center_final(self):
        self.ctrl_list = []
        curve_pos_list = []
        curve_k_val = []
        # Template_Face_Center_1_Tem_1_LOC
        loc_name = self.prefix_name + '_Face_Center_*_Tem_' + str(self.val) + '_LOC'
        cmds.select(loc_name)
        sel_loc = cmds.ls(sl=True)
        a = 0
        for each in sel_loc:
            loc_name = self.prefix_name + '_Face_Center_' + str(a + 1) + '_Tem_' + str(self.val) + '_LOC'
            loc_pos = cmds.xform(loc_name, q=1, ws=1, rp=1)

            curve_pos_list.append(loc_pos)
            number = a + 1
            curve_k_val.append(number)

            common_name = self.prefix_name + '_Face_Center_' + str(a + 1) + '_' + str(self.val)
            loc_new_name = common_name + '_Loc'
            sphere_name = common_name + '_Secondary_Ctrl'
            sphere_grp_name = sphere_name + '_Grp'

            cmds.spaceLocator(n=loc_new_name, p=(0, 0, 0))
            cmds.move(loc_pos[0], loc_pos[1], loc_pos[2])

            cmds.polySphere(r=0.3, sx=6, sy=6, ax=(0, 1, 0), cuv=2, ch=1, n=sphere_name)
            cmds.move(loc_pos[0], loc_pos[1], loc_pos[2])
            cmds.DeleteHistory()
            cmds.FreezeTransformations()
            cmds.select(sphere_name)
            cmds.group(n=sphere_grp_name)

            grp_common_name = self.prefix_name + '_Face_Center_' + str(self.val)
            loc_grp_name = grp_common_name + '_Loc_Grp'
            if cmds.objExists(loc_grp_name):
                cmds.select(loc_new_name, loc_grp_name)
                cmds.parent()
            else:
                cmds.select(loc_new_name)
                cmds.group(n=loc_grp_name)

            secondary_ctrl_grp_name = grp_common_name + '_Secondary_Ctrl_Grp'
            if cmds.objExists(secondary_ctrl_grp_name):
                cmds.select(sphere_grp_name, secondary_ctrl_grp_name)
                cmds.parent()
            else:
                cmds.select(sphere_grp_name)
                cmds.group(n=secondary_ctrl_grp_name)

            a += 1

        curve_name = self.prefix_name + '_Face_Center_' + str(self.val) + '_no_Smooth_Crv'
        curve_shape_name = curve_name + 'Shape'
        cmds.curve(n=curve_name, d=0, p=curve_pos_list,
                   k=curve_k_val)
        shape_name = cmds.listRelatives(curve_name, s=True)
        cmds.rename(shape_name[0], curve_shape_name)
        crv_grp_name = self.prefix_name + '_Face_Center_' + str(self.val) + '_Crv_Grp'
        cmds.select(curve_name)
        cmds.group(n=crv_grp_name)
        # Create a Each curve ane make a smooth
        mouth_side_smooth_crv_name = self.prefix_name + '_Face_Center_' + str(self.val) + '_Smooth_Crv'
        wire_name = self.prefix_name + '_Face_Center_' + str(self.val) + '_Wire'
        cmds.select(curve_name)
        cmds.duplicate(n=mouth_side_smooth_crv_name)
        cmds.rebuildCurve(mouth_side_smooth_crv_name, ch=0,
                          rpo=1, rt=0, end=1, kr=0, kcp=0, kep=1, kt=0, d=2, tol=0.01, s=1)
        cmds.select(mouth_side_smooth_crv_name)
        mel.eval('wire -gw false -en 1.000000 -ce 0.000000 -li 0.000000 -w %s %s;' % (
        mouth_side_smooth_crv_name, curve_name))
        list = cmds.listConnections(curve_shape_name, type='wire')
        cmds.rename(list[0], wire_name)

        a = 0
        while a < len(sel_loc):
            common_name = self.prefix_name + '_Face_Center_' + str(a + 1) + '_' + str(self.val)
            loc_new_name = common_name + '_Loc'
            sphere_name = common_name + '_Secondary_Ctrl'
            sphere_grp_name = sphere_name + '_Grp'

            poc_name = common_name + '_Poc'
            plus_minus_name = common_name + '_Plus_Minus'

            cmds.createNode('pointOnCurveInfo', n=poc_name)
            cmds.connectAttr((curve_shape_name + '.worldSpace[0]'),
                             (poc_name + '.inputCurve'),
                             f=True)
            cmds.setAttr((poc_name + '.parameter'), a + 1)
            cmds.connectAttr((poc_name + '.result.position'), (loc_new_name + '.t'))

            # get the loc val
            loc_value = cmds.getAttr(loc_new_name + '.t')[0]

            cmds.createNode('plusMinusAverage', n=plus_minus_name)
            mel.eval('AEnewNonNumericMultiAddNewItem("%s","input3D");' % plus_minus_name)
            mel.eval('AEnewNonNumericMultiAddNewItem("%s","input3D");' % plus_minus_name)
            cmds.connectAttr((loc_new_name + '.t'), (plus_minus_name + '.input3D[0]'))
            cmds.setAttr((plus_minus_name + '.input3D[1].input3Dx'), loc_value[0])
            cmds.setAttr((plus_minus_name + '.input3D[1].input3Dy'), loc_value[1])
            cmds.setAttr((plus_minus_name + '.input3D[1].input3Dz'), loc_value[2])
            cmds.setAttr((plus_minus_name + '.operation'), 2)

            cmds.connectAttr((plus_minus_name + '.output3D'), (sphere_grp_name + '.t'))

            a += 1

        vtx_no = [mouth_side_smooth_crv_name + '.cv[0]']
        common = self.prefix_name + '_Face_Center_slide_1_' + str(self.val)
        mouth_side_2_1_clu_handle, mouth_side_2_1_primary_ctrl = self.primary_ctrl_create(vtx_no, common)
        self.ctrl_list.append(mouth_side_2_1_primary_ctrl)

        vtx_no = [mouth_side_smooth_crv_name + '.cv[1]']
        common = self.prefix_name + '_Face_Center_slide_2_' + str(self.val)
        mouth_side_2_2_clu_handle, mouth_side_2_2_primary_ctrl = self.primary_ctrl_create(vtx_no, common)
        self.ctrl_list.append(mouth_side_2_2_primary_ctrl)

        vtx_no = [mouth_side_smooth_crv_name + '.cv[2]']
        common = self.prefix_name + '_Face_Center_slide_3_' + str(self.val)
        mouth_side_2_3_clu_handle, mouth_side_2_3_primary_ctrl = self.primary_ctrl_create(vtx_no, common)
        self.ctrl_list.append(mouth_side_2_3_primary_ctrl)

        vtx_no = [mouth_side_smooth_crv_name + '.cv[3]']
        common = self.prefix_name + '_Face_Center_slide_4_' + str(self.val)
        mouth_side_2_4_clu_handle, mouth_side_2_4_primary_ctrl = self.primary_ctrl_create(vtx_no, common)
        self.ctrl_list.append(mouth_side_2_4_primary_ctrl)

        clu_grp_name = grp_common_name + '_Clu_Grp'
        cmds.select(mouth_side_2_1_clu_handle, mouth_side_2_2_clu_handle, mouth_side_2_3_clu_handle,
                    mouth_side_2_4_clu_handle)
        cmds.group(n=clu_grp_name)

        primary_ctrl_grp_name = grp_common_name + '_Primary_Ctrl_Grp'
        cmds.select(mouth_side_2_1_primary_ctrl, mouth_side_2_2_primary_ctrl, mouth_side_2_3_primary_ctrl,
                    mouth_side_2_4_primary_ctrl)
        cmds.group(n=primary_ctrl_grp_name)

        ctrl_grp_name = grp_common_name + '_Ctrl_Grp'
        cmds.select(secondary_ctrl_grp_name, primary_ctrl_grp_name)
        cmds.group(n=ctrl_grp_name)

        mouth_side_2_grp = grp_common_name + '_Grp'
        cmds.select(loc_grp_name, clu_grp_name, ctrl_grp_name, crv_grp_name)
        cmds.group(n=mouth_side_2_grp)

        list = [loc_grp_name, clu_grp_name, crv_grp_name]
        for each in list:
            cmds.setAttr((each + '.inheritsTransform'), 0)
            cmds.setAttr((each + '.v'), 0)

        self.final_grp(mouth_side_2_grp)

    def nose_side_final(self, side):
        self.ctrl_list = []
        curve_pos_list = []
        curve_k_val = []
        loc_name = self.prefix_name + '_' + side + '_Nose_Side_*_Tem_' + str(self.val) + '_LOC'
        cmds.select(loc_name)
        sel_loc = cmds.ls(sl=True)
        a = 0
        for each in sel_loc:
            loc_name = self.prefix_name + '_' + side + '_Nose_Side_' + str(a + 1) + '_Tem_' + str(self.val) + '_LOC'
            loc_pos = cmds.xform(loc_name, q=1, ws=1, rp=1)

            curve_pos_list.append(loc_pos)
            number = a + 1
            curve_k_val.append(number)

            common_name = self.prefix_name + '_' + side + '_Nose_Side_' + str(a + 1) + '_' + str(self.val)
            loc_new_name = common_name + '_Loc'
            sphere_name = common_name + '_Secondary_Ctrl'
            sphere_grp_name = sphere_name + '_Grp'

            cmds.spaceLocator(n=loc_new_name, p=(0, 0, 0))
            cmds.move(loc_pos[0], loc_pos[1], loc_pos[2])

            cmds.polySphere(r=0.3, sx=6, sy=6, ax=(0, 1, 0), cuv=2, ch=1, n=sphere_name)
            cmds.move(loc_pos[0], loc_pos[1], loc_pos[2])
            cmds.DeleteHistory()
            cmds.FreezeTransformations()
            cmds.select(sphere_name)
            cmds.group(n=sphere_grp_name)

            grp_common_name = self.prefix_name + '_' + side + '_Nose_Side_' + str(self.val)
            loc_grp_name = grp_common_name + '_Loc_Grp'
            if cmds.objExists(loc_grp_name):
                cmds.select(loc_new_name, loc_grp_name)
                cmds.parent()
            else:
                cmds.select(loc_new_name)
                cmds.group(n=loc_grp_name)

            secondary_ctrl_grp_name = grp_common_name + '_Secondary_Ctrl_Grp'
            if cmds.objExists(secondary_ctrl_grp_name):
                cmds.select(sphere_grp_name, secondary_ctrl_grp_name)
                cmds.parent()
            else:
                cmds.select(sphere_grp_name)
                cmds.group(n=secondary_ctrl_grp_name)

            a += 1

        curve_name = self.prefix_name + '_' + side + '_Nose_Side_' + str(self.val) + '_no_Smooth_Crv'
        curve_shape_name = curve_name + 'Shape'
        cmds.curve(n=curve_name, d=0, p=curve_pos_list,
                   k=curve_k_val)
        shape_name = cmds.listRelatives(curve_name, s=True)
        cmds.rename(shape_name[0], curve_shape_name)
        crv_grp_name = self.prefix_name + '_' + side + '_Nose_Side_' + str(self.val) + '_Crv_Grp'
        cmds.select(curve_name)
        cmds.group(n=crv_grp_name)
        # Create a Each curve ane make a smooth
        mouth_side_smooth_crv_name = self.prefix_name + '_' + side + '_Nose_Side_' + str(self.val) + '_Smooth_Crv'
        wire_name = self.prefix_name + '_' + side + '_Nose_Side_' + str(self.val) + '_Wire'
        cmds.select(curve_name)
        cmds.duplicate(n=mouth_side_smooth_crv_name)
        cmds.rebuildCurve(mouth_side_smooth_crv_name, ch=0,
                          rpo=1, rt=0, end=1, kr=0, kcp=0, kep=1, kt=0, d=2, tol=0.01, s=1)
        cmds.select(mouth_side_smooth_crv_name)
        mel.eval('wire -gw false -en 1.000000 -ce 0.000000 -li 0.000000 -w %s %s;' % (
        mouth_side_smooth_crv_name, curve_name))
        list = cmds.listConnections(curve_shape_name, type='wire')
        cmds.rename(list[0], wire_name)

        a = 0
        while a < len(sel_loc):
            common_name = self.prefix_name + '_' + side + '_Nose_Side_' + str(a + 1) + '_' + str(self.val)
            loc_new_name = common_name + '_Loc'
            sphere_name = common_name + '_Secondary_Ctrl'
            sphere_grp_name = sphere_name + '_Grp'

            poc_name = common_name + '_Poc'
            plus_minus_name = common_name + '_Plus_Minus'

            cmds.createNode('pointOnCurveInfo', n=poc_name)
            cmds.connectAttr((curve_shape_name + '.worldSpace[0]'),
                             (poc_name + '.inputCurve'),
                             f=True)
            cmds.setAttr((poc_name + '.parameter'), a + 1)
            cmds.connectAttr((poc_name + '.result.position'), (loc_new_name + '.t'))

            # get the loc val
            loc_value = cmds.getAttr(loc_new_name + '.t')[0]

            cmds.createNode('plusMinusAverage', n=plus_minus_name)
            mel.eval('AEnewNonNumericMultiAddNewItem("%s","input3D");' % plus_minus_name)
            mel.eval('AEnewNonNumericMultiAddNewItem("%s","input3D");' % plus_minus_name)
            cmds.connectAttr((loc_new_name + '.t'), (plus_minus_name + '.input3D[0]'))
            cmds.setAttr((plus_minus_name + '.input3D[1].input3Dx'), loc_value[0])
            cmds.setAttr((plus_minus_name + '.input3D[1].input3Dy'), loc_value[1])
            cmds.setAttr((plus_minus_name + '.input3D[1].input3Dz'), loc_value[2])
            cmds.setAttr((plus_minus_name + '.operation'), 2)

            cmds.connectAttr((plus_minus_name + '.output3D'), (sphere_grp_name + '.t'))

            a += 1

        vtx_no = [mouth_side_smooth_crv_name + '.cv[0]']
        common = self.prefix_name + '_' + side + '_Nose_Side_1_' + str(self.val)
        mouth_side_2_1_clu_handle, mouth_side_2_1_primary_ctrl = self.primary_ctrl_create(vtx_no, common)
        self.ctrl_list.append(mouth_side_2_1_primary_ctrl)

        vtx_no = [mouth_side_smooth_crv_name + '.cv[1]']
        common = self.prefix_name + '_' + side + '_Nose_Side_2_' + str(self.val)
        mouth_side_2_2_clu_handle, mouth_side_2_2_primary_ctrl = self.primary_ctrl_create(vtx_no, common)
        self.ctrl_list.append(mouth_side_2_2_primary_ctrl)

        vtx_no = [mouth_side_smooth_crv_name + '.cv[2]']
        common = self.prefix_name + '_' + side + '_Nose_Side_3_' + str(self.val)
        mouth_side_2_3_clu_handle, mouth_side_2_3_primary_ctrl = self.primary_ctrl_create(vtx_no, common)
        self.ctrl_list.append(mouth_side_2_3_primary_ctrl)

        vtx_no = [mouth_side_smooth_crv_name + '.cv[3]']
        common = self.prefix_name + '_' + side + '_Nose_Side_4_' + str(self.val)
        mouth_side_2_4_clu_handle, mouth_side_2_4_primary_ctrl = self.primary_ctrl_create(vtx_no, common)
        self.ctrl_list.append(mouth_side_2_4_primary_ctrl)

        clu_grp_name = grp_common_name + '_Clu_Grp'
        cmds.select(mouth_side_2_1_clu_handle, mouth_side_2_2_clu_handle, mouth_side_2_3_clu_handle,
                    mouth_side_2_4_clu_handle)
        cmds.group(n=clu_grp_name)

        primary_ctrl_grp_name = grp_common_name + '_Primary_Ctrl_Grp'
        cmds.select(mouth_side_2_1_primary_ctrl, mouth_side_2_2_primary_ctrl, mouth_side_2_3_primary_ctrl,
                    mouth_side_2_4_primary_ctrl)
        cmds.group(n=primary_ctrl_grp_name)

        ctrl_grp_name = grp_common_name + '_Ctrl_Grp'
        cmds.select(secondary_ctrl_grp_name, primary_ctrl_grp_name)
        cmds.group(n=ctrl_grp_name)

        mouth_side_2_grp = grp_common_name + '_Grp'
        cmds.select(loc_grp_name, clu_grp_name, ctrl_grp_name, crv_grp_name)
        cmds.group(n=mouth_side_2_grp)

        list = [loc_grp_name, clu_grp_name, crv_grp_name]
        for each in list:
            cmds.setAttr((each + '.inheritsTransform'), 0)
            cmds.setAttr((each + '.v'), 0)

        self.final_grp(mouth_side_2_grp)
