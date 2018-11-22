import maya.cmds as cmds
import maya.mel as mel

class CONTROLLER:
    '''
    all the controller create
    '''
    def triangle_ctrl(self):
        controller_name = self.get_controller("triangle_ctrl")
        cmds.curve(d=1,p=[(- 1.03923 ,0,0.6),(1.03923,0,0.6),(0,0,-1.2),(-1.03923,0,0.6)],k=[0,1,2,3],n=controller_name)
        self.set_shape(controller_name)
        return controller_name

    def square_ctrl(self):
        controller_name = self.get_controller("Square_ctrl")
        cmds.curve(d=1, p=[(1,0,-1), (-1,0,-1), (-1,0,1), (1,0,1),(1,0,-1)], k=[0, 1, 2, 3,4],n=controller_name)
        # change the shape name
        self.set_shape(controller_name)
        return controller_name

    def angle_ctrl(self):
        controller_name = self.get_controller("angle_ctrl")
        cmds.curve(d=1, p=[(-1,0,-3), (1,0,-3), (1,0,1), (-3,0,1), (-3,0,-1),(-1,0,-1),(-1,0,-3)], k=[0,1,2,3,4,5,6],n=controller_name)
        # change the shape name
        self.set_shape(controller_name)
        return controller_name

    def cross_ctrl(self):
        controller_name = self.get_controller("cross_ctrl")
        cmds.curve(d=1,p=[(0.4,0,-0.4),(0.4,0,-2),(-0.4,0,-2),(-0.4,0,-0.4),(-2,0,-0.4),(-2,0,0.4),(-0.4,0,0.4),(-0.4,0,2),(0.4,0,2),(0.4,0,0.4),(2,0,0.4),(2,0,-0.4),(0.4,0,-0.4)],k=[0,1,2,3,4,5,6,7,8,9,10,11,12],n=controller_name)
        # change the shape name
        self.set_shape(controller_name)
        return controller_name

    def fat_cross_ctrl(self):
        controller_name = self.get_controller("fat_cross_ctrl")
        cmds.curve(d=1,p=[(2,0,1),(2,0,-1),(1,0,-1),(1,0,-2),(-1,0,-2),(-1,0,-1),(-2,0,-1),(-2,0,1),(-1,0,1),(-1,0,2),(1,0,2),(1,0,1 ),(2,0,1 )],k=[0,1,2,3,4,5,6,7,8,9,10,11,12],n=controller_name)
        # change the shape name
        self.set_shape(controller_name)
        return controller_name

    def circle_ctrl(self):
        controller_name = self.get_controller("circle_ctrl")
        cmds.circle(c=(0,0,0),nr=(0,1,0),sw=360,r=1,d=3,ut=0,tol=0.01,s=8,ch=0,n=controller_name)
        # change the shape name
        self.set_shape(controller_name)
        return controller_name

    def arc_270_ctrl(self):
        controller_name = self.get_controller("arc_270_ctrl")
        cmds.curve(d=3, p=[(-0.707107,0,-0.707107 ),(-0.570265,0,-0.843948),(-0.205819,0,-1.040044),(0.405223,0,-0.978634),(0.881027,0,-0.588697),(1.059487,0,0),(0.881027,0,0.588697),(0.405223,0,0.978634),(-0.205819,0,1.040044),(-0.570265,0,0.843948),(-0.707107,0,0.707107)], k=[0,0,0,1,2,3,4,5,6,7,8,8,8], n=controller_name)
        # change the shape name
        self.set_shape(controller_name)
        return controller_name

    def arc_180_ctrl(self):
        controller_name = self.get_controller("arc_180_ctrl")
        cmds.circle(c=(0,0,0),nr=(0,1,0),sw=-180,r=1,d=3,ut=0,tol=0.01,s=8,ch=0,n="arc_180_ctrl")
        self.set_shape(controller_name)
        return controller_name

    def spiral_ctrl(self):
        controller_name = self.get_controller("spiral_ctrl")
        cmds.curve(d=3, p=[(0.474561, 0, -1.241626 ), (-0.171579, 0, -1.214307), (-0.434384, 0, -1.159672),(-1.124061, 0, -0.419971), (-1.169741, 0, 0.305922), (-0.792507, 0, 1.018176),(-0.0412486, 0, 1.262687), (0.915809, 0, 1.006098), (1.258635, 0, 0.364883),(1.032378, 0, -0.461231), (0.352527, 0, -0.810017), (-0.451954, 0, -0.43765),(-0.634527, 0, 0.208919), (-0.0751226, 0, 0.696326), (0.292338, 0, 0.414161),(0.476068, 0, 0.273078)], k=[0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 13, 13], n=controller_name)
        self.set_shape(controller_name)
        return controller_name

    def half_pyramid_ctrl(self):
        controller_name = self.get_controller("half_pyramid_ctrl")
        cmds.curve(d=1, p=[(-1, 0, 0), (0, 0, 1), (0, 1, 0), (-1, 0, 0), (1, 0, 0), (0, 1, 0), (1, 0, 0), (0, 0, 1), (0, 1, 0)],k=[0, 1, 2, 3, 4, 5, 6, 7, 8], n=controller_name)
        self.set_shape(controller_name)
        return controller_name

    def Pyramid_ctrl(self):
        controller_name = self.get_controller("Pyramid_ctrl")
        cmds.curve(d=1, p=[(0, 2, 0), (1, 0, -1), (-1, 0, -1), (0, 2, 0), (-1, 0, 1), (1, 0, 1), (0, 2, 0), (1, 0, -1), (1, 0, 1), (-1, 0, 1), (-1, 0, -1)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], n = controller_name)
        self.set_shape(controller_name)
        return controller_name

    def half_spear_ctrl(self):
        controller_name = self.get_controller("half_spear_ctrl")
        cmds.curve(d=1, p=[(0, 2, 0), (0, 0, 2), (0, 0, -2), (0, 2, 0), (-2, 0, 0), (2, 0, 0), (0, 2, 0)],k=[0, 1, 2, 3, 4, 5, 6], n=controller_name)
        self.set_shape(controller_name)
        return controller_name

    def cube_ctrl(self):
        controller_name = self.get_controller("cube_ctrl")
        cmds.curve(d=1, p=[(0.5, 0.5, 0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (0.5, -0.5, -0.5),(0.5, 0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, 0.5, 0.5), (0.5, 0.5, 0.5), (0.5, -0.5, 0.5),(0.5, -0.5, -0.5), (-0.5, -0.5, -0.5), (-0.5, -0.5, 0.5), (0.5, -0.5, 0.5), (-0.5, -0.5, 0.5),(-0.5, 0.5, 0.5)], k = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], n = controller_name)
        self.set_shape(controller_name)
        return controller_name

    def sphere_ctrl(self):
        controller_name = self.get_controller("sphere_ctrl")
        cmds.curve(d=1, p=[(0, 2, 0), (0, 0, 2), (0, -2, 0), (0, 0, -2), (0, 2, 0), (0, -2, 0), (0, 0, 0), (0, 0, 2), (0, 0, -2), (2, 0, 0), (0, 0, 2), (-2, 0, 0), (0, 0, -2), (0, 0, 2), (0, 0, 0), (-2, 0, 0), (2, 0, 0)],k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], n=controller_name)
        self.set_shape(controller_name)
        return controller_name

    def hexagon_ctrl(self):
        controller_name = self.get_controller("hexagon_ctrl")
        cmds.curve(d=1, p=[(-0.5, 1, 0.866025), (0.5, 1, 0.866025), (0.5, -1, 0.866025), (1, -1, 0), (1, 1, 0),(0.5, 1, -0.866025), (0.5, -1, -0.866025), (-0.5, -1, -0.866026), (-0.5, 1, -0.866026),(-1, 1, -1.5885e-007), (-1, -1, -1.5885), (-0.5, -1, 0.866025), (-0.5, 1, 0.866025),(-1, 1, -1.5885e-007), (-0.5, 1, -0.866026), (0.5, 1, -0.866025), (1, 1, 0),(0.5, 1, 0.866025), (0.5, -1, 0.866025), (-0.5, -1, 0.866025), (-1, -1, -1.5885),(-0.5, -1, -0.866026), (0.5, -1, -0.866025), (1, -1, 0)],k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],n=controller_name)
        self.set_shape(controller_name)
        return controller_name

    def rombus_ctrl(self):
        controller_name = self.get_controller("rombus_ctrl")
        cmds.curve(d=1, p=[(0, 1, 0), (1, 0, 0), (0, 0, 1), (-1, 0, 0), (0, 0, -1), (0, 1, 0), (0, 0, 1), (0, -1, 0), (0, 0, -1), (1, 0, 0), (0, 1, 0), (-1, 0, 0), (0, -1, 0), (1, 0, 0)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],n=controller_name)
        self.set_shape(controller_name)
        return controller_name

    def rombus_two_ctrl(self):
        controller_name = self.get_controller("rombus_two_ctrl")
        cmds.curve(d=1, p=[(0, 0, 2), (0, 1, 0), (0, 0, -2), (0, -1, 0), (-1, 0, 0), (0, 1, 0), (1, 0, 0), (0, -1, 0),(0, 0, 2), (1, 0, 0), (0, 0, -2), (-1, 0, 0), (0, 0, 2)],k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], n=controller_name)
        self.set_shape(controller_name)
        return controller_name

    def rombus_three_ctrl(self):
        controller_name = self.get_controller("rombus_three_ctrl")
        cmds.curve(d=1, p=[(0, 0, 2), (-0.707107, 0.707107, 0), (0, 0, -2), (0.707107, 0.707107, 0), (0, 0, 2),(0.707107, -0.707107, 0), (0, 0, -2), (-0.707107, -0.707107, 0), (0.707107, -0.707107, 0),(0.707107, 0.707107, 0), (-0.707107, 0.707107, 0), (-0.707107, -0.707107, 0), (0, 0, 2)],k = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], n = controller_name)
        self.set_shape(controller_name)
        return controller_name

    def cone_ctrl(self):
        controller_name = self.get_controller("cone_ctrl")
        cmds.curve(d=1,p=[(0.5, -1, 0.866025), (0.5, -1, 0.866025), (0, 1, 0), (0.5, -1, 0.866025), (1, -1, 0), (0, 1, 0),(0.5, -1, -0.866025), (1, -1, 0), (0, 1, 0), (-0.5, -1, -0.866026), (0.5, -1, -0.866025),(0, 1, 0), (-1, -1, -1.5885), (-0.5, -1, -0.866026), (0, 1, 0), (-0.5, -1, 0.866025),(-1, -1, -1.5885)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], n=controller_name)
        self.set_shape(controller_name)
        return controller_name

    def single_thine_ctrl(self):
        controller_name = self.get_controller("single_thine_ctrl")
        cmds.curve(d=1, p=[(0, 0, 1), (0, 0, -1), (-1, 0, 0), (0, 0, -1), (1, 0, 0)], k=[0, 1, 2, 3, 4], n=controller_name)
        self.set_shape(controller_name)
        return controller_name

    def single_normal_ctrl(self):
        controller_name = self.get_controller("single_normal_ctrl")
        cmds.curve(d=1, p=[(0, 0, -1.32), (-0.99, 0, 0), (-0.33, 0, 0), (-0.33, 0, 0.99), (0.33, 0, 0.99), (0.33, 0, 0),(0.99, 0, 0), (0, 0, -1.32)], k=[0, 1, 2, 3, 4, 5, 6, 7], n=controller_name)
        self.set_shape(controller_name)
        return controller_name

    def single_fat_ctrl(self):
        controller_name = self.get_controller("single_fat_ctrl")
        cmds.curve(d=1, p=[(0, 0, -0.99), (-0.66, 0, 0), (-0.33, 0, 0), (-0.33, 0, 0.66), (0.33, 0, 0.66), (0.33, 0, 0),(0.66, 0, 0), (0, 0, -0.99)], k=[0, 1, 2, 3, 4, 5, 6, 7], n=controller_name)
        self.set_shape(controller_name)
        return controller_name

    def double_thine_ctrl(self):
        controller_name = self.get_controller("double_thine_ctrl")
        cmds.curve(d=1,p=[(1, 0, 1), (0, 0, 2), (-1, 0, 1), (0, 0, 2), (0, 0, -2), (-1, 0, -1), (0, 0, -2), (1, 0, -1)],k=[0, 1, 2, 3, 4, 5, 6, 7], n=controller_name)
        self.set_shape(controller_name)
        return controller_name

    def double_normal_ctrl(self):
        controller_name = self.get_controller("double_normal_ctrl")
        cmds.curve(d=1, p=[(0, 0, -2.31), (-0.99, 0, -0.99), (-0.33, 0, -0.99), (-0.33, 0, 0.99), (-0.99, 0, 0.99),(0, 0, 2.31), (0.99, 0, 0.99), (0.33, 0, 0.99), (0.33, 0, -0.99), (0.99, 0, -0.99),(0, 0, -2.31)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], n = controller_name)
        self.set_shape(controller_name)
        return controller_name

    def double_fat_ctrl(self):
        controller_name = self.get_controller("double_fat_ctrl")
        cmds.curve(d=1, p=[(0, 0, -1.35), (-0.66, 0, -0.36), (-0.33, 0, -0.36), (-0.33, 0, 0.36), (-0.66, 0, 0.36),(0, 0, 1.35), (0.66, 0, 0.36), (0.33, 0, 0.36), (0.33, 0, -0.36), (0.66, 0, -0.36),(0, 0, -1.35)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], n=controller_name)
        self.set_shape(controller_name)
        return controller_name

    def four_thin_ctrl(self):
        controller_name = self.get_controller("four_thin_ctrl")
        cmds.curve(d=1, p=[(1.25, 0, -0.5), (1.75, 0, 0), (1.25, 0, 0.5), (1.75, 0, 0), (-1.75, 0, 0), (-1.25, 0, -0.5),(-1.75, 0, 0), (-1.25, 0, 0.5), (-1.75, 0, 0), (0, 0, 0), (0, 0, 1.75), (-0.5, 0, 1.25),(0, 0, 1.75), (0.5, 0, 1.25), (0, 0, 1.75), (0, 0, -1.75), (0.5, 0, -1.25), (0,0 ,-1.75), (-0.5, 0, -1.25), (0, 0, -1.75)], k = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,19], n = controller_name)
        self.set_shape(controller_name)
        return controller_name

    def four_normal_ctrl(self):
        controller_name = self.get_controller("four_normal_ctrl")
        cmds.curve(d=1,p=[(0, 0, -1.98), (-0.495, 0, -1.32), (-0.165, 0, -1.32), (-0.165, 0, -0.165), (-1.32, 0, -0.165),(-1.32, 0, -0.495), (-1.98, 0, 0), (-1.32, 0, 0.495), (-1.32, 0, 0.165), (-0.165, 0, 0.165),(-0.165, 0, 1.32), (-0.495, 0, 1.32), (0, 0, 1.98), (0.495, 0, 1.32), (0.165, 0, 1.32),(0.165, 0, 0.165), (1.32, 0, 0.165), (1.32, 0, 0.495), (1.98, 0, 0), (1.32, 0, -0.495),(1.32, 0, -0.165), (0.165, 0, -0.165), (0.165, 0, -1.32), (0.495, 0, -1.32), (0, 0, -1.98)], k = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24], n = controller_name)
        self.set_shape(controller_name)
        return controller_name

    def four_fat_ctrl(self):
        controller_name = self.get_controller("four_fat_ctrl")
        cmds.curve(d=1, p=[(0, 0, -1.1025), (-0.33, 0, -0.6075), (-0.165, 0, -0.6075), (-0.165, 0, -0.165),(-0.6075, 0, -0.165), (-0.6075, 0, -0.33), (-1.1025, 0, 0), (-0.6075, 0, 0.33),(-0.6075, 0, 0.165), (-0.165, 0, 0.165), (-0.165, 0, 0.6075), (-0.33, 0, 0.6075),(0, 0, 1.1025), (0.33, 0, 0.6075), (0.165, 0, 0.6075), (0.165, 0, 0.165), (0.6075, 0, 0.165),(0.6075, 0, 0.33), (1.1025, 0, 0), (0.6075, 0, -0.33), (0.6075, 0, -0.165),(0.165, 0, -0.165), (0.165, 0, -0.6075), (0.33, 0, -0.6075), (0, 0, -1.1025)], k = [0, 1, 2,3, 4, 5,6, 7, 8,9, 10, 11,12, 13,14, 15,16, 17,18, 19,20, 21,22, 23,24], n = controller_name)
        self.set_shape(controller_name)
        return controller_name

    def eight_ctrl(self):
        controller_name = self.get_controller("eight_ctrl")
        cmds.curve(d=1, p=[(-1.8975, 0, 0), (-1.4025, 0, 0.37125), (-1.4025, 0, 0.12375), (-0.380966, 0, 0.157801),(-1.079222, 0, 0.904213), (-1.254231, 0, 0.729204), (-1.341735, 0, 1.341735),(-0.729204, 0, 1.254231), (-0.904213, 0, 1.079222), (-0.157801, 0, 0.380966),(-0.12375, 0, 1.4025), (-0.37125, 0, 1.4025), (0, 0, 1.8975), (0.37125, 0, 1.4025),(0.12375, 0, 1.4025), (0.157801, 0, 0.380966), (0.904213, 0, 1.079222),(0.729204, 0, 1.254231), (1.341735, 0, 1.341735), (1.254231, 0, 0.729204),(1.079222, 0, 0.904213), (0.380966, 0, 0.157801), (1.4025, 0, 0.12375), (1.4025, 0, 0.37125),(1.8975,0,0), (1.4025, 0, -0.37125), (1.4025, 0, -0.12375), (0.380966, 0, -0.157801), (1.079222, 0, -0.904213), (1.254231, 0, -0.729204), (1.341735, 0, -1.341735), (0.729204, 0, -1.254231), (0.904213, 0, -1.079222), (0.157801, 0, -0.380966), (0.12375, 0, -1.4025), (0.37125, 0, -1.4025), (0, 0, -1.8975), (-0.37125, 0, -1.4025), (-0.12375, 0, -1.4025), (-0.157801, 0, -0.380966), (-0.904213, 0, -1.079222), (-0.729204, 0, -1.254231), (-1.341735, 0, -1.341735), (-1.254231, 0, -0.729204), (-1.079222, 0, -0.904213), (-0.380966, 0, -0.157801), (-1.4025, 0, -0.12375), (-1.4025, 0, -0.37125), (-1.8975, 0, 0)], k = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46,47, 48], n = controller_name)
        self.set_shape(controller_name)
        return controller_name

    def ninty_thin_ctrl(self):
        controller_name = self.get_controller("ninty_thin_ctrl")
        cmds.curve(d=1,p=[(-1.026019, 0, 0), (-0.947961, 0, 0.392646), (-0.725413, 0, 0.725516), (-0.393028, 0, 0.947932),(-0.13006, 0, 1), (0.0107043, 0, 1.001418), (-0.339542, 0, 0.5442), (0.0107043, 0, 1.001418),(-0.446514, 0, 1.351664)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8], n=controller_name)
        self.set_shape(controller_name)
        return controller_name

    def ninty_normal_ctrl(self):
        controller_name = self.get_controller("ninty_normal_ctrl")
        cmds.curve(d=1, p=[(-0.251045, 0, 1.015808), (-0.761834, 0, 0.979696), (-0.486547, 0, 0.930468),(-0.570736, 0, 0.886448), (-0.72786, 0, 0.774834), (-0.909301, 0, 0.550655),(-1.023899, 0, 0.285854), (-1.063053, 0, 9.80765e-009), (-0.961797, 0, 8.87346e-009),(-0.926399, 0, 0.258619), (-0.822676, 0, 0.498232), (-0.658578, 0, 0.701014),(-0.516355, 0, 0.802034), (-0.440202, 0, 0.841857), (-0.498915, 0, 0.567734), (-0.251045,01.015808)], k = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], n =controller_name)
        self.set_shape(controller_name)
        return controller_name

    def ninty_fat_ctrl(self):
        controller_name = self.get_controller("ninty_fat_ctrl")
        cmds.curve(d=1, p=[(-0.923366, 0, 0), (-1.128672, 0, 0), (-1.042702, 0, 0.431934), (-0.798049, 0, 0.798033),(-0.560906, 0, 0.946236), (-0.975917, 0, 1.036319), (-0.124602, 0, 1.096506),(-0.537718, 0, 0.349716), (-0.440781, 0, 0.788659), (-0.652776, 0, 0.652998),(-0.853221, 0, 0.353358), (-0.923366, 0, 0)],k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], n = controller_name)
        self.set_shape(controller_name)
        return controller_name

    def oneeighty_thin_ctrl(self):
        controller_name = self.get_controller("oneeighty_thin_ctrl")
        cmds.curve(d=1, p=[(-0.446514, 0, -1.351664), (0.0107043, 0, -1.001418), (-0.339542, 0, -0.5442),(0.0107043, 0, -1.001418), (-0.13006, 0, -1), (-0.393028, 0, -0.947932),(-0.725413, 0, -0.725516), (-0.947961, 0, -0.392646), (-1.026019, 0, 0),(-0.947961, 0, 0.392646), (-0.725413, 0, 0.725516), (-0.393028, 0, 0.947932),(-0.13006, 0, 1), (0, 0, 1), (-0.339542, 0, 0.5442), (0, 0, 1), (-0.446514, 0, 1.351664)],k = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], n = controller_name)
        self.set_shape(controller_name)
        return controller_name

    def oneeight_normal_ctrl(self):
        controller_name = self.get_controller("oneeight_normal_ctrl")
        cmds.curve(d=1, p=[(-0.251045, 0, -1.015808), (-0.761834, 0, -0.979696), (-0.486547, 0, -0.930468),(-0.570736, 0, -0.886448), (-0.72786, 0, -0.774834), (-0.909301, 0, -0.550655),(-1.023899, 0, -0.285854), (-1.063053, 0, 9.80765e-009), (-1.023899, 0, 0.285854),(-0.909301, 0, 0.550655), (-0.72786, 0, 0.774834), (-0.570736, 0, 0.886448),(-0.486547, 0, 0.930468), (-0.761834, 0, 0.979696), (-0.251045, 0, 1.015808),(-0.498915, 0, 0.567734), (-0.440202, 0, 0.841857), (-0.516355, 0, 0.802034),(-0.658578, 0, 0.701014), (-0.822676, 0, 0.498232), (-0.926399, 0, 0.258619),(-0.961797, 0, 8.87346e-009), (-0.926399, 0, -0.258619), (-0.822676, 0, -0.498232),(-0.658578, 0, -0.701014), (-0.516355, 0, -0.802034), (-0.440202, 0, -0.841857),(-0.498915, 0, -0.567734), (-0.251045, 0, -1.015808)],k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,27, 28], n=controller_name)
        self.set_shape(controller_name)
        return controller_name

    def oneeight_fat_ctrl(self):
        controller_name = self.get_controller("oneeight_fat_ctrl")
        cmds.curve(d=1, p=[(-0.124602, 0, -1.096506), (-0.975917, 0, -1.036319), (-0.559059, 0, -0.944259),(-0.798049, 0, -0.798033), (-1.042702, 0, -0.431934), (-1.128672, 0, 0),(-1.042702, 0, 0.431934), (-0.798049, 0, 0.798033), (-0.560906, 0, 0.946236),(-0.975917, 0, 1.036319), (-0.124602, 0, 1.096506), (-0.537718, 0, 0.349716),(-0.440781, 0, 0.788659), (-0.652776, 0, 0.652998), (-0.853221, 0, 0.353358),(-0.923366, 0, 0), (-0.853221, 0, -0.353358), (-0.652776, 0, -0.652998),(-0.439199, 0, -0.785581), (-0.537718, 0, -0.349716), (-0.124602, 0, -1.096506)], k = [0, 1,2, 3,4, 5,6, 7,8, 9,10, 11,12, 13,14, 15,16, 17,18, 19,20], n =controller_name)
        self.set_shape(controller_name)
        return controller_name

    def transform_ctrl(self):
        controller_name = self.get_controller("transform_ctrl")
        circleHelper = cmds.circle(c=(0, 0, 0), nr=(0, 1, 0), sw=360, r=1.5, d=3, ut=0, tol=0.01, s=8, ch=0,n=controller_name)
        cmds.curve(d=1, p=[(1.75625, 0, 0.115973), (1.75625, 0, -0.170979),(2.114939, 0, -0.170979),(2.114939, 0, -0.314454), (2.473628, 0, -0.0275029), (2.114939, 0, 0.259448),(2.114939, 0, 0.115973), (1.75625, 0, 0.115973)],k=[0, 1, 2, 3, 4, 5, 6, 7], n = "helperArrow1")
        cmds.curve(d=1, p=[(0.143476, 0, -1.783753), (0.143476, 0, -2.142442), (0.286951, 0, -2.142442),(0, 0, -2.501131), (-0.286951, 0, -2.142442), (-0.143476, 0, -2.142442),(-0.143476, 0, -1.783753), (0.143476, 0, -1.783753)], k=[0, 1, 2, 3, 4, 5, 6,7], n = "helperArrow2")
        cmds.curve(d=1, p=[(-1.75625, 0, -0.170979), (-2.114939, 0, -0.170979), (-2.114939, 0, -0.314454),(-2.473628, 0, -0.0275029), (-2.114939, 0, 0.259448), (-2.114939, 0, 0.115973),(-1.75625, 0, 0.115973), (-1.75625, 0, -0.170979)], k=[0, 1, 2, 3, 4, 5, 6, 7],n="helperArrow3")
        cmds.curve(d=1, p=[(-0.143476, 0, 1.728747), (-0.143476, 0, 2.087436), (-0.286951, 0, 2.087436),(0, 0, 2.446125), (0.286951, 0, 2.087436), (0.143476, 0, 2.087436),(0.143476, 0, 1.728747), (-0.143476, 0, 1.728747)], k=[0, 1, 2, 3, 4, 5, 6, 7],n="helperArrow4")
        cmds.select("helperArrow1","helperArrow2","helperArrow3","helperArrow4")
        cmds.pickWalk(d='down')
        cmds.select(controller_name,add=True)
        cmds.parent(r=True,s=True)
        cmds.delete("helperArrow1", "helperArrow2", "helperArrow3", "helperArrow4")
        cmds.select(controller_name)
        self.set_shape(controller_name)
        return controller_name

    def footprint_ctrl(self):
        controller_name = self.get_controller("footprint_ctrl")
        cmds.curve(d=1, p=[(-0.081122, 0, -1.11758), (0.390719, 0, -0.921584), (0.514124, 0, -0.616704),(0.412496, 0, 0.0293557), (0.86256, 0, 0.552008), (0.920632, 0, 1.161772),(0.775452, 0, 1.669908), (0.38346, 0, 2.011088), (-0.131936, 0, 2.330484),(-0.552964, 0, 2.308708), (-0.654588, 0, 1.691688), (-0.57474, 0, 0.63912),(-0.364226, 0, 0.109206), (-0.531184, 0, -0.39893), (-0.465852, 0, -0.841736),(-0.081122, 0, -1.11758)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],n=controller_name)
        self.set_shape(controller_name)
        return controller_name

    def hand_ctrl(self):
        controller_name = self.get_controller("hand_ctrl")
        CONTROLLERS_1 = cmds.curve(d=1, p=[(-0.718223, 0, -0.925311), (-0.718223, 0, 0.462656),(-0.462656, 0, 0.925311),(0, 0, 0.925311), (0.170548, 0, 0.873409), (0.341096, 0, 0.925311),(0.925311, 0, 0.925311), (0.925311, 0, 0), (0.718223, 0, -0.462656),(0.718223, 0, -0.925311), (0.457051, 0, -1.156639),(-0.462656, 0, -1.156639), (-0.718223, 0, -0.925311)],k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], n=controller_name)
        CONTROLLERS_2 = cmds.curve(d=1,p=[(-0.718223, 0, -0.925311), (-0.718223, 0, -2.544605), (-0.457051, 0, -2.544605),(-0.462656, 0, -1.156639)], k=[0, 1, 2, 3], n="controler_2")
        CONTROLLERS_3 = cmds.curve(d=1,p=[(-0.326465, 0, -1.156639), (-0.326465, 0, -2.775933), (-0.065293, 0, -2.775933),(-0.065293, 0, -1.156639)], k=[0, 1, 2, 3], n="controler_3")
        CONTROLLERS_4 = cmds.curve(d=1, p=[(0.065293, 0, -1.156639), (0.065293, 0, -3.007261), (0.326465, 0, -3.007261),(0.326465, 0, -1.156639)], k=[0, 1, 2, 3], n="controler_4")
        CONTROLLERS_5 = cmds.curve(d=1, p=[(0.457051, 0, -1.156639), (0.457051, 0, -2.775933), (0.718223, 0, -2.775933),(0.718223, 0, -0.925311)], k=[0, 1, 2, 3], n="controler_5")
        CONTROLLERS_6 = cmds.curve(d=1, p=[(0.925311, 0, 0), (1.156639, 0, -0.231328), (1.387967, 0, -0.693983),(1.619294, 0, -0.462656), (1.387967, 0, 0.231328), (0.925311, 0, 0.925311)],k=[0, 1, 2, 3, 4, 5], n = "controler_6")
        cmds.select("controler_2","controler_3","controler_4","controler_5","controler_6")
        cmds.pickWalk(d="down")
        cmds.select(controller_name,add=True)
        cmds.parent(r=True,s=True)
        cmds.delete("controler_2", "controler_3", "controler_4", "controler_5", "controler_6")
        self.set_shape(controller_name)
        return controller_name

    def vision(self):
        cmds.curve(d=1, p=[(-0.870728, -0.000469542, -0.28747), (-0.667456, -0.000469542, -0.203272),(-0.583258, -0.000469542, 0), (-0.667456, -0.000469542, 0.203272),(-0.870728, -0.000469542, 0.28747), (-1.073999, -0.000469542, 0.203272),(-1.158197, -0.000469542, 0), (-1.073999, -0.000469542, -0.203272),(-0.870728, -0.000469542, -0.28747)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8], n="Left_Eye")
        cmds.CenterPivot()
        cmds.curve(d=1, p=[(0.870728, -0.000469542, -0.28747), (1.073999, -0.000469542, -0.203272),(1.158197, -0.000469542, 0), (1.073999, -0.000469542, 0.203272),(0.870728, -0.000469542, 0.28747), (0.667456, -0.000469542, 0.203272),(0.583258, -0.000469542, 0), (0.667456, -0.000469542, -0.203272),(0.870728, -0.000469542, -0.28747)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8], n="Right_Eye")
        cmds.CenterPivot()
        cmds.curve(d=1, p=[(-0.583258, -0.000469542, 0), (0.583258, -0.000469542, 0)], k=[0, 1], n="Center")
        cmds.parent('Left_Eye', 'Right_Eye', 'Center')
        return controller_name

    def arrows_on_ball_ctrl(self):
        controller_name = self.get_controller("arrows_on_ball_ctrl")
        cmds.curve(d=1, p=[(0, 0.35, -1.001567), (-0.336638, 0.677886, -0.751175), (-0.0959835, 0.677886, -0.751175),(-0.0959835, 0.850458, -0.500783), (-0.0959835, 0.954001, -0.0987656),(-0.500783, 0.850458, -0.0987656), (-0.751175, 0.677886, -0.0987656),(-0.751175, 0.677886, -0.336638), (-1.001567, 0.35, 0), (-0.751175, 0.677886, 0.336638),(-0.751175, 0.677886, 0.0987656), (-0.500783, 0.850458, 0.0987656),(-0.0959835, 0.954001, 0.0987656), (-0.0959835, 0.850458, 0.500783),(-0.0959835, 0.677886, 0.751175), (-0.336638, 0.677886, 0.751175), (0, 0.35, 1.001567),(0.336638, 0.677886, 0.751175), (0.0959835, 0.677886, 0.751175),(0.0959835, 0.850458, 0.500783), (0.0959835, 0.954001, 0.0987656),(0.500783, 0.850458, 0.0987656), (0.751175, 0.677886, 0.0987656),(0.751175, 0.677886, 0.336638), (1.001567, 0.35, 0), (0.751175, 0.677886, -0.336638),(0.751175, 0.677886, -0.0987656), (0.500783, 0.850458, -0.0987656),(0.0959835, 0.954001, -0.0987656), (0.0959835, 0.850458, -0.500783),(0.0959835, 0.677886, -0.751175), (0.336638, 0.677886, -0.751175), (0, 0.35, -1.001567)],k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,27, 28, 29, 30, 31, 32], n=controller_name)
        self.set_shape(controller_name)
        return controller_name

    def cog_ctrl(self):
        controller_name = self.get_controller("cog_ctrl")
        cmds.curve(d=3, p=[(7.06316e-009, 0, -1), (0.104714, 0, -0.990425), (0.314142, 0, -0.971274),(0.597534, 0, -0.821244), (0.822435, 0, -0.597853), (0.96683, 0, -0.314057),(1.016585, 0, -2.28604e-005), (0.96683, 0, 0.314148), (0.822435, 0, 0.597532),(0.597534, 0, 0.822435), (0.314142, 0, 0.96683), (1.22886e-008, 0, 1.016585),(-0.314142, 0, 0.96683), (-0.597534, 0, 0.822435), (-0.822435, 0, 0.597532),(-0.96683, 0, 0.314148), (-1.016585, 0, -2.29279e-005), (-0.96683, 0, -0.314057),(-0.822435, 0, -0.597853), (-0.597534, 0, -0.821244), (-0.314142, 0, -0.971274),(-0.104714, 0, -0.990425), (7.06316e-009, 0, -1)],k=[0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20, 20],n=controller_name)
        cmds.select("cog_ctrl.cv[1]", "cog_ctrl.cv[3]", "cog_ctrl.cv[5]", "cog_ctrl.cv[7]", "cog_ctrl.cv[9]", "cog_ctrl.cv[11]", "cog_ctrl.cv[13]", "cog_ctrl.cv[15]", "cog_ctrl.cv[17]", "cog_ctrl.cv[19]", r = True)
        cmds.scale(0.732056, 0.732056, 0.732056, r=True, p=('0cm', '0cm', '0cm'))
        cmds.select(cl=True)
        self.set_shape(controller_name)
        return controller_name

    def sun_ctrl(self):
        controller_name = self.get_controller("sun_ctrl")
        CONTROLLER_1 = cmds.circle(c=(0, 0, 0), nr=(0, 1, 0), sw=360, r=1, d=3, ut=0, tol=0.01, s=16, ch=1,n=sun_ctrl)
        cmds.select((CONTROLLER_1[0] + ".cv[0]"), (CONTROLLER_1[0] + ".cv[2]"), (CONTROLLER_1[0] + ".cv[4]"),(CONTROLLER_1[0] + ".cv[6]"), (CONTROLLER_1[0] + ".cv[8]"), (CONTROLLER_1[0] + ".cv[10]"), (CONTROLLER_1[0] + ".cv[12]"), (CONTROLLER_1[0] + ".cv[14]"), r = True)
        CONTROLCLUSTER = cmds.cluster(relative=True, envelope=1)
        cmds.setAttr((CONTROLCLUSTER[0] + "Handle.scale"), 0.5, 0.5, 0.5)
        CONTROLLER2 = cmds.circle(c=(0, 0, 0), nr=(0, 1, 0), sw=360, r=0.25, d=3, ut=0, tol=0.01, s=8, ch=1,n="controller2");
        cmds.select(CONTROLLER2[0], CONTROLLER_1, r=True)
        cmds.parent()
        cmds.pickWalk(d='up')
        cmds.DeleteHistory()
        self.set_shape(controller_name)
        return controller_name

    def pin_ctrl(self):
        controller_name = self.get_controller("pin_ctrl")
        cmds.curve(d=1, p=[(0, 0, 0), (0, 0, -1), (0, 0.5, -1), (0, 0.5, -0.5), (0, 1.5, -0.5), (0, 1.5, -1), (0, 2.5, -1), (0, 2.5, 1), (0, 1.5, 1), (0, 1.5, 0.5), (0, 0.5, 0.5), (0, 0.5, 1), (0, 0, 1), (0, 0, 0), (1, 0, 0), (1, 0.5, 0), (0.5, 0.5, 0), (0.5, 1.5, 0), (1, 1.5, 0), (1, 2.5, 0), (-1, 2.5, 0), (-1, 1.5, 0), (-0.5, 1.5, 0), (-0.5, 0.5, 0), (-1, 0.5, 0), (-1, 0, 0), (0, 0, 0)],k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,26],n =controller_name)
        self.set_shape(controller_name)
        return controller_name

    def jack_ctrl(self):
        controller_name = self.get_controller("jack_ctrl")
        cmds.curve(d=1,p=[(0, 0, 0,), (0.75, 0, 0), (1, 0.25, 0), (1.25, 0, 0), (1, -0.25, 0), (0.75, 0, 0), (1, 0, 0.25),(1.25, 0, 0), (1, 0, -0.25), (1, 0.25, 0), (1, 0, 0.25), (1, -0.25, 0), (1, 0, -0.25),(0.75, 0, 0), (0, 0, 0), (-0.75, 0, 0), (-1, 0.25, 0), (-1.25, 0, 0), (-1, -0.25, 0),(-0.75, 0, 0), (-1, 0, 0.25), (-1.25, 0, 0), (-1, 0, -0.25), (-1, 0.25, 0), (-1, 0, 0.25),(-1, -0.25, 0), (-1, 0, -0.25), (-0.75, 0, 0), (0, 0, 0), (0, 0.75, 0), (0, 1, -0.25),(0, 1.25, 0), (0, 1, 0.25), (0, 0.75, 0), (-0.25, 1, 0), (0, 1.25, 0), (0.25, 1, 0), (0, 1, 0.25),(-0.25, 1, 0), (0, 1, -0.25), (0.25, 1, 0), (0, 0.75, 0), (0, 0, 0), (0, -0.75, 0),(0, -1, -0.25), (0, -1.25, 0), (0, -1, 0.25), (0, -0.75, 0), (-0.25, -1, 0), (0, -1.25, 0),(0.25, -1, 0), (0, -1, -0.25), (-0.25, -1, 0), (0, -1, 0.25), (0.25, -1, 0), (0, -0.75, 0),(0, 0, 0), (0, 0, -0.75), (0, 0.25, -1), (0, 0, -1.25), (0, -0.25, -1), (0, 0, -0.75),(-0.25, 0, -1), (0, 0, -1.25), (0.25, 0, -1), (0, 0.25, -1), (-0.25, 0, -1), (0, -0.25, -1),(0.25, 0, -1), (0, 0, -0.75), (0, 0, 0), (0, 0, 0.75), (0, 0.25, 1), (0, 0, 1.25), (0, -0.25, 1),(0, 0, 0.75), (-0.25, 0, 1), (0, 0, 1.25), (0.25, 0, 1), (0, 0.25, 1), (-0.25, 0, 1),(0, -0.25, 1), (0.25, 0, 1), (0, 0, 0.75)],k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74,75, 76, 77, 78, 79, 80, 81, 82, 83], n=controller_name)
        self.set_shape(controller_name)
        return controller_name

    def nail_ctrl(self):
        controller_name = self.get_controller("nail_ctrl")
        cmds.curve(d=1, p=[(0, 0, 0), (-2, 0, 0), (-2.292893, 0, 0.707107), (-3, 0, 1), (-3.707107, 0, 0.707107), (-4, 0, 0), (-3.707107, 0, -0.707107), (-3, 0, -1), (-2.292893, 0, -0.707107), (-2, 0, 0), (-2.292893, 0, 0.707107), (-3.707107, 0, -0.707107), (-4, 0, 0), (-3.707107, 0, 0.707107), (-2.292893, 0, -0.707107)],k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], n=controller_name)
        self.set_shape(controller_name)
        return controller_name

    def double_nail_ctrl(self):
        controller_name = self.get_controller("double_nail_ctrl")
        cmds.curve(d=1, p=[(0, 0, 0), (-2, 0, 0), (-2.292893, 0, -0.707107), (-3, 0, -1), (-3.707107, 0, -0.707107),(-4, 0, 0), (-3.707107, 0, 0.707107), (-3, 0, 1), (-2.292893, 0, 0.707107), (-2, 0, 0),(-2.292893, 0, 0.707107), (-3.707107, 0, -0.707107), (-3, 0, -1), (-2.292893, 0, -0.707107),(-3.707107, 0, 0.707107), (-3, 0, 1), (-2.292893, 0, 0.707107), (-2, 0, 0), (0, 0, 0),(2, 0, 0), (2.292893, 0, -0.707107), (3, 0, -1), (3.707107, 0, -0.707107), (4, 0, 0),(3.707107, 0, 0.707107), (3, 0, 1), (2.292893, 0, 0.707107), (2, 0, 0),(2.292893, 0, 0.707107), (3.707107, 0, -0.707107), (3, 0, -1), (2.292893, 0, -0.707107),(3.707107, 0, 0.707107)],k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,27, 28, 29, 30, 31, 32], n=controller_name)
        self.set_shape(controller_name)
        return controller_name

    def four_nail_ctrl(self):
        controller_name = self.get_controller("four_nail_ctrl")
        cmds.curve(d=1, p=[(-2, 0, 0), (-2.292893, 0, -0.707107), (-3, 0, -1), (-3.707107, 0, -0.707107), (-4, 0, 0),(-3.707107, 0, 0.707107), (-3, 0, 1), (-2.292893, 0, 0.707107), (-2, 0, 0),(-2.292893, 0, 0.707107), (-3.707107, 0, -0.707107), (-4, 0, 0), (-3.707107, 0, 0.707107),(-2.292893, 0, -0.707107), (-2, 0, 0), (0, 0, 0), (2, 0, 0), (2.292893, 0, 0.707107),(3, 0, 1), (3.707107, 0, 0.707107), (4, 0, 0), (3.707107, 0, -0.707107), (3, 0, -1),(2.292893, 0, -0.707107), (2, 0, 0), (2.292893, 0, 0.707107), (3.707107, 0, -0.707107),(4, 0, 0), (3.707107, 0, 0.707107), (2.292893, 0, -0.707107), (2, 0, 0), (0, 0, 0),(0, 0, 2), (-0.707107, 0, 2.292893), (-1, 0, 3), (-0.707107, 0, 3.707107), (0, 0, 4),(0.707107, 0, 3.707107), (1, 0, 3), (0.707107, 0, 2.292893), (0, 0, 2),(0.707107, 0, 2.292893), (-0.707107, 0, 3.707107), (0, 0, 4), (0.707107, 0, 3.707107),(-0.707107, 0, 2.292893), (0, 0, 2), (0, 0, -2), (-0.707107, 0, -2.292893), (-1, 0, -3),(-0.707107, 0, -3.707107), (0, 0, -4), (0.707107, 0, -3.707107), (1, 0, -3),(0.707107, 0, -2.292893), (0, 0, -2), (0.707107, 0, -2.292893), (-0.707107, 0, -3.707107),(0, 0, -4), (0.707107, 0, -3.707107), (-0.707107, 0, -2.292893)],k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,51, 52, 53, 54, 55, 56, 57, 58, 59, 60], n=controller_name)
        self.set_shape(controller_name)
        return controller_name

    def dumbell_ctrl(self):
        controller_name = self.get_controller("dumbell_ctrl")
        cmds.curve(d=1, p=[(-1.207536, 0, 0.0254483), (-1.123549, -0.202763, 0.0254483), (-0.920786, -0.28675, 0.0254483), (-0.718023, -0.202763, 0.0254483), (-0.63504, -0.00242492, 0.0254483), (0.634091, 0, 0.0254483), (0.718023, -0.202763, 0.0254483), (0.920786, -0.28675, 0.0254483), (1.123549, -0.202763, 0.0254483), (1.207536, 0, 0.0254483), (1.123549, 0.202763, 0.0254483), (0.920786, 0.28675, 0.0254483), (0.718023, 0.202763, 0.0254483), (0.634091, 0, 0.0254483), (-0.63504, -0.00242492, 0.0254483), (-0.718023, 0.202763, 0.0254483), (-0.920786, 0.28675, 0.0254483), (-1.123549, 0.202763, 0.0254483), (-1.207536, 0, 0.0254483)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],n=controller_name)
        self.set_shape(controller_name)
        return controller_name

    def pointer_ctrl(self):
        controller_name = self.get_controller("pointer_ctrl")
        cmds.curve(d=3, p=[(-1.508537, 0, 0), (-1.059622, 0, -0.316884), (-0.161791, 0, -0.950653), (-0.231491, 0, -0.132891), (0.0199252, 0, 0.0238494), (0.843595, 0, -0.46025), (1.7044, 0, -1.130663), (1.00832, 0, -0.442815), (0.512875, 0, -0.0222687), (1.031578, 0, 0.508979), (1.701544, 0, 1.119434), (0.831393, 0, 0.447942), (0.018681, 0, 0.000680685), (-0.212893, 0, 0.0475119), (-0.15231, 0, 0.973132), (-1.056461, 0, 0.324377), (-1.508537, 0, 0)], k=[0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 14, 14], n=controller_name)
        self.set_shape(controller_name)
        return controller_name

    def aim_ctrl(self):
        controller_name = self.get_controller("aim_ctrl")
        cmds.curve(d=1, p=[(0, 0, 1), (0, 0, -1), (0, 2, 0), (0, -2, 0), (0, 0, -1), (1, 0, 0), (-1, 0, 0), (0, 0, -1)],k=[0, 1, 2, 3, 4, 5, 6, 7], n=controller_name)
        self.set_shape(controller_name)
        return controller_name

    def aim_two_ctrl(self):
        controller_name = self.get_controller("aim_two_ctrl")
        cmds.curve(d=1, p=[(0, 0, 1), (0, 0, -1), (0, 2, 0), (0, -2, 0), (0, 0, -1), (2, 0, 0), (-2, 0, 0), (0, 0, -1)],k=[0, 1, 2, 3, 4, 5, 6, 7], n=controller_name)
        self.set_shape(controller_name)
        return controller_name

    def eye_ctrl(self,prefix_no='',prefix_name='',side=''):
        controller_name = self.get_controller("four_nail_ctrl")
        #Create main Circle
        controler_class.circle_ctrl()
        eye_main_ctrl_name  = prefix_name + "_" + str(prefix_no) + '_'  + side + '_Eye_Main_Circle_CTRL'
        cmds.select('circle_ctrl')
        cmds.rename(eye_main_ctrl_name)
        #Create inner Circle 1
        controler_class.circle_ctrl()
        cmds.select('circle_ctrl')
        eye_inner_circle_1_ctrl = prefix_name + "_" + str(prefix_no) + '_' + side + '_Eye_Inner_Circle_1_CTRL'
        cmds.rename(eye_inner_circle_1_ctrl)
        cmds.setAttr((eye_inner_circle_1_ctrl + '.sx'),0.8)
        cmds.setAttr((eye_inner_circle_1_ctrl + '.sy'), 0.8)
        cmds.setAttr((eye_inner_circle_1_ctrl + '.sz'), 0.8)
        cmds.select(eye_inner_circle_1_ctrl)
        cmds.DeleteHistory()
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1)

        #Create a joint on Curve
        #Create a 7 Cluster and Joint
        total_cv = 8
        i = 0
        while i < total_cv:
            plusone = i + 1
            #Select the CV and Create a Cluster
            cmds.select(eye_inner_circle_1_ctrl + '.cv[%s]' % i)
            cmds.cluster()
            sel_cluster = cmds.ls(sl=True)
            cmds.select(sel_cluster)
            cluster_name = prefix_name + "_" + str(prefix_no) + '_' + side + '_Eye_Inner_Circle_1_CTRL_VTX_%s_Cluster' % plusone
            cmds.rename(cluster_name)
            cluster_getAttr = cmds.getAttr(cluster_name + '.t')
            #Create a Joint and point to the Cluster Position
            jnt_name = prefix_name + "_" + str(prefix_no) + '_' + side + '_Eye_Inner_Circle_1_CTRL_VTX_%s_JNT' % plusone
            cmds.select(cl=True)
            jnt = cmds.joint(p=(0,0,0),n=jnt_name)
            cmds.select(cl=True)
            cmds.parentConstraint(cluster_name,jnt_name,mo=False)
            cmds.select(jnt_name + '_parentConstraint1')
            cmds.delete()
            #make a cluster in Grp
            cluster_grp_name = prefix_name + "_" + str(prefix_no) + '_' + side + '_Eye_Inner_Circle_1_CTRL_VTX_Cluster_Grp'
            if cmds.objExists(cluster_grp_name):
                cmds.select(cluster_name,cluster_grp_name)
                cmds.parent()
            else:
                cmds.select(cluster_name)
                cmds.group(n=cluster_grp_name)

            jnt_grp_name = prefix_name + "_" + str(prefix_no) + '_' + side + '_Eye_Inner_Circle_1_CTRL_VTX_JNT_Grp'
            if cmds.objExists(jnt_grp_name):
                cmds.select(jnt_name,jnt_grp_name)
                cmds.parent()
            else:
                cmds.select(jnt_name)
                cmds.group(n=jnt_grp_name)
            i+=1
        #make Joint as a Variable


        eye_inner_circle_1_1_jnt = prefix_name + "_" + str(prefix_no) + '_' + side + '_Eye_Inner_Circle_1_CTRL_VTX_1_JNT'
        eye_inner_circle_1_2_jnt = prefix_name + "_" + str(prefix_no) + '_' + side + '_Eye_Inner_Circle_1_CTRL_VTX_2_JNT'
        eye_inner_circle_1_3_jnt = prefix_name + "_" + str(prefix_no) + '_' + side + '_Eye_Inner_Circle_1_CTRL_VTX_3_JNT'
        eye_inner_circle_1_4_jnt = prefix_name + "_" + str(prefix_no) + '_' + side + '_Eye_Inner_Circle_1_CTRL_VTX_4_JNT'
        eye_inner_circle_1_5_jnt = prefix_name + "_" + str(prefix_no) + '_' + side + '_Eye_Inner_Circle_1_CTRL_VTX_5_JNT'
        eye_inner_circle_1_6_jnt = prefix_name + "_" + str(prefix_no) + '_' + side + '_Eye_Inner_Circle_1_CTRL_VTX_6_JNT'
        eye_inner_circle_1_7_jnt = prefix_name + "_" + str(prefix_no) + '_' + side + '_Eye_Inner_Circle_1_CTRL_VTX_7_JNT'
        eye_inner_circle_1_8_jnt = prefix_name + "_" + str(prefix_no) + '_' + side + '_Eye_Inner_Circle_1_CTRL_VTX_8_JNT'

        #Select the Jnt and bind to the Curve
        cmds.select(eye_inner_circle_1_1_jnt,eye_inner_circle_1_2_jnt,eye_inner_circle_1_3_jnt,eye_inner_circle_1_4_jnt,
                    eye_inner_circle_1_5_jnt,eye_inner_circle_1_6_jnt,eye_inner_circle_1_7_jnt,eye_inner_circle_1_8_jnt,
                    eye_inner_circle_1_ctrl)
        cmds.SmoothBindSkin()

        #Delete the Cluster Grp
        cmds.select(cluster_grp_name)
        cmds.delete()

        #make circle_1 Grp
        cmds.select(eye_inner_circle_1_ctrl,jnt_grp_name)
        circle_1_grp = prefix_name + "_" + str(prefix_no) + '_' + side + '_Eye_Inner_Circle_1_Grp'
        cmds.group(n= circle_1_grp)

        # Create inner Circle 2
        controler_class.circle_ctrl()
        cmds.select('circle_ctrl')
        eye_inner_circle_2_ctrl = prefix_name + "_" + str(prefix_no) + '_' + side + '_Eye_Inner_Circle_2_CTRL'
        cmds.rename(eye_inner_circle_2_ctrl)
        cmds.setAttr((eye_inner_circle_2_ctrl + '.sx'), 0.8)
        cmds.setAttr((eye_inner_circle_2_ctrl + '.sy'), 0.8)
        cmds.setAttr((eye_inner_circle_2_ctrl + '.sz'), 0.8)
        cmds.select(eye_inner_circle_2_ctrl)
        cmds.DeleteHistory
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1)

        # Create a joint on Curve
        # Create a 7 Cluster and Joint
        total_cv = 8
        i = 0
        while i < total_cv:
            plusone = i + 1
            # Select the CV and Create a Cluster
            cmds.select(eye_inner_circle_2_ctrl + '.cv[%s]' % i)
            cmds.cluster()
            sel_cluster = cmds.ls(sl=True)
            cmds.select(sel_cluster)
            cluster_name = prefix_name + "_" + str(
                prefix_no) + '_' + side + '_Eye_Inner_Circle_2_CTRL_VTX_%s_Cluster' % plusone
            cmds.rename(cluster_name)
            cluster_getAttr = cmds.getAttr(cluster_name + '.t')
            # Create a Joint and point to the Cluster Position
            jnt_name = prefix_name + "_" + str(prefix_no) + '_' + side + '_Eye_Inner_Circle_2_CTRL_VTX_%s_JNT' % plusone
            cmds.select(cl=True)
            jnt = cmds.joint(p=(0, 0, 0), n=jnt_name)
            cmds.select(cl=True)
            cmds.parentConstraint(cluster_name, jnt_name, mo=False)
            cmds.select(jnt_name + '_parentConstraint1')
            cmds.delete()
            # make a cluster in Grp
            cluster_grp_name = prefix_name + "_" + str(
                prefix_no) + '_' + side + '_Eye_Inner_Circle_2_CTRL_VTX_Cluster_Grp'
            if cmds.objExists(cluster_grp_name):
                cmds.select(cluster_name, cluster_grp_name)
                cmds.parent()
            else:
                cmds.select(cluster_name)
                cmds.group(n=cluster_grp_name)

            jnt_grp_name = prefix_name + "_" + str(prefix_no) + '_' + side + '_Eye_Inner_Circle_2_CTRL_VTX_JNT_Grp'
            if cmds.objExists(jnt_grp_name):
                cmds.select(jnt_name, jnt_grp_name)
                cmds.parent()
            else:
                cmds.select(jnt_name)
                cmds.group(n=jnt_grp_name)
            i += 1
        # make Joint as a Variable


        eye_inner_circle_2_1_jnt = prefix_name + "_" + str(
            prefix_no) + '_' + side + '_Eye_Inner_Circle_2_CTRL_VTX_1_JNT'
        eye_inner_circle_2_2_jnt = prefix_name + "_" + str(
            prefix_no) + '_' + side + '_Eye_Inner_Circle_2_CTRL_VTX_2_JNT'
        eye_inner_circle_2_3_jnt = prefix_name + "_" + str(
            prefix_no) + '_' + side + '_Eye_Inner_Circle_2_CTRL_VTX_3_JNT'
        eye_inner_circle_2_4_jnt = prefix_name + "_" + str(
            prefix_no) + '_' + side + '_Eye_Inner_Circle_2_CTRL_VTX_4_JNT'
        eye_inner_circle_2_5_jnt = prefix_name + "_" + str(
            prefix_no) + '_' + side + '_Eye_Inner_Circle_2_CTRL_VTX_5_JNT'
        eye_inner_circle_2_6_jnt = prefix_name + "_" + str(
            prefix_no) + '_' + side + '_Eye_Inner_Circle_2_CTRL_VTX_6_JNT'
        eye_inner_circle_2_7_jnt = prefix_name + "_" + str(
            prefix_no) + '_' + side + '_Eye_Inner_Circle_2_CTRL_VTX_7_JNT'
        eye_inner_circle_2_8_jnt = prefix_name + "_" + str(
            prefix_no) + '_' + side + '_Eye_Inner_Circle_2_CTRL_VTX_8_JNT'

        # Select the Jnt and bind to the Curve
        cmds.select(eye_inner_circle_2_1_jnt, eye_inner_circle_2_2_jnt, eye_inner_circle_2_3_jnt,
                    eye_inner_circle_2_4_jnt,
                    eye_inner_circle_2_5_jnt, eye_inner_circle_2_6_jnt, eye_inner_circle_2_7_jnt,
                    eye_inner_circle_2_8_jnt,
                    eye_inner_circle_2_ctrl)
        cmds.SmoothBindSkin()

        # Delete the Cluster Grp
        cmds.select(cluster_grp_name)
        cmds.delete()

        #make circle_2 Grp
        cmds.select(eye_inner_circle_2_ctrl,jnt_grp_name)
        circle_2_grp = prefix_name + "_" + str(prefix_no) + '_' + side + '_Eye_Inner_Circle_2_Grp'
        cmds.group(n= circle_2_grp)

        #make Selected Jnt x Axis 0
        cmds.select(eye_inner_circle_1_1_jnt,eye_inner_circle_1_7_jnt,eye_inner_circle_1_8_jnt,
                    eye_inner_circle_2_3_jnt,eye_inner_circle_2_4_jnt,eye_inner_circle_2_5_jnt)
        sel_jnt =cmds.ls(sl=True)
        len_sel_jnt = len(sel_jnt)
        i = 0
        while i < len_sel_jnt :
            cmds.setAttr((sel_jnt[i] + '.tx'),0)
            i+=1

        #Create a Inside Circle
        #Dynamic Blend
        controler_class.circle_ctrl()
        inner_circle_dynamic_blink_ctrl_name = prefix_name + "_" + str(prefix_no) + '_' + side + '_Eye_Inner_Circle_Dynamic_Blink_CTRL'
        cmds.rename('circle_ctrl')
        cmds.rename(inner_circle_dynamic_blink_ctrl_name)
        cmds.setAttr((inner_circle_dynamic_blink_ctrl_name + '.sx'),0.15)
        cmds.setAttr((inner_circle_dynamic_blink_ctrl_name + '.sy'), 0.15)
        cmds.setAttr((inner_circle_dynamic_blink_ctrl_name + '.sz'), 0.15)
        cmds.DeleteHistory()
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1)

        #Manual Blend
        controler_class.circle_ctrl()
        inner_circle_manual_blink_ctrl_name = prefix_name + "_" + str(prefix_no) + '_' + side + '_Eye_Inner_Circle_Manual_Blink_CTRL'
        cmds.rename('circle_ctrl')
        cmds.rename(inner_circle_manual_blink_ctrl_name)
        cmds.setAttr((inner_circle_manual_blink_ctrl_name + '.sx'),0.15)
        cmds.setAttr((inner_circle_manual_blink_ctrl_name + '.sy'), 0.15)
        cmds.setAttr((inner_circle_manual_blink_ctrl_name + '.sz'), 0.15)
        cmds.DeleteHistory()
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1)



        #parent to the Main CTRL
        cmds.select(inner_circle_dynamic_blink_ctrl_name,inner_circle_manual_blink_ctrl_name , eye_main_ctrl_name)
        cmds.parent()

        #Set Driven Key
        cmds.setAttr((inner_circle_manual_blink_ctrl_name + '.tx'),0)
        cmds.setAttr((eye_inner_circle_1_8_jnt + '.tx'),0)
        cmds.setAttr((eye_inner_circle_2_4_jnt + '.tx'),0)

        cmds.setDrivenKeyframe((eye_inner_circle_1_8_jnt + '.tx'),
                               currentDriver=(inner_circle_manual_blink_ctrl_name + '.tx'))
        cmds.setDrivenKeyframe((eye_inner_circle_2_4_jnt + '.tx'),
                               currentDriver=(inner_circle_manual_blink_ctrl_name + '.tx'))

        cmds.setAttr((inner_circle_manual_blink_ctrl_name + '.tx'),0.5)
        cmds.setAttr((eye_inner_circle_1_8_jnt + '.tx'),-0.7)
        cmds.setAttr((eye_inner_circle_2_4_jnt + '.tx'),0.7)

        cmds.setDrivenKeyframe((eye_inner_circle_1_8_jnt + '.tx'),
                               currentDriver=(inner_circle_manual_blink_ctrl_name + '.tx'))
        cmds.setDrivenKeyframe((eye_inner_circle_2_4_jnt + '.tx'),
                               currentDriver=(inner_circle_manual_blink_ctrl_name + '.tx'))

        cmds.setAttr((inner_circle_manual_blink_ctrl_name + '.tx'), 0)

        #Set Driven Key
        cmds.setAttr((inner_circle_dynamic_blink_ctrl_name + '.tx'),0)
        cmds.setAttr((eye_inner_circle_1_8_jnt + '.tx'),0)
        cmds.setAttr((eye_inner_circle_2_4_jnt + '.tx'),0)

        cmds.setDrivenKeyframe((eye_inner_circle_1_8_jnt + '.tx'),
                               currentDriver=(inner_circle_dynamic_blink_ctrl_name + '.tx'))
        cmds.setDrivenKeyframe((eye_inner_circle_2_4_jnt + '.tx'),
                               currentDriver=(inner_circle_dynamic_blink_ctrl_name + '.tx'))

        cmds.setAttr((inner_circle_dynamic_blink_ctrl_name + '.tx'),0.5)
        cmds.setAttr((eye_inner_circle_1_8_jnt + '.tx'),-0.7)
        cmds.setAttr((eye_inner_circle_2_4_jnt + '.tx'),0.7)

        cmds.setDrivenKeyframe((eye_inner_circle_1_8_jnt + '.tx'),
                               currentDriver=(inner_circle_dynamic_blink_ctrl_name + '.tx'))
        cmds.setDrivenKeyframe((eye_inner_circle_2_4_jnt + '.tx'),
                               currentDriver=(inner_circle_dynamic_blink_ctrl_name + '.tx'))

        cmds.setAttr((inner_circle_dynamic_blink_ctrl_name + '.tx'), 0)

        #Lock and Hide Unwanted Object
        #Select all the Object
        cmds.select(eye_inner_circle_1_1_jnt,eye_inner_circle_1_2_jnt,eye_inner_circle_1_3_jnt,eye_inner_circle_1_4_jnt,
                    eye_inner_circle_1_5_jnt,eye_inner_circle_1_6_jnt,eye_inner_circle_1_7_jnt,eye_inner_circle_1_8_jnt,
                    eye_inner_circle_2_1_jnt,eye_inner_circle_2_2_jnt,eye_inner_circle_2_3_jnt,eye_inner_circle_2_4_jnt,
                    eye_inner_circle_2_5_jnt,eye_inner_circle_2_6_jnt,eye_inner_circle_2_7_jnt,eye_inner_circle_2_8_jnt)
        sel_jnt =cmds.ls(sl=True)
        len_sel_jnt = len(sel_jnt)
        i = 0
        while i < len_sel_jnt:
            cmds.setAttr((sel_jnt[i] + '.tx'),lock=True,keyable=False,channelBox=False)
            cmds.setAttr((sel_jnt[i] + '.ty'), lock=True, keyable=False, channelBox=False)
            cmds.setAttr((sel_jnt[i] + '.tz'), lock=True, keyable=False, channelBox=False)
            cmds.setAttr((sel_jnt[i] + '.sx'), lock=True, keyable=False, channelBox=False)
            cmds.setAttr((sel_jnt[i] + '.sy'), lock=True, keyable=False, channelBox=False)
            cmds.setAttr((sel_jnt[i] + '.sz'), lock=True, keyable=False, channelBox=False)
            cmds.setAttr((sel_jnt[i] + '.rx'), lock=True, keyable=False, channelBox=False)
            cmds.setAttr((sel_jnt[i] + '.ry'), lock=True, keyable=False, channelBox=False)
            cmds.setAttr((sel_jnt[i] + '.rz'), lock=True, keyable=False, channelBox=False)
            cmds.setAttr((sel_jnt[i] + '.v'), 0)
            cmds.setAttr((sel_jnt[i] + '.v'), lock=True, keyable=False, channelBox=False)




            i+=1

        cmds.setAttr((eye_main_ctrl_name + '.tx'), lock=True, keyable=False, channelBox=False)
        cmds.setAttr((eye_main_ctrl_name + '.ty'), lock=True, keyable=False, channelBox=False)
        cmds.setAttr((eye_main_ctrl_name + '.tz'), lock=True, keyable=False, channelBox=False)
        cmds.setAttr((eye_main_ctrl_name + '.sx'), lock=True, keyable=False, channelBox=False)
        cmds.setAttr((eye_main_ctrl_name + '.sy'), lock=True, keyable=False, channelBox=False)
        cmds.setAttr((eye_main_ctrl_name + '.sz'), lock=True, keyable=False, channelBox=False)
        cmds.setAttr((eye_main_ctrl_name + '.rx'), lock=True, keyable=False, channelBox=False)
        cmds.setAttr((eye_main_ctrl_name + '.ry'), lock=True, keyable=False, channelBox=False)
        cmds.setAttr((eye_main_ctrl_name + '.rz'), lock=True, keyable=False, channelBox=False)
        cmds.setAttr((eye_main_ctrl_name + '.v'), lock=True, keyable=False, channelBox=False)
        #Create a Dybanic and Manual Switch CTRL
        controler_class.circle_ctrl()
        eye_ctrl_name = prefix_name + "_" + str(prefix_no) + '_' + side + '_Eye_CTRL'
        cmds.rename('circle_ctrl',eye_ctrl_name)
        cmds.setAttr((eye_ctrl_name + '.scaleX'), 0.2)
        cmds.setAttr((eye_ctrl_name + '.scaleY'), 0.2)
        cmds.setAttr((eye_ctrl_name + '.scaleZ'), 0.2)
        cmds.DeleteHistory()
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1)


        controler_class.circle_ctrl()
        eye_ctrl_1_name = prefix_name + "_" + str(prefix_no) + '_' + side + '_Eye_1_CTRL'
        cmds.rename('circle_ctrl',eye_ctrl_1_name)
        cmds.setAttr((eye_ctrl_1_name + '.scaleX'), 0.2)
        cmds.setAttr((eye_ctrl_1_name + '.scaleY'), 0.2)
        cmds.setAttr((eye_ctrl_1_name + '.scaleZ'), 0.2)
        cmds.setAttr((eye_ctrl_1_name + '.rx'), 90)
        cmds.DeleteHistory()
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1)

        cmds.select((eye_ctrl_1_name + 'Shape'),eye_ctrl_name)
        cmds.parent(r=True,s=True)
        cmds.select(eye_ctrl_1_name)
        cmds.delete()
        cmds.setAttr((eye_ctrl_name + '.tx'), -2)
        cmds.select(eye_ctrl_name)
        cmds.DeleteHistory()
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1)

        cmds.select(eye_main_ctrl_name,circle_1_grp,circle_2_grp,eye_ctrl_name)
        cmds.parent()

        cmds.setAttr((eye_inner_circle_1_ctrl + ".inheritsTransform"),0)
        cmds.setAttr((eye_inner_circle_1_ctrl + ".overrideEnabled"), 1)
        cmds.setAttr ((eye_inner_circle_1_ctrl + ".overrideDisplayType"),1)

        cmds.setAttr((eye_inner_circle_2_ctrl + ".inheritsTransform"), 0)
        cmds.setAttr((eye_inner_circle_2_ctrl + ".overrideEnabled"), 1)
        cmds.setAttr ((eye_inner_circle_2_ctrl + ".overrideDisplayType"),1)

        #add Attr to left eye ctrl
        cmds.select(eye_ctrl_name)
        rig_tool.attr_create(name='Dynamic_Manual',min=0,max=1,dv=0)

        cmds.connectAttr((eye_ctrl_name + '.Dynamic_Manual'),(inner_circle_dynamic_blink_ctrl_name + '.v'))
        cmds.select(eye_ctrl_name,inner_circle_manual_blink_ctrl_name)
        node_class.reverse_node('Dynamic_Manual','v')

        #make a Limit to the 0.5
        cmds.transformLimits(inner_circle_dynamic_blink_ctrl_name, tx=(0, 0.5), etx=(1, 1))
        cmds.transformLimits(inner_circle_manual_blink_ctrl_name, tx=(0, 0.5), etx=(1, 1))
        cmds.select(inner_circle_dynamic_blink_ctrl_name,inner_circle_manual_blink_ctrl_name)
        sel_ctrl = cmds.ls(sl=True)

        total_obj = 2
        i = 0
        while i < total_obj:
            cmds.setAttr((sel_ctrl[i] + '.ty'), lock=True, keyable=False, channelBox=False)
            cmds.setAttr((sel_ctrl[i] + '.tz'), lock=True, keyable=False, channelBox=False)
            cmds.setAttr((sel_ctrl[i] + '.sx'), lock=True, keyable=False, channelBox=False)
            cmds.setAttr((sel_ctrl[i] + '.sy'), lock=True, keyable=False, channelBox=False)
            cmds.setAttr((sel_ctrl[i] + '.sz'), lock=True, keyable=False, channelBox=False)
            cmds.setAttr((sel_ctrl[i] + '.rx'), lock=True, keyable=False, channelBox=False)
            cmds.setAttr((sel_ctrl[i] + '.ry'), lock=True, keyable=False, channelBox=False)
            cmds.setAttr((sel_ctrl[i] + '.rz'), lock=True, keyable=False, channelBox=False)
            cmds.setAttr((sel_ctrl[i] + '.v'), lock=True, keyable=False, channelBox=False)

            i+=1

        #Create a Upper Middle and Lower Controler
        # Create Dynamic Upperlid Lowerlid and Middle CTRL
        cmds.textCurves(ch=0, f="Times New Roman|h-13|w400|c0", t="Lower")
        cmds.select('Char_L_1', 'Char_o_1', 'Char_w_1', 'Char_e_1', 'Char_r_1')
        sel_curve = cmds.ls(sl=True)
        len_sel_curve = len(sel_curve)
        i = 0
        while i < len_sel_curve:
            cmds.select(sel_curve[i])
            child_list = cmds.listRelatives(children=True)
            cmds.select(child_list)
            cmds.parent(w=True)
            cmds.select(sel_curve[i])
            cmds.Delete()
            if cmds.objExists('Lower_CRV_Grp'):
                cmds.select(child_list, 'Lower_CRV_Grp')
                cmds.parent()
            else:
                cmds.select(child_list)
                cmds.group(n='Lower_CRV_Grp')

            i += 1

        cmds.select('Lower_CRV_Grp')
        child_list = cmds.listRelatives(children=True)
        cmds.select(child_list[0])
        name = prefix_name + "_" + str(prefix_no) + '_' + side + '_Lower_CTRL'
        cmds.rename(name)
        len_child_list = len(child_list) - 1
        i = 0
        while i < len_child_list:
            plusOne = i + 1
            if plusOne == 1:
                cmds.select(child_list[plusOne])
            else:
                cmds.select(child_list[plusOne], add=True)
            i += 1
        cmds.DeleteHistory()
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1)
        cmds.pickWalk(d='down')
        cmds.select(name, add=True)
        cmds.parent(r=True, s=True)
        cmds.select(name)
        cmds.parent(w=True)
        cmds.CenterPivot()
        cmds.select('Lower_CRV_Grp', 'Text_Lower_1')
        cmds.delete()

        #Middle CTRL as a variable
        lower_ctrl_name =  prefix_name + "_" + str(prefix_no) + '_' + side + '_Eye_Lower_CTRL'
        cmds.select(name)
        cmds.rename(lower_ctrl_name)

        # Create Dynamic Upperlid Lowerlid and Middle CTRL
        cmds.textCurves(ch=0, f="Times New Roman|h-13|w400|c0", t="Upper")
        cmds.select('Char_U_1', 'Char_p_1', 'Char_p_2', 'Char_e_1', 'Char_r_1')
        sel_curve = cmds.ls(sl=True)
        len_sel_curve = len(sel_curve)
        i = 0
        while i < len_sel_curve:
            cmds.select(sel_curve[i])
            child_list = cmds.listRelatives(children=True)
            cmds.select(child_list)
            cmds.parent(w=True)
            cmds.select(sel_curve[i])
            cmds.Delete()
            if cmds.objExists('Upper_CRV_Grp'):
                cmds.select(child_list, 'Upper_CRV_Grp')
                cmds.parent()
            else:
                cmds.select(child_list)
                cmds.group(n='Upper_CRV_Grp')

            i += 1

        cmds.select('Upper_CRV_Grp')
        child_list = cmds.listRelatives(children=True)
        cmds.select(child_list[0])
        name = prefix_name + "_" + str(prefix_no) + '_' + side + '_Upper_CTRL'
        cmds.rename(name)
        len_child_list = len(child_list) - 1
        i = 0
        while i < len_child_list:
            plusOne = i + 1
            if plusOne == 1:
                cmds.select(child_list[plusOne])
            else:
                cmds.select(child_list[plusOne], add=True)
            i += 1
        cmds.DeleteHistory()
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1)
        cmds.pickWalk(d='down')
        cmds.select(name, add=True)
        cmds.parent(r=True, s=True)
        cmds.select(name)
        cmds.parent(w=True)
        cmds.CenterPivot()
        cmds.select('Upper_CRV_Grp', 'Text_Upper_1')
        cmds.delete()

        # Middle CTRL as a variable
        upper_ctrl_name = prefix_name + "_" + str(prefix_no) + '_' + side + '_Eye_Upper_CTRL'
        cmds.select(name)
        cmds.rename(upper_ctrl_name)

        # Create Dynamic Upperlid Lowerlid and Middle CTRL
        cmds.textCurves(ch=0, f="Times New Roman|h-13|w400|c0", t="Middle")
        cmds.select('Char_M_1', 'Char_i_1', 'Char_d_1', 'Char_d_2', 'Char_l_1', 'Char_e_1')
        sel_curve = cmds.ls(sl=True)
        len_sel_curve = len(sel_curve)
        i = 0
        while i < len_sel_curve:
            cmds.select(sel_curve[i])
            child_list = cmds.listRelatives(children=True)
            cmds.select(child_list)
            cmds.parent(w=True)
            cmds.select(sel_curve[i])
            cmds.Delete()
            if cmds.objExists('Middle_CRV_Grp'):
                cmds.select(child_list, 'Middle_CRV_Grp')
                cmds.parent()
            else:
                cmds.select(child_list)
                cmds.group(n='Middle_CRV_Grp')

            i += 1

        cmds.select('Middle_CRV_Grp')
        child_list = cmds.listRelatives(children=True)
        cmds.select(child_list[0])
        name = prefix_name + "_" + str(prefix_no) + '_' + side + '_Middle_CTRL'
        cmds.rename(name)
        len_child_list = len(child_list) - 1
        i = 0
        while i < len_child_list:
            plusOne = i + 1
            if plusOne == 1:
                cmds.select(child_list[plusOne])
            else:
                cmds.select(child_list[plusOne], add=True)
            i += 1
        cmds.DeleteHistory()
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1)
        cmds.pickWalk(d='down')
        cmds.select(name, add=True)
        cmds.parent(r=True, s=True)
        cmds.select(name)
        cmds.parent(w=True)
        cmds.CenterPivot()
        cmds.select('Middle_CRV_Grp', 'Text_Middle_1')
        cmds.delete()

        # Middle CTRL as a variable
        middle_ctrl_name = prefix_name + "_" + str(prefix_no) + '_' + side + '_Eye_Middle_CTRL'
        cmds.select(name)
        cmds.rename(middle_ctrl_name)

        #place to the main place
        cmds.select(lower_ctrl_name,upper_ctrl_name,middle_ctrl_name)
        upper_middle_lower_grp = prefix_name + "_" + str(prefix_no) + '_' + side + '_Eye_Middle_Upper_Lower_CTRL_Grp'
        cmds.group(n=upper_middle_lower_grp)
        cmds.CenterPivot()
        cmds.setAttr((upper_middle_lower_grp + '.rx'), -90)
        cmds.setAttr((upper_middle_lower_grp + '.ry'),-90)
        cmds.move(-1.5,0,0,r=True)
        cmds.setAttr((upper_middle_lower_grp + '.sx'), 0.3)
        cmds.setAttr((upper_middle_lower_grp + '.sy'), 0.3)
        cmds.setAttr((upper_middle_lower_grp + '.sz'), 0.3)
        cmds.move(0,0,-1.5,r=True)

        #parent to the Main CTRL
        cmds.select(upper_middle_lower_grp,eye_ctrl_name)
        cmds.parent()

        #make a Controler as a Dynamic

        cmds.setAttr((inner_circle_dynamic_blink_ctrl_name + '.tx'), 0)
        cmds.setAttr((middle_ctrl_name +  '.v'), 1)
        cmds.setAttr((upper_ctrl_name + '.v'), 0)
        cmds.setAttr((lower_ctrl_name + '.v'), 0)


        cmds.setDrivenKeyframe((middle_ctrl_name + ".v"),
                               currentDriver= (inner_circle_dynamic_blink_ctrl_name + '.tx'))
        cmds.setDrivenKeyframe((upper_ctrl_name + ".v"),
                               currentDriver= (inner_circle_dynamic_blink_ctrl_name + '.tx'))
        cmds.setDrivenKeyframe((lower_ctrl_name + ".v"),
                               currentDriver= (inner_circle_dynamic_blink_ctrl_name + '.tx'))



        cmds.setAttr((inner_circle_dynamic_blink_ctrl_name + '.tx'), 0.5)
        cmds.setAttr((middle_ctrl_name +  '.v'), 0)
        cmds.setAttr((upper_ctrl_name + '.v'), 1)
        cmds.setAttr((lower_ctrl_name + '.v'), 1)


        cmds.setDrivenKeyframe((middle_ctrl_name + ".v"),
                               currentDriver= (inner_circle_dynamic_blink_ctrl_name + '.tx'))
        cmds.setDrivenKeyframe((upper_ctrl_name + ".v"),
                               currentDriver= (inner_circle_dynamic_blink_ctrl_name + '.tx'))
        cmds.setDrivenKeyframe((lower_ctrl_name + ".v"),
                               currentDriver= (inner_circle_dynamic_blink_ctrl_name + '.tx'))



        ###########
        cmds.setAttr((inner_circle_dynamic_blink_ctrl_name + '.tx'), 0)
        cmds.setAttr((lower_ctrl_name + '.ty'), 1.8)
        cmds.setAttr((upper_ctrl_name + '.ty'), -1.8)


        cmds.setDrivenKeyframe((lower_ctrl_name + ".ty"),
                               currentDriver=(inner_circle_dynamic_blink_ctrl_name + '.tx'))
        cmds.setDrivenKeyframe((upper_ctrl_name + ".ty"),
                               currentDriver=(inner_circle_dynamic_blink_ctrl_name + '.tx'))

        cmds.connectAttr((eye_ctrl_name + '.Dynamic_Manual'),(upper_middle_lower_grp + '.v'))

        cmds.select(upper_ctrl_name,lower_ctrl_name)
        sel_ctrl = cmds.ls(sl=True)
        len_sel_ctrl = len(sel_ctrl)
        i = 0
        while i < len_sel_ctrl:
            cmds.addAttr(sel_ctrl[i], ln="Twist", at="double", min=0, max=1, dv=0)
            cmds.setAttr((sel_ctrl[i] + ".Twist"), e=True, keyable=True)

            cmds.addAttr(sel_ctrl[i], ln="Twist_Vis", at="double", min=0, max=1, dv=0)
            cmds.setAttr((sel_ctrl[i] + ".Twist_Vis"), e=True, keyable=True)

            cmds.addAttr(sel_ctrl[i], ln="Side", at="double", min=0, max=1, dv=0)
            cmds.setAttr((sel_ctrl[i] + ".Side"), e=True, keyable=True)

            cmds.addAttr(sel_ctrl[i], ln="Side_Vis", at="double", min=0, max=1, dv=0)
            cmds.setAttr((sel_ctrl[i] + ".Side_Vis"), e=True, keyable=True)

            cmds.addAttr(sel_ctrl[i], ln="SEPERATOR", at="double", min=0, max=0, dv=0)
            cmds.setAttr((sel_ctrl[i] + ".SEPERATOR"), e=True, keyable=True)

            cmds.addAttr(sel_ctrl[i], ln="Twist_Envelop", at="double", min=0, max=1, dv=0)
            cmds.setAttr((sel_ctrl[i] + ".Twist_Envelop"), e=True, keyable=True)

            cmds.addAttr(sel_ctrl[i], ln="Twist_Amptitute", at="double")
            cmds.setAttr((sel_ctrl[i] + ".Twist_Amptitute"), e=True, keyable=True)

            cmds.addAttr(sel_ctrl[i], ln="Twist_WaveLength", at="double")
            cmds.setAttr((sel_ctrl[i] + ".Twist_WaveLength"), e=True, keyable=True)

            cmds.addAttr(sel_ctrl[i], ln="Twist_Offset", at="double")
            cmds.setAttr((sel_ctrl[i] + ".Twist_Offset"), e=True, keyable=True)

            i+=1

        ####Make a Display Type
        cmds.select(upper_ctrl_name,lower_ctrl_name,middle_ctrl_name)
        sel_ctrl = cmds.ls(sl=True)
        len_sel_ctrl = len(sel_ctrl)
        i = 0
        while i < len_sel_ctrl:

            cmds.setAttr((sel_ctrl[i] + '.tx'), lock=True, keyable=False, channelBox=False)
            cmds.setAttr((sel_ctrl[i] + '.ty'), lock=True, keyable=False, channelBox=False)
            cmds.setAttr((sel_ctrl[i] + '.tz'), lock=True, keyable=False, channelBox=False)
            cmds.setAttr((sel_ctrl[i] + '.sx'), lock=True, keyable=False, channelBox=False)
            cmds.setAttr((sel_ctrl[i] + '.sy'), lock=True, keyable=False, channelBox=False)
            cmds.setAttr((sel_ctrl[i] + '.sz'), lock=True, keyable=False, channelBox=False)
            cmds.setAttr((sel_ctrl[i] + '.rx'), lock=True, keyable=False, channelBox=False)
            cmds.setAttr((sel_ctrl[i] + '.ry'), lock=True, keyable=False, channelBox=False)
            cmds.setAttr((sel_ctrl[i] + '.rz'), lock=True, keyable=False, channelBox=False)
            cmds.setAttr((sel_ctrl[i] + '.v'), lock=True, keyable=False, channelBox=False)

            i+=1

        cmds.select(cl=True)

    def get_controller(self,controller):
        #get the name
        if cmds.objExists(controller):
            cmds.select(controller + '*')
            sel_controller = cmds.ls(sl=True)
            len_sel_controller = len(sel_controller)
            new_name = controller + str(len_sel_controller)
        else:
            new_name = controller

        return new_name

    def set_shape(self,controller_name):
        #change the shape name
        controller_shape_name = controller_name + "Shape"
        controller_shape = cmds.listRelatives(controller_name,shapes=True)
        cmds.rename(controller_shape,controller_shape_name)

    def len_controller(self):
        controler_list = ['triangle_ctrl','square_ctrl','angle_ctrl','cross_ctrl','fat_cross_ctrl','circle_ctrl','arc_270_ctrl','arc_180_ctrl',
                          'spiral_ctrl','half_pyramid_ctrl','Pyramid_ctrl','half_spear_ctrl','cube_ctrl','sphere_ctrl','hexagon_ctrl','rombus_ctrl',
                          'rombus_two_ctrl','rombus_three_ctrl','cone_ctrl','single_thine_ctrl','single_normal_ctrl','single_fat_ctrl',
                          'double_thine_ctrl','double_normal_ctrl','double_fat_ctrl','four_thin_ctrl','four_normal_ctrl','four_fat_ctrl',
                          'eight_ctrl','ninty_thin_ctrl','ninty_normal_ctrl','ninty_fat_ctrl','oneeighty_thin_ctrl','oneeight_normal_ctrl',
                          'oneeight_fat_ctrl','transform_ctrl','footprint_ctrl','hand_ctrl','vision','arrows_on_ball_ctrl','cog_ctrl','sun_ctrl',
                          'pin_ctrl','jack_ctrl','nail_ctrl','double_nail_ctrl','four_nail_ctrl','dumbell_ctrl','pointer_ctrl','aim_ctrl','aim_two_ctrl','eye_ctrl']
        len_controler_list = len(controler_list)
        return controler_list







