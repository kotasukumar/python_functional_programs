import math


def calculate_wind_chill(temp, vel):
    return 35.74 + 0.6215 + 0.4275 * temp - 35.75 * math.pow(vel, 0.16)


if __name__ == "__main__":
    temperature = float(input("Enter the value of temperature(in fahrenheit): "))
    velocity = float(input("Enter the value of velocity(in miles per hour): "))
    wind_chill = calculate_wind_chill(temperature, velocity)
    print("Effective temperature is: ", wind_chill)
