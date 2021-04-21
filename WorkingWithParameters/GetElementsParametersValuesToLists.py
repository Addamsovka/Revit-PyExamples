# Made by Addamsovka
# Version 1.0.0
# Tested in Revit 2020.2, Dynamo Revit 2.3.0.7661
# Takes list of room elements and list of parameter names as strings

import clr
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.AddReference("RevitAPI")

import Autodesk
from Autodesk.Revit.DB import *

rooms_r = IN[0] if isinstance(IN[0], list) else ([IN[0]])
rooms = UnwrapElement(rooms_r)
params = IN[1] if isinstance(IN[1], list) else ([IN[1]])

all_rooms = []
header = []
header.append("Id")


for p in params: # Create Header from first room
    param_1 = rooms[0].GetParameters(p)
    for par in param_1:
        param_name = par.Definition.Name # Each parameter has its definition
        header.append(param_name)

all_rooms.append(header)

try:
	for r in rooms: # Create data from room parameters
	    all_par = []
	    for p in params:
	        pars_by_name = r.GetParameters(p)
	        for each in pars_by_name:
	           all_par.append(each)
	    param_bundle = []
	    param_bundle.append(r.Id)
	    for par in all_par:
	        if par.StorageType == StorageType.String:
	            a = par.AsString()
	            param_bundle.append(a)
	        else:
	            a = par.AsValueString()
	            param_bundle.append(a)
	    all_rooms.append(param_bundle)
except Exception as inst:
    all_rooms.append(inst)
    
OUT = all_rooms
