
#import all the moduler
import maya.cmds as cmds
import maya.mel as mel
import sys

class CLUSTER_TO_JOINT:
    def __init__(self):
        self.cluster_to_joint_def()

    def cluster_to_joint_def(self):
        obj_list = []
        sel_cluster = cmds.ls(sl=True)
        len_sel_cluster = len(sel_cluster)
        #cehck individual cluster and check the object influ
        a = 0
        while a < len_sel_cluster:
            #cehck the object connected
            cluster_name = cmds.listConnections(sel_cluster[a])
            cluster_sets_name = cmds.listConnections(cluster_name[0], type="objectSet")
            # query the selectd vtx connected to the sets
            # sets -q cluster1Set;
            cluster_set_member = cmds.sets(cluster_sets_name, q=True)
            obj_name = cluster_set_member[0].split(".vtx")[0]
            print cluster_name
            #print obj_name
            #get the particullar object list of the joint influ value
            #add to the list
            print obj_name
            obj_list.append(obj_name)

            cmds.select(obj_name)
            get_val = cmds.percent(cluster_name[0],q=True, v=True)
            no_vtx = cmds.polyEvaluate(obj_name, v=True)
            skin_cluster_name = mel.eval("findRelatedSkinCluster(\"%s\");" % obj_name)
            if skin_cluster_name == "":
                jnt_name = "base_JNT"
                cmds.select(cl=True)
                cmds.joint(p=(0, 0, 0), n=jnt_name)
                cmds.select(cl=True)
                # move this joint to the object base locatoion
                cmds.parentConstraint(obj_name, jnt_name, mo=False)
                cmds.select(jnt_name + "_parentConstraint1")
                cmds.delete()
                # bind with surface
                cmds.select(jnt_name, obj_name)
                cmds.SmoothBindSkin()
                # find the skin cluster name
                skin_cluster_name = mel.eval("findRelatedSkinCluster(\"%s\");" % obj_name)
            else:
                #Create a base joint if there is not
                if cmds.objExists("base_JNT"):
                    pass
                else:
                    #Create a base Jnt
                    jnt_name = "base_JNT"
                    cmds.select(cl=True)
                    cmds.joint(p=(0, 0, 0), n=jnt_name)
                    cmds.select(cl=True)
                    # move this joint to the object base locatoion
                    cmds.parentConstraint(obj_name, jnt_name, mo=False)
                    cmds.select(jnt_name + "_parentConstraint1")
                    cmds.delete()
                    # bind with surface
                    cmds.select(jnt_name, obj_name)
                    cmds.AddInfluence()
                    #make all the lock and only make a base jnt as a on


            a+=1

        #print obj_list
        #


        b = 0
        while b < len(obj_list):
            #query all the cluster and get the value
            skin_cluster_name = mel.eval("findRelatedSkinCluster(\"%s\");" % obj_list[b])
            c = 0
            while c < len_sel_cluster:
                cluster_name = cmds.listConnections(sel_cluster[c])
                cmds.select(obj_list[b])
                get_val = cmds.percent(cluster_name[0], q=True, v=True)
                # add a new joint to the object
                new_jnt_name = sel_cluster[c] + "_Bind_Jnt"
                cmds.select(cl=True)
                cmds.joint(p=(0, 0, 0), n=new_jnt_name)
                cmds.select(cl=True)
                cmds.parentConstraint(sel_cluster[c], new_jnt_name, mo=False)
                cmds.select(new_jnt_name + "_parentConstraint1")
                cmds.delete()
                # add the influence value
                cmds.select(new_jnt_name, obj_name)
                cmds.AddInfluence()

                d = 0
                while d < no_vtx:
                    # put the value on that
                    cmds.skinPercent(skin_cluster_name, (obj_list[b] + '.vtx[%s]' % d),
                                     transformValue=[new_jnt_name, get_val[d]])

                    d += 1


                c+=1


            b+=1
