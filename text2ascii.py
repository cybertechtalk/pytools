import PIL.Image

def main():
    path = input("Enter the path to the image field : \n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "Unable to find image ");

    ASCII_CHARS = ["@", "#", "＄", "%", "?", "*", "+", ";", ":", ",", "."]

    def resize(image, new_width = 100):
        old_width, old_height = image.size
        new_height = new_width * old_height / old_width
        return image.resize(new_width, new_height)

    def to_greyscale(image):
        return image.convert("L")

    def pixel_to_ascii(image):
        pixels = image.getdata()
        ascii_str = "";
        for pixel in pixels:
            ascii_str += ASCII_CHARS[pixel//25];
        return ascii_str

    #image = resize(image);
    #convert image to greyscale image
    greyscale_image = to_greyscale(image)
    # convert greyscale image to ascii characters
    ascii_str = pixel_to_ascii(greyscale_image)
    img_width = greyscale_image.width
    ascii_str_len = len(ascii_str)
    ascii_img=""

    #Split the string based on width  of the image
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"
    #save the string to a file
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_img);

main()