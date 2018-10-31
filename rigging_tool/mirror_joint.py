
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




class MIRROR_JOINT(MayaQWidgetDockableMixin, QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MIRROR_JOINT, self).__init__(parent=parent)
        # self.cluster_mirror()
        self.ui()

    def ui(self):
        self.setObjectName("mirror_joint")
        self.setWindowTitle('Mirror Joint')
        self.resize(500, 142)
        self.joint_mirror_central_widget = QtGui.QWidget(self)
        self.joint_mirror_central_widget.setObjectName("joint_mirror_central_widget")
        self.verticalLayout = QtGui.QVBoxLayout(self.joint_mirror_central_widget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.joint_mirror_scroll_area = QtGui.QScrollArea(self.joint_mirror_central_widget)
        self.joint_mirror_scroll_area.setWidgetResizable(True)
        self.joint_mirror_scroll_area.setObjectName("joint_mirror_scroll_area")
        self.cluster_mirror_scrollArea_widget_contents = QtGui.QWidget()
        self.cluster_mirror_scrollArea_widget_contents.setGeometry(QtCore.QRect(0, 0, 478, 97))
        self.cluster_mirror_scrollArea_widget_contents.setObjectName("cluster_mirror_scrollArea_widget_contents")
        self.gridLayout = QtGui.QGridLayout(self.cluster_mirror_scrollArea_widget_contents)
        self.gridLayout.setObjectName("gridLayout")

        # MIRROR RADIO BUTTON
        self.mirror_with_same_joint_radio_button = QtGui.QRadioButton(self.cluster_mirror_scrollArea_widget_contents)
        self.mirror_with_same_joint_radio_button.setObjectName("mirror_with_same_joint_radio_button")
        self.mirror_with_same_joint_radio_button.setText('Mirror With Same Joint')
        self.mirror_with_same_joint_radio_button.setChecked(True)
        self.gridLayout.addWidget(self.mirror_with_same_joint_radio_button, 0, 0, 1, 1)

        self.mirror_with_new_joint_radio_button = QtGui.QRadioButton(self.cluster_mirror_scrollArea_widget_contents)
        self.mirror_with_new_joint_radio_button.setObjectName("mirror_with_new_joint_radio_button")
        self.mirror_with_new_joint_radio_button.setText('Mirror With New Joint')
        self.gridLayout.addWidget(self.mirror_with_new_joint_radio_button, 0, 1, 1, 1)

        # AXIS
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

        # BUTTON
        self.create_mirror_button = QtGui.QPushButton(self.cluster_mirror_scrollArea_widget_contents)
        self.create_mirror_button.setObjectName("create_mirror_button")
        self.create_mirror_button.setText('Create Mirror')
        self.create_mirror_button.clicked.connect(self.joint_mirror)
        self.gridLayout.addWidget(self.create_mirror_button, 2, 0, 1, 2)

        # SPACE ITEM
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)

        self.joint_mirror_scroll_area.setWidget(self.cluster_mirror_scrollArea_widget_contents)
        self.verticalLayout.addWidget(self.joint_mirror_scroll_area)
        self.setCentralWidget(self.joint_mirror_central_widget)
        return self

    def joint_mirror(self):
        # get the comboBox value
        self.axis_combo_box_query = str(self.axis_combo_box.currentText())
        if self.mirror_with_same_joint_radio_button.isChecked() == True:
            self.mirror_with_same_joint_query = True
            self.mirror_with_new_joint = False
        elif self.mirror_with_new_joint_radio_button.isChecked() == True:
            self.mirror_with_same_joint_query = False
            self.mirror_with_new_joint = True

        select_joint = cmds.ls(sl=True)
        for each_joint in select_joint:
            skin_cluster_name = cmds.listConnections(each_joint, type='skinCluster')
            skin_cluster_name = list(set(skin_cluster_name))
            for each_skin_cluster in skin_cluster_name:
                self.obj_name = cmds.listConnections(each_skin_cluster, type='mesh')[0]

                self.set_base_move_pos_list(each_joint)

                # cluster influence list
                cluster_vtx_list = []
                clustert_vtx_list_no = []
                for vertexIndex in range(len(self.movePosition)):
                    length = self.movePosition[vertexIndex] - self.base_vtx_list[vertexIndex]
                    if length.x != 0.0000000:
                        clustert_vtx_list_no.append(vertexIndex)
                        cluster_vtx_list.append(self.movePosition[vertexIndex])

                if self.axis_combo_box_query == 'X':
                    axis = [-1, 1, 1]
                    self.point_position = cmds.xform(each_joint, q=1, ws=1, rp=1)
                    self.new_position = [(self.point_position[0] * -1), self.point_position[1], self.point_position[2]]
                elif self.axis_combo_box_query == 'Y':
                    axis = [1, -1, 1]
                    self.point_position = cmds.xform(each_joint, q=1, ws=1, rp=1)
                    self.new_position = [(self.point_position[0]), (self.point_position[1] * -1),
                                         self.point_position[2]]
                elif self.axis_combo_box_query == 'Z':
                    axis = [1, 1, -1]
                    self.point_position = cmds.xform(each_joint, q=1, ws=1, rp=1)
                    self.new_position = [(self.point_position[0]), (self.point_position[1]),
                                         (self.point_position[2] * -1)]
                mitMeshPolygon = om.MItMeshPolygon(self.base_geo_dag_path)
                opp_vtx_list = []
                cluster_wight_value_list = []
                for index in range(len(cluster_vtx_list)):
                    xyz = cluster_vtx_list[index]
                    opp_xyz = om.MPoint(xyz.x * axis[0], xyz.y * axis[1], xyz.z * axis[2])
                    closetPoint, faceID = self.base_mfn_mesh.getClosestPoint(opp_xyz, om.MSpace.kObject)
                    mitMeshPolygon.setIndex(faceID)
                    facevertex_list = mitMeshPolygon.getVertices()
                    mVectorLengthList = []
                    for each_vertex in facevertex_list:
                        oppvertexPosition = self.base_mfn_mesh.getPoint(each_vertex, om.MSpace.kObject)
                        oppMVector = om.MVector(oppvertexPosition)
                        mirrorMVector = om.MVector(opp_xyz)
                        mVectorLength = oppMVector - mirrorMVector
                        length = mVectorLength.length()
                        mVectorLengthList.append(length)
                    closetvertex = min(mVectorLengthList)
                    vertexIndex = mVectorLengthList.index(closetvertex)
                    currentVertexId = facevertex_list[vertexIndex]

                    self.vtx_no = self.obj_name + '.vtx[%s]' % currentVertexId
                    opp_vtx_list.append(self.vtx_no)

                    # now get the cluster value
                    self.vtx_no = self.obj_name + '.vtx[%s]' % clustert_vtx_list_no[index]
                    percent_val = cmds.skinPercent(each_skin_cluster, self.vtx_no, q=True, v=True)[0]
                    cluster_wight_value_list.append(percent_val)

                # base_joint
                base_joint_name = 'Base_Jnt'

                if self.mirror_with_same_joint_query == True:
                    a = 0
                    while a < len(opp_vtx_list):
                        # percent -v 0.692 Soft_Selection_to_Cluster1 pSphere1.vtx[217] ;

                        # cmds.skinPercent(each_skin_cluster,opp_vtx_list[a],tv=(each_joint,cluster_wight_value_list[a]))
                        differnce = 1.0 - cluster_wight_value_list[a]
                        cmds.skinPercent(each_skin_cluster, opp_vtx_list[a],
                                         transformValue=[(each_joint, differnce),
                                                         (base_joint_name, cluster_wight_value_list[a])])
                        a += 1
                else:
                    mirror_joint_name = 'Mirror_' + each_joint
                    cmds.select(cl=True)
                    cmds.joint(n=mirror_joint_name, p=(self.new_position[0],
                                                       self.new_position[1],
                                                       self.new_position[2]))

                    jnt_connection_list = cmds.listConnections(each_skin_cluster, type='joint')
                    for each_joint in jnt_connection_list:
                        cmds.setAttr((each_joint + '.liw'), 1)
                        '''
                        if not each_joint == base_joint_name:
                            cmds.setAttr((each_joint + '.liw'),1)
                        '''
                    cmds.select(mirror_joint_name, self.obj_name)
                    cmds.AddInfluence()
                    a = 0
                    while a < len(opp_vtx_list):
                        # percent -v 0.692 Soft_Selection_to_Cluster1 pSphere1.vtx[217] ;

                        # cmds.skinPercent(each_skin_cluster,opp_vtx_list[a],tv=(each_joint,cluster_wight_value_list[a]))
                        differnce = 1.0 - cluster_wight_value_list[a]
                        cmds.skinPercent(each_skin_cluster, opp_vtx_list[a],
                                         transformValue=[(mirror_joint_name, differnce),
                                                         (base_joint_name, cluster_wight_value_list[a])])
                        a += 1

                self.mFnTransform.setTranslation(self.world, om.MSpace.kWorld)
                print('SucessFully Mirror the Cluster Value')

    def set_base_move_pos_list(self, each_joint):
        self.base_MSelection_list = om.MSelectionList()
        self.base_MSelection_list.add(self.obj_name)
        self.base_geo_dag_path = self.base_MSelection_list.getDagPath(0)

        # get the base vertex position
        self.base_mfn_mesh = om.MFnMesh(self.base_geo_dag_path)
        self.base_vtx_list = self.base_mfn_mesh.getPoints(om.MSpace.kObject)

        # get the move vertex position
        self.clusterMSelection = om.MSelectionList()
        self.clusterMSelection.add(each_joint)
        self.clusterDagPath = self.clusterMSelection.getDagPath(0)
        self.mFnTransform = om.MFnTransform(self.clusterDagPath)
        self.world = self.mFnTransform.translation(om.MSpace.kWorld)
        self.moveWorld = om.MVector(self.world.x + 1, self.world.y, self.world.z)
        self.mFnTransform.setTranslation(self.moveWorld, om.MSpace.kWorld)
        self.movePosition = self.base_mfn_mesh.getPoints(om.MSpace.kObject)

        self.vtx_name = []
        self.vtx_no = []
        self.base_vtx_position = []
        self.move_vtx_position = []
        self.base_vtx_position_x = []
        self.base_vtx_position_y = []
        self.base_vtx_position_z = []
        self.move_vtx_position_x = []
        self.move_vtx_position_y = []
        self.move_vtx_position_z = []
        a = 0
        while a < len(self.base_vtx_list):
            # self.vtx_name
            # pSphere1.vtx[191]
            self.vtx_name_1 = self.obj_name + '.vtx[%s]' % a
            self.vtx_name.append(self.vtx_name_1)
            # self.vtx_no
            self.vtx_no.append(a)
            # self.base_vtx_position
            self.base_vtx_position.append(self.base_vtx_list[a])
            # self.move_vtx_position
            self.move_vtx_position.append(self.movePosition[a])

            # self.base_vtx_position_x
            self.base_vtx_position_x_value = self.base_vtx_list[a].x
            self.base_vtx_position_x.append(self.base_vtx_position_x_value)

            # self.base_vtx_position_y
            self.base_vtx_position_y_value = self.base_vtx_list[a].y
            self.base_vtx_position_y.append(self.base_vtx_position_y_value)

            # self.base_vtx_position_z
            self.base_vtx_position_z_value = self.base_vtx_list[a].z
            self.base_vtx_position_z.append(self.base_vtx_position_z_value)

            # self.base_vtx_position_x
            self.move_vtx_position_x_value = self.movePosition[a].x
            self.move_vtx_position_x.append(self.move_vtx_position_x_value)

            # self.base_vtx_position_y
            self.move_vtx_position_y_value = self.movePosition[a].y
            self.move_vtx_position_y.append(self.move_vtx_position_y_value)

            # self.base_vtx_position_x
            self.move_vtx_position_z_value = self.movePosition[a].z
            self.move_vtx_position_z.append(self.move_vtx_position_z_value)

            a += 1


def main():
    w = MIRROR_JOINT()

    w.show()
