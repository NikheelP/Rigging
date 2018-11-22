

# basic import  or add command
from PySide import QtCore
from PySide import QtGui
import rig_helper
reload(rig_helper)

class ADD_NEW:

    def __init__(self):
        self.wing_finger_label = {}
        self.wing_finger_line_edit = {}
        self.rig_helper_class = rig_helper.rig_help()

    def ui(self, widget, layout):
        self.widget = widget
        self.wing_grid_layout = QtGui.QGridLayout()
        self.wing_grid_layout.setObjectName("wing_grid_layout")

        # MIRROR CHECK BOX
        self.wing_mirror_check_box = QtGui.QCheckBox(self.widget)
        self.wing_mirror_check_box.setObjectName("mirror_check_box")
        self.wing_mirror_check_box.setText('Mirror')
        self.wing_mirror_check_box.setChecked(True)
        #self.wing_mirror_check_box.stateChanged.connect(self.mirror_status_def)
        self.wing_grid_layout.addWidget(self.wing_mirror_check_box, 0, 0, 1, 1)

        # LEFT WING CHECK BOX
        self.wing_left_check_box = QtGui.QCheckBox(self.widget)
        self.wing_left_check_box.setObjectName("left_check_box")
        self.wing_left_check_box.setText('Left Wing')
        self.wing_left_check_box.setChecked(True)
        self.wing_grid_layout.addWidget(self.wing_left_check_box, 1, 0, 1, 1)

        # RIGHT WING CHECK BOX
        self.wing_right_check_box = QtGui.QCheckBox(self.widget)
        self.wing_right_check_box.setObjectName("right_check_box")
        self.wing_right_check_box.setText('Righ Wing')
        self.wing_right_check_box.setChecked(True)
        self.wing_grid_layout.addWidget(self.wing_right_check_box, 1, 2, 1, 1)

        # WING TYPE COMBO BOX
        self.wing_type_combo_box = QtGui.QComboBox(self.widget)
        self.wing_type_combo_box.setObjectName("wing_type_combo")
        self.wing_type_combo_box.addItem("Dragon")
        self.wing_type_combo_box.addItem("Bird")
        self.wing_type_combo_box.currentIndexChanged.connect(self.wing_type_combo_box_def)
        self.wing_grid_layout.addWidget(self.wing_type_combo_box, 2, 0, 1, 4)

        # UPPER WING BASE JOINT LABEL
        self.upper_wing_base_jnt_label = QtGui.QLabel(self.widget)
        self.upper_wing_base_jnt_label.setObjectName("upper_wing_base_jnt_label")
        self.upper_wing_base_jnt_label.setText('Upper Wing Base Joint')
        self.wing_grid_layout.addWidget(self.upper_wing_base_jnt_label, 3, 0, 1, 1)
        # UPPER WING BASE JOINT LINE EDIT
        self.upper_wing_base_jnt_line_edit = QtGui.QLineEdit(self.widget)
        self.upper_wing_base_jnt_line_edit.setObjectName("upper_wing_base_jnt_line_edit")
        self.validator = QtGui.QDoubleValidator()
        self.upper_wing_base_jnt_line_edit.setValidator(self.validator)
        self.upper_wing_base_jnt_line_edit.setText(str(6))
        self.wing_grid_layout.addWidget(self.upper_wing_base_jnt_line_edit, 3, 1, 1, 3)

        # LOWER WING BASE JOINT LABEL
        self.lower_wing_base_jnt_label = QtGui.QLabel(self.widget)
        self.lower_wing_base_jnt_label.setObjectName("lower_wing_base_jnt_label")
        self.lower_wing_base_jnt_label.setText('Lower Wing Base Joint')
        self.wing_grid_layout.addWidget(self.lower_wing_base_jnt_label, 4, 0, 1, 1)
        # LOWER WING BASE JOINT LINE EDIT
        self.lower_wing_base_jnt_line_edit = QtGui.QLineEdit(self.widget)
        self.lower_wing_base_jnt_line_edit.setObjectName("lower_wing_base_jnt_line_edit")
        self.lower_wing_base_jnt_line_edit.setValidator(self.validator)
        self.lower_wing_base_jnt_line_edit.setText(str(6))
        self.wing_grid_layout.addWidget(self.lower_wing_base_jnt_line_edit, 4, 1, 1, 3)

        # HAND CHECK BOX
        self.wing_hand_check_box = QtGui.QCheckBox(self.widget)
        self.wing_hand_check_box.setObjectName("hand_check_box")
        self.wing_hand_check_box.setText('Wing Hand')
        #self.wing_hand_check_box.stateChanged.connect(self.wing_hand_check_def)
        self.wing_grid_layout.addWidget(self.wing_hand_check_box, 5, 0, 1, 1)

        # NO OF FINGER LABEL
        self.wing_no_of_finger_label = QtGui.QLabel(self.widget)
        self.wing_no_of_finger_label.setObjectName("no_of_finger_label")
        self.wing_no_of_finger_label.setText('No Of Finger')
        self.wing_no_of_finger_label.setDisabled(True)
        self.wing_grid_layout.addWidget(self.wing_no_of_finger_label, 6, 0, 1, 1)
        # NO OF FINGER LINE EDIT
        self.wing_no_of_finger_line_edit = QtGui.QLineEdit(self.widget)
        self.wing_no_of_finger_line_edit.setObjectName("no_of_finger_line_edit")
        self.wing_no_of_finger_line_edit.setValidator(self.validator)
        self.wing_no_of_finger_line_edit.setDisabled(True)
        #self.wing_no_of_finger_line_edit.textChanged.connect(self.no_finger_line_edit_def)
        self.wing_grid_layout.addWidget(self.wing_no_of_finger_line_edit, 6, 1, 1, 3)

        # CREATE WING
        self.create_wing_button = QtGui.QPushButton(self.widget)
        self.create_wing_button.setObjectName("create_wing_button")
        self.create_wing_button.setText('Create Wing')
        #self.create_wing_button.clicked.connect(self.new_wing_def)
        self.wing_grid_layout.addWidget(self.create_wing_button, 7, 0, 1, 4)

        self.spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.wing_grid_layout.addItem(self.spacerItem, 8, 0, 1, 1)
        layout.addLayout(self.wing_grid_layout)

    def clear(self):
        self.rig_helper_class.clearLayout(self.wing_grid_layout)

    def wing_type_combo_box_def(self):
        self.wing_type_combo_box_query = self.wing_type_combo_box.currentText()
        if self.wing_type_combo_box_query == 'Dragon':
            if self.wing_end_jnt_label:
                self.wing_end_jnt_label.deleteLater()
                self.wing_end_jnt_line_edit.deleteLater()
            self.wing_hand_check_box = QtGui.QCheckBox(self.widget)
            self.wing_hand_check_box.setObjectName("hand_check_box")
            self.wing_hand_check_box.setText('Wing Hand')
            #self.wing_hand_check_box.stateChanged.connect(self.wing_hand_check_def)
            self.wing_grid_layout.addWidget(self.wing_hand_check_box, 5, 0, 1, 1)

            # NO OF FINGER LABEL
            self.wing_no_of_finger_label = QtGui.QLabel(self.widget)
            self.wing_no_of_finger_label.setObjectName("no_of_finger_label")
            self.wing_no_of_finger_label.setText('No Of Finger')
            self.wing_no_of_finger_label.setDisabled(True)
            self.wing_grid_layout.addWidget(self.wing_no_of_finger_label, 6, 0, 1, 1)
            # NO OF FINGER LINE EDIT
            self.wing_no_of_finger_line_edit = QtGui.QLineEdit(self.widget)
            self.wing_no_of_finger_line_edit.setObjectName("no_of_finger_line_edit")
            self.wing_no_of_finger_line_edit.setValidator(self.validator)
            self.wing_no_of_finger_line_edit.setDisabled(True)
            #self.wing_no_of_finger_line_edit.textChanged.connect(self.no_finger_line_edit_def)
            self.wing_grid_layout.addWidget(self.wing_no_of_finger_line_edit, 6, 1, 1, 3)
            a = 0
            while a < len(self.wing_finger_label):
                self.wing_finger_label[a].setDisabled(False)
                self.wing_finger_line_edit[a].setDisabled(False)
                a += 1
        elif self.wing_type_combo_box_query == 'Bird':
            self.wing_hand_check_box.deleteLater()
            self.wing_no_of_finger_label.deleteLater()
            self.wing_no_of_finger_line_edit.deleteLater()
            a = 0
            while a < len(self.wing_finger_label):
                self.wing_finger_label[a].deleteLater()
                self.wing_finger_line_edit[a].deleteLater()
                a += 1

            self.wing_end_jnt_label = QtGui.QLabel(self.widget)
            self.wing_end_jnt_label.setObjectName("Wing_End_label")
            self.wing_end_jnt_label.setText('Wing End')
            self.wing_grid_layout.addWidget(self.wing_end_jnt_label, 5, 0, 1, 3)

            self.wing_end_jnt_line_edit = QtGui.QLineEdit(self.widget)
            self.wing_end_jnt_line_edit.setObjectName("Wing_End_line_edit")
            self.wing_end_jnt_line_edit.setValidator(self.validator)
            self.wing_end_jnt_line_edit.setText(str(6))
            self.wing_grid_layout.addWidget(self.wing_end_jnt_line_edit, 5, 1, 1, 3)


    def wing_def(self):
        mirror = self.wing_mirror_check_box.isChecked()
        left = self.wing_left_check_box.isChecked()
        right = self.wing_right_check_box.isChecked()
        type = self.wing_type_combo_box.currentText()
