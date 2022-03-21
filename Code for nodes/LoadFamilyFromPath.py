# Collected from c.poupin at https://forum.dynamobim.com/t/reload-family-and-overwrite-parameter-values/13667/10

import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
doc = DocumentManager.Instance.CurrentDBDocument

# Ensure loaded families can overwrite existing families.
class FamilyOption(IFamilyLoadOptions) :
    def OnFamilyFound(self, familyInUse, overwriteParameterValues):
        overwriteParameterValues.Value = False
        return True

    def OnSharedFamilyFound(self, sharedFamily, familyInUse, source, overwriteParameterValues):
        overwriteParameterValues.Value = False
        return True


toList = lambda x : x if hasattr(x, '__iter__') else [x]
pathsFamily = toList(UnwrapElement(IN[0]))

TransactionManager.Instance.EnsureInTransaction(doc)

opts = FamilyOption()
for path in pathsFamily :
    doc.LoadFamily(path, opts)

TransactionManager.Instance.TransactionTaskDone()

OUT = pathsFamily