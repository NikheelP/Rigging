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

class TRASNLATE_TO_JOINT(MayaQWidgetDockableMixin, QtGui.QMainWindow):
    def __init__(self,parent=None):
        super(TRASNLATE_TO_JOINT, self).__init__(parent=parent)
        self.ui()

    def ui(self):
        self.setObjectName("transform_to_joint")
        self.setWindowTitle('Transform To Joint')
        self.resize(246, 455)
        self.setMinimumSize(QtCore.QSize(246, 455))
        self.setMaximumSize(QtCore.QSize(246, 455))
        self.transform_central_widget = QtGui.QWidget(self)
        self.transform_central_widget.setObjectName("transform_central_widget")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.transform_central_widget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        #TRANSFORM LIST
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

        #TRANSFORM BUTTON
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

        #SURFACE_LIST
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
        item = QtGui.QListWidgetItem()
        self.surface_list_widget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.surface_list_widget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.surface_list_widget.addItem(item)
        self.verticalLayout_5.addWidget(self.surface_list_widget)
        self.surface_list_scroll_area.setWidget(self.surface_list_scrollArea_widget_contents)
        self.verticalLayout_6.addWidget(self.surface_list_scroll_area)

        #SURFACE BUTTON
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
        self.extract_cluster_button.setObjectName("extract_joint_button")
        self.extract_cluster_button.setText('Extract Joint')
        self.extract_cluster_button.clicked.connect(self.extract_joint)
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

    def extract_joint(self):

        for each_transform in self.sel_transform_obj:
            jointMSelection = OpenMaya.MSelectionList()
            jointMSelection.add(each_transform)
            jointDagPath = jointMSelection.getDagPath(0)
            for each_surface in self.sel_surface_obj:
                shape_name = cmds.listRelatives(each_surface,shapes=True)[0]
                #get the no of the vertex
                meshMSelection = OpenMaya.MSelectionList()
                meshMSelection.add(shape_name)

                #reque
                meshDagPath = meshMSelection.getDagPath(0)
                mFnMesh = OpenMaya.MFnMesh(meshDagPath)
                get_position = mFnMesh.getPoints(OpenMaya.MSpace.kWorld)

                #move the the transform and get the position
                mFnTransform = OpenMaya.MFnTransform(jointDagPath)
                world = mFnTransform.translation(OpenMaya.MSpace.kWorld)
                moveWorld = OpenMaya.MVector(world.x+5,world.y,world.z)
                mFnTransform.setTranslation(moveWorld,OpenMaya.MSpace.kWorld)
                movePosition = mFnMesh.getPoints(OpenMaya.MSpace.kWorld)
                #get the object has the skin cluster or not
                point_position = cmds.xform(each_transform,q=1,ws=1,rp=1)
                skin_cluster_name = mel.eval('findRelatedSkinCluster("%s");' % each_surface)
                base_jnt_name = 'Base_Jnt'
                if skin_cluster_name:
                    if cmds.objExists(base_jnt_name):
                        cmds.select(cl=True)
                        jnt_name = each_transform + '_' + each_surface + '_Jnt'
                        cmds.joint(n=jnt_name,p=(point_position[0],
                                                 point_position[1],
                                                 point_position[2]))
                        skin_cluster_name = mel.eval('findRelatedSkinCluster("%s");' % each_surface)
                        jnt_connection_list = cmds.listConnections( skin_cluster_name, type='joint')
                        for each_joint in jnt_connection_list:
                            if not each_joint == base_jnt_name:
                                cmds.setAttr((each_joint + '.liw'),1)
                        cmds.select(jnt_name,each_surface)
                        cmds.AddInfluence()
                        for vertexIndex in range(len(movePosition)):
                            value = movePosition[vertexIndex].x - get_position[vertexIndex].x
                            per = float(value) * (1 / 5.0)
                            vtx_no = each_surface + '.vtx[%s]' % vertexIndex
                            cmds.skinPercent(skin_cluster_name,vtx_no ,tv=(jnt_name,per))

                    else:
                        print('Object has the skin cluster print convert  all  the joint object to the cluster and '
                          'then transfer to joint to avoide the uneven blend skin value')
                else:
                    #create a base a joint name

                    if not cmds.objExists(base_jnt_name):
                        cmds.select(cl=True)
                        cmds.joint(n=base_jnt_name,p=(0,0,0))
                        cmds.select(cl=True)
                        jnt_name = each_transform + '_' + each_surface + '_Jnt'
                        cmds.joint(n=jnt_name,p=(point_position[0],
                                                 point_position[1],
                                                 point_position[2]))
                        cmds.select(base_jnt_name,jnt_name,each_surface)
                        cmds.SmoothBindSkin()
                        skin_cluster_name = mel.eval('findRelatedSkinCluster("%s");' % each_surface)
                        cmds.skinPercent(skin_cluster_name,(each_surface + '.vtx[0:%s]' % len(get_position)),tv=(base_jnt_name,1))

                        for vertexIndex in range(len(movePosition)):
                            value = movePosition[vertexIndex].x - get_position[vertexIndex].x
                            per = float(value) * (1 / 5.0)
                            vtx_no = each_surface + '.vtx[%s]' % vertexIndex
                            cmds.skinPercent(skin_cluster_name,vtx_no ,tv=(jnt_name,per))
                mFnTransform.setTranslation(world,OpenMaya.MSpace.kWorld)

def main():

    w = TRASNLATE_TO_JOINT()

    w.show()
