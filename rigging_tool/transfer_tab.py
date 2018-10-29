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



class TRANSFER:
    def __init__(self):
        pass

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
        #self.transfer_cluster_def()
        self.transfer_tool_box.addItem(self.transfer_cluster, "Cluster")

        # JOINT
        self.transfer_joint = QtGui.QWidget()
        self.transfer_joint.setGeometry(QtCore.QRect(0, 0, 530, 256))
        self.transfer_joint.setObjectName("transfer_joint")
        #self.transfer_joint_def()
        self.transfer_tool_box.addItem(self.transfer_joint, "Joint")

        # INDIVIDUAL TRANSFER
        self.transfer_individual = QtGui.QWidget()
        self.transfer_individual.setGeometry(QtCore.QRect(0, 0, 530, 256))
        self.transfer_individual.setObjectName("transfer_individual")
        #self.transfer_individual_def()
        self.transfer_tool_box.addItem(self.transfer_individual, "Individual Transfer")

        self.gridLayout_5.addWidget(self.transfer_tool_box, 0, 0, 1, 1)
        self.transfer_scroll_area.setWidget(self.transfer_scrollArea_widget_contents)
        self.horizontalLayout_8.addWidget(self.transfer_scroll_area)









