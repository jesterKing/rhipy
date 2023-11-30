import System
import Rhino.Display
import Rhino.Render

import scriptcontext
import random

# get object selection
object_selection = [ob for ob in scriptcontext.doc.Objects if ob.IsSelected(False)]

# only if we have a selection do the work
if object_selection:
    # create material
    render_material = Rhino.Render.RenderContent.Create(
        System.Guid("E6CD1973-B739-496E-AB69-32957FA48492"),
        Rhino.Render.RenderContent.ShowContentChooserFlags.None,
        scriptcontext.doc)
    render_material.BeginChange(Rhino.Render.RenderContent.ChangeContexts.Program)
    render_material.Name = "Double-Sided Material " + System.Guid.NewGuid().ToString()
    
    front_material = Rhino.Render.RenderContent.Create(
        Rhino.Render.RenderMaterial.MetalMaterialGuid,
        render_material,
        "front",
        Rhino.Render.RenderContent.ShowContentChooserFlags.None,
        scriptcontext.doc)
    
    back_material = Rhino.Render.RenderContent.Create(
        Rhino.Render.RenderMaterial.PlasterMaterialGuid,
        render_material,
        "back",
        Rhino.Render.RenderContent.ShowContentChooserFlags.None,
        scriptcontext.doc)
    random_color1 = Rhino.Display.Color4f(
        random.random(),
        random.random(),
        random.random(),
        1.0)
    random_color2 = Rhino.Display.Color4f(
        random.random(),
        random.random(),
        random.random(),
        1.0)
    # set color for front material
    front_material.BeginChange(Rhino.Render.RenderContent.ChangeContexts.Program)
    front_material.SetParameter("color", random_color1)
    # set color for back material
    back_material.BeginChange(Rhino.Render.RenderContent.ChangeContexts.Program)
    back_material.SetParameter("color", random_color2)
    render_material.EndChange()
    
    # assign
    for ob in object_selection:
        print("Adding material", render_material.Name, "to", ob)
        ob.RenderMaterial = render_material
        ob.CommitChanges()
