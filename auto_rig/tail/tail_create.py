
import maya.cmds as cmds
import rig_helper
reload(rig_helper)

class TAIL_CREATE:

    def __init__(self):
        self.rig_helper_class = rig_helper.rig_help()

    def tail_create(self,tail_segment,prefix_name,pos):

        self.tail_segment = int(tail_segment)
        self.prefix_name = prefix_name
        self.base_ctrl_color = 'Yellow'
        self.cylinder_ctrl_roate = [90, 0, 0]
        self.cylinder_rotate = [90, 0, 0]
        self.pos = pos

        if cmds.objExists("*_Tail_Tem_*_Main_Grp"):
            cmds.select("*_Tail_Tem_*_Main_Grp")
            sel_main_grp = cmds.ls(sl=True)
            len_sel_main_grp = len(sel_main_grp)
            self.val = len_sel_main_grp + 1
        else:
            self.val = 1

        self.tail_def(self.pos)

    def tail_def(self,pos):
        self.sphere_list = []
        self.cluster_list = []
        self.cylinder_list = []
        self.ctrl_list = []
        self.crv_list = []
        default_pos = -2
        a = 0
        while a < self.tail_segment:

            if a == 0:
                self.tail_common_name = self.prefix_name + '_Tail_Base_Tem_' + str(self.val)
                self.sphere_name = self.tail_common_name + '_Geo'
                self.sphere_clu_name = self.tail_common_name + '_Clu'
                self.sphere_clu_handle_name = self.sphere_clu_name + 'Handle'
                self.sphere_list.append(self.sphere_name)
                self.cluster_list.append(self.sphere_clu_handle_name)
                self.pos = pos
                self.rig_helper_class.set_sphere_position(self.sphere_name,
                                                      self.pos,
                                                      self.sphere_clu_name)

                # create a cylinder
                # create a controller
                self.cylinder_ctrl_name = self.prefix_name + '_Tail_Base_Tem_' + str(self.val) + '_Ctrl'
                self.ctrl_list.append(self.cylinder_ctrl_name)
                self.cylinder_ctrl_size_ctrl = [0.5, 0.5, 0.5]
                self.cylinder_parent_const_list = [self.sphere_clu_handle_name]
                self.cylinder_ctrl_color = 'Yellow'
                self.cylinder_ctrl_freez_trans = True
                self.cylinder_ctrl_freez_rotate = True
                self.cylinder_ctrl_freez_scale = True
                self.rig_helper_class.set_controller(self.cylinder_ctrl_name, self.pos, self.cylinder_ctrl_size_ctrl,
                                                 self.cylinder_ctrl_roate, self.cylinder_parent_const_list,
                                                 self.cylinder_parent_const_list,
                                                 color=self.cylinder_ctrl_color,
                                                 freez_trans=self.cylinder_ctrl_freez_trans,
                                                 freez_rotate=self.cylinder_ctrl_freez_rotate,
                                                 freez_scale=self.cylinder_ctrl_freez_scale)

            self.tail_common_name = self.prefix_name + '_Tail_' + str(a + 1) + '_Tem_' + str(self.val)
            self.sphere_name = self.tail_common_name + '_Geo'
            self.sphere_clu_name = self.tail_common_name + '_Clu'
            self.sphere_clu_handle_name = self.sphere_clu_name + 'Handle'
            self.sphere_list.append(self.sphere_name)
            self.cluster_list.append(self.sphere_clu_handle_name)
            self.sphere_list.append(self.sphere_name)
            self.cluster_list.append(self.sphere_clu_handle_name)
            self.pos = [0, 0, default_pos]
            self.rig_helper_class.set_sphere_position(self.sphere_name,
                                                  self.pos,
                                                  self.sphere_clu_name)

            # create a cylinder
            # create a controller
            self.cylinder_ctrl_name = self.prefix_name + '_Tail_' + str(a + 1) + "_Tem_" + str(self.val) + '_Ctrl'
            self.ctrl_list.append(self.cylinder_ctrl_name)
            self.cylinder_ctrl_size_ctrl = [0.5, 0.5, 0.5]
            self.cylinder_parent_const_list = [self.sphere_clu_handle_name]
            self.cylinder_ctrl_color = 'Yellow'
            self.cylinder_ctrl_freez_trans = True
            self.cylinder_ctrl_freez_rotate = True
            self.cylinder_ctrl_freez_scale = True
            self.rig_helper_class.set_controller(self.cylinder_ctrl_name, self.pos, self.cylinder_ctrl_size_ctrl,
                                             self.cylinder_ctrl_roate, self.cylinder_parent_const_list,
                                             self.cylinder_parent_const_list,
                                             color=self.cylinder_ctrl_color,
                                             freez_trans=self.cylinder_ctrl_freez_trans,
                                             freez_rotate=self.cylinder_ctrl_freez_rotate,
                                             freez_scale=self.cylinder_ctrl_freez_scale)

            if a + 1 != 1:
                self.cylinder_name = self.prefix_name + '_Tail_' + str(a) + "_" + str(a + 1) + "_Tem_" + str(
                    self.val) + "_Geo"
                self.cylinder_list.append(self.cylinder_name)
                self.cylinder_upper_cluster_name = self.prefix_name + '_Tail_Upper_' + str(a) + "_" + str(
                    a + 1) + "_Tem_" + str(self.val) + "_Clu"
                self.cylinder_upper_cluster_handle_name = self.cylinder_upper_cluster_name + 'Handle'
                self.cluster_list.append(self.cylinder_upper_cluster_handle_name)
                self.cylinder_lower_cluster_name = self.prefix_name + '_Tail_Lower_' + str(a) + "_" + str(
                    a + 1) + "_Tem_" + str(self.val) + "_Clu"
                self.cylinder_lower_cluster_handle_name = self.cylinder_lower_cluster_name + 'Handle'
                self.cluster_list.append(self.cylinder_lower_cluster_handle_name)
                ##########################self.prefix_name + '_Tail_' + str(a+1) + '_Tem_' + str(self.val)
                self.current_sphere_name = self.prefix_name + '_Tail_' + str(a) + '_Tem_' + str(self.val) + "_Geo"
                self.rig_helper_class.set_cylinder_position(self.cylinder_name,
                                                        self.cylinder_lower_cluster_name,
                                                        self.cylinder_upper_cluster_name,
                                                        self.current_sphere_name,
                                                        self.sphere_name,
                                                        rotate_val=self.cylinder_rotate)
            default_pos -= 2
            a += 1

        a = 0
        while a < self.tail_segment:

            if a == 0:
                self.tail_common_name = self.prefix_name + '_Tail_' + str(a + 1) + '_Tem_' + str(self.val)
                self.sphere_name = self.tail_common_name + '_Geo'
                # create a cylinder
                self.cylinder_name = self.prefix_name + '_Tail_Base_' + str(a + 1) + "_Tem_" + str(self.val) + "_Geo"
                self.cylinder_list.append(self.cylinder_name)
                self.cylinder_upper_cluster_name = self.prefix_name + '_Tail_Upper_Base_' + str(a + 1) + "_Tem_" + str(
                    self.val) + "_Clu"
                self.cylinder_upper_cluster_handle_name = self.cylinder_upper_cluster_name + 'Handle'
                self.cylinder_lower_cluster_name = self.prefix_name + '_Tail_Lower_Base_' + str(a + 1) + "_Tem_" + str(
                    self.val) + "_Clu"
                self.cylinder_lower_cluster_handle_name = self.cylinder_lower_cluster_name + 'Handle'
                self.cluster_list.append(self.cylinder_upper_cluster_handle_name)
                self.cluster_list.append(self.cylinder_lower_cluster_handle_name)

                self.current_sphere_name = self.prefix_name + '_Tail_Base_Tem_' + str(self.val) + "_Geo"
                self.rig_helper_class.set_cylinder_position(self.cylinder_name,
                                                        self.cylinder_lower_cluster_name,
                                                        self.cylinder_upper_cluster_name,
                                                        self.current_sphere_name,
                                                        self.sphere_name,
                                                        rotate_val=self.cylinder_rotate)
                # Template_Tail_Base_0_Tem_2_Ctrl
                self.base_ctrl_name = self.prefix_name + '_Tail_Base_Tem_' + str(self.val) + '_Ctrl'
                # Template_Tail_Lower_Base_1_Tem_2_CluHandle
                self.lower_cluster = self.prefix_name + '_Tail_Lower_Base_' + str(a + 1) + "_Tem_" + str(
                    self.val) + "_CluHandle"
                self.tail_common_name = self.prefix_name + '_Tail_Base_Tem_' + str(self.val)
                self.sphere_clu_name = self.tail_common_name + '_Clu'
                self.sphere_clu_handle_name = self.sphere_clu_name + 'Handle'
                cmds.parentConstraint(self.base_ctrl_name, self.lower_cluster, mo=False)
                cmds.parentConstraint(self.base_ctrl_name, self.sphere_clu_handle_name, mo=False)

                # Template_Tail_0_1_Tem_2_Ctrl
                ctrl_name = self.prefix_name + '_Tail_' + str(a + 1) + "_Tem_" + str(self.val) + '_Ctrl'
                # upper_cluster handle
                # Template_Tail_Upper_Base_1_Tem_2_CluHandle
                cluster_upper_handle = self.prefix_name + '_Tail_Upper_Base_' + str(a + 1) + "_Tem_" + str(
                    self.val) + '_CluHandle'

                # lower cluster_handle
                # Template_Tail_Lower_1_2_Tem_2_CluHandle
                cluster_lower_handle = self.prefix_name + '_Tail_Lower_' + str(a + 1) + "_" + str(
                    a + 2) + "_Tem_" + str(self.val) + "_CluHandle"
                cmds.parentConstraint(ctrl_name, cluster_upper_handle, mo=False)
                cmds.parentConstraint(ctrl_name, cluster_lower_handle, mo=False)
                next_ctrl = self.prefix_name + '_Tail_' + str(a + 2) + "_Tem_" + str(self.val) + '_Ctrl'

                cmds.select(ctrl_name, self.base_ctrl_name)
                cmds.parent()

                cmds.select(next_ctrl, ctrl_name)
                cmds.parent()
            else:
                # Template_Tail_1_2_Tem_2_Ctrl
                ctrl_name = self.prefix_name + '_Tail_' + str(a + 1) + "_Tem_" + str(self.val) + '_Ctrl'
                # upper_cluster handle
                # Template_Tail_Upper_1_2_Tem_2_CluHandle
                cluster_upper_handle = self.prefix_name + '_Tail_Upper_' + str(a) + "_" + str(a + 1) + "_Tem_" + str(
                    self.val) + '_CluHandle'

                # lower cluster_handle
                # Template_Tail_Upper_1_2_Tem_2_CluHandle
                # Template_Tail_Lower_2_3_Tem_2_CluHandle
                cluster_lower_handle = self.prefix_name + '_Tail_Lower_' + str(a + 1) + "_" + str(
                    a + 2) + "_Tem_" + str(self.val) + "_CluHandle"
                cmds.parentConstraint(ctrl_name, cluster_upper_handle, mo=False)
                next_ctrl = self.prefix_name + '_Tail_' + str(a + 2) + "_Tem_" + str(self.val) + '_Ctrl'
                if cmds.objExists(cluster_lower_handle):
                    cmds.parentConstraint(ctrl_name, cluster_lower_handle, mo=False)
                    cmds.select(next_ctrl, ctrl_name)
                    cmds.parent()
            a += 1

        self.sphere_group_name = self.prefix_name + '_Tail_Tem_' + str(self.val) + '_Sphere_Grp'
        cmds.select(cl=True)
        for each in self.sphere_list:
            self.rig_helper_class.parent_child_grp(parent=self.sphere_group_name,
                                               child=each)

        self.cluster_group_name = self.prefix_name + '_Tail_Tem_' + str(self.val) + "_Cluster_Grp"
        cmds.select(cl=True)
        for each in self.cluster_list:
            self.rig_helper_class.parent_child_grp(parent=self.cluster_group_name,
                                               child=each,
                                               vis=True)

        self.cylinder_group_name = self.prefix_name + '_Tail_Tem_' + str(self.val) + "_Cylinder_Grp"
        cmds.select(cl=True)
        for each in self.cylinder_list:
            self.rig_helper_class.parent_child_grp(parent=self.cylinder_group_name,
                                               child=each)

        ctrl_name = self.prefix_name + '_Tail_Base_Tem_' + str(self.val) + '_Ctrl'
        self.main_grp_name = self.prefix_name + '_Tail_Tem_' + str(self.val) + '_Main_Grp'
        ctrl_list = [self.sphere_group_name,
                     self.cylinder_group_name,
                     self.cluster_group_name,
                     ctrl_name]
        for each in ctrl_list:
            self.rig_helper_class.parent_child_grp(parent=self.main_grp_name,
                                               child=each)

        # create a mirror object
        cmds.select(self.main_grp_name)
        self.grp_name = 'Tail_Grp'
        self.rig_helper_class.parent_child_grp(parent=self.grp_name,
                                           child=self.main_grp_name,
                                           trans_rot_scale=False)
        self.rig_helper_class.transform_rotation_scale_visible(self.grp_name,
                                                           v=False)









