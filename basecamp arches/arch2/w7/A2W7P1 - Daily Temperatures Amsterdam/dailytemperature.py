"""
Menu:
[1] Print the average temperature per year (Fahrenheit).
[2] Print the average temperature per year (Celsius) Hint: Use the built-in map() function.
[3] Print the warmest and coldest year as tuple based on the average temperature.
[4] Print the warmest month of a year based on the input year of the user (full month name)
[5] Print the coldest month of a year based on the input year of the user (full month name)
[6] Print a list of tuples where the first element of each tuple is the year and
    the second element of the tuple is a dictionary with months as the keys and
    the average temperature (in Celsius) of each month as the value

---Criteria---
function:
-load_txt_file
storage:
{year: {month: [temp, temp, temp, ...]}, ...}

function:
-fahrenheit_to_celsius(fahrenheit: float) -> float
that given the value in Fahrenheit returns the temperature in Celsius (rounding is not needed)

-average_temp_per_month(temperatures_for_year: dict) -> list
that calculates the average temperature per month. Return a list of tuples (month, temperature).

-average_temp_per_year(temperatures: dict) -> list
that calculates the average temperature per year. Return a list of tuples (year, temperature).
"""
import os
import sys


def load_txt_file(file_name):
    file_content = []
    data = {}
    with open(os.path.join(sys.path[0], file_name), newline='', encoding="utf8") as file_obj:
        for line in file_obj.readlines():
            file_content.append(line.split())
    for lines in file_content:
        year = int(lines[2])
        month = int(lines[0])
        temp = float(lines[3])
        if year not in data:
            data[year] = {}
        if month not in data[year]:
            data[year][month] = []
        data[year][month].append(temp)
        
    return data

def average_temp_per_year(temperatures: dict) -> list:
    avarage_year = {}
    results = []
    for year in temperatures.keys():
        year_val = []
        days = 0
        for month in temperatures[year]:
            for i in range(len(temperatures[year][month])):
                year_val.append(temperatures[year][month][i])
                days += 1
        avg_fahr = (sum(year_val) / days)
        results.append((year, avg_fahr))
    return results

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9

def average_temp_per_month(temperatures_for_year: dict) -> list:
    avg_month = {}
    monthly = []
    for month, temps in temperatures_for_year.items():
        avg = sum(temps) / len(temps)
        avg_month[month] = avg
        sorted_month =  sorted(avg_month.items(), key=lambda x: x[1], reverse=True)
    return sorted_month

def chosen(choice, data):
    month_names = {
        1: "January", 2: "February", 3: "March", 4: "April",
        5: "May", 6: "June", 7: "July", 8: "August",
        9: "September", 10: "October", 11: "November", 12: "December"
        }
    if choice == '1':
        return print(average_temp_per_year(data))
    if choice == '2':
        for year in data:
            for month in data[year]:
                data[year][month] = list(map(fahrenheit_to_celsius, data[year][month]))
        return print(average_temp_per_year(data))
    if choice == '3':
        result = average_temp_per_year(data)
        sorted_result = sorted(result, key=lambda x: x[1])
        return print((sorted_result[-1][0], sorted_result[0][0]))
        pass
    if choice == '4':
        year = int(input("which year?: "))
        sorted_month = average_temp_per_month(data[year])
        warmest_month_num = sorted_month[0][0]
        return print(month_names[warmest_month_num])
    if choice == '5':
        year = int(input("which year?: "))
        sorted_month = average_temp_per_month(data[year])
        coldest_month = sorted_month[-1][0]
        return print(month_names[coldest_month])
    if choice == '6':
        result = []
        
        for year in data:
            monthly_avg = {}
            for month in data[year]:
                celcius_temp = list(map(fahrenheit_to_celsius, data[year][month]))
                data[year][month] = celcius_temp
                avg_celcius = sum(celcius_temp) / len(celcius_temp)
                monthly_avg[month] = avg_celcius
            result.append((year, monthly_avg))
        return print(result)
    pass

if __name__ == "__main__":
    data = load_txt_file("NLAMSTDM.txt")
    choice = input("[1] Print the average temperature per year (Fahrenheit).\n[2] Print the average temperature per year (Celsius)\n[3] Print the warmest and coldest year\n[4] Print the warmest month of a year based on the input year of the user (full month name)\n[5] Print the coldest month of a year based on the input year of the user (full month name)\n[6]\n>")
    chosen(choice, data)