import bpy
import bmesh
import numpy as np
from PIL import Image

# Load image and convert to grayscale
im = Image.open("/home/radmin/Documents/python projects/blender/image.png").convert("L")

# Convert to numpy array
im_np = np.array(im)

# Create a new mesh
mesh = bpy.data.meshes.new("image_mesh")

# Create a new object with the mesh
obj = bpy.data.objects.new("image_obj", mesh)

# Add the object to the scene
bpy.context.collection.objects.link(obj)

# Create vertices and faces
vertices = []
faces = []
for y in range(im_np.shape[0]):
    for x in range(im_np.shape[1]):
        brightness = im_np[y, x]
        z = brightness / 255 * 100
        vertices.append((x, y, z))
        if y < im_np.shape[0] - 1 and x < im_np.shape[1] - 1:
            faces.append((y * im_np.shape[1] + x, y * im_np.shape[1] + x + 1, (y + 1) * im_np.shape[1] + x + 1))
            faces.append((y * im_np.shape[1] + x, (y + 1) * im_np.shape[1] + x + 1, (y + 1) * im_np.shape[1] + x))

# Set the vertices and faces of the mesh
mesh.from_pydata(vertices, [], faces)

# Update the mesh
mesh.update()

bpy.ops.object.mode_set(mode='OBJECT')
