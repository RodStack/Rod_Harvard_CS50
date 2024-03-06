import pyfiglet
import sys
from pyfiglet import Figlet

figlet = Figlet()

fonts = figlet.getFonts()

if len(sys.argv) == 1:
    letters = input()
    result = pyfiglet.figlet_format(letters)
    print(result)
elif len(sys.argv) > 1 and "-f" in sys.argv[1] and sys.argv[2] in fonts and "--f" not in sys.argv[1]:
    try:
        font = sys.argv[2]
        letters = input()
        result = pyfiglet.figlet_format(letters, font=font)
        print(result)

    except NameError:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")