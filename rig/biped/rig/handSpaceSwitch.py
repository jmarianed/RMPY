from RMPY.rig import rigBase
from RMPY.rig.spaceSwitches import rigEnumSpaceSwitch


class HandSpaceSwitch(rigBase.RigBase):
    def __init__(self, *args, **kwargs):
        super(HandSpaceSwitch, self).__init__(*args, **kwargs)

    def build(self, hand_rig, world_rig, arm_rig):
        enum_space_switch = rigEnumSpaceSwitch.RigEnumSpaceSwitch(world_rig.tip, arm_rig.rig_arm.joints[-2],
                                                                  alias_list=['world', 'arm'],
                                                                  attribute_name='space',
                                                                  control=hand_rig.controls[0],
                                                                  orient=True)
        enum_space_switch.add_object(hand_rig.controls[0])

