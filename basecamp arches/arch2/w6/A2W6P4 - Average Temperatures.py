"""
---criteria---
implement a program that prints the answer of the given questions:
-how many unique days have equal avarege temp in march 1995 and march 2010
-How many unique days have equal average temperatures in March 1995 and March 2020?
-Which year has a day with the highest temperature in March?
-Which year had the warmest March?
"""

temperatures = (
    ('1995', '3', [
        '47.3', '40.0', '38.3', '36.3', '37.4', '40.3', '41.1', '40.5', '41.6', '43.2',
        '46.2', '45.8', '44.9', '39.4', '40.5', '42.0', '46.5', '46.2', '43.3', '41.7',
        '40.7', '39.6', '44.2', '47.8', '45.9', '47.3', '39.8', '35.2', '38.5', '40.5', '47.0'
    ]),
    ('2010', '3', [
        '39.2', '36.7', '35.5', '35.2', '35.8', '33.8', '30.7', '33.2', '32.3', '33.3',
        '37.3', '39.9', '40.8', '42.9', '42.7', '42.6', '44.8', '50.3', '52.2', '55.2',
        '47.2', '45.0', '48.6', '55.0', '57.4', '50.9', '48.6', '46.2', '49.6', '50.1', '43.6'
    ]),
    ('2020', '3', [
        '43.2', '41.1', '40.0', '43.6', '42.6', '44.0', '44.0', '47.9', '46.6', '50.5',
        '51.5', '47.7', '44.7', '44.0', '48.9', '45.3', '46.6', '49.7', '47.2', '44.8',
        '41.8', '40.9', '41.0', '42.7', '43.4', '44.0', '46.4', '45.5', '40.7', '39.5', '40.6'
    ])
)
year_temps = {
    '1995': set(temperatures[0][2]),
    '2010': set(temperatures[1][2]),
    '2020': set(temperatures[2][2])
}
"""
questions:
1.how many unique days have equal avarege temp in march 1995 and march 2010
2.How many unique days have equal average temperatures in March 1995 and March 2020?
3.Which year has a day with the highest temperature in March?
4.Which year had the warmest March?
"""
if __name__ == "__main__":
    print(f'Answer_1 = {len(year_temps["1995"] & year_temps["2010"])}')
    print(f'Answer_2 = {len(year_temps["1995"] & year_temps["2020"])}')

    max_temp = max(
        max(map(float, temps)) for temps in year_temps.values()
    )

    for year, temps in year_temps.items():
        if max_temp in map(float, temps):
            print(f'Answer_3 = {year}')
            break
        
    avg_temp_year = {
        year: sum(map(float, temps)) / len(temps)
        for year, temps in year_temps.items()
    }

    warmest_year = max(avg_temp_year.items(), key=lambda x: x[1])[0]
    print(f'Answer_4 = {warmest_year}')