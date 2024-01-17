import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

def plotTetreahedron():
    # Vertices of a regular tetrahedron
    sqrt_2 = np.sqrt(2)
    vertices = np.array([
        [1, 0, -1 / sqrt_2],
        [-1, 0, -1 / sqrt_2],
        [0, 1, 1 / sqrt_2],
        [0, -1, 1 / sqrt_2]
    ])

    # Define the faces of the tetrahedron
    faces = [
        [vertices[0], vertices[1], vertices[2]],
        [vertices[0], vertices[1], vertices[3]],
        [vertices[0], vertices[2], vertices[3]],
        [vertices[1], vertices[2], vertices[3]]
    ]

    # Create a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Create a Poly3DCollection object for the faces
    poly3d = [[face[0], face[1], face[2]] for face in faces]
    tetra = Poly3DCollection(poly3d, facecolors='red', linewidths=1, edgecolors='r', alpha=.25)

    # Add the tetrahedron to the plot
    ax.add_collection3d(tetra)

    # Auto scale to the mesh size
    scale = np.concatenate([v.flatten() for v in vertices])
    ax.auto_scale_xyz(scale, scale, scale)

    # Set labels and title
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.set_title('Red Tetrahedron')

    # Show the plot
    plt.show()

def plotCube():
    # Define vertices of the cube
    vertices = np.array([
        [1, 1, -1],
        [1, -1, -1],
        [-1, -1, -1],
        [-1, 1, -1],
        [1, 1, 1],
        [1, -1, 1],
        [-1, -1, 1],
        [-1, 1, 1]
    ])

    # Define the faces of the cube
    faces = [
        [vertices[0], vertices[1], vertices[2], vertices[3]],
        [vertices[4], vertices[5], vertices[6], vertices[7]],
        [vertices[0], vertices[3], vertices[7], vertices[4]],
        [vertices[1], vertices[2], vertices[6], vertices[5]],
        [vertices[2], vertices[3], vertices[7], vertices[6]],
        [vertices[0], vertices[1], vertices[5], vertices[4]]
    ]

    # Create a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Create a Poly3DCollection object for the faces
    poly3d = [[face[0], face[1], face[2], face[3]] for face in faces]
    cube = Poly3DCollection(poly3d, facecolors='blue', linewidths=1, edgecolors='b', alpha=.25)

    # Add the cube to the plot
    ax.add_collection3d(cube)

    # Auto scale to the mesh size
    scale = np.concatenate([v.flatten() for v in vertices])
    ax.auto_scale_xyz(scale, scale, scale)

    # Set labels and title
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.set_title('Blue Cube')

    # Show the plot
    plt.show()

def plotOctahedron():
    # Vertices of a regular octahedron
    vertices = np.array([
        [1, 0, 0],
        [-1, 0, 0],
        [0, 1, 0],
        [0, -1, 0],
        [0, 0, 1],
        [0, 0, -1]
    ])

    # Define the faces of the octahedron
    faces = [
        [vertices[0], vertices[2], vertices[4]],
        [vertices[2], vertices[1], vertices[4]],
        [vertices[1], vertices[3], vertices[4]],
        [vertices[3], vertices[0], vertices[4]],
        [vertices[0], vertices[2], vertices[5]],
        [vertices[2], vertices[1], vertices[5]],
        [vertices[1], vertices[3], vertices[5]],
        [vertices[3], vertices[0], vertices[5]]
    ]

    # Create a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Create a Poly3DCollection object for the faces
    poly3d = [[face[0], face[1], face[2]] for face in faces]
    octa = Poly3DCollection(poly3d, facecolors='green', linewidths=1, edgecolors='g', alpha=.25)

    # Add the octahedron to the plot
    ax.add_collection3d(octa)

    # Auto scale to the mesh size
    scale = np.concatenate([v.flatten() for v in vertices])
    ax.auto_scale_xyz(scale, scale, scale)

    # Set labels and title
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.set_title('Green Octahedron')

    # Show the plot
    plt.show()


def plotDodecahedron():
    # Golden ratio
    phi = (1 + np.sqrt(5)) / 2

    # Vertices of a dodecahedron
    vertices = np.array([
        [1, 1, 1],
        [1, 1, -1],
        [1, -1, 1],
        [1, -1, -1],
        [-1, 1, 1],
        [-1, 1, -1],
        [-1, -1, 1],
        [-1, -1, -1],
        [0, phi, 1/phi],
        [0, phi, -1/phi],
        [0, -phi, 1/phi],
        [0, -phi, -1/phi],
        [1/phi, 0, phi],
        [1/phi, 0, -phi],
        [-1/phi, 0, phi],
        [-1/phi, 0, -phi],
        [phi, 1/phi, 0],
        [phi, -1/phi, 0],
        [-phi, 1/phi, 0],
        [-phi, -1/phi, 0]
    ])

    # Define the faces of the dodecahedron
    faces = [
        [vertices[0], vertices[8], vertices[4], vertices[14], vertices[12]],
        [vertices[0], vertices[12], vertices[13], vertices[1], vertices[16]],
        [vertices[0], vertices[16], vertices[17], vertices[2], vertices[8]],
        [vertices[1], vertices[13], vertices[5], vertices[9], vertices[18]],
        [vertices[1], vertices[18], vertices[19], vertices[3], vertices[16]],
        [vertices[2], vertices[17], vertices[3], vertices[19], vertices[11]],
        [vertices[2], vertices[11], vertices[10], vertices[6], vertices[8]],
        [vertices[3], vertices[17], vertices[16], vertices[1], vertices[13]],
        [vertices[4], vertices[8], vertices[6], vertices[10], vertices[15]],
        [vertices[4], vertices[15], vertices[14], vertices[0], vertices[12]],
        [vertices[5], vertices[13], vertices[12], vertices[4], vertices[14]],
        [vertices[5], vertices[14], vertices[15], vertices[7], vertices[9]],
        [vertices[6], vertices[10], vertices[11], vertices[2], vertices[8]],
        [vertices[7], vertices[15], vertices[10], vertices[6], vertices[11]],
        [vertices[7], vertices[11], vertices[19], vertices[3], vertices[17]],
        [vertices[7], vertices[17], vertices[16], vertices[1], vertices[18]],
        [vertices[7], vertices[18], vertices[9], vertices[5], vertices[14]],
        [vertices[9], vertices[15], vertices[7], vertices[11], vertices[10]],
        [vertices[9], vertices[10], vertices[6], vertices[8], vertices[0]],
        [vertices[9], vertices[0], vertices[12], vertices[4], vertices[14]]
    ]

    # Create a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Create a Poly3DCollection object for the faces
    poly3d = [[face[0], face[1], face[2], face[3], face[4]] for face in faces]
    dodeca = Poly3DCollection(poly3d, facecolors='purple', linewidths=1, edgecolors='black', alpha=.25)

    # Add the dodecahedron to the plot
    ax.add_collection3d(dodeca)

    # Auto scale to the mesh size
    scale = np.concatenate([v.flatten() for v in vertices])
    ax.auto_scale_xyz(scale, scale, scale)

    # Set labels and title
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.set_title('Purple Dodecahedron')

    # Show the plot
    plt.show()

plotDodecahedron()
#plotOctahedron()
#plotTetreahedron()
#plotCube()