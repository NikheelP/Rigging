

# basic import  or add command
from PySide import QtCore
from PySide import QtGui
import rig_helper
reload(rig_helper)

class FACE_UPDATE:
    def __init__(self):
        self.rig_helper_class = rig_helper.rig_help()

    def ui(self, widget):
        self.update_widget = widget
        self.head_verticalLayout = QtGui.QVBoxLayout(self.update_widget)
        self.head_verticalLayout.setObjectName("head_verticalLayout")
        self.head_splitter = QtGui.QSplitter(self.update_widget)
        self.head_splitter.setOrientation(QtCore.Qt.Vertical)
        self.head_splitter.setObjectName("head_splitter")

        # get the radio button
        self.attr_list = []
        self.get_update_radio_button()
        self.get_detail_update_def()

        # lock the attr
        self.rig_helper_class.lock_ui_attr(self.attr_list)

    def get_update_radio_button(self):
        self.head_name_scroll_area = QtGui.QScrollArea(self.head_splitter)
        self.head_name_scroll_area.setWidgetResizable(True)
        self.head_name_scroll_area.setObjectName("head_name_scroll_area")
        self.head_name_scrollArea_widget_contents = QtGui.QWidget()
        self.head_name_scrollArea_widget_contents.setGeometry(QtCore.QRect(0, 0, 642, 64))
        self.head_name_scrollArea_widget_contents.setObjectName("head_name_scrollArea_widget_contents")
        self.gridLayout_15 = QtGui.QGridLayout(self.head_name_scrollArea_widget_contents)
        self.gridLayout_15.setObjectName("gridLayout_15")

    def get_detail_update_def(self):
        pass