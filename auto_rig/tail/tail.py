class TAIL:
    def __init__(self):
        self.helper_class = helper.HELPER()
        self.controller_class = controller_rig.controler()

    def new(self,widget,layout):
        self.tail_grid_layout = QtGui.QGridLayout()
        self.tail_grid_layout.setObjectName("tail_grid_layout")

        #SEGMENT LABEL
        self.tail_segment_label = QtGui.QLabel(widget)
        self.tail_segment_label.setObjectName("tail_segment_label")
        self.tail_segment_label.setText('Tail Segment')
        self.tail_grid_layout.addWidget(self.tail_segment_label, 0, 0, 1, 1)
        #SEGMENT LINE EDIT
        self.tail_segment_line_edit = QtGui.QLineEdit(widget)
        self.tail_segment_line_edit.setObjectName("tail_segment_line_edit")
        self.validator = QtGui.QDoubleValidator()
        self.tail_segment_line_edit.setValidator(self.validator)
        self.tail_segment_line_edit.setText(str(8))
        self.tail_grid_layout.addWidget(self.tail_segment_line_edit, 0, 1, 1, 1)

        #TAIL BUTTON
        self.create_tail_button = QtGui.QPushButton(widget)
        self.create_tail_button.setObjectName("create_tail_button")
        self.create_tail_button.setText('Create Tail')
        self.create_tail_button.clicked.connect(self.tail_query_def)
        self.tail_grid_layout.addWidget(self.create_tail_button, 1, 0, 1, 2)

        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.tail_grid_layout.addItem(spacerItem, 2, 0, 1, 1)
        layout.addLayout(self.tail_grid_layout)

    def new_clear(self):
        self.helper_class.clearLayout(self.tail_grid_layout)

    def tail_query_def(self):
        self.tail_segment_line_edit_query = int(self.tail_segment_line_edit.text())

        if cmds.objExists("*_Tail_Tem_*_Main_Grp"):
            cmds.select("*_Tail_Tem_*_Main_Grp")
            sel_main_grp = cmds.ls(sl=True)
            len_sel_main_grp = len(sel_main_grp)
            self.val = len_sel_main_grp + 1
        else:
            self.val = 1

        self.prefix_name = 'Template'
        self.base_ctrl_color = 'Yellow'
        self.cylinder_ctrl_roate = [90,0,0]
        self.cylinder_rotate = [90,0,0]


        self.tail_def(pos=[0,0,0])

    def tail_def(self,pos):
        self.sphere_list = []
        self.cluster_list = []
        self.cylinder_list = []
        self.ctrl_list = []
        self.crv_list = []
        default_pos = -2
        a = 0
        while a < self.tail_segment_line_edit_query:

            if a  == 0:
                self.tail_common_name  = self.prefix_name + '_Tail_Base_Tem_' + str(self.val)
                self.sphere_name = self.tail_common_name + '_Geo'
                self.sphere_clu_name = self.tail_common_name + '_Clu'
                self.sphere_clu_handle_name = self.sphere_clu_name + 'Handle'
                self.sphere_list.append(self.sphere_name)
                self.cluster_list.append(self.sphere_clu_handle_name)
                self.pos = pos
                self.helper_class.set_sphere_position(self.sphere_name,
                                                      self.pos,
                                                      self.sphere_clu_name)


                #create a cylinder
                #create a controller
                self.cylinder_ctrl_name = self.prefix_name + '_Tail_Base_Tem_' + str(self.val) + '_Ctrl'
                self.ctrl_list.append(self.cylinder_ctrl_name)
                self.cylinder_ctrl_size_ctrl = [0.5,0.5,0.5]
                self.cylinder_parent_const_list = [self.sphere_clu_handle_name]
                self.cylinder_ctrl_color = 'Yellow'
                self.cylinder_ctrl_freez_trans = True
                self.cylinder_ctrl_freez_rotate = True
                self.cylinder_ctrl_freez_scale = True
                self.helper_class.set_controller(self.cylinder_ctrl_name,self.pos,self.cylinder_ctrl_size_ctrl,
                                                 self.cylinder_ctrl_roate,self.cylinder_parent_const_list,self.cylinder_parent_const_list,
                                                 color=self.cylinder_ctrl_color,
                                                 freez_trans = self.cylinder_ctrl_freez_trans,
                                                 freez_rotate = self.cylinder_ctrl_freez_rotate,
                                                 freez_scale = self.cylinder_ctrl_freez_scale)


            self.tail_common_name  = self.prefix_name + '_Tail_' + str(a+1) + '_Tem_' + str(self.val)
            self.sphere_name = self.tail_common_name + '_Geo'
            self.sphere_clu_name = self.tail_common_name + '_Clu'
            self.sphere_clu_handle_name = self.sphere_clu_name + 'Handle'
            self.sphere_list.append(self.sphere_name)
            self.cluster_list.append(self.sphere_clu_handle_name)
            self.sphere_list.append(self.sphere_name)
            self.cluster_list.append(self.sphere_clu_handle_name)
            self.pos = [0,0,default_pos]
            self.helper_class.set_sphere_position(self.sphere_name,
                                                  self.pos,
                                                  self.sphere_clu_name)


            #create a cylinder
            #create a controller
            self.cylinder_ctrl_name = self.prefix_name + '_Tail_'  + str(a+1) + "_Tem_" + str(self.val) + '_Ctrl'
            self.ctrl_list.append(self.cylinder_ctrl_name)
            self.cylinder_ctrl_size_ctrl = [0.5,0.5,0.5]
            self.cylinder_parent_const_list = [self.sphere_clu_handle_name]
            self.cylinder_ctrl_color = 'Yellow'
            self.cylinder_ctrl_freez_trans = True
            self.cylinder_ctrl_freez_rotate = True
            self.cylinder_ctrl_freez_scale = True
            self.helper_class.set_controller(self.cylinder_ctrl_name,self.pos,self.cylinder_ctrl_size_ctrl,
                                             self.cylinder_ctrl_roate,self.cylinder_parent_const_list,self.cylinder_parent_const_list,
                                             color=self.cylinder_ctrl_color,
                                             freez_trans = self.cylinder_ctrl_freez_trans,
                                             freez_rotate = self.cylinder_ctrl_freez_rotate,
                                             freez_scale = self.cylinder_ctrl_freez_scale)

            if a+1 != 1:
                self.cylinder_name = self.prefix_name + '_Tail_' + str(a) + "_" + str(a+1) + "_Tem_" + str(self.val) + "_Geo"
                self.cylinder_list.append(self.cylinder_name)
                self.cylinder_upper_cluster_name = self.prefix_name + '_Tail_Upper_' + str(a) + "_" + str(a+1) + "_Tem_" + str(self.val) + "_Clu"
                self.cylinder_upper_cluster_handle_name = self.cylinder_upper_cluster_name + 'Handle'
                self.cluster_list.append(self.cylinder_upper_cluster_handle_name)
                self.cylinder_lower_cluster_name = self.prefix_name + '_Tail_Lower_' + str(a) + "_" + str(a+1) + "_Tem_" + str(self.val) + "_Clu"
                self.cylinder_lower_cluster_handle_name = self.cylinder_lower_cluster_name + 'Handle'
                self.cluster_list.append(self.cylinder_lower_cluster_handle_name)
                ##########################self.prefix_name + '_Tail_' + str(a+1) + '_Tem_' + str(self.val)
                self.current_sphere_name = self.prefix_name + '_Tail_' + str(a) + '_Tem_' + str(self.val) + "_Geo"
                self.helper_class.set_cylinder_position(self.cylinder_name,
                                                        self.cylinder_lower_cluster_name,
                                                        self.cylinder_upper_cluster_name,
                                                        self.current_sphere_name,
                                                        self.sphere_name,
                                                        rotate_val=self.cylinder_rotate)
            default_pos -=2
            a+=1

        a = 0
        while a < self.tail_segment_line_edit_query:

            if a == 0:
                self.tail_common_name  = self.prefix_name + '_Tail_' + str(a+1) + '_Tem_' + str(self.val)
                self.sphere_name = self.tail_common_name + '_Geo'
                #create a cylinder
                self.cylinder_name = self.prefix_name + '_Tail_Base_' + str(a+1) + "_Tem_" + str(self.val) + "_Geo"
                self.cylinder_list.append(self.cylinder_name)
                self.cylinder_upper_cluster_name = self.prefix_name + '_Tail_Upper_Base_' + str(a+1) + "_Tem_" + str(self.val) + "_Clu"
                self.cylinder_upper_cluster_handle_name = self.cylinder_upper_cluster_name + 'Handle'
                self.cylinder_lower_cluster_name = self.prefix_name + '_Tail_Lower_Base_' + str(a+1) + "_Tem_" + str(self.val) + "_Clu"
                self.cylinder_lower_cluster_handle_name = self.cylinder_lower_cluster_name + 'Handle'
                self.cluster_list.append(self.cylinder_upper_cluster_handle_name)
                self.cluster_list.append(self.cylinder_lower_cluster_handle_name)

                self.current_sphere_name = self.prefix_name + '_Tail_Base_Tem_' + str(self.val) + "_Geo"
                self.helper_class.set_cylinder_position(self.cylinder_name,
                                                        self.cylinder_lower_cluster_name,
                                                        self.cylinder_upper_cluster_name,
                                                        self.current_sphere_name,
                                                        self.sphere_name,
                                                        rotate_val=self.cylinder_rotate)
                #Template_Tail_Base_0_Tem_2_Ctrl
                self.base_ctrl_name = self.prefix_name + '_Tail_Base_Tem_' + str(self.val) + '_Ctrl'
                #Template_Tail_Lower_Base_1_Tem_2_CluHandle
                self.lower_cluster = self.prefix_name + '_Tail_Lower_Base_'  + str(a+1) + "_Tem_" + str(self.val) + "_CluHandle"
                self.tail_common_name  = self.prefix_name + '_Tail_Base_Tem_' + str(self.val)
                self.sphere_clu_name = self.tail_common_name + '_Clu'
                self.sphere_clu_handle_name = self.sphere_clu_name + 'Handle'
                cmds.parentConstraint(self.base_ctrl_name,self.lower_cluster,mo=False)
                cmds.parentConstraint(self.base_ctrl_name,self.sphere_clu_handle_name,mo=False)


                #Template_Tail_0_1_Tem_2_Ctrl
                ctrl_name = self.prefix_name + '_Tail_' + str(a+1) + "_Tem_" + str(self.val) + '_Ctrl'
                #upper_cluster handle
                #Template_Tail_Upper_Base_1_Tem_2_CluHandle
                cluster_upper_handle = self.prefix_name + '_Tail_Upper_Base_' +  str(a+1) + "_Tem_" + str(self.val) + '_CluHandle'

                #lower cluster_handle
                #Template_Tail_Lower_1_2_Tem_2_CluHandle
                cluster_lower_handle = self.prefix_name + '_Tail_Lower_' + str(a+1) + "_" + str(a+2) + "_Tem_" + str(self.val) + "_CluHandle"
                cmds.parentConstraint(ctrl_name,cluster_upper_handle,mo=False)
                cmds.parentConstraint(ctrl_name,cluster_lower_handle,mo=False)
                next_ctrl = self.prefix_name + '_Tail_' + str(a+2)  + "_Tem_" + str(self.val) + '_Ctrl'


                cmds.select(ctrl_name,self.base_ctrl_name)
                cmds.parent()

                cmds.select(next_ctrl,ctrl_name)
                cmds.parent()
            else:
                #Template_Tail_1_2_Tem_2_Ctrl
                ctrl_name = self.prefix_name + '_Tail_' + str(a+1) + "_Tem_" + str(self.val) + '_Ctrl'
                #upper_cluster handle
                #Template_Tail_Upper_1_2_Tem_2_CluHandle
                cluster_upper_handle = self.prefix_name + '_Tail_Upper_' + str(a) + "_" + str(a+1) + "_Tem_" + str(self.val) + '_CluHandle'

                #lower cluster_handle
                #Template_Tail_Upper_1_2_Tem_2_CluHandle
                #Template_Tail_Lower_2_3_Tem_2_CluHandle
                cluster_lower_handle = self.prefix_name + '_Tail_Lower_' + str(a+1) + "_" + str(a+2) + "_Tem_" + str(self.val) + "_CluHandle"
                cmds.parentConstraint(ctrl_name,cluster_upper_handle,mo=False)
                next_ctrl = self.prefix_name + '_Tail_'  + str(a+2) + "_Tem_" + str(self.val) + '_Ctrl'
                if cmds.objExists(cluster_lower_handle):
                    cmds.parentConstraint(ctrl_name,cluster_lower_handle,mo=False)
                    cmds.select(next_ctrl,ctrl_name)
                    cmds.parent()
            a+=1

        self.sphere_group_name = self.prefix_name + '_Tail_Tem_' + str(self.val) + '_Sphere_Grp'
        cmds.select(cl=True)
        for each in self.sphere_list:
            self.helper_class.parent_child_grp(parent=self.sphere_group_name,
                                               child=each)

        self.cluster_group_name = self.prefix_name + '_Tail_Tem_' + str(self.val) + "_Cluster_Grp"
        cmds.select(cl=True)
        for each in self.cluster_list:
            self.helper_class.parent_child_grp(parent=self.cluster_group_name,
                                               child=each,
                                               vis=True)

        self.cylinder_group_name = self.prefix_name + '_Tail_Tem_' + str(self.val) + "_Cylinder_Grp"
        cmds.select(cl=True)
        for each in self.cylinder_list:
            self.helper_class.parent_child_grp(parent=self.cylinder_group_name,
                                               child=each)

        ctrl_name = self.prefix_name + '_Tail_Base_Tem_' + str(self.val) + '_Ctrl'
        self.main_grp_name = self.prefix_name + '_Tail_Tem_' + str(self.val) + '_Main_Grp'
        ctrl_list = [self.sphere_group_name,
                    self.cylinder_group_name,
                    self.cluster_group_name,
                    ctrl_name]
        for each in ctrl_list:
            self.helper_class.parent_child_grp(parent=self.main_grp_name,
                                               child=each)

        #create a mirror object
        cmds.select(self.main_grp_name)
        self.grp_name = 'Tail_Grp'
        self.helper_class.parent_child_grp(parent=self.grp_name,
                                           child=self.main_grp_name,
                                           trans_rot_scale=False)
        self.helper_class.transform_rotation_scale_visible(self.grp_name,
                                                           v=False)

    def update_gui(self,widget):
        self.update_widget = widget

        self.verticalLayout = QtGui.QVBoxLayout(self.update_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.head_splitter = QtGui.QSplitter(self.update_widget)
        self.head_splitter.setOrientation(QtCore.Qt.Vertical)
        self.head_splitter.setObjectName("head_splitter")

        #get the radio button
        self.get_update_radio_button()
        self.get_detail_update_def()

        #lock the attr
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


        self.no_tail = self.helper_class.get_tail()
        a = 0
        value = 0
        grid_value = 0
        while a < len(self.no_tail):
            self.radio_button = QtGui.QRadioButton(self.head_name_scrollArea_widget_contents)
            self.radio_button.setObjectName(self.no_tail[a])
            self.radio_button.setText(self.no_tail[a])
            self.gridLayout_15.addWidget(self.radio_button, grid_value, value, 1, 1)
            self.radio_button.toggled.connect(partial(self.radio_button_change, a))
            value+=1
            if value == 3:
                value = 0
                grid_value+=1

            a+=1

        self.head_name_scroll_area.setWidget(self.head_name_scrollArea_widget_contents)

    def get_detail_update_def(self):
        self.head_detail_scroll_area = QtGui.QScrollArea(self.head_splitter)
        self.head_detail_scroll_area.setWidgetResizable(True)
        self.head_detail_scroll_area.setObjectName("head_detail_scroll_area")
        self.head_detail_scrollArea_widget_contents = QtGui.QWidget()
        self.head_detail_scrollArea_widget_contents.setGeometry(QtCore.QRect(0, 0, 489, 350))
        self.head_detail_scrollArea_widget_contents.setObjectName("head_detail_scrollArea_widget_contents")

        #UPDATE
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

        #SEGMENT
        #SEGMENT LABEL
        self.tail_segment_label = QtGui.QLabel(self.head_detail_2_scrollArea_widget_contents)
        self.tail_segment_label.setObjectName("segment_label")
        self.tail_segment_label.setText('Segment : ')
        self.gridLayout_23.addWidget(self.tail_segment_label, 0, 0, 1, 1)
        #LEFT EYE LINE EDIT
        self.tail_segment_line_edit = QtGui.QLineEdit(self.head_detail_2_scrollArea_widget_contents)
        self.tail_segment_line_edit.setObjectName("tail_segment_line_edit")
        self.gridLayout_23.addWidget(self.tail_segment_line_edit, 0, 1, 1, 1)

        #NAME
        #NAME LABEL
        self.name_label = QtGui.QLabel(self.head_detail_2_scrollArea_widget_contents)
        self.name_label.setObjectName("name_label")
        self.name_label.setText('Name : ')
        self.gridLayout_23.addWidget(self.name_label, 2, 0, 1, 1)
        #NAME BUTTON
        self.name_button = QtGui.QPushButton(self.head_detail_2_scrollArea_widget_contents)
        self.name_button.setObjectName("name_button")
        self.name_button.clicked.connect(self.rename)
        self.gridLayout_23.addWidget(self.name_button, 2, 1, 1, 1)

        #PARENT
        #PARENT LABEL
        self.parent_label = QtGui.QLabel(self.head_detail_2_scrollArea_widget_contents)
        self.parent_label.setObjectName("parent_label")
        self.parent_label.setText('Parent : ')
        self.gridLayout_23.addWidget(self.parent_label, 3, 0, 1, 1)
        #PARENT BUTTON
        self.parent_button = QtGui.QPushButton(self.head_detail_2_scrollArea_widget_contents)
        self.parent_button.setObjectName("parent_button")
        self.parent_button.clicked.connect(self.parent)

        self.gridLayout_23.addWidget(self.parent_button, 3, 1, 1, 1)

        spacerItem10 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_23.addItem(spacerItem10, 4, 0, 1, 1)

        self.gridLayout_16.addLayout(self.gridLayout_23, 0, 0, 1, 1)
        self.head_detail_2_scroll_area.setWidget(self.head_detail_2_scrollArea_widget_contents)



        #UPDATE AND DELETE BUTTON
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

        #UPDATE BUTTON
        self.tail_update_button = QtGui.QPushButton(self.head_update_scrollArea_widget_contents)
        self.tail_update_button.setObjectName("tail_update_button")
        self.tail_update_button.setText('Update (Tail name)')
        self.tail_update_button.clicked.connect(self.leg_update_button_def)
        self.gridLayout_17.addWidget(self.tail_update_button, 1, 0, 1, 1)

        #DELETE BUTTON
        self.tail_delete_button = QtGui.QPushButton(self.head_update_scrollArea_widget_contents)
        self.tail_delete_button.setObjectName("tail_delete_button")
        self.tail_delete_button.setText('Delete(Tail Name)')
        self.gridLayout_17.addWidget(self.tail_delete_button, 1, 1, 1, 1)

        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_17.addItem(spacerItem9, 0, 0, 1, 1)

        self.head_update_scroll_area.setWidget(self.head_update_scrollArea_widget_contents)
        self.gridLayout_18.addWidget(self.head_update_scroll_area, 1, 0, 1, 1)

        self.gridLayout_18.addWidget(self.head_detail_2_scroll_area, 0, 0, 1, 1)
        self.head_detail_scroll_area.setWidget(self.head_detail_scrollArea_widget_contents)
        self.verticalLayout.addWidget(self.head_splitter)

        self.head_detail_scroll_area.setWidget(self.head_detail_scrollArea_widget_contents)
        self.verticalLayout.addWidget(self.head_splitter)

    def delete_all(self):
        print('now all tail is going to delete')

    def radio_button_change(self,b,val):
        if val == True:
            #unlock the val
            self.unlock_attr()

            self.get_input_data(self.no_tail[b])

    def get_input_data(self,tail_name):
        self.tail_name = tail_name
        split_tail = self.tail_name.split('_')
        self.val = split_tail[-1]

        #get the prefix name
        #Template_Tail_Tem_1_Main_Grp
        main_grp_name = '*_Tail_Tem_' + str(self.val) + '_Main_Grp'
        cmds.select(main_grp_name)
        sel_main = cmds.ls(sl=True)[0]
        self.prefix_name = sel_main.split('_Tail_Tem_')[0]

        #get the controller
        #Template_Tail_1_Tem_1_Ctrl
        ctrl_name = self.prefix_name + '_Tail_*_Tem_' + str(self.val) + '_Ctrl'
        base_ctrl = self.prefix_name + '_Tail_Base_Tem_' + str(self.val) + '_Ctrl'
        cmds.select(ctrl_name)
        cmds.select(base_ctrl,d=True)
        self.sel_ctrl = cmds.ls(sl=True)
        self.tail_segment_line_edit.setText(str(len(self.sel_ctrl)))

        #set the name
        self.name_button.setText(self.prefix_name)

        #get the parent const
        self.parent_button.setText(self.parent_query())

    def parent_query(self):
        #Template_Human_Head_Base_Tem_1_Ctrl
        base_ctrl_name = self.prefix_name + '_Tail_Base_Tem_'  + str(self.val) + '_Ctrl'

        value = cmds.listRelatives(base_ctrl_name,type='parentConstraint')
        if value == None:
            parent = 'None'
        else:
            parent = cmds.listConnections((value[0] + '.target[0].targetTranslate'),type='transform')[0]
        return parent

    def lock_attr(self):
        self.tail_segment_label.setDisabled(True)
        self.tail_segment_line_edit.setDisabled(True)
        self.name_label.setDisabled(True)
        self.name_button.setDisabled(True)
        self.parent_button.setDisabled(True)
        self.parent_label.setDisabled(True)
        self.tail_update_button.setDisabled(True)
        self.tail_delete_button.setDisabled(True)

    def unlock_attr(self):
        self.tail_segment_label.setDisabled(False)
        self.tail_segment_line_edit.setDisabled(False)
        self.name_label.setDisabled(False)
        self.name_button.setDisabled(False)
        self.parent_button.setDisabled(False)
        self.parent_label.setDisabled(False)
        self.tail_update_button.setDisabled(False)
        self.tail_delete_button.setDisabled(False)

    def rename(self):
        rename.main('Tail',self.tail_name,self.name_button)

    def parent(self):
        parent.main('Tail',self.tail_name,self.parent_button)

    def get_update_ui(self):
        #get the segmen
        self.tail_segment_line_edit_query = int(self.tail_segment_line_edit.text())

    def leg_update_button_def(self):
        #GET THE UPDATE
        self.get_update_ui()

        if len(self.sel_ctrl) != self.tail_segment_line_edit_query:
            #ctrl_name
            #Template_Tail_1_Tem_1_Ctrl
            ctrl_name = self.prefix_name + '_Tail_Base_Tem_' + str(self.val) + '_Ctrl'
            get_pos = cmds.xform(ctrl_name,q=1,ws=1,rp=1)
            #Template_Tail_Base_Tem_1_Geo
            common_name = self.prefix_name + '_Tail_*_Tem_' + str(self.val)
            geo_name = common_name + '_Geo'
            base_name = self.prefix_name + '_Tail_Base_Tem_' + str(self.val) + '_Geo'
            #Template_Tail_1_Tem_1_CluHandle
            clu_handle_name = common_name + '_CluHandle'
            base_clu_handle_name = self.prefix_name + '_Tail_Base_Tem_' + str(self.val) + '_CluHandle'
            #Template_Tail_1_2_Tem_1_Geo
            cylinder_name = self.prefix_name + '_Tail_*_*_Tem_' + str(self.val) + '_Geo'

            cmds.select(ctrl_name,geo_name,
                        clu_handle_name,cylinder_name)
            cmds.delete()


            self.base_ctrl_color = 'Yellow'
            self.cylinder_ctrl_roate = [90,0,0]
            self.cylinder_rotate = [90,0,0]

            self.tail_def(pos=get_pos)

    def tail_create(self):
        self.grp_list = ['Tail_Grp']
        for each_grp in self.grp_list:
            #list of the all children
            if cmds.objExists(each_grp):
                children_list = cmds.listRelatives(each_grp,children=True)
                for each_child in children_list:
                    #get all the controller data
                    self.tail_data(each_child)

                    #FINAL THE ARM
                    self.final_arm_def()

    def tail_data(self,children_name):
        split_name = children_name.split('_')
        self.prefix_name = split_name[0]
        self.val = split_name[3]

    def final_arm_def(self):
        root_grp_name = "Root_Grp"
        if cmds.objExists(root_grp_name):
            pass
        else:
            cmds.createNode('transform',n=root_grp_name)


        #Template_Tail_1_Tem_1_Ctrl
        #Template_Tail_Base_Tem_1_Ctrl
        tail_ctrl_name = self.prefix_name + '_Tail_*_Tem_' + str(self.val) + '_Ctrl'
        base_ctrl_name = self.prefix_name + '_Tail_Base_Tem_' + str(self.val) + '_Ctrl'
        cmds.select(tail_ctrl_name)
        cmds.select(base_ctrl_name,d=True)
        sel_obj = cmds.ls(sl=True)
        a = 0
        cmds.select(cl=True)
        while a < len(sel_obj):
            #Create a joint on each position
            spine_get_trans = cmds.xform(sel_obj[a],q=1,ws=1,rp=1)
            jnt_name = self.prefix_name + '_Tail_' + str(a+1) + '_Tem_' + str(self.val) + '_Jnt'
            cmds.joint(n=jnt_name,p=(spine_get_trans[0],
                                     spine_get_trans[1],
                                     spine_get_trans[2]))

            a+=1
        first_jnt = self.prefix_name + '_Tail_1_Tem_' + str(self.val) + '_Jnt'
        tail_first_get_pos = cmds.xform(first_jnt,q=1,ws=1,rp=1)
        cmds.select(first_jnt)
        #cmds.joint(e=True,oj='xyz',secondaryAxisOrient='xup',ch=True,zso=True)
        a = 0
        while a < len(sel_obj):
            jnt_name = self.prefix_name + '_Tail_' + str(a+1) + '_Tem_' + str(self.val) + '_Jnt'
            ctrl_name = jnt_name + '_Ctrl'
            ctrl_shape_name = ctrl_name + 'Shape'
            self.controller_class.circle_ctrl()
            cmds.rename('circle_ctrl',ctrl_name)
            cmds.select(ctrl_shape_name,jnt_name)
            cmds.parent(r=True,s=True)
            cmds.select(ctrl_name)
            cmds.delete()
            a+=1

        tail_grp_name = self.prefix_name + '_Tail_Tem_' + str(self.val) + '_grp'
        cmds.select(first_jnt)
        cmds.group(n=tail_grp_name)
        cmds.move(tail_first_get_pos[0],
                  tail_first_get_pos[1],
                  tail_first_get_pos[2],
                  (tail_grp_name + '.scalePivot'),
                  (tail_grp_name + '.rotatePivot'))


        tail_loc_name = self.prefix_name + '_Tail_Tem_' + str(self.val) + '_Loc'
        cmds.spaceLocator(n=tail_loc_name,p=(tail_first_get_pos[0],
                                             tail_first_get_pos[1],
                                             tail_first_get_pos[2]))
        cmds.select(tail_loc_name)
        cmds.CenterPivot()
        cmds.parentConstraint(tail_loc_name,tail_grp_name,mo=True)
        cmds.select(tail_loc_name,tail_grp_name,root_grp_name)
        cmds.parent()

    def bone_def(self):
        self.grp_list = ['Tail_Grp']
        for each_grp in self.grp_list:
            #list of the all children
            if cmds.objExists(each_grp):
                children_list = cmds.listRelatives(each_grp,children=True)
                for each_child in children_list:
                    #get all the controller data
                    self.tail_data(each_child)

                    self.final_bone_tail()

    def controller_twick_def(self):
        self.grp_list = ['Tail_Grp']
        for each_grp in self.grp_list:
            #list of the all children
            if cmds.objExists(each_grp):
                children_list = cmds.listRelatives(each_grp,children=True)
                for each_child in children_list:
                    #get all the controller data
                    self.tail_data(each_child)

                    self.final_controller_def()

    def final_controller_def(self):
        #Create a Fk Controller
        grp_name = self.prefix_name + '_Tail_' + str(self.val) + '_Twick_Ctrl_Grp'
        main_grp_name = 'Tail_Twick_Ctrl_Grp'

        tail_ctrl_name = self.prefix_name + '_Tail_*_Tem_' + str(self.val) + '_Ctrl'
        base_ctrl_name = self.prefix_name + '_Tail_Base_Tem_' + str(self.val) + '_Ctrl'
        cmds.select(tail_ctrl_name)
        cmds.select(base_ctrl_name,d=True)
        sel_obj = cmds.ls(sl=True)
        a = 0
        cmds.select(cl=True)
        while a < len(sel_obj):
            #Create a joint on each position
            spine_get_trans = cmds.xform(sel_obj[a],q=1,ws=1,rp=1)
            split_name = sel_obj[a].split('_Ctrl')
            twick_ctrl_name = split_name[0] + '_Twick_Ctrl'
            self.controller_class.circle_ctrl()
            cmds.rename('circle_ctrl',twick_ctrl_name)
            cmds.setAttr((twick_ctrl_name + '.rx'),90)

            cmds.setAttr((twick_ctrl_name + '.tx'),spine_get_trans[0])
            cmds.setAttr((twick_ctrl_name + '.ty'),spine_get_trans[1])
            cmds.setAttr((twick_ctrl_name + '.tz'),spine_get_trans[2])

            self.helper_class.color_val(color='Yellow',
                                        obj_name=twick_ctrl_name)

            self.helper_class.grp_create(object_name=twick_ctrl_name,
                                         grp_name=grp_name)



            a+=1
        self.helper_class.grp_create(object_name=grp_name,
                                     grp_name=main_grp_name)



    def final_bone_tail(self):
        grp_namne = self.prefix_name + '_Tail_Tem_' + str(self.val) + '_Grp'
        main_grp_name = 'Tail_Bone_Grp'

        tail_ctrl_name = self.prefix_name + '_Tail_*_Tem_' + str(self.val) + '_Ctrl'
        base_ctrl_name = self.prefix_name + '_Tail_Base_Tem_' + str(self.val) + '_Ctrl'
        cmds.select(tail_ctrl_name)
        cmds.select(base_ctrl_name,d=True)
        sel_obj = cmds.ls(sl=True)
        a = 0
        cmds.select(cl=True)
        while a < len(sel_obj):
            common_name = sel_obj[a].split('_Ctrl')[0]
            bone_name = common_name + '_Bone'
            ctrl_pos = cmds.xform(sel_obj[a],q=1,ws=1,rp=1)
            cmds.select(cl=True)
            cmds.joint(n=bone_name,p=(ctrl_pos[0],ctrl_pos[1],ctrl_pos[2]))
            if a > 0:
                p_commmon = sel_obj[a-1].split('_Ctrl')[0]
                previous_bone = p_commmon + '_Bone'
                cmds.parent(bone_name,previous_bone)
            else:
                first_jnt_name = bone_name
            a+=1

        self.helper_class.grp_create(object_name=first_jnt_name,
                                     grp_name=grp_namne)

        self.helper_class.grp_create(object_name=grp_namne,
                                     grp_name=main_grp_name)


    def get_tail(self):
        list = []
        self.grp_list = ['Tail_Grp']
        for each_grp in self.grp_list:
            #list of the all children
            if cmds.objExists(each_grp):
                children_list = cmds.listRelatives(each_grp,children=True)
                for each_child in children_list:
                    #get all the controller data
                    list.append(each_child)
        return len(list)






