"""Run inside Blender with BLENDER_USER_CONFIG set to the project profile."""
import bpy
bpy.context.preferences.view.language = 'en_US'
bpy.context.preferences.view.use_translate_interface = False
bpy.context.preferences.view.use_translate_tooltips = False
bpy.ops.wm.save_userpref()
print('Blender interface configured in English.')
