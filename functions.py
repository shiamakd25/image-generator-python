def list_intersection(lists, min_length):
    filtered_lists = [lst for lst in lists if len(lst) >= min_length]
    if not filtered_lists:
        return set()
    common_set = set(filtered_lists[0])
    for lst in filtered_lists[1:]:
        common_set.intersection_update(lst)   
    return common_set

def find_min_attr(list, attribute):
    attr_list = []
    for elem in list:
        attr = getattr(elem, attribute)
        attr_list.append(attr)
    min_attr = min(attr_list)
    return min_attr