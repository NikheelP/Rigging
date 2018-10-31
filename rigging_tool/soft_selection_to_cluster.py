
import maya.api.OpenMaya as om
import maya.api.OpenMayaAnim as oma
import maya.cmds as cmds
import maya.mel as mel


class SOFT_SELECTION_TO_CLUSTER:
    def __init__(self):
        self.soft_select_to_cluster_def()

    def soft_select_to_cluster_def(self):
        sel_vert = cmds.ls(sl=True)
        soft_selcetion = om.MGlobal.getRichSelection()
        rich_selection = om.MRichSelection(soft_selcetion)
        selection_list = rich_selection.getSelection()
        component = selection_list.getComponent(0)
        component_index = om.MFnSingleIndexedComponent(component[1])
        vertex_list = component_index.getElements()
        weight_list = {}
        for loop in range(len(vertex_list)):
            weight = component_index.weight(loop)
            influence = weight.influence
            weight_list.setdefault(vertex_list[loop],influence)


        obj_name = sel_vert[0].split(".vtx")[0]
        cmds.select(obj_name)
        #get the object name
        if cmds.objExists('Soft_Selection_to_Cluster*Handle'):
            cmds.select('Soft_Selection_to_Cluster*')
            sel_cluster = cmds.ls(sl=True)
            len_sel_cluster = len(sel_cluster)
            cluster_name = 'Soft_Selection_to_Cluster' + str(len_sel_cluster + 1)
        else:
            cluster_name = 'Soft_Selection_to_Cluster1'
        cmds.cluster(n=cluster_name)
        cluster_handle_name = cluster_name + 'Handle'
        cluster_shape_name = cmds.listRelatives(cluster_handle_name,s=True)[0]
        cmds.percent(cluster_name, (obj_name + '.vtx[0:]'), v=0)
        gMainProgressBar = mel.eval('$tmp = $gMainProgressBar')
        cmds.progressBar( gMainProgressBar,
                          edit=True,
                          beginProgress=True,
                          isInterruptable=True,
                          status='Creating a soft Selection....',
                          maxValue=len(weight_list) )
        equal_value = len(weight_list)/100
        add_value = 0
        for each_weight in weight_list:
            current_vertex = obj_name + '.vtx[%s]' % each_weight
            weight_value = weight_list[each_weight]
            cmds.percent(cluster_name, current_vertex, v=weight_value)
            add_value = add_value + equal_value
            cmds.progressBar(gMainProgressBar, edit=True, step=add_value)
        cmds.progressBar(gMainProgressBar, edit=True, endProgress=True)


        point_position  = cmds.pointPosition(sel_vert[0])
        cmds.setAttr((cluster_handle_name + '.rotatePivotX'),point_position[0])
        cmds.setAttr((cluster_handle_name + '.rotatePivotY'),point_position[1])
        cmds.setAttr((cluster_handle_name + '.rotatePivotZ'),point_position[2])
        cmds.setAttr((cluster_handle_name + '.scalePivotX'),point_position[0])
        cmds.setAttr((cluster_handle_name + '.scalePivotY'),point_position[1])
        cmds.setAttr((cluster_handle_name + '.scalePivotZ'),point_position[2])

        cmds.setAttr((cluster_shape_name + '.originX'),point_position[0])
        cmds.setAttr((cluster_shape_name + '.originY'),point_position[1])
        cmds.setAttr((cluster_shape_name + '.originZ'),point_position[2])

        cmds.select(cluster_handle_name)

        return cluster_name


