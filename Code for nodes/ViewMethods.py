# Created by Addamsovka 2022

# Working with views
# To be pasted in a Dynamo Python Script nodes.

from msilib.schema import Dialog
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument

# View Duplicate
for view in views:
    # Views with specific names
    if view.Name == "desired name":
        # do something cool
        bb = view.CropBox
        boundingBox = view.BoundingBox
        view.CropBoxVisible = False
        view.CropBoxActive = False
        id = view.Id
        parameters = view.ParameterMap

# Create dependent copy - use in transaction!
def CreateDependentCopy(view):
    v = UnwrapElement(view)
    if v.CanViewBeDuplicated(ViewDuplicateOption.AsDependent):
        newViewId = v.Duplicate(ViewDuplicateOption.AsDependent) #Generate new dependent view (other options WithDetailing or Duplicate)
        dependentView = v.Document.GetElement(newViewId) # get view with the new id
        if dependentView != None:
            if dependentView.GetPrimaryViewId() == v.Id:
                TaskDialog.Show("Dependent View", "Dependent VIew has been created successfully")
    return dependentView


# Give me list of views that cointain this element(by Id)
def ViewsContatiningElement(doc, elementId, views):
    listOfViews = []
    for view in views:
        v = UnwrapElement(view)
        ids = []
        items = FilteredElementCollector(doc, v.Id).ToElementIds()
        for i in items:
            ids.append(int(i.ToString()))
        if elementId in ids:
            listOfViews.append(view)
    return set(listOfViews)




# Working with sheets

# Show sheet info
def getSheetInfo(viewSheet):
    message = ""

    # Whole Title
    title = viewSheet.Title
    message = message + "\nTitle: " + str(title.ToString())

    # Get number of the sheet
    sheetNumber = viewSheet.SheetNumber
    message = message + "\nSheet Number: " + str(sheetNumber)

    # Get all placed views
    views = viewSheet.GetAllPlacedViews()
    message = message + "\nNumber of views in the sheet : " + str(views.Count)

    TaskDialog.Show("Revit", message)

    return views


# Schedules needs to be sho differently


#------------------------------------

# Get all titleblocks in project
def getAllTitleBLocks(doc):
    ttbs = FilteredElementCollector(doc).OfClass(FamilySymbol).OfCategory(BuiltInCategory.OST_TitleBlocks).ToElements()
    return ttbs

# Create new view sheet - use in transaction!
def CreateSheetView(doc, view, ttb):
    if ttb != None:
        try:
            # Create a sheet view
            viewSheet = ViewSheet.Create(doc, ElementId(ttb.Id))
            if viewSheet == None:
                raise Exception("Failed to create new ViewSheet.")
            # Get location of that viewSheet
            x = (viewSheet.Outline.Max.U - viewSheet.Outline.Min.U)/2
            y = (viewSheet.Outline.Max.V - viewSheet.Outline.Min.V)/2
            center = UV(x, y)

            # Add a viewport
            Viewport.Create(doc, viewSheet.Id, ElementId(view.Id), XYZ(center.U, center.V, 0))
        except:
            TaskDialog.Show("Revit", "Sheet not created!")
    return "Sheet Created" + viewSheet.Name

# TODO test method 
def CreateSheet(doc, view):
    if ttb != None:
        TaskDialog.Show("Revit", "Create to")

        # Create a sheet view
        viewSheet = ViewSheet.Create(doc, ElementId(ttb.Id))
        TaskDialog.Show("Revit", viewSheet.ToString())
        if viewSheet == None:
            raise Exception("Failed to create new ViewSheet.")
        # Get location of that viewSheet
        
        x = (viewSheet.Outline.Max.U - viewSheet.Outline.Min.U)/2
        y = (viewSheet.Outline.Max.V - viewSheet.Outline.Min.V)/2
        center = UV(x, y)
        TaskDialog.Show("Revit", center.ToString())
        return viewSheet
