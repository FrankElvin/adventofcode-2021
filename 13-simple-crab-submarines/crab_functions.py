
def get_fuel_consumption(crabs, target_position):
    consumption = 0
    for crab in crabs:
        #print("Fuel cost from %d to %d: %d" %(crab, target_position, abs(target_position-crab)))
        consumption += abs(crab - target_position)
    return consumption
