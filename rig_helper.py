'''
This is the helo file for rigging to Create Few Repeat command
'''
import maya.cmds as cmds
import maya.mel as mel
from PySide import QtCore
from PySide import QtGui
import maya_nodes
reload(maya_nodes)

class rig_help:
    def __init__(self):
        self.maya_node_class = maya_nodes.MAYA_NODE()


    def pivot_move(self,obj_name,pos):
        cmds.setAttr((obj_name + '.rotatePivotX'), pos[0])
        cmds.setAttr((obj_name + '.rotatePivotY'), pos[1])
        cmds.setAttr((obj_name + '.rotatePivotZ'), pos[2])
        cmds.setAttr((obj_name + '.scalePivotX'), pos[0])
        cmds.setAttr((obj_name + '.scalePivotY'), pos[1])
        cmds.setAttr((obj_name + '.scalePivotZ'), pos[2])

    def clearLayout(self,layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def lock_ui_attr(self,attr_list):
        for each in attr_list:
            each.setDisabled(True)

    def unlock_ui_attr(self,attr_list):
        for each in attr_list:
            each.setDisabled(False)

    def set_sphere_position(self,name,transform_pos,cluster_name):
        cmds.polySphere(r=1, sx=6, sy=6, ax=(0, 1, 0), cuv=2, ch=1, n=name)
        cmds.move(transform_pos[0],
                  transform_pos[1],
                  transform_pos[2])
        cmds.select(name)
        cmds.cluster(n=cluster_name)
        cmds.setAttr((name + '.overrideEnabled'),1)
        cmds.setAttr((name + '.overrideDisplayType'),2)
        #lock and hide everything
        self.transform_rotation_scale_visible(name)

    def transform_rotation_scale_visible(self,object_name,t=True,r=True,s=True,v=True):
        if t == True:
            self.transform_lock_hide(object_name)
        if r == True:
            self.rotate_lock_hide(object_name)
        if s == True:
            self.scale_lock_hide(object_name)
        if v == True:
            self.lock_hide(object_name,'v')

    def lock_hide(self,object_name,object_attr,lock=True,keyable=False):
        cmds.setAttr((object_name + '.' + object_attr ),lock=lock,keyable=keyable)

    def transform_lock_hide(self,object_name,lock=True,keyable=False):
        t = ['tx','ty','tz']
        for each in t:
            self.lock_hide(object_name,each,lock=lock,keyable=keyable)

    def scale_lock_hide(self,object_name,lock=True,keyable=False):
        s = ['sx','sy','sz']
        for each in s:
            self.lock_hide(object_name,each,lock=lock,keyable=keyable)

    def rotate_lock_hide(self,object_name,lock=True,keyable=False):
        r = ['rx','ry','rz']
        for each in r:
            self.lock_hide(object_name,each,lock=lock,keyable=keyable)

    def grp_create(self,object_name,grp_name):
        if cmds.objExists(grp_name):
            cmds.select(object_name,grp_name)
            cmds.parent()
        else:
            cmds.select(object_name)
            cmds.group(n=grp_name)

    def set_cylinder_position(self,cylinder_name,
                              cluster_1,
                              cluster_2,
                              cluster_1_parent,
                              cluster_2_parent,
                              rotate_val = [0,0,0]):
        cmds.polyCylinder(r=0.5, h=2, sx=20, sy=1, sz=1, ax=(0, 1, 0), rcp=0, cuv=3, ch=1, n=cylinder_name)
        cmds.setAttr((cylinder_name + '.rx'),rotate_val[0])
        cmds.setAttr((cylinder_name + '.ry'),rotate_val[1])
        cmds.setAttr((cylinder_name + '.rz'),rotate_val[2])
        # select all neck to face cylinder lower vtx
        cmds.select((cylinder_name + ".vtx[0:19]"), (cylinder_name + ".vtx[40]"))
        cluster_1_handle_name = cluster_1 + "Handle"
        cmds.cluster(n=cluster_1)
        # move to the face
        cmds.parentConstraint(cluster_1_parent, cluster_1_handle_name, mo=False)
        cmds.delete(cluster_1_handle_name + "_parentConstraint1")

        # select all neck to face cylinder upper vtx
        cmds.select((cylinder_name + ".vtx[20:39]"), (cylinder_name + ".vtx[41]"))
        cluster_2_handle_name = cluster_2 + "Handle"
        cmds.cluster(n=cluster_2)
        # move to the face
        cmds.parentConstraint(cluster_2_parent, cluster_2_handle_name, mo=False)
        cmds.delete(cluster_2_handle_name + "_parentConstraint1")

        self.make_refrence(cylinder_name)

        #lock and hide the transform object
        self.transform_rotation_scale_visible(cylinder_name)

    def make_refrence(self,obj_name):
        cmds.setAttr((obj_name + '.overrideEnabled'), 1)
        cmds.setAttr((obj_name + '.overrideDisplayType'), 2)



    def set_controller(self,name,transform_pos,
                       size,rotation,
                       parent_const_child_list,
                       scale_const_child_list,
                       color,
                       freez_trans = True,
                       freez_rotate = True,
                       freez_scale = True):
        cmds.circle(c=(0, 0, 0), nr=(0, 1, 0), sw=360, r=4, d=3, ut=0, tol=0.01, s=8, ch=1, n=name)
        cmds.select(name)
        cmds.move(transform_pos[0],
                  transform_pos[1],
                  transform_pos[2])
        cmds.rotate(rotation[0],
                    rotation[1],
                    rotation[2])
        cmds.scale(size[0],
                   size[1],
                   size[2])
        cmds.select(name)
        cmds.DeleteHistory()
        if freez_trans == True:
            mel.eval('channelBoxCommand -freezeTranslate;')
        if freez_rotate == True:
            mel.eval('channelBoxCommand -freezeRotate;')
        if freez_scale == True:
            mel.eval('channelBoxCommand -freezeScale;')

        self.parent_constraint(name,parent_const_child_list,mo=True)
        self.scale_constraint(name,scale_const_child_list,mo=True)
        self.color_val(color,name)

    def parent_constraint(self,parent,child_list,mo=False):

        for each_obj in child_list:
            cmds.parentConstraint(parent, each_obj, mo=mo)

    def scale_constraint(self,parent,child_list,mo=False):
        for each_obj in child_list:
            cmds.scaleConstraint(parent, each_obj, mo=mo)

    def color_val(self,color,obj_name):
        shapeNodes = cmds.listRelatives(obj_name, shapes=True)
        if color == 'Red':
            for shape in shapeNodes:
                cmds.setAttr("{0}.overrideEnabled".format(shape), True)
                cmds.setAttr("{0}.overrideColor".format(shape), 1)
        elif color == 'Blue':
            for shape in shapeNodes:
                cmds.setAttr("{0}.overrideEnabled".format(shape), True)
                cmds.setAttr("{0}.overrideColor".format(shape), 6)
        elif color == 'Yellow':
            for shape in shapeNodes:
                cmds.setAttr("{0}.overrideEnabled".format(shape), True)
                cmds.setAttr("{0}.overrideColor".format(shape), 22)

    def mirror_def(self,mirror,left,right):
        if mirror.isChecked():
            left.setChecked(True)
            right.setChecked(True)
        else:
            left.setChecked(False)
            right.setChecked(False)

    def test_def(self):
        print('this is the test def')

    def sphere_create(self,sphere_list,pos_list,cluster_list):
        a=0
        for each in sphere_list:
            self.set_sphere_position(name=each,
                                     transform_pos=pos_list[a],
                                     cluster_name=cluster_list[a])
            a+=1

    def final_grp(self,type,list_grp,list,prefix_name,side,val,character_type):
        list_grp = list_grp
        list = list
        self.prefix_name = prefix_name
        self.side = side
        self.val = val
        self.character_type = character_type
        #'*_' + self.side + '_' + self.type + '_Leg_Tem_*_Main_Grp')
        main_group_name = self.prefix_name + '_' + self.side + '_' +  self.character_type+  '_' + type + '_Tem_' + str(self.val) + '_Main_Grp'

        a = 0
        while a < len(list):
            for each in list[a]:
                if cmds.objectType(each) == 'cluster':
                    name = each + 'Handle'
                    cmds.setAttr((name + '.v'),0)
                else:
                    name = each
                self.grp_create(object_name=name,
                                grp_name=list_grp[a])

            self.grp_create(object_name=list_grp[a],
                            grp_name=main_group_name)

            a+=1

        grp_name  = type + '_Grp'
        self.grp_create(object_name=main_group_name,
                                         grp_name=grp_name)

    def parent_child_grp(self,parent,child,vis=False,trans_rot_scale= True):
        if cmds.objExists(parent):
            parent_obj = cmds.listRelatives(child,p=True)
            if parent_obj == None:
                cmds.select(child,parent)
                cmds.parent()
        else:
            cmds.select(child)
            cmds.group(n=parent)
            if vis == True:
                cmds.setAttr((parent + '.v'),0)
            if trans_rot_scale== True:
                self.transform_rotation_scale_visible(parent,v=False)


    def mirror_grp(self,left_ctrl,right_ctrl,rotation=True):
        #create each group
        cmds.select(left_ctrl)
        left_mirror_group_name = left_ctrl + '_' + right_ctrl + '_to_left_Mirror_Grp'
        cmds.group(n=left_mirror_group_name)
        self.point_position = cmds.xform(left_ctrl,q=1,ws=1,rp=1)
        cmds.setAttr((left_mirror_group_name + '.rotatePivotX'),self.point_position[0])
        cmds.setAttr((left_mirror_group_name + '.rotatePivotY'),self.point_position[1])
        cmds.setAttr((left_mirror_group_name + '.rotatePivotZ'),self.point_position[2])
        cmds.setAttr((left_mirror_group_name + '.scalePivotX'),self.point_position[0])
        cmds.setAttr((left_mirror_group_name + '.scalePivotY'),self.point_position[1])
        cmds.setAttr((left_mirror_group_name + '.scalePivotZ'),self.point_position[2])



        cmds.select(right_ctrl)
        right_mirror_group_name = left_ctrl + '_' + right_ctrl + '_to_right_Mirror_Grp'
        cmds.group(n=right_mirror_group_name)
        self.point_position = cmds.xform(right_ctrl,q=1,ws=1,rp=1)
        cmds.setAttr((right_mirror_group_name + '.rotatePivotX'),self.point_position[0])
        cmds.setAttr((right_mirror_group_name + '.rotatePivotY'),self.point_position[1])
        cmds.setAttr((right_mirror_group_name + '.rotatePivotZ'),self.point_position[2])
        cmds.setAttr((right_mirror_group_name + '.scalePivotX'),self.point_position[0])
        cmds.setAttr((right_mirror_group_name + '.scalePivotY'),self.point_position[1])
        cmds.setAttr((right_mirror_group_name + '.scalePivotZ'),self.point_position[2])

        #create a translate ,rotate scale mirror
        #connectAttr -f Template_R_Arm_Upper_Hand_Tem_1_Outer_Ctrl.translateX Template_R_Arm_Double_lBow_Side_1_Tem_1_Outer_Ctrl.translateX;
        cmds.connectAttr((left_ctrl + '.ty'),(right_mirror_group_name + '.ty'),f=True)
        cmds.connectAttr((left_ctrl + '.tz'),(right_mirror_group_name + '.tz'),f=True)
        cmds.connectAttr((left_ctrl + '.rx'),(right_mirror_group_name + '.rx'),f=True)

        cmds.connectAttr((left_ctrl + '.sx'), (right_mirror_group_name + '.sx'), f=True)
        cmds.connectAttr((left_ctrl + '.sy'), (right_mirror_group_name + '.sy'), f=True)
        cmds.connectAttr((left_ctrl + '.sz'), (right_mirror_group_name + '.sz'), f=True)

        #reverse tx
        self.reverse_axis(left_ctrl=left_ctrl,
                          right_ctrl=right_ctrl,
                          axis='tx',
                          left_mirror_group_name=left_mirror_group_name,
                          right_mirror_group_name=right_mirror_group_name)

        if rotation == True:

            #reverse rx
            self.reverse_axis(left_ctrl=left_ctrl,
                              right_ctrl=right_ctrl,
                              axis='rz',
                              left_mirror_group_name=left_mirror_group_name,
                              right_mirror_group_name=right_mirror_group_name)
            #reverse ry
            self.reverse_axis(left_ctrl=left_ctrl,
                              right_ctrl=right_ctrl,
                              axis='ry',
                              left_mirror_group_name=left_mirror_group_name,
                              right_mirror_group_name=right_mirror_group_name)


    def reverse_axis(self,left_ctrl,right_ctrl,axis,
                     left_mirror_group_name,
                     right_mirror_group_name):
        #create a reverse
        reverse_node_name = left_ctrl + '_' + right_ctrl + '_' + axis + '_Reverse'

        #plusminus
        plus_minus_name = left_ctrl + '_' + right_ctrl + '_' + axis + '_Plus_Minus'
        cmds.createNode('plusMinusAverage',n=plus_minus_name)
        sel_plus_minus = cmds.ls(sl=True)[0]
        cmds.rename(sel_plus_minus,plus_minus_name)
        mel.eval('AEnewNonNumericMultiAddNewItem("%s","input3D");' % plus_minus_name)
        #setAttr "plusMinusAverage4.operation" 2;
        cmds.setAttr((plus_minus_name + '.operation'),2)

        self.maya_node_class.reverse(name=reverse_node_name,
                                input_ctrl=left_ctrl,
                                input_value=axis,
                                output_ctrl=plus_minus_name,
                                output_value='input3D[0].input3Dx')
        #etAttr "plusMinusAverage4.input3D[1].input3Dx" 1;
        cmds.setAttr((plus_minus_name + '.input3D[1].input3Dx'),1)
        cmds.connectAttr((plus_minus_name + '.output3Dx'),
                         (right_mirror_group_name + '.' + axis),
                         f=True)

        '''
        #REVERSE
        #create a reverse
        reverse_node_name = right_ctrl + '_' + left_ctrl + '_' + axis + '_Reverse'

        #plusminus
        plus_minus_name = right_ctrl + '_' + left_ctrl + '_' + axis + '_Plus_Minus'
        cmds.createNode('plusMinusAverage',n=plus_minus_name)
        sel_plus_minus = cmds.ls(sl=True)[0]
        cmds.rename(sel_plus_minus,plus_minus_name)
        mel.eval('AEnewNonNumericMultiAddNewItem("%s","input3D");' % plus_minus_name)
        #setAttr "plusMinusAverage4.operation" 2;
        cmds.setAttr((plus_minus_name + '.operation'),2)

        self.maya_node_class.reverse(name=reverse_node_name,
                                input_ctrl=right_ctrl,
                                input_value=axis,
                                output_ctrl=plus_minus_name,
                                output_value='input3D[0].input3Dx')
        #etAttr "plusMinusAverage4.input3D[1].input3Dx" 1;
        cmds.setAttr((plus_minus_name + '.input3D[1].input3Dx'),1)
        #connectAttr -f plusMinusAverage4.output3Dx Template_Human_Head_Left_Ear_Tem_1_Ctrl_right_to_left_Mirror_Grp.translateX;
        cmds.connectAttr((plus_minus_name + '.output3Dx'),
                         (left_mirror_group_name + '.' + axis),
                         f=True)
        '''

    def mirror_value(self,ctrl_list,side):
        for each in ctrl_list:
            right_ctrl = each
            if side == 'L':
                old_val = 'L'
                new_val = 'R'
            elif side == 'R':
                old_val = 'R'
                new_val = 'L'
            left_ctrl = each.replace(old_val, new_val)

            self.mirror_grp(left_ctrl,right_ctrl)

    def controller_small_big(self, base_name, parent_list, pos, ctrl_rotate,base_ctrl_color):
        self.ctrl_lower_size = [0.5, 0.5, 0.5]
        self.ctrl_outer_size = [0.8, 0.8, 0.8]
        self.base_ctrl_freez_trans = True
        self.base_ctrl_freez_rotate = True
        self.base_ctrl_freez_scale = True
        self.base_ctrl_color = base_ctrl_color

        # SMALL CONTROLLER
        self.base_inner_ctrl = base_name + '_Inner_Ctrl'
        self.base_ctrl_size_ctrl = self.ctrl_lower_size
        self.base_ctrl_roate = ctrl_rotate
        self.base_parent_const_list = parent_list
        self.set_controller(self.base_inner_ctrl, pos, self.base_ctrl_size_ctrl,
                                         self.base_ctrl_roate, self.base_parent_const_list, self.base_parent_const_list,
                                         color=self.base_ctrl_color,
                                         freez_trans=self.base_ctrl_freez_trans,
                                         freez_rotate=self.base_ctrl_freez_rotate,
                                         freez_scale=self.base_ctrl_freez_scale)

        # BIF CONTROLLER
        self.base_outer_ctrl = base_name + '_Outer_Ctrl'
        self.base_ctrl_size_ctrl = self.ctrl_outer_size
        self.base_ctrl_roate = ctrl_rotate
        self.base_parent_const_list = []
        self.set_controller(self.base_outer_ctrl, pos, self.base_ctrl_size_ctrl,
                                         self.base_ctrl_roate, self.base_parent_const_list, self.base_parent_const_list,
                                         color=self.base_ctrl_color,
                                         freez_trans=self.base_ctrl_freez_trans,
                                         freez_rotate=self.base_ctrl_freez_rotate,
                                         freez_scale=self.base_ctrl_freez_scale)
        cmds.select(self.base_inner_ctrl, self.base_outer_ctrl)
        cmds.parent()

    def butt_def(self,thine_pos,prefix_name,side,val,base_ctrl_color,type,thine_sphere_name,thine_inner_ctrl):
        '''

        :param thine_pos: get the Thine Position
        :param prefix_name: get the Prefix no
        :param side: get the Side
        :param val: get the Val
        :param base_ctrl_color: get Base_Ctrl_Color
        :return: sphere_name,butt_clu_handle_name,
                thie_to_butt_cylinder_name,thine_to_butt_lower_cylinder_cluster_handle_name,thine_to_butt_upper_cylinder_cluster_handle_name,
                thine_outer_ctrl,

        '''

        self.thine_pos = thine_pos
        self.prefix_name = prefix_name
        self.side = side
        self.val = val
        self.type = type
        self.base_ctrl_color = base_ctrl_color
        self.thine_sphere_name = thine_sphere_name
        self.thine_inner_ctrl = thine_inner_ctrl

        butt_common = self.prefix_name + '_' + self.side + '_' + self.type + '_Butt_Tem_' + str(self.val)
        butt_sphere_name = butt_common + '_Geo'
        butt_clu_name = butt_common + '_Clu'
        butt_clu_handle_name = butt_clu_name + 'Handle'
        butt_pos = [self.thine_pos[0],self.thine_pos[1],(self.thine_pos[2] + (-8.5))]
        self.set_sphere_position(name=butt_sphere_name,
                                 transform_pos=butt_pos,
                                 cluster_name=butt_clu_name)

        #Create a sphere
        thine_to_butt_common = self.prefix_name + '_' + self.side + '_' + self.type + '_Thine_to_Butt_Tem_' + str(self.val)
        thine_to_butt_cylinder_name = thine_to_butt_common + '_Geo'
        thine_to_butt_lower_cylinder_cluster_name = self.prefix_name + "_" + self.side + '_' + self.type + '_Thine_to_Butt_Lower_Tem_' + str(
            self.val) + '_Clu'
        thine_to_butt_lower_cylinder_cluster_handle_name = thine_to_butt_lower_cylinder_cluster_name + 'Handle'
        thine_to_butt_upper_cylinder_cluster_name = self.prefix_name + "_" + self.side + '_' + self.type + '_Thine_to_Butt_Upper_Tem_' + str(
            self.val) + '_Clu'
        thine_to_butt_upper_cylinder_cluster_handle_name = thine_to_butt_upper_cylinder_cluster_name + 'Handle'
        self.cylinder_rotate = [90, 0, 0]
        self.set_cylinder_position(cylinder_name=thine_to_butt_cylinder_name,
                                   cluster_1=thine_to_butt_lower_cylinder_cluster_name,
                                   cluster_2=thine_to_butt_upper_cylinder_cluster_name,
                                   cluster_1_parent=butt_sphere_name,
                                   cluster_2_parent=self.thine_sphere_name,
                                   rotate_val=[self.cylinder_rotate[0],
                                               self.cylinder_rotate[1],
                                               self.cylinder_rotate[2]])

        ctrl_rotate = [90,0,0]
        butt_const_list = [butt_clu_handle_name,
                           thine_to_butt_lower_cylinder_cluster_handle_name]
        self.controller_small_big(base_name=butt_common,
                                  parent_list=butt_const_list,
                                  pos=butt_pos,
                                  ctrl_rotate=ctrl_rotate,
                                  base_ctrl_color=self.base_ctrl_color)

        self.butt_inner_ctrl = butt_common + '_Inner_Ctrl'
        self.butt_outer_ctrl = butt_common + '_Outer_Ctrl'

        parent_list = [thine_to_butt_upper_cylinder_cluster_handle_name]
        self.parent_constraint(self.thine_inner_ctrl, parent_list)


        return butt_sphere_name,\
               butt_clu_handle_name, \
               thine_to_butt_cylinder_name, \
               thine_to_butt_lower_cylinder_cluster_handle_name,\
               thine_to_butt_upper_cylinder_cluster_handle_name,\
               self.butt_outer_ctrl

    def hip_def(self,type,hip_pos,side,val,connector,common_name,prefix_name):
        '''

        :param type: set the which type os this
        :param hip_pos: set the hip Position
        :param side: set the side of the object
        :param val: set the no of the val
        :param connector: set the connector
        :param inner_ctrl: set eh inner control to constaint
        :return: hip_sphere_name,hip_outer_ctrl,thine_to_hip_lower_clu_handle_name,thine_hip_upper_clu_handle_name,
        '''

        self.type = type
        self.hip_pos = hip_pos
        self.side = side
        self.val = val
        self.connector = connector
        self.prefix_name = prefix_name
        self.inner_ctrl = common_name + '_Inner_Ctrl'
        self.sphere_name = common_name + '_Geo'


        # create a sphere
        self.hip_common = self.prefix_name + '_' + self.type + '_Hip_Tem_' + str(self.val)
        self.hip_sphere_name = self.hip_common + "_Geo"
        self.hip_inner_ctrl = self.hip_common + '_Inner_Ctrl'
        self.hip_outer_ctrl = self.hip_common + '_Outer_Ctrl'
        self.ctrl_rotate = [0, 0, 0]
        if cmds.objExists(self.hip_sphere_name):
            pass
        else:
            self.hip_sphere_clu_name = self.hip_common + '_Clu'
            self.hip_sphere_clu_handle_name = self.hip_sphere_clu_name + 'Handle'
            self.set_sphere_position(self.hip_sphere_name,
                                     self.hip_pos,
                                     self.hip_sphere_clu_name)

            #Create a Controller for the
            self.base_ctrl_color = 'Yellow'
            self.hip_const_list = [self.hip_sphere_clu_handle_name]
            self.controller_small_big(base_name=self.hip_common,
                                      parent_list=self.hip_const_list,
                                      pos=self.hip_pos,
                                      ctrl_rotate=self.ctrl_rotate,
                                      base_ctrl_color=self.base_ctrl_color)



        # create a cylinder
        self.thine_to_hip_common = self.prefix_name + "_" + self.side + '_' + self.type + '_' + self.connector + '_Tem_' + str(self.val)
        self.thine_to_hip_cylinder_name = self.thine_to_hip_common + '_Geo'
        self.thine_to_hip_lower_cylinder_cluster_name = self.prefix_name + "_" + self.side + '_' + self.type + '_' + self.connector + '_Lower_Tem_' + str(self.val) + '_Clu'
        self.thine_to_hip_lower_cylinder_cluster_handle_name = self.thine_to_hip_lower_cylinder_cluster_name + 'Handle'
        self.thine_to_hip_upper_cylinder_cluster_name = self.prefix_name + "_" + self.side + '_' + self.type + '_' + self.connector + '_Upper_Tem_' + str(self.val) + '_Clu'
        self.thine_to_hip_upper_cylinder_cluster_handle_name = self.thine_to_hip_upper_cylinder_cluster_name + 'Handle'
        self.cylinder_rotate = [0, 0, 0]
        self.set_cylinder_position(self.thine_to_hip_cylinder_name,
                                   self.thine_to_hip_lower_cylinder_cluster_name,
                                   self.thine_to_hip_upper_cylinder_cluster_name,
                                   self.hip_sphere_name,
                                   self.sphere_name,
                                   rotate_val=[self.cylinder_rotate[0],
                                               self.cylinder_rotate[1],
                                               self.cylinder_rotate[2]])
        # do parent const
        cmds.parentConstraint(self.inner_ctrl, self.thine_to_hip_upper_cylinder_cluster_handle_name, mo=False)
        cmds.parentConstraint(self.hip_inner_ctrl, self.thine_to_hip_lower_cylinder_cluster_handle_name, mo=False)

        #hip_sphere_name,hip_outer_ctrl,thine_to_hip_lower_clu_handle_name,thine_hip_upper_clu_handle_name,
        return self.hip_sphere_name\
            ,self.hip_outer_ctrl\
            ,self.thine_to_hip_lower_cylinder_cluster_handle_name\
            ,self.thine_to_hip_upper_cylinder_cluster_handle_name\
            ,self.thine_to_hip_cylinder_name\
            ,self.hip_sphere_clu_handle_name

    def finger_loc_def(self,no_finger,finger_default_pos):
        self.no_finger = int(no_finger)
        self.finger_default_pos = finger_default_pos
        a = 0
        self.locator_list = []
        x_val = 0
        while a < self.no_finger:
            locator_name = 'Finger_' + str(a) + '_Loc'
            self.locator_list.append(locator_name)
            cmds.spaceLocator(n=locator_name, p=(x_val, 0, 0))
            cmds.select(locator_name)
            cmds.CenterPivot()
            #parent to the finger grp
            locator_grp_name  = 'Finger_Grp'
            self.grp_create(object_name=locator_name,
                            grp_name=locator_grp_name)

            x_val += 3
            a += 1

        cmds.select(locator_grp_name)
        cmds.CenterPivot()
        cmds.move(0, 0, 0, rpr=True)
        cmds.FreezeTransformations()
        cmds.move(self.finger_default_pos[0],
                  self.finger_default_pos[1],
                  self.finger_default_pos[2])

        return self.locator_list,locator_grp_name

    def set_parent(self,child_name,grp_name):
        #checkt the object in the grpe bane
        grp_name = self.check_grp(grp_name)
        child_list = cmds.listRelatives(grp_name,c=True)
        if child_list != None:
            if child_name in child_list:
                pass
            else:
                cmds.parent(child_name,grp_name)
        else:
            cmds.parent(child_name,grp_name)

    def check_grp(self,grp_name):
        if cmds.objExists(grp_name):
            pass
        else:
            cmds.createNode('transform',n=grp_name)
        return grp_name



    def get_var(self,common_name):

        sphere_name = common_name + "_Geo"
        clu_name = common_name + '_Clu'
        clu_handle_name = clu_name + 'Handle'

        return sphere_name,clu_name,clu_handle_name









