# Sports Highlights Generator

This project aims to automate the process of generating highlights from sports match videos using various AI techniques. It includes modules for transcription, natural language processing (NLP), and video editing to create engaging highlight reels from raw match footage.

## Features

- **Automated Transcription**: Utilizes state-of-the-art automatic speech recognition (ASR) models to transcribe commentary from sports match videos into text.
- **NLP-based Highlight Extraction**: Applies natural language processing techniques to identify key moments in the match commentary, such as boundaries, wickets, and notable events.
- **AI-powered Video Editing**: Cuts and stitches video segments corresponding to the identified highlights to produce a concise and engaging highlight reel.
- **Multiple AI Models**: Supports multiple AI models for transcription, NLP-based analysis, and video editing, providing flexibility and customization options.

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

### 4. Web Application (`app.py`, `videouploadpage.js`)

- **Description**: Provides a user-friendly interface for uploading sports match videos and generating highlight reels.
- **Technologies**: Built using React.js for the frontend and Flask for the backend, facilitating seamless integration with the AI modules.

## Usage

1. **Install Dependencies**: Ensure all required dependencies are installed by running `pip install -r requirements.txt` for the backend and `npm install` for the frontend.
2. **Start the Server**: Run `python app.py` to start the Flask server for the web application.
3. **Access the Web Interface**: Open the provided URL in your web browser to access the web application.
4. **Upload Video**: Use the file upload feature to upload a sports match video.
5. **Generate Highlights**: Click the "Generate Highlights" button to initiate the highlights generation process.
6. **View Highlights**: Once the process is complete, the generated highlight reel will be displayed on the web interface for viewing and sharing.
