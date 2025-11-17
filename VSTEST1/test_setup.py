#!/usr/bin/env python3
"""
Test script to verify all packages are installed correctly
"""

def test_imports():
    """Test if all required packages can be imported"""
    print("Testing package imports...")
    
    try:
        import flask
        print("✓ Flask imported successfully")
    except ImportError as e:
        print(f"❌ Flask import failed: {e}")
        
    try:
        from flask_cors import CORS
        print("✓ Flask-CORS imported successfully")
    except ImportError as e:
        print(f"❌ Flask-CORS import failed: {e}")
        
    try:
        import pyaudio
        print("✓ PyAudio imported successfully")
    except ImportError as e:
        print(f"❌ PyAudio import failed: {e}")
        
    try:
        import vosk
        print("✓ VOSK imported successfully")
    except ImportError as e:
        print(f"❌ VOSK import failed: {e}")
        
    try:
        from textblob import TextBlob
        print("✓ TextBlob imported successfully")
    except ImportError as e:
        print(f"❌ TextBlob import failed: {e}")
        
    try:
        import speech_recognition as sr
        print("✓ SpeechRecognition imported successfully")
    except ImportError as e:
        print(f"❌ SpeechRecognition import failed: {e}")
        
    try:
        from werkzeug.utils import secure_filename
        print("✓ Werkzeug imported successfully")
    except ImportError as e:
        print(f"❌ Werkzeug import failed: {e}")

def test_basic_functionality():
    """Test basic functionality of key packages"""
    print("\nTesting basic functionality...")
    
    try:
        from textblob import TextBlob
        blob = TextBlob("Hello world")
        print(f"✓ TextBlob working: '{blob}' -> sentiment: {blob.sentiment}")
    except Exception as e:
        print(f"❌ TextBlob functionality test failed: {e}")
        
    try:
        import speech_recognition as sr
        r = sr.Recognizer()
        print("✓ SpeechRecognition recognizer created successfully")
    except Exception as e:
        print(f"❌ SpeechRecognition functionality test failed: {e}")
        
    try:
        import pyaudio
        p = pyaudio.PyAudio()
        device_count = p.get_device_count()
        print(f"✓ PyAudio working: Found {device_count} audio devices")
        p.terminate()
    except Exception as e:
        print(f"❌ PyAudio functionality test failed: {e}")

def check_directories():
    """Check if required directories exist"""
    import os
    print("\nChecking project directories...")
    
    required_dirs = [
        "alphabetimages",
        "mp4videos", 
        "indianalphabetsandnumbers",
        "templates",
        "static"
    ]
    
    for dir_name in required_dirs:
        if os.path.exists(dir_name):
            file_count = len(os.listdir(dir_name))
            print(f"✓ {dir_name}/ exists with {file_count} files")
        else:
            print(f"❌ {dir_name}/ directory not found")

if __name__ == "__main__":
    print("=== Package Installation Verification ===")
    test_imports()
    test_basic_functionality()
    check_directories()
    print("\n=== Verification Complete ===")