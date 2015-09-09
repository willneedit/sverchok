# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import bpy
from sverchok.node_tree import SverchCustomTreeNode
from sverchok.data_structure import (updateNode)


class SvBvhOverlapNode(bpy.types.Node, SverchCustomTreeNode):
    ''' BVH Tree Overlap '''
    bl_idname = 'SvBvhOverlapNode'
    bl_label = 'bvh_overlap'
    bl_icon = 'OUTLINER_OB_EMPTY'

    def sv_init(self, context):
        self.inputs.new('StringsSocket', 'BVH_tree_list(A)')
        self.inputs.new('StringsSocket', 'BVH_tree_list(B)')
        self.outputs.new('StringsSocket', 'outlist')

    def process(self):
        out = []
        for i, i2 in zip(self.inputs[0].sv_get(), self.inputs[1].sv_get()):
            out.append(i.overlap(i2))
        self.outputs[0].sv_set(out)

    def update_socket(self, context):
        self.update()


def register():
    bpy.utils.register_class(SvBvhOverlapNode)


def unregister():
    bpy.utils.unregister_class(SvBvhOverlapNode)
