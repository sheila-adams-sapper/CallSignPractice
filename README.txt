# Amateur Radio Call-Sign Practice

A Streamlit web application for practicing amateur radio call-sign recognition using the ITU phonetic alphabet.

## Features

- Generates random amateur radio call signs
- Speaks call signs using phonetic alphabet
- Adjustable delay between call signs
- Cross-platform text-to-speech support (Windows, macOS, Linux)
- Simple start/stop controls

## Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd CallSignPractice
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application locally:
```bash
streamlit run streamlit_callsign_practice.py
```

The application will open in your default web browser at `http://localhost:8501`

## How to Use

1. Adjust the delay slider (2-10 seconds between call signs)
2. Click "Start" to begin generating random call signs
3. Listen to the phonetic pronunciation
4. Click "Stop" to pause the practice session

## Call Sign Format

The app generates call signs using standard amateur radio formats:
- **Prefixes**: K, N, W, AA, AB, AC, AD, AE
- **Number**: 0-9
- **Suffix**: 2-3 random letters

## Requirements

- Python 3.7+
- Streamlit
- Built-in OS text-to-speech capabilities

## License

This project is open source and available under the [MIT License](LICENSE).

