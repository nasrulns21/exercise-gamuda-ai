def celsius_to_fahrenheit(celsius: float) -> float:
    if not isinstance(celsius, (int, float)) or isinstance(celsius, bool):
        raise TypeError("celsius must be a number")
    return celsius * 9 / 5 + 32


def main() -> None:
    try:
        value = float(input("Enter temperature in Celsius: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    print(f"{value:.1f}°C = {celsius_to_fahrenheit(value):.1f}°F")


if __name__ == "__main__":
    main()
