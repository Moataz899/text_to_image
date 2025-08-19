# 🎨 AI Text-to-Image Generator

## 🎯 Overview
This application is a powerful AI-powered text-to-image generator that transforms textual descriptions into stunning, high-quality images. Built with Python Flask, it provides an intuitive web interface for creating unique AI-generated artwork from simple text prompts.

## 🚀 Features
- **🎨 AI Image Generation**: Generate unique, high-quality images from text descriptions using a local model.
- **🌐 Web Interface**: Clean, responsive web interface built with HTML, CSS, and JavaScript.
- **💾 Automatic Saving**: Generated images are automatically saved to organized folders.
- **⚡ Real-time Processing**: Fast image generation with progress indicators.
- **🎯 Customizable Prompts**: Support for detailed, creative text prompts.
- **📱 Responsive Design**: Works seamlessly on desktop and mobile devices.

## 📁 Project Structure
```
Text_to_Image/
├── 📁 data/
│   └── 📁 generated_images/          # Storage for AI-generated images
├── 📁 models/
│   └── model1.py                    # AI model configuration and utilities
├── 📁 notebooks/
│   └── text_to_image.ipynb          # Jupyter notebook for experimentation
├── 📁 static/
│   ├── script.js                    # Frontend JavaScript functionality
│   └── styles.css                   # CSS styling for web interface
├── 📁 templates/
│   └── index.html                   # Main web interface template
├── 📁 venv3135/                     # Python virtual environment
├── app.py                           # Main Flask application
├── requirements.txt                 # Python dependencies
├── .gitignore                       # Git ignore rules
├── LICENSE                          # Project license
└── README.md                        # This file
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Git

### Step-by-Step Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Moataz899/text_to_image.git
   cd Text_to_Image
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv3135
   ```

3. **Activate virtual environment**
   - On Windows:
     ```bash
     venv3135\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv3135/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 📊 Model Details

### AI Model Specifications
- **Model**: Local model for image generation
- **Image Size**: 512x512 pixels (default)
- **Inference Steps**: 50 (configurable)

### Technical Architecture
- **Backend**: Python Flask web framework
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Image Processing**: PIL (Pillow) library
- **File Management**: Automatic timestamp-based naming

## 🖥️ Usage Guide

### Starting the Application
1. Ensure virtual environment is activated
2. Run the Flask application:
   ```bash
   python app.py
   ```
3. Open your browser to: `http://127.0.0.1:5000`

### Web Interface Navigation
1. **Home Page**: Clean interface with text input area
2. **Prompt Input**: Enter your creative description
3. **Generate Button**: Click to start image generation
4. **Progress Indicator**: Shows generation progress
5. **Result Display**: Generated image appears with download option

## 🚀 Quick Start

### 5-Minute Setup
```bash
# 1. Clone and enter directory
git clone https://github.com/Moataz899/text_to_image.git
cd Text_to_Image

# 2. Setup environment
python -m venv venv3135
venv3135\Scripts\activate  # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
```

### First Image Generation
1. Open `http://127.0.0.1:5000`
2. Enter prompt: "A serene Japanese garden with cherry blossoms and a koi pond"
3. Click "Generate Image"
4. Wait 10-30 seconds for generation
5. Download your AI-generated artwork!

## 📝 Example Usage

### Creative Prompt Examples
```
1. "A futuristic cyberpunk city at night, neon lights reflecting on wet streets, flying cars, ultra-detailed, cinematic lighting"

2. "A peaceful mountain landscape at sunrise, crystal-clear lake reflecting snow-capped peaks, hyper-realistic, 8k nature photography"

3. "An elderly Egyptian man in traditional clothing, wise eyes, golden hour lighting, portrait photography style"

4. "A magical forest with glowing mushrooms, fairy lights, mystical atmosphere, fantasy art style"
```

### Advanced Usage Tips
- **Be Specific**: Include details about lighting, style, mood
- **Use Adjectives**: Descriptive words improve results
- **Specify Style**: Mention "photorealistic", "oil painting", "digital art", etc.
- **Include Context**: Time of day, weather, setting details

## 🔍 Troubleshooting

### Common Issues and Solutions

**Issue**: "RuntimeError: CUDA out of memory"
- **Solution**: Reduce image size or use CPU inference

**Issue**: "Port 5000 already in use"
- **Solution**: Change port in app.py or kill existing process:
  ```bash
  # Windows
  netstat -ano | findstr :5000
  taskkill /PID <PID> /F
  
  # macOS/Linux
  lsof -i :5000
  kill -9 <PID>
  ```

**Issue**: "ModuleNotFoundError"
- **Solution**: Ensure virtual environment is activated and requirements installed:
  ```bash
  pip install -r requirements.txt
  ```

### Performance Optimization
- **For faster generation**: Use GPU if available
- **For better quality**: Increase inference steps (slower)
- **For testing**: Use shorter prompts and fewer steps

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Ways to Contribute
- 🐛 **Report bugs** via GitHub Issues
- 💡 **Suggest features** through Discussions
- 📝 **Improve documentation** with pull requests
- 🔧 **Submit code improvements** via pull requests

### Contribution Guidelines
1. **Fork the repository**
2. **Create feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit changes**: `git commit -m 'Add amazing feature'`
4. **Push to branch**: `git push origin feature/amazing-feature`
5. **Open Pull Request**

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact Me

### Author Information
- **Name**: Abdelraouf
- **Project**: AI Text-to-Image Generator
- **Location**: Egypt

### Contact Methods
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Moataz899)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/moataz-abdelraouf/)
[![Email](https://img.shields.io/badge/Email-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](mailto:abdelraoufdahy%40gmail.com)
