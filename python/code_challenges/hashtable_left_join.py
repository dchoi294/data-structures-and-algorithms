from data_structures.hashtable import Hashtable


def left_join(map1, map2):
    result = []
    for key in map1:
        row = [key, map1[key]]
        if key in map2:
            row.append(map2[key])
        else:
            row.append(None)
        result.append(row)
    return result

