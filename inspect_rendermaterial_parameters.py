import scriptcontext as sc
import clr

clr.AddReference('System.Xml')
import System.Xml as xml

rms = list(sc.doc.RenderMaterials)

for rm in rms:
    print('material:', rm.Name)
    rmdoc = xml.XmlDocument()
    rmdoc.LoadXml(rm.Xml)
    params = rmdoc.DocumentElement.SelectSingleNode('parameters')
    param = params.FirstChild
    while param:
        param_type = param.GetAttributeNode('type')
        try:
            param_type = param_type.Value
        except:
            param_type = 'N/A'
    
        print('parameter', param.Name, 'is a', param_type, 'with value', param.InnerXml)
        param = param.NextSibling
