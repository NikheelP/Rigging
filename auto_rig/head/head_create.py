
import maya.cmds as cmds
import rig_helper
reload(rig_helper)

class HEAD_CREATE:

    def __init__(self):
        self.rig_helper_class = rig_helper.rig_help()

    def head_create(self,type,base_pos,
                    neck_pos,head_pos,
                    head_top_pos,lower_mouth_pos,
                    upper_mouth_pos,left_ear_pos,
                    right_ear_pos,left_eye,left_eye_pos,
                    right_eye,right_eye_pos,prefix_name,
                    base_ctrl_size, base_ctrl_rotate, base_ctrl_color, neck_ctrl_size, neck_ctrl_rotate,
                    neck_ctrl_color,
                    head_ctrl_size, head_ctrl_rotate, head_ctrl_color, lower_mouth_ctrl_size, lower_mouth_ctrl_rotate,
                    lower_mouth_ctrl_color,
                    upper_mouth_ctrl_size, upper_mouth_ctrl_rotate, upper_mouth_ctrl_color,
                    head_top_ctrl_size, head_top_ctrl_rotate, head_top_ctrl_color,
                    left_ear_ctrl_size, left_ear_ctrl_rotate, left_ear_ctrl_color,
                    right_ear_ctrl_size, right_ear_ctrl_rotate, right_ear_ctrl_color):
        self.type = type
        self.base_pos = base_pos
        self.neck_pos = neck_pos
        self.head_pos = head_pos
        self.head_top_pos = head_top_pos
        self.lower_mouth_pos = lower_mouth_pos
        self.upper_mouth_pos = upper_mouth_pos
        self.left_ear_pos = left_ear_pos
        self.right_ear_pos = right_ear_pos
        self.left_eye = left_eye
        self.left_eye_pos = left_eye_pos
        self.right_eye = right_eye
        self.right_eye_pos = right_eye_pos
        self.prefix_name = prefix_name


        self.clu_list = []
        self.sphere_list = []
        self.cylinder_name = []

        # CREATE CONTROLLER
        # BASE
        self.base_ctrl_size = base_ctrl_size
        self.base_ctrl_rotate = base_ctrl_rotate
        self.base_ctrl_color = base_ctrl_color
        self.base_ctrl_freez_trans = True
        self.base_ctrl_freez_rotate = True
        self.base_ctrl_freez_scale = True

        # NECK
        self.neck_ctrl_size = neck_ctrl_size
        self.neck_ctrl_rotate = neck_ctrl_rotate
        self.neck_ctrl_color = neck_ctrl_color
        self.neck_ctrl_freez_trans = True
        self.neck_ctrl_freez_rotate = True
        self.neck_ctrl_freez_scale = True

        # HEAD
        self.head_ctrl_size = head_ctrl_size
        self.head_ctrl_rotate = head_ctrl_rotate
        self.head_ctrl_color = head_ctrl_color
        self.head_ctrl_freez_trans = True
        self.head_ctrl_freez_rotate = True
        self.head_ctrl_freez_scale = True

        # LOWER MOUTH
        self.lower_mouth_ctrl_size = lower_mouth_ctrl_size
        self.lower_mouth_ctrl_rotate = lower_mouth_ctrl_rotate
        self.lower_mouth_ctrl_color = lower_mouth_ctrl_color
        self.lower_mouth_ctrl_freez_trans = True
        self.lower_mouth_ctrl_freez_rotate = True
        self.lower_mouth_ctrl_freez_scale = True

        # UPPER MOUTH
        self.upper_mouth_ctrl_size = upper_mouth_ctrl_size
        self.upper_mouth_ctrl_rotate = upper_mouth_ctrl_rotate
        self.upper_mouth_ctrl_color = upper_mouth_ctrl_color
        self.upper_mouth_ctrl_freez_trans = True
        self.upper_mouth_ctrl_freez_rotate = True
        self.upper_mouth_ctrl_freez_scale = True

        # HEAD TOP
        self.head_top_ctrl_size = head_top_ctrl_size
        self.head_top_ctrl_rotate = head_top_ctrl_rotate
        self.head_top_ctrl_color = head_top_ctrl_size
        self.head_top_ctrl_freez_trans = True
        self.head_top_ctrl_freez_rotate = True
        self.head_top_ctrl_freez_scale = True

        # LEFT EAR
        self.left_ear_ctrl_size = left_ear_ctrl_size
        self.left_ear_ctrl_rotate = left_ear_ctrl_rotate
        self.left_ear_ctrl_color = left_ear_ctrl_color
        self.left_ear_ctrl_freez_trans = True
        self.left_ear_ctrl_freez_rotate = True
        self.left_ear_ctrl_freez_scale = True

        # RIGHT EAR
        self.right_ear_ctrl_size = right_ear_ctrl_size
        self.right_ear_ctrl_rotate = right_ear_ctrl_rotate
        self.right_ear_ctrl_color = right_ear_ctrl_color
        self.right_ear_ctrl_freez_trans = True
        self.right_ear_ctrl_freez_rotate = True
        self.right_ear_ctrl_freez_scale = True

        self.main_group_name = '*_' + self.type + '_Head_Tem_*_Main_Grp'
        if cmds.objExists(self.main_group_name):
            cmds.select(self.main_group_name)
            sel_main_grp = cmds.ls(sl=True)
            self.val = len(sel_main_grp) + 1
        else:
            self.val = 1


        #CREAT A VARIABLE
        self.head_var()

        #CREATE SPHERE
        self.head_sphere()

        #CREATE CYLINDER
        self.head_cylinder()

        #CREATE CTRL
        self.head_ctrl()

        #EYES
        self.eye(self.left_eye_pos, 'Left', 'Blue', int(self.left_eye))
        self.eye(self.right_eye_pos, 'Right', 'Red', int(self.right_eye))

        #FINAL GRP
        self.final_grp()


    def head_var(self):
        self.head_list = {}

        #BASE
        self.base_common_name = self.prefix_name + '_' + self.type + '_Head_Base_Tem_' + str(self.val)
        self.base_sphere_name = self.base_common_name + '_Geo'
        self.base_clu_name = self.base_common_name + '_Clu'
        self.base_clu_handle_name = self.base_clu_name + 'Handle'
        self.base_ctrl_name = self.base_common_name + '_Ctrl'
        self.head_list[self.base_common_name] = [self.base_sphere_name,self.base_pos,self.base_clu_name]

        #NECK
        self.neck_common_name  = self.prefix_name + '_' + self.type + '_Head_Neck_Tem_' + str(self.val)
        self.neck_sphere_name = self.neck_common_name + '_Geo'
        self.neck_clu_name = self.neck_common_name + '_Clu'
        self.neck_clu_handle_name = self.neck_clu_name + 'Handle'
        self.neck_ctrl_name = self.neck_common_name + '_Ctrl'
        self.head_list[self.neck_common_name] = [self.neck_sphere_name, self.neck_pos, self.neck_clu_name]

        #HEAD
        self.head_common_name = self.prefix_name + '_' + self.type + '_Head_Head_Tem_' + str(self.val)
        self.head_sphere_name = self.head_common_name + '_Geo'
        self.head_clu_name = self.head_common_name + '_Clu'
        self.head_clu_handle_name = self.head_clu_name + 'Handle'
        self.head_ctrl_name  = self.head_common_name + '_Ctrl'
        self.head_list[self.head_common_name] = [self.head_sphere_name, self.head_pos, self.head_clu_name]

        #HEAD TOP
        self.head_top_common_name = self.prefix_name + '_' + self.type + '_Head_Head_Top_Tem_' + str(self.val)
        self.head_top_sphere_name = self.head_top_common_name + '_Geo'
        self.head_top_clu_name = self.head_top_common_name + '_Clu'
        self.head_top_clu_handle_name = self.head_top_clu_name + 'Handle'
        self.head_top_ctrl_name  = self.head_top_common_name + '_Ctrl'
        self.head_list[self.head_top_common_name] = [self.head_top_sphere_name, self.head_top_pos, self.head_top_clu_name]

        #LOWER MOUTH
        self.lower_mouth_common_name = self.prefix_name + '_' + self.type + '_Head_Lower_Mouth_Tem_' + str(self.val)
        self.lower_mouth_sphere_name = self.lower_mouth_common_name + '_Geo'
        self.lower_mouth_clu_name = self.lower_mouth_common_name + '_Clu'
        self.lower_mouth_clu_handle_name = self.lower_mouth_clu_name + 'Handle'
        self.lower_mouth_ctrl_name = self.lower_mouth_common_name + '_Ctrl'
        self.head_list[self.lower_mouth_common_name] = [self.lower_mouth_sphere_name, self.lower_mouth_pos, self.lower_mouth_clu_name]

        #UPPER MOUTH
        self.upper_mouth_common_name = self.prefix_name + '_' + self.type + '_Head_Upper_Mouth_Tem_' + str(self.val)
        self.upper_mouth_sphere_name = self.upper_mouth_common_name + '_Geo'
        self.upper_mouth_clu_name = self.upper_mouth_common_name + '_Clu'
        self.upper_mouth_clu_handle_name = self.upper_mouth_clu_name + 'Handle'
        self.upper_mouth_ctrl_name  = self.upper_mouth_common_name + '_Ctrl'
        self.head_list[self.upper_mouth_common_name] = [self.upper_mouth_sphere_name, self.upper_mouth_pos, self.upper_mouth_clu_name]

        #LEFT EAR
        self.left_ear_common_name = self.prefix_name + '_' + self.type + '_Head_Left_Ear_Tem_' + str(self.val)
        self.left_ear_sphere_name = self.left_ear_common_name + '_Geo'
        self.left_ear_clu_name = self.left_ear_common_name + '_Clu'
        self.left_ear_clu_handle_name = self.left_ear_clu_name + 'Handle'
        self.left_ear_ctrl_name = self.left_ear_common_name + '_Ctrl'
        self.head_list[self.left_ear_common_name] = [self.left_ear_sphere_name, self.left_ear_pos, self.left_ear_clu_name]

        #RIGHT EAR
        self.right_ear_common_name = self.prefix_name + '_' + self.type + '_Head_Right_Ear_Tem_' + str(self.val)
        self.right_ear_sphere_name = self.right_ear_common_name + '_Geo'
        self.right_ear_clu_name = self.right_ear_common_name + '_Clu'
        self.right_ear_clu_handle_name = self.right_ear_clu_name + 'Handle'
        self.right_ear_ctrl_name = self.right_ear_common_name + '_Ctrl'
        self.head_list[self.right_ear_common_name] = [self.right_ear_sphere_name, self.right_ear_pos, self.right_ear_clu_name]

        #Grp Variable
        grp_common_name = self.prefix_name + '_' + self.type + '_Head_Tem_' + str(self.val)
        self.clu_grp_name = grp_common_name + '_Clu_Grp'
        self.sphere_grp_name = grp_common_name + '_Sphere_Grp'
        self.cylinder_grp_name = grp_common_name + '_Cylinder_Grp'
        self.ctrl_grp_name = grp_common_name + '_Ctrl_Grp'

    def head_sphere(self):
        #Head SPHERE
        for each in self.head_list:
            self.rig_helper_class.set_sphere_position(name=self.head_list[each][0],
                                                      transform_pos=self.head_list[each][1],
                                                      cluster_name=self.head_list[each][2])
            self.clu_list.append(self.head_list[each][2] + 'Handle')
            self.sphere_list.append(self.head_list[each][0])

            self.rig_helper_class.grp_create(object_name=self.head_list[each][2] + 'Handle',
                                             grp_name=self.clu_grp_name)
            self.rig_helper_class.grp_create(object_name=self.head_list[each][0],
                                             grp_name=self.sphere_grp_name)
        cmds.setAttr((self.clu_grp_name + '.v'),0)

    def head_cylinder(self):
        clu_list = []
        cylinder_list = []

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

        self.rig_helper_class.set_cylinder_position(self.base_to_neck_cylinder_name,
                                                    self.base_to_neck_lower_cylinder_cluster_name,
                                                    self.base_to_neck_upper_cylinder_cluster_name,
                                                    self.neck_sphere_name,
                                                    self.base_sphere_name)
        clu_list.append(self.base_to_neck_lower_cylinder_cluster_handle_name)
        clu_list.append(self.base_to_neck_upper_cylinder_cluster_handle_name)
        cylinder_list.append(self.base_to_neck_cylinder_name)


        # NECK TO FACE CYLINDER
        self.neck_to_face_cylinder_name = self.prefix_name + '_' + self.type + '_Head_Neck_to_Face_Tem_' + str(
            self.val) + '_Geo'
        self.neck_to_face_lower_cylinder_cluster_name = self.prefix_name + '_' + self.type + '_Head_Neck_to_Face_Lower_Tem_' + str(
            self.val) + '_Clu'
        self.neck_to_face_lower_cylinder_cluster_handle_name = self.neck_to_face_lower_cylinder_cluster_name + 'Handle'
        self.neck_to_face_upper_cylinder_cluster_name = self.prefix_name + '_' + self.type + '_Head_Neck_to_Face_Upper_Tem_' + str(
            self.val) + '_Clu'
        self.neck_to_face_upper_cylinder_cluster_handle_name = self.neck_to_face_upper_cylinder_cluster_name + 'Handle'
        self.rig_helper_class.set_cylinder_position(self.neck_to_face_cylinder_name,
                                                self.neck_to_face_lower_cylinder_cluster_name,
                                                self.neck_to_face_upper_cylinder_cluster_name,
                                                self.neck_sphere_name,
                                                self.head_sphere_name)
        clu_list.append(self.neck_to_face_lower_cylinder_cluster_handle_name)
        clu_list.append(self.neck_to_face_upper_cylinder_cluster_handle_name)
        cylinder_list.append(self.neck_to_face_cylinder_name)

        # FACE TO LOWER MOUTH CYLINDER
        self.face_to_lower_mouth_cylinder_name = self.prefix_name + '_' + self.type + '_Head_Face_to_Lower_Mouth_Tem_' + str(
            self.val) + '_Geo'
        self.face_to_lower_mouth_lower_cylinder_cluster_name = self.prefix_name + '_' + self.type + '_Head_Face_to_Lower_Mouth_Lower_Tem_' + str(
            self.val) + '_Clu'
        self.face_to_lower_mouth_lower_cylinder_cluster_handle_name = self.face_to_lower_mouth_lower_cylinder_cluster_name + 'Handle'
        self.face_to_lower_mouth_upper_cylinder_cluster_name = self.prefix_name + '_' + self.type + '_Head_Face_to_Lower_Mouth_Upper_Tem_' + str(
            self.val) + '_Clu'
        self.face_to_lower_mouth_upper_cylinder_cluster_handle_name = self.face_to_lower_mouth_upper_cylinder_cluster_name + 'Handle'
        self.rig_helper_class.set_cylinder_position(self.face_to_lower_mouth_cylinder_name,
                                                self.face_to_lower_mouth_lower_cylinder_cluster_name,
                                                self.face_to_lower_mouth_upper_cylinder_cluster_name,
                                                self.lower_mouth_sphere_name,
                                                self.head_sphere_name)
        clu_list.append(self.face_to_lower_mouth_lower_cylinder_cluster_handle_name)
        clu_list.append(self.face_to_lower_mouth_upper_cylinder_cluster_handle_name)
        cylinder_list.append(self.face_to_lower_mouth_cylinder_name)


        # FACE TO UPPER MOUTH CYLINDER
        self.face_to_upper_mouth_cylinder_name = self.prefix_name + '_' + self.type + '_Head_Face_to_Upper_Mouth_Tem_' + str(
            self.val) + '_Geo'
        self.face_to_upper_mouth_lower_cylinder_cluster_name = self.prefix_name + '_' + self.type + '_Head_Face_to_Upper_Mouth_Lower_Tem_' + str(
            self.val) + '_Clu'
        self.face_to_upper_mouth_lower_cylinder_cluster_handle_name = self.face_to_upper_mouth_lower_cylinder_cluster_name + 'Handle'
        self.face_to_upper_mouth_upper_cylinder_cluster_name = self.prefix_name + '_' + self.type + '_Head_Face_to_Upper_Mouth_Upper_Tem_' + str(
            self.val) + '_Clu'
        self.face_to_upper_mouth_upper_cylinder_cluster_handle_name = self.face_to_upper_mouth_upper_cylinder_cluster_name + 'Handle'
        self.rig_helper_class.set_cylinder_position(self.face_to_upper_mouth_cylinder_name,
                                                self.face_to_upper_mouth_lower_cylinder_cluster_name,
                                                self.face_to_upper_mouth_upper_cylinder_cluster_name,
                                                self.upper_mouth_sphere_name,
                                                self.head_sphere_name)
        clu_list.append(self.face_to_upper_mouth_lower_cylinder_cluster_handle_name)
        clu_list.append(self.face_to_upper_mouth_upper_cylinder_cluster_handle_name)
        cylinder_list.append(self.face_to_upper_mouth_cylinder_name)

        # FACE TO HEAD TOP CYLINDER
        self.face_to_head_top_cylinder_name = self.prefix_name + '_' + self.type + '_Head_Face_to_Head_Top_Tem_' + str(
            self.val) + '_Geo'
        self.face_to_head_top_lower_cylinder_cluster_name = self.prefix_name + '_' + self.type + '_Head_Face_to_Head_Top_Lower_Tem_' + str(
            self.val) + '_Clu'
        self.face_to_head_top_lower_cylinder_cluster_handle_name = self.face_to_head_top_lower_cylinder_cluster_name + 'Handle'
        self.face_to_head_top_upper_cylinder_cluster_name = self.prefix_name + '_' + self.type + '_Head_Face_to_Head_Top_Upper_Tem_' + str(
            self.val) + '_Clu'
        self.face_to_head_top_upper_cylinder_cluster_handle_name = self.face_to_head_top_upper_cylinder_cluster_name + 'Handle'
        self.rig_helper_class.set_cylinder_position(self.face_to_head_top_cylinder_name,
                                                self.face_to_head_top_lower_cylinder_cluster_name,
                                                self.face_to_head_top_upper_cylinder_cluster_name,
                                                self.head_sphere_name,
                                                self.head_top_sphere_name)
        clu_list.append(self.face_to_head_top_lower_cylinder_cluster_handle_name)
        clu_list.append(self.face_to_head_top_upper_cylinder_cluster_handle_name)
        cylinder_list.append(self.face_to_head_top_cylinder_name)

        # FACE TO LEFT EAR CYLINDER
        self.face_to_left_ear_cylinder_name = self.prefix_name + '_' + self.type + '_Head_Face_to_Left_Ear_Tem_' + str(
            self.val) + '_Geo'
        self.face_to_left_ear_lower_cylinder_cluster_name = self.prefix_name + '_' + self.type + '_Head_Face_to_Left_Ear_Lower_Tem_' + str(
            self.val) + '_Clu'
        self.face_to_left_ear_lower_cylinder_cluster_handle_name = self.face_to_left_ear_lower_cylinder_cluster_name + 'Handle'
        self.face_to_left_ear_upper_cylinder_cluster_name = self.prefix_name + '_' + self.type + '_Head_Face_to_Left_Ear_Upper_Tem_' + str(
            self.val) + '_Clu'
        self.face_to_left_ear_upper_cylinder_cluster_handle_name = self.face_to_left_ear_upper_cylinder_cluster_name + 'Handle'
        self.rig_helper_class.set_cylinder_position(self.face_to_left_ear_cylinder_name,
                                                self.face_to_left_ear_lower_cylinder_cluster_name,
                                                self.face_to_left_ear_upper_cylinder_cluster_name,
                                                self.head_sphere_name,
                                                self.left_ear_sphere_name)
        clu_list.append(self.face_to_left_ear_lower_cylinder_cluster_handle_name)
        clu_list.append(self.face_to_left_ear_upper_cylinder_cluster_handle_name)
        cylinder_list.append(self.face_to_left_ear_cylinder_name)

        # FACE TO RIGHT EAR CYLINDER
        self.face_to_right_ear_cylinder_name = self.prefix_name + '_' + self.type + '_Head_Face_to_Right_Ear_Tem_' + str(
            self.val) + '_Geo'
        self.face_to_right_ear_lower_cylinder_cluster_name = self.prefix_name + '_' + self.type + '_Head_Face_to_Right_Ear_Lower_Tem_' + str(
            self.val) + '_Clu'
        self.face_to_right_ear_lower_cylinder_cluster_handle_name = self.face_to_right_ear_lower_cylinder_cluster_name + 'Handle'
        self.face_to_right_ear_upper_cylinder_cluster_name = self.prefix_name + '_' + self.type + '_Head_Face_to_Right_Ear_Upper_Tem_' + str(
            self.val) + '_Clu'
        self.face_to_right_ear_upper_cylinder_cluster_handle_name = self.face_to_right_ear_upper_cylinder_cluster_name + 'Handle'
        self.rig_helper_class.set_cylinder_position(self.face_to_right_ear_cylinder_name,
                                                self.face_to_right_ear_lower_cylinder_cluster_name,
                                                self.face_to_right_ear_upper_cylinder_cluster_name,
                                                self.head_sphere_name,
                                                self.right_ear_sphere_name)
        clu_list.append(self.face_to_right_ear_lower_cylinder_cluster_handle_name)
        clu_list.append(self.face_to_right_ear_upper_cylinder_cluster_handle_name)
        cylinder_list.append(self.face_to_right_ear_cylinder_name)

        for each in clu_list:
            self.rig_helper_class.grp_create(object_name=each,
                                             grp_name=self.clu_grp_name)
        for each in cylinder_list:
            self.rig_helper_class.grp_create(object_name=each,
                                             grp_name=self.cylinder_grp_name)

    def head_ctrl(self):
        #BASE
        self.base_ctrl_size_ctrl = self.base_ctrl_size
        self.base_ctrl_roate = self.base_ctrl_rotate
        self.base_parent_const_list = [self.base_clu_handle_name,
                                       self.base_to_neck_lower_cylinder_cluster_handle_name]
        self.rig_helper_class.set_controller(self.base_ctrl_name, self.base_pos, self.base_ctrl_size_ctrl,
                                         self.base_ctrl_roate, self.base_parent_const_list, self.base_parent_const_list,
                                         color=self.base_ctrl_color,
                                         freez_trans=self.base_ctrl_freez_trans,
                                         freez_rotate=self.base_ctrl_freez_rotate,
                                         freez_scale=self.base_ctrl_freez_scale)

        # NECK CONTROLLER
        self.neck_ctrl_size_ctrl = self.neck_ctrl_size
        self.neck_ctrl_roate = self.neck_ctrl_rotate
        self.neck_parent_const_list = [self.neck_clu_handle_name,
                                       self.base_to_neck_upper_cylinder_cluster_handle_name,
                                       self.neck_to_face_lower_cylinder_cluster_handle_name]
        self.rig_helper_class.set_controller(self.neck_ctrl_name, self.neck_pos, self.neck_ctrl_size_ctrl,
                                         self.neck_ctrl_roate, self.neck_parent_const_list, self.neck_parent_const_list,
                                         color=self.neck_ctrl_color,
                                         freez_trans=self.neck_ctrl_freez_trans,
                                         freez_rotate=self.neck_ctrl_freez_rotate,
                                         freez_scale=self.neck_ctrl_freez_scale)

        # HEAD CONTROLLER
        self.head_ctrl_size_ctrl = self.head_ctrl_size
        self.head_ctrl_roate = self.head_ctrl_rotate
        self.head_parent_const_list = [self.face_to_right_ear_lower_cylinder_cluster_handle_name,
                                       self.face_to_head_top_lower_cylinder_cluster_handle_name,
                                       self.face_to_left_ear_lower_cylinder_cluster_handle_name,
                                       self.head_clu_handle_name,
                                       self.neck_to_face_upper_cylinder_cluster_handle_name,
                                       self.face_to_lower_mouth_upper_cylinder_cluster_handle_name,
                                       self.face_to_upper_mouth_upper_cylinder_cluster_handle_name]
        self.rig_helper_class.set_controller(self.head_ctrl_name, self.head_pos, self.head_ctrl_size_ctrl,
                                         self.head_ctrl_roate, self.head_parent_const_list, self.head_parent_const_list,
                                         color=self.head_ctrl_color,
                                         freez_trans=self.head_ctrl_freez_trans,
                                         freez_rotate=self.head_ctrl_freez_rotate,
                                         freez_scale=self.head_ctrl_freez_scale)

        # HEAD TOP
        self.head_top_ctrl_size_ctrl = self.head_top_ctrl_size
        self.head_top_ctrl_roate = self.head_top_ctrl_rotate
        self.head_top_parent_const_list = [self.face_to_head_top_upper_cylinder_cluster_handle_name,
                                           self.head_top_clu_handle_name]
        self.rig_helper_class.set_controller(self.head_top_ctrl_name, self.head_top_pos, self.head_top_ctrl_size_ctrl,
                                         self.head_top_ctrl_roate, self.head_top_parent_const_list,
                                         self.head_top_parent_const_list,
                                         color=self.head_top_ctrl_color,
                                         freez_trans=self.head_top_ctrl_freez_trans,
                                         freez_rotate=self.head_top_ctrl_freez_rotate,
                                         freez_scale=self.head_top_ctrl_freez_scale)

        # LOWER MOUTH
        self.lower_mouth_ctrl_size_ctrl = self.lower_mouth_ctrl_size
        self.lower_mouth_ctrl_roate = self.lower_mouth_ctrl_rotate
        self.lower_mouth_parent_const_list = [self.face_to_lower_mouth_lower_cylinder_cluster_handle_name,
                                              self.lower_mouth_clu_handle_name]
        self.rig_helper_class.set_controller(self.lower_mouth_ctrl_name, self.lower_mouth_pos,
                                         self.lower_mouth_ctrl_size_ctrl,
                                         self.lower_mouth_ctrl_roate, self.lower_mouth_parent_const_list,
                                         self.lower_mouth_parent_const_list,
                                         color=self.lower_mouth_ctrl_color,
                                         freez_trans=self.lower_mouth_ctrl_freez_trans,
                                         freez_rotate=self.lower_mouth_ctrl_freez_rotate,
                                         freez_scale=self.lower_mouth_ctrl_freez_scale)

        # UPPER MOUTH
        self.upper_mouth_ctrl_size_ctrl = self.upper_mouth_ctrl_size
        self.upper_mouth_ctrl_roate = self.upper_mouth_ctrl_rotate
        self.upper_mouth_parent_const_list = [self.face_to_upper_mouth_lower_cylinder_cluster_handle_name,
                                              self.upper_mouth_clu_handle_name]
        self.rig_helper_class.set_controller(self.upper_mouth_ctrl_name, self.upper_mouth_pos,
                                         self.upper_mouth_ctrl_size_ctrl,
                                         self.upper_mouth_ctrl_roate, self.upper_mouth_parent_const_list,
                                         self.upper_mouth_parent_const_list,
                                         color=self.upper_mouth_ctrl_color,
                                         freez_trans=self.upper_mouth_ctrl_freez_trans,
                                         freez_rotate=self.upper_mouth_ctrl_freez_rotate,
                                         freez_scale=self.upper_mouth_ctrl_freez_scale)

        # LEFT EAR
        self.left_ear_ctrl_size_ctrl = self.left_ear_ctrl_size
        self.left_ear_ctrl_roate = self.left_ear_ctrl_rotate
        self.left_ear_parent_const_list = [self.face_to_left_ear_upper_cylinder_cluster_handle_name,
                                           self.left_ear_clu_handle_name]
        self.rig_helper_class.set_controller(self.left_ear_ctrl_name, self.left_ear_pos, self.left_ear_ctrl_size_ctrl,
                                         self.left_ear_ctrl_roate, self.left_ear_parent_const_list,
                                         self.left_ear_parent_const_list,
                                         color=self.left_ear_ctrl_color,
                                         freez_trans=self.left_ear_ctrl_freez_trans,
                                         freez_rotate=self.left_ear_ctrl_freez_rotate,
                                         freez_scale=self.left_ear_ctrl_freez_scale)

        # RIGHT EAR
        self.right_ear_ctrl_size_ctrl = self.right_ear_ctrl_size
        self.right_ear_ctrl_roate = self.right_ear_ctrl_rotate
        self.right_ear_parent_const_list = [self.face_to_right_ear_upper_cylinder_cluster_handle_name,
                                            self.right_ear_clu_handle_name]
        self.rig_helper_class.set_controller(self.right_ear_ctrl_name, self.right_ear_pos, self.right_ear_ctrl_size_ctrl,
                                         self.right_ear_ctrl_roate, self.right_ear_parent_const_list,
                                         self.right_ear_parent_const_list,
                                         color=self.right_ear_ctrl_color,
                                         freez_trans=self.right_ear_ctrl_freez_trans,
                                         freez_rotate=self.right_ear_ctrl_freez_rotate,
                                         freez_scale=self.right_ear_ctrl_freez_scale)

        #PARENT THE CONTROLLER
        cmds.parent(self.neck_ctrl_name,self.base_ctrl_name)
        cmds.parent(self.head_ctrl_name,self.neck_ctrl_name)
        cmds.parent(self.lower_mouth_ctrl_name,self.upper_mouth_ctrl_name,
                    self.left_ear_ctrl_name,self.right_ear_ctrl_name,
                    self.head_top_ctrl_name,self.head_ctrl_name)

        self.rig_helper_class.grp_create(object_name=self.base_ctrl_name,
                                         grp_name=self.ctrl_grp_name)

    def eye(self,eye_position, eye_side, ctrl_color, eye_query):
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
            self.rig_helper_class.set_sphere_position(self.eye_sphere_name, self.new_value, self.eye_sphere_clu_name)

            self.eye_ctrl_name = self.prefix_name + '_' + self.type + '_Head_' + self.eye_side + '_Eye_' + str(
                a + 1) + '_Tem_' + str(self.val) + '_Ctrl'
            eye_ctrl_grp_name = self.eye_ctrl_name + '_Grp'

            self.eye_ctrl_size_ctrl = [0.5, 0.5, 0.5]
            self.eye_ctrl_roate = [0, 0, 0]
            self.eye_parent_const_list = [self.eye_sphere_clu_handle_name]
            self.rig_helper_class.set_controller(self.eye_ctrl_name, self.new_value, self.eye_ctrl_size_ctrl,
                                             self.eye_ctrl_roate, self.eye_parent_const_list,
                                             self.eye_parent_const_list,
                                             color=self.ctrl_color)
            cmds.select(self.eye_ctrl_name)
            cmds.group(n=eye_ctrl_grp_name)

            self.rig_helper_class.grp_create(object_name=self.eye_sphere_name,
                                             grp_name=self.sphere_grp_name)
            self.rig_helper_class.grp_create(object_name=self.eye_sphere_clu_handle_name,
                                             grp_name=self.clu_grp_name)
            self.rig_helper_class.grp_create(object_name=eye_ctrl_grp_name,
                                             grp_name=self.ctrl_grp_name)


            #parent const to the object
            cmds.parentConstraint(self.head_ctrl_name,eye_ctrl_grp_name,mo=True)
            cmds.scaleConstraint(self.head_ctrl_name, eye_ctrl_grp_name, mo=True)
            add_value += 2
            a += 1

    def final_grp(self):
        list = [self.clu_grp_name,self.ctrl_grp_name,self.sphere_grp_name,self.cylinder_grp_name]
        main_group_name = self.prefix_name + '_' + self.type + '_Head_Tem_' + str(self.val) + '_Main_Grp'
        for each in list:
            self.rig_helper_class.grp_create(object_name=each,
                                             grp_name=main_group_name)

        head_grp_name  = 'Head_Grp'
        self.rig_helper_class.grp_create(object_name=main_group_name,
                                         grp_name=head_grp_name)

