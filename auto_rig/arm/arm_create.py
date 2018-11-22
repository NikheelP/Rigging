import maya.cmds as cmds
import rig_helper
reload(rig_helper)


class ARM_CREATE:

    def __init__(self):
        self.rig_helper_class = rig_helper.rig_help()

    def arm_def(self,mirror,left_hand,right_hand,
                   upper_arm_roll,lower_arm_roll,hand,no_finger,
                   base_pos,shoulder_pos,upper_hand_pos,lbow_pos,hand_pos,
                   hand_end_pos,double_wrist_pos,double_lbow_side_1_pos,double_lbow_side_2_pos,
                   finger_default_pos,prefix_name,side,base_ctrl_color,finger_list):

        self.mirror = mirror
        self.left_hand = left_hand
        self.right_hand = right_hand
        self.upper_arm_roll = int(upper_arm_roll)
        self.lower_arm_roll = int(lower_arm_roll)
        self.hand = hand
        self.no_finger = int(no_finger)
        self.side  = side
        self.base_ctrl_color = base_ctrl_color
        self.base_pos = base_pos
        self.shoulder_pos = shoulder_pos
        self.upper_hand_pos = upper_hand_pos
        self.lbow_pos = lbow_pos
        self.hand_pos = hand_pos
        self.hand_end_pos = hand_end_pos
        self.double_wrist_pos = double_wrist_pos
        self.double_lbow_side_1_pos = double_lbow_side_1_pos
        self.double_lbow_side_2_pos = double_lbow_side_2_pos
        self.finger_default_pos = finger_default_pos
        self.prefix_name = prefix_name
        self.finger_list = finger_list

        self.pos_list = [self.base_pos,self.shoulder_pos,self.upper_hand_pos,self.lbow_pos,self.hand_pos,self.hand_end_pos]

        # Chck if left val
        if cmds.objExists('*_' + self.side + '_Arm_Tem_*_Main_Grp'):
            cmds.select('*_' + self.side + '_Arm_Tem_*_Main_Grp')
            sel_main_grp = cmds.ls(sl=True)
            len_sel_main_grp = len(sel_main_grp)
            self.val = len_sel_main_grp + 1
        else:
            self.val = 1

        #Create a Variable
        self.arm_var()

        #Create a sphere on each position
        self.rig_helper_class.sphere_create(sphere_list=self.sphere_list,
                                            pos_list=self.pos_list,
                                            cluster_list=self.cluster_list)
        
        #Create Cylinder
        self.arm_cylinder()
        
        #Create a Controller
        self.controller_def()
        
        #Create a finger
        if self.hand == True:
            self.finger_def()

        #Create a Final Grp
        self.final_grp()


        return self.mirror_list

    def arm_var(self):
        self.sphere_list = []
        self.cluster_list = []
        self.cylinder_list = []
        self.ctrl_list = []
        self.crv_list = []
        self.mirror_list = []

        grp_common_name = self.prefix_name + '_' + self.side + '_Arm_Tem_' + str(self.val)
        self.clu_grp_name = grp_common_name + '_Clu_Grp'
        self.sphere_grp_name = grp_common_name + '_Sphere_Grp'
        self.cylinder_grp_name = grp_common_name + '_Cylinder_Grp'
        self.ctrl_grp_name = grp_common_name + '_Ctrl_Grp'
        self.crv_grp_name = grp_common_name + '_Crv_Grp'

        #BASE
        self.base_common = self.prefix_name + "_" + self.side + "_Arm_Base_Tem_" + str(self.val)
        self.base_sphere_name = self.base_common + "_Geo"
        self.base_clu_name = self.base_common + '_Clu'
        self.base_clu_handle_name = self.base_clu_name + 'Handle'
        self.base_ctrl_name = self.base_common + '_Ctrl'
        self.sphere_list.append(self.base_sphere_name)
        self.cluster_list.append(self.base_clu_name)

        # SHOULDER
        self.shoulder_common = self.prefix_name + "_" + self.side + "_Arm_Shoulder_Tem_" + str(self.val)
        self.shoulder_sphere_name = self.shoulder_common + "_Geo"
        self.shoulder_clu_name = self.shoulder_common + '_Clu'
        self.shoulder_clu_handle_name = self.shoulder_clu_name + 'Handle'
        self.shoulder_ctrl_name = self.shoulder_common + '_Ctrl'
        self.sphere_list.append(self.shoulder_sphere_name)
        self.cluster_list.append(self.shoulder_clu_name)

        # UPPPER HAND
        self.upper_hand_common = self.prefix_name + "_" + self.side + "_Arm_Upper_Hand_Tem_" + str(self.val)
        self.upper_hand_sphere_name = self.upper_hand_common + "_Geo"
        self.upper_hand_clu_name = self.upper_hand_common + '_Clu'
        self.upper_handle_clu_handle_name = self.upper_hand_clu_name + 'Handle'
        self.upper_hand_ctrl_name  = self.upper_hand_common + '_Ctrl'
        self.sphere_list.append(self.upper_hand_sphere_name)
        self.cluster_list.append(self.upper_hand_clu_name)

        # LBOW
        self.lbow_common = self.prefix_name + "_" + self.side + "_Arm_lBow_Tem_" + str(self.val)
        self.lbow_sphere_name = self.lbow_common + "_Geo"
        self.lbow_clu_name = self.lbow_common + '_Clu'
        self.lbow_clu_handle_name = self.lbow_clu_name + 'Handle'
        self.lbow_ctrl_name = self.lbow_common + '_Ctrl'
        self.sphere_list.append(self.lbow_sphere_name)
        self.cluster_list.append(self.lbow_clu_name)

        # HAND
        self.hand_common = self.prefix_name + "_" + self.side + "_Arm_Hand_Tem_" + str(self.val)
        self.hand_sphere_name = self.hand_common + "_Geo"
        self.hand_clu_name = self.hand_common + '_Clu'
        self.hand_clu_handle_name = self.hand_clu_name + 'Handle'
        self.hand_ctrl_name = self.hand_common + '_Ctrl'
        self.sphere_list.append(self.hand_sphere_name)
        self.cluster_list.append(self.hand_clu_name)

        # HAND END
        self.hand_end_common = self.prefix_name + "_" + self.side + "_Arm_Hand_End_Tem_" + str(self.val)
        self.hand_end_sphere_name = self.hand_end_common + "_Geo"
        self.hand_end_clu_name = self.hand_end_common + '_Clu'
        self.hand_end_clu_handle_name = self.hand_end_clu_name + 'Handle'
        self.hand_end_ctrl_name = self.hand_end_common + '_Ctrl'
        self.sphere_list.append(self.hand_end_sphere_name)
        self.cluster_list.append(self.hand_end_clu_name)

    def arm_cylinder(self):
        self.base_to_shoulder_common = self.prefix_name + "_" + self.side + "_Hand_Base_to_Shoulder_Tem_" + str(
            self.val)
        self.base_to_shoulder_cylinder_name = self.base_to_shoulder_common + '_Geo'
        self.base_to_shoulder_lower_cylinder_cluster_name = self.prefix_name + "_" + self.side + "_Hand_Base_to_Shoulder_Lower_Tem_" + str(
            self.val) + '_Clu'
        self.base_to_shoulder_lower_cylinder_cluster_handle_name = self.base_to_shoulder_lower_cylinder_cluster_name + 'Handle'
        self.base_to_shoulder_upper_cylinder_cluster_name = self.prefix_name + "_" + self.side + "_Hand_Base_to_Shoulder_Upper_Tem_" + str(
            self.val) + '_Clu'
        self.base_to_shoulder_upper_cylinder_cluster_handle_name = self.base_to_shoulder_upper_cylinder_cluster_name + 'Handle'
        self.cylinder_rotate = [0, 0, 90]
        self.cluster_list.append(self.base_to_shoulder_lower_cylinder_cluster_name)
        self.cluster_list.append(self.base_to_shoulder_upper_cylinder_cluster_name)
        self.cylinder_list.append(self.base_to_shoulder_cylinder_name)
        self.rig_helper_class.set_cylinder_position(self.base_to_shoulder_cylinder_name,
                                                    self.base_to_shoulder_lower_cylinder_cluster_name,
                                                    self.base_to_shoulder_upper_cylinder_cluster_name,
                                                    self.shoulder_sphere_name,
                                                    self.base_sphere_name,
                                                    rotate_val=[self.cylinder_rotate[0],
                                                                self.cylinder_rotate[1],
                                                                self.cylinder_rotate[2]])

        # SHOULDER TO UPPER HAND CYLINDER
        self.shouler_to_upper_hand_common = self.prefix_name + "_" + self.side + "_Hand_Shoulder_to_upper_hand_Tem_" + str(
            self.val)
        self.shouler_to_upper_hand_cylinder_name = self.shouler_to_upper_hand_common + '_Geo'
        self.shouler_to_upper_hand_lower_cylinder_cluster_name = self.prefix_name + "_" + self.side + "_Hand_Shoulder_to_upper_hand_Lower_Tem_" + str(
            self.val) + '_Clu'
        self.shouler_to_upper_hand_lower_cylinder_cluster_handle_name = self.shouler_to_upper_hand_lower_cylinder_cluster_name + 'Handle'
        self.shouler_to_upper_hand_upper_cylinder_cluster_name = self.prefix_name + "_" + self.side + "_Hand_Shoulder_to_upper_hand_Upper_Tem_" + str(
            self.val) + '_Clu'
        self.shouler_to_upper_hand_upper_cylinder_cluster_handle_name = self.shouler_to_upper_hand_upper_cylinder_cluster_name + 'Handle'
        self.cylinder_rotate = [0, 0, 90]
        self.cluster_list.append(self.shouler_to_upper_hand_lower_cylinder_cluster_name)
        self.cluster_list.append(self.shouler_to_upper_hand_upper_cylinder_cluster_name)
        self.cylinder_list.append(self.shouler_to_upper_hand_cylinder_name)
        self.rig_helper_class.set_cylinder_position(self.shouler_to_upper_hand_cylinder_name,
                                                    self.shouler_to_upper_hand_lower_cylinder_cluster_name,
                                                    self.shouler_to_upper_hand_upper_cylinder_cluster_name,
                                                    self.upper_hand_sphere_name,
                                                    self.shoulder_sphere_name,
                                                    rotate_val=[self.cylinder_rotate[0],
                                                                self.cylinder_rotate[1],
                                                                self.cylinder_rotate[2]])

        self.upper_hand_to_lbow_hand_common = self.prefix_name + "_" + self.side + "_Hand_upper_hand_to_lbow_Tem_" + str(
            self.val)
        self.upper_hand_to_lbow_hand_cylinder_name = self.upper_hand_to_lbow_hand_common + '_Geo'
        self.upper_hand_to_lbow_hand_lower_cylinder_cluster_name = self.prefix_name + "_" + self.side + "_Hand_upper_hand_to_lbow_Lower_Tem_" + str(
            self.val) + '_Clu'
        self.upper_hand_to_lbow_hand_lower_cylinder_cluster_handle_name = self.upper_hand_to_lbow_hand_lower_cylinder_cluster_name + 'Handle'
        self.upper_hand_to_lbow_hand_upper_cylinder_cluster_name = self.prefix_name + "_" + self.side + "_Hand_upper_hand_to_lbow_Upper_Tem_" + str(
            self.val) + '_Clu'
        self.upper_hand_to_lbow_hand_upper_cylinder_cluster_handle_name = self.upper_hand_to_lbow_hand_upper_cylinder_cluster_name + 'Handle'
        self.cylinder_rotate = [0, 0, 90]
        self.cluster_list.append(self.upper_hand_to_lbow_hand_lower_cylinder_cluster_name)
        self.cluster_list.append(self.upper_hand_to_lbow_hand_upper_cylinder_cluster_name)
        self.cylinder_list.append(self.upper_hand_to_lbow_hand_cylinder_name)
        self.rig_helper_class.set_cylinder_position(self.upper_hand_to_lbow_hand_cylinder_name,
                                                    self.upper_hand_to_lbow_hand_lower_cylinder_cluster_name,
                                                    self.upper_hand_to_lbow_hand_upper_cylinder_cluster_name,
                                                    self.lbow_sphere_name,
                                                    self.upper_hand_sphere_name,
                                                    rotate_val=[self.cylinder_rotate[0],
                                                                self.cylinder_rotate[1],
                                                                self.cylinder_rotate[2]])

        self.lbow_to_hand_hand_common = self.prefix_name + "_" + self.side + "_Hand_lbow_to_Hand_Tem_" + str(
            self.val)
        self.lbow_to_hand_hand_cylinder_name = self.lbow_to_hand_hand_common + '_Geo'
        self.lbow_to_hand_hand_lower_cylinder_cluster_name = self.prefix_name + "_" + self.side + "_Hand_lbow_to_hand_Lower_Tem_" + str(
            self.val) + '_Clu'
        self.lbow_to_hand_hand_lower_cylinder_cluster_handle_name = self.lbow_to_hand_hand_lower_cylinder_cluster_name + 'Handle'
        self.lbow_to_hand_hand_upper_cylinder_cluster_name = self.prefix_name + "_" + self.side + "_Hand_lbow_to_hand_Upper_Tem_" + str(
            self.val) + '_Clu'
        self.lbow_to_hand_hand_upper_cylinder_cluster_handle_name = self.lbow_to_hand_hand_upper_cylinder_cluster_name + 'Handle'
        self.cylinder_rotate = [0, 0, 90]
        self.cluster_list.append(self.lbow_to_hand_hand_lower_cylinder_cluster_name)
        self.cluster_list.append(self.lbow_to_hand_hand_upper_cylinder_cluster_name)
        self.cylinder_list.append(self.lbow_to_hand_hand_cylinder_name)
        self.rig_helper_class.set_cylinder_position(self.lbow_to_hand_hand_cylinder_name,
                                                    self.lbow_to_hand_hand_lower_cylinder_cluster_name,
                                                    self.lbow_to_hand_hand_upper_cylinder_cluster_name,
                                                    self.hand_sphere_name,
                                                    self.lbow_sphere_name,
                                                    rotate_val=[self.cylinder_rotate[0],
                                                                self.cylinder_rotate[1],
                                                                self.cylinder_rotate[2]])

        # hand to hand end
        self.hand_to_hand_end_hand_common = self.prefix_name + "_" + self.side + "_Hand_Hand_to_Hand_End_Tem_" + str(
            self.val)
        self.hand_to_hand_end_hand_cylinder_name = self.hand_to_hand_end_hand_common + '_Geo'
        self.hand_to_hand_end_hand_lower_cylinder_cluster_name = self.prefix_name + "_" + self.side + "_Hand_Hand_to_Hand_End_Lower_Tem_" + str(
            self.val) + '_Clu'
        self.hand_to_hand_end_hand_lower_cylinder_cluster_handle_name = self.hand_to_hand_end_hand_lower_cylinder_cluster_name + 'Handle'
        self.hand_to_hand_end_hand_upper_cylinder_cluster_name = self.prefix_name + "_" + self.side + "_Hand_Hand_to_Hand_End_Upper_Tem_" + str(
            self.val) + '_Clu'
        self.hand_to_hand_end_hand_upper_cylinder_cluster_handle_name = self.hand_to_hand_end_hand_upper_cylinder_cluster_name + 'Handle'
        self.cylinder_rotate = [0, 0, 90]
        self.cluster_list.append(self.hand_to_hand_end_hand_lower_cylinder_cluster_name)
        self.cluster_list.append(self.hand_to_hand_end_hand_upper_cylinder_cluster_name)
        self.cylinder_list.append(self.hand_to_hand_end_hand_cylinder_name)
        self.rig_helper_class.set_cylinder_position(self.hand_to_hand_end_hand_cylinder_name,
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
        self.base_parent_const_list = [self.base_clu_handle_name,
                                       self.base_to_shoulder_upper_cylinder_cluster_handle_name]
        self.controller_small_big(base_name=self.base_common,
                                  parent_list=self.base_parent_const_list,
                                  pos=self.base_pos)
        self.arm_base_inner_ctrl = self.base_common + '_Inner_Ctrl'
        self.arm_base_outer_ctrl = self.base_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.arm_base_outer_ctrl)
        self.mirror_list.append(self.arm_base_outer_ctrl)
        self.mirror_list.append(self.arm_base_inner_ctrl)

        # SHOULDER CONTROLLER
        self.base_parent_const_list = [self.shoulder_clu_handle_name,
                                       self.base_to_shoulder_lower_cylinder_cluster_handle_name,
                                       self.shouler_to_upper_hand_upper_cylinder_cluster_handle_name]
        self.controller_small_big(base_name=self.shoulder_common,
                                  parent_list=self.base_parent_const_list,
                                  pos=self.shoulder_pos)
        self.arm_shoulder_inner_ctrl = self.shoulder_common + '_Inner_Ctrl'
        self.arm_shoulder_outer_ctrl = self.shoulder_common + '_Outer_Ctrl'
        cmds.parent(self.arm_shoulder_outer_ctrl,self.arm_base_outer_ctrl)
        self.mirror_list.append(self.arm_shoulder_outer_ctrl)
        self.mirror_list.append(self.arm_shoulder_inner_ctrl)

        # UPPER ARM
        self.base_parent_const_list = [self.upper_handle_clu_handle_name,
                                       self.shouler_to_upper_hand_lower_cylinder_cluster_handle_name,
                                       self.upper_hand_to_lbow_hand_upper_cylinder_cluster_handle_name]
        self.controller_small_big(base_name=self.upper_hand_common,
                                  parent_list=self.base_parent_const_list,
                                  pos=self.upper_hand_pos)
        self.arm_upper_hand_inner_ctrl = self.upper_hand_common + '_Inner_Ctrl'
        self.arm_upper_hand_outer_ctrl = self.upper_hand_common + '_Outer_Ctrl'
        cmds.parent(self.arm_upper_hand_outer_ctrl, self.arm_shoulder_outer_ctrl)
        self.mirror_list.append(self.arm_upper_hand_inner_ctrl)
        self.mirror_list.append(self.arm_upper_hand_outer_ctrl)

        # LBOW
        self.base_parent_const_list = [self.lbow_clu_handle_name,
                                       self.upper_hand_to_lbow_hand_lower_cylinder_cluster_handle_name,
                                       self.lbow_to_hand_hand_upper_cylinder_cluster_handle_name]
        self.controller_small_big(base_name=self.lbow_common,
                                  parent_list=self.base_parent_const_list,
                                  pos=self.lbow_pos)
        self.arm_lbow_inner_ctrl = self.lbow_common + '_Inner_Ctrl'
        self.arm_lbow_outer_ctrl = self.lbow_common + '_Outer_Ctrl'
        cmds.parent(self.arm_lbow_outer_ctrl, self.arm_upper_hand_outer_ctrl)
        self.mirror_list.append(self.arm_lbow_inner_ctrl)
        self.mirror_list.append(self.arm_lbow_outer_ctrl)

        # HAND
        self.base_parent_const_list = [self.hand_clu_handle_name,
                                       self.lbow_to_hand_hand_lower_cylinder_cluster_handle_name,
                                       self.hand_to_hand_end_hand_upper_cylinder_cluster_handle_name]
        self.controller_small_big(base_name=self.hand_common,
                                  parent_list=self.base_parent_const_list,
                                  pos=self.hand_pos)
        self.arm_hand_inner_ctrl = self.hand_common + '_Inner_Ctrl'
        self.arm_hand_outer_ctrl = self.hand_common + '_Outer_Ctrl'
        cmds.parent(self.arm_hand_outer_ctrl, self.arm_lbow_outer_ctrl)
        self.mirror_list.append(self.arm_hand_inner_ctrl)
        self.mirror_list.append(self.arm_hand_outer_ctrl)

        # HAND END
        self.base_parent_const_list = [self.hand_end_clu_handle_name,
                                       self.hand_to_hand_end_hand_lower_cylinder_cluster_handle_name]
        self.controller_small_big(base_name=self.hand_end_common,
                                  parent_list=self.base_parent_const_list,
                                  pos=self.hand_end_pos)
        self.arm_hand_end_inner_ctrl = self.hand_end_common + '_Inner_Ctrl'
        self.arm_hand_end_outer_ctrl = self.hand_end_common + '_Outer_Ctrl'
        cmds.parent(self.arm_hand_end_outer_ctrl, self.arm_hand_outer_ctrl)
        self.mirror_list.append(self.arm_hand_end_inner_ctrl)
        self.mirror_list.append(self.arm_hand_end_outer_ctrl)

        # roll bone
        self.roll_bone('Upper',
                       self.arm_upper_hand_inner_ctrl,
                       self.arm_lbow_inner_ctrl,
                       self.upper_arm_roll)
        self.roll_bone('Lower',
                       self.arm_lbow_inner_ctrl,
                       self.arm_hand_inner_ctrl,
                       self.lower_arm_roll)

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
        self.rig_helper_class.set_controller(self.base_inner_ctrl, pos, self.base_ctrl_size_ctrl,
                                             self.base_ctrl_roate, self.base_parent_const_list,
                                             self.base_parent_const_list,
                                             color=self.base_ctrl_color,
                                             freez_trans=self.base_ctrl_freez_trans,
                                             freez_rotate=self.base_ctrl_freez_rotate,
                                             freez_scale=self.base_ctrl_freez_scale)

        # BIF CONTROLLER
        self.base_outer_ctrl = base_name + '_Outer_Ctrl'
        self.base_ctrl_size_ctrl = self.ctrl_outer_size
        self.base_ctrl_roate = self.ctrl_rotate
        self.base_parent_const_list = []
        self.rig_helper_class.set_controller(self.base_outer_ctrl, pos, self.base_ctrl_size_ctrl,
                                             self.base_ctrl_roate, self.base_parent_const_list,
                                             self.base_parent_const_list,
                                             color=self.base_ctrl_color,
                                             freez_trans=self.base_ctrl_freez_trans,
                                             freez_rotate=self.base_ctrl_freez_rotate,
                                             freez_scale=self.base_ctrl_freez_scale)
        cmds.select(self.base_inner_ctrl, self.base_outer_ctrl)
        cmds.parent()

    def final_grp(self):
        list_grp = [self.clu_grp_name, self.ctrl_grp_name, self.sphere_grp_name, self.cylinder_grp_name,self.crv_grp_name]
        list = [self.cluster_list,self.ctrl_list,self.sphere_list,self.cylinder_list,self.crv_list]
        main_group_name = self.prefix_name + '_' + self.side + '_Arm_Tem_' + str(self.val) + '_Main_Grp'
        a = 0
        while a < len(list):
            for each in list[a]:
                if cmds.objectType(each) == 'cluster':
                    name = each + 'Handle'
                    cmds.setAttr((name + '.v'),0)
                else:
                    name = each
                self.rig_helper_class.grp_create(object_name=name,
                                                 grp_name=list_grp[a])

            self.rig_helper_class.grp_create(object_name=list_grp[a],
                                             grp_name=main_group_name)
            a+=1

        arm_grp_name  = 'Arm_Grp'
        self.rig_helper_class.grp_create(object_name=main_group_name,
                                         grp_name=arm_grp_name)

    def roll_bone(self, type, upper_object, lower_object, no_of_bone):

        # create a curve
        self.curve_common = self.prefix_name + "_" + self.side + "_Arm_" + type + "_Tem_" + str(self.val)
        self.curve_name = self.curve_common + '_Crv'
        self.curve_shape_name = self.curve_name + 'Shape'
        self.curve_0_clu_name = self.prefix_name + "_" + self.side + "_Arm_" + type + "_0_Tem_" + str(
            self.val) + '_Clu'
        self.curve_0_clu_handle_name = self.curve_0_clu_name + 'Handle'
        self.curve_1_clu_name = self.prefix_name + "_" + self.side + "_Arm_" + type + "_1_Tem_" + str(
            self.val) + '_Clu'
        self.curve_1_clu_handle_name = self.curve_1_clu_name + 'Handle'
        self.crv_list.append(self.curve_name)
        cmds.curve(d=1, p=[(0, 0, 0), (12, 0, 0)], k=[0, 1], n=self.curve_name)
        self.shape_name = cmds.listRelatives(self.curve_name, s=True)[0]
        cmds.rename(self.shape_name, self.curve_shape_name)
        cmds.select(self.curve_name + ".cv[0]")
        cmds.cluster(n=self.curve_0_clu_name)
        self.rig_helper_class.parent_constraint(upper_object,
                                           [self.curve_0_clu_handle_name])
        cmds.select(self.curve_name + ".cv[1]")
        cmds.cluster(n=self.curve_1_clu_name)
        self.rig_helper_class.parent_constraint(lower_object,
                                           [self.curve_1_clu_handle_name])
        self.cluster_list.append(self.curve_0_clu_name)
        self.cluster_list.append(self.curve_1_clu_name)

        # create a point on curve
        a = 0
        toal_minus = 0
        value = 1.0 - toal_minus
        average_val = value / (no_of_bone + 1.0)
        start_val = average_val
        while a < no_of_bone:
            common_name = self.prefix_name + "_" + self.side + "_Arm_" + type + "_" + str(a) + "_Tem_" + str(
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

            self.rig_helper_class.make_refrence(self.sphere_name)
            cmds.setAttr((self.poc_name + '.parameter'), start_val)
            start_val += average_val
            a += 1

    def finger_def(self):
        # get the rotation value
        get_attr = cmds.getAttr(self.arm_hand_outer_ctrl + '.r')[0]
        cmds.setAttr((self.arm_hand_outer_ctrl + '.rx'), 0)
        cmds.setAttr((self.arm_hand_outer_ctrl + '.ry'), 0)
        cmds.setAttr((self.arm_hand_outer_ctrl + '.rz'), 0)

        a = 0
        self.locator_list = []

        x_val = 0
        while a < len(self.finger_list):
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
        if self.side == 'L':
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
        while a < len(self.finger_list):
            loc_name = 'Finger_' + str(a) + '_Loc'
            self.finger_query = int(self.finger_list[a])
            b = 0
            x_value = 0
            while b < int(self.finger_query):
                cmds.select(loc_name)
                cmds.Duplicate()
                sel_new_loc = cmds.ls(sl=True)[0]
                new_loc_name = 'Finger_' + str(a) + '_' + str(b) + '_Loc'
                cmds.rename(sel_new_loc, new_loc_name)
                cmds.select(new_loc_name)
                cmds.setAttr((new_loc_name + '.tz'), x_value)

                if self.side == 'L':
                    x_value += 3
                else:
                    x_value -= 3
                b += 1
            a += 1

        # now get each positiona dn create a finger
        a = 0
        while a < len(self.finger_list):
            self.finger_query = int(self.finger_list[a])
            self.finger_indi_def(finger_query=self.finger_query,
                                 value=a)
            a += 1

        a = 0
        while a < len(self.finger_list):
            self.loc_position = cmds.xform(self.locator_list[a], q=1, ws=1, rp=1)
            self.finger_query = int(self.finger_list[a])
            self.finger_indi_parent_def(finger_query=self.finger_query,
                                        value=a)
            a += 1

        cmds.select(self.locator_new_grp_name)
        cmds.delete()

        cmds.setAttr((self.arm_hand_outer_ctrl + '.rx'), get_attr[0])
        cmds.setAttr((self.arm_hand_outer_ctrl + '.ry'), get_attr[1])
        cmds.setAttr((self.arm_hand_outer_ctrl + '.rz'), get_attr[2])

    def finger_indi_def(self, finger_query, value):
        b = 0
        while b < finger_query:
            self.cylinder_rotate = [0, 0, -90]
            self.finger_common = self.prefix_name + "_" + self.side + "_Arm_Finger_" + str(value + 1) + '_' + str(
                b + 1) + "_Tem_" + str(self.val)
            self.finger_sphere_name = self.finger_common + "_Geo"
            self.finger_sphere_clu_name = self.finger_common + '_Clu'
            self.finger_sphere_clu_handle_name = self.finger_sphere_clu_name + 'Handle'
            # self.finger_default_pos = [61.0,0,]
            # Finger_0_0_Loc
            loc_name = 'Finger_' + str(value) + '_' + str(b) + '_Loc'

            self.finger_pos = cmds.xform(loc_name, q=1, ws=1, rp=1)

            self.sphere_list.append(self.finger_sphere_name)
            self.cluster_list.append(self.finger_sphere_clu_handle_name)
            self.rig_helper_class.set_sphere_position(self.finger_sphere_name,
                                                  self.finger_pos,
                                                  self.finger_sphere_clu_name)
            cmds.setAttr((self.finger_sphere_clu_handle_name + '.v'),0)

            if b == 0:
                self.cylinder_name = self.prefix_name + '_' + self.side + "_Arm_Finger_Hand_to_" + str(
                    value + 1) + "_" + str(b + 1) + "_Tem_" + str(self.val) + "_Cylinder_Geo"
                self.cylinder_upper_cluster_name = self.prefix_name + '_' + self.side + "_Arm_Finger_Hand_to_Upper_" + str(
                    value + 1) + "_" + str(b + 1) + "_Tem_" + str(self.val) + "_Clu"
                self.finger_to_hand_cylinder_upper_cluster_handle_name = self.cylinder_upper_cluster_name + 'Handle'
                self.cylinder_lower_cluster_name = self.prefix_name + '_' + self.side + "_Arm_Finger_Hand_to_Lower_" + str(
                    value + 1) + "_" + str(b + 1) + "_Tem_" + str(self.val) + "_Clu"
                self.cylinder_lower_cluster_handle_name = self.cylinder_lower_cluster_name + 'Handle'
                self.rig_helper_class.set_cylinder_position(self.cylinder_name,
                                                        self.cylinder_lower_cluster_name,
                                                        self.cylinder_upper_cluster_name,
                                                        self.hand_sphere_name,
                                                        self.finger_sphere_name,
                                                        rotate_val=self.cylinder_rotate)
                cmds.setAttr((self.finger_to_hand_cylinder_upper_cluster_handle_name + '.v'),0)
                cmds.setAttr((self.cylinder_lower_cluster_handle_name + '.v'), 0)
                self.cluster_list.append(self.finger_to_hand_cylinder_upper_cluster_handle_name)
                self.cluster_list.append(self.cylinder_lower_cluster_handle_name)
                self.cylinder_list.append(self.cylinder_name)

            if b+1 != 1:
                self.cylinder_name = self.prefix_name + '_' + self.side + "_Arm_Finger_" + str(
                    value + 1) + "_" + str(b + 1) + "_Tem_" + str(self.val) + "_Cylinder_Geo"
                self.cylinder_upper_cluster_name = self.prefix_name + '_' + self.side + "_Arm_Finger_Upper_" + str(
                    value + 1) + "_" + str(b + 1) + "_Tem_" + str(self.val) + "_Clu"
                self.cylinder_upper_cluster_handle_name = self.cylinder_upper_cluster_name + 'Handle'
                self.cylinder_lower_cluster_name = self.prefix_name + '_' + self.side + "_Arm_Finger_Lower_" + str(
                    value + 1) + "_" + str(b + 1) + "_Tem_" + str(self.val) + "_Clu"
                self.cylinder_lower_cluster_handle_name = self.cylinder_lower_cluster_name + 'Handle'
                self.current_sphere_name = self.prefix_name + '_' + self.side + "_Arm_Finger_" + str(
                    value + 1) + "_" + str(b) + "_Tem_" + str(self.val) + "_Geo"
                self.rig_helper_class.set_cylinder_position(self.cylinder_name,
                                                        self.cylinder_lower_cluster_name,
                                                        self.cylinder_upper_cluster_name,
                                                        self.current_sphere_name,
                                                        self.finger_sphere_name,
                                                        rotate_val=self.cylinder_rotate)
                self.cluster_list.append(self.cylinder_upper_cluster_handle_name)
                self.cluster_list.append(self.cylinder_lower_cluster_handle_name)
                self.cylinder_list.append(self.cylinder_name)
                cmds.setAttr((self.cylinder_upper_cluster_handle_name + '.v'), 0)
                cmds.setAttr((self.cylinder_lower_cluster_handle_name + '.v'), 0)

                # create a controller and snap
                previous_upper_cluster_handle_name = self.prefix_name + "_" + self.side + "_Arm_Finger_Upper_" + str(
                    value + 1) + '_' + str(b + 1) + "_Tem_" + str(self.val) + '_CluHandle'
                next_lower_cluster_handle_name = self.prefix_name + "_" + self.side + "_Arm_Finger_Lower_" + str(
                    value + 1) + '_' + str(b + 2) + "_Tem_" + str(self.val) + '_CluHandle'
                self.base_parent_const_list = [self.finger_sphere_clu_handle_name,
                                               previous_upper_cluster_handle_name]
                self.controller_small_big(base_name=self.finger_common,
                                          parent_list=self.base_parent_const_list,
                                          pos=self.finger_pos)
                self.inner_ctrl_name = self.finger_common + '_Inner_Ctrl'
                self.outer_ctrl_name = self.finger_common + '_Outer_Ctrl'
                self.mirror_list.append(self.inner_ctrl_name)
                self.mirror_list.append(self.outer_ctrl_name)

            b+=1

    def finger_indi_parent_def(self, finger_query, value):
        b = 0
        while b < finger_query:
            self.finger_common = self.prefix_name + "_" + self.side + "_Arm_Finger_" + str(value + 1) + '_' + str(
                b + 1) + "_Tem_" + str(self.val)
            self.finger_sphere_name = self.finger_common + "_Geo"
            self.finger_sphere_clu_name = self.finger_common + '_Clu'
            self.finger_sphere_clu_handle_name = self.finger_sphere_clu_name + 'Handle'
            loc_name = 'Finger_' + str(value) + '_' + str(b) + '_Loc'

            self.finger_pos = cmds.xform(loc_name, q=1, ws=1, rp=1)
            if b==0:
                # create a controller and snap
                previous_upper_cluster_handle_name = self.prefix_name + "_" + self.side + "_Arm_Finger_Hand_to_Upper_" + str(
                    value + 1) + '_' + str(b + 1) + "_Tem_" + str(self.val) + '_CluHandle'
                previous_lower_cluster_handle_name = self.prefix_name + "_" + self.side + "_Arm_Finger_Hand_to_Lower_" + str(
                    value + 1) + '_' + str(b + 1) + "_Tem_" + str(self.val) + '_CluHandle'
                next_lower = self.prefix_name + "_" + self.side + "_Arm_Finger_Lower_" + str(value + 1) + '_' + str(
                    b + 2) + "_Tem_" + str(self.val) + '_CluHandle'
                self.base_parent_const_list = [self.finger_sphere_clu_handle_name,
                                               previous_upper_cluster_handle_name,
                                               next_lower]
                self.controller_small_big(base_name=self.finger_common,
                                          parent_list=self.base_parent_const_list,
                                          pos=self.finger_pos)
                self.arm_shoulder_inner_ctrl = self.finger_common + '_Inner_Ctrl'
                self.first_finger_outer = self.finger_common + '_Outer_Ctrl'
                first_finger_outer_grp_name = self.first_finger_outer + '_Grp'
                cmds.select(self.first_finger_outer)
                cmds.group(n=first_finger_outer_grp_name)
                self.ctrl_list.append(first_finger_outer_grp_name)
                cmds.parentConstraint(self.arm_hand_outer_ctrl,first_finger_outer_grp_name,mo=True)
                cmds.scaleConstraint(self.arm_hand_outer_ctrl, first_finger_outer_grp_name, mo=True)


                cmds.parentConstraint(self.arm_hand_inner_ctrl, previous_lower_cluster_handle_name, mo=False)

                # parent hand controller to the finger each one controller
                cmds.select(self.first_finger_outer, self.arm_hand_outer_ctrl)
                cmds.parent()

            self.arm_shoulder_inner_ctrl = self.finger_common + '_Inner_Ctrl'
            self.arm_shoulder_outer_ctrl = self.finger_common + '_Outer_Ctrl'
            next_cluster_lower_cluster_handle_name = self.prefix_name + '_' + self.side + "_Arm_Finger_Lower_" + str(
                value + 1) + "_" + str(b + 2) + "_Tem_" + str(self.val) + "_CluHandle"
            next_ctrl_outer_name = self.prefix_name + "_" + self.side + "_Arm_Finger_" + str(value + 1) + '_' + str(
                b + 2) + "_Tem_" + str(self.val) + '_Outer_Ctrl'
            if cmds.objExists(next_ctrl_outer_name):
                cmds.select(next_ctrl_outer_name, self.arm_shoulder_outer_ctrl)
                cmds.parent()
                cmds.parentConstraint(self.arm_shoulder_inner_ctrl, next_cluster_lower_cluster_handle_name, mo=False)
            b+=1














