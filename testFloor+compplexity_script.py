"Rooms to floors"

__doc__ = 'Gets all rooms boundaries and create floors with the floor room parameters and boundaries.'
__title__ = 'Test one floor by id'
__author__ = 'Addamsovka'

import sys
import os

from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, BuiltInParameter
from Autodesk.Revit.DB import Element, XYZ, CurveArray
from Autodesk.Revit.DB import Transaction, Transform
from Autodesk.Revit.DB import SpatialElementBoundaryOptions, Options, SpatialElement, ElementId

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument


room_id = 269067

def transform_boundary_lines(room_id):
    room_boundary_options = SpatialElementBoundaryOptions()
    room = doc.GetElement(ElementId(room_id))
    print(room)
    room_name = room.get_Parameter(BuiltInParameter.ROOM_NAME).AsString()
    print(room_name)
    room_level_id = room.Level.Id
    print(room_level_id)
    room_boundary = room.GetBoundarySegments(room_boundary_options)[0]
    boundary2 = []
    for boundy in room_boundary:
        curve = boundy.GetCurve()
        a = curve.GetEndPoint(0)
        b = curve.GetEndPoint(1)
        myVector = XYZ(0,0,(-a.Z))
        tf = Transform.CreateTranslation(myVector)
        curve = curve.CreateTransformed(tf)
        print(curve.GetEndPoint(1))
        boundary2.append(curve)
    print(boundary2)

transform_boundary_lines(room_id)