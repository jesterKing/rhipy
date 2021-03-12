import System
import Rhino.Display
import Rhino.Render
import scriptcontext
import random

# get object selection
object_selection = [ob for ob in scriptcontext.doc.Objects if ob.IsSelected]

# create material
render_material = Rhino.Render.RenderContent.Create(Rhino.Render.RenderMaterial.PaintMaterialGuid, Rhino.Render.RenderContent.ShowContentChooserFlags.None, scriptcontext.doc)
render_material.BeginChange(Rhino.Render.RenderContent.ChangeContexts.Program)
render_material.Name = "PYSCRIPTCREATED " + System.Guid.NewGuid().ToString()
random_color = Rhino.Display.Color4f(random.random(), random.random(), random.random(), 1.0)
render_material.SetParameter("color", random_color)
render_material.EndChange()

# assign
for ob in object_selection:
    print("Adding material", render_material.Name, "to", ob)
    ob.RenderMaterial = render_material
    ob.CommitChanges()
