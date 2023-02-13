def forecast(*args):
    # Initialize a dictionary to store locations based on weather condition
    weather = {'Sunny': [], 'Cloudy': [], 'Rainy': []}

    # Loop through all the arguments and categorize each location based on its weather condition
    for arg in args:
        weather[arg[1]].append(arg[0])

    # Initialize an empty list to store the result
    result = []

    # Loop through the weather conditions in the desired order
    for key in ['Sunny', 'Cloudy', 'Rainy']:
        # Sort the locations for each weather condition alphabetically
        weather[key].sort()
        # Loop through the locations for each weather condition
        for location in weather[key]:
            # Append the location and weather condition to the result list
            result.append(location + ' - ' + key)

    # Join the result list into a single string and return it
    return '\n'.join(result)



print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))



