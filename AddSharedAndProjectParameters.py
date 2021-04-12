# Version Dynamo Core 2.3.0.5885
# Version Dynamo Revit 2.3.0.7661
# Create Shared Parameters from string-lists (Excel) and bind them to categories as Project Parameters
# Made by Addamsovka 2021
# Version 1.0

import clr

import sys

sys.path.append('C:\Program Files\IronPython 2.7\Lib')

import System
from System import Array
from System.Collections.Generic import *

clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference("RevitNodes")
import Revit

clr.ImportExtensions(Revit.Elements)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference("RevitAPI")
clr.AddReference("RevitAPIUI")

import Autodesk
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
from Autodesk.Revit.ApplicationServices import *

# Current doc/app/ui
doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application
uidoc = uiapp.ActiveUIDocument

# Inputs from user
"""
Format of excel file needs to be in exact structure or next lines needs to be adjusted.
[
  String, # parName (exapmle: Name-DE)
  String, # parGroupName (example: My New Group)
  String, # parType (exapmle: Text)
  String, # parVisible (true)
  String, # parCaterories separeted by "," (exapmle: Generic Models, Casework, Furniture)
  String, # parGroup (example: Text)
  String, # instance (for type parameter set: false; for instance parameter set: true)
  String, # parDescription (description of parameter)
  ]
"""
params = IN[0]
out = []

for param in params:
    parName = param[0]  # Parameter Name
    parGroupName = param[1]  # To which group add the SharedParameter
    parType = param[2]  # ParameterType needs to be from existing list in Revit
    parVisible = param[3]  # Will be converted to bool/ TODO not needed in this version
    parCaterories = param[4]  # Main Categories from Revit
    parGroup = param[5]  # Gets String / Not needed in this version
    instance = param[6]  # Is instance? If not then Type
    parDescription = param[7]  # Description od parameter
    out.append("Adding new parameter..." + parName)
    
    try:
        # Get ParameterType by a name
        parTypeOfParameter = getattr(ParameterType, parType)
        # Open the Shared Parameter FIle
        sharedParameterFile = Application.OpenSharedParameterFile(app)
        groups = sharedParameterFile.Groups

        if not groups.Item[parGroupName]:
            groups.Create(parGroupName)  # Creates group if those not exist

        # Get all Definitions of parameters in group
        externalDefinitions = groups.Item[parGroupName].Definitions

        if not externalDefinitions.Item[parName]:  # Create new Definition of shared parameter
            externalDefinitionCreationOptions = ExternalDefinitionCreationOptions(parName, parTypeOfParameter)
            externalDefinitionCreationOptions.Description = parDescription
            externalDefinitionCreationOptions.UserModifiable = True
            externalDefinitions.Create(externalDefinitionCreationOptions)
            # Create new Shared parameter
            TransactionManager.Instance.EnsureInTransaction(doc)
            SharedParameterElement.Create(doc, externalDefinitions.Item[parName])
            TransactionManager.Instance.TransactionTaskDone()

        out.append("Added to shared parameters...")

        # Create CategorySet
        splitList = parCaterories.split(",")
        categorySet = CategorySet()
        for parCat in splitList:
            category = doc.Settings.Categories.Item[parCat]
            categorySet.Insert(category)
        
        out.append("Set categories")

        # Sets Type or Instance
        binding = None
        if instance.lower() == "true":
            binding = InstanceBinding(categorySet)
        else:
            binding = TypeBinding(categorySet)
        
        out.append("Set type/instance")
        
        bipGroup = getattr(BuiltInParameterGroup, "INVALID") # TODO define Built Parameter Group by user
        docBinding = doc.ParameterBindings
        
        TransactionManager.Instance.EnsureInTransaction(doc)
        docBinding.Insert(externalDefinitions.Item[parName], binding, bipGroup)
        TransactionManager.Instance.TransactionTaskDone()
        
        out.append("Added -" + parName + " to group " + parGroupName + " with description: " + parDescription + " as " + parType + ".")

    except AttributeError:
        out.append("Attribute was not added" + parType + ". Please check data if correct.")

out.append("Finished")

OUT = out
