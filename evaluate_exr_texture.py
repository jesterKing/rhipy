import Rhino

file_dialog = Rhino.UI.OpenFileDialog()
file_dialog.Filter = "EXR (*.exr)|*.exr"
if file_dialog.ShowDialog():
    print(file_dialog.FileName)
    render_texture = Rhino.Render.RenderContentType.NewContentFromTypeId(
        Rhino.Render.ContentUuids.HDRTextureType
    )
    render_texture.BeginChange(Rhino.Render.RenderContent.ChangeContexts.Program)
    render_texture.SetParameter("filename", file_dialog.FileName)
    render_texture.EndChange()
    evaluator = render_texture.CreateEvaluator(Rhino.Render.RenderTexture.TextureEvaluatorFlags.DisableLocalMapping | Rhino.Render.RenderTexture.TextureEvaluatorFlags.DisableAdjustment | Rhino.Render.RenderTexture.TextureEvaluatorFlags.DisableProjectionChange)
    size = render_texture.PixelSize2
    if size:
        width = size[0]
        height = size[1]
        half_pixel_u = 0.5 / width
        half_pixel_v = 0.5 / height
        col4f = Rhino.Display.Color4f()
        pt = Rhino.Geometry.Point3d.Origin
        dummy_duvw = Rhino.Geometry.Vector3d.Zero
        count = 0
        for y in range(height):
            for x in range(width):
                if count % 1013 == 0:
                    pt.X = float(x) / float(width) + half_pixel_u
                    pt.Y = float(y) / float(height) + half_pixel_v
                    pt.Z = 0.0
    
                    ok, col4f = evaluator.GetColor(pt, dummy_duvw, dummy_duvw, col4f)
    
                    if ok:
                        print col4f.R, col4f.G, col4f.B, col4f.A
            count += 1
