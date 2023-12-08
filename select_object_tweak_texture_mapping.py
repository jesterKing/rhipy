import scriptcontext as sc
import Rhino
import Rhino.Render
obs = [ob for ob in sc.doc.Objects if ob.IsSelected(False)]
for ob in obs:
    render_material = ob.RenderMaterial
    if not render_material:
        continue
    mat = render_material.SimulatedMaterial(Rhino.Render.RenderTexture.TextureGeneration.Allow)
    if mat.IsPhysicallyBased and mat.PhysicallyBased:
        slot = Rhino.Render.RenderMaterial.StandardChildSlots.PbrBaseColor
    else:
        slot = Rhino.Render.RenderMaterial.StandardChildSlots.Diffuse
    diffuse_texture = render_material.GetTextureFromUsage(slot)
    context = Rhino.Render.RenderContent.ChangeContexts.UI
    repeat = diffuse_texture.GetRepeat()
    print(repeat)
    repeat *= 2
    repeat.Z = 0
    print(repeat)
    diffuse_texture.BeginChange(context)
    diffuse_texture.SetRepeat(repeat, context)
    diffuse_texture.EndChange()

