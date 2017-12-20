import os
import bpy
import bpy.utils.previews

custom_icons = None

class customIconImport(bpy.types.Operator):
	bl_idname = 'timy_minecraft_rig_beta.icons'
	bl_label = 'timy_minecraft_rig_beta'
	
	def execute(self,context):
		global custom_icons
		custom_icons = bpy.utils.previews.new()
		icons_dir = os.path.join(os.path.dirname(__file__), "icons")
		custom_icons.load("custom_icon", os.path.join(icons_dir, "test_icon.png"), 'IMAGE')
		
		return {custom_icons["custom_icon"].icon_id}
		
def register():
	bpy.utils.register_class(customIconImport)
	
def unregister():
	bpy.utils.unregister_class(customIconImport)