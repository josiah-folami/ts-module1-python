while True:
    try:
        fraction = input("Fraction: ")
        numerator, denominator = fraction.split("/")
        numerator = int(numerator)
        denominator = int(denominator)

        if denominator == 0 or numerator < 0 or denominator < 0:
            continue

        if numerator > denominator:
            continue

        percentage = round(numerator / denominator * 100)
        break

    except (ValueError, ZeroDivisionError):
        continue

if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")