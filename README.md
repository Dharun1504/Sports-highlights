# Sports Highlights Generator

This project aims to automate the process of generating highlights from sports match videos using various AI techniques. It includes modules for transcription, natural language processing (NLP), and video editing to create engaging highlight reels from raw match footage.

## Features

- **Automated Transcription**: Utilizes state-of-the-art automatic speech recognition (ASR) models to transcribe commentary from sports match videos into text.
- **NLP-based Highlight Extraction**: Applies natural language processing techniques to identify key moments in the match commentary, such as boundaries, wickets, and notable events.
- **AI-powered Video Editing**: Cuts and stitches video segments corresponding to the identified highlights to produce a concise and engaging highlight reel.
- **Multiple AI Models**: Supports multiple AI models for transcription, NLP-based analysis, and video editing, providing flexibility and customization options.
- **Web Interface with Flask API**: Provides a user-friendly web interface for uploading videos and generating highlights, powered by a Flask API backend.
- **Responsive Frontend with React**: Offers a modern and responsive user interface built using React for seamless interaction and user experience.

## Modules

### 1. Transcription (`transcription.py`)

- **Description**: Converts audio from sports match videos into text transcripts using automatic speech recognition (ASR) models.
- **Technologies**: Utilizes the Whisper ASR model for accurate and efficient transcription.

### 2. Natural Language Processing (NLP)

#### a. GPT-based Model (`gpt.py`)

- **Description**: Performs natural language processing tasks, such as identifying key events from match commentary and extracting timestamps for highlights.
- **Technologies**: Employs the GPT (Generative Pre-trained Transformer) model for language understanding and generation.

#### b. Gemini Model (`gemini.py`)

- **Description**: An alternative NLP model for extracting highlight timestamps from match commentary.
- **Technologies**: Utilizes the Gemini model, providing an alternative approach for highlight extraction.

### 3. Video Editing (`vidaud.py`, `vidgen.py`)

- **Description**: Handles the editing of sports match videos based on the timestamps extracted from the NLP module.
- **Technologies**: Employs the MoviePy library for video editing operations, including cutting, concatenation, and export.

### 4. Flask API (`flask-api.py`)

- **Description**: Provides a Flask API backend for the web interface, allowing users to upload videos and initiate the highlights generation process.
- **Technologies**: Utilizes Flask framework for building the API endpoints and handling requests.

### 5. React Frontend (`react`)

- **Description**: Implements a modern and responsive user interface using React for seamless interaction and user experience.
- **Technologies**: Utilizes React framework along with other related libraries and tools for frontend development.

## Usage

1. **Install Dependencies**: Ensure all required dependencies are installed by running `pip install -r requirements.txt` for the backend and `npm install` for the frontend.
2. **Start the Server**: Run `python flask-api.py` to start the Flask server for the web application and API.

   ![image](https://github.com/demi2k-sudo/Sports-highlights/assets/85375873/d86f66fe-c8d6-4ed7-9c53-e6862bf00fac)
   ![image](https://github.com/demi2k-sudo/Sports-highlights/assets/85375873/b95d52eb-11d6-4e0a-a04a-0df1db620f90)


4. **Access the Web Interface**: Open the provided URL in your web browser to access the web application.
5. **Upload Video**: Use the file upload feature to upload a sports match video.
6. **Generate Highlights**: Click the "Generate Highlights" button to initiate the highlights generation process.
7. **View Highlights**: Once the process is complete, the generated highlight reel will be displayed on the web interface for viewing and sharing.

