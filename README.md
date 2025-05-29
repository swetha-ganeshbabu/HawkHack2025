# 3Ducate

3Ducate is an interactive web application that transforms flat textbook diagrams into immersive 3D experiences. Using augmented reality, users can scan, explore, and interact with 3D models in real-time. The application is powered by AI to provide smart labels, voice-guided insights, and curated educational videos, making learning more engaging and memorable.

## Features

- **3D Model Viewer**: Display GLB models using Three.js with enhanced lighting and camera setup for a realistic experience.
- **Advanced Mouse Controls**: Rotate, zoom, and interact with 3D models easily using smooth mouse controls.
- **Spline 3D Robot UI**: Utilize Spline 3D CSS robot models for an advanced, polished, and visually engaging user interface.
- **AR Integration**: Overlay 3D models directly onto live webcam feeds with options for white, black, or live backgrounds.
- **Gesture-Based Hand Tracking**: Interact with models in real-time using hand gestures detected by MediaPipe Hands.
- **AI Object Recognition**: Capture photos and analyze them using the Gemini API for smart object detection.
- **3D Model Auto-Labeling**: Use the Gemini API to automatically label parts of 3D models for enhanced learning and exploration.
- **Multimedia Integration**: Fetch related YouTube videos and synthesize speech to read explanations, enhancing multimedia learning.

## Dependencies

- **Flask**: Web framework for building the application.
- **Flask-CORS**: Extension for handling Cross-Origin Resource Sharing (CORS).
- **Gunicorn**: WSGI HTTP Server for serving the application.
- **Three.js**: JavaScript library for creating and displaying 3D graphics.
- **MediaPipe**: Library for hand tracking and gesture recognition.
- **Gemini API**: For AI object recognition and model labeling.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd 3Ducate
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your web browser and navigate to `http://localhost:5000` to access the application.

## Usage

- **Open Camera**: Click the "Open Camera" button to start the webcam feed.
- **Take Photo**: Use the "Take Photo" button to capture an image for AI analysis.
- **Change Background**: Toggle between webcam, white, and black backgrounds.
- **Interact with 3D Models**: Use mouse controls or hand gestures to rotate, zoom, and explore the 3D models.
- **View Educational Videos**: Access related YouTube videos for further learning.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 