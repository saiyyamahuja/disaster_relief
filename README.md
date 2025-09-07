# Disaster Relief Emergency Assistant

A voice-activated chatbot that provides step-by-step guidance for various natural disasters and emergency situations. The assistant uses speech recognition to understand user input and provides audio responses with disaster relief instructions.

## Features

- **Voice Recognition**: Listen to voice commands and respond with audio guidance
- **Comprehensive Disaster Coverage**: Support for multiple disaster scenarios including:
  - Natural Disasters: Earthquakes, Floods, Hurricanes, Wildfires, Tornadoes, Tsunamis, Blizzards, Droughts, Heatwaves
  - Infrastructure Failures: Power Outages, Gas Leaks
  - Emergency Response: Evacuation procedures
- **Critical vs Non-Critical Classification**: Different urgency levels for appropriate response
- **Step-by-Step Instructions**: Detailed guidance for each disaster scenario
- **Emergency Service Integration**: Directs users to call 911 for life-threatening situations

## Requirements

- Python 3.12+
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd disaster_relief
```

2. Create and activate a virtual environment:
```bash
python -m venv disaster_relief_env
source disaster_relief_env/bin/activate  # On Windows: disaster_relief_env\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Download the spaCy English model:
```bash
python -m spacy download en_core_web_sm
```

## Usage

1. Activate the virtual environment:
```bash
source disaster_relief_env/bin/activate
```

2. Run the disaster relief assistant:
```bash
python disaster_relief_chatbot.py
```

3. Speak your emergency situation clearly. Examples:
   - "I'm experiencing an earthquake"
   - "There's a flood in my area"
   - "Wildfire approaching my home"
   - "Power outage in my neighborhood"
   - "I need evacuation guidance"

4. Follow the step-by-step instructions provided by the assistant.

## Voice Commands

- **Emergency Descriptions**: Describe the disaster or emergency situation
- **Navigation**: Say "next" to continue through instructions, "stop" to exit
- **Exit**: Say "exit", "quit", "goodbye", or "bye" to close the application

## Safety Notice

⚠️ **IMPORTANT**: This assistant provides general guidance and should not replace professional emergency services. For life-threatening emergencies, always call 911 immediately.

## Dependencies

- `spacy`: Natural language processing
- `speechrecognition`: Voice recognition
- `gtts`: Google Text-to-Speech
- `pygame`: Audio playback
- `pyaudio`: Microphone access

## Project Structure

```
disaster_relief/
├── disaster_relief_chatbot.py    # Main application
├── disaster_data.json            # Disaster scenarios and instructions
├── requirements.txt              # Python dependencies
├── README.md                     # This file
└── disaster_relief_env/          # Virtual environment (not tracked)
```

## Contributing

Feel free to add more disaster scenarios or improve the existing instructions by editing the `disaster_data.json` file.

## License

This project is open source and available under the MIT License.
