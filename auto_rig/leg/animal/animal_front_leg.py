
import maya.cmds as cmds
import rig_helper
reload(rig_helper)



class FRONT_LEG:
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

        self.hand_center_pos = pos_list['leg_center']
        self.scapula_pos = pos_list['scapula_pos']
        self.upper_hand_pos = pos_list['upper_hand_pos']
        self.shoulder_pos = pos_list['shoulder_pos']
        self.lbow_pos = pos_list['lbow_pos']
        self.hand_pos = pos_list['hand_pos']
        self.hand_offset_1_pos = pos_list['hand_offset_1_pos']
        self.hand_offset_2_pos = pos_list['hand_offset_2_pos']
        self.end_pos = pos_list['end_pos']
        self.hand_side_1_pos = pos_list['hand_side_1_pos']
        self.hand_side_2_pos = pos_list['hand_side_2_pos']
        self.hand_back_pos = pos_list['hand_back_pos']
        self.shoulder_center_pos = pos_list['Shoulder_Center_pos']

        self.leg_create(self.side)


    def leg_create(self,side):
        self.side = side
        if cmds.objExists('*_' + self.side + '_' + self.type + '_Front_Leg_Tem_*_Main_Grp'):
            cmds.select('*_' + self.side + '_' + self.type + '_Front_Leg_Tem_*_Main_Grp')
            sel_main_grp = cmds.ls(sl=True)
            len_sel_main_grp = len(sel_main_grp)
            self.val = len_sel_main_grp + 1
        else:
            self.val = 1

        # Create a Var
        self.pos_list = [self.scapula_pos, self.upper_hand_pos, self.shoulder_pos, self.lbow_pos,
                         self.hand_pos, self.hand_offset_1_pos, self.hand_offset_2_pos, self.end_pos,
                         self.hand_side_1_pos, self.hand_side_2_pos, self.hand_back_pos]
        self.leg_var(prefix_name=self.prefix_name,
                     type=self.type,
                     side= self.side,
                     val=self.val)

        # Create a Sphere
        self.rig_helper_class.sphere_create(sphere_list=self.sphere_list,
                                            pos_list=self.pos_list,
                                            cluster_list=self.cluster_list)

        #Create a Cylinder
        self.leg_cylinder()

        #Create a Controller
        self.controller_def()

        # Create a Final Grp
        list_grp = [self.clu_grp_name, self.ctrl_grp_name, self.sphere_grp_name, self.cylinder_grp_name]
        list = [self.cluster_list, self.ctrl_list, self.sphere_list, self.cylinder_list]
        type = 'Leg'
        self.rig_helper_class.final_grp(type=type,
                                        list_grp=list_grp,
                                        list=list,
                                        prefix_name=self.prefix_name,
                                        side=self.side,
                                        val=self.val,
                                        character_type=self.type)
        
        cmds.setAttr((self.clu_grp_name + '.v'), 0)

        #Set the Hip if the Grp is not PARENT
        if self.hip == True:
            type_grp = type + '_Grp'
            self.rig_helper_class.set_parent(child_name=self.hand_center_outer_ctrl,
                                             grp_name=type_grp)

    def leg_var(self,prefix_name,side,type,val):
        self.prefix_name = prefix_name
        self.type = type
        self.side = side
        self.val  = val

        self.sphere_list = []
        self.cluster_list = []
        self.cylinder_list = []
        self.ctrl_list = []
        self.crv_list = []

        # GRP NAME
        # self.clu_grp_name, self.ctrl_grp_name, self.sphere_grp_name, self.cylinder_grp_name,self.crv_grp_name
        grp_common_name = self.prefix_name + '_' + self.side + '_' + self.type + '_Front_Leg_Tem_' + str(self.val)
        self.clu_grp_name = grp_common_name + '_Clu_Grp'
        self.sphere_grp_name = grp_common_name + '_Sphere_Grp'
        self.cylinder_grp_name = grp_common_name + '_Cylinder_Grp'
        self.ctrl_grp_name = grp_common_name + '_Ctrl_Grp'
        self.crv_grp_name = grp_common_name + '_Crv_Grp'

        # LEG CENTER
        #SCAPULA
        self.scapula_common = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Leg_Scapula_Tem_' + str(
            self.val)
        self.scapula_sphere_name, self.scapula_clu_name, self.scapula_clu_handle_name = self.rig_helper_class.get_var(
            common_name=self.scapula_common)
        self.sphere_list.append(self.scapula_sphere_name)
        self.cluster_list.append(self.scapula_clu_name)

        #UPPER HAND
        self.upper_hand_common = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Leg_Upper_Hand_Tem_' + str(
            self.val)
        self.upper_hand_sphere_name, self.upper_hand_clu_name, self.upper_hand_clu_handle_name = self.rig_helper_class.get_var(
            common_name=self.upper_hand_common)
        self.sphere_list.append(self.upper_hand_sphere_name)
        self.cluster_list.append(self.upper_hand_clu_name)

        #SHOULDER
        self.shoulder_common = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Leg_Shoulder_Tem_' + str(
            self.val)
        self.shoulder_sphere_name, self.shoulder_clu_name, self.shoulder_clu_handle_name = self.rig_helper_class.get_var(
            common_name=self.shoulder_common)
        self.sphere_list.append(self.shoulder_sphere_name)
        self.cluster_list.append(self.shoulder_clu_name)

        #LBOW
        self.lbow_common = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Leg_lbow_Tem_' + str(
            self.val)
        self.lbow_sphere_name, self.lbow_clu_name, self.lbow_clu_handle_name = self.rig_helper_class.get_var(
            common_name=self.lbow_common)
        self.sphere_list.append(self.lbow_sphere_name)
        self.cluster_list.append(self.lbow_clu_name)

        #HAND
        self.hand_common = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Leg_Hand_Tem_' + str(
            self.val)
        self.hand_sphere_name, self.hand_clu_name, self.hand_clu_handle_name = self.rig_helper_class.get_var(
            common_name=self.hand_common)
        self.sphere_list.append(self.hand_sphere_name)
        self.cluster_list.append(self.hand_clu_name)

        #HAND OFFSET
        self.hand_offset_1_common = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Leg_Hand_Offset_1_Tem_' + str(
            self.val)
        self.hand_offset_1_sphere_name, self.hand_offset_1_clu_name, self.hand_offset_1_clu_handle_name = self.rig_helper_class.get_var(
            common_name=self.hand_offset_1_common)
        self.sphere_list.append(self.hand_offset_1_sphere_name)
        self.cluster_list.append(self.hand_offset_1_clu_name)

        #HAND OFFSET 2
        self.hand_offset_2_common = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Leg_Hand_Offset_2_Tem_' + str(
            self.val)
        self.hand_offset_2_sphere_name, self.hand_offset_2_clu_name, self.hand_offset_2_clu_handle_name = self.rig_helper_class.get_var(
            common_name=self.hand_offset_2_common)
        self.sphere_list.append(self.hand_offset_2_sphere_name)
        self.cluster_list.append(self.hand_offset_2_clu_name)

        #END
        self.end_common = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Leg_End_Tem_' + str(
            self.val)
        self.end_sphere_name, self.end_clu_name, self.end_clu_handle_name = self.rig_helper_class.get_var(
            common_name=self.end_common)
        self.sphere_list.append(self.end_sphere_name)
        self.cluster_list.append(self.end_clu_name)

        #HAND SIDE 1
        self.hand_side_1_common = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Hand_Side_1_Tem_' + str(
            self.val)
        self.hand_side_1_sphere_name, self.hand_side_1_clu_name, self.hand_side_1_clu_handle_name = self.rig_helper_class.get_var(
            common_name=self.hand_side_1_common)
        self.sphere_list.append(self.hand_side_1_sphere_name)
        self.cluster_list.append(self.hand_side_1_clu_name)

        #HAND SIDE 2
        self.hand_side_2_common = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Hand_Side_2_Tem_' + str(
            self.val)
        self.hand_side_2_sphere_name, self.hand_side_2_clu_name, self.hand_side_2_clu_handle_name = self.rig_helper_class.get_var(
            common_name=self.hand_side_2_common)
        self.sphere_list.append(self.hand_side_2_sphere_name)
        self.cluster_list.append(self.hand_side_2_clu_name)

        #HAND BACK
        self.hand_back_common = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Hand_Back_Tem_' + str(
            self.val)
        self.hand_back_sphere_name, self.hand_back_clu_name, self.hand_back_clu_handle_name = self.rig_helper_class.get_var(
            common_name=self.hand_back_common)
        self.sphere_list.append(self.hand_back_sphere_name)
        self.cluster_list.append(self.hand_back_clu_name)

        if self.hip == True:
            self.hand_center_common = self.prefix_name + '_' + self.type + '_Front_Hand_Center_Tem_' + str(self.val)
            self.hand_center_sphere_name,self.hand_center_clu_name,self.hand_center_clu_handle_name = self.rig_helper_class.get_var(common_name=self.hand_center_common)
            if cmds.objExists(self.hand_center_sphere_name):
                pass
            else:
                self.sphere_list.append(self.hand_center_sphere_name)
                self.cluster_list.append(self.hand_center_clu_name)
                self.pos_list.append(self.hand_center_pos)

    def leg_cylinder(self):
        # SCAPULA TO UPPER HAND
        self.scapula_to_upper_hand_common = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Hand_Scapula_to_Upper_Hand_Tem_' + str(
            self.val)
        self.scapula_to_upper_hand_cylinder_name = self.scapula_to_upper_hand_common + '_Geo'
        self.scapula_to_upper_hand_lower_cylinder_cluster_name = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Hand_Scapula_to_Upper_Hand_Lower_Tem_' + str(
            self.val) + '_Clu'
        self.scapula_to_upper_hand_lower_cylinder_cluster_handle_name = self.scapula_to_upper_hand_lower_cylinder_cluster_name + 'Handle'
        self.scapula_to_upper_hand_upper_cylinder_cluster_name = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Hand_Scapula_to_Upper_Hand_Upper_Tem_' + str(
            self.val) + '_Clu'
        self.scapula_to_upper_hand_upper_cylinder_cluster_handle_name = self.scapula_to_upper_hand_upper_cylinder_cluster_name + 'Handle'
        self.cylinder_rotate = [0, 0, 0]
        self.cluster_list.append(self.scapula_to_upper_hand_lower_cylinder_cluster_handle_name)
        self.cluster_list.append(self.scapula_to_upper_hand_upper_cylinder_cluster_handle_name)
        self.cylinder_list.append(self.scapula_to_upper_hand_cylinder_name)
        self.rig_helper_class.set_cylinder_position(self.scapula_to_upper_hand_cylinder_name,
                                                    self.scapula_to_upper_hand_lower_cylinder_cluster_name,
                                                    self.scapula_to_upper_hand_upper_cylinder_cluster_name,
                                                    self.scapula_sphere_name,
                                                    self.upper_hand_sphere_name,
                                                    rotate_val=[self.cylinder_rotate[0],
                                                                self.cylinder_rotate[1],
                                                                self.cylinder_rotate[2]])

        # UPPER HAND TO SHOULDER
        self.upper_hand_to_shoulder_common = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Hand_Upper_hand_to_Shoulder_Tem_' + str(
            self.val)
        self.upper_hand_to_shoulder_cylinder_name = self.upper_hand_to_shoulder_common + '_Geo'
        self.upper_hand_to_shoulder_lower_cylinder_cluster_name = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Hand_Upper_hand_to_Shoulder_Lower_Tem_' + str(
            self.val) + '_Clu'
        self.upper_hand_to_shoulder_lower_cylinder_cluster_handle_name = self.upper_hand_to_shoulder_lower_cylinder_cluster_name + 'Handle'
        self.upper_hand_to_shoulder_upper_cylinder_cluster_name = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Hand_Upper_hand_to_Shoulder_Upper_Tem_' + str(
            self.val) + '_Clu'
        self.upper_hand_to_shoulder_upper_cylinder_cluster_handle_name = self.upper_hand_to_shoulder_upper_cylinder_cluster_name + 'Handle'
        self.cylinder_rotate = [0, 0, 0]
        self.cluster_list.append(self.upper_hand_to_shoulder_lower_cylinder_cluster_handle_name)
        self.cluster_list.append(self.upper_hand_to_shoulder_upper_cylinder_cluster_handle_name)
        self.cylinder_list.append(self.upper_hand_to_shoulder_cylinder_name)
        self.rig_helper_class.set_cylinder_position(self.upper_hand_to_shoulder_cylinder_name,
                                                    self.upper_hand_to_shoulder_lower_cylinder_cluster_name,
                                                    self.upper_hand_to_shoulder_upper_cylinder_cluster_name,
                                                    self.upper_hand_sphere_name,
                                                    self.shoulder_sphere_name,
                                                    rotate_val=[self.cylinder_rotate[0],
                                                                self.cylinder_rotate[1],
                                                                self.cylinder_rotate[2]])

        # SHOULDER TO LBOW
        self.shoulder_to_lbow_common = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Hand_Shoulder_to_lBow_Tem_' + str(
            self.val)
        self.shoulder_to_lbow_cylinder_name = self.shoulder_to_lbow_common + '_Geo'
        self.shoulder_to_lbow_lower_cylinder_cluster_name = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Hand_Shoulder_to_lBow_Lower_Tem_' + str(
            self.val) + '_Clu'
        self.shoulder_to_lbow_lower_cylinder_cluster_handle_name = self.shoulder_to_lbow_lower_cylinder_cluster_name + 'Handle'
        self.shoulder_to_lbow_upper_cylinder_cluster_name = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Hand_Shoulder_to_lBow_Upper_Tem_' + str(
            self.val) + '_Clu'
        self.shoulder_to_lbow_upper_cylinder_cluster_handle_name = self.shoulder_to_lbow_upper_cylinder_cluster_name + 'Handle'
        self.cylinder_rotate = [0, 0, 0]
        self.cluster_list.append(self.shoulder_to_lbow_lower_cylinder_cluster_handle_name)
        self.cluster_list.append(self.shoulder_to_lbow_upper_cylinder_cluster_handle_name)
        self.cylinder_list.append(self.shoulder_to_lbow_cylinder_name)
        self.rig_helper_class.set_cylinder_position(self.shoulder_to_lbow_cylinder_name,
                                                    self.shoulder_to_lbow_lower_cylinder_cluster_name,
                                                    self.shoulder_to_lbow_upper_cylinder_cluster_name,
                                                    self.shoulder_sphere_name,
                                                    self.lbow_sphere_name,
                                                    rotate_val=[self.cylinder_rotate[0],
                                                                self.cylinder_rotate[1],
                                                                self.cylinder_rotate[2]])

        # LBOW TO HAND
        self.lbow_to_hand_common = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Hand_lBow_to_Hand_Tem_' + str(
            self.val)
        self.lbow_to_hand_cylinder_name = self.lbow_to_hand_common + '_Geo'
        self.lbow_to_hand_lower_cylinder_cluster_name = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Hand_lBow_to_Hand_Lower_Tem_' + str(
            self.val) + '_Clu'
        self.lbow_to_hand_lower_cylinder_cluster_handle_name = self.lbow_to_hand_lower_cylinder_cluster_name + 'Handle'
        self.lbow_to_hand_upper_cylinder_cluster_name = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Hand_lBow_to_Hand_Upper_Tem_' + str(
            self.val) + '_Clu'
        self.lbow_to_hand_upper_cylinder_cluster_handle_name = self.lbow_to_hand_upper_cylinder_cluster_name + 'Handle'
        self.cylinder_rotate = [0, 0, 0]
        self.cluster_list.append(self.lbow_to_hand_lower_cylinder_cluster_handle_name)
        self.cluster_list.append(self.lbow_to_hand_upper_cylinder_cluster_handle_name)
        self.cylinder_list.append(self.lbow_to_hand_cylinder_name)
        self.rig_helper_class.set_cylinder_position(self.lbow_to_hand_cylinder_name,
                                                    self.lbow_to_hand_lower_cylinder_cluster_name,
                                                    self.lbow_to_hand_upper_cylinder_cluster_name,
                                                    self.lbow_sphere_name,
                                                    self.hand_sphere_name,
                                                    rotate_val=[self.cylinder_rotate[0],
                                                                self.cylinder_rotate[1],
                                                                self.cylinder_rotate[2]])

        # HAND TO HAND OFFSET 1
        self.hand_to_hand_offset_1_common = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Hand_Hand_to_Hand_Offset_1_Tem_' + str(
            self.val)
        self.hand_to_hand_offset_1_cylinder_name = self.hand_to_hand_offset_1_common + '_Geo'
        self.hand_to_hand_offset_1_lower_cylinder_cluster_name = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Hand_Hand_to_Hand_Offset_1_Lower_Tem_' + str(
            self.val) + '_Clu'
        self.hand_to_hand_offset_1_lower_cylinder_cluster_handle_name = self.hand_to_hand_offset_1_lower_cylinder_cluster_name + 'Handle'
        self.hand_to_hand_offset_1_upper_cylinder_cluster_name = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Hand_Hand_to_Hand_Offset_1_Upper_Tem_' + str(
            self.val) + '_Clu'
        self.hand_to_hand_offset_1_upper_cylinder_cluster_handle_name = self.hand_to_hand_offset_1_upper_cylinder_cluster_name + 'Handle'
        self.cylinder_rotate = [0, 0, 0]
        self.cluster_list.append(self.hand_to_hand_offset_1_lower_cylinder_cluster_handle_name)
        self.cluster_list.append(self.hand_to_hand_offset_1_upper_cylinder_cluster_handle_name)
        self.cylinder_list.append(self.hand_to_hand_offset_1_cylinder_name)
        self.rig_helper_class.set_cylinder_position(self.hand_to_hand_offset_1_cylinder_name,
                                                    self.hand_to_hand_offset_1_lower_cylinder_cluster_name,
                                                    self.hand_to_hand_offset_1_upper_cylinder_cluster_name,
                                                    self.hand_sphere_name,
                                                    self.hand_offset_1_sphere_name,
                                                    rotate_val=[self.cylinder_rotate[0],
                                                                self.cylinder_rotate[1],
                                                                self.cylinder_rotate[2]])

        # HAND OFFSET 1  TO HAND OFFSET 2
        self.hand_offset_1_to_hand_offset_2_common = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Hand_Hand_Offset_1_to_Hand_Offset_2_Tem_' + str(
            self.val)
        self.hand_offset_1_to_hand_offset_2_cylinder_name = self.hand_offset_1_to_hand_offset_2_common + '_Geo'
        self.hand_offset_1_to_hand_offset_2_lower_cylinder_cluster_name = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Hand_Hand_Offset_1_to_Hand_Offset_2_Lower_Tem_' + str(
            self.val) + '_Clu'
        self.hand_offset_1_to_hand_offset_2_lower_cylinder_cluster_handle_name = self.hand_offset_1_to_hand_offset_2_lower_cylinder_cluster_name + 'Handle'
        self.hand_offset_1_to_hand_offset_2_upper_cylinder_cluster_name = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Hand_Hand_Offset_1_to_Hand_Offset_2_Upper_Tem_' + str(
            self.val) + '_Clu'
        self.hand_offset_1_to_hand_offset_2_upper_cylinder_cluster_handle_name = self.hand_offset_1_to_hand_offset_2_upper_cylinder_cluster_name + 'Handle'
        self.cylinder_rotate = [0, 0, 0]
        self.cluster_list.append(self.hand_offset_1_to_hand_offset_2_lower_cylinder_cluster_handle_name)
        self.cluster_list.append(self.hand_offset_1_to_hand_offset_2_upper_cylinder_cluster_handle_name)
        self.cylinder_list.append(self.hand_offset_1_to_hand_offset_2_cylinder_name)
        self.rig_helper_class.set_cylinder_position(self.hand_offset_1_to_hand_offset_2_cylinder_name,
                                                    self.hand_offset_1_to_hand_offset_2_lower_cylinder_cluster_name,
                                                    self.hand_offset_1_to_hand_offset_2_upper_cylinder_cluster_name,
                                                    self.hand_offset_1_sphere_name,
                                                    self.hand_offset_2_sphere_name,
                                                    rotate_val=[self.cylinder_rotate[0],
                                                                self.cylinder_rotate[1],
                                                                self.cylinder_rotate[2]])

        # HAND OFFSET 2  TO END
        self.hand_offset_2_to_end_common = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Hand_Hand_Offset_2_to_End_Tem_' + str(
            self.val)
        self.hand_offset_2_to_end_cylinder_name = self.hand_offset_2_to_end_common + '_Geo'
        self.hand_offset_2_to_end_lower_cylinder_cluster_name = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Hand_Hand_Offset_2_to_End_Lower_Tem_' + str(
            self.val) + '_Clu'
        self.hand_offset_2_to_end_lower_cylinder_cluster_handle_name = self.hand_offset_2_to_end_lower_cylinder_cluster_name + 'Handle'
        self.hand_offset_2_to_end_upper_cylinder_cluster_name = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Hand_Hand_Offset_2_to_End_Upper_Tem_' + str(
            self.val) + '_Clu'
        self.hand_offset_2_to_end_upper_cylinder_cluster_handle_name = self.hand_offset_2_to_end_upper_cylinder_cluster_name + 'Handle'
        self.cylinder_rotate = [0, 0, 0]
        self.cluster_list.append(self.hand_offset_2_to_end_lower_cylinder_cluster_handle_name)
        self.cluster_list.append(self.hand_offset_2_to_end_upper_cylinder_cluster_handle_name)
        self.cylinder_list.append(self.hand_offset_2_to_end_cylinder_name)
        self.rig_helper_class.set_cylinder_position(self.hand_offset_2_to_end_cylinder_name,
                                                    self.hand_offset_2_to_end_lower_cylinder_cluster_name,
                                                    self.hand_offset_2_to_end_upper_cylinder_cluster_name,
                                                    self.hand_offset_2_sphere_name,
                                                    self.end_sphere_name,
                                                    rotate_val=[self.cylinder_rotate[0],
                                                                self.cylinder_rotate[1],
                                                                self.cylinder_rotate[2]])

        # HAND OFFSET 2  TO BACK
        self.hand_offset_2_to_back_common = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Hand_Hand_Offset_2_to_Back_Tem_' + str(
            self.val)
        self.hand_offset_2_to_back_cylinder_name = self.hand_offset_2_to_back_common + '_Geo'
        self.hand_offset_2_to_back_lower_cylinder_cluster_name = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Hand_Hand_Offset_2_to_Back_Lower_Tem_' + str(
            self.val) + '_Clu'
        self.hand_offset_2_to_back_lower_cylinder_cluster_handle_name = self.hand_offset_2_to_back_lower_cylinder_cluster_name + 'Handle'
        self.hand_offset_2_to_back_upper_cylinder_cluster_name = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Hand_Hand_Offset_2_to_Back_Upper_Tem_' + str(
            self.val) + '_Clu'
        self.hand_offset_2_to_back_upper_cylinder_cluster_handle_name = self.hand_offset_2_to_back_upper_cylinder_cluster_name + 'Handle'
        self.cylinder_rotate = [0, 0, 0]
        self.cluster_list.append(self.hand_offset_2_to_back_lower_cylinder_cluster_handle_name)
        self.cluster_list.append(self.hand_offset_2_to_back_upper_cylinder_cluster_handle_name)
        self.cylinder_list.append(self.hand_offset_2_to_back_cylinder_name)
        self.rig_helper_class.set_cylinder_position(self.hand_offset_2_to_back_cylinder_name,
                                                    self.hand_offset_2_to_back_lower_cylinder_cluster_name,
                                                    self.hand_offset_2_to_back_upper_cylinder_cluster_name,
                                                    self.hand_offset_2_sphere_name,
                                                    self.hand_back_sphere_name,
                                                    rotate_val=[self.cylinder_rotate[0],
                                                                self.cylinder_rotate[1],
                                                                self.cylinder_rotate[2]])

        # HAND OFFSET 2  TO HAND SIDE 1
        self.hand_offset_2_to_hand_side_1_common = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Hand_Hand_Offset_2_to_Hand_side_1_Tem_' + str(
            self.val)
        self.hand_offset_2_to_hand_side_1_cylinder_name = self.hand_offset_2_to_hand_side_1_common + '_Geo'
        self.hand_offset_2_to_hand_side_1_lower_cylinder_cluster_name = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Hand_Hand_Offset_2_to_Hand_side_1_Lower_Tem_' + str(
            self.val) + '_Clu'
        self.hand_offset_2_to_hand_side_1_lower_cylinder_cluster_handle_name = self.hand_offset_2_to_hand_side_1_lower_cylinder_cluster_name + 'Handle'
        self.hand_offset_2_to_hand_side_1_upper_cylinder_cluster_name = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Hand_Hand_Offset_2_to_Hand_side_1_Upper_Tem_' + str(
            self.val) + '_Clu'
        self.hand_offset_2_to_hand_side_1_upper_cylinder_cluster_handle_name = self.hand_offset_2_to_hand_side_1_upper_cylinder_cluster_name + 'Handle'
        self.cylinder_rotate = [0, 0, 90]
        self.cluster_list.append(self.hand_offset_2_to_hand_side_1_lower_cylinder_cluster_handle_name)
        self.cluster_list.append(self.hand_offset_2_to_hand_side_1_upper_cylinder_cluster_handle_name)
        self.cylinder_list.append(self.hand_offset_2_to_hand_side_1_cylinder_name)
        self.rig_helper_class.set_cylinder_position(self.hand_offset_2_to_hand_side_1_cylinder_name,
                                                    self.hand_offset_2_to_hand_side_1_lower_cylinder_cluster_name,
                                                    self.hand_offset_2_to_hand_side_1_upper_cylinder_cluster_name,
                                                    self.hand_offset_2_sphere_name,
                                                    self.hand_side_1_sphere_name,
                                                    rotate_val=[self.cylinder_rotate[0],
                                                                self.cylinder_rotate[1],
                                                                self.cylinder_rotate[2]])

        # HAND OFFSET 2  TO HAND SIDE 2
        self.hand_offset_2_to_hand_side_2_common = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Hand_Hand_Offset_2_to_Hand_Side_2_Tem_' + str(
            self.val)
        self.hand_offset_2_to_hand_side_2_cylinder_name = self.hand_offset_2_to_hand_side_2_common + '_Geo'
        self.hand_offset_2_to_hand_side_2_lower_cylinder_cluster_name = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Hand_Hand_Offset_2_to_Hand_Side_2_Lower_Tem_' + str(
            self.val) + '_Clu'
        self.hand_offset_2_to_hand_side_2_lower_cylinder_cluster_handle_name = self.hand_offset_2_to_hand_side_2_lower_cylinder_cluster_name + 'Handle'
        self.hand_offset_2_to_hand_side_2_upper_cylinder_cluster_name = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Hand_Hand_Offset_2_to_Hand_Side_2_Upper_Tem_' + str(
            self.val) + '_Clu'
        self.hand_offset_2_to_hand_side_2_upper_cylinder_cluster_handle_name = self.hand_offset_2_to_hand_side_2_upper_cylinder_cluster_name + 'Handle'
        self.cylinder_rotate = [0, 0, 90]
        self.cluster_list.append(self.hand_offset_2_to_hand_side_2_lower_cylinder_cluster_handle_name)
        self.cluster_list.append(self.hand_offset_2_to_hand_side_2_upper_cylinder_cluster_handle_name)
        self.cylinder_list.append(self.hand_offset_2_to_hand_side_2_cylinder_name)
        self.rig_helper_class.set_cylinder_position(self.hand_offset_2_to_hand_side_2_cylinder_name,
                                                    self.hand_offset_2_to_hand_side_2_lower_cylinder_cluster_name,
                                                    self.hand_offset_2_to_hand_side_2_upper_cylinder_cluster_name,
                                                    self.hand_offset_2_sphere_name,
                                                    self.hand_side_2_sphere_name,
                                                    rotate_val=[self.cylinder_rotate[0],
                                                                self.cylinder_rotate[1],
                                                                self.cylinder_rotate[2]])

        if self.hip == True:
            self.scapula_to_hand_center_common = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Hand_Scapula_to_Hand_Center_Tem_' + str(
                self.val)
            self.scapula_to_hand_center_cylinder_name = self.scapula_to_hand_center_common + '_Geo'
            self.scapula_to_hand_center_lower_cylinder_cluster_name = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Hand_Scapula_to_Hand_Center_Lower_Tem_' + str(
                self.val) + '_Clu'
            self.scapula_to_hand_center_lower_cylinder_cluster_handle_name = self.scapula_to_hand_center_lower_cylinder_cluster_name + 'Handle'
            self.scapula_to_hand_center_upper_cylinder_cluster_name = self.prefix_name + "_" + self.side + '_' + self.type + '_Front_Hand_Scapula_to_Hand_Center_Upper_Tem_' + str(
                self.val) + '_Clu'
            self.scapula_to_hand_center_upper_cylinder_cluster_handle_name = self.scapula_to_hand_center_upper_cylinder_cluster_name + 'Handle'
            self.cylinder_rotate = [0, 0, 90]
            self.cluster_list.append(self.scapula_to_hand_center_lower_cylinder_cluster_handle_name)
            self.cluster_list.append(self.scapula_to_hand_center_upper_cylinder_cluster_handle_name)
            self.cylinder_list.append(self.scapula_to_hand_center_cylinder_name)
            self.rig_helper_class.set_cylinder_position(self.scapula_to_hand_center_cylinder_name,
                                                        self.scapula_to_hand_center_lower_cylinder_cluster_name,
                                                        self.scapula_to_hand_center_upper_cylinder_cluster_name,
                                                        self.scapula_sphere_name,
                                                        self.hand_center_sphere_name,
                                                        rotate_val=[self.cylinder_rotate[0],
                                                                    self.cylinder_rotate[1],
                                                                    self.cylinder_rotate[2]])


    def controller_def(self):
        # CREATE CONTROLLER
        self.ctrl_lower_size = [0.5, 0.5, 0.5]
        self.ctrl_outer_size = [1.5, 1.5, 1.5]
        self.ctrl_rotate = [0, 0, 0]
        self.base_ctrl_freez_trans = True
        self.base_ctrl_freez_rotate = True
        self.base_ctrl_freez_scale = True

        # SCAPULA CONTROLLER
        self.scapula_const_list = [self.scapula_clu_handle_name,
                                 self.scapula_to_upper_hand_lower_cylinder_cluster_handle_name]
        self.rig_helper_class.controller_small_big(base_name=self.scapula_common,
                                                   parent_list=self.scapula_const_list,
                                                   pos=self.scapula_pos,
                                                   ctrl_rotate=self.ctrl_rotate,
                                                   base_ctrl_color=self.base_ctrl_color)
        self.scapula_inner_ctrl = self.scapula_common + '_Inner_Ctrl'
        self.scapula_outer_ctrl = self.scapula_common + '_Outer_Ctrl'
        scapula_ctrl_grp = self.scapula_outer_ctrl + '_Grp'
        cmds.select(self.scapula_outer_ctrl)
        cmds.group(n=scapula_ctrl_grp)
        self.ctrl_list.append(scapula_ctrl_grp)

        # UPPER HAND CONTROLLER
        self.const_list = [self.upper_hand_clu_handle_name,
                           self.scapula_to_upper_hand_upper_cylinder_cluster_handle_name,
                           self.upper_hand_to_shoulder_lower_cylinder_cluster_handle_name]
        self.rig_helper_class.controller_small_big(base_name=self.upper_hand_common,
                                                   parent_list=self.const_list,
                                                   pos=self.upper_hand_pos,
                                                   ctrl_rotate=self.ctrl_rotate,
                                                   base_ctrl_color=self.base_ctrl_color)
        self.upper_hand_inner_ctrl = self.upper_hand_common + '_Inner_Ctrl'
        self.upper_hand_outer_ctrl = self.upper_hand_common + '_Outer_Ctrl'
        cmds.parent(self.upper_hand_outer_ctrl,self.scapula_outer_ctrl)

        # SHOULDER CONTROLLER
        self.const_list = [self.shoulder_clu_handle_name,
                           self.upper_hand_to_shoulder_upper_cylinder_cluster_handle_name,
                           self.shoulder_to_lbow_lower_cylinder_cluster_handle_name]
        self.rig_helper_class.controller_small_big(base_name=self.shoulder_common,
                                                   parent_list=self.const_list,
                                                   pos=self.shoulder_pos,
                                                   ctrl_rotate=self.ctrl_rotate,
                                                   base_ctrl_color=self.base_ctrl_color)
        self.shoulder_inner_ctrl = self.shoulder_common + '_Inner_Ctrl'
        self.shoulder_outer_ctrl = self.shoulder_common + '_Outer_Ctrl'
        cmds.parent(self.shoulder_outer_ctrl, self.upper_hand_outer_ctrl)

        # LBOW CONTROLLER
        self.const_list = [self.lbow_clu_handle_name,
                           self.shoulder_to_lbow_upper_cylinder_cluster_handle_name,
                           self.lbow_to_hand_lower_cylinder_cluster_handle_name]
        self.rig_helper_class.controller_small_big(base_name=self.lbow_common,
                                                   parent_list=self.const_list,
                                                   pos=self.lbow_pos,
                                                   ctrl_rotate=self.ctrl_rotate,
                                                   base_ctrl_color=self.base_ctrl_color)
        self.lbow_inner_ctrl = self.lbow_common + '_Inner_Ctrl'
        self.lbow_outer_ctrl = self.lbow_common + '_Outer_Ctrl'
        cmds.parent(self.lbow_outer_ctrl, self.shoulder_outer_ctrl)

        # HAND CONTROLLER
        self.const_list = [self.hand_clu_handle_name,
                           self.lbow_to_hand_upper_cylinder_cluster_handle_name,
                           self.hand_to_hand_offset_1_lower_cylinder_cluster_handle_name]
        self.rig_helper_class.controller_small_big(base_name=self.hand_common,
                                                   parent_list=self.const_list,
                                                   pos=self.hand_pos,
                                                   ctrl_rotate=self.ctrl_rotate,
                                                   base_ctrl_color=self.base_ctrl_color)
        self.hand_inner_ctrl = self.hand_common + '_Inner_Ctrl'
        self.hand_outer_ctrl = self.hand_common + '_Outer_Ctrl'
        cmds.parent(self.hand_outer_ctrl, self.lbow_outer_ctrl)

        # HAND OFFSET 1 CONTROLLER
        self.const_list = [self.hand_offset_1_clu_handle_name,
                           self.hand_to_hand_offset_1_upper_cylinder_cluster_handle_name,
                           self.hand_offset_1_to_hand_offset_2_lower_cylinder_cluster_handle_name]
        self.rig_helper_class.controller_small_big(base_name=self.hand_offset_1_common,
                                                   parent_list=self.const_list,
                                                   pos=self.hand_offset_1_pos,
                                                   ctrl_rotate=self.ctrl_rotate,
                                                   base_ctrl_color=self.base_ctrl_color)
        self.hand_offset_1_inner_ctrl = self.hand_offset_1_common + '_Inner_Ctrl'
        self.hand_offset_1_outer_ctrl = self.hand_offset_1_common + '_Outer_Ctrl'
        cmds.parent(self.hand_offset_1_outer_ctrl, self.hand_outer_ctrl)

        # HAND OFFSET 2 CONTROLLER
        self.const_list = [self.hand_offset_2_clu_handle_name,
                           self.hand_offset_1_to_hand_offset_2_upper_cylinder_cluster_handle_name,
                           self.hand_offset_2_to_end_lower_cylinder_cluster_handle_name,
                           self.hand_offset_2_to_back_lower_cylinder_cluster_handle_name,
                           self.hand_offset_2_to_hand_side_1_lower_cylinder_cluster_handle_name,
                           self.hand_offset_2_to_hand_side_2_lower_cylinder_cluster_handle_name]

        self.rig_helper_class.controller_small_big(base_name=self.hand_offset_2_common,
                                                   parent_list=self.const_list,
                                                   pos=self.hand_offset_2_pos,
                                                   ctrl_rotate=self.ctrl_rotate,
                                                   base_ctrl_color=self.base_ctrl_color)
        self.hand_offset_2_inner_ctrl = self.hand_offset_2_common + '_Inner_Ctrl'
        self.hand_offset_2_outer_ctrl = self.hand_offset_2_common + '_Outer_Ctrl'
        cmds.parent(self.hand_offset_2_outer_ctrl, self.hand_offset_1_outer_ctrl)

        # HAND END
        self.const_list = [self.end_clu_handle_name,
                           self.hand_offset_2_to_end_upper_cylinder_cluster_handle_name]

        self.rig_helper_class.controller_small_big(base_name=self.end_common,
                                                   parent_list=self.const_list,
                                                   pos=self.end_pos,
                                                   ctrl_rotate=self.ctrl_rotate,
                                                   base_ctrl_color=self.base_ctrl_color)
        self.end_inner_ctrl = self.end_common + '_Inner_Ctrl'
        self.end_outer_ctrl = self.end_common + '_Outer_Ctrl'
        cmds.parent(self.end_outer_ctrl, self.hand_offset_2_outer_ctrl)

        # HAND BACK
        self.const_list = [self.hand_back_clu_handle_name,
                           self.hand_offset_2_to_back_upper_cylinder_cluster_handle_name]

        self.rig_helper_class.controller_small_big(base_name=self.hand_back_common,
                                                   parent_list=self.const_list,
                                                   pos=self.hand_back_pos,
                                                   ctrl_rotate=self.ctrl_rotate,
                                                   base_ctrl_color=self.base_ctrl_color)
        self.back_inner_ctrl = self.hand_back_common + '_Inner_Ctrl'
        self.back_outer_ctrl = self.hand_back_common + '_Outer_Ctrl'
        cmds.parent(self.back_outer_ctrl, self.hand_offset_2_outer_ctrl)

        # HAND SIDE 1 BACK
        self.ctrl_lower_size = [0.2, 0.2, 0.2]
        self.ctrl_outer_size = [1.0, 1.0, 1.0]
        self.const_list = [self.hand_side_1_clu_handle_name,
                           self.hand_offset_2_to_hand_side_1_upper_cylinder_cluster_handle_name]

        self.rig_helper_class.controller_small_big(base_name=self.hand_side_1_common,
                                                   parent_list=self.const_list,
                                                   pos=self.hand_side_1_pos,
                                                   ctrl_rotate=self.ctrl_rotate,
                                                   base_ctrl_color=self.base_ctrl_color)
        self.hand_side_1_inner_ctrl = self.hand_side_1_common + '_Inner_Ctrl'
        self.hand_side_1_outer_ctrl = self.hand_side_1_common + '_Outer_Ctrl'
        cmds.parent(self.hand_side_1_outer_ctrl, self.hand_offset_2_outer_ctrl)

        # HAND SIDE 2 BACK
        self.const_list = [self.hand_side_2_clu_handle_name,
                           self.hand_offset_2_to_hand_side_2_upper_cylinder_cluster_handle_name]

        self.rig_helper_class.controller_small_big(base_name=self.hand_side_2_common,
                                                   parent_list=self.const_list,
                                                   pos=self.hand_side_2_pos,
                                                   ctrl_rotate=self.ctrl_rotate,
                                                   base_ctrl_color=self.base_ctrl_color)
        self.hand_side_2_inner_ctrl = self.hand_side_2_common + '_Inner_Ctrl'
        self.hand_side_2_outer_ctrl = self.hand_side_2_common + '_Outer_Ctrl'
        cmds.parent(self.hand_side_2_outer_ctrl, self.hand_offset_2_outer_ctrl)

        if self.hip == True:
            self.hand_center_inner_ctrl_name = self.hand_center_common + '_Inner_Ctrl'
            if cmds.objExists(self.hand_center_inner_ctrl_name):
                cmds.parentConstraint(self.hand_center_inner_ctrl_name, self.scapula_to_hand_center_upper_cylinder_cluster_handle_name, mo=True)
                cmds.parentConstraint(self.scapula_inner_ctrl,
                                      self.scapula_to_hand_center_lower_cylinder_cluster_handle_name, mo=True)
            else:
                self.const_list = [self.scapula_to_hand_center_upper_cylinder_cluster_handle_name]
                self.rig_helper_class.controller_small_big(base_name=self.hand_center_common,
                                                           parent_list=self.const_list,
                                                           pos=self.hand_center_pos,
                                                           ctrl_rotate=self.ctrl_rotate,
                                                           base_ctrl_color=self.base_ctrl_color)
                self.hand_center_inner_ctrl = self.hand_center_common + '_Inner_Ctrl'
                self.hand_center_outer_ctrl = self.hand_center_common + '_Outer_Ctrl'
                cmds.parentConstraint(self.hand_center_inner_ctrl,self.hand_center_clu_handle_name,mo=True)
                cmds.parentConstraint(self.scapula_inner_ctrl,
                                      self.scapula_to_hand_center_lower_cylinder_cluster_handle_name, mo=True)


            cmds.parentConstraint(self.hand_center_outer_ctrl,
                                  self.scapula_outer_ctrl,mo=True)

























