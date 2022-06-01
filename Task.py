from typing import List

def find_maximum_distance(number_of_cities: int, cities_with_train_station: List[int]) -> int:
    maximum = cities_with_train_station[0]
    for i in range(1, len(cities_with_train_station)):
        difference = cities_with_train_station[i] - cities_with_train_station[i-1]
        length = difference/2
        maximum = max(maximum, length)
    maximum = max(maximum, number_of_cities - cities_with_train_station[len(cities_with_train_station) - 1] - 1)
    return maximum


# These are some of test cases. When evaluating the task, more will be added:
assert find_maximum_distance(number_of_cities=3, cities_with_train_station=[1]) == 1
assert find_maximum_distance(number_of_cities=4, cities_with_train_station=[3]) == 3
assert (find_maximum_distance(number_of_cities=5, cities_with_train_station=[0, 4]) == 2)
print("ALL TESTS PASSED")