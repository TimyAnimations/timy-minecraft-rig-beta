import os
import bpy
import bpy.utils.previews

custom_icons = None

class customIconImport(bpy.types.Operator):
	bl_idname = 'timy_minecraft_rig_beta.icons'
	bl_label = 'timy_minecraft_rig_beta'
	
	def execute(self,context):
		icons_dir = os.path.join(os.path.dirname(__file__), "icons")
		
		return {icons_dir}
		
def register():
	bpy.utils.register_class(customIconImport)
	
def unregister():
	bpy.utils.unregister_class(customIconImport)