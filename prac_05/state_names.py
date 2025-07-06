"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

#loop to print all states and nearly lined up with string formatting
max_code_length = max(len(state_code) for state_code in CODE_TO_NAME.keys())
state_codes = CODE_TO_NAME.keys()
for state_code in state_codes:
    print(f"{state_code:{max_code_length}} is {CODE_TO_NAME[state_code]}")

