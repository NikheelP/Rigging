

# basic import  or add command
from PySide import QtCore
from PySide import QtGui
import rig_helper,head_create
reload(rig_helper)
reload(head_create)

class ADD_NEW:

    def __init__(self):
        self.rig_helper_class = rig_helper.rig_help()
        self.head_create_class = head_create.HEAD_CREATE()
        pass

    def ui(self, widget, layout):
        self.head_grid_layout = QtGui.QGridLayout()
        self.head_grid_layout.setObjectName("head_grid_layout")

        # LEFT EYE LABEL
        self.left_eye_label = QtGui.QLabel(widget)
        self.left_eye_label.setObjectName("left_eye_label")
        self.left_eye_label.setText('Left Eye')
        self.head_grid_layout.addWidget(self.left_eye_label, 0, 0, 1, 1)
        # LEFT EYE LINE EDIT
        self.left_eye_line_edit = QtGui.QLineEdit(widget)
        self.left_eye_line_edit.setObjectName("left_eye_line_edit")
        self.validator = QtGui.QDoubleValidator()
        self.left_eye_line_edit.setValidator(self.validator)
        self.left_eye_line_edit.setText(str(1))
        self.head_grid_layout.addWidget(self.left_eye_line_edit, 0, 1, 1, 1)

        # RIGHT EYE LABEL
        self.right_eye_label = QtGui.QLabel(widget)
        self.right_eye_label.setObjectName("right_eye_label")
        self.right_eye_label.setText('Right Eye')
        self.head_grid_layout.addWidget(self.right_eye_label, 1, 0, 1, 1)
        # RIGHT EYE LINE EDIT
        self.right_eye_line_edit = QtGui.QLineEdit(widget)
        self.right_eye_line_edit.setObjectName("right_eye_line_edit")
        self.right_eye_line_edit.setValidator(self.validator)
        self.right_eye_line_edit.setText(str(1))
        self.head_grid_layout.addWidget(self.right_eye_line_edit, 1, 1, 1, 1)

        # TYPE COMBO BOX
        self.type_combo_box = QtGui.QComboBox(widget)
        self.type_combo_box.setObjectName("type_combo_box")
        self.type_combo_box.addItem("Human")
        self.type_combo_box.addItem("Animal")
        self.head_grid_layout.addWidget(self.type_combo_box, 2, 0, 1, 2)

        # HEAD CREATE BUTTON
        self.head_create_button = QtGui.QPushButton(widget)
        self.head_create_button.setObjectName("head_create_button")
        self.head_create_button.setText('Create Head')
        self.head_create_button.clicked.connect(self.new_create)
        self.head_grid_layout.addWidget(self.head_create_button, 3, 0, 1, 2)

        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.head_grid_layout.addItem(spacerItem, 4, 0, 1, 1)

        layout.addLayout(self.head_grid_layout)

    def clear(self):
        self.rig_helper_class.clearLayout(self.head_grid_layout)


    def new_create(self):
        #get the data
        left_eye = self.left_eye_line_edit.text()
        right_eye = self.right_eye_line_edit.text()
        type = self.type_combo_box.currentText()
        prefix_name = 'Template'

        if type == 'Animal':
            base_pos = [0, 0, 0]
            neck_pos = [0, 0, 0]
            head_pos = [0, 5.769, 5.631]
            head_top_pos = [0, 12.851, 6.136]
            lower_mouth_pos = [0, 1.386, 15.772]
            upper_mouth_pos = [0, 4.179, 18.565]
            left_ear_pos = [4.022, 10.3, 5.064]
            right_ear_pos = [-3.642, 10.3, 5.064]
            left_eye_pos = [2.026, 8.391, 11.297]
            right_eye_pos = [-2.095, 8.391, 11.297]

            # CREATE CONTROLLER
            # BASE
            base_ctrl_size = [0.5, 0.5, 0.5]
            base_ctrl_rotate = [0, 0, 0]
            base_ctrl_color = 'Yellow'
            base_ctrl_freez_trans = True
            base_ctrl_freez_rotate = True
            base_ctrl_freez_scale = True

            # NECK
            neck_ctrl_size = [1.5, 1.5, 1.5]
            neck_ctrl_rotate = [0, 0, 0]
            neck_ctrl_color = 'Yellow'
            neck_ctrl_freez_trans = True
            neck_ctrl_freez_rotate = True
            neck_ctrl_freez_scale = True

            # HEAD
            head_ctrl_size = [1.5, 1.5, 1.5]
            head_ctrl_rotate = [0, 0, 0]
            head_ctrl_color = 'Yellow'
            head_ctrl_freez_trans = True
            head_ctrl_freez_rotate = True
            head_ctrl_freez_scale = True

            # LOERT MOUTH
            lower_mouth_ctrl_size = [0.5, 0.5, 0.5]
            lower_mouth_ctrl_rotate = [90, 0, 0]
            lower_mouth_ctrl_color = 'Yellow'
            lower_mouth_ctrl_freez_trans = True
            lower_mouth_ctrl_freez_rotate = True
            lower_mouth_ctrl_freez_scale = True

            # UPPER MPUTH
            upper_mouth_ctrl_size = [0.5, 0.5, 0.5]
            upper_mouth_ctrl_rotate = [90, 0, 0]
            upper_mouth_ctrl_color = 'Yellow'
            upper_mouth_ctrl_freez_trans = True
            upper_mouth_ctrl_freez_rotate = True
            upper_mouth_ctrl_freez_scale = True

            # HEAD TOP
            head_top_ctrl_size = [1.5, 1.5, 1.5]
            head_top_ctrl_rotate = [0, 0, 0]
            head_top_ctrl_color = 'Yellow'
            head_top_ctrl_freez_trans = True
            head_top_ctrl_freez_rotate = True
            head_top_ctrl_freez_scale = True

            # LEFT EAR
            left_ear_ctrl_size = [0.5, 0.5, 0.5]
            left_ear_ctrl_rotate = [0, 0, 90]
            left_ear_ctrl_color = 'Blue'
            left_ear_ctrl_freez_trans = True
            left_ear_ctrl_freez_rotate = True
            left_ear_ctrl_freez_scale = True

            # RIGHT EAR
            right_ear_ctrl_size = [0.5, 0.5, 0.5]
            right_ear_ctrl_rotate = [0, 0, 90]
            right_ear_ctrl_color = 'Red'
            right_ear_ctrl_freez_trans = True
            right_ear_ctrl_freez_rotate = True
            right_ear_ctrl_freez_scale = True

        if type == 'Human':
            base_pos = [0, 0, 0]
            neck_pos = [0, 0, 0]
            head_pos = [0, 9.958, 2.056]
            head_top_pos = [0, 31.339, 3.198]
            lower_mouth_pos = [0, 4.665, 13.597]
            upper_mouth_pos = [0, 9.328, 15.108]
            left_ear_pos = [9.42, 14.506, -0.042]
            right_ear_pos = [-8.42, 14.506, -0.042]
            left_eye_pos = [4.999, 15.786, 10.84]
            right_eye_pos = [-5.449, 15.786, 10.84]

            base_ctrl_size = [0.5, 0.5, 0.5]
            base_ctrl_rotate = [0, 0, 0]
            base_ctrl_color = 'Yellow'
            base_ctrl_freez_trans = True
            base_ctrl_freez_rotate = True
            base_ctrl_freez_scale = True

            # NECK
            neck_ctrl_size = [1.5, 1.5, 1.5]
            neck_ctrl_rotate = [0, 0, 0]
            neck_ctrl_color = 'Yellow'
            neck_ctrl_freez_trans = True
            neck_ctrl_freez_rotate = False
            neck_ctrl_freez_scale = True

            # HEAD
            head_ctrl_size = [1.5, 1.5, 1.5]
            head_ctrl_rotate = [0, 0, 0]
            head_ctrl_color = 'Yellow'
            head_ctrl_freez_trans = True
            head_ctrl_freez_rotate = False
            head_ctrl_freez_scale = True

            # LOWER MOUTH
            lower_mouth_ctrl_size = [0.5, 0.5, 0.5]
            lower_mouth_ctrl_rotate = [90, 0, 0]
            lower_mouth_ctrl_color = 'Yellow'
            lower_mouth_ctrl_freez_trans = True
            lower_mouth_ctrl_freez_rotate = True
            lower_mouth_ctrl_freez_scale = True

            # UPPER MOUTH
            upper_mouth_ctrl_size = [0.5, 0.5, 0.5]
            upper_mouth_ctrl_rotate = [90, 0, 0]
            upper_mouth_ctrl_color = 'Yellow'
            upper_mouth_ctrl_freez_trans = True
            upper_mouth_ctrl_freez_rotate = True
            upper_mouth_ctrl_freez_scale = True

            # HEAD TOP
            head_top_ctrl_size = [1.5, 1.5, 1.5]
            head_top_ctrl_rotate = [0, 0, 0]
            head_top_ctrl_color = 'Yellow'
            head_top_ctrl_freez_trans = True
            head_top_ctrl_freez_rotate = True
            head_top_ctrl_freez_scale = True

            # LEFT EAR
            left_ear_ctrl_size = [0.5, 0.5, 0.5]
            left_ear_ctrl_rotate = [0, 0, 90]
            left_ear_ctrl_color = 'Blue'
            left_ear_ctrl_freez_trans = True
            left_ear_ctrl_freez_rotate = True
            left_ear_ctrl_freez_scale = True

            # RIGHT EAR
            right_ear_ctrl_size = [0.5, 0.5, 0.5]
            right_ear_ctrl_rotate = [0, 0, 90]
            right_ear_ctrl_color = 'Red'
            right_ear_ctrl_freez_trans = True
            right_ear_ctrl_freez_rotate = True
            right_ear_ctrl_freez_scale = True

        self.head_create_class.head_create(type=type,
                                           base_pos=base_pos,
                                           neck_pos=neck_pos,
                                           head_pos=head_pos,
                                           head_top_pos=head_top_pos,
                                           lower_mouth_pos=lower_mouth_pos,
                                           upper_mouth_pos=upper_mouth_pos,
                                           left_ear_pos=left_ear_pos,
                                           right_ear_pos=right_ear_pos,
                                           left_eye=left_eye,
                                           left_eye_pos=left_eye_pos,
                                           right_eye=right_eye,
                                           right_eye_pos=right_eye_pos,
                                           prefix_name=prefix_name,
                                           base_ctrl_size=base_ctrl_size,
                                           base_ctrl_rotate=base_ctrl_rotate,
                                           base_ctrl_color=base_ctrl_color,
                                           neck_ctrl_size=neck_ctrl_size,
                                           neck_ctrl_rotate=neck_ctrl_rotate,
                                           neck_ctrl_color=neck_ctrl_color,
                                           head_ctrl_size=head_ctrl_size,
                                           head_ctrl_rotate=head_ctrl_rotate,
                                           head_ctrl_color=head_ctrl_color,
                                           lower_mouth_ctrl_size=lower_mouth_ctrl_size,
                                           lower_mouth_ctrl_rotate=lower_mouth_ctrl_rotate,
                                           lower_mouth_ctrl_color=lower_mouth_ctrl_color,
                                           upper_mouth_ctrl_size=upper_mouth_ctrl_size,
                                           upper_mouth_ctrl_rotate=upper_mouth_ctrl_rotate,
                                           upper_mouth_ctrl_color=upper_mouth_ctrl_color,
                                           head_top_ctrl_size=head_top_ctrl_size,
                                           head_top_ctrl_rotate=head_top_ctrl_rotate,
                                           head_top_ctrl_color=head_top_ctrl_color,
                                           left_ear_ctrl_size=left_ear_ctrl_size,
                                           left_ear_ctrl_rotate=left_ear_ctrl_rotate,
                                           left_ear_ctrl_color=left_ear_ctrl_color,
                                           right_ear_ctrl_size=right_ear_ctrl_size,
                                           right_ear_ctrl_rotate=right_ear_ctrl_rotate,
                                           right_ear_ctrl_color=right_ear_ctrl_color)

