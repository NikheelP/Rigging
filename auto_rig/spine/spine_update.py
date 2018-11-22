

# basic import  or add command
from PySide import QtCore
from PySide import QtGui
import rig_helper
reload(rig_helper)

class SPINE_UPDATE:

    def __init__(self):
        self.rig_helper_class = rig_helper.rig_help()

    def ui(self,widget):
        self.update_widget = widget

        self.verticalLayout = QtGui.QVBoxLayout(self.update_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.common_spitter = QtGui.QSplitter(self.update_widget)
        self.common_spitter.setOrientation(QtCore.Qt.Vertical)
        self.common_spitter.setObjectName("common_spitter")
        self.attr_list = []

        # get the radio button
        self.get_update_radio_button()
        self.get_detail_update_def()

        # lock the attr
        self.rig_helper_class.lock_ui_attr(self.attr_list)

    def get_update_radio_button(self):
        self.spine_name_scroll_area = QtGui.QScrollArea(self.common_spitter)
        self.spine_name_scroll_area.setWidgetResizable(True)
        self.spine_name_scroll_area.setObjectName("spine_name_scroll_area")
        self.spine_name_scrollArea_widget_contents = QtGui.QWidget()
        self.spine_name_scrollArea_widget_contents.setGeometry(QtCore.QRect(0, 0, 642, 64))
        self.spine_name_scrollArea_widget_contents.setObjectName("spine_name_scrollArea_widget_contents")
        self.gridLayout_15 = QtGui.QGridLayout(self.spine_name_scrollArea_widget_contents)
        self.gridLayout_15.setObjectName("gridLayout_15")

    def get_detail_update_def(self):
        self.head_detail_scroll_area = QtGui.QScrollArea(self.common_spitter)
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

        # SPINE NO
        # SPINE NO LABEL
        self.spine_no_label = QtGui.QLabel(self.head_detail_2_scrollArea_widget_contents)
        self.spine_no_label.setObjectName("Spine_No")
        self.spine_no_label.setText('Spine No : ')
        self.attr_list.append(self.spine_no_label)
        self.gridLayout_23.addWidget(self.spine_no_label, 1, 0, 1, 1)
        # SPINE NO LINE EDIT
        self.spine_no_line_edit = QtGui.QLineEdit(self.head_detail_2_scrollArea_widget_contents)
        self.spine_no_line_edit.setObjectName("Spine_No_Line")
        self.validator = QtGui.QDoubleValidator()
        self.spine_no_line_edit.setValidator(self.validator)
        self.attr_list.append(self.spine_no_line_edit)
        self.gridLayout_23.addWidget(self.spine_no_line_edit, 1, 1, 1, 1)

        # LEFT BREAST
        # LEFT BREAST LABEL
        self.left_breast_label = QtGui.QLabel(self.head_detail_2_scrollArea_widget_contents)
        self.left_breast_label.setObjectName("Left_Breast_Label")
        self.left_breast_label.setText('Left Breast : ')
        self.attr_list.append(self.left_breast_label)
        self.gridLayout_23.addWidget(self.left_breast_label, 2, 0, 1, 1)
        # LEFT EYE LINE EDIT
        self.left_breast_line_edit = QtGui.QLineEdit(self.head_detail_2_scrollArea_widget_contents)
        self.left_breast_line_edit.setObjectName("Left_Breast_LineEdit")
        self.left_breast_line_edit.setValidator(self.validator)
        self.attr_list.append(self.left_breast_line_edit)
        self.gridLayout_23.addWidget(self.left_breast_line_edit, 2, 1, 1, 1)

        # RIGHT EYE
        # RIGH EYE LABEL
        self.right_breast_label = QtGui.QLabel(self.head_detail_2_scrollArea_widget_contents)
        self.right_breast_label.setObjectName("Right_Breast_Label")
        self.right_breast_label.setText('Right Breast : ')
        self.attr_list.append(self.right_breast_label)
        self.gridLayout_23.addWidget(self.right_breast_label, 3, 0, 1, 1)
        # LEFT EYE LINE EDIT
        self.right_breast_line_edit = QtGui.QLineEdit(self.head_detail_2_scrollArea_widget_contents)
        self.right_breast_line_edit.setObjectName("Right_Breast_LineEdit")
        self.right_breast_line_edit.setValidator(self.validator)
        self.attr_list.append(self.right_breast_line_edit)
        self.gridLayout_23.addWidget(self.right_breast_line_edit, 3, 1, 1, 1)

        # NAME
        # NAME LABEL
        self.name_label = QtGui.QLabel(self.head_detail_2_scrollArea_widget_contents)
        self.name_label.setObjectName("name_label")
        self.name_label.setText('Name : ')
        self.attr_list.append(self.name_label)
        self.gridLayout_23.addWidget(self.name_label, 4, 0, 1, 1)
        # NAME BUTTON
        self.name_button = QtGui.QPushButton(self.head_detail_2_scrollArea_widget_contents)
        self.name_button.setObjectName("name_button")
        #self.name_button.clicked.connect(self.rename)
        self.attr_list.append(self.name_button)
        self.gridLayout_23.addWidget(self.name_button, 4, 1, 1, 1)

        # PARENT
        # PARENT LABEL
        self.parent_label = QtGui.QLabel(self.head_detail_2_scrollArea_widget_contents)
        self.parent_label.setObjectName("parent_label")
        self.parent_label.setText('Parent : ')
        self.attr_list.append(self.parent_label)
        self.gridLayout_23.addWidget(self.parent_label, 5, 0, 1, 1)
        # PARENT BUTTON
        self.parent_button = QtGui.QPushButton(self.head_detail_2_scrollArea_widget_contents)
        self.parent_button.setObjectName("parent_button")
        #self.parent_button.clicked.connect(self.parent)
        self.attr_list.append(self.parent_button)
        self.gridLayout_23.addWidget(self.parent_button, 5, 1, 1, 1)

        spacerItem10 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_23.addItem(spacerItem10, 6, 0, 1, 1)

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
        self.spine_update_button = QtGui.QPushButton(self.head_update_scrollArea_widget_contents)
        self.spine_update_button.setObjectName("spine_update_button")
        #self.spine_update_button.clicked.connect(self.spine_update_button_def)
        self.spine_update_button.setText('Update (Spine name)')
        self.attr_list.append(self.spine_update_button)
        self.gridLayout_17.addWidget(self.spine_update_button, 1, 0, 1, 1)

        # DELETE BUTTON
        self.spine_delete_button = QtGui.QPushButton(self.head_update_scrollArea_widget_contents)
        self.spine_delete_button.setObjectName("spine_delete_button")
        self.spine_delete_button.setText('Delete(Spine Name)')
        self.attr_list.append(self.spine_delete_button)
        self.gridLayout_17.addWidget(self.spine_delete_button, 1, 1, 1, 1)

        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_17.addItem(spacerItem9, 0, 0, 1, 1)

        self.head_update_scroll_area.setWidget(self.head_update_scrollArea_widget_contents)
        self.gridLayout_18.addWidget(self.head_update_scroll_area, 1, 0, 1, 1)

        self.gridLayout_18.addWidget(self.head_detail_2_scroll_area, 0, 0, 1, 1)
        self.head_detail_scroll_area.setWidget(self.head_detail_scrollArea_widget_contents)
        self.verticalLayout.addWidget(self.common_spitter)

        self.head_detail_scroll_area.setWidget(self.head_detail_scrollArea_widget_contents)
        self.verticalLayout.addWidget(self.common_spitter)
