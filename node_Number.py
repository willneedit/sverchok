import bpy
from node_s import *

class NumberNode(Node, SverchCustomTreeNode):
    ''' Number '''
    bl_idname = 'NumberNode'
    bl_label = 'Number'
    bl_icon = 'OUTLINER_OB_EMPTY'
    
    def init(self, context):
        self.inputs.new('StringsSocket', "Number", "Number")
        self.outputs.new('StringsSocket', "Number", "Number")
        

    def update(self):
        # inputs
        if len(self.inputs['Number'].links)>0 and type(self.inputs['Number'].links[0].from_socket) == bpy.types.StringsSocket:
            if not self.inputs['Number'].node.socket_value_update:
                self.inputs['Number'].node.update()
            Number = self.inputs['Number'].links[0].from_socket.StringsProperty
        else:
            Number = []
        
        # outputs
        if 'Number' in self.outputs and len(self.outputs['Number'].links)>0:
            if not self.outputs['Number'].node.socket_value_update:
                self.inputs['Number'].node.update()
            num = eval(Number)
            #level = self.levels(num)
            result = self.inte(num)
            #print (result)
            
            self.outputs['Number'].StringsProperty = str(result)
    
    def update_socket(self, context):
        self.update()
    
    def inte(self, l):
        if type(l) == int or type(l) == float:
            t = round(l)
        else:
            t = []
            for i in l:
                i = self.inte(i)
                t.append(i)
        return t
            
    
    def levels(self, list):
        level = 1
        for n in list:
            if type(n) == list:
                level += self.levels(n)
            return level


def register():
    bpy.utils.register_class(NumberNode)
    
def unregister():
    bpy.utils.unregister_class(NumberNode)

if __name__ == "__main__":
    register()