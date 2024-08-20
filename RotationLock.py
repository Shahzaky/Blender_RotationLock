# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <https://www.gnu.org/licenses/>.

import bpy

bl_info = {
    "name": "Rotation Lock",
    "blender": (3, 3, 0),
    "category": "3D View",
}

class VIEW3D_PT_view_rotation_lock_toggle(bpy.types.Panel):
    bl_label = "Rotation Lock"
    bl_idname = "VIEW3D_PT_view_rotation_lock_toggle"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'View'
    
    def draw(self, context):
        layout = self.layout
        view = context.space_data.region_3d
        row = layout.row()
        row.prop(view, "lock_rotation", text="Lock View Rotation", toggle=True)

def register():
    bpy.utils.register_class(VIEW3D_PT_view_rotation_lock_toggle)

def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_view_rotation_lock_toggle)

if __name__ == "__main__":
    register()
