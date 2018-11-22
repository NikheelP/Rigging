
import maya.cmds as cmds
import rig_helper

class COMBINE_CLUSTER:
    def __init__(self):
        self.rig_help_class = rig_helper.rig_help()
        self.combine_cluster_def()

    def combine_cluster_def(self):
        #get the number of the cluster and combine that
        #select the cluster
        sel_cluster = cmds.ls(sl=True)
        len_sel_cluster = len(sel_cluster)
        obj_list = []

        if len_sel_cluster <= 1:
            cmds.error("Please select Minimum 2 cluster")
        else:
            cmds.select(cl=True)
            per = []

            #get the obj name from the cluster handle
            #Create a Obj List and make a list
            a = 0
            progressControl = cmds.progressWindow(title='addding Cluster', progress=a, status='Sleeping: 0%',
                                                  isInterruptable=True)
            percentage_add = 0
            while a < len_sel_cluster:
                percentage = 100.0 / len_sel_cluster
                percentage_add = percentage_add + percentage
                status_info = "adding  " + sel_cluster[a] + " to Combine Cluster"
                progressInc = cmds.progressWindow(progressControl, status=status_info, edit=True, pr=percentage_add)

                # query the cluster name
                cluster_name = cmds.listConnections(sel_cluster[a], type="cluster")
                # query the sets name
                cluster_sets_name = cmds.listConnections(cluster_name[0], type="objectSet")
                # query the selectd vtx connected to the sets
                # sets -q cluster1Set;
                cluster_set_member = cmds.sets(cluster_sets_name, q=True)
                # make a split
                obj_name = cluster_set_member[0].split(".vtx")[0]
                obj_list.append(obj_name)

                a += 1
                # remove the Duplicate object from the obj list
            filter_list = list(set(obj_list))
            #select all of the geo and create a cluster on that
            cmds.select(cl=True)
            e = 0
            while e < len(filter_list):
                cmds.select(filter_list[e],add=True)
                e+=1
            combine_cluster_name = "Combine_Cluster"
            cmds.cluster(n=combine_cluster_name)

            #make a all the value 0
            h = 0
            while h < len(filter_list):
                no_vtx = cmds.polyEvaluate(filter_list[h], v=True)
                g = 0
                while g < no_vtx:
                    cmds.percent(combine_cluster_name, (filter_list[h] + '.vtx[%s]' % g), v=0)
                    g+=1
                h += 1

            #work according to the obj
            d = 0
            while d < len(filter_list):
                # get the total vertex count
                no_vtx = cmds.polyEvaluate(filter_list[d], v=True)
                # get the default vertex value

                def_value = []
                b = 0
                while b < no_vtx:
                    base_value = cmds.pointPosition(filter_list[d] + '.vtx[%s]' % b)[1]
                    # append to the list
                    def_value.append(base_value)
                    b += 1

                c = 0
                #Create a combine Cluster
                while c < len_sel_cluster:
                    cmds.select(sel_cluster[c])
                    cmds.move(0, 5, 0, r=True, os=True, wd=True)
                    # get the object vertex value

                    f = 0
                    new_value = []
                    while f < no_vtx:
                        # get the new vertex value
                        new_value_1 = cmds.pointPosition(filter_list[d] + '.vtx[%s]' % f)[1]
                        new_value.append(new_value_1)
                        # Compare the old and new Value
                        if def_value[f] != new_value_1:
                            #adding the value to the combine clustae
                            #get the current value of the cluster
                            cluster_name = cmds.listConnections(sel_cluster[c], type="cluster")
                            value = cmds.percent(cluster_name[0],(filter_list[d] + '.vtx[%s]' % f),v=True,q=True)
                            #set the same value to the combine cluster
                            cmds.percent(combine_cluster_name,(filter_list[d] + '.vtx[%s]' % f),v=value[0])
                        else:
                            pass

                        f += 1

                    #put the cluster zero
                    cmds.select(sel_cluster[c])
                    cmds.move(0, -5, 0, r=True, os=True, wd=True)
                    c+=1
                d+=1

            cmds.progressWindow(progressControl, endProgress=1)

