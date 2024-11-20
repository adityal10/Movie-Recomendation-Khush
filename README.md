# Movie Recommendation System

## Overview
A sophisticated movie recommendation application built using Python, leveraging machine learning techniques to suggest similar movies based on user input. The system uses TF-IDF vectorization and cosine similarity to generate personalized movie recommendations.

## Features
- Interactive GUI with CustomTkinter
- Movie recommendation based on multiple features
- Intelligent movie name matching
- Top 10 similar movie suggestions
- User-friendly interface
- Error handling for invalid inputs

## Technical Stack
- **Language**: Python
- **Machine Learning Libraries**: 
  - scikit-learn
  - pandas
  - numpy
- **Natural Language Processing**: 
  - NLTK
- **GUI Framework**: 
  - CustomTkinter
  - Tkinter
- **Additional Libraries**: 
  - matplotlib
  - PIL (Python Imaging Library)

## Key Components
- TF-IDF Vectorization
- Cosine Similarity Algorithm
- Movie Feature Extraction
- Fuzzy Movie Name Matching

## Recommendation Methodology
The system combines multiple movie features to generate recommendations:
- Genres
- Keywords
- Tagline
- Cast
- Director

## Prerequisites
- Python 3.7+
- pip package manager

## Installation

### Required Libraries
```bash
pip install pandas numpy scikit-learn nltk customtkinter pillow matplotlib
```

### Additional Setup
1. Download the `movies.csv` dataset
2. Place the dataset in the same directory as the script
3. Ensure search and background images are in the correct path

## Usage
1. Run the script
2. Enter a movie name in the input field
3. Click the search button or press Enter
4. View top 10 movie recommendations in the text box

## Input Guidelines
- Enter the movie name exactly or close to its actual title
- If the movie is not found, an error message will be displayed

## Project Structure
- `main.py`: Main application script
- `movies.csv`: Movie dataset
- `search1.png`: Search button image
- `pic.png`: Background image

## Potential Improvements
- Add more sophisticated recommendation algorithms
- Implement caching for faster recommendations
- Create a web-based interface
- Add more detailed movie information
- Improve error handling and user feedback

## Limitations
- Recommendations based on limited features
- Requires local dataset
- Performance depends on dataset quality

## Disclaimer
This recommendation system is for educational purposes and may not reflect professional recommendation engines.
