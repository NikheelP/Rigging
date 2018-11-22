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
import sys
import rig_helper

class TRANSFORM_OBJECT_TO_CLUSTER(MayaQWidgetDockableMixin, QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(TRANSFORM_OBJECT_TO_CLUSTER, self).__init__(parent=parent)
        self.icon_size_x = 100
        self.icon_size_y = 80
        self.button_color_x = 64
        self.button_color_y = 64
        self.button_color_z = 64

        self.rig_help_class = rig_helper.rig_help()

        self.ui()

    def ui(self):
        self.setObjectName("transform_to_cluster")
        self.setWindowTitle('Transform To Cluster')
        self.resize(246, 455)
        self.setMinimumSize(QtCore.QSize(246, 455))
        self.setMaximumSize(QtCore.QSize(246, 455))
        self.transform_central_widget = QtGui.QWidget(self)
        self.transform_central_widget.setObjectName("transform_central_widget")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.transform_central_widget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        # TRANSFORM LIST
        self.trasnform_list_scroll_area = QtGui.QScrollArea(self.transform_central_widget)
        self.trasnform_list_scroll_area.setMinimumSize(QtCore.QSize(0, 145))
        self.trasnform_list_scroll_area.setWidgetResizable(True)
        self.trasnform_list_scroll_area.setObjectName("trasnform_list_scroll_area")
        self.transform_scrollArea_widget_contents = QtGui.QWidget()
        self.transform_scrollArea_widget_contents.setGeometry(QtCore.QRect(0, 0, 226, 143))
        self.transform_scrollArea_widget_contents.setObjectName("transform_scrollArea_widget_contents")
        self.horizontalLayout = QtGui.QHBoxLayout(self.transform_scrollArea_widget_contents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.transform_list_widget = QtGui.QListWidget(self.transform_scrollArea_widget_contents)
        self.transform_list_widget.setObjectName("transform_list_widget")
        self.horizontalLayout.addWidget(self.transform_list_widget)
        self.trasnform_list_scroll_area.setWidget(self.transform_scrollArea_widget_contents)
        self.verticalLayout_6.addWidget(self.trasnform_list_scroll_area)

        # TRANSFORM BUTTON
        self.transform_group_box = QtGui.QGroupBox(self.transform_central_widget)
        self.transform_group_box.setTitle("")
        self.transform_group_box.setObjectName("transform_group_box")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.transform_group_box)
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.transform_vertical_layout = QtGui.QVBoxLayout()
        self.transform_vertical_layout.setObjectName("transform_vertical_layout")
        self.transform_button = QtGui.QPushButton(self.transform_group_box)
        self.transform_button.setObjectName("transform_button")
        self.transform_button.setText('Transform')
        self.transform_button.clicked.connect(self.trasnform_def)
        self.transform_vertical_layout.addWidget(self.transform_button)
        self.verticalLayout_2.addLayout(self.transform_vertical_layout)
        self.verticalLayout_6.addWidget(self.transform_group_box)

        # SURFACE_LIST
        self.surface_list_scroll_area = QtGui.QScrollArea(self.transform_central_widget)
        self.surface_list_scroll_area.setMinimumSize(QtCore.QSize(0, 159))
        self.surface_list_scroll_area.setWidgetResizable(True)
        self.surface_list_scroll_area.setObjectName("surface_list_scroll_area")
        self.surface_list_scrollArea_widget_contents = QtGui.QWidget()
        self.surface_list_scrollArea_widget_contents.setGeometry(QtCore.QRect(0, 0, 226, 157))
        self.surface_list_scrollArea_widget_contents.setObjectName("surface_list_scrollArea_widget_contents")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.surface_list_scrollArea_widget_contents)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.surface_list_widget = QtGui.QListWidget(self.surface_list_scrollArea_widget_contents)
        self.surface_list_widget.setObjectName("surface_list_widget")
        self.verticalLayout_5.addWidget(self.surface_list_widget)
        self.surface_list_scroll_area.setWidget(self.surface_list_scrollArea_widget_contents)
        self.verticalLayout_6.addWidget(self.surface_list_scroll_area)

        # SURFACE BUTTON
        self.surface_extract_cluster_group_box = QtGui.QGroupBox(self.transform_central_widget)
        self.surface_extract_cluster_group_box.setTitle("")
        self.surface_extract_cluster_group_box.setObjectName("surface_extract_cluster_group_box")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.surface_extract_cluster_group_box)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.surface_extract_cluster_vertical_layout = QtGui.QVBoxLayout()
        self.surface_extract_cluster_vertical_layout.setSpacing(0)
        self.surface_extract_cluster_vertical_layout.setObjectName("surface_extract_cluster_vertical_layout")
        self.surface_button = QtGui.QPushButton(self.surface_extract_cluster_group_box)
        self.surface_button.setObjectName("surface_button")
        self.surface_button.setText('Surface')
        self.surface_button.clicked.connect(self.surface_def)
        self.surface_extract_cluster_vertical_layout.addWidget(self.surface_button)

        self.extract_cluster_button = QtGui.QPushButton(self.surface_extract_cluster_group_box)
        self.extract_cluster_button.setObjectName("extract_cluster_button")
        self.extract_cluster_button.setText('Extract Cluster')
        self.extract_cluster_button.clicked.connect(self.extract_cluster_def)
        self.surface_extract_cluster_vertical_layout.addWidget(self.extract_cluster_button)
        self.verticalLayout_4.addLayout(self.surface_extract_cluster_vertical_layout)
        self.verticalLayout_6.addWidget(self.surface_extract_cluster_group_box)

        self.setCentralWidget(self.transform_central_widget)

        return self

    def trasnform_def(self):
        self.transform_list_widget.clear()
        self.sel_transform_obj = cmds.ls(sl=True)
        for each in self.sel_transform_obj:
            item = QtGui.QListWidgetItem()
            item.setText(each)
            self.transform_list_widget.addItem(item)

    def surface_def(self):
        self.surface_list_widget.clear()
        self.sel_surface_obj = cmds.ls(sl=True)
        for each in self.sel_surface_obj:
            item = QtGui.QListWidgetItem()
            item.setText(each)
            self.surface_list_widget.addItem(item)


    def extract_cluster_def(self):
        self.extract_cluster(self.sel_transform_obj,self.sel_surface_obj)


    def extract_cluster(self,transform_list,surface_list):
        # now extract the cluster
        for each_transform in transform_list:
            jointMSelection = om.MSelectionList()
            jointMSelection.add(each_transform)
            jointDagPath = jointMSelection.getDagPath(0)
            for each_surface in surface_list:
                # set the defaule and move object vertex value
                self.set_base_move_pos_list(each_transform, each_surface)

                # create a cluster and set the position
                self.create_cluster_set_position(each_transform, each_surface)

                for vertexIndex in range(len(self.movePosition)):
                    value = self.movePosition[vertexIndex].x - self.base_vtx_list[vertexIndex].x
                    per = float(value) * (1 / 5.0)
                    vtx_no = each_surface + '.vtx[%s]' % vertexIndex
                    cmds.percent(self.cluster_name, vtx_no, v=per)

    def set_base_move_pos_list(self, each_joint, each_surface):
        self.base_MSelection_list = om.MSelectionList()
        self.base_MSelection_list.add(each_surface)
        self.base_geo_dag_path = self.base_MSelection_list.getDagPath(0)

        # get the base vertex position
        self.base_mfn_mesh = om.MFnMesh(self.base_geo_dag_path)
        self.base_vtx_list = self.base_mfn_mesh.getPoints(om.MSpace.kWorld)

        # get the move vertex position
        self.clusterMSelection = om.MSelectionList()
        self.clusterMSelection.add(each_joint)
        self.clusterDagPath = self.clusterMSelection.getDagPath(0)
        self.mFnTransform = om.MFnTransform(self.clusterDagPath)
        self.world = self.mFnTransform.translation(om.MSpace.kWorld)
        self.moveWorld = om.MVector(self.world.x + 5.0, self.world.y, self.world.z)
        self.mFnTransform.setTranslation(self.moveWorld, om.MSpace.kWorld)
        self.movePosition = self.base_mfn_mesh.getPoints(om.MSpace.kWorld)

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
            self.vtx_name_1 = each_surface + '.vtx[%s]' % a
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
        self.mFnTransform.setTranslation(self.world, om.MSpace.kWorld)

    def create_cluster_set_position(self, each_transform, each_surface):
        cmds.select(each_surface)
        self.cluster_name = each_transform + '_' + each_surface + '_Cluster'
        cmds.cluster(n=self.cluster_name)
        self.cluster_handle_name = self.cluster_name + 'Handle'
        self.cluster_shape_name = cmds.listRelatives(self.cluster_handle_name, s=True)[0]

        self.point_position = cmds.xform(each_transform, q=1, ws=1, rp=1)

        #move the pivot
        self.rig_help_class.pivot_move(self.cluster_handle_name,self.point_position)

        cmds.setAttr((self.cluster_shape_name + '.originX'), self.point_position[0])
        cmds.setAttr((self.cluster_shape_name + '.originY'), self.point_position[1])
        cmds.setAttr((self.cluster_shape_name + '.originZ'), self.point_position[2])


def main():
    w = TRANSFORM_OBJECT_TO_CLUSTER()

    w.show()
