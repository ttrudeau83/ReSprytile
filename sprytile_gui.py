import bpy

# The GUI uses the gpu module and works on every platform. (The old Apple Silicon
# variant relied on the bgl module, which was removed in Blender 5.0.)
import spryTile_OS_EverythingElse
classes = (spryTile_OS_EverythingElse)

classe = classes
def register():
    for c in classe.classes:
        bpy.utils.register_class(c)


def unregister():
    for c in classe.classes:
        bpy.utils.unregister_class(c)


if __name__ == '__main__':
    register()
