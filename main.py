def calculate_state_of_health(present_capacity, rated_capacity):
    return (present_capacity / rated_capacity) * 100

def classify_batteries(capacities):
    health_counts = {
        "healthy": 0,
        "exchange": 0,
        "failed": 0
    }
    
    rated_capacity = 120  # Assume all batteries have a rated capacity of 120 Ah

    for present_capacity in capacities:
        soh = calculate_state_of_health(present_capacity, rated_capacity)

        if soh > 80:
            health_counts["healthy"] += 1
        elif 62 < soh <= 80:
            health_counts["exchange"] += 1
        else:
            health_counts["failed"] += 1

    return health_counts

def test_battery_classification():
    print("Classifying batteries by state of health...\n")
    present_capacities = [113, 116, 80, 95, 92, 70]
    counts = classify_batteries(present_capacities)
    assert counts["healthy"] == 2
    assert counts["exchange"] == 3
    assert counts["failed"] == 1
    print("Battery classification done :)")

if __name__ == '__main__':
    test_battery_classification()
