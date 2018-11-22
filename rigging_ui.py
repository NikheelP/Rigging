#GENERAL INFO
_version = 'V001'
_author =  'Nikheel patel'
_email  =  'spark.visualartist@gmail.com'
_last_modify = '10/28/2018'

#Create a Basic Variab;e



#IMPORT MODULER
import maya.cmds as cmds
import maya.mel as mel
from PySide import QtCore
from PySide import QtGui
#import sip
import sys
import os
from functools import partial
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

rigging_path = 'H:/Script/Git/Rigging'
auto_rig_path = rigging_path + '/auto_rig'
rigging_tool_path = rigging_path + '/rigging_tool'
skinning_tool_path = rigging_path + '/skinning'
ui_path = rigging_path + '/ui'
auto_rig_arm_path = auto_rig_path + '/arm'
auto_rig_controller_path = auto_rig_path + '/controller'
auto_rig_face_path = auto_rig_path + '/face'

auto_rig_head_path = auto_rig_path + '/head'
auto_rig_head_animal_path = auto_rig_head_path + '/animal'
auto_rig_head_human_path = auto_rig_head_path + '/bird'
auto_rig_head_bird_path = auto_rig_head_path + '/human'

auto_rig_leg_path = auto_rig_path + '/leg'
auto_rig_leg_human = auto_rig_leg_path + '/human'

auto_rig_spine_path = auto_rig_path + '/spine'
auto_rig_tail_path = auto_rig_path + '/tail'
auto_rig_wing_path = auto_rig_path + '/wing'
blend_color_path = rigging_tool_path + '/blend_color'

# append the object
list = [rigging_path,auto_rig_path,rigging_tool_path,skinning_tool_path,ui_path,
        auto_rig_arm_path,auto_rig_controller_path,auto_rig_face_path,auto_rig_head_path,auto_rig_head_human_path,auto_rig_head_animal_path,auto_rig_head_bird_path,
        auto_rig_leg_path,auto_rig_spine_path,auto_rig_wing_path,auto_rig_tail_path,auto_rig_leg_human,
        blend_color_path]

for each in list:
    sys.path.append(each)

import auto_rig_ui,skinning_ui,create_tab,connection_tab,custom_tab,transfer_tab
reload(auto_rig_ui)
reload(skinning_ui)
reload(create_tab)
reload(connection_tab)
reload(custom_tab)
reload(transfer_tab)

class RIGGING(MayaQWidgetDockableMixin, QtGui.QMainWindow):
    def __init__(self,parent=None):
        super(RIGGING, self).__init__(parent=parent)

        #create class
        '''
        make a Class from the Import variable
        '''
        #self.rigging_tool_class = rigging_tool.RIGGING_TOOL()
        self.auto_rig_class = auto_rig_ui.AUTO_RIG()
        self.skinning_class = skinning_ui.SKINNING()
        self.create_tab_class = create_tab.CREATE()
        self.connection_tab_class = connection_tab.CONNECTION()
        self.custom_tab_class = custom_tab.CUSTOM()
        self.transfer_tab_class = transfer_tab.TRANSFER()

        #Gui
        '''
        Create a Main Gui
        '''
        self.window_gui()


    def window_gui(self):
        '''
        Window Main Gui
        :return: Window
        '''
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

        #Create  Menu Bar
        self.menu_bar_def(self)

        return self

    def menu_bar_def(self,main_window):
        self.menubar = QtGui.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 745, 21))
        self.menubar.setObjectName("menubar")
        self.file_menu = QtGui.QMenu(self.menubar)
        self.file_menu.setObjectName("file_menu")
        self.help_menu = QtGui.QMenu(self.menubar)
        self.help_menu.setObjectName("help_menu")
        self.edit_menu = QtGui.QMenu(self.menubar)
        self.edit_menu.setObjectName("edit_menu")
        self.setMenuBar(self.menubar)

        self.new_action = QtGui.QAction(self)
        self.new_action.setObjectName("new_action")
        self.new_action.setText('New')
        self.copy_action = QtGui.QAction(self)
        self.copy_action.setObjectName("copy_action")
        self.copy_action.setText('Copy')
        self.help_action = QtGui.QAction(self)
        self.help_action.setObjectName("help_action")
        self.help_action.setText('Help')
        self.save_auto_rig_template_action = QtGui.QAction(self)
        self.save_auto_rig_template_action.setObjectName("save_auto_rig_template_action")
        self.load_auto_rig_template_action = QtGui.QAction(self)
        self.load_auto_rig_template_action.setObjectName("load_auto_rig_template_action")
        self.reload_window_action = QtGui.QAction(self)
        self.reload_window_action.setObjectName("reload_window_action")
        self.file_menu.addAction(self.new_action)
        self.file_menu.setTitle('File')
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.save_auto_rig_template_action)
        self.file_menu.addAction(self.load_auto_rig_template_action)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.reload_window_action)
        self.help_menu.addAction(self.help_action)
        self.help_menu.setTitle('Help')
        self.edit_menu.addAction(self.copy_action)
        self.edit_menu.setTitle('Edit')
        self.menubar.addAction(self.file_menu.menuAction())
        self.menubar.addAction(self.edit_menu.menuAction())
        self.menubar.addAction(self.help_menu.menuAction())

    def rigging_tool_ui_new(self,widget_name):

        '''
        Rigging Tool Ui Function
        :param widget_name: Define the Widget name to append the Gui
        :return:
        '''

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

        # CREATE TAB
        self.create_tab = QtGui.QWidget()
        self.create_tab.setObjectName("create_tab")
        self.create_tab_class.widget_def(self.create_tab)
        self.rigging_tool_tab_widget.addTab(self.create_tab, "Create")

        # CONNECTION TAB
        self.connection_tab = QtGui.QWidget()
        self.connection_tab.setObjectName("connection_tab")
        self.connection_tab_class.widget_def(self.connection_tab)
        # self.connection_def()
        self.rigging_tool_tab_widget.addTab(self.connection_tab, "Connection")

        # TRANSFER TAB
        self.transfer_tab = QtGui.QWidget()
        self.transfer_tab.setObjectName("transfer_tab")
        self.transfer_tab_class.widget_def(self.transfer_tab)
        self.rigging_tool_tab_widget.addTab(self.transfer_tab, "Transfer")

        # CUSTOM TAB
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












