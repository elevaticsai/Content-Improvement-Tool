# Content-Improvement-Tool

This project is a web-based application that uses AI models (Llama3.2 and Ollama) to generate, optimize, and analyze content. The application provides users with the ability to input a topic, generate initial content, and then optimize it based on tone, style, and length preferences. Additionally, the tool provides a detailed analysis of the content, including scores for spelling, grammar, vocabulary, clarity, readability, and an overall score, each on a scale of 0 to 10.

## Features
- **Content Generation**: Generates initial content based on a given topic using Llama3.2.
- **Content Optimization**: Allows users to optimize the generated content by specifying tone, style, and length.
- **Detailed Analysis**: Provides scores for:
  - Spelling
  - Grammar
  - Vocabulary
  - Clarity
  - Readability
  - Overall Score (average of all other scores)
- **Score Visualization**: Displays scores as progress bars on a scale of 0 to 10.

## Prerequisites
- **Python 3.11 or higher**
- **Flask**
- **Requests** library

Ensure that the Llama3.2 and Ollama APIs are set up and running locally or accessible from your machine.

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/content-improvement-tool.git
   cd content-improvement-tool
   ```

2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install Flask requests
   ```

4. **Run the Application**:
   ```bash
   export FLASK_APP=app.py  # On Windows: set FLASK_APP=app.py
   export FLASK_ENV=development  # On Windows: set FLASK_ENV=development
   flask run
   ```

   The application will be available at `http://127.0.0.1:5000/`.

## Usage

1. **Open the Web Application**:
   Visit `http://127.0.0.1:5000/` in your web browser.

2. **Generate Content**:
   - Enter a topic in the input field.
   - Click the "Generate Content" button.
   - The generated content will appear in the "Generated Content" window.

3. **Optimize Content**:
   - Select tone, style, and length options.
   - Click the "Optimize Content" button.
   - The optimized content will appear in the "Generated Optimized Content" window.

4. **View Analysis Results**:
   - After optimization, detailed analysis scores will be displayed as progress bars under "Analysis Results".

## Code Overview

### Backend (`app.py`)
- **`/generate`**: Generates initial content using Llama3.2.
- **`/analyze`**: Optimizes the content based on user preferences and returns detailed analysis scores.
- **Dependencies**: Flask, requests.

### Frontend (`index.html`)
- Contains the user interface for inputting topics, selecting options, and displaying results.
- Includes JavaScript functions to handle API calls to the backend and update the UI with results.

## API Endpoints

### `POST /generate`
- **Request**:
  ```json
  {
    "topic": "Sample topic"
  }
  ```
- **Response**:
  ```json
  {
    "generatedContent": "Generated content based on the sample topic."
  }
  ```

### `POST /analyze`
- **Request**:
  ```json
  {
    "content": "Generated content here",
    "tone": "neutral",
    "style": "simple",
    "length": "medium"
  }
  ```
- **Response**:
  ```json
  {
    "generatedContent": "Optimized content here",
    "scores": {
      "spelling": 9,
      "grammar": 8,
      "vocabulary": 7,
      "clarity": 8,
      "readability": 9
    },
    "overallScore": 8
  }
  ```

## Troubleshooting

1. **Ensure the Llama3.2 and Ollama APIs are running and accessible.**
2. **Check Flask logs for any errors**: Flask will display errors in the terminal where it is running.
3. **Ensure correct Python version**: This application requires Python 3.11 or higher.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributing
If you would like to contribute to this project, feel free to open a pull request or submit an issue on GitHub.

