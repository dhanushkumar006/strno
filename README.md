StegoPy - Image Steganography Tool

📌 About the Project

StegoPy is a Python-based steganography tool designed to securely hide and extract messages within image files. It leverages image processing techniques to embed encrypted data within images while maintaining their visual integrity. This tool can be useful for secure communication, watermarking, and digital forensics.

✨ Features

✔️ Hide secret messages within image files
✔️ Extract hidden messages from steganographic images
✔️ Supports multiple image formats (PNG, JPG, BMP)
✔️ Lightweight and easy to use with minimal dependencies

🛠️ Installation

Ensure you have Python installed, then install the required dependencies:

pip install pillow

🚀 Usage

1️⃣ Encrypt a Message into an Image

To embed a secret message inside an image, run:

python stego.py --encrypt --input image.png --output encrypted_image.png --message "Hidden Secret"

After execution, encrypted_image.png will contain the hidden message.

2️⃣ Decrypt the Hidden Message

To extract a hidden message from an image, use:

python stego.py --decrypt --input encrypted_image.png

The script will retrieve and display the hidden message.

🔍 Example Output

Image encrypted successfully!
Image decrypted successfully!
Hidden message: "Hidden Secret"

🤝 Contribution

We welcome contributions! If you’d like to improve the project, feel free to fork the repository and submit a pull request.
