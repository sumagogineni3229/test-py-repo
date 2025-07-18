def convert_temperature(value, unit):
    unit = unit.lower()
    if unit == 'c':
        fahrenheit = (value * 9/5) + 32
        kelvin = value + 273.15
        return {'Celsius': value, 'Fahrenheit': fahrenheit, 'Kelvin': kelvin}
    elif unit == 'f':
        celsius = (value - 32) * 5/9
        kelvin = celsius + 273.15
        return {'Celsius': celsius, 'Fahrenheit': value, 'Kelvin': kelvin}
    elif unit == 'k':
        celsius = value - 273.15
        fahrenheit = (celsius * 9/5) + 32
        return {'Celsius': celsius, 'Fahrenheit': fahrenheit, 'Kelvin': value}
    else:
        raise ValueError("Invalid unit. Please enter 'C' for Celsius, 'F' for Fahrenheit, or 'K' for Kelvin.")

def main():
    try:
        value = float(input("Enter the temperature value: "))
        unit = input("Enter the unit of the temperature (C/F/K): ")
        conversions = convert_temperature(value, unit)
        print("\nConverted Temperatures:")
        for scale, temp in conversions.items():
            print(f"{scale}: {temp:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()