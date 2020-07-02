from Autodesk.Revit.DB import*
from Autodesk.Revit.DB.Architecture import*
from Autodesk.Revit.DB.Analysis import*
from Autodesk.Revit.UI import*

import clr
clr.AddReferenceByPartialName('PresentationCore')
clr.AddReferenceByPartialName('PresentationFramework')
clr.AddReferenceByPartialName('System.Windows.Forms')
import System.Windows

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document
selection = [ doc.GetElement( elId) for elId in __revit__.ActiveUIDocument.Selection.GetElementIds() ]

def alert(msg):
    TaskDialog.Show('pyRevit', msg)

def quit():
    __window__.Close()

if len(selection) > 0:
    el = selection[0]