import Rhino as rh
import Rhino.Render as rr
import Rhino.DocObjects as rd
import scriptcontext as sc

bitmap_texture_type_guid = rr.ContentUuids.BitmapTextureType
pbr_material_type_guid = rr.ContentUuids.PhysicallyBasedMaterialType

bmtex = rr.RenderContentType.NewContentFromTypeId(bitmap_texture_type_guid)
bmtex.Filename = "C:\\Users\\Nathan\\Pictures\\uvtester.png"

simtex = bmtex.SimulatedTexture(rr.RenderTexture.TextureGeneration.Allow)

# first create an empty PBR material
pbr_rm = rr.RenderContentType.NewContentFromTypeId(pbr_material_type_guid)

# to get to a Rhino.DocObjects.PhysicallyBasedMaterial we need to simulate the
# render material first.
sim = pbr_rm.SimulatedMaterial(rr.RenderTexture.TextureGeneration.Allow)

# from the simulated material we can get the Rhino.DocObjects.PhysicallyBasedMaterial
pbr = sim.PhysicallyBased

# now we have an instance of a type that has all the API you need to set the PBR
# properties. For simple glass we set color to white, opacity to 0 and opacity
# IOR to 1.52
pbr.Opacity = 0.0
pbr.OpacityIOR = 1.52
pbr.BaseColor = rh.Display.Color4f.White

pbr.SetTexture(simtex.Texture(), rd.TextureType.PBR_BaseColor)

# convert it back to RenderMaterial
new_pbr = rr.RenderMaterial.FromMaterial(pbr.Material, sc.doc)
# Set a good name
new_pbr.Name = "My Own PBR Glass"

# Add it to the document
sc.doc.RenderMaterials.Add(new_pbr)
