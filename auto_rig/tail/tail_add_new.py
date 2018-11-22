

# basic import  or add command
from PySide import QtCore
from PySide import QtGui
import rig_helper,tail_create
reload(rig_helper)
reload(tail_create)

class ADD_NEW:

    def __init__(self):
        self.rig_helper_class = rig_helper.rig_help()
        self.tail_create_class = tail_create.TAIL_CREATE()

    def ui(self, widget, layout):
        self.tail_grid_layout = QtGui.QGridLayout()
        self.tail_grid_layout.setObjectName("tail_grid_layout")

        # SEGMENT LABEL
        self.tail_segment_label = QtGui.QLabel(widget)
        self.tail_segment_label.setObjectName("tail_segment_label")
        self.tail_segment_label.setText('Tail Segment')
        self.tail_grid_layout.addWidget(self.tail_segment_label, 0, 0, 1, 1)
        # SEGMENT LINE EDIT
        self.tail_segment_line_edit = QtGui.QLineEdit(widget)
        self.tail_segment_line_edit.setObjectName("tail_segment_line_edit")
        self.validator = QtGui.QDoubleValidator()
        self.tail_segment_line_edit.setValidator(self.validator)
        self.tail_segment_line_edit.setText(str(8))
        self.tail_grid_layout.addWidget(self.tail_segment_line_edit, 0, 1, 1, 1)

        # TAIL BUTTON
        self.create_tail_button = QtGui.QPushButton(widget)
        self.create_tail_button.setObjectName("create_tail_button")
        self.create_tail_button.setText('Create Tail')
        self.create_tail_button.clicked.connect(self.tail_def)
        self.tail_grid_layout.addWidget(self.create_tail_button, 1, 0, 1, 2)

        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.tail_grid_layout.addItem(spacerItem, 2, 0, 1, 1)
        layout.addLayout(self.tail_grid_layout)

    def clear(self):
        self.rig_helper_class.clearLayout(self.tail_grid_layout)

    def tail_def(self):
        #get the value
        tail_segment = self.tail_segment_line_edit.text()
        prefix_name = 'Template'
        pos = [0,0,0]

        self.tail_create_class.tail_create(tail_segment=tail_segment,
                                           prefix_name=prefix_name,
                                           pos=pos)



        pass







