def add_to_buckets(pair, count, buckets):
    if pair in buckets.keys():
        buckets[pair] += count
    else:
        buckets[pair] = count

def one_step(buckets, insertion):
    new_buckets = {}
    for pair in buckets.keys():
        #print("Processing buckets: %s. Pair: %s" %(new_buckets, pair))
        new_item = insertion[pair]
        left = pair[0] + new_item
        right = new_item + pair[1]
        #print("\tLeft: %s, Right: %s" %(left, right))

        add_to_buckets(left, buckets[pair], new_buckets)
        add_to_buckets(right, buckets[pair], new_buckets)
        #print("Bucket result: %s" %(new_buckets))

    return new_buckets
