# Big thanks to Filip Nekic from https://bimworkaround.com/ who found way to open closed workset with a script
# -------------------------- IMPORTS --------------------------------
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# Import DocumentManager and TransactionManager
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

from System.Collections.Generic import *

# Import RevitAPI
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Electrical import *
from Autodesk.Revit.DB.Analysis import *

uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application

# Import ToDSType(bool) extension method
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

# Import timestamp
import datetime
import time

# Import System
import sys
sys.path.append('C:\Program Files (x86)\IronPython 2.7\Lib')
import os

# ------------------------- INPUTS -----------------------------

#docList = IN[0]
dataList = list()

#------------------------ SCRIPT ---------------------------------

# Current doc/app/ui
doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application
uidoc = uiapp.ActiveUIDocument


# ----------------WORKSET COLLECTOR--------------------

worksetCollector = FilteredWorksetCollector(doc).OfKind(WorksetKind.UserWorkset).ToWorksets()
worksets = UnwrapElement(worksetCollector)
wNames = []

for w in worksetCollector:
    name = str(w.Name)
    wNames.append(name)


openWorksets = []
closedWorksets = []

# Open workset workaround - creates element move into a workset and show, delete element

for w in worksetCollector:
    if not w.IsOpen:
        TransactionManager.Instance.EnsureInTransaction(doc)
        typeID = FilteredElementCollector(doc).WhereElementIsElementType().OfClass(CableTray).FirstElementId()
        levelID = FilteredElementCollector(doc).OfClass(Level).FirstElementId()
        ct = CableTray.Create(doc, typeID, XYZ(0, 0, 0), XYZ(0, 0, 1), levelID)
        elementId = ct.Id

        # Changing workset of cable tray to workset which we want to open
        # Electrician workset parameter - TODO HERE
        wsparam = ct.get_Parameter(BuiltInParameter.ELEM_PARTITION_PARAM)
        if wsparam != None and not wsparam.IsReadOnly:
            wsparam.Set(w.Id.IntegerValue)
        ids = List<ElementId>() # add list icollector
        ids.Add(elementId)
        #This command will actualy open workset
        uidoc.ShowElements(ids)

        # Delete temporary cable tray
        doc.Delete(elementId)
        TransactionManager.Instance.TransactionTaskDone()

OUT = "done"