import os
import rhinoscriptsyntax
import scriptcontext
import Rhino.Render
import System.Convert

def handle_render_content(render_content, target):
    child = render_content.FirstChild
    while child:
        handle_render_content(child, target)
        if child.IsImageBased():
            child.BeginChange(Rhino.Render.RenderContent.ChangeContexts.Program)
            source_path = System.Convert.ToString(child.GetParameter("filename"))
            source_file = os.path.basename(source_path)
            child.SetParameter("filename", target + os.sep + source_file)
            child.EndChange()
        child = child.NextSibling

target = rhinoscriptsyntax.BrowseForFolder()

for render_material in scriptcontext.doc.RenderMaterials:
    handle_render_content(render_material, target)

