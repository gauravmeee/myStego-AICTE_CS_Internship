# Image-Based Message Encryption

This project allows you to securely hide secret messages in images using steganography. The message is embedded within the pixels of an image, and the image remains visually unchanged. The encrypted image can only be decrypted using a passcode, ensuring that unauthorized users cannot retrieve the hidden message.

## Features
- Encrypt a message into an image.
- Decrypt the hidden message using a passcode.
- User-friendly input for entering a secret message and passcode.
- The ability to open the encrypted image automatically after encryption.
- Password-protected decryption to ensure security.

## Problem Statement
Traditional methods of text encryption may leave traces or become vulnerable to interception. This project solves the problem by using steganography to hide the message within an image. Only the correct passcode allows decryption, ensuring secure communication.

## Technologies Used
- **Python**: The programming language used for developing the project.
- **OpenCV**: For image processing (reading, manipulating, and saving images).
- **OS Module**: For opening the encrypted image on Windows automatically.

## How It Works
1. **Encryption**: 
   - The secret message is converted into its ASCII values and embedded into the RGB values of the image's pixels.
   - Each character of the message is placed in the pixels in sequence, and the image remains visually unchanged.

2. **Decryption**:
   - The hidden message is extracted from the image by reading the pixel values.
   - The message is then reconstructed by converting the pixel values back to ASCII characters.
   - The passcode is required to unlock the decryption process.

## Prerequisites
Make sure you have the following installed:
- Python 3.x
- OpenCV (`pip install opencv-python`)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/gauravmeee/myStego-AICTE_CS_Internship.git
   ```

2. Install dependencies:
   ```bash
   pip install opencv-python
   ```

## Usage

### Encrypt Message
1. Run the `encrypt_image` function.
2. Provide the following inputs:
   - The path to the image you want to use.
   - The secret message you want to hide.
   - A passcode for encryption.

   Example:
   ```python
   encrypt_image("path_to_image.jpg", "This is a secret message!", "mypassword")
   ```

### Decrypt Message
1. Run the decryption script.
2. Provide the passcode you used during encryption to retrieve the hidden message.

### Example:

```python
message = input("Enter secret message: ")
password = input("Enter a passcode: ")
encrypt_image("OriginalImage.jpg", message, password)
```

## Output
- The encrypted image will be saved as `EncryptedImage.jpg`.
- The message can be decrypted only by providing the correct passcode.

## GitHub Link
[GitHub Repository](https://github.com/gauravmeee/myStego-AICTE_CS_Internship.git)

## Future Scope
- Support for multiple messages within one image.
- Use stronger encryption techniques for added security.
- Explore web-based or mobile implementations for secure messaging.
