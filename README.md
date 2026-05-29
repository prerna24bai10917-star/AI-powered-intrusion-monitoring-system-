# AI-powered-intrusion-monitoring-system-
The AI-Based Border Intrusion Detection and Restricted Zone Monitoring System is a computer vision project developed to improve surveillance and security in sensitive areas. The system uses artificial intelligence to detect people in surveillance images and determine whether they have entered a restricted zone.
# AI-Based Border Intrusion Detection and Restricted Zone Monitoring System

## Overview

This project uses Artificial Intelligence and Computer Vision to detect unauthorized human entry into restricted border zones.
A YOLOv8 object detection model identifies people in surveillance images. The system then checks whether the detected individual has crossed a predefined virtual border line.
If a person enters the restricted zone, an intrusion alert is generated.

## Features

- Human Detection using YOLOv8
- Restricted Border Zone Monitoring
- Intrusion Detection
- Alert Generation
- Evidence Capture
- Confidence Score Display

## Technologies Used

- Python
- OpenCV
- YOLOv8
- NumPy

## System Workflow

1. Input Surveillance Image
2. Human Detection using AI
3. Virtual Border Creation
4. Zone Crossing Analysis
5. Intrusion Alert Generation
6. Output Visualization

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python intrusion_detection.py
```

## Future Scope

- Drone Surveillance Integration
- Thermal Camera Support
- Real-Time Video Monitoring
- Face Recognition
- Weapon Detection
- Automated Security Alerts
