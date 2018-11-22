

# basic import  or add command
from PySide import QtCore
from PySide import QtGui
import rig_helper
reload(rig_helper)

class HEAD_UPDATE:
    def __init__(self):
        self.rig_helper_class = rig_helper.rig_help()

    def ui(self, widget):
        self.update_widget = widget

        self.head_verticalLayout = QtGui.QVBoxLayout(self.update_widget)
        self.head_verticalLayout.setObjectName("head_verticalLayout")
        self.head_splitter = QtGui.QSplitter(self.update_widget)
        self.head_splitter.setOrientation(QtCore.Qt.Vertical)
        self.head_splitter.setObjectName("head_splitter")

        self.head_name_scroll_area = QtGui.QScrollArea(self.head_splitter)
        self.head_name_scroll_area.setWidgetResizable(True)
        self.head_name_scroll_area.setObjectName("head_name_scroll_area")
        self.head_name_scrollArea_widget_contents = QtGui.QWidget()
        self.head_name_scrollArea_widget_contents.setGeometry(QtCore.QRect(0, 0, 642, 64))
        self.head_name_scrollArea_widget_contents.setObjectName("head_name_scrollArea_widget_contents")
        self.gridLayout_15 = QtGui.QGridLayout(self.head_name_scrollArea_widget_contents)
        self.gridLayout_15.setObjectName("gridLayout_15")

        # get the radio button
        self.attr_list = []
        self.get_update_radio_button()
        self.get_detail_update_def()

        # lock the attr
        self.rig_helper_class.lock_ui_attr(self.attr_list)

    def get_update_radio_button(self):
        pass

    def get_detail_update_def(self):
        self.head_detail_scroll_area = QtGui.QScrollArea(self.head_splitter)
        self.head_detail_scroll_area.setWidgetResizable(True)
        self.head_detail_scroll_area.setObjectName("head_detail_scroll_area")
        self.head_detail_scrollArea_widget_contents = QtGui.QWidget()
        self.head_detail_scrollArea_widget_contents.setGeometry(QtCore.QRect(0, 0, 489, 350))
        self.head_detail_scrollArea_widget_contents.setObjectName("head_detail_scrollArea_widget_contents")

        # UPDATE
        self.head_detail_2_scroll_area = QtGui.QScrollArea(self.head_detail_scrollArea_widget_contents)
        self.head_detail_2_scroll_area.setMinimumSize(QtCore.QSize(0, 207))
        self.head_detail_2_scroll_area.setWidgetResizable(True)
        self.head_detail_2_scroll_area.setObjectName("head_detail_2_scroll_area")
        self.head_detail_2_scrollArea_widget_contents = QtGui.QWidget()
        self.head_detail_2_scrollArea_widget_contents.setGeometry(QtCore.QRect(0, 0, 469, 275))
        self.head_detail_2_scrollArea_widget_contents.setObjectName("head_detail_2_scrollArea_widget_contents")
        self.gridLayout_16 = QtGui.QGridLayout(self.head_detail_2_scrollArea_widget_contents)
        self.gridLayout_16.setObjectName("gridLayout_16")

        self.gridLayout_23 = QtGui.QGridLayout()
        self.gridLayout_23.setObjectName("gridLayout_23")

        # CHARACTER TYPE
        # CHARACTER LABEL
        self.character_type_label = QtGui.QLabel(self.head_detail_2_scrollArea_widget_contents)
        self.character_type_label.setObjectName("character_type_label")
        self.character_type_label.setText('Character Type : ')
        self.attr_list.append(self.character_type_label)
        self.gridLayout_23.addWidget(self.character_type_label, 0, 0, 1, 1)
        # CHARACTER OPTION MENU
        self.character_type_combo_box = QtGui.QComboBox(self.head_detail_2_scrollArea_widget_contents)
        self.character_type_combo_box.setObjectName("character_type_combo_box")
        self.character_type_combo_box.addItem("Human")
        self.character_type_combo_box.addItem("Animal")
        self.character_type_combo_box.addItem("Bird")
        self.character_type_combo_box.setMinimumWidth(363)
        self.attr_list.append(self.character_type_combo_box)
        self.gridLayout_23.addWidget(self.character_type_combo_box, 0, 1, 1, 1)

        # LEFT EYE
        # LEFT EYE LABEL
        self.left_eye_label = QtGui.QLabel(self.head_detail_2_scrollArea_widget_contents)
        self.left_eye_label.setObjectName("left_eye_label")
        self.left_eye_label.setText('Left Eye : ')
        self.attr_list.append(self.left_eye_label)
        self.gridLayout_23.addWidget(self.left_eye_label, 1, 0, 1, 1)
        # LEFT EYE LINE EDIT
        self.left_eye_line_edit = QtGui.QLineEdit(self.head_detail_2_scrollArea_widget_contents)
        self.left_eye_line_edit.setObjectName("left_eye_line_edit")
        self.attr_list.append(self.left_eye_line_edit)
        self.gridLayout_23.addWidget(self.left_eye_line_edit, 1, 1, 1, 1)

        # RIGHT EYE
        # RIGH EYE LABEL
        self.right_eye_label = QtGui.QLabel(self.head_detail_2_scrollArea_widget_contents)
        self.right_eye_label.setObjectName("right_eye_label")
        self.right_eye_label.setText('Right Eye : ')
        self.attr_list.append(self.right_eye_label)
        self.gridLayout_23.addWidget(self.right_eye_label, 2, 0, 1, 1)
        # RIGHT EYE LINE EDIT
        self.right_eye_line_edit = QtGui.QLineEdit(self.head_detail_2_scrollArea_widget_contents)
        self.right_eye_line_edit.setObjectName("right_eye_line_dit")
        self.attr_list.append(self.right_eye_line_edit)
        self.gridLayout_23.addWidget(self.right_eye_line_edit, 2, 1, 1, 1)

        # NAME
        # NAME LABEL
        self.name_label = QtGui.QLabel(self.head_detail_2_scrollArea_widget_contents)
        self.name_label.setObjectName("name_label")
        self.name_label.setText('Name : ')
        self.attr_list.append(self.name_label)
        self.gridLayout_23.addWidget(self.name_label, 3, 0, 1, 1)
        # NAME BUTTON
        self.name_button = QtGui.QPushButton(self.head_detail_2_scrollArea_widget_contents)
        self.name_button.setObjectName("name_button")
        #self.name_button.clicked.connect(self.rename)
        self.attr_list.append(self.name_button)
        self.gridLayout_23.addWidget(self.name_button, 3, 1, 1, 1)

        # PARENT
        # PARENT LABEL
        self.parent_label = QtGui.QLabel(self.head_detail_2_scrollArea_widget_contents)
        self.parent_label.setObjectName("parent_label")
        self.parent_label.setText('Parent : ')
        self.attr_list.append(self.parent_label)
        self.gridLayout_23.addWidget(self.parent_label, 4, 0, 1, 1)
        # PARENT BUTTON
        self.parent_button = QtGui.QPushButton(self.head_detail_2_scrollArea_widget_contents)
        self.parent_button.setObjectName("parent_button")
        #self.parent_button.clicked.connect(self.parent)
        self.attr_list.append(self.parent_button)
        self.gridLayout_23.addWidget(self.parent_button, 4, 1, 1, 1)

        spacerItem10 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_23.addItem(spacerItem10, 5, 0, 1, 1)

        self.gridLayout_16.addLayout(self.gridLayout_23, 0, 0, 1, 1)
        self.head_detail_2_scroll_area.setWidget(self.head_detail_2_scrollArea_widget_contents)

        # UPDATE AND DELETE BUTTON
        self.gridLayout_18 = QtGui.QGridLayout(self.head_detail_scrollArea_widget_contents)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.head_update_scroll_area = QtGui.QScrollArea(self.head_detail_scrollArea_widget_contents)
        self.head_update_scroll_area.setMaximumSize(QtCore.QSize(16777215, 49))
        self.head_update_scroll_area.setWidgetResizable(True)
        self.head_update_scroll_area.setObjectName("head_update_scroll_area")
        self.head_update_scrollArea_widget_contents = QtGui.QWidget()
        self.head_update_scrollArea_widget_contents.setGeometry(QtCore.QRect(0, 0, 469, 47))
        self.head_update_scrollArea_widget_contents.setObjectName("head_update_scrollArea_widget_contents")
        self.gridLayout_17 = QtGui.QGridLayout(self.head_update_scrollArea_widget_contents)
        self.gridLayout_17.setObjectName("gridLayout_17")

        # UPDATE BUTTON
        self.head_update_button = QtGui.QPushButton(self.head_update_scrollArea_widget_contents)
        self.head_update_button.setObjectName("head_update_button")
        self.head_update_button.setText('Update (Head name)')
        #self.head_update_button.clicked.connect(self.head_update_button_def)
        self.attr_list.append(self.head_update_button)
        self.gridLayout_17.addWidget(self.head_update_button, 1, 0, 1, 1)

        # DELETE BUTTON
        self.head_delete_button = QtGui.QPushButton(self.head_update_scrollArea_widget_contents)
        self.head_delete_button.setObjectName("head_delete_button")
        self.head_delete_button.setText('Delete(Head Name)')
        #self.head_delete_button.clicked.connect(self.head_delete_button_def)
        self.attr_list.append(self.head_delete_button)
        self.gridLayout_17.addWidget(self.head_delete_button, 1, 1, 1, 1)

        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_17.addItem(spacerItem9, 0, 0, 1, 1)

        self.head_update_scroll_area.setWidget(self.head_update_scrollArea_widget_contents)
        self.gridLayout_18.addWidget(self.head_update_scroll_area, 1, 0, 1, 1)

        self.gridLayout_18.addWidget(self.head_detail_2_scroll_area, 0, 0, 1, 1)
        self.head_detail_scroll_area.setWidget(self.head_detail_scrollArea_widget_contents)
        self.head_verticalLayout.addWidget(self.head_splitter)

        self.head_detail_scroll_area.setWidget(self.head_detail_scrollArea_widget_contents)
        self.head_verticalLayout.addWidget(self.head_splitter)


