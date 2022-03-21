import clr
from System.Collections.Generic import List

# Import RevitAPI
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

# Import DocumentManager and TransactionManager
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager


doc = DocumentManager.Instance.CurrentDBDocument

#------------------------ VIEWS ---------------------------------

# Retrieve all sheets includes placeholders
def getAllSheets(doc):
    sheets = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Sheets)
    return sheets

def getAllLegends(doc):
    legends = []
    elems = FilteredElementCollector(doc).OfClass(View).ToElements()
    for e in elems:
        if e.ViewType == ViewType.Legend:
            legends.append(e)
    return legends

def getAllSchedules(doc):
    return [v for v in FilteredElementCollector(doc).OfClass(View).ToElements() if v.ViewType == ViewType.Schedule]

def getAllFloorplans(doc):
    return [v for v in FilteredElementCollector(doc).OfClass(View).ToElements() if v.ViewType == ViewType.FloorPlan]

def getAllDraftingViews(doc):
    return [v for v in FilteredElementCollector(doc).OfClass(View).ToElements() if v.ViewType == ViewType.DraftingView]

def getAllAreaPlans(doc):
    return [v for v in FilteredElementCollector(doc).OfClass(View).ToElements() if v.ViewType == ViewType.AreaPlan]

def getAllSections(doc):
    return [v for v in FilteredElementCollector(doc).OfClass(View).ToElements() if v.ViewType == ViewType.Section]

def getAllThreeDs(doc):
    return [v for v in FilteredElementCollector(doc).OfClass(View).ToElements() if v.ViewType == ViewType.ThreeD]

def getAllElevations(doc):
    return [v for v in FilteredElementCollector(doc).OfClass(View).ToElements() if v.ViewType == ViewType.Elevation]

def getAllCeilingPlans(doc):
    return [v for v in FilteredElementCollector(doc).OfClass(View).ToElements() if v.ViewType == ViewType.CeilingPlan]

def getAllThreeDs(doc):
    return [v for v in FilteredElementCollector(doc).OfClass(View).ToElements() if v.ViewType == ViewType.ThreeD]

def getAllDrawingSheets(doc):
    return [v for v in FilteredElementCollector(doc).OfClass(View).ToElements() if v.ViewType == ViewType.DrawingSheet]


# ---------------- WORKSETS --------------------


def getAllWorksets(doc):
    worksetCollector = FilteredWorksetCollector(doc).OfKind(WorksetKind.UserWorkset).ToWorksets()
    return UnwrapElement(worksetCollector)


def getWorksetByName(doc, name):
    try:
        worksetCollector = FilteredWorksetCollector(doc).OfKind(WorksetKind.UserWorkset).ToWorksets()
        worksets = UnwrapElement(worksetCollector)
        wNames = []

        for w in worksetCollector:
            name = str(w.Name)
            wNames.append(name)

        workset = worksets[wNames.index(name)]

        return 	workset
    except:
        return "Did not find this workset."


def getAllFromWorkset(doc, workset):
    uWorkset = UnwrapElement(workset)
    id = uWorkset.Id
    elementWorksetFilter = ElementWorksetFilter(id)
    elements = FilteredElementCollector(doc).WhereElementIsNotElementType().WherePasses(elementWorksetFilter).ToElements()
    return elements



# ---------------- FAMILIES --------------------

def getAllFamilies(doc):
    return FilteredElementCollector(doc).OfClass(Family).ToElements()


# ---------------- SCOPE BOXES --------------------

def getAllScopeBoxes(doc):
    return FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_VolumeOfInterest)