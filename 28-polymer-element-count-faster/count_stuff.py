
from copy import deepcopy

def get_counts(polymer, symbols):
    min_res = [None, None]
    max_res = [0, None]
    for char in symbols:
        count = polymer.count(char)

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
    print("Recursion level: %s" %len(route))
    out_routes = []

    new_buckets = deepcopy(buckets)
    new_buckets[item] -= 1
    for key in list(new_buckets.keys()):
        if new_buckets[key] == 0:
            del new_buckets[key]
    #print("%sRoute: %s. Buckets: %s" %(recursion_level, route, new_buckets))

    if len(new_buckets) == 0:
        #print("%sWe found a way!!" %(recursion_level))
        return [route], True

    for key in new_buckets.keys():
        if key.startswith(search_letter) and new_buckets[key]>0:
            #print("%sGoing to next item: %s" %(recursion_level, key))
            result = get_options(key, route, new_buckets)
            if result[1] == False:
                out_routes.extend(result[0])
            if result[1] == True:
                #print("%sGot right result. Returining it higher" %(recursion_level))
                return result

    #if not out_routes:
        #print("%sWow! Founded a dead end" %recursion_level)

    return (out_routes, False)


def repair_polymer(buckets):
    start = list(buckets.keys())[0]
    route = start[0]
    print("=== Starting polymer building from %s" %start)
    result = get_options(start, route, buckets)
    print("Our result: ", result)
    return result[0][0], result[1]
