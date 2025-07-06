COLOR_TO_CODE = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "Blue": "#0000ff"
}

LOWERCASE_COLOR_TO_CODE = {names.lower(): codes for names, codes in COLOR_TO_CODE.items()}
color_input = input("Enter color name: ").lower()
while color_input != "":
    try:
        print(f"{color_input} is {LOWERCASE_COLOR_TO_CODE[color_input]}")
    except KeyError:
        print("Invalid color name")
    color_input = input("Enter color name: ").lower()