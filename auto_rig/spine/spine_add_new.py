

# basic import  or add command
from PySide import QtCore
from PySide import QtGui
import rig_helper,spine_create
reload(rig_helper)
reload(spine_create)

class ADD_NEW:

    def __init__(self):
        self.rig_helper_class = rig_helper.rig_help()
        self.spine_create_class = spine_create.SPINE_CREATE()

    def ui(self, widget, layout):
        self.spine_grid_layout = QtGui.QGridLayout()
        self.spine_grid_layout.setObjectName("spine_grid_layout")

        # TYPE
        self.spine_type_combo_box = QtGui.QComboBox(widget)
        self.spine_type_combo_box.setObjectName("spine_type_combo_box")
        self.spine_type_combo_box.addItem("Human")
        self.spine_type_combo_box.addItem("Animal")
        self.spine_type_combo_box.addItem("Bird")
        self.spine_grid_layout.addWidget(self.spine_type_combo_box, 0, 0, 1, 2)

        # LEFT BREAST LABEL
        self.left_breast_label = QtGui.QLabel(widget)
        self.left_breast_label.setObjectName("left_breast_label")
        self.left_breast_label.setText('Left Breast')
        self.spine_grid_layout.addWidget(self.left_breast_label, 1, 0, 1, 1)
        # LEFT BREAST LINE EDIT
        self.left_breast_line_edit = QtGui.QLineEdit(widget)
        self.left_breast_line_edit.setObjectName("left_breast_line_edit")
        self.validator = QtGui.QDoubleValidator()
        self.left_breast_line_edit.setValidator(self.validator)
        self.left_breast_line_edit.setText(str(1))
        self.spine_grid_layout.addWidget(self.left_breast_line_edit, 1, 1, 1, 1)

        # RIGHT BREAST LABEL
        self.right_breast_label = QtGui.QLabel(widget)
        self.right_breast_label.setObjectName("right_breast_label")
        self.right_breast_label.setText('Right Breast')
        self.spine_grid_layout.addWidget(self.right_breast_label, 2, 0, 1, 1)
        # RIGHT BREAST LINE EDIT
        self.right_breast_line_edit = QtGui.QLineEdit(widget)
        self.right_breast_line_edit.setObjectName("right_breast_line_edit")
        self.right_breast_line_edit.setValidator(self.validator)
        self.right_breast_line_edit.setText(str(1))
        self.spine_grid_layout.addWidget(self.right_breast_line_edit, 2, 1, 1, 1)

        # NO OF THE JOINT LABEL
        self.no_of_joint_label = QtGui.QLabel(widget)
        self.no_of_joint_label.setObjectName("no_of_joint_label")
        self.no_of_joint_label.setText('No Of the Joint')
        self.spine_grid_layout.addWidget(self.no_of_joint_label, 3, 0, 1, 1)
        # NO OF THE JOINT LINE EDIT
        self.no_of_joint_line_edit = QtGui.QLineEdit(widget)
        self.no_of_joint_line_edit.setObjectName("no_of_joint_line_edit")
        self.no_of_joint_line_edit.setValidator(self.validator)
        self.no_of_joint_line_edit.setText(str(8))
        self.spine_grid_layout.addWidget(self.no_of_joint_line_edit, 3, 1, 1, 1)

        # SPINE BUTTON
        self.spine_create_button = QtGui.QPushButton(widget)
        self.spine_create_button.setObjectName("spine_create_button")
        self.spine_create_button.setText('Create Spine')
        self.spine_create_button.clicked.connect(self.new_create)
        self.spine_grid_layout.addWidget(self.spine_create_button, 4, 0, 1, 2)

        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.spine_grid_layout.addItem(spacerItem, 5, 0, 1, 1)
        layout.addLayout(self.spine_grid_layout)

        layout.addLayout(self.spine_grid_layout)

    def clear(self):
        self.rig_helper_class.clearLayout(self.spine_grid_layout)

    def new_create(self):
        left_breast = self.left_breast_line_edit.text()
        right_breast = self.right_breast_line_edit.text()
        no_jnt = self.no_of_joint_line_edit.text()
        spine_type = self.spine_type_combo_box.currentText()
        prefix_name = 'Template'
        val = 0
        if spine_type == 'Human':
            left_brest_pos = [2, 23, 3]
            right_brest_pos = [-2, 23, 3]
        elif spine_type == 'Animal':
            left_brest_pos = [3, 0, 21.969]
            right_brest_pos = [-3, 0, 21.969]

        self.spine_create_class.spine_create(type=spine_type,
                                             right_breast=right_breast,
                                             left_breast=left_breast,
                                             no_jnt=no_jnt,
                                             prefix_name=prefix_name,
                                             left_breast_pos=left_brest_pos,
                                             right_breast_pos=right_brest_pos,
                                             val=val)
















