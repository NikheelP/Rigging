

import maya.cmds as cmds
import rig_helper
reload(rig_helper)

class WING_CREATE:

    def __init__(self):
        self.rig_helper_class = rig_helper.rig_help()


    def wing_create(self,side,prefix_name,wing_list):
        self.side = side
        self.prefix_name = prefix_name







        self.wing_side = 'L'
        self.prefix_name = 'Template'
        self.base_ctrl_color = 'Blue'
        self.wing_base_pos = [0, 0, 0]
        self.wing_shoulder_pos = [3.978, 3.344, 0]
        self.wing_upper_pos = [10.838, 5.503, 0]
        self.wing_lbow_pos = [39.802, 5.578, -5.31]
        self.wing_hand_pos = [69.438, 6.028, 3.403]
        self.wing_hand_2_pos = [75.194, 5.578, 4.147]
        self.wing_branch_1_1_pos = [80.749, 5.558, 3.007]
        self.wing_branch_1_2_pos = [120.568, 5.442, -3.569]
        self.wing_branch_1_3_pos = [144.519, 5.57, -21.348]
        self.wing_branch_1_4_pos = [158.283, 5.361, -37.462]
        self.wing_branch_2_1_pos = [78.766, 5.802, -1.023]
        self.wing_branch_2_2_pos = [104.89, 5.401, -34.693]
        self.wing_branch_2_3_pos = [109.776, 5.57, -66.382]
        self.wing_branch_2_4_pos = [108.887, 5.421, -92.353]
        self.wing_branch_3_1_pos = [72.002, 5.615, -1.492]
        self.wing_branch_3_2_pos = [68.684, 5.448, -40.505]
        self.wing_branch_3_3_pos = [58.507, 5.289, -67.983]
        self.wing_branch_3_4_pos = [45.556, 5.417, -89.574]
        self.wing_branch_4_1_pos = [39.075, 5.396, -10.858]
        self.wing_branch_4_2_pos = [35.639, 5.341, -31.178]
        self.wing_branch_4_3_pos = [29.772, 5.603, -46.35]
        self.wing_branch_4_4_pos = [23.898, 5.23, -55.344]
        self.finger_pos = [75.194, 5.578, 4.147]
        pass