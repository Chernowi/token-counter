# Token Counter Application

## Overview
The Token Counter application is a Streamlit-based tool that allows users to upload various file formats (PDF, TXT, DOCX) and count the number of tokens in the text extracted from these files.

## Features
- Upload files in PDF, TXT, or DOCX format.
- Extract text from the uploaded files.
- Count the total number of tokens in the extracted text.
- Display a preview of the text extracted from the file.

## Installation
To set up the project, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd token-counter
pip install -r requirements.txt
```

## Usage
To run the application, execute the following command:

```bash
streamlit run src/app.py
```

Open your web browser and navigate to `http://localhost:8501` to access the application.

## Testing
To run the tests for the application, use the following command:

```bash
pytest
```

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.