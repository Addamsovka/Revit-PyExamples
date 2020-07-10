"Rooms to floors"

__doc__ = 'Gets all rooms boundaries and create floors with the floor room parameters and boundaries.'
__title__ = 'Rooms to Floors'
__author__ = 'Addamsovka'

import sys
import os

from Autodesk.Revit.UI import TaskDialog
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, BuiltInParameter
from Autodesk.Revit.DB import Element, XYZ, CurveArray
from Autodesk.Revit.DB import Transaction, ElementId, Transform, Curve, CurveArray
from Autodesk.Revit.DB import SpatialElementBoundaryOptions, Options, SpatialElement
from Autodesk.Revit.DB.Architecture import RoomFilter, Room
from Autodesk.Revit.Creation import *
from System.Collections.Generic import List
from System import ArgumentOutOfRangeException

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument


def main():
    floor_dict = {}  # {'name':'id'} Make floor type dictionary
    floor_types = select_all_floor_types()
    for floor_type in floor_types:
        floor_dict[Element.Name.GetValue(floor_type)] = floor_type.Id

    room_boundary_options = SpatialElementBoundaryOptions()  # SpatialElement class

    room_id = 269067
    print(room_id)
    room = doc.GetElement(ElementId(room_id))

    room_level_id = room.Level.Id
    room_id = room.Id
    room_name = room.get_Parameter(BuiltInParameter.ROOM_NAME).AsString()
    print(room_name)
    room_boundary = room.GetBoundarySegments(room_boundary_options)[0]
    if len(room_boundary) > 0:
        room_floor_finish = room.get_Parameter(BuiltInParameter.ROOM_FINISH_FLOOR).AsString()
        if room_floor_finish not in floor_dict:
            t = Transaction(doc, 'duplicate')
            t.Start()
            floor_type = doc.GetElement(floor_dict.get('Undefined'))
            new_floor_type = floor_type.Duplicate(room_floor_finish)
            add_floor_type(floor_dict, new_floor_type)
            t.Commit()
        type_id = floor_dict.get(room_floor_finish)
        new_floor = Floor(type_id, room_boundary, room_level_id, room_id)
        new_floor.make_floor()
        print(room_floor_finish + ' floor placed in ' + room_name + '.')
    else:
        print("Room boundary of " + room_name + " does not found.")


# Help transaction wrapper
def revit_transaction(transaction_name):
    def wrap(f):
        @wraps(f)
        def wrapped_f(*args, **kwargs):
            try:
                t = Transaction(doc, transaction_name)
                t.Start()
            except InvalidOperationException as errmsg:
                print('Transaciton Error: {}'.format(errmsg))
                return_value = f(*args, **kwargs)
            else:
                return_value = f(*args, **kwargs)
                t.Commit()
            return return_value

        return wrapped_f

    return wrap


# Select all floor types from Active project
def select_all_floor_types():
    global doc
    return FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Floors).WhereElementIsElementType()


# Add new floor type into existing dictionary, needs existing dictionary and a new floor type
def add_floor_type(floor_dict, new_floor_type):
    floor_dict[Element.Name.GetValue(new_floor_type)] = new_floor_type.Id
    return floor_dict



class Floor:
    """
    Class floor for creating new floors from type id, boundary and level

    """
    def __init__(self, type_id, boundary, level_id, room_id):
        self.type_id = type_id
        self.boundary = boundary
        self.level_id = level_id

    # TODO solve issue here * curves - when room does not have a boundary
    def make_floor(self):
        global doc
        t = Transaction(doc, 'Floor Creator')
        t.Start()
        floor_curves = CurveArray()
        # todo solve array vs boundary object control
        for boundary_segment in self.boundary:
            floor_curves.Append(boundary_segment.GetCurve())
        if floor_curves[0].GetEndPoint(0).Z != 0:
            print('test')
            floor_curves = transform_boundary_lines(floor_curves)
        floor_type = doc.GetElement(self.type_id)
        level = doc.GetElement(self.level_id)
        normal = XYZ.BasisZ
        doc.Create.NewFloor(floor_curves, floor_type, level, False, normal)
        t.Commit()

def transform_boundary_lines(room_boundary):
    point = room_boundary.GetEndPoint(0)
    myVector = XYZ(0,0,(-point.Z))
    tf = Transform.CreateTranslation(myVector)
    room_boundary = room_boundary.CreateTransformed(tf)
    return room_boundary

# Code:
main()



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
