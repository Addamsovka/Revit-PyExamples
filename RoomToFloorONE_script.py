"Rooms to floors"

__doc__ = 'Gets all rooms boundaries and create floors with the floor room parameters and boundaries.'
__title__ = 'Rooms to Floors'
__author__ = 'Addamsovka'

import sys
import os

from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, BuiltInParameter
from Autodesk.Revit.DB import Element, XYZ, CurveArray
from Autodesk.Revit.DB import Transaction, ElementId, Transform, Curve, CurveArray
from Autodesk.Revit.DB import SpatialElementBoundaryOptions, Options, SpatialElement
from Autodesk.Revit.UI import TaskDialog

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument

def main():
    # {'name':'id'} Make floor type dictionary
    floor_dict = {}
    floor_types = select_all_floor_types()
    for floor_type in floor_types:
        floor_dict[Element.Name.GetValue(floor_type)] = floor_type.Id
    # Sets room
    room_id = 269067
    room = doc.GetElement(ElementId(room_id))
    room_floor_finish = room.get_Parameter(BuiltInParameter.ROOM_FINISH_FLOOR).AsString()
    # Checking if the floor type exists
    if room_floor_finish not in floor_dict:
        t = Transaction(doc, 'duplicate')
        t.Start()
        floor_type = doc.GetElement(floor_dict.get('Undefined'))
        new_floor_type = floor_type.Duplicate(room_floor_finish)
        add_floor_type(floor_dict, new_floor_type)
        t.Commit()
    # SpatialElement class
    room_boundary_options = SpatialElementBoundaryOptions()
    # Gets room boundary, name and level and force to make floor if boundary exists
    room_boundary = room.GetBoundarySegments(room_boundary_options)[0]
    room_name = room.get_Parameter(BuiltInParameter.ROOM_NAME).AsString()
    room_level_id = room.Level.Id
    if len(room_boundary) > 0:
        type_id = floor_dict.get(room_floor_finish)
        new_floor = Floor(type_id, room_boundary, room_level_id)
        new_floor.make_floor()
        print(room_floor_finish + ' floor placed in ' + room_name + '.')
    else:
        print("Room boundary of " + room_name + " does not found.")


class Floor:
    """
    Represents floor object, made from room type_id, boundary and level_id.

    Parameters
        ----------
        type_id : floor type Id
            Id of the floor type element
        boundary : BoundarySegments
            Boundary of a room to make boundary of a floor
        level_id : room level.Id
            Sets level of the floor
    """
    def __init__(self, type_id, boundary, level_id):
        self.type_id = type_id
        self.boundary = boundary
        self.level_id = level_id

    def boundary_to_array(self, boundary):
        """
        Create CurveArray from room boundary given.
        Check if boundary on Z=0, if not, puts in boundary there.
        :return: CurveArray -> can be used for make_floor
        """
        floor_curves = CurveArray()
        if boundary[0].GetCurve().Z != 0:
            for boundy in self.boundary:
                curve = boundy.GetCurve()
                a = curve.GetEndPoint(0)
                myVector = XYZ(0, 0, (-a.Z))
                tf = Transform.CreateTranslation(myVector)
                curve = curve.CreateTransformed(tf)
                floor_curves.append(curve)
        else:
            for boundary_segment in self.boundary:
                floor_curves.Append(boundary_segment.GetCurve())
        return floor_curves

    def make_floor(self):
        """
        Creates floor
        """
        global doc
        t = Transaction(doc, 'Floor Creator')
        t.Start()
        floor_curves = self.boundary_to_array(self.boundary)
        floor_type = doc.GetElement(self.type_id)
        level = doc.GetElement(self.level_id)
        normal = XYZ.BasisZ
        doc.Create.NewFloor(floor_curves, floor_type, level, False, normal)
        t.Commit()

# Select all floor types from Active project
def select_all_floor_types():
    global doc
    return FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Floors).WhereElementIsElementType()

# Add new floor type into existing dictionary, needs existing dictionary and a new floor type
def add_floor_type(floor_dict, new_floor_type):
    floor_dict[Element.Name.GetValue(new_floor_type)] = new_floor_type.Id
    return floor_dict

# Select elements
def get_selected_elements():
    global uidoc
    selection = uidoc # user selection, TODO check if works
    selection_ids = selection.GetElementIds()
    selection_size = selection_ids.Count
    if not selection_ids:
        TaskDialog.Show('MakeFloors', 'No Elements Selected.')
        __window__.Close()
        sys.exit(0)
    else:
        return selection_ids

main()

# testing floors / these worked until last one
# 134997
# Undefined floor placed in Chodba.
# 135009
# Undefined floor placed in Koupelna.
# 135012
# Undefined floor placed in WC.
# 135015
# Undefined floor placed in Šatna.
# 135018
# Undefined floor placed in Pokoj.
# 135021
# Undefined floor placed in Pokoj.
# 135025
# Undefined floor placed in Ložnice.
# 135028
# Undefined floor placed in Obývací pokoj + KK.
# 137596
# Undefined floor placed in Chodba.
# 137604
# Undefined floor placed in Koupelna.
# 137607
# Undefined floor placed in Ložnice.
# 137610
# Undefined floor placed in Obývací pokoj.
# 137613
# Undefined floor placed in Chodba.
# 137620
# Undefined floor placed in Ložnice.
# 137623
# Undefined floor placed in Koupelna.
# 137626
# Undefined floor placed in Obývací pokoj + KK.
# 137629
# Undefined floor placed in Chodba.
# 137636
# Undefined floor placed in Pokoj.
# 137639
# Undefined floor placed in Pokoj.
# 137642
# Undefined floor placed in Pokoj.
# 137645
# Undefined floor placed in WC.
# 137648
# Undefined floor placed in Koupelna.
# 137651
# Undefined floor placed in Obývací pokoj + KK.
# 137654
# Undefined floor placed in Chodba.
# 137661
# Undefined floor placed in Koupelna.
# 137664
# Undefined floor placed in Obývací pokoj + KK.
# 260114
# Undefined floor placed in Šachta.
# 260175
# Undefined floor placed in Šachta.
# 260178
# Undefined floor placed in Šachta.
# 260181
# Undefined floor placed in Šachta.
# 260184
# Undefined floor placed in Šachta.
# 260187
# Undefined floor placed in Šachta.
# 260190
# Undefined floor placed in Šachta.
# 260193
# Undefined floor placed in Šachta.
# 269067
