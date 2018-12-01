import maya.cmds as cmds
import rig_helper
reload(rig_helper)



class BACK_LEG:
    def __init__(self):
        self.rig_helper_class = rig_helper.rig_help()

    def new(self,mirror,left_leg,right_leg,hip,thine_to_knee,knee_to_foot,foot,no_finger,prefix_name,finger_list,
            pos_list,butt,side,base_ctrl_color,leg_finger):
        self.mirror = mirror
        self.left_leg = left_leg
        self.right_leg = right_leg
        self.hip = hip
        self.thine_to_knee = int(thine_to_knee)
        self.knee_to_foot = int(knee_to_foot)
        self.foot = foot
        self.butt = butt
        self.no_finger = int(no_finger)
        self.prefix_name = prefix_name
        self.finger_list = finger_list
        self.pos_list = pos_list
        self.hip_pos = [0, 88, 3]
        self.side = side
        self.base_ctrl_color = base_ctrl_color
        self.leg_finger = leg_finger
        self.type = 'Animal'

        self.thine_pos = pos_list['thine_pos']
        self.shine_pos = pos_list['shine_pos']
        self.foot_pos = pos_list['foot_pos']
        self.foot_offset_1_pos = pos_list['foot_offset_1']
        self.foot_offset_2_pos = pos_list['foot_offset_2']
        self.foot_offset_3_pos = pos_list['foot_offset_2']
        self.foot_end_pos = pos_list['foot_end']
        self.foot_back_pos = pos_list['foot_back']
        self.foot_side_1_pos = pos_list['foot_side_1']
        self.foot_side_2_pos = pos_list['foot_side_2']
        self.leg_center_pos = pos_list['leg_Center']

        self.leg_create(self.side)

    def leg_create(self,side):
        self.side = side
        if cmds.objExists('*_' + self.side + '_' + self.type + '_Backt_Leg_Tem_*_Main_Grp'):
            cmds.select('*_' + self.side + '_' + self.type + '_Back_Leg_Tem_*_Main_Grp')
            sel_main_grp = cmds.ls(sl=True)
            len_sel_main_grp = len(sel_main_grp)
            self.val = len_sel_main_grp + 1
        else:
            self.val = 1

        # Create a Var
        self.pos_list = [self.thine_pos, self.shine_pos, self.foot_pos, self.foot_offset_1_pos,
                         self.foot_offset_2_pos, self.foot_end_pos, self.foot_back_pos, self.foot_back_pos,
                         self.foot_side_1_pos, self.foot_side_2_pos]
        self.leg_var(prefix_name=self.prefix_name,
                     type=self.type,
                     side= self.side,
                     val=self.val)


    def leg_var(self,prefix_name,type,side,val):
        self.prefix_name = prefix_name
        self.type = type
        self.side = side
        self.val = val

        self.sphere_list = []
        self.cluster_list = []
        self.cylinder_list = []
        self.ctrl_list = []
        self.crv_list = []

        # GRP NAME
        # self.clu_grp_name, self.ctrl_grp_name, self.sphere_grp_name, self.cylinder_grp_name,self.crv_grp_name
        grp_common_name = self.prefix_name + '_' + self.side + '_' + self.type + '_Back_Leg_Tem_' + str(self.val)
        self.clu_grp_name = grp_common_name + '_Clu_Grp'
        self.sphere_grp_name = grp_common_name + '_Sphere_Grp'
        self.cylinder_grp_name = grp_common_name + '_Cylinder_Grp'
        self.ctrl_grp_name = grp_common_name + '_Ctrl_Grp'
        self.crv_grp_name = grp_common_name + '_Crv_Grp'

        # THINE
        self.thine_common = self.prefix_name + "_" + self.side + '_' + self.type + '_Back_Leg_Thine_Tem_' + str(
            self.val)
        self.thine_sphere_name, self.thine_clu_name, self.thine_clu_handle_name = self.rig_helper_class.get_var(
            common_name=self.thine_common)
        self.sphere_list.append(self.thine_sphere_name)
        self.cluster_list.append(self.thine_clu_name)

        # SHINE
        self.shine_common = self.prefix_name + "_" + self.side + '_' + self.type + '_Back_Leg_Shine_Tem_' + str(
            self.val)
        self.shine_sphere_name, self.shine_clu_name, self.shine_clu_handle_name = self.rig_helper_class.get_var(
            common_name=self.shine_common)
        self.sphere_list.append(self.shine_sphere_name)
        self.cluster_list.append(self.shine_clu_name)

        # FOOT
        self.foot_common = self.prefix_name + "_" + self.side + '_' + self.type + '_Back_Leg_Foot_Tem_' + str(
            self.val)
        self.foot_sphere_name, self.foot_clu_name, self.foot_clu_handle_name = self.rig_helper_class.get_var(
            common_name=self.foot_common)
        self.sphere_list.append(self.foot_sphere_name)
        self.cluster_list.append(self.foot_clu_name)

        # FOOR OFFSET 1
        self.foot_offset_1_common = self.prefix_name + "_" + self.side + '_' + self.type + '_Back_Leg_Foot_Offset_1_Tem_' + str(
            self.val)
        self.foot_offset_1_sphere_name, self.foot_offset_1_clu_name, self.foot_offset_1_clu_handle_name = self.rig_helper_class.get_var(
            common_name=self.foot_offset_1_common)
        self.sphere_list.append(self.foot_offset_1_sphere_name)
        self.cluster_list.append(self.foot_offset_1_clu_name)

        # FOOT OFFSET 2
        self.foot_offset_2_common = self.prefix_name + "_" + self.side + '_' + self.type + '_Back_Leg_Foot_Offset_2_Tem_' + str(
            self.val)
        self.foot_offset_2_sphere_name, self.foot_offset_2_clu_name, self.foot_offset_2_clu_handle_name = self.rig_helper_class.get_var(
            common_name=self.foot_offset_2_common)
        self.sphere_list.append(self.foot_offset_2_sphere_name)
        self.cluster_list.append(self.foot_offset_2_clu_name)

        # FOOT END
        self.foot_end_common = self.prefix_name + "_" + self.side + '_' + self.type + '_Back_Leg_Foot_End_Tem_' + str(
            self.val)
        self.foot_end_sphere_name, self.foot_end_clu_name, self.foot_end_clu_handle_name = self.rig_helper_class.get_var(
            common_name=self.foot_end_common)
        self.sphere_list.append(self.foot_end_sphere_name)
        self.cluster_list.append(self.foot_end_clu_name)

        self.thine_pos = pos_list['thine_pos']
        self.shine_pos = pos_list['shine_pos']
        self.foot_pos = pos_list['foot_pos']
        self.foot_offset_1_pos = pos_list['foot_offset_1']
        self.foot_offset_2_pos = pos_list['foot_offset_2']
        self.foot_end_pos = pos_list['foot_end']
        self.foot_back_pos = pos_list['foot_back']
        self.foot_side_1_pos = pos_list['foot_side_1']
        self.foot_side_2_pos = pos_list['foot_side_2']
        self.leg_center_pos = pos_list['leg_Center']






























