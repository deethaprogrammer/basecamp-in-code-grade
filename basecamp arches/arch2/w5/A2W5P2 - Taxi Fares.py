def calculate_fare(distance):
    dis_m = distance * 1000
    amount = dis_m
    times = 0
    while amount > 0:
        amount = dis_m - 140
        dis_m = amount
        times += 1
    print(f'Total fare: {times * 0.25 + 4} euro')

if __name__  ==  "__main__":
    distance_km = float(input("Distance traveled: "))
    calculate_fare(distance_km)