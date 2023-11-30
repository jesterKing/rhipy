import Rhino
import scriptcontext as sc

render_texture = Rhino.Render.RenderContent.Create(sc.doc, Rhino.Render.ContentUuids.BitmapTextureType)
decal_params = Rhino.Render.DecalCreateParams()
decal_params.TextureInstanceId = render_texture.Id
decal_params.DecalMapping = Rhino.Render.DecalMapping.Planar
decal_params.DecalProjection = Rhino.Render.DecalProjection.Both
decal_params.Origin = Rhino.Geometry.Point3d(0, 0, 0)
decal_params.VectorAcross = Rhino.Geometry.Vector3d(5, 0, 0)
decal_params.VectorUp = Rhino.Geometry.Vector3d(0, 5, 0)
decal = Rhino.Render.Decal.Create(decal_params)
obs = [ob for ob in sc.doc.Objects if ob.IsSelected(False)]
if len(obs)>0:
    ob = obs[0]
    ob.Attributes.Decals.Add(decal)
    ob.CommitChanges()

sc.doc.Views.Redraw()
