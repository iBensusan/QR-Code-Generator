# QR Code Generator

A simple web application built with Flask that generates QR codes for any URL entered by the user. Users can download the generated QR code as an image file.

## Features

- **QR Code Generation**: Generates a QR code based on the URL entered by the user.
- **Downloadable QR Code**: Allows users to download the generated QR code as a PNG image.
- **Elegant UI**: User-friendly and responsive interface with a dark-themed design.

## Requirements

- Python 3.13
- Flask
- qrcode
- pillow

## Installation

1. Clone the repository and navigate to the project directory:
    ```bash
    git clone https://github.com/yourusername/qr_code_generator.git
    cd qr_code_generator
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```bash
    pip install Flask qrcode[pil]
    ```

## Usage

1. Run the Flask application:
    ```bash
    python app.py
    ```
   
2. Open a web browser and go to `http://127.0.0.1:5000`.

3. Enter a URL in the input field and click **Generate QR Code**. The application will generate a QR code and provide a download link.

## Example Workflow

1. Start the Flask application and open it in a browser.
2. Enter the desired URL in the provided field.
3. Click the **Generate QR Code** button.
4. Download the generated QR code image and scan it with a mobile device to test the link.

## Files

- `app.py`: The main Python script that implements the Flask application and QR code generation functionality.
- `static/styles.css`: Contains the custom CSS for styling the application's interface.
- `templates/index.html`: The HTML template file for the application's front-end layout.
- `README.md`: Project description and instructions.

## License

This project is licensed under the MIT License 
