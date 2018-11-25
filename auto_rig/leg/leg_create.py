
import maya.cmds as cmds
import rig_helper,human_leg,animal_front_leg
reload(rig_helper)
reload(human_leg)
reload(animal_front_leg)

class LEG_CREATE:

    def __init__(self):
        self.rig_helper_class = rig_helper.rig_help()
        self.human_leg_class = human_leg.HUMAN_LEG()
        self.animal_front_leg_class = animal_front_leg.FRONT_LEG()

    def leg_create(self,mirror,left_leg,right_leg,hip,butt,
                   thine_to_knee,knee_to_foot,foot,no_finger,
                   base_color,pos_list,hip_pos,prefix_name,side,base_ctrl_color,finger_list,
                   type,leg_finger):
        self.mirror = mirror
        self.left_leg = left_leg
        self.right_leg = right_leg
        self.hip = hip
        self.type = type
        self.thine_to_knee = int(thine_to_knee)
        self.knee_to_foot = int(knee_to_foot)
        self.foot = foot
        self.no_finger = int(no_finger)
        self.base_color = base_color
        self.prefix_name = prefix_name
        self.side = side
        self.base_ctrl_color = base_ctrl_color
        self.finger_list = finger_list
        self.hip_pos = hip_pos
        self.leg_finger = leg_finger

        if self.type == 'Human':
            self.human_leg_class.new(mirror =mirror,
                                     left_leg=left_leg,
                                     right_leg=right_leg,
                                     hip=hip,
                                     thine_to_knee=thine_to_knee,
                                     knee_to_foot=knee_to_foot,
                                     foot=foot,
                                     no_finger=no_finger,
                                     prefix_name=prefix_name,
                                     finger_list=finger_list,
                                     hip_pos=hip_pos,
                                     pos_list=pos_list,
                                     butt = butt,
                                     side=self.side,
                                     base_ctrl_color = self.base_ctrl_color,
                                     leg_finger = self.leg_finger)

        if self.type == 'Animal_Front_Leg':
            self.animal_front_leg_class.new(mirror=mirror,
                                            left_leg=left_leg,
                                            right_leg=right_leg,
                                            hip=hip,
                                            thine_to_knee=thine_to_knee,
                                            knee_to_foot=knee_to_foot,
                                            foot=foot,
                                            no_finger=no_finger,
                                            prefix_name=prefix_name,
                                            finger_list=finger_list,
                                            pos_list=pos_list,
                                            butt=butt,
                                            side=self.side,
                                            base_ctrl_color=self.base_ctrl_color,
                                            leg_finger=self.leg_finger)


        if self.type == 'Animal_Back_Leg':
            self.thine_pos = pos_list['thine_pos']
            self.shine_pos = pos_list['shine_pos']
            self.foot_pos = pos_list['foot_pos']
            self.foot_offset_1_pos = pos_list['foot_offset_1']
            self.foot_offset_2_pos = pos_list['foot_offset_2']
            self.foot_offset_3_pos = pos_list['foot_offset_3']
            self.foot_end_pos = pos_list['foot_end']
            self.foot_back_pos = pos_list['foot_back']
            self.foot_side_1_pos = pos_list['foot_side_1']
            self.foot_side_2_pos = pos_list['foot_side_2']






    def leg_var(self):
        self.sphere_list = []
        self.cluster_list = []
        self.cylinder_list = []
        self.ctrl_list = []
        self.crv_list = []

        #GRP NAME
        #self.clu_grp_name, self.ctrl_grp_name, self.sphere_grp_name, self.cylinder_grp_name,self.crv_grp_name
        grp_common_name = self.prefix_name + '_' + self.side + '_Leg_Tem_' + str(self.val)
        self.clu_grp_name = grp_common_name + '_Clu_Grp'
        self.sphere_grp_name = grp_common_name + '_Sphere_Grp'
        self.cylinder_grp_name = grp_common_name + '_Cylinder_Grp'
        self.ctrl_grp_name = grp_common_name + '_Ctrl_Grp'
        self.crv_grp_name = grp_common_name + '_Crv_Grp'


        # THINE
        self.thine_common = self.prefix_name + "_" + self.side + "_Leg_Thine_Tem_" + str(self.val)
        self.thine_sphere_name = self.thine_common + "_Geo"
        self.thine_sphere_clu_name = self.thine_common + '_Clu'
        self.thine_sphere_clu_handle_name = self.thine_sphere_clu_name + 'Handle'
        self.sphere_list.append(self.thine_sphere_name)
        self.cluster_list.append(self.thine_sphere_clu_name)

        # SHINE
        self.shine_common = self.prefix_name + "_" + self.side + "_Leg_Shine_Tem_" + str(self.val)
        self.shine_sphere_name = self.shine_common + "_Geo"
        self.shine_sphere_clu_name = self.shine_common + '_Clu'
        self.shine_sphere_clu_handle_name = self.shine_sphere_clu_name + 'Handle'
        self.sphere_list.append(self.shine_sphere_name)
        self.cluster_list.append(self.shine_sphere_clu_name)

        # FOOT
        self.foot_common = self.prefix_name + "_" + self.side + "_Leg_Foot_Tem_" + str(self.val)
        self.foot_sphere_name = self.foot_common + "_Geo"
        self.foot_sphere_clu_name = self.foot_common + '_Clu'
        self.foot_sphere_clu_handle_name = self.foot_sphere_clu_name + 'Handle'
        self.sphere_list.append(self.foot_sphere_name)
        self.cluster_list.append(self.foot_sphere_clu_name)

        # BALL
        self.ball_common = self.prefix_name + "_" + self.side + "_Leg_Ball_Tem_" + str(self.val)
        self.ball_sphere_name = self.ball_common + "_Geo"
        self.ball_sphere_clu_name = self.ball_common + '_Clu'
        self.ball_sphere_clu_handle_name = self.ball_sphere_clu_name + 'Handle'
        self.sphere_list.append(self.ball_sphere_name)
        self.cluster_list.append(self.ball_sphere_clu_name)

        # END
        self.end_common = self.prefix_name + "_" + self.side + "_Leg_End_Tem_" + str(self.val)
        self.end_sphere_name = self.end_common + "_Geo"
        self.end_sphere_clu_name = self.end_common + '_Clu'
        self.end_sphere_clu_handle_name = self.end_sphere_clu_name + 'Handle'
        self.sphere_list.append(self.end_sphere_name)
        self.cluster_list.append(self.end_sphere_clu_name)

    def leg_sphere(self):
        a = 0
        for each in self.sphere_list:
            self.rig_helper_class.set_sphere_position(name=each,
                                                      transform_pos=self.pos_list[a],
                                                      cluster_name=self.cluster_list[a])
            a += 1

    def leg_cylinder(self):
        # THINE TO SHINE
        self.thine_to_shine_common = self.prefix_name + "_" + self.side + "_Leg_Thine_to_Shine_Tem_" + str(self.val)
        self.thine_to_shine_cylinder_name = self.thine_to_shine_common + '_Geo'
        self.thine_to_shine_lower_cylinder_cluster_name = self.prefix_name + "_" + self.side + "_Leg_Thine_to_Shine_Lower_Tem_" + str(
            self.val) + '_Clu'
        self.thine_to_shine_lower_cylinder_cluster_handle_name = self.thine_to_shine_lower_cylinder_cluster_name + 'Handle'
        self.thine_to_shine_upper_cylinder_cluster_name = self.prefix_name + "_" + self.side + "_Leg_Thine_to_Shine_Upper_Tem_" + str(
            self.val) + '_Clu'
        self.thine_to_shine_upper_cylinder_cluster_handle_name = self.thine_to_shine_upper_cylinder_cluster_name + 'Handle'
        self.cylinder_rotate = [0, 0, 0]
        self.cluster_list.append(self.thine_to_shine_lower_cylinder_cluster_handle_name)
        self.cluster_list.append(self.thine_to_shine_upper_cylinder_cluster_handle_name)
        self.cylinder_list.append(self.thine_to_shine_cylinder_name)
        self.rig_helper_class.set_cylinder_position(self.thine_to_shine_cylinder_name,
                                                self.thine_to_shine_lower_cylinder_cluster_name,
                                                self.thine_to_shine_upper_cylinder_cluster_name,
                                                self.shine_sphere_name,
                                                self.thine_sphere_name,
                                                rotate_val=[self.cylinder_rotate[0],
                                                            self.cylinder_rotate[1],
                                                            self.cylinder_rotate[2]])

        # SHINE TO FOOT
        self.shine_to_foot_common = self.prefix_name + "_" + self.side + "_Leg_Shine_to_Foot_Tem_" + str(self.val)
        self.shine_to_foot_cylinder_name = self.shine_to_foot_common + '_Geo'
        self.shine_to_foot_lower_cylinder_cluster_name = self.prefix_name + "_" + self.side + "_Leg_Shine_to_Foot_Lower_Tem_" + str(
            self.val) + '_Clu'
        self.shine_to_foot_lower_cylinder_cluster_handle_name = self.shine_to_foot_lower_cylinder_cluster_name + 'Handle'
        self.shine_to_foot_upper_cylinder_cluster_name = self.prefix_name + "_" + self.side + "_Leg_Shine_to_Foot_Upper_Tem_" + str(
            self.val) + '_Clu'
        self.shine_to_foot_upper_cylinder_cluster_handle_name = self.shine_to_foot_upper_cylinder_cluster_name + 'Handle'
        self.cylinder_rotate = [0, 0, 0]
        self.cluster_list.append(self.shine_to_foot_lower_cylinder_cluster_handle_name)
        self.cluster_list.append(self.shine_to_foot_upper_cylinder_cluster_handle_name)
        self.cylinder_list.append(self.shine_to_foot_cylinder_name)
        self.rig_helper_class.set_cylinder_position(self.shine_to_foot_cylinder_name,
                                                self.shine_to_foot_lower_cylinder_cluster_name,
                                                self.shine_to_foot_upper_cylinder_cluster_name,
                                                self.foot_sphere_name,
                                                self.shine_sphere_name,
                                                rotate_val=[self.cylinder_rotate[0],
                                                            self.cylinder_rotate[1],
                                                            self.cylinder_rotate[2]])

        # FOOT TO BALL
        self.foot_to_ball_common = self.prefix_name + "_" + self.side + "_Leg_Foot_to_Ball_Tem_" + str(self.val)
        self.foot_to_ball_cylinder_name = self.foot_to_ball_common + '_Geo'
        self.foot_to_ball_lower_cylinder_cluster_name = self.prefix_name + "_" + self.side + "_Leg_Foot_to_Ball_Lower_Tem_" + str(
            self.val) + '_Clu'
        self.foot_to_ball_lower_cylinder_cluster_handle_name = self.foot_to_ball_lower_cylinder_cluster_name + 'Handle'
        self.foot_to_ball_upper_cylinder_cluster_name = self.prefix_name + "_" + self.side + "_Leg_Foot_to_Ball_Upper_Tem_" + str(
            self.val) + '_Clu'
        self.foot_to_ball_upper_cylinder_cluster_handle_name = self.foot_to_ball_upper_cylinder_cluster_name + 'Handle'
        self.cylinder_rotate = [90, 0, 0]
        self.cluster_list.append(self.foot_to_ball_lower_cylinder_cluster_handle_name)
        self.cluster_list.append(self.foot_to_ball_upper_cylinder_cluster_handle_name)
        self.cylinder_list.append(self.foot_to_ball_cylinder_name)
        self.rig_helper_class.set_cylinder_position(self.foot_to_ball_cylinder_name,
                                                self.foot_to_ball_lower_cylinder_cluster_name,
                                                self.foot_to_ball_upper_cylinder_cluster_name,
                                                self.foot_sphere_name,
                                                self.ball_sphere_name,
                                                rotate_val=[self.cylinder_rotate[0],
                                                            self.cylinder_rotate[1],
                                                            self.cylinder_rotate[2]])

        # BALL TO END
        self.ball_to_end_common = self.prefix_name + "_" + self.side + "_Leg_Ball_to_End_Tem_" + str(self.val)
        self.ball_to_end_cylinder_name = self.ball_to_end_common + '_Geo'
        self.ball_to_end_lower_cylinder_cluster_name = self.prefix_name + "_" + self.side + "_Leg_Ball_to_End_Lower_Tem_" + str(
            self.val) + '_Clu'
        self.ball_to_end_lower_cylinder_cluster_handle_name = self.ball_to_end_lower_cylinder_cluster_name + 'Handle'
        self.ball_to_end_upper_cylinder_cluster_name = self.prefix_name + "_" + self.side + "_Leg_Ball_to_End_Upper_Tem_" + str(
            self.val) + '_Clu'
        self.ball_to_end_upper_cylinder_cluster_handle_name = self.ball_to_end_upper_cylinder_cluster_name + 'Handle'
        self.cylinder_rotate = [90, 0, 0]
        self.cluster_list.append(self.ball_to_end_lower_cylinder_cluster_handle_name)
        self.cluster_list.append(self.ball_to_end_upper_cylinder_cluster_handle_name)
        self.cylinder_list.append(self.ball_to_end_cylinder_name)
        self.rig_helper_class.set_cylinder_position(self.ball_to_end_cylinder_name,
                                                self.ball_to_end_lower_cylinder_cluster_name,
                                                self.ball_to_end_upper_cylinder_cluster_name,
                                                self.ball_sphere_name,
                                                self.end_sphere_name,
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

        # THINE CONTROLLER
        self.thine_const_list = [self.thine_sphere_clu_handle_name,
                                 self.thine_to_shine_upper_cylinder_cluster_handle_name]
        self.controller_small_big(base_name=self.thine_common,
                                  parent_list=self.thine_const_list,
                                  pos=self.thine_pos,
                                  ctrl_rotate=self.ctrl_rotate)
        self.thine_inner_ctrl = self.thine_common + '_Inner_Ctrl'
        self.thine_outer_ctrl = self.thine_common + '_Outer_Ctrl'
        self.ctrl_list.append(self.thine_outer_ctrl)

        # SHINE CONTROLLER
        self.shine_const_list = [self.shine_sphere_clu_handle_name,
                                 self.thine_to_shine_lower_cylinder_cluster_handle_name,
                                 self.shine_to_foot_upper_cylinder_cluster_handle_name]
        self.controller_small_big(base_name=self.shine_common,
                                  parent_list=self.shine_const_list,
                                  pos=self.shine_pos,
                                  ctrl_rotate=self.ctrl_rotate)
        self.shine_inner_ctrl = self.shine_common + '_Inner_Ctrl'
        self.shine_outer_ctrl = self.shine_common + '_Outer_Ctrl'
        cmds.select(self.shine_outer_ctrl,
                    self.thine_outer_ctrl)
        cmds.parent()

        # FOOT CONTROLLER
        self.foot_const_list = [self.foot_sphere_clu_handle_name,
                                self.shine_to_foot_lower_cylinder_cluster_handle_name,
                                self.foot_to_ball_lower_cylinder_cluster_handle_name]
        self.controller_small_big(base_name=self.foot_common,
                                  parent_list=self.foot_const_list,
                                  pos=self.foot_pos,
                                  ctrl_rotate=self.ctrl_rotate)
        self.foot_inner_ctrl = self.foot_common + '_Inner_Ctrl'
        self.foot_outer_ctrl = self.foot_common + '_Outer_Ctrl'
        cmds.select(self.foot_outer_ctrl,
                    self.shine_outer_ctrl)
        cmds.parent()

        # BALL CONTROLLER
        self.ctrl_rotate = [90, 0, 0]
        self.ball_const_list = [self.ball_sphere_clu_handle_name,
                                self.foot_to_ball_upper_cylinder_cluster_handle_name,
                                self.ball_to_end_lower_cylinder_cluster_handle_name]
        self.controller_small_big(base_name=self.ball_common,
                                  parent_list=self.ball_const_list,
                                  pos=self.ball_pos,
                                  ctrl_rotate=self.ctrl_rotate)
        self.ball_inner_ctrl = self.ball_common + '_Inner_Ctrl'
        self.ball_outer_ctrl = self.ball_common + '_Outer_Ctrl'
        cmds.select(self.ball_outer_ctrl,
                    self.foot_outer_ctrl)
        cmds.parent()

        # END CONTROLLER
        self.end_const_list = [self.end_sphere_clu_handle_name,
                               self.ball_to_end_upper_cylinder_cluster_handle_name]
        self.controller_small_big(base_name=self.end_common,
                                  parent_list=self.end_const_list,
                                  pos=self.end_pos,
                                  ctrl_rotate=self.ctrl_rotate)
        self.end_inner_ctrl = self.end_common + '_Inner_Ctrl'
        self.end_outer_ctrl = self.end_common + '_Outer_Ctrl'
        cmds.select(self.end_outer_ctrl,
                    self.ball_outer_ctrl)
        cmds.parent()

        # roll bone
        self.roll_bone('Upper',
                       self.thine_inner_ctrl,
                       self.shine_inner_ctrl,
                       self.thine_to_knee)
        self.roll_bone('Lower',
                       self.shine_inner_ctrl,
                       self.foot_inner_ctrl,
                       self.knee_to_foot)

    def controller_small_big(self, base_name, parent_list, pos, ctrl_rotate):
        self.ctrl_lower_size = [0.5, 0.5, 0.5]
        self.ctrl_outer_size = [0.8, 0.8, 0.8]
        self.base_ctrl_freez_trans = True
        self.base_ctrl_freez_rotate = True
        self.base_ctrl_freez_scale = True

        # SMALL CONTROLLER
        self.base_inner_ctrl = base_name + '_Inner_Ctrl'
        self.base_ctrl_size_ctrl = self.ctrl_lower_size
        self.base_ctrl_roate = ctrl_rotate
        self.base_parent_const_list = parent_list
        self.rig_helper_class.set_controller(self.base_inner_ctrl, pos, self.base_ctrl_size_ctrl,
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
        self.rig_helper_class.set_controller(self.base_outer_ctrl, pos, self.base_ctrl_size_ctrl,
                                         self.base_ctrl_roate, self.base_parent_const_list, self.base_parent_const_list,
                                         color=self.base_ctrl_color,
                                         freez_trans=self.base_ctrl_freez_trans,
                                         freez_rotate=self.base_ctrl_freez_rotate,
                                         freez_scale=self.base_ctrl_freez_scale)
        cmds.select(self.base_inner_ctrl, self.base_outer_ctrl)
        cmds.parent()

    def roll_bone(self, type, upper_object, lower_object, no_of_bone):
        # create a curve
        self.curve_common = self.prefix_name + "_" + self.side + "_Leg_" + type + "_Tem_" + str(self.val)
        self.curve_name = self.curve_common + '_Crv'
        self.curve_shape_name = self.curve_name + 'Shape'
        self.curve_0_clu_name = self.prefix_name + "_" + self.side + "_Leg_" + type + "_0_Tem_" + str(
            self.val) + '_Clu'
        self.curve_0_clu_handle_name = self.curve_0_clu_name + 'Handle'
        self.curve_1_clu_name = self.prefix_name + "_" + self.side + "_Leg_" + type + "_1_Tem_" + str(
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
        self.cluster_list.append(self.curve_0_clu_handle_name)
        self.cluster_list.append(self.curve_1_clu_handle_name)

        # create a point on curve
        a = 0
        toal_minus = 0
        value = 1.0 - toal_minus
        average_val = value / (no_of_bone + 1.0)
        start_val = average_val

        while a < no_of_bone:
            common_name = self.prefix_name + "_" + self.side + "_Leg_" + type + "_" + str(a) + "_Tem_" + str(
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

            cmds.setAttr((self.poc_name + '.parameter'), start_val)
            start_val += average_val

            # setAttr "Template_L_Arm_Lower_0_Tem_1_POC.parameter" 0.2;

            a += 1

    def finger_def(self):
        self.finger_ctrl_list = []
        a = 0
        self.locator_list = []
        x_val = 0
        while a < self.no_finger:
            locator_name = 'Finger_' + str(a) + '_Loc'
            self.locator_list.append(locator_name)
            cmds.spaceLocator(n=locator_name, p=(x_val, 0, 0))
            cmds.select(locator_name)
            cmds.CenterPivot()
            x_val += 3
            a += 1
        self.locator_grp_name = 'Finger_Grp'
        cmds.select('Finger_*_Loc')
        cmds.group(n=self.locator_grp_name)
        cmds.select(self.locator_grp_name)
        cmds.CenterPivot()
        cmds.move(0, 0, 0, rpr=True)
        cmds.FreezeTransformations()
        cmds.move(self.finger_default_pos[0],
                  self.finger_default_pos[1],
                  self.finger_default_pos[2])
        if self.side == 'R':
            cmds.setAttr((self.locator_grp_name + '.rz'), 180)
        # now get each positiona dn create a finger

        a = 0
        while a < self.no_finger:
            new_loc = 'New_Loc_' + str(a)
            cmds.spaceLocator(n=new_loc, p=(0, 0, 0))
            cmds.parentConstraint(self.locator_list[a], new_loc, mo=False)
            self.loc_position = cmds.getAttr(new_loc + '.t')[0]
            cmds.select(new_loc)
            cmds.delete()

            self.finger_query = int(self.finger_list[a])
            b = 0
            x_value = self.loc_position[2]
            while b < self.finger_query:
                self.cylinder_rotate = [90, 0, 0]
                self.finger_common = self.prefix_name + "_" + self.side + "_Leg_Finger_" + str(a + 1) + '_' + str(
                    b + 1) + "_Tem_" + str(self.val)
                self.finger_sphere_name = self.finger_common + "_Geo"
                self.finger_sphere_clu_name = self.finger_common + '_Clu'
                self.finger_sphere_clu_handle_name = self.finger_sphere_clu_name + 'Handle'
                # self.finger_default_pos = [61.0,0,]

                self.finger_pos = [self.loc_position[0], 0, x_value]
                self.sphere_list.append(self.finger_sphere_name)
                self.cluster_list.append(self.finger_sphere_clu_handle_name)
                self.rig_helper_class.set_sphere_position(self.finger_sphere_name,
                                                      self.finger_pos,
                                                      self.finger_sphere_clu_name)
                if b == 0:
                    self.cylinder_name = self.prefix_name + '_' + self.side + "_Leg_Finger_Leg_to_" + str(
                        a + 1) + "_" + str(b + 1) + "_Tem_" + str(self.val) + "_Cylinder_Geo"
                    self.cylinder_upper_cluster_name = self.prefix_name + '_' + self.side + "_Leg_Finger_Leg_to_Upper_" + str(
                        a + 1) + "_" + str(b + 1) + "_Tem_" + str(self.val) + "_Clu"
                    self.finger_to_hand_cylinder_upper_cluster_handle_name = self.cylinder_upper_cluster_name + 'Handle'
                    self.cylinder_lower_cluster_name = self.prefix_name + '_' + self.side + "_Leg_Finger_Leg_to_Lower_" + str(
                        a + 1) + "_" + str(b + 1) + "_Tem_" + str(self.val) + "_Clu"
                    self.cylinder_lower_cluster_handle_name = self.cylinder_lower_cluster_name + 'Handle'
                    self.rig_helper_class.set_cylinder_position(self.cylinder_name,
                                                            self.cylinder_lower_cluster_name,
                                                            self.cylinder_upper_cluster_name,
                                                            self.ball_sphere_name,
                                                            self.finger_sphere_name,
                                                            rotate_val=self.cylinder_rotate)
                    self.cluster_list.append(self.finger_to_hand_cylinder_upper_cluster_handle_name)
                    self.cluster_list.append(self.cylinder_lower_cluster_handle_name)
                    self.cylinder_list.append(self.cylinder_name)

                    self.base_parent_const_list = [self.finger_sphere_clu_handle_name,
                                                   self.finger_to_hand_cylinder_upper_cluster_handle_name]
                    cmds.parentConstraint(self.ball_outer_ctrl, self.cylinder_lower_cluster_handle_name, mo=False)
                    ctrl_rotate = (90, 0, 0)
                    self.controller_small_big(base_name=self.finger_common,
                                              parent_list=self.base_parent_const_list,
                                              pos=self.finger_pos,
                                              ctrl_rotate=ctrl_rotate)
                    self.leg_shoulder_inner_ctrl = self.finger_common + '_Inner_Ctrl'
                    self.leg_shoulder_outer_ctrl = self.finger_common + '_Outer_Ctrl'

                if b + 1 != 1:
                    self.cylinder_name = self.prefix_name + '_' + self.side + "_Leg_Finger_" + str(
                        a + 1) + "_" + str(b + 1) + "_Tem_" + str(self.val) + "_Cylinder_Geo"
                    self.cylinder_upper_cluster_name = self.prefix_name + '_' + self.side + "_Leg_Finger_Upper_" + str(
                        a + 1) + "_" + str(b + 1) + "_Tem_" + str(self.val) + "_Clu"
                    self.cylinder_upper_cluster_handle_name = self.cylinder_upper_cluster_name + 'Handle'
                    self.cylinder_lower_cluster_name = self.prefix_name + '_' + self.side + "_Leg_Finger_Lower_" + str(
                        a + 1) + "_" + str(b + 1) + "_Tem_" + str(self.val) + "_Clu"
                    self.cylinder_lower_cluster_handle_name = self.cylinder_lower_cluster_name + 'Handle'
                    self.current_sphere_name = self.prefix_name + '_' + self.side + "_Leg_Finger_" + str(
                        a + 1) + "_" + str(b) + "_Tem_" + str(self.val) + "_Geo"
                    self.rig_helper_class.set_cylinder_position(self.cylinder_name,
                                                            self.cylinder_lower_cluster_name,
                                                            self.cylinder_upper_cluster_name,
                                                            self.current_sphere_name,
                                                            self.finger_sphere_name,
                                                            rotate_val=self.cylinder_rotate)
                    self.cluster_list.append(self.cylinder_upper_cluster_handle_name)
                    self.cluster_list.append(self.cylinder_lower_cluster_handle_name)
                    self.cylinder_list.append(self.cylinder_name)

                    # create a controller and snap
                    previous_upper_cluster_handle_name = self.prefix_name + "_" + self.side + "_Leg_Finger_Upper_" + str(
                        a + 1) + '_' + str(b + 1) + "_Tem_" + str(self.val) + '_CluHandle'
                    next_lower_cluster_handle_name = self.prefix_name + "_" + self.side + "_Leg_Finger_Lower_" + str(
                        a + 1) + '_' + str(b + 1) + "_Tem_" + str(self.val) + '_CluHandle'
                    self.base_parent_const_list = [self.finger_sphere_clu_handle_name,
                                                   previous_upper_cluster_handle_name]
                    ctrl_rotate = (90, 0, 0)
                    self.controller_small_big(base_name=self.finger_common,
                                              parent_list=self.base_parent_const_list,
                                              pos=self.finger_pos,
                                              ctrl_rotate=ctrl_rotate)
                    self.leg_shoulder_inner_ctrl = self.finger_common + '_Inner_Ctrl'
                    self.leg_shoulder_outer_ctrl = self.finger_common + '_Outer_Ctrl'
                x_value += 3
                b += 1
            a += 1

        a = 0
        while a < self.no_finger:
            b = 0
            while b < self.finger_query:

                # Template_L_Leg_Finger_Lower_1_2_Tem_1_CluHandle
                common_ctrl_name = self.prefix_name + "_" + self.side + "_Leg_Finger_" + str(a + 1) + '_' + str(
                    b + 1) + "_Tem_" + str(self.val)
                common_lower_cluster_handle_name = self.prefix_name + "_" + self.side + "_Leg_Finger_Lower_" + str(
                    a + 1) + '_' + str(b + 2) + "_Tem_" + str(self.val)

                inner_ctrl_name = common_ctrl_name + '_Inner_Ctrl'
                outer_ctrl_name = common_ctrl_name + '_Outer_Ctrl'
                lower_cluster_handle = common_lower_cluster_handle_name + '_CluHandle'
                if cmds.objExists(lower_cluster_handle):
                    cmds.parentConstraint(inner_ctrl_name, lower_cluster_handle, mo=False)
                next_common = self.prefix_name + "_" + self.side + "_Leg_Finger_" + str(a + 1) + '_' + str(
                    b + 2) + "_Tem_" + str(self.val)
                if b == 0:
                    cmds.select(outer_ctrl_name, self.ball_outer_ctrl)
                    cmds.parent()

                next_outer_ctrl = next_common + '_Outer_Ctrl'
                if cmds.objExists(next_outer_ctrl):
                    cmds.select(next_outer_ctrl, outer_ctrl_name)
                    cmds.parent()

                b += 1
            a += 1
        cmds.select(self.locator_grp_name)
        cmds.delete()

    def hip_def(self):
        # create a sphere
        self.hip_common = self.prefix_name + "_Leg_Hip_Tem_" + str(self.val)
        self.hip_sphere_name = self.hip_common + "_Geo"
        self.ctrl_rotate = [0, 0, 0]
        if cmds.objExists(self.hip_sphere_name):
            pass
        else:
            self.hip_sphere_clu_name = self.hip_common + '_Clu'
            self.hip_sphere_clu_handle_name = self.hip_sphere_clu_name + 'Handle'
            self.sphere_list.append(self.hip_sphere_name)
            self.cluster_list.append(self.hip_sphere_clu_handle_name)
            self.rig_helper_class.set_sphere_position(self.hip_sphere_name,
                                                  self.hip_pos,
                                                  self.hip_sphere_clu_name)

        # create a cylinder
        self.thine_to_hip_common = self.prefix_name + "_" + self.side + "_Leg_Thine_to_Hip_Tem_" + str(self.val)
        self.thine_to_hip_cylinder_name = self.thine_to_hip_common + '_Geo'
        self.thine_to_hip_lower_cylinder_cluster_name = self.prefix_name + "_" + self.side + "_Leg_Thine_to_Hip_Lower_Tem_" + str(
            self.val) + '_Clu'
        self.thine_to_hip_lower_cylinder_cluster_handle_name = self.thine_to_hip_lower_cylinder_cluster_name + 'Handle'
        self.thine_to_hip_upper_cylinder_cluster_name = self.prefix_name + "_" + self.side + "_Leg_Thine_to_Hip_Upper_Tem_" + str(
            self.val) + '_Clu'
        self.thine_to_hip_upper_cylinder_cluster_handle_name = self.thine_to_hip_upper_cylinder_cluster_name + 'Handle'
        self.cylinder_rotate = [0, 0, 0]
        self.cluster_list.append(self.thine_to_hip_lower_cylinder_cluster_handle_name)
        self.cluster_list.append(self.thine_to_hip_upper_cylinder_cluster_handle_name)
        self.cylinder_list.append(self.thine_to_hip_cylinder_name)
        self.rig_helper_class.set_cylinder_position(self.thine_to_hip_cylinder_name,
                                                self.thine_to_hip_lower_cylinder_cluster_name,
                                                self.thine_to_hip_upper_cylinder_cluster_name,
                                                self.hip_sphere_name,
                                                self.thine_sphere_name,
                                                rotate_val=[self.cylinder_rotate[0],
                                                            self.cylinder_rotate[1],
                                                            self.cylinder_rotate[2]])
        # do parent const
        cmds.parentConstraint(self.thine_inner_ctrl, self.thine_to_hip_upper_cylinder_cluster_handle_name, mo=False)

        if self.mirror_check_box_query == True:
            self.side = 'L'
            # create a cylinder
            self.left_thine_to_hip_common = self.prefix_name + "_" + self.side + "_Leg_Thine_to_Hip_Tem_" + str(
                self.val)
            self.thine_to_hip_cylinder_name = self.left_thine_to_hip_common + '_Geo'
            self.thine_to_hip_lower_cylinder_cluster_name = self.prefix_name + "_" + self.side + "_Leg_Thine_to_Hip_Lower_Tem_" + str(
                self.val) + '_Clu'
            self.left_thine_to_hip_lower_cylinder_cluster_handle_name = self.thine_to_hip_lower_cylinder_cluster_name + 'Handle'
            self.thine_to_hip_upper_cylinder_cluster_name = self.prefix_name + "_" + self.side + "_Leg_Thine_to_Hip_Upper_Tem_" + str(
                self.val) + '_Clu'
            self.thine_to_hip_upper_cylinder_cluster_handle_name = self.thine_to_hip_upper_cylinder_cluster_name + 'Handle'
            self.hip_common = self.prefix_name + "_Leg_Hip_Tem_" + str(self.val)
            self.hip_sphere_name = self.hip_common + "_Geo"
            self.thine_common = self.prefix_name + "_" + self.side + "_Leg_Thine_Tem_" + str(self.val)
            self.thine_sphere_name = self.thine_common + "_Geo"
            self.cylinder_rotate = [0, 0, 0]
            self.cluster_list.append(self.left_thine_to_hip_lower_cylinder_cluster_handle_name)
            self.cluster_list.append(self.thine_to_hip_upper_cylinder_cluster_handle_name)
            self.cylinder_list.append(self.thine_to_hip_cylinder_name)
            self.rig_helper_class.set_cylinder_position(self.thine_to_hip_cylinder_name,
                                                    self.thine_to_hip_lower_cylinder_cluster_name,
                                                    self.thine_to_hip_upper_cylinder_cluster_name,
                                                    self.hip_sphere_name,
                                                    self.thine_sphere_name,
                                                    rotate_val=[self.cylinder_rotate[0],
                                                                self.cylinder_rotate[1],
                                                                self.cylinder_rotate[2]])
            # Template_R_Leg_Thine_Tem_1_Inner_Ctrl
            self.left_thinner_inner_ctrl = self.prefix_name + "_" + self.side + "_Leg_Thine_Tem_" + str(
                self.val) + '_Inner_Ctrl'
            cmds.parentConstraint(self.left_thinner_inner_ctrl, self.thine_to_hip_upper_cylinder_cluster_handle_name,
                                  mo=False)

            # create a controller
            # THINE CONTROLLER
            new_color = self.base_ctrl_color
            self.base_ctrl_color = 'Yellow'
            self.hip_const_list = [self.hip_sphere_clu_handle_name,
                                   self.left_thine_to_hip_lower_cylinder_cluster_handle_name,
                                   self.thine_to_hip_lower_cylinder_cluster_handle_name]
            self.controller_small_big(base_name=self.hip_common,
                                      parent_list=self.hip_const_list,
                                      pos=self.hip_pos,
                                      ctrl_rotate=self.ctrl_rotate)
            self.hip_inner_ctrl = self.hip_common + '_Inner_Ctrl'
            self.hip_outer_ctrl = self.hip_common + '_Outer_Ctrl'

            self.base_ctrl_color = new_color
            # parent the both thine ctrl

    def butt_def(self):
        # create a sphere
        self.butt_common = self.prefix_name + "_" + self.side + "_Leg_Butt_Tem_" + str(self.val)
        self.butt_sphere_name = self.butt_common + "_Geo"
        self.butt_sphere_clu_name = self.butt_common + '_Clu'
        self.butt_sphere_clu_handle_name = self.butt_sphere_clu_name + 'Handle'
        self.sphere_list.append(self.butt_sphere_name)
        self.cluster_list.append(self.butt_sphere_clu_handle_name)
        self.rig_helper_class.set_sphere_position(self.butt_sphere_name,
                                              self.butt_pos,
                                              self.butt_sphere_clu_name)

        # cylinder
        self.thine_to_butt_common = self.prefix_name + "_" + self.side + "_Leg_Thine_to_Butt_Tem_" + str(self.val)
        self.thine_to_butt_cylinder_name = self.thine_to_butt_common + '_Geo'
        self.thine_to_butt_lower_cylinder_cluster_name = self.prefix_name + "_" + self.side + "_Leg_Thine_to_Butt_Lower_Tem_" + str(
            self.val) + '_Clu'
        self.thine_to_butt_lower_cylinder_cluster_handle_name = self.thine_to_butt_lower_cylinder_cluster_name + 'Handle'
        self.thine_to_butt_upper_cylinder_cluster_name = self.prefix_name + "_" + self.side + "_Leg_Thine_to_Butt_Upper_Tem_" + str(
            self.val) + '_Clu'
        self.thine_to_butt_upper_cylinder_cluster_handle_name = self.thine_to_butt_upper_cylinder_cluster_name + 'Handle'
        self.cylinder_rotate = [90, 0, 0]
        self.cluster_list.append(self.thine_to_butt_lower_cylinder_cluster_handle_name)
        self.cluster_list.append(self.thine_to_butt_upper_cylinder_cluster_handle_name)
        self.cylinder_list.append(self.thine_to_butt_cylinder_name)
        self.rig_helper_class.set_cylinder_position(self.thine_to_butt_cylinder_name,
                                                self.thine_to_butt_lower_cylinder_cluster_name,
                                                self.thine_to_butt_upper_cylinder_cluster_name,
                                                self.butt_sphere_name,
                                                self.thine_sphere_name,
                                                rotate_val=[self.cylinder_rotate[0],
                                                            self.cylinder_rotate[1],
                                                            self.cylinder_rotate[2]])

        self.ctrl_rotate = [90, 0, 0]
        self.butt_const_list = [self.butt_sphere_clu_handle_name,
                                self.thine_to_butt_lower_cylinder_cluster_handle_name]
        self.controller_small_big(base_name=self.butt_common,
                                  parent_list=self.butt_const_list,
                                  pos=self.butt_pos,
                                  ctrl_rotate=self.ctrl_rotate)
        self.butt_inner_ctrl = self.butt_common + '_Inner_Ctrl'
        self.butt_outer_ctrl = self.butt_common + '_Outer_Ctrl'
        cmds.select(self.butt_outer_ctrl,
                    self.thine_outer_ctrl)
        cmds.parent()
        parent_list = [self.thine_to_butt_upper_cylinder_cluster_handle_name]
        self.rig_helper_class.parent_constraint(self.thine_outer_ctrl, parent_list)












