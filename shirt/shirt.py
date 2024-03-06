from PIL import Image, ImageOps
import sys

def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif "jpg" in sys.argv[1] and "jpg" in sys.argv[2]:
        get_image(sys.argv[1], sys.argv[2])
    elif "png" in sys.argv[1] and "png" in sys.argv[2]:
        get_image(sys.argv[1], sys.argv[2])
    elif "jpg" not in sys.argv[1] and "jpg" not in sys.argv[2] and "png" not in sys.argv[1] and "png" not in sys.argv[2]:
        sys.exit("Invalid output")
    else:
        sys.exit("Input and output have different extensions")

def get_image(arg1, arg2):
    try:
        shirt = Image.open("shirt.png")
        with Image.open(arg1) as arg1:
            img_cropped = ImageOps.fit(arg1, shirt.size)
            img_cropped.paste(shirt, mask = shirt)
            img_cropped.save(arg2)
    except FileNotFoundError:
        sys.exit(f"Input does not exist")
if __name__ == "__main__":
    main()




