"Rooms to floors"

__doc__ = 'Gets all rooms boundaries and create floors with the floor room parameters and boundaries.'
__title__ = 'Rooms to Floors'
__author__ = 'Addamsovka'

import sys
import os

from Autodesk.Revit.UI import TaskDialog
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, BuiltInParameter
from Autodesk.Revit.DB import Element, XYZ, CurveArray
from Autodesk.Revit.DB import Transaction
from Autodesk.Revit.DB import SpatialElementBoundaryOptions, Options
from Autodesk.Revit.DB.Architecture import RoomFilter, Room
from Autodesk.Revit.Creation import *
from System.Collections.Generic import List

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument


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


# Select elements
def get_selected_elements():
    selection = uidoc.Selection
    selection_ids = selection.GetElementIds()
    selection_size = selection_ids.Count
    if not selection_ids:
        TaskDialog.Show('MakeFloors', 'No Elements Selected.')
        __window__.Close()
        sys.exit(0)
    elements = []
    for element_id in selection_ids:
        elements.append(doc.GetElement(element_id))
    return elements


# Select all rooms from Active project
def select_all_rooms():
    return FilteredElementCollector(doc).WherePasses(RoomFilter()).ToElements()


# Edit all rooms in project - automaticly fills Floor Finish parameter
def edit_rooms_floor_finish():
    rooms = select_all_rooms()
    for room in rooms:  # Control if the Floor finish is set
        room_floor_finish = room.get_Parameter(BuiltInParameter.ROOM_FINISH_FLOOR).AsString()
        if room_floor_finish == None:
            transaction = Transaction(doc, 'Add Undefined to room param transaction')
            transaction.Start()
            p = room.LookupParameter('Floor Finish')  # Sets parameter of the None Floor Finish to "Undefined"
            p.Set("Undefined")
            transaction.Commit()


# Select all floor types from Active project
def select_all_floor_types():
    return FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Floors).WhereElementIsElementType()


# Add new floor type into existing dictionary, needs existing dictionary and a new floor type
def add_floor_type(floor_dict, new_floor_type):
    floor_dict[Element.Name.GetValue(new_floor_type)] = new_floor_type.Id
    return floor_dict


# Class floor for creating new floors from type id, boundary and level
class Floor:
    def __init__(self, type_id, boundary, level_id):
        self.type_id = type_id
        self.boundary = boundary
        self.level_id = level_id

    def make_floor(self):
        t = Transaction(doc, 'Floor Creator')
        t.Start()
        floor_curves = CurveArray()
        for boundary_segment in self.boundary:
            floor_curves.Append(boundary_segment.Curve)
        floor_type = doc.GetElement(self.type_id)
        level = doc.GetElement(self.level_id)
        normal = XYZ.BasisZ
        doc.Create.NewFloor(floor_curves, floor_type, level, False, normal)
        t.Commit()


# Code:
edit_rooms_floor_finish() # Just in case, there are empty fields
rooms = select_all_rooms()

floor_dict = {}  # {'name':'id'} Make floor type dictionary
floor_types = select_all_floor_types()
for floor_type in floor_types:
    floor_dict[Element.Name.GetValue(floor_type)] = floor_type.Id
    if Element.Name.GetValue(floor_type) == 'Undefined':
        uni_floor_type = floor_type
        print('test01')
        print(uni_floor_type)

new_floors = []  # Make list with Floor objects

for room in select_all_rooms():  # for all rooms - get their boundary and name of the floor finish
    room_level_id = room.Level.Id
    print(room_level_id)
    room_boundary = room.GetBoundarySegments(room_boundary_options)[0]
    print(room_boundary)
    room_floor_finish = room.get_Parameter(BuiltInParameter.ROOM_FINISH_FLOOR).AsString()
    print(room_floor_finish)
    # If name of the floor is not in dictionary, duplicate floor and add to dictionary
    if room_floor_finish not in floor_dict:
        t = Transaction(doc, 'Floor type duplicate')
        t.Start()
        print('test03')
        print(room_floor_finish)
        # upravit duplikaci podlahz....

        new_floor_type = uni_floor_type.Duplicate("Final Floor - " + room_floor_finish)
        print('test04')
        print(room_floor_finish)
        add_floor_type(floor_dict, new_floor_type)
        t.Commit()
    type_id = floor_dict[room_floor_finish]
    new_floor = Floor(type_id, room_boundary, room_level_id)
    new_floors.append(new_floor)
    print(new_floor)

# Creating floors
# for new_floor in new_floors:
# view = make_floor(new_floor)


# cl = List[Curve]()
# one = uidoc.Selection.SetElelemetIds(List[ElementId](pythonElelemtIdList))
