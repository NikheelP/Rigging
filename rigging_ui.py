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

import rigging_tool,auto_rig,skinning
reload(rigging_tool)
reload(auto_rig)
reload(skinning)





class RIGGING(MayaQWidgetDockableMixin, QtGui.QMainWindow):
    def __init__(self,parent=None):
        super(RIGGING, self).__init__(parent=parent)

        #create class
        self.rigging_tool_class = rigging_tool.RIGGING_TOOL()
        self.auto_rig_class = auto_rig.AUTO_RIG()
        self.skinning_class = skinning.SKINNING()



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
        self.rigging_tool_class.ui(self.rigging_tool_tab)
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












