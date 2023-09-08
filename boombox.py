import maya.cmds as cmds

def get_edge_length(vertex1, vertex2):
    edge_length = (
        (vertex2[0] - vertex1[0]) ** 2
        + (vertex2[1] - vertex1[1]) ** 2
        + (vertex2[2] - vertex1[2]) ** 2
    ) ** 0.5

    return round(edge_length, 3)


# Clear selection
cmds.select(clear=True)

# Constants
EDGE_LENGTH = 0.104

xCoordinate_outer_side1 = -14.345
xCoordinate_inner_side1 = -14.305

zCoordinate_outer_side2 = 9.725
zCoordinate_inner_side2 = 9.765

xCoordinate_outer_side3 = -28.248
xCoordinate_inner_side3 = -28.288

yCoordinates = [18.006, 17.910, 17.870, 0.627, 0.723, 0.763]

# Get all the edges
edges = cmds.polyListComponentConversion("pPlane33", toEdge=True)
edge_list = cmds.ls(edges, flatten=True)

for edge in edge_list:
    edgeName = format(edge)

    vertices = cmds.polyListComponentConversion(edge, toVertex=True)
    vertex_list = cmds.ls(vertices, flatten=True)

    # Check weather the edge contains 2 vertices
    if len(vertex_list) != 2:
        continue

    # Get the coordinates of the two vertices
    vertex1 = cmds.pointPosition(vertex_list[0], w=True)
    vertex2 = cmds.pointPosition(vertex_list[1], w=True)

    edgeLength = get_edge_length(vertex1, vertex2)
    if edgeLength != EDGE_LENGTH:
        continue

    vertex1XCoordiante = round(vertex1[0], 3)
    vertex2XCoordiante = round(vertex2[0], 3)

    vertex1YCoordiante = round(vertex1[1], 3)
    vertex2YCoordiante = round(vertex2[1], 3)

    vertex1ZCoordiante = round(vertex1[2], 3)
    vertex2ZCoordiante = round(vertex2[2], 3)

    if (
        #Side 1
        (
            vertex1XCoordiante == xCoordinate_outer_side1
            and vertex2XCoordiante == xCoordinate_outer_side1
        )
        or (
            vertex1XCoordiante == xCoordinate_inner_side1
            and vertex2XCoordiante == xCoordinate_inner_side1
        )
        #Side 2
        or (
            vertex1ZCoordiante == zCoordinate_outer_side2
            and vertex2ZCoordiante == zCoordinate_outer_side2
        )
        or (
            vertex1ZCoordiante == zCoordinate_inner_side2
            and vertex2ZCoordiante == zCoordinate_inner_side2
        )
        #Side 3
        or (
            vertex1XCoordiante == xCoordinate_outer_side3
            and vertex2XCoordiante == xCoordinate_outer_side3
        )
        or (
            vertex1XCoordiante == xCoordinate_inner_side3
            and vertex2XCoordiante == xCoordinate_inner_side3
        )
    ):
        if vertex1YCoordiante in yCoordinates and vertex2YCoordiante in yCoordinates:
            continue
        cmds.select(edgeName, add=True)
