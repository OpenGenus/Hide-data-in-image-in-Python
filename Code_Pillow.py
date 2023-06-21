from PIL import Image
from tkinter import * 
from tkinter import messagebox

def hide(image_path, output_path, text):
    image = Image.open(image_path)
    binary_str = ''.join(format(ord(char), '08b') for char in text)
    Len = (image.width * image.height)
    if len(binary_str)>Len:
        messagebox.showerror("Error", "Error")
        
    pixel_index = 0
    for bit in binary_str:
        pixel = image.getpixel((pixel_index % image.width, pixel_index))
        new_pixel = (pixel[0] & 0xFE) | int(bit)
        image.putpixel((pixel_index % image.width, pixel_index), new_pixel)
        pixel_index += 1
        
    image.save(output_path)
    messagebox.showinfo("Success", "Successful encoding")

def show (image_path):
    image = Image.open(image_path)
    binary_string = ''
    for pixel_index in range(image.width * image.height):
        pixel = image.getpixel((pixel_index % image.width, pixel_index))
        binary_string += str(pixel[0] & 1)
        
    text = ''.join(chr(int(binary_str[i:i+8], 2)) for i in range(0, 
    len(binary_string), 8))
    return text