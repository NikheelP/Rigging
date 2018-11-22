import maya.cmds as cmds
import maya.mel as mel
import sys


class JOINT_TO_CLUSTER:
    def __init__(self):
        print('this is the joint to cluster')
        self.joint_to_cluster_def()

    def joint_to_cluster_def(self):
        sel_jnt = cmds.ls(sl=True)
        len_sel_jnt = len(sel_jnt)
        if len_sel_jnt == 0:
            cmds.error("Please selecet atleast one Joint to run the command")
        else:
            # get all the skincluster name
            cmds.SelectAllGeometry()
            sel_geo = cmds.ls(sl=True)
            len_sel_obj = len(sel_geo)
            b = 0
            total_skin_cluster = []
            obj_name = []
            while b < len_sel_obj:
                # get the skincluster name and add to the list
                skin_cluster_name = mel.eval("findRelatedSkinCluster(\"%s\");" % sel_geo[b])
                total_skin_cluster.append(skin_cluster_name)
                obj_name.append(sel_geo[b])
                b += 1

            a = 0
            total_skin_new_list = []
            while a < len_sel_jnt:
                # get the cluster name
                # get the skincluster name
                list_connection = cmds.listConnections(sel_jnt[a])
                filter_list_connection = list(set(list_connection))
                # sect the all the object and get the skin cluster name
                # Create a cluster and snap to the joint position
                c = 0
                while c < len(filter_list_connection):
                    # see the skin cluster in the list
                    d = 0
                    while d < len(total_skin_cluster):
                        if filter_list_connection[c] == total_skin_cluster[d]:
                            # assign the cluster to the object
                            # print obj_name[d]
                            # print obj_name
                            cmds.select(obj_name[d])
                            cluster_name = sel_jnt[a] + "_" + obj_name[d] + '_Cluster'
                            cmds.cluster(n=cluster_name)
                            cluster_handle_name = cluster_name + 'Handle'
                            cluster_shape_name = cmds.listRelatives(cluster_handle_name, s=True)[0]
                            point_position = cmds.getAttr((sel_jnt[a] + '.t'))[0]
                            cmds.setAttr((cluster_handle_name + '.rotatePivotX'), point_position[0])
                            cmds.setAttr((cluster_handle_name + '.rotatePivotY'), point_position[1])
                            cmds.setAttr((cluster_handle_name + '.rotatePivotZ'), point_position[2])
                            cmds.setAttr((cluster_handle_name + '.scalePivotX'), point_position[0])
                            cmds.setAttr((cluster_handle_name + '.scalePivotY'), point_position[1])
                            cmds.setAttr((cluster_handle_name + '.scalePivotZ'), point_position[2])

                            cmds.setAttr((cluster_shape_name + '.originX'), point_position[0])
                            cmds.setAttr((cluster_shape_name + '.originY'), point_position[1])
                            cmds.setAttr((cluster_shape_name + '.originZ'), point_position[2])

                            # now Transfer the value joint to the cluster
                            no_vtx = cmds.polyEvaluate(obj_name[d], v=True)
                            # get the cluster name
                            e = 0
                            while e < no_vtx:
                                # get the influ val and snap to the cluster
                                val = cmds.skinPercent(filter_list_connection[c], (obj_name[d] + ".vtx[%s]" % e),
                                                       q=True, transform=sel_jnt[a])

                                cmds.percent(cluster_name, (obj_name[d] + ".vtx[%s]" % e), v=val)
                                e += 1
                        d += 1
                    c += 1
                a += 1

