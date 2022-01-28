
from copy import deepcopy

def get_counts(buckets, symbols):
    min_res = [None, None]
    max_res = [0, None]
    for char in symbols:
        count = 0
        for pair in buckets.keys():
            if char in pair:
                count += buckets[pair]

        if min_res[0]:
            if count < min_res[0]:
                min_res = [count, char]
        else:
            min_res = [count, char]
        if count > max_res[0]:
            max_res = [count, char]
    return min_res, max_res

def get_options(item, route, buckets):
    search_letter = item[1]
    route += search_letter
    recursion_level = ' '*len(route)
    out_routes = []

    new_buckets = deepcopy(buckets)
    new_buckets[item] -= 1
    for key in list(new_buckets.keys()):
        if new_buckets[key] == 0:
            del new_buckets[key]
    print("%sRoute: %s. Buckets: %s" %(recursion_level, route, new_buckets))

    if len(new_buckets) == 0:
        print("%sWe found a way!!" %(recursion_level))
        return [route]

    for key in new_buckets.keys():
        if key.startswith(search_letter) and new_buckets[key]>0:
            print("%sGoing to next item: %s" %(recursion_level, key))
            out_routes.extend(get_options(key, route, new_buckets))

    if not out_routes:
        print("Wow! Founded a dead end")

    return out_routes


def repair_polymer(buckets):
    start = list(buckets.keys())[0]
    route = start[0]
    print("=== Starting polymer building from %s" %start)
    result = get_options(start, route, buckets)
    print("result:", result)
