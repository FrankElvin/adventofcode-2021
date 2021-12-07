
def get_fuel_consumption(crabs, target_position):
    consumption = 0
    for crab in crabs:
        for i in range(1, abs(crab-target_position) +1):
            consumption += i
        #print("Fuel cost from %d to %d: %d" %(crab, target_position, consumption))

    return consumption

def get_fuel_consumption_better(crabs, target_position):
    consumption = 0
    for crab in crabs:
        curr_consumption = (1 + abs(crab-target_position))/2 * abs(crab-target_position)
        consumption += curr_consumption
    return consumption
