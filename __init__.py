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

bl_info = {
	"name":        "Timy's Minecraft Rig Beta",
	"description": "An advanced rig for Minecraft Characters",
	"author":      "Timy Animations",
	"version":     (7, 0, 2),
	"blender":     (2, 7, 7),
	"location":    "View 3D > Rigs",
	"warning":     "",  # used for warning icon and text in addons panel
	"wiki_url":    "",
	"tracker_url": "https://goo.gl/forms/99l2dvY3Ky0U5sDQ2",
	"category":    "System"
	}


import os
import bpy
import bpy.utils.previews

# updater ops import, all setup in this file
from . import addon_updater_ops


class rigTimyMinecraftRig(bpy.types.Panel):
	"""Creates a Custom Rig Mesh UI Panel"""
	bl_label = "Add Rig"
	bl_idname = "RIG_timy_minecraft_rig"
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'TOOLS'
	bl_category = "Rigs"

	def draw(self, context):
		layout = self.layout

		# Call to check for update in background
		# note: built-in checks ensure it runs at most once
		# and will run in the background thread, not blocking
		# or hanging blender
		# Internal also checks to see if auto-check enabeld
		# and if the time interval has passed
		addon_updater_ops.check_for_update_background(context)
		row = layout.row()
		row.label(text="Test Icon", icon_value=custom_icons["custom_icon"].icon_id)
		if bpy.app.version[1] >= 78:
			row = layout.row()
			row.label(icon="ERROR", text=" In Blender 2.78+, Restart Blender between appending multiple rigs")
		row = layout.row()
		row.operator("object.append_timy_minecraft_rig" , text = "Timy's Minecraft Rig")

		# call built-in function with draw code/checks
		addon_updater_ops.update_notice_box_ui(self, context)

def append_timy_minecraft_rig(context):
	
	import os

	script_file = os.path.realpath(__file__)
	script_directory = os.path.dirname(script_file)
	
	print(script_file)
	print(script_directory)
	
	blendfile = script_directory+"\\rigs/timys_minecraft_rig.blend"
	section   = "/Group/"
	object    = "timyv7"

	filepath  = blendfile + section + object
	directory = blendfile + section
	filename  = object
	
	print(filepath)
	print(directory)
	print(filename)
	
	try:
		bpy.ops.wm.append(filepath=filepath, filename=filename,directory=directory)

		section ="/Text/"
		object = "timy_minecraft_rig_ui.py"
		
		filepath  = blendfile + section + object
		directory = blendfile + section
		filename  = object
		
		bpy.ops.wm.append(filepath=filepath, filename=filename,directory=directory)
		import timy_minecraft_rig_ui
		
	except:
		print("Failed to append rig")
            
class appendTimyMinecraftRig(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.append_timy_minecraft_rig"
    bl_label = ""

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        append_timy_minecraft_rig(context)
        return {'FINISHED'}


# demo bare-bones preferences
class TimyMinecraftRigPreferences(bpy.types.AddonPreferences):
	bl_idname = __package__

	# addon updater preferences

	auto_check_update = bpy.props.BoolProperty(
		name = "Auto-check for Update",
		description = "If enabled, auto-check for updates using an interval",
		default = False,
		)
	
	updater_intrval_months = bpy.props.IntProperty(
		name='Months',
		description = "Number of months between checking for updates",
		default=0,
		min=0
		)
	updater_intrval_days = bpy.props.IntProperty(
		name='Days',
		description = "Number of days between checking for updates",
		default=7,
		min=0,
		)
	updater_intrval_hours = bpy.props.IntProperty(
		name='Hours',
		description = "Number of hours between checking for updates",
		default=0,
		min=0,
		max=23
		)
	updater_intrval_minutes = bpy.props.IntProperty(
		name='Minutes',
		description = "Number of minutes between checking for updates",
		default=0,
		min=0,
		max=59
		)

	def draw(self, context):
		
		layout = self.layout

		# updater draw function
		addon_updater_ops.update_settings_ui(self,context)

custom_icons = None
		
def register():
	
	global custom_icons
    custom_icons = bpy.utils.previews.new()
    script_path = bpy.context.space_data.text.filepath
    icons_dir = os.path.join(os.path.dirname(script_path), "icons")
    custom_icons.load("custom_icon", os.path.join(icons_dir, "test_icon.png"), 'IMAGE')


	# addon updater code and configurations
	# in case of broken version, try to register the updater first
	# so that users can revert back to a working version
	addon_updater_ops.register(bl_info)

	# register the example panel, to show updater buttons
	bpy.utils.register_class(TimyMinecraftRigPreferences)
	bpy.utils.register_class(rigTimyMinecraftRig)
	bpy.utils.register_class(appendTimyMinecraftRig)


def unregister():

	global custom_icons
    bpy.utils.previews.remove(custom_icons)

	# addon updater unregister
	addon_updater_ops.unregister()

	# register the example panel, to show updater buttons
	bpy.utils.unregister_class(TimyMinecraftRigPreferences)
	bpy.utils.unregister_class(rigTimyMinecraftRig)
	bpy.utils.unregister_class(appendTimyMinecraftRig)


