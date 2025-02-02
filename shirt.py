"""

After finishing CS50 itself, students on campus at Harvard traditionally receive their very own I took CS50 t-shirt. No need to buy one online, but like to try one on virtually?

In a file called shirt.py, implement a program that expects exactly two command-line arguments:

in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output
The program should then overlay shirt.png (which has a transparent background) on the input after resizing and cropping the input to be the same size, saving the result as its output.

Open the input with Image.open, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open, resize and crop the input with ImageOps.fit,
per pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit, using default values for method, bleed, and centering, overlay the shirt with Image.paste,
per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste, and save the result with Image.save, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.

The program should instead exit via sys.exit:

if the user does not specify exactly two command-line arguments,
if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
if the input’s name does not have the same extension as the output’s name, or
if the specified input does not exist.
Assume that the input will be a photo of someone posing in just the right way, like these demos, so that, when they’re resized and cropped, the shirt appears to fit perfectly.

If you’d like to run your program on a photo of yourself, first drag the photo over to VS Code’s file explorer, into the same folder as shirt.py. No need to submit any photos with your code.
But, if you would like, you’re welcome (but not expected) to share a photo of yourself wearing your virtual shirt in any of CS50’s communities!

image = Image.open(prompt_input)
                    images.append(image)
"""
import sys
from PIL import Image, ImageOps
#ImageOps.fit
#Image.paste, method, bleed, centering
#Image.save


def main():
    convert_photo()

#we have now the 2 args with all the filters passed
def convert_photo():
    muppet = open_input()
    combined = open_output()
    shirt = Image.open("shirt.png")
    #Before paste i have to resize and crop
    muppet = ImageOps.fit(muppet, shirt.size)
    #all done, just paste and save
    muppet.paste(shirt, shirt)
    muppet.save(combined)

#catch FileNotFoundError (File1 or File2 don't exist)
#Return values case insensitive
def open_input():
    file1, file2 = take_argvs()
    try:
        return Image.open(file1)
    except FileNotFoundError:
        sys.exit("Input does not exist")

def open_output():
    file1, file2 = take_argvs()
    try:
        return file2
    except FileNotFoundError:
        sys.exit("Invalid output")

def take_argvs():
    prompt_input = sys.argv[1].casefold()
    prompt_output = sys.argv[2].casefold()
    catch_IndexError()
    #could have used os.path.splitext(path)
    if prompt_output.endswith(".jpg") or prompt_output.endswith(".jpeg") or prompt_output.endswith(".png"):
        pass
    else:
        sys.exit(f"{sys.argv[2]} is not a jpg, jpeg or png file")

    if prompt_input.endswith(".jpg") or prompt_input.endswith(".jpeg") or prompt_input.endswith(".png"):
        # argv 1 y 2 != extension
        if prompt_input.endswith(".jpg") and prompt_output.endswith(".jpg") or prompt_input.endswith(".jpeg") and prompt_output.endswith(".jpeg") or prompt_input.endswith(".png") and prompt_output.endswith(".png"):
            return (prompt_input, prompt_output)
        else:
            sys.exit("Input and output have different extensions")
    else:
        sys.exit(f"{sys.argv[1]} is not a jpg, jpeg or png file")

def catch_IndexError():
    #catch IndexError (too few or too many Command-line argvs)
    try:
        #expects 2 command-line argument
        if len(sys.argv) == 3:
            pass
        elif len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        else:
            sys.exit("Too many command-line arguments")
    except IndexError:
        pass


if __name__ == "__main__":
    main()
