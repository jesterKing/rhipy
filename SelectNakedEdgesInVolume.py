"""
Select naked edges of a mesh bounded by a volume.

Only naked edges that fully are contained within
the volume will be selected.

v0.0.1
"""

__author__ = "Nathan 'jesterKing' Letwory <nathan@mcneel.com>"
__version__ = "0.0.1"

import Rhino


def getMeshBoundaries(mesh):
    topoEdges = mesh.TopologyEdges
    idxType = Rhino.Geometry.ComponentIndexType.MeshTopologyEdge
    
    nakedEdges = []
    
    for i in xrange(0,topoEdges.Count):
        conFaces = topoEdges.GetConnectedFaces(i)
        if len(conFaces)==1:
            verts = topoEdges.GetTopologyVertices(i)
            nakedEdges.append((i, verts))  
    return nakedEdges
    

def DoSelection():
    rc, objRef = Rhino.Input.RhinoGet.GetOneObject("Select mesh", True, Rhino.DocObjects.ObjectType.Mesh)
    if rc != Rhino.Commands.Result.Success:
        return rc
    mesh = objRef.Mesh()
    
    if mesh.IsClosed:
        print "Can't select naked edges on closed mesh."
        return Rhino.Commands.Result.Failure
    obj = objRef.Object()
    
    rc, objRef = Rhino.Input.RhinoGet.GetOneObject("Select polysurface volume", True, Rhino.DocObjects.ObjectType.PolysrfFilter)
    if rc != Rhino.Commands.Result.Success:
        return rc
    brep = objRef.Brep()
    if None == brep:
        return Rhino.Commands.Result.Failure

    if not brep.IsSolid:
        print "Polysurface is not closed."
        return
        
    for o in Rhino.RhinoDoc.ActiveDoc.Objects:
        o.Select(False)
    
    Rhino.RhinoDoc.ActiveDoc.Views.RedrawEnabled = False

    topoEdges = mesh.TopologyEdges
    idxType = Rhino.Geometry.ComponentIndexType.MeshTopologyEdge
    
    nakedEdges = getMeshBoundaries(mesh)
    
    count = 0

    for e in nakedEdges:
        i = e[0]
        edge = topoEdges.EdgeLine(i)
        
        fromInside = brep.IsPointInside(edge.From, Rhino.RhinoMath.SqrtEpsilon, True)
        toInside = brep.IsPointInside(edge.To, Rhino.RhinoMath.SqrtEpsilon, True)
        
        if fromInside and toInside:
            compIdx = Rhino.Geometry.ComponentIndex(idxType, i)
            obselrc = obj.SelectSubObject(compIdx, True, True, True)
            count += 1
    Rhino.RhinoDoc.ActiveDoc.Views.RedrawEnabled = True
    Rhino.RhinoDoc.ActiveDoc.Views.Redraw()
    print "Selected", count, "naked edges inside volume."


DoSelection()
