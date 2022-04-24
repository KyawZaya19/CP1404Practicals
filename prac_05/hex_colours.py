"""   program that allows you to look
 up hexadecimal colour codes """

COLOUR_CODES = {"ACIDGREEN": "#b0bf1a", "ALICEBLUE": "#f0f8ff",
                "ALIZARINCRIMSON": "#e32636", "AQUAMARINE1": "#7fffd4", "AQUAMARINE2": "#76eec6",
                "AQUAMARINE4": "#458b74", "AZURE1": "#f0ffff",
                "AZURE2": "#e0eeee", "AZURE3": "#c1cdcd", "AZURE4": "#838b8b"}

colour_name = input("Enter a colour name: ").upper()
while colour_name != "":
    if colour_name in COLOUR_CODES:
        print(colour_name, "is", COLOUR_CODES[colour_name])
    else:
        print("Invalid colour name")
    colour_name = input("Enter a colour name: ")

