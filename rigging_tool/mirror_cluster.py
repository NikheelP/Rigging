
#GENERAL INFO
_version = 'V001'
_author =  'Nikheel patel'
_email  =  'spark.visualartist@gmail.com'
_last_modify = '10/28/2018'

# import modulers
import os
import maya.cmds as cmds
import maya.OpenMayaUI as omu
from functools import partial
import maya.api.OpenMaya as om
import maya.OpenMayaMPx as OpenMayaMPx
import maya.OpenMayaAnim as oma
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

# basic import  or add command
from PySide import QtCore
from PySide import QtGui
#import sip
import maya.mel as mel

class MIRROR_CLUSTER(MayaQWidgetDockableMixin, QtGui.QMainWindow):
    def __init__(self,parent=None):
        super(MIRROR_CLUSTER, self).__init__(parent=parent)
        #self.cluster_mirror()
        self.ui()

    def ui(self):
        self.setObjectName("mirror_cluster")
        self.setWindowTitle('Mirror Cluster')
        self.resize(500, 142)
        self.cluster_mirror_central_widget = QtGui.QWidget(self)
        self.cluster_mirror_central_widget.setObjectName("cluster_mirror_central_widget")
        self.verticalLayout = QtGui.QVBoxLayout(self.cluster_mirror_central_widget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.cluster_mirror_scroll_area = QtGui.QScrollArea(self.cluster_mirror_central_widget)
        self.cluster_mirror_scroll_area.setWidgetResizable(True)
        self.cluster_mirror_scroll_area.setObjectName("cluster_mirror_scroll_area")
        self.cluster_mirror_scrollArea_widget_contents = QtGui.QWidget()
        self.cluster_mirror_scrollArea_widget_contents.setGeometry(QtCore.QRect(0, 0, 478, 97))
        self.cluster_mirror_scrollArea_widget_contents.setObjectName("cluster_mirror_scrollArea_widget_contents")
        self.gridLayout = QtGui.QGridLayout(self.cluster_mirror_scrollArea_widget_contents)
        self.gridLayout.setObjectName("gridLayout")

        #MIRROR RADIO BUTTON
        self.mirror_with_same_cluster_radio_button = QtGui.QRadioButton(self.cluster_mirror_scrollArea_widget_contents)
        self.mirror_with_same_cluster_radio_button.setObjectName("mirror_with_same_cluster_radio_button")
        self.mirror_with_same_cluster_radio_button.setText('Mirror With Same Cluster')
        self.mirror_with_same_cluster_radio_button.setChecked(True)
        self.gridLayout.addWidget(self.mirror_with_same_cluster_radio_button, 0, 0, 1, 1)

        self.mirror_with_new_cluster_radio_button = QtGui.QRadioButton(self.cluster_mirror_scrollArea_widget_contents)
        self.mirror_with_new_cluster_radio_button.setObjectName("mirror_with_new_cluster_radio_button")
        self.mirror_with_new_cluster_radio_button.setText('Mirror With New Cluster')
        self.gridLayout.addWidget(self.mirror_with_new_cluster_radio_button, 0, 1, 1, 1)

        #AXIS
        self.axis_label = QtGui.QLabel(self.cluster_mirror_scrollArea_widget_contents)
        self.axis_label.setObjectName("axis_label")
        self.axis_label.setText('Axis : ')
        self.gridLayout.addWidget(self.axis_label, 1, 0, 1, 1)

        self.axis_combo_box = QtGui.QComboBox(self.cluster_mirror_scrollArea_widget_contents)
        self.axis_combo_box.setMinimumSize(QtCore.QSize(303, 0))
        self.axis_combo_box.setObjectName("axis_combo_box")
        self.axis_combo_box.addItem("X")
        self.axis_combo_box.addItem("Y")
        self.axis_combo_box.addItem("Z")
        self.gridLayout.addWidget(self.axis_combo_box, 1, 1, 1, 1)

        #BUTTON
        self.create_mirror_button = QtGui.QPushButton(self.cluster_mirror_scrollArea_widget_contents)
        self.create_mirror_button.setObjectName("create_mirror_button")
        self.create_mirror_button.setText('Create Mirror')
        self.create_mirror_button.clicked.connect(self.cluster_mirror)
        self.gridLayout.addWidget(self.create_mirror_button, 2, 0, 1, 2)

        #SPACE ITEM
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)

        self.cluster_mirror_scroll_area.setWidget(self.cluster_mirror_scrollArea_widget_contents)
        self.verticalLayout.addWidget(self.cluster_mirror_scroll_area)
        self.setCentralWidget(self.cluster_mirror_central_widget)
        return self

    def cluster_mirror(self):
        #get the comboBox value
        self.axis_combo_box_query = str(self.axis_combo_box.currentText())
        if self.mirror_with_same_cluster_radio_button.isChecked() == True:
            self.mirror_with_same_cluster_query = True
            self.mirror_with_new_cluster = False
        elif self.mirror_with_new_cluster_radio_button.isChecked() == True:
            self.mirror_with_same_cluster_query = False
            self.mirror_with_new_cluster = True

        select_cluster = cmds.ls(sl=True)
        for each_cluster in select_cluster:
            cluster_name = cmds.listConnections(each_cluster)
            cluster_sets_name = cmds.listConnections(cluster_name[0], type="objectSet")
            # query the selectd vtx connected to the sets
            # sets -q cluster1Set;
            cluster_set_member = cmds.sets(cluster_sets_name, q=True)
            obj_name = cluster_set_member[0].split(".vtx")[0]

            base_MSelection_list = om.MSelectionList()
            base_MSelection_list.add(obj_name)
            base_geo_dag_path = base_MSelection_list.getDagPath(0)

            #get the base vertex position
            base_mfn_mesh = om.MFnMesh(base_geo_dag_path)
            base_vtx_list = base_mfn_mesh.getPoints(om.MSpace.kObject)

            #get the move vertex position
            clusterMSelection = om.MSelectionList()
            clusterMSelection.add(each_cluster)
            clusterDagPath = clusterMSelection.getDagPath(0)
            mFnTransform = om.MFnTransform(clusterDagPath)
            world = mFnTransform.translation(om.MSpace.kWorld)
            moveWorld = om.MVector(world.x+1,world.y,world.z)
            mFnTransform.setTranslation(moveWorld,om.MSpace.kWorld)
            movePosition = base_mfn_mesh.getPoints(om.MSpace.kObject)

            vtx_name = []
            vtx_no = []
            base_vtx_position = []
            move_vtx_position = []
            base_vtx_position_x = []
            base_vtx_position_y = []
            base_vtx_position_z = []
            move_vtx_position_x = []
            move_vtx_position_y = []
            move_vtx_position_z = []
            a = 0
            while a < len(base_vtx_list):
                #vtx_name
                #pSphere1.vtx[191]
                vtx_name_1 = obj_name + '.vtx[%s]' % a
                vtx_name.append(vtx_name_1)
                #vtx_no
                vtx_no.append(a)
                #base_vtx_position
                base_vtx_position.append(base_vtx_list[a])
                #move_vtx_position
                move_vtx_position.append(movePosition[a])

                #base_vtx_position_x
                base_vtx_position_x_value = base_vtx_list[a].x
                base_vtx_position_x.append(base_vtx_position_x_value)

                #base_vtx_position_y
                base_vtx_position_y_value = base_vtx_list[a].y
                base_vtx_position_y.append(base_vtx_position_y_value)

                #base_vtx_position_z
                base_vtx_position_z_value = base_vtx_list[a].z
                base_vtx_position_z.append(base_vtx_position_z_value)

                #base_vtx_position_x
                move_vtx_position_x_value = movePosition[a].x
                move_vtx_position_x.append(move_vtx_position_x_value)

                #base_vtx_position_y
                move_vtx_position_y_value = movePosition[a].y
                move_vtx_position_y.append(move_vtx_position_y_value)

                #base_vtx_position_x
                move_vtx_position_z_value = movePosition[a].z
                move_vtx_position_z.append(move_vtx_position_z_value)


                a+=1
            min_value_x = min(base_vtx_position_x)
            max_valye_x = max(base_vtx_position_x)
            middle_value_x = (min_value_x + max_valye_x)/2
            a = 0
            while a < len(base_vtx_position_x):
                if rig_help_class.decimal_point(middle_value_x) == rig_help_class.decimal_point(base_vtx_position_x[a]):
                    middle_vertex_no = a
                a+=1

            #cluster influence list
            cluster_vtx_list = []
            clustert_vtx_list_no = []
            for vertexIndex in range(len(movePosition)):
                length = movePosition[vertexIndex] - base_vtx_list[vertexIndex]
                if length.x != 0.0000000:
                    clustert_vtx_list_no.append(vertexIndex)
                    cluster_vtx_list.append(movePosition[vertexIndex])

            if self.axis_combo_box_query == 'X':
                axis = [-1,1,1]
                self.point_position = cmds.xform(each_cluster,q=1,ws=1,rp=1)
                self.new_position = [(self.point_position[0]*-1),self.point_position[1],self.point_position[2]]
            elif self.axis_combo_box_query == 'Y':
                axis = [1,-1,1]
                self.point_position = cmds.xform(each_cluster,q=1,ws=1,rp=1)
                self.new_position = [(self.point_position[0]),(self.point_position[1]*-1),self.point_position[2]]
            elif self.axis_combo_box_query == 'Z':
                axis = [1,1,-1]
                self.point_position = cmds.xform(each_cluster,q=1,ws=1,rp=1)
                self.new_position = [(self.point_position[0]),(self.point_position[1]),(self.point_position[2]*-1)]
            mitMeshPolygon = om.MItMeshPolygon(base_geo_dag_path)
            opp_vtx_list = []
            cluster_wight_value_list = []
            for index in range (len(cluster_vtx_list)):
                xyz = cluster_vtx_list[index]
                opp_xyz = om.MPoint(xyz.x*axis[0],xyz.y*axis[1],xyz.z*axis[2])
                closetPoint,faceID = base_mfn_mesh.getClosestPoint(opp_xyz,om.MSpace.kObject)
                mitMeshPolygon.setIndex(faceID)
                facevertex_list = mitMeshPolygon.getVertices()
                mVectorLengthList = []
                for each_vertex in facevertex_list:
                    oppvertexPosition = base_mfn_mesh.getPoint(each_vertex,om.MSpace.kObject)
                    oppMVector = om.MVector(oppvertexPosition)
                    mirrorMVector = om.MVector(opp_xyz)
                    mVectorLength = oppMVector-mirrorMVector
                    length = mVectorLength.length()
                    mVectorLengthList.append(length)
                closetvertex = min(mVectorLengthList)
                vertexIndex  = mVectorLengthList.index(closetvertex)
                currentVertexId = facevertex_list[vertexIndex]

                opp_vtx_no = obj_name + '.vtx[%s]' % currentVertexId
                opp_vtx_list.append(opp_vtx_no)


                #now get the cluster value
                cluster_vtx_no = obj_name + '.vtx[%s]' % clustert_vtx_list_no[index]
                percent_val = cmds.percent( cluster_name[0],cluster_vtx_no,q=True, v=True)[0]
                cluster_wight_value_list.append(percent_val)


            if self.mirror_with_same_cluster_query == True:
                print('Mirror with the same Cluster')
                a = 0
                while a < len(opp_vtx_list):
                    #percent -v 0.692 Soft_Selection_to_Cluster1 pSphere1.vtx[217] ;
                    cmds.percent(cluster_name[0],opp_vtx_list[a],v=cluster_wight_value_list[a])
                    a+=1
            else:
                mirror_cluster_name = 'Mirror_' + cluster_name[0]
                cmds.select(obj_name)
                cmds.cluster(n=mirror_cluster_name)
                cluster_handle_name = mirror_cluster_name + 'Handle'
                cluster_shape_name = cmds.listRelatives(cluster_handle_name,s=True)[0]
                cmds.percent(mirror_cluster_name, (obj_name + '.vtx[0:]'), v=0)

                a = 0
                while a < len(opp_vtx_list):
                    #percent -v 0.692 Soft_Selection_to_Cluster1 pSphere1.vtx[217] ;
                    cmds.percent(mirror_cluster_name,opp_vtx_list[a],v=cluster_wight_value_list[a])
                    a+=1

                cmds.setAttr((cluster_handle_name + '.rotatePivotX'),self.new_position[0])
                cmds.setAttr((cluster_handle_name + '.rotatePivotY'),self.new_position[1])
                cmds.setAttr((cluster_handle_name + '.rotatePivotZ'),self.new_position[2])
                cmds.setAttr((cluster_handle_name + '.scalePivotX'),self.new_position[0])
                cmds.setAttr((cluster_handle_name + '.scalePivotY'),self.new_position[1])
                cmds.setAttr((cluster_handle_name + '.scalePivotZ'),self.new_position[2])

                cmds.setAttr((cluster_shape_name + '.originX'),self.new_position[0])
                cmds.setAttr((cluster_shape_name + '.originY'),self.new_position[1])
                cmds.setAttr((cluster_shape_name + '.originZ'),self.new_position[2])

            mFnTransform.setTranslation(world,om.MSpace.kWorld)
            print('SucessFully Mirror the Cluster Value')


def main():
    w = MIRROR_CLUSTER()
    w.show()
