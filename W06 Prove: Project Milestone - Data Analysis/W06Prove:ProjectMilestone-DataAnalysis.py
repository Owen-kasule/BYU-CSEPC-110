# W06 Prove: Project Milestone - Data Analysis || Author = Muhereza Owen Kasule || 2024-02-21
# This program analyzes a dataset containing information about life expectancies over the years throughout the countries of the world.

# Creativity: In addition to the required functionalities, this program allows the user to input a year,
# then shows the average life expectancy for that year along with the countries with the minimum and maximum life expectancies.
# It also allows the user to input a country and displays the minimum, maximum, and average life expectancies for that country.

# Load dataset
def load_dataset(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Error: Dataset file not found.")
        exit()

    # Skip the header
    data = [line.strip().split(',') for line in lines[1:]]

    # Convert year and life expectancy to int and float
    for i in range(len(data)):
        data[i][2] = int(data[i][2])  # year
        data[i][3] = float(data[i][3])  # life expectancy

    return data

def find_min_max_life_expectancy(data):
    min_life_expectancy = float('inf')
    max_life_expectancy = float('-inf')
    min_country = ''
    max_country = ''

    for entity, code, year, life_expectancy in data:
        if life_expectancy < min_life_expectancy:
            min_life_expectancy = life_expectancy
            min_country = entity

        if life_expectancy > max_life_expectancy:
            max_life_expectancy = life_expectancy
            max_country = entity

    return min_life_expectancy, min_country, max_life_expectancy, max_country

def find_average_life_expectancy(data, year):
    total_life_expectancy = 0
    count = 0
    countries = []

    for entity, code, yr, life_expectancy in data:
        if yr == year:
            total_life_expectancy += life_expectancy
            count += 1
            countries.append(entity)

    if count == 0:
        return None, None, None

    average_life_expectancy = total_life_expectancy / count
    min_life_expectancy_country = min(countries, key=lambda x: data[countries.index(x)][3])
    max_life_expectancy_country = max(countries, key=lambda x: data[countries.index(x)][3])

    return average_life_expectancy, min_life_expectancy_country, max_life_expectancy_country

def find_country_life_expectancy(data, country):
    country_data = [x for x in data if x[0] == country]
    
    if not country_data:
        return None, None, None

    min_life_expectancy_country = min(country_data, key=lambda x: x[3])[0]
    max_life_expectancy_country = max(country_data, key=lambda x: x[3])[0]
    avg_life_expectancy_country = sum([x[3] for x in country_data]) / len(country_data)

    return min_life_expectancy_country, max_life_expectancy_country, avg_life_expectancy_country

# Load dataset
dataset_filename = "life-expectancy.csv"
data = load_dataset(dataset_filename)

# Find lowest and highest life expectancy
min_life_expectancy, min_country, max_life_expectancy, max_country = find_min_max_life_expectancy(data)

print("The overall min life expectancy is:", min_life_expectancy, "from", min_country)
print("The overall max life expectancy is:", max_life_expectancy, "from", max_country)

# Allow user to input a year
year = input("Enter the year of interest: ")
year = int(year)

# Find average life expectancy for the input year
average_life_expectancy, min_country_year, max_country_year = find_average_life_expectancy(data, year)

if average_life_expectancy is None:
    print(f"No data available for the year {year}")
else:
    print(f"For the year {year}:")
    print("The average life expectancy across all countries was:", average_life_expectancy)
    print("The country with the min life expectancy was:", min_country_year)
    print("The country with the max life expectancy was:", max_country_year)

# Allow user to input a country
country = input("Enter the country to analyze: ")

min_life_country, max_life_country, avg_life_country = find_country_life_expectancy(data, country)

if min_life_country is None:
    print(f"No data available for {country}")
else:
    print(f"Statistics for {country}:")
    print("Minimum Life Expectancy:", min_life_country)
    print("Maximum Life Expectancy:", max_life_country)
    print("Average Life Expectancy:", avg_life_country)
