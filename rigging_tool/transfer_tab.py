#GENERAL INFO
_version = 'V001'
_author =  'Nikheel patel'
_email  =  'spark.visualartist@gmail.com'
_last_modify = '10/28/2018'

#IMPORT MODULER
import maya.cmds as cmds
import maya.mel as mel
from PySide import QtCore
from PySide import QtGui
#import sip
import sys
from functools import partial

import trasnlate_objrct_to_cluster,soft_selection_to_cluster,combine_cluster,traslate_to_joint,soft_selection_to_joint,combine_joint
import cluster_to_joint,joint_to_cluster,mirror_cluster,mirror_joint
reload(trasnlate_objrct_to_cluster)
reload(soft_selection_to_cluster)
reload(combine_cluster)
reload(traslate_to_joint)
reload(soft_selection_to_joint)
reload(combine_joint)
reload(cluster_to_joint)
reload(joint_to_cluster)
reload(mirror_cluster)
reload(mirror_joint)

class TRANSFER:
    def __init__(self):
        self.icon_size_x = 100
        self.icon_size_y = 80
        self.button_color_x = 64
        self.button_color_y = 64
        self.button_color_z = 64

    def widget_def(self,widget_name):
        self.horizontalLayout_8 = QtGui.QHBoxLayout(widget_name)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.transfer_scroll_area = QtGui.QScrollArea(widget_name)
        self.transfer_scroll_area.setWidgetResizable(True)
        self.transfer_scroll_area.setObjectName("transfer_scroll_area")
        self.transfer_scrollArea_widget_contents = QtGui.QWidget()
        self.transfer_scrollArea_widget_contents.setGeometry(QtCore.QRect(0, 0, 548, 355))
        self.transfer_scrollArea_widget_contents.setObjectName("transfer_scrollArea_widget_contents")
        self.gridLayout_5 = QtGui.QGridLayout(self.transfer_scrollArea_widget_contents)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.transfer_tool_box = QtGui.QToolBox(self.transfer_scrollArea_widget_contents)
        self.transfer_tool_box.setObjectName("transfer_tool_box")

        # CLUSTER
        self.transfer_cluster = QtGui.QWidget()
        self.transfer_cluster.setGeometry(QtCore.QRect(0, 0, 530, 256))
        self.transfer_cluster.setObjectName("transfer_cluster")
        self.transfer_cluster_def()
        self.transfer_tool_box.addItem(self.transfer_cluster, "Cluster")

        # JOINT
        self.transfer_joint = QtGui.QWidget()
        self.transfer_joint.setGeometry(QtCore.QRect(0, 0, 530, 256))
        self.transfer_joint.setObjectName("transfer_joint")
        self.transfer_joint_def()
        self.transfer_tool_box.addItem(self.transfer_joint, "Joint")

        # INDIVIDUAL TRANSFER
        self.transfer_individual = QtGui.QWidget()
        self.transfer_individual.setGeometry(QtCore.QRect(0, 0, 530, 256))
        self.transfer_individual.setObjectName("transfer_individual")
        self.transfer_individual_def()
        self.transfer_tool_box.addItem(self.transfer_individual, "Individual Transfer")

        self.gridLayout_5.addWidget(self.transfer_tool_box, 0, 0, 1, 1)
        self.transfer_scroll_area.setWidget(self.transfer_scrollArea_widget_contents)
        self.horizontalLayout_8.addWidget(self.transfer_scroll_area)

    def transfer_cluster_def(self):
        self.horizontalLayout_16 = QtGui.QHBoxLayout(self.transfer_cluster)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.transfer_cluster_scroll_area = QtGui.QScrollArea(self.transfer_cluster)
        self.transfer_cluster_scroll_area.setWidgetResizable(True)
        self.transfer_cluster_scroll_area.setObjectName("transfer_cluster_scroll_area")
        self.transfer_cluster_scrollArea_widget_contents = QtGui.QWidget()
        self.transfer_cluster_scrollArea_widget_contents.setGeometry(QtCore.QRect(0, 0, 510, 236))
        self.transfer_cluster_scrollArea_widget_contents.setObjectName("transfer_cluster_scrollArea_widget_contents")
        self.gridLayout_12 = QtGui.QGridLayout(self.transfer_cluster_scrollArea_widget_contents)
        self.gridLayout_12.setObjectName("gridLayout_12")

        # TRANSLATE OBJECT TO CLUSTER
        self.translate_object_to_cluster_button = QtGui.QPushButton(self.transfer_cluster_scrollArea_widget_contents)
        self.translate_object_to_cluster_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Translate Object to Cluster'
        self.translate_object_to_cluster_button.setObjectName(name)
        self.translate_object_to_cluster_button.setText(name)
        self.translate_object_to_cluster_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        button_tool_tip = 'Select all the Transform Deformation and convert into the Cluster'
        self.translate_object_to_cluster_button.setToolTip(
            "<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))
        self.translate_object_to_cluster_button.clicked.connect(traslate_to_joint.main)
        self.gridLayout_12.addWidget(self.translate_object_to_cluster_button, 0, 0, 1, 1)

        # SOFT SELECTION TO CLUSTER
        self.soft_selection_to_cluster_button = QtGui.QPushButton(self.transfer_cluster_scrollArea_widget_contents)
        self.soft_selection_to_cluster_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Soft Selection to Cluster'
        self.soft_selection_to_cluster_button.setObjectName(name)
        self.soft_selection_to_cluster_button.setText(name)
        self.soft_selection_to_cluster_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        button_tool_tip = 'Select soft selection of the object and convert into the Cluster'
        self.soft_selection_to_cluster_button.setToolTip(
            "<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))
        self.soft_selection_to_cluster_button.clicked.connect(soft_selection_to_cluster.SOFT_SELECTION_TO_CLUSTER)
        self.gridLayout_12.addWidget(self.soft_selection_to_cluster_button, 0, 1, 1, 1)

        # COMBINE CLUSTER
        self.combine_cluster_button = QtGui.QPushButton(self.transfer_cluster_scrollArea_widget_contents)
        self.combine_cluster_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Combine Cluster'
        self.combine_cluster_button.setObjectName(name)
        self.combine_cluster_button.setText(name)
        self.combine_cluster_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        button_tool_tip = 'Select n Number of the cluster and combine into one cluster'
        self.combine_cluster_button.setToolTip("<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))
        self.combine_cluster_button.clicked.connect(combine_cluster.COMBINE_CLUSTER)
        self.gridLayout_12.addWidget(self.combine_cluster_button, 0, 2, 1, 1)

        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem4, 1, 1, 1, 1)

        self.transfer_cluster_scroll_area.setWidget(self.transfer_cluster_scrollArea_widget_contents)
        self.horizontalLayout_16.addWidget(self.transfer_cluster_scroll_area)

    def transfer_joint_def(self):
        self.horizontalLayout_17 = QtGui.QHBoxLayout(self.transfer_joint)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.transfer_joint_scroll_area = QtGui.QScrollArea(self.transfer_joint)
        self.transfer_joint_scroll_area.setWidgetResizable(True)
        self.transfer_joint_scroll_area.setObjectName("transfer_joint_scroll_area")
        self.transfer_joint_scrollArea_widget_contents = QtGui.QWidget()
        self.transfer_joint_scrollArea_widget_contents.setGeometry(QtCore.QRect(0, 0, 510, 236))
        self.transfer_joint_scrollArea_widget_contents.setObjectName("transfer_joint_scrollArea_widget_contents")
        self.gridLayout_13 = QtGui.QGridLayout(self.transfer_joint_scrollArea_widget_contents)
        self.gridLayout_13.setObjectName("gridLayout_13")

        # TRANSLATE TO JOINT
        self.transfer_to_joint_button = QtGui.QPushButton(self.transfer_joint_scrollArea_widget_contents)
        self.transfer_to_joint_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Translate to Joint'
        self.transfer_to_joint_button.setObjectName(name)
        self.transfer_to_joint_button.setText(name)
        self.transfer_to_joint_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        button_tool_tip = 'Select All the Transform object and convert into the joint'
        self.transfer_to_joint_button.setToolTip(
            "<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))
        self.transfer_to_joint_button.clicked.connect(traslate_to_joint.main)
        self.gridLayout_13.addWidget(self.transfer_to_joint_button, 0, 0, 1, 1)

        # SOFT SELECTION TO JOINT
        self.soft_selection_to_joint_button = QtGui.QPushButton(self.transfer_joint_scrollArea_widget_contents)
        self.soft_selection_to_joint_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Soft Selection to Joint'
        self.soft_selection_to_joint_button.setObjectName(name)
        self.soft_selection_to_joint_button.setText(name)
        self.soft_selection_to_joint_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        button_tool_tip = 'Select soft selection to object and convert into the joint'
        self.soft_selection_to_joint_button.setToolTip(
            "<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))
        self.soft_selection_to_joint_button.clicked.connect(soft_selection_to_joint.SOFT_SELECTION_TO_JOINT)
        self.gridLayout_13.addWidget(self.soft_selection_to_joint_button, 0, 1, 1, 1)

        # COMBINE TO JOINT
        self.combine_joint_button = QtGui.QPushButton(self.transfer_joint_scrollArea_widget_contents)
        self.combine_joint_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Combine Joint'
        self.combine_joint_button.setObjectName(name)
        self.combine_joint_button.setText(name)
        self.combine_joint_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        button_tool_tip = 'Select two or more than two joint and combine with one joint'
        self.combine_joint_button.setToolTip("<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))
        self.combine_joint_button.clicked.connect(combine_joint.COMBINE_JOINT)
        self.gridLayout_13.addWidget(self.combine_joint_button, 0, 2, 1, 1)

        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_13.addItem(spacerItem4, 1, 1, 1, 1)

        self.transfer_joint_scroll_area.setWidget(self.transfer_joint_scrollArea_widget_contents)
        self.horizontalLayout_17.addWidget(self.transfer_joint_scroll_area)

    def transfer_individual_def(self):
        self.horizontalLayout_18 = QtGui.QHBoxLayout(self.transfer_individual)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.transfer_individual_scroll_area = QtGui.QScrollArea(self.transfer_individual)
        # self.transfer_individual_scroll_area.setWidgetResizable(True)
        self.transfer_individual_scroll_area.setObjectName("transfer_individual_scroll_area")
        self.transfer_individual_scrollArea_widget_contents = QtGui.QWidget()
        self.transfer_individual_scrollArea_widget_contents.setGeometry(QtCore.QRect(0, 0, 510, 236))
        self.transfer_individual_scrollArea_widget_contents.setObjectName(
            "transfer_individual_scrollArea_widget_contents")
        self.gridLayout_14 = QtGui.QGridLayout(self.transfer_individual_scrollArea_widget_contents)
        self.gridLayout_14.setObjectName("gridLayout_14")

        # CLUSTER TO JOINT
        self.cluster_to_joint_button = QtGui.QPushButton(self.transfer_individual_scrollArea_widget_contents)
        self.cluster_to_joint_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Cluster To Joint'
        self.cluster_to_joint_button.setObjectName(name)
        self.cluster_to_joint_button.setText(name)
        self.cluster_to_joint_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        button_tool_tip = 'Convert selected Cluster to the Joint'
        self.cluster_to_joint_button.setToolTip("<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))
        self.cluster_to_joint_button.clicked.connect(cluster_to_joint.CLUSTER_TO_JOINT)
        self.gridLayout_14.addWidget(self.cluster_to_joint_button, 0, 0, 1, 1)

        # JOINT TO CLUSTER
        self.joint_to_cluster_button = QtGui.QPushButton(self.transfer_individual_scrollArea_widget_contents)
        self.joint_to_cluster_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Joint to Cluster'
        self.joint_to_cluster_button.setObjectName(name)
        self.joint_to_cluster_button.setText(name)
        self.joint_to_cluster_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        button_tool_tip = 'Convert selected Joint to the cluster'
        self.joint_to_cluster_button.setToolTip("<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))
        self.joint_to_cluster_button.clicked.connect(joint_to_cluster.JOINT_TO_CLUSTER)
        self.gridLayout_14.addWidget(self.joint_to_cluster_button, 0, 1, 1, 1)

        # Mirror CLUSTER
        self.mirror_cluster_button = QtGui.QPushButton(self.transfer_individual_scrollArea_widget_contents)
        self.mirror_cluster_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Mirror Cluster'
        self.mirror_cluster_button.setObjectName(name)
        self.mirror_cluster_button.setText(name)
        self.mirror_cluster_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        button_tool_tip = 'Mirror Joint'
        self.mirror_cluster_button.setToolTip("<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))
        self.mirror_cluster_button.clicked.connect(mirror_cluster.main)
        self.gridLayout_14.addWidget(self.mirror_cluster_button, 0, 2, 1, 1)

        # Mirror JOINT
        self.mirror_joint_button = QtGui.QPushButton(self.transfer_individual_scrollArea_widget_contents)
        self.mirror_joint_button.setMinimumSize(QtCore.QSize(0, 100))
        name = 'Mirror Joint'
        self.mirror_joint_button.setObjectName(name)
        self.mirror_joint_button.setText(name)
        self.mirror_joint_button.setStyleSheet(
            "background-color: rgb(%s,%s,%s)" % (self.button_color_x, self.button_color_y, self.button_color_z))
        button_tool_tip = 'Mirror Joint'
        self.mirror_joint_button.setToolTip("<font color=white>%s</font>" % button_tool_tip.replace("   ", "<br/>"))
        self.mirror_joint_button.clicked.connect(mirror_joint.main)
        self.gridLayout_14.addWidget(self.mirror_joint_button, 1, 0, 1, 1)

        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_14.addItem(spacerItem4, 2, 1, 1, 1)

        self.transfer_individual_scroll_area.setWidget(self.transfer_individual_scrollArea_widget_contents)
        self.horizontalLayout_18.addWidget(self.transfer_individual_scroll_area)


