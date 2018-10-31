
import maya.cmds as cmds
import maya.mel as mel

class COMBINE_JOINT:
    def __init__(self):
        self.combine_jnt()

    def combine_jnt(self):
        #Combine Joint
        sel_jnt = cmds.ls(sl=True)
        len_sel_jnt = len(sel_jnt)
        obj_list = []

        if len_sel_jnt <= 1:
            cmds.error("Please select Minimum 2 Joint")
        else:
            a = 0
            while a < len_sel_jnt:
                #get the skincluster name
                bind_pose_name = cmds.listConnections(sel_jnt[a] + '.bindPose')[0]
                skin_clster_name = cmds.listConnections( (bind_pose_name + '.message'),type='skinCluster')
                #get the geo
                geo_name = cmds.listConnections(skin_clster_name[0] + '.outputGeometry')[0]
                #create a new joint
                combine_jnt_name = sel_jnt[0] + '_' + sel_jnt[1] + '_Combine_Jnt'
                if cmds.objExists(combine_jnt_name):
                    pass
                else:
                    cmds.select(cl=True)
                    cmds.joint(n=combine_jnt_name,p=(0,0,0))
                    cmds.select(cl=True)
                #make all the jnt value zero
                jnt_connection_list = cmds.listConnections( skin_clster_name[0], type='joint')
                c = 0
                while c < len(jnt_connection_list):
                    cmds.setAttr((jnt_connection_list[c] + '.liw'),1)
                    c+=1
                #now add influ
                cmds.setAttr((sel_jnt[a] + '.liw'),0)
                if a == 0:
                    cmds.select(combine_jnt_name,geo_name)
                    mel.eval('skinClusterInfluence 1 "-ug -dr 4 -ps 0 -ns 10";')

                #now switch on the value
                cmds.setAttr((sel_jnt[a] + '.liw'),0)
                cmds.setAttr((combine_jnt_name + '.liw'),0)
                #get the influence of th eobj
                no_vtx = cmds.polyEvaluate(geo_name,v=True)
                b = 0
                while b < no_vtx:
                    vtx_no = geo_name + '.vtx[%s]' % b
                    value = cmds.skinPercent(skin_clster_name[0],vtx_no,transform=sel_jnt[a],query=True)
                    if value != 0:
                        cmds.skinPercent( skin_clster_name[0], vtx_no,
                                          transformValue=[(sel_jnt[a], 0)])

                    b+=1
                jnt_connection_list = cmds.listConnections( skin_clster_name[0], type='joint')
                c = 0
                while c < len(jnt_connection_list):
                    cmds.setAttr((jnt_connection_list[c] + '.liw'),1)
                    c+=1


                a+=1

            a = 0
            while a < len_sel_jnt:
                combine_jnt_name = sel_jnt[0] + '_' + sel_jnt[1] + '_Combine_Jnt'
                cmds.setAttr((sel_jnt[a] + '.liw'),0)
                cmds.setAttr((combine_jnt_name + '.liw'),0)
                a+=1





