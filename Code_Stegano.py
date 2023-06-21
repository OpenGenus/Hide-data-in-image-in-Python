from stegano import lsb

# Function to hide text data in an image
def hide_text_in_image(image_path, output_path, text):
    # Hide the text in the image using Stegano
    secret_image = lsb.hide(image_path, text)
    
    # Save the modified image with the hidden text
    secret_image.save(output_path)
    print('Text hidden successfully in the image.')

# Function to extract hidden text from an image
def extract_text_from_image(image_path):
    # Extract the hidden text from the image using Stegano
    secret_image = lsb.reveal(image_path)
    
    return secret_image