#GENERAL INFO
_version = 'V001'
_author =  'Nikheel patel'
_email  =  'spark.visualartist@gmail.com'
_last_modify = '10/28/2018'

#Create a Basic Variab;e
rigging_path = 'H:/Script/Git/Rigging'
auto_rig_path = rigging_path + '/auto_rig'
rigging_tool_path = rigging_path + '/rigging_tool'
skinning_tool_path = rigging_path + '/skinning'



#IMPORT MODULER
import maya.cmds as cmds
import maya.mel as mel
from PySide import QtCore
from PySide import QtGui
#import sip
import sys
from functools import partial
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

#append the object
sys.path.append(rigging_path)
sys.path.append(auto_rig_path)
sys.path.append(rigging_tool_path)
sys.path.append(skinning_tool_path)

import rigging_tool,auto_rig,skinning,create_tab,connection_tab,custom_tab,transfer_tab
reload(rigging_tool)
reload(auto_rig)
reload(skinning)
reload(create_tab)
reload(connection_tab)
reload(custom_tab)
reload(transfer_tab)


class RIGGING(MayaQWidgetDockableMixin, QtGui.QMainWindow):
    def __init__(self,parent=None):
        super(RIGGING, self).__init__(parent=parent)

        #create class
        self.rigging_tool_class = rigging_tool.RIGGING_TOOL()
        self.auto_rig_class = auto_rig.AUTO_RIG()
        self.skinning_class = skinning.SKINNING()
        self.create_tab_class = create_tab.CREATE()
        self.connection_tab_class = connection_tab.CONNECTION()
        self.custom_tab_class = custom_tab.CUSTOM()
        self.transfer_tab_class = transfer_tab.TRANSFER()

        #Gui
        self.window_gui()

    def window_gui(self):
        # main window
        self.setWindowTitle('Rigging')

        # central widget
        self.rigging_central_widget = QtGui.QWidget(self)
        self.rigging_central_widget.setObjectName("rigging_central_widget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.rigging_central_widget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # RIGGING TAB WIDGET
        self.rigging_tab_widget = QtGui.QTabWidget(self.rigging_central_widget)
        self.rigging_tab_widget.setObjectName("rigging_tab_widget")

        # RIGGING TOOL TAB
        self.rigging_tool_tab = QtGui.QWidget()
        self.rigging_tool_tab.setObjectName("rigging_tool_tab")
        self.rigging_tool_ui_new(self.rigging_tool_tab)
        self.rigging_tab_widget.addTab(self.rigging_tool_tab, "Rigging Tool")

        # AUTO RIG
        self.auto_rig_tab = QtGui.QWidget()
        self.auto_rig_tab.setObjectName("auto_rig_tab")
        self.auto_rig_class.ui(self.auto_rig_tab)
        self.rigging_tab_widget.addTab(self.auto_rig_tab, "Auto Rig")

        # SKINNING TAB
        self.skinning_tab = QtGui.QWidget()
        self.skinning_tab.setObjectName("skinning_tab")
        self.skinning_class.ui(self.skinning_tab)
        self.rigging_tab_widget.addTab(self.skinning_tab, "Skinning")

        self.horizontalLayout.addWidget(self.rigging_tab_widget)
        self.setCentralWidget(self.rigging_central_widget)

        return self

    def rigging_tool_ui_new(self,widget_name):
        self.horizontalLayout_2 = QtGui.QHBoxLayout(widget_name)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rigging_tool_tab_widget = QtGui.QTabWidget(widget_name)
        self.rigging_tool_tab_widget.setObjectName("rigging_tool_tab_widget")
        self.horizontalLayout_2.addWidget(self.rigging_tool_tab_widget)

        # NEW TAB
        self.rigging_tool_tab = QtGui.QWidget()
        self.rigging_tool_tab.setObjectName("rigging_tool_tab")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.rigging_tool_tab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rigging_tool_tab_widget = QtGui.QTabWidget(self.rigging_tool_tab)
        self.rigging_tool_tab_widget.setObjectName("rigging_tool_tab_widget")

        # CREATE
        self.create_tab = QtGui.QWidget()
        self.create_tab.setObjectName("create_tab")
        self.create_tab_class.widget_def(self.create_tab)
        self.rigging_tool_tab_widget.addTab(self.create_tab, "Create")

        # CONNECTION
        self.connection_tab = QtGui.QWidget()
        self.connection_tab.setObjectName("connection_tab")
        self.connection_tab_class.widget_def(self.connection_tab)
        # self.connection_def()
        self.rigging_tool_tab_widget.addTab(self.connection_tab, "Connection")

        # TRANSFER
        self.transfer_tab = QtGui.QWidget()
        self.transfer_tab.setObjectName("transfer_tab")
        self.transfer_tab_class.widget_def(self.transfer_tab)
        self.rigging_tool_tab_widget.addTab(self.transfer_tab, "Transfer")

        # CUSTOM
        self.custom_tab = QtGui.QWidget()
        self.custom_tab.setObjectName("custom_tab")
        self.custom_tab_class.widget_def(self.custom_tab)
        self.rigging_tool_tab_widget.addTab(self.custom_tab, "Custom")

        self.horizontalLayout_2.addWidget(self.rigging_tool_tab_widget)




    def dockCloseEventTriggered(self):
        self.deleteLater()

    def run(self):
        self.show(dockable=True, floating=False, area='right')



try:
    w.dockCloseEventTriggered()
except:
    pass

def main():

    w = RIGGING()

    w.run()

main()












