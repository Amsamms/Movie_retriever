## TMDb Movie Info Retriever
A simple Streamlit app that retrieves detailed movie information from The Movie Database (TMDb) API. The app allows you to enter your TMDb API key, search for a movie by title, and select which attributes to display. The results are shown in a neatly formatted table.

## Features
Movie Search: Input a movie name to search for its details.
Attribute Selection: Choose from a comprehensive list of movie attributes (with an "ALL" option to display all available data).
Formatted Output: Display selected movie information in a clean, easy-to-read table.
TMDb API Integration: Retrieves movie details and actor information (credits) using TMDb endpoints.

## Getting Started
Prerequisites
Python 3.7 or higher
Streamlit
Requests
Pandas
## Installation
Clone the Repository:
bash
Copy
git clone https://github.com/Amsamms/Movie_retrievercd Movie_retriever
## (Optional point) Create and Activate a Virtual Environment:
bash
Copy
python -m venv venv# On macOS/Linux:source venv/bin/activate# On Windows:
venv\Scripts\activate
## Install Dependencies:
pip install -r requirements.txt

## Usage
Obtain Your TMDb API Key

Sign up at TMDb and request an API key.
## Run the App

streamlit run app.py
## Using the App
- Enter your TMDb API key and the movie name.
- Select the movie attributes you want to display (or choose "ALL").
- Click Get Movie Info to view the results in a neatly formatted table.
## File Structure
app.py: The main Streamlit application script.
README.md: This README file.
requirements.txt: (Optional) File listing the project's dependencies.
## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests with improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
TMDb for providing the movie database API.
Streamlit for their intuitive app framework.
```
