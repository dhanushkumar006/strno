from PIL import Image
def encrypt_image(input_path , output_path):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # swapping red and blue channels
            encrypted_pixel = (b, g, r)

            pixels[i, j] = encrypted_pixel

    img.save(output_path)
    print("Image encrypted successfully!")

def decrypt_image(input_path , output_path):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # swapping red and blue channels back
            decrypted_pixel = (b, g, r)

            pixels[i, j] = decrypted_pixel

    img.save(output_path)
    print("Image decrypted successfully!")

input_image = r"C:\Users\dhanu\OneDrive\Desktop\New folder (3)\Input.jpg"
encrypted_image = r"C:\Users\dhanu\OneDrive\Desktop\New folder (3)\encrypted_image.jpg"
decrypted_image = r"C:\Users\dhanu\OneDrive\Desktop\New folder (3)\decrypted_image.jpg"


encrypt_image(input_image , encrypted_image)


decrypt_image(encrypted_image , decrypted_image)


