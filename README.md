# QR-Studio
A highly customizable QR Code generator built in Python.

# Custom QR Code Generator (Python) 🎨🔍

A lightweight and highly customizable QR Code generator built in Python. This project allows you to move away from boring, standard black-and-white QR codes by giving you full control over colors, sizing, margins, and resolution.

## ✨ Features
- **Custom Palette:** Choose any foreground (`fill_color`) and background (`back_color`) color using standard names (e.g., `"purple"`) or Hexadecimal codes (e.g., `"#1A5276"`).
- **High Resolution:** Adjust the pixel size of individual blocks (`box_size`) to scale the resolution for print or digital media.
- **Safety Margin:** Customize the border size to guarantee flawless scanning on any device.
- **Clean Output:** Automatically saves the generated image directly adjacent to the script execution path.

## 🛠️ Prerequisites & Installation

To run this project locally, make sure you have Python installed. Then, install the required dependencies:

```bash
pip install qrcode[pil] Pillow
