def list_intersection(lists, min_length):
    filtered_lists = [lst for lst in lists if len(lst) >= min_length]
    if not filtered_lists:
        return set()
    common_set = set(filtered_lists[0])
    for lst in filtered_lists[1:]:
        common_set.intersection_update(lst)   
    return common_set