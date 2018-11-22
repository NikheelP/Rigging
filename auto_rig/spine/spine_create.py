
import maya.cmds as cmds
import rig_helper
reload(rig_helper)

class SPINE_CREATE:

    def __init__(self):
        self.rig_helper_class = rig_helper.rig_help()

    def spine_create(self,type,right_breast,left_breast,no_jnt,
                     prefix_name,left_breast_pos,right_breast_pos,val):
        self.spine_type = type
        self.right_breast = int(right_breast)
        self.left_breast = int(left_breast)
        self.no_jnt = int(no_jnt)
        self.prefix_name = prefix_name
        self.left_breast_pos = left_breast_pos
        self.right_breast_pos = right_breast_pos
        self.val = val

        # find the global name
        if cmds.objExists('*_Human_Spine_Tem_*_Main_Grp'):
            # get the val
            cmds.select("*_Human_Spine_Tem_*_Main_Grp")
            sel_spine_list = cmds.ls(sl=True)
            len_sel_spine_list = len(sel_spine_list)
            self.val = len_sel_spine_list + 1
        else:
            self.val = 1

        #Create a Spine
        self.spine_def(val=self.val)

        self.breast_def(self.left_breast,
                        self.left_breast_pos,
                        'L',
                        'Blue')
        self.breast_def(self.right_breast,
                        self.right_breast_pos,
                        'R',
                        'Red')

        #final grp
        self.final_grp()


    def spine_def(self ,val=0 ,update_val=1 ,def_val = 2):
        a = 0
        default_value = def_val + val
        while a < self.no_jnt:
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

            self.rig_helper_class.set_sphere_position(self.spine_sphere_name,
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
            self.rig_helper_class.set_controller(self.cylinder_ctrl_name ,self.spine_pos ,self.cylinder_ctrl_size_ctrl,
                                             self.cylinder_ctrl_roate ,self.cylinder_parent_const_list
                                             ,self.cylinder_parent_const_list,
                                             color=self.cylinder_ctrl_color,
                                             freez_trans = self.cylinder_ctrl_freez_trans,
                                             freez_rotate = self.cylinder_ctrl_freez_rotate,
                                             freez_scale = self.cylinder_ctrl_freez_scale)

            if a == 0:
                self.ctrl_grp_name = self.prefix_name + '_' + self.spine_type + "_Spine_Tem_" + str(self.val) + '_Ctrl_Grp'
                self.rig_helper_class.grp_create(object_name=self.cylinder_ctrl_name,
                                                 grp_name=self.ctrl_grp_name)

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
                self.rig_helper_class.set_cylinder_position(self.cylinder_name,
                                                        self.cylinder_lower_cluster_name,
                                                        self.cylinder_upper_cluster_name,
                                                        self.current_sphere_name,
                                                        self.spine_sphere_name,
                                                        rotate_val=self.cylinder_rotate)

                self.previous_ctrl = self.prefix_name + '_' + self.spine_type + "_Spine_" + str(
                    update_val - 1) + "_Tem_" + str(self.val) + '_Ctrl'
                self.parent_list = [self.cylinder_lower_cluster_handle_name]
                self.rig_helper_class.parent_constraint(self.previous_ctrl, self.parent_list)
                self.rig_helper_class.scale_constraint(self.previous_ctrl, self.parent_list)

                self.parent_list = [self.cylinder_upper_cluster_handle_name]
                self.rig_helper_class.parent_constraint(self.cylinder_ctrl_name, self.parent_list)
                self.rig_helper_class.scale_constraint(self.cylinder_ctrl_name, self.parent_list)

                # pare the controller
                cmds.select(self.cylinder_ctrl_name, self.previous_ctrl)
                cmds.parent()

                self.cylinder_grp_name = self.prefix_name + '_' + self.spine_type + "_Spine_Tem_" + str(
                    self.val) + "_Cylinder_Grp"
                self.rig_helper_class.grp_create(object_name=self.cylinder_name,
                                                 grp_name=self.cylinder_grp_name)

                self.cluster_grp_name = self.prefix_name + '_' + self.spine_type + '_Spine_Tem_' + str(
                    self.val) + "_Cluster_Grp"
                self.rig_helper_class.grp_create(object_name=self.cylinder_upper_cluster_handle_name,
                                                 grp_name=self.cluster_grp_name)
                self.rig_helper_class.grp_create(object_name=self.cylinder_lower_cluster_handle_name,
                                                 grp_name=self.cluster_grp_name)


            default_value += 4

            self.sphere_grp_name = self.prefix_name + '_' + self.spine_type + '_Spine_Tem_' + str(
                self.val) + "_Sphere_Grp"
            self.rig_helper_class.grp_create(object_name=self.spine_sphere_name,
                                             grp_name=self.sphere_grp_name)

            self.cluster_grp_name = self.prefix_name + '_' + self.spine_type + '_Spine_Tem_' + str(
                self.val) + "_Cluster_Grp"
            self.rig_helper_class.grp_create(object_name=self.spine_clu_handle_name,
                                             grp_name=self.cluster_grp_name)
            cmds.setAttr((self.cluster_grp_name + '.v'),0)
            update_val += 1
            a += 1

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

            self.rig_helper_class.set_sphere_position(self.sphere_name,
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
            self.rig_helper_class.set_controller(self.spine_breast_ctrl_name, self.pos, self.spine_ctrl_size_ctrl,
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
            cmds.scaleConstraint(self.last_ctrl, self.spine_breast_ctrl_grp_name, mo=True)

            self.rig_helper_class.grp_create(object_name=self.sphere_name,
                                             grp_name=self.sphere_grp_name)
            self.rig_helper_class.grp_create(object_name=self.clu_handle_name,
                                             grp_name=self.cluster_grp_name)
            self.rig_helper_class.grp_create(object_name=self.spine_breast_ctrl_grp_name,
                                             grp_name=self.ctrl_grp_name)

            value += 2
            a += 1

    def final_grp(self):
        list = [self.ctrl_grp_name,self.cluster_grp_name,self.sphere_grp_name,self.cylinder_grp_name]
        main_grp_name = self.prefix_name + '_' + self.spine_type + '_Spine_Tem_' + str(self.val) + '_Main_Grp'
        for each in list:
            self.rig_helper_class.grp_create(object_name=each,
                                             grp_name=main_grp_name)

        spine_grp_name = 'Spine_Grp'
        self.rig_helper_class.grp_create(object_name=main_grp_name,
                                         grp_name=spine_grp_name)



