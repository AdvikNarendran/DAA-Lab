def maximumPeople(town_populations, town_locations, cloud_locations, cloud_ranges):
    max_people = 0

    # Iterate through each cloud
    for i in range(len(cloud_locations)):
        current_cloud_location = cloud_locations[i]
        current_cloud_range = cloud_ranges[i]

        # Calculate the number of people in sunny towns if this cloud is removed
        sunny_people = 0
        for j in range(len(town_populations)):
            town_location = town_locations[j]
            population = town_populations[j]

            # Check if the town is within the range of the current cloud
            if town_location < current_cloud_location or town_location >= current_cloud_location + current_cloud_range:
                sunny_people += population

        # Update max_people if necessary
        max_people = max(max_people, sunny_people)

    return max_people

# Sample Input
num_towns = 2
town_populations = [10,100]
town_locations = [5,100]
num_clouds = 1
cloud_locations = [4]
cloud_ranges = [1]

# Output
print(maximumPeople(town_populations, town_locations, cloud_locations, cloud_ranges))
