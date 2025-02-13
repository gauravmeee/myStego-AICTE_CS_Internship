import cv2
import os
import string

img = cv2.imread("Original.jpg")  # Replace with the correct image path

msg = input("Enter secret message:")
password = input("Enter a passcode:")

d = {}
c = {}

# Create dictionaries for mapping characters to their ASCII values and vice versa
for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

m = 0
n = 0
z = 0

# Embed the message into the image
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]  # Set pixel value to the ASCII value of the message character
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

# Save the modified image
cv2.imwrite("Encrypted.jpg", img)
os.system("start Encrypted.jpg")  # Open the image on Windows

# Decryption part
message = ""
n = 0
m = 0
z = 0

pas = input("Enter passcode for Decryption:")
if password == pas:
    for i in range(len(msg)):
        message = message + c[img[n, m, z]]  # Extract ASCII value from pixel and convert to character
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    print("Decryption message:", message)
else:
    print("YOU ARE NOT authorized")
