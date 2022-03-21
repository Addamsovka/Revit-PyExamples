# Returns views that have same id inside
def viewWithThisElement(doc, views, elementIDnumber):
    results = []
    for view in views:
        v = UnwrapElement(view)
        ids = []
        f = FilteredElementCollector(doc, v.Id).ToElementIds()
        for ele in f:
            ids.append(int(ele.ToString()))
        if elementIDnumber in ids:
            results.append(view)
    return results