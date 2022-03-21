# Outputs selected elements

import clr

clr.AddReference("RevitNodes")

import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

clr.AddReference("RevitAPI")
clr.AddReference("RevitAPIUI")

import Autodesk
#from Autodesk.Revit.DB import *
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI.Selection import *

# Current doc/app/ui
doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
uidoc = uiapp.ActiveUIDocument

selectedIds = uidoc.Selection.GetElementIds()
elements = Document.GetElement(doc, selectedIds[0])

OUT = elements