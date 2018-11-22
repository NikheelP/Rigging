

# basic import  or add command
from PySide import QtCore
from PySide import QtGui
import rig_helper
reload(rig_helper)

class ADD_NEW:

    def __init__(self):
        self.rig_helper_class = rig_helper.rig_help()
        pass

    def ui(self, widget, layout):
        self.widget = widget
        self.layout = layout

        self.face_grid_layout = QtGui.QGridLayout()
        self.face_grid_layout.setObjectName("leg_grid_layout")

        # MIRROR CHECKBOX
        self.mirror_check_box = QtGui.QCheckBox(self.widget)
        self.mirror_check_box.setObjectName("mirror_check_box")
        self.mirror_check_box.setText('Mirror')
        self.mirror_check_box.setChecked(True)
        #self.mirror_check_box.stateChanged.connect(self.mirror_status_def)
        self.face_grid_layout.addWidget(self.mirror_check_box, 0, 0, 1, 1)

        # LEFT CHECKBOX
        self.left_check_box = QtGui.QCheckBox(self.widget)
        self.left_check_box.setObjectName("left_check_box")
        self.left_check_box.setText('Left Face')
        self.left_check_box.setChecked(True)
        self.face_grid_layout.addWidget(self.left_check_box, 1, 0, 1, 1)

        # RIGHT CHECKBOX
        self.right_check_box = QtGui.QCheckBox(self.widget)
        self.right_check_box.setObjectName("right_check_box")
        self.right_check_box.setText('Right Face')
        self.right_check_box.setChecked(True)
        self.face_grid_layout.addWidget(self.right_check_box, 1, 1, 1, 1)

        # EYE LABEL
        self.eye_label = QtGui.QLabel(self.widget)
        self.eye_label.setObjectName("eye_label")
        self.eye_label.setText('Eye : ')
        self.face_grid_layout.addWidget(self.eye_label, 2, 0, 1, 1)
        # EYE CHECKBOX
        self.eye_check_box = QtGui.QCheckBox(self.widget)
        self.eye_check_box.setObjectName("eye_check_box")
        self.eye_check_box.setText('Eye')
        #self.eye_check_box.stateChanged.connect(partial(self.face_checkbox_change, 0))
        self.face_grid_layout.addWidget(self.eye_check_box, 3, 0, 1, 1)

        # EYE SIDE CHECKBOX
        self.eye_side_check_box = QtGui.QCheckBox(self.widget)
        self.eye_side_check_box.setObjectName("eye_side_check_box")
        self.eye_side_check_box.setText('Eye Side')
        #self.eye_side_check_box.stateChanged.connect(partial(self.face_checkbox_change, 1))
        self.face_grid_layout.addWidget(self.eye_side_check_box, 3, 1, 1, 1)

        # EYE SIDE 2 CHECKBOX
        self.eye_side_2_check_box = QtGui.QCheckBox(self.widget)
        self.eye_side_2_check_box.setObjectName("eye_side_2_check_box")
        self.eye_side_2_check_box.setText('Eye Side 2')
        #self.eye_side_2_check_box.stateChanged.connect(partial(self.face_checkbox_change, 2))
        self.face_grid_layout.addWidget(self.eye_side_2_check_box, 3, 2, 1, 1)

        # EYE LABEL
        self.no_eye_label = QtGui.QLabel(self.widget)
        self.no_eye_label.setObjectName("no_eye_eye_label")
        self.no_eye_label.setText('No Eye : ')
        self.no_eye_label.hide()
        self.face_grid_layout.addWidget(self.no_eye_label, 4, 0, 1, 1)

        # EYE LINE EIDT
        self.no_eye_line_edit = QtGui.QLineEdit(self.widget)
        self.no_eye_line_edit.setObjectName("no_eye_eye_line_edit")
        self.validator = QtGui.QDoubleValidator()
        self.no_eye_line_edit.setValidator(self.validator)
        self.no_eye_line_edit.setText(str(15))
        self.no_eye_line_edit.hide()
        self.face_grid_layout.addWidget(self.no_eye_line_edit, 4, 1, 1, 3)

        # EYE SIDE LABEL
        self.eye_side_label = QtGui.QLabel(self.widget)
        self.eye_side_label.setObjectName("eye_side_label")
        self.eye_side_label.setText('Eye Side : ')
        self.eye_side_label.hide()
        self.face_grid_layout.addWidget(self.eye_side_label, 5, 0, 1, 1)

        # EYE SIDE LINE EIDT
        self.eye_side_line_edit = QtGui.QLineEdit(self.widget)
        self.eye_side_line_edit.setObjectName("eye_side_line_edit")
        self.eye_side_line_edit.setValidator(self.validator)
        self.eye_side_line_edit.setText(str(12))
        self.eye_side_line_edit.hide()
        self.face_grid_layout.addWidget(self.eye_side_line_edit, 5, 1, 1, 3)

        # EYE SIDE 2 LABEL
        self.eye_side_2_label = QtGui.QLabel(self.widget)
        self.eye_side_2_label.setObjectName("eye_side_2_label")
        self.eye_side_2_label.setText('Eye Side 2 : ')
        self.eye_side_2_label.hide()
        self.face_grid_layout.addWidget(self.eye_side_2_label, 6, 0, 1, 1)

        # EYE SIDE 2 LINE EIDT
        self.eye_side_2_line_edit = QtGui.QLineEdit(self.widget)
        self.eye_side_2_line_edit.setObjectName("eye_side_2_line_edit")
        self.eye_side_2_line_edit.setValidator(self.validator)
        self.eye_side_2_line_edit.setText(str(16))
        self.eye_side_2_line_edit.hide()
        self.face_grid_layout.addWidget(self.eye_side_2_line_edit, 6, 1, 1, 3)

        # NOSE LABEL
        self.nose_label = QtGui.QLabel(self.widget)
        self.nose_label.setObjectName("nose_label")
        self.nose_label.setText('Nose : ')
        self.face_grid_layout.addWidget(self.nose_label, 7, 0, 1, 1)

        # NOSE CHECKBOX
        self.nose_check_box = QtGui.QCheckBox(self.widget)
        self.nose_check_box.setObjectName("nose_check_box")
        self.nose_check_box.setText('Nose')
        self.face_grid_layout.addWidget(self.nose_check_box, 8, 0, 1, 1)

        # NOSE SIDE CHECKBOX
        self.nose_side_check_box = QtGui.QCheckBox(self.widget)
        self.nose_side_check_box.setObjectName("nose_side_check_box")
        self.nose_side_check_box.setText('Nose Side')
        #self.nose_side_check_box.stateChanged.connect(partial(self.face_checkbox_change, 3))
        self.face_grid_layout.addWidget(self.nose_side_check_box, 8, 1, 1, 1)

        # NOSE SIDE LABEL
        self.nose_side_label = QtGui.QLabel(self.widget)
        self.nose_side_label.setObjectName("nose_side_label")
        self.nose_side_label.setText('Nose Side : ')
        self.nose_side_label.hide()
        self.face_grid_layout.addWidget(self.nose_side_label, 9, 0, 1, 1)

        # EYE SIDE LINE EIDT
        self.nose_side_line_edit = QtGui.QLineEdit(self.widget)
        self.nose_side_line_edit.setObjectName("nose_side_line_edit")
        self.nose_side_line_edit.setValidator(self.validator)
        self.nose_side_line_edit.setText(str(3))
        self.nose_side_line_edit.hide()
        self.face_grid_layout.addWidget(self.nose_side_line_edit, 9, 1, 1, 3)

        # COMMON LABEL
        self.common_label = QtGui.QLabel(self.widget)
        self.common_label.setObjectName("common_label")
        self.common_label.setText('Common : ')
        self.face_grid_layout.addWidget(self.common_label, 10, 0, 1, 1)

        # FOR HEAD CHCKBOX
        self.for_head_check_box = QtGui.QCheckBox(self.widget)
        self.for_head_check_box.setObjectName("for_head_check_box")
        self.for_head_check_box.setText('ForHead')
        #self.for_head_check_box.stateChanged.connect(partial(self.face_checkbox_change, 4))
        self.face_grid_layout.addWidget(self.for_head_check_box, 11, 0, 1, 1)

        # NOSE SIDE LABEL
        self.for_head_label = QtGui.QLabel(self.widget)
        self.for_head_label.setObjectName("for_head_label")
        self.for_head_label.setText('ForHead : ')
        self.for_head_label.hide()
        self.face_grid_layout.addWidget(self.for_head_label, 12, 0, 1, 1)

        # EYE SIDE LINE EIDT
        self.for_head_line_edit = QtGui.QLineEdit(self.widget)
        self.for_head_line_edit.setObjectName("for_head_line_edit")
        self.for_head_line_edit.setValidator(self.validator)
        self.for_head_line_edit.setText(str(9))
        self.for_head_line_edit.hide()
        self.face_grid_layout.addWidget(self.for_head_line_edit, 12, 1, 1, 3)

        # MOUTH CHECKBOX
        self.mouth_check_box = QtGui.QCheckBox(self.widget)
        self.mouth_check_box.setObjectName("mouth_check_box")
        self.mouth_check_box.setText('Mouth')
        #self.mouth_check_box.stateChanged.connect(partial(self.face_checkbox_change, 5))
        self.face_grid_layout.addWidget(self.mouth_check_box, 13, 0, 1, 1)

        # MOUTH SIDE CHECKBOX
        self.mouth_side_check_box = QtGui.QCheckBox(self.widget)
        self.mouth_side_check_box.setObjectName("mouth_side_check_box")
        self.mouth_side_check_box.setText('Mouth Side')
        #self.mouth_side_check_box.stateChanged.connect(partial(self.face_checkbox_change, 6))
        self.face_grid_layout.addWidget(self.mouth_side_check_box, 13, 1, 1, 1)

        # MOUTH SIDE 2 CHECKBOX
        self.mouth_side_2_check_box = QtGui.QCheckBox(self.widget)
        self.mouth_side_2_check_box.setObjectName("mouth_side_2_check_box")
        self.mouth_side_2_check_box.setText('Mouth Side 2')
        #self.mouth_side_2_check_box.stateChanged.connect(partial(self.face_checkbox_change, 7))
        self.face_grid_layout.addWidget(self.mouth_side_2_check_box, 13, 2, 1, 1)

        # MOUTH LABEL
        self.mouth_label = QtGui.QLabel(self.widget)
        self.mouth_label.setObjectName("no_eye_eye_label")
        self.mouth_label.setText('Mouth : ')
        self.mouth_label.hide()
        self.face_grid_layout.addWidget(self.mouth_label, 14, 0, 1, 1)

        # MOUTH LINE EIDT
        self.mouth_line_edit = QtGui.QLineEdit(self.widget)
        self.mouth_line_edit.setObjectName("mouth_line_edit")
        self.validator = QtGui.QDoubleValidator()
        self.mouth_line_edit.setValidator(self.validator)
        self.mouth_line_edit.setText(str(22))
        self.mouth_line_edit.hide()
        self.face_grid_layout.addWidget(self.mouth_line_edit, 14, 1, 1, 3)

        # MOUTH SIDE LABEL
        self.mouth_side_label = QtGui.QLabel(self.widget)
        self.mouth_side_label.setObjectName("mouth_side_label")
        self.mouth_side_label.setText('Mouth Side : ')
        self.mouth_side_label.hide()
        self.face_grid_layout.addWidget(self.mouth_side_label, 15, 0, 1, 1)

        # MOUTH SIDE LINE EIDT
        self.mouth_side_line_edit = QtGui.QLineEdit(self.widget)
        self.mouth_side_line_edit.setObjectName("mouth_side_line_edit")
        self.mouth_side_line_edit.setValidator(self.validator)
        self.mouth_side_line_edit.setText(str(20))
        self.mouth_side_line_edit.hide()
        self.face_grid_layout.addWidget(self.mouth_side_line_edit, 15, 1, 1, 3)

        # MOUTH SIDE 2 LABEL
        self.mouth_side_2_label = QtGui.QLabel(self.widget)
        self.mouth_side_2_label.setObjectName("mouth_side_2_label")
        self.mouth_side_2_label.setText('Mouth Side 2 : ')
        self.mouth_side_2_label.hide()
        self.face_grid_layout.addWidget(self.mouth_side_2_label, 16, 0, 1, 1)

        # MOUTH SIDE 2 LINE EIDT
        self.mouth_side_2_line_edit = QtGui.QLineEdit(self.widget)
        self.mouth_side_2_line_edit.setObjectName("mouth_side_2_line_edit")
        self.mouth_side_2_line_edit.setValidator(self.validator)
        self.mouth_side_2_line_edit.setText(str(5))
        self.mouth_side_2_line_edit.hide()
        self.face_grid_layout.addWidget(self.mouth_side_2_line_edit, 16, 1, 1, 3)

        # FACE CENTER CHECKBOX
        self.face_center_check_box = QtGui.QCheckBox(self.widget)
        self.face_center_check_box.setObjectName("face_center_check_box")
        self.face_center_check_box.setText('Face Center')
        #self.face_center_check_box.stateChanged.connect(partial(self.face_checkbox_change, 8))
        self.face_grid_layout.addWidget(self.face_center_check_box, 17, 0, 1, 1)

        # FACE CENTER LABEL
        self.face_center_label = QtGui.QLabel(self.widget)
        self.face_center_label.setObjectName("face_center_label")
        self.face_center_label.setText('Face Center : ')
        self.face_center_label.hide()
        self.face_grid_layout.addWidget(self.face_center_label, 18, 0, 1, 1)

        # FACE CENTER LINE EIDT
        self.face_center_line_edit = QtGui.QLineEdit(self.widget)
        self.face_center_line_edit.setObjectName("face_center_line_edit")
        self.face_center_line_edit.setValidator(self.validator)
        self.face_center_line_edit.setText(str(6))
        self.face_center_line_edit.hide()
        self.face_grid_layout.addWidget(self.face_center_line_edit, 18, 1, 1, 3)

        # FACE BUTTON
        self.face_create_button = QtGui.QPushButton(self.widget)
        self.face_create_button.setObjectName("face_create_button")
        self.face_create_button.setText('Create Face')
        #self.face_create_button.clicked.connect(self.new_face_def)
        self.face_grid_layout.addWidget(self.face_create_button, 19, 0, 1, 4)

        self.spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.face_grid_layout.addItem(self.spacerItem, 20, 0, 1, 1)
        self.layout.addLayout(self.face_grid_layout)

    def clear(self):
        self.rig_helper_class.clearLayout(self.face_grid_layout)