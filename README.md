# Flask File Upload App

This Flask application allows users to upload files through a web interface. The uploaded files are saved in a specified folder on the server. The application supports various file types, which are specified in the configuration.

## Features

- Multiple file upload
- Support for a wide range of file extensions
- File upload status messages

## Requirements

- Python 3.x
- Flask

## Installation

1. Clone the repository:

    ```bash
    git clone <your-repository-url>
    ```
  
2. Navigate to the project directory:

    ```bash
    cd <your-project-directory>
    ```

3. Install the required Python packages:

    ```bash
    pip install flask
    ```

## Configuration

You can configure the allowed file extensions in the `app.config['ALLOWED_EXTENSIONS']` list in the `main.py` file.

## Usage

1. Ensure that the `uploads` folder exists in the project directory. If it doesn't, the application will create it automatically when you run the app.

2. Run the application:

    ```bash
    python main.py
    ```

3. Open a web browser and navigate to `http://0.0.0.0:5000/`. You'll see the file upload form.

4. Select files to upload, and click the 'Upload' button. Uploaded files will be saved in the `uploads` folder.

## Folder Structure

```plaintext
├── uploads/
│   └── (uploaded files)
├── templates/
│   └── index.html
└── main.py
