import maya.cmds as cmds


class MAYA_NODE:

    def __init__(self):
        pass

    def reverse(self,name,
                input_ctrl,
                input_value,
                output_ctrl,
                output_value):
        cmds.createNode('reverse',n=name)
        #connectAttr -f locator1.translateX reverse1.inputX;
        #connectAttr -f reverse1.outputX locator2.translateX;
        cmds.connectAttr((input_ctrl + '.' + input_value ),
                         (name + '.inputX'),f=True)

        cmds.connectAttr((name + '.outputX' ),
                         (output_ctrl + '.' + output_value),f=True)
