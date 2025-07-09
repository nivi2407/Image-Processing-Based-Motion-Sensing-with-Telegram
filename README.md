# Image Processing-Based Motion Sensing with Telegram

Image Processing-Based Motion Sensing with Telegram is an intelligent surveillance system built using Python, OpenCV, and deep learning. It leverages real-time video processing and object detection to identify motion from humans, cats, and dogs, and sends automated alerts (images or videos) directly to a Telegram chat via a bot interface. This project is ideal for security, home automation, or pet monitoring applications, offering an interactive and responsive way to track activity through a simple yet powerful communication channel.

## Features:

- **🎥 Motion Detection:** Utilizes a reliable background updating model and threshold methods to detect complete moving objects, including humans, cats, and dogs.

- **📲 Telegram Bot Integration:** Sends notifications to an admin via a Telegram chat bot when movements are detected. Enables real-time communication by retrieving images and videos.
  
- **📸 On-Demand Image Capture**
Responds to /image command to capture and send the current camera frame.

- **🎞️ On-Demand Video Recording**
Responds to /video command to record and send a short video from the live feed.

- **💬 Smart Interaction**
Responds to greetings and provides a help menu via /help or similar commands.

## Setup instructions:

**Clone the repository**
   ```bash
   git clone https://github.com/nivi2407/Image-Processing-Based-Motion-Sensing-with-Telegram.git
   cd Image-Processing-Based-Motion-Sensing-with-Telegram
```
## Install dependencies:
```bash
pip install opencv-python imutils numpy telepot
```

## Setup your Telegram bot
⁍ Talk to BotFather on Telegram <br>
⁍ Create a bot and get the API token <br>
⁍ Get your chat ID using any Telegram user ID bot

## Update main.py:
▹Replace #Enter token id with your bot token <br>
▹Replace #Enter chat id with your actual chat ID

## Run the project

```bash
python main.py
```

## Commands to use:
/image – Captures current frame from webcam <br>
/video – Records a 10-second video and sends it <br>
/help – Shows command list


## Motion Detection Examples

Cat Motion Detection | Dog Motion Detection
<div>
  <img src="https://github.com/nivi2407/IMAGE-PROCESSING-BASED-MOTION-SENSING-WITH-TELEGRAM/assets/79712578/8cde14a5-5d36-4e1b-8d9b-f4cbc0043a29" alt="Cat Motion" width="350" height="450" style="margin-right: 20px;">
  <img src="https://github.com/nivi2407/IMAGE-PROCESSING-BASED-MOTION-SENSING-WITH-TELEGRAM/assets/79712578/514288d3-f9d1-44ab-887b-fb11008530d0" alt="Dog Motion" width="350" height="450">
</div>

Human Motion Detection
<div>
  <img src="https://github.com/nivi2407/IMAGE-PROCESSING-BASED-MOTION-SENSING-WITH-TELEGRAM/assets/79712578/9dcdd30d-867a-44e6-8d60-5713e9be4462" alt="Real-time Motion Detection" width="350" height="450" style="margin-right: 20px;">
  <img src="https://github.com/nivi2407/IMAGE-PROCESSING-BASED-MOTION-SENSING-WITH-TELEGRAM/assets/79712578/2c08536e-0e7b-48c2-8647-8d3ffd3bdbd3" alt="Real-time Motion Detection" width="350" height="450">
</div>

## Technologies Used

| Area                   | Technology                 |
|------------------------|----------------------------|
| Programming Language   | Python                     |
| Computer Vision        | OpenCV, imutils            |
| Deep Learning Model    | MobileNet SSD (Caffe)      |
| Bot Integration        | Telegram + telepot         |
| Utilities              | NumPy, time, datetime      |

