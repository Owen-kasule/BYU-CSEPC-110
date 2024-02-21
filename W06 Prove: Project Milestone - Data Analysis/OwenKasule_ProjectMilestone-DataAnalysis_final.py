# W06 Prove: Project - Data Analysis Final || Muhereza Owen Kasule|| 21/02/2024
# This Python script analyzes life expectancy data from a CSV file.
# It provides overall minimum and maximum life expectancy, and allows the user to analyze data for a specific year.
# The user can input a year of interest and the program will output the average, minimum, and maximum life expectancy for that year.
# The user can input a country of interest and the program will output the average, minimum, and maximum life expectancy for that Country.


import csv

def read_file(filename):
  """
  Reads a CSV file and returns a list of dictionaries, where each dictionary represents a data point.
  """
  with open(filename, "r") as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]
  return data

def find_min_max(data, key):
  """
  Finds the minimum and maximum values for a given key in the data list.
  Returns a tuple containing the minimum value, maximum value, and corresponding data points.
  """
  min_data = min(data, key=lambda x: float(x[key]))
  max_data = max(data, key=lambda x: float(x[key]))
  return min_data, max_data

def analyze_year(data, year):
  """
  Analyzes data for a specific year and returns relevant statistics.
  Returns a tuple containing the average life expectancy, minimum life expectancy data, and maximum life expectancy data.
  """
  filtered_data = [d for d in data if d["Year"] == year]
  if not filtered_data:
    return None, None, None
  average_life_expectancy = sum(float(d["Life expectancy (years)"]) for d in filtered_data) / len(filtered_data)
  min_data, max_data = find_min_max(filtered_data, "Life expectancy (years)")
  return average_life_expectancy, min_data, max_data

def analyze_country(data, country):
    """
    Analyzes data for a specific country and returns relevant statistics.
    Returns a tuple containing the average life expectancy, minimum life expectancy data, and maximum life expectancy data.
    """
    filtered_data = [d for d in data if d["Entity"] == country]
    if not filtered_data:
        return None, None, None
    average_life_expectancy = sum(float(d["Life expectancy (years)"]) for d in filtered_data) / len(filtered_data)
    min_data, max_data = find_min_max(filtered_data, "Life expectancy (years)")
    return average_life_expectancy, min_data, max_data

def find_anomalies(data):
    """
    Finds years where the life expectancy dropped significantly compared to the previous year.
    Returns a list of tuples, where each tuple contains the year and the amount of drop.
    """
    anomalies = []
    for i in range(1, len(data)):
        prev_year = data[i - 1]
        curr_year = data[i]
        if prev_year["Entity"] == curr_year["Entity"]:
            drop = float(prev_year["Life expectancy (years)"]) - float(curr_year["Life expectancy (years)"])
            if drop > 5:  # change this value to adjust the threshold for what is considered a significant drop
                anomalies.append((curr_year["Year"], drop))
    return anomalies

def main():
  print("This program analyzes life expectancy data.")
  data = read_file("life-expectancy.csv")

  # Find overall min and max life expectancy
  min_data, max_data = find_min_max(data, "Life expectancy (years)")
  print(f"Overall minimum life expectancy: {min_data['Life expectancy (years)']} in {min_data['Entity']} ({min_data['Year']})")
  print(f"Overall maximum life expectancy: {max_data['Life expectancy (years)']} in {max_data['Entity']} ({max_data['Year']})")

  # User input for year analysis:
  while True:
    year = input("Enter year of interest (or 'quit' to quit): ")
    if year.lower() == 'quit':
      break

    # Analyze data for the year
    average_life_expectancy, min_data, max_data = analyze_year(data, year)
    if average_life_expectancy is None:
      print(f"No data found for year {year}.")
    else:
      print(f"Average life expectancy for {year}: {average_life_expectancy}")
      print(f"Minimum life expectancy: {min_data['Life expectancy (years)']} in {min_data['Entity']}")
      print(f"Maximum life expectancy: {max_data['Life expectancy (years)']} in {max_data['Entity']}")

      while True:
        country = input("Enter country of interest (or 'quit' to quit): ")
        if country.lower() == 'quit':
            break

        average_life_expectancy, min_data, max_data = analyze_country(data, country)
        if average_life_expectancy is None:
            print(f"No data found for country {country}.")
        else:
            print(f"Average life expectancy for {country}: {average_life_expectancy}")
            print(f"Minimum life expectancy: {min_data['Life expectancy (years)']} in {min_data['Entity']} ({min_data['Year']})")
            print(f"Maximum life expectancy: {max_data['Life expectancy (years)']} in {max_data['Entity']} ({max_data['Year']})")

    # Find and print anomalies:
    anomalies = find_anomalies(data)
    for year, drop in anomalies:
        print(f"Significant drop in life expectancy in year {year}: {drop}")

if __name__ == "__main__":
  main()


# This test creates a small dataset where the life expectancy drops by 5 years from 2000 to 2001 in both countries. It then calls the find_anomalies function with this data and checks if the returned result matches the expected result.

# To run the test, you can save it in a Python file and run that file

#   import unittest

# class TestFindAnomalies(unittest.TestCase):
#     def test_find_anomalies(self):
#         data = [
#             {"Entity": "Country1", "Year": "2000", "Life expectancy (years)": "80"},
#             {"Entity": "Country1", "Year": "2001", "Life expectancy (years)": "75"},
#             {"Entity": "Country1", "Year": "2002", "Life expectancy (years)": "78"},
#             {"Entity": "Country2", "Year": "2000", "Life expectancy (years)": "70"},
#             {"Entity": "Country2", "Year": "2001", "Life expectancy (years)": "65"},
#             {"Entity": "Country2", "Year": "2002", "Life expectancy (years)": "68"},
#         ]
#         expected_result = [("2001", 5.0), ("2001", 5.0)]
#         self.assertEqual(find_anomalies(data), expected_result)

# if __name__ == "__main__":
#     unittest.main()