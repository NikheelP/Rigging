
import maya.api.OpenMaya as om
import maya.api.OpenMayaAnim as oma
import maya.cmds as cmds
import maya.mel as mel

class SOFT_SELECTION_TO_JOINT:
    def __init__(self):
        pass

    def soft_selection_to_joint(self):
        sel_vert = cmds.ls(sl=True)
        soft_selcetion = om.MGlobal.getRichSelection()
        rich_selection = om.MRichSelection(soft_selcetion)
        selection_list = rich_selection.getSelection()
        component = selection_list.getComponent(0)
        component_index = om.MFnSingleIndexedComponent(component[1])
        vertex_list = component_index.getElements()
        obj_name = sel_vert[0].split(".vtx")[0]
        weight_list = {}
        for loop in range(len(vertex_list)):
            weight = component_index.weight(loop)
            influence = weight.influence
            weight_list.setdefault(vertex_list[loop],influence)
        #create a two joint and paste a joint position on the

        skin_cluster_name = mel.eval('findRelatedSkinCluster("%s");' % obj_name)
        jnt_name = obj_name + '_Soft_Selection_to_Jnt'
        point_position  = cmds.pointPosition(sel_vert[0])
        if not skin_cluster_name:
            base_jnt_name = 'Base_Jnt'
            cmds.select(cl=True)
            cmds.joint(n=base_jnt_name,p=(0,0,0))
            cmds.select(cl=True)
            jnt_name = obj_name + '_Soft_selection_Jnt'
            self.joint_name = jnt_name
            cmds.joint(n=jnt_name,p=(point_position[0],
                                     point_position[1],
                                     point_position[2]))
            cmds.select(base_jnt_name,jnt_name,obj_name)
            cmds.SmoothBindSkin()
            skin_cluster_name = mel.eval('findRelatedSkinCluster("%s");' % obj_name)
            cmds.skinPercent(skin_cluster_name,(obj_name + '.vtx[0:]'),tv=(base_jnt_name,1))

            for each_weight in weight_list:
                current_vertex = obj_name + '.vtx[%s]' % each_weight
                weight_value = weight_list[each_weight]
                cmds.skinPercent(skin_cluster_name,current_vertex ,tv=(jnt_name,weight_value))

            #transfer the value to the jonint
            cmds.select(self.joint_name)
            print('\n\n\n\nSucessfully Create a Soft Selection to Joint')
        else:
            print('Skin Custer is already there can u please delete the skin cluster and run the'
                  'script again')


