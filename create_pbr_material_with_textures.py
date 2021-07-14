import Rhino
import scriptcontext as sc

bitmap_texture_type_guid = Rhino.Render.ContentUuids.BitmapTextureType
pbr_material_type_guid = Rhino.Render.ContentUuids.PhysicallyBasedMaterialType

bmtex = Rhino.Render.RenderContentType.NewContentFromTypeId(bitmap_texture_type_guid)
bmtex.Filename = "C:\\Users\\Nathan\\Pictures\\uvtester.png"

simtex = bmtex.SimulatedTexture(Rhino.Render.RenderTexture.TextureGeneration.Allow)

# first create an empty PBR material
pbr_rm = Rhino.Render.RenderContentType.NewContentFromTypeId(pbr_material_type_guid)

# to get to a Rhino.DocObjects.PhysicallyBasedMaterial we need to simulate the
# render material first.
sim = pbr_rm.SimulatedMaterial(Rhino.Render.RenderTexture.TextureGeneration.Allow)

# from the simulated material we can get the Rhino.DocObjects.PhysicallyBasedMaterial
pbr = sim.PhysicallyBased

# now we have an instance of a type that has all the API you need to set the PBR
# properties. For simple glass we set color to white, opacity to 0 and opacity
# IOR to 1.52
pbr.Opacity = 0.0
pbr.OpacityIOR = 1.52
pbr.BaseColor = Rhino.Display.Color4f.White

pbr.SetTexture(simtex.Texture(), Rhino.DocObjects.TextureType.PBR_BaseColor)

# convert it back to RenderMaterial
new_pbr = Rhino.Render.RenderMaterial.FromMaterial(pbr.Material, sc.doc)
# Set a good name
new_pbr.Name = "My Own PBR Glass"

# Add it to the document
sc.doc.RenderMaterials.Add(new_pbr)
