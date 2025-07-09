# Image Processing-Based Motion Sensing with Telegram
> Real-time object detection and motion alerts via Telegram

Image Processing-Based Motion Sensing with Telegram is an intelligent surveillance system built using Python, OpenCV, and deep learning. It leverages real-time video processing and object detection to identify motion from humans, cats, and dogs, and sends automated alerts (images or videos) directly to a Telegram chat via a bot interface. This project is ideal for security, home automation, or pet monitoring applications, offering an interactive and responsive way to track activity through a simple yet powerful communication channel.

## 🚀 How It Works

- 📷 **Capture**: Continuously captures video frames.
- 🔍 **Detect**: Compares consecutive frames to detect motion.
- 📡 **Notify**: If motion is detected:
  - Takes a snapshot.
  - Sends a Telegram alert with the image.

## ✨ Key Features:

- ⏱️ Real-time motion detection
- 🧠 Frame differencing using OpenCV
- 🤖 Telegram bot integration for instant alerts
- 📸 Captures and sends a snapshot when motion is detected
- 💻 Lightweight – runs on Raspberry Pi or PC
  
## ⚙️ Setup instructions:

### Clone the repository
   ```bash
   git clone https://github.com/nivi2407/Image-Processing-Based-Motion-Sensing-with-Telegram.git
   cd Image-Processing-Based-Motion-Sensing-with-Telegram
```
### Install dependencies:
```bash
pip install opencv-python imutils numpy telepot
```

### 🤖 Telegram Bot Setup

1. Go to [@BotFather](https://t.me/BotFather) on Telegram.
2. Type `/newbot` and follow the prompts.
3. Copy the **Bot Token** given by BotFather.
4. Get your **Chat ID** via [@userinfobot](https://t.me/userinfobot).

```python
BOT_TOKEN = 'your-telegram-bot-token'
CHAT_ID = 'your-chat-id'
```

### Commands to use:
| Command  | Description                       |
|----------|-----------------------------------|
| `/image` | Captures and sends a frame        |
| `/video` | Sends a 10-second video clip      |
| `/help`  | Lists available commands          |

## Snapshots:

| Cat Detection | Dog Detection |
|---------------|---------------|
| ![Cat](https://github.com/nivi2407/IMAGE-PROCESSING-BASED-MOTION-SENSING-WITH-TELEGRAM/assets/79712578/8cde14a5-5d36-4e1b-8d9b-f4cbc0043a29) | ![Dog](https://github.com/nivi2407/IMAGE-PROCESSING-BASED-MOTION-SENSING-WITH-TELEGRAM/assets/79712578/514288d3-f9d1-44ab-887b-fb11008530d0) |

| Image Retrieval | Video Retreival |
|------------------|------------------|
| ![imageretreival](https://github.com/nivi2407/IMAGE-PROCESSING-BASED-MOTION-SENSING-WITH-TELEGRAM/assets/79712578/9dcdd30d-867a-44e6-8d60-5713e9be4462) | ![Videoretreival](https://github.com/nivi2407/IMAGE-PROCESSING-BASED-MOTION-SENSING-WITH-TELEGRAM/assets/79712578/2c08536e-0e7b-48c2-8647-8d3ffd3bdbd3) |

## 🧰 Technologies Used

| Area                   | Technology                 |
|------------------------|----------------------------|
| Programming Language   | Python                     |
| Computer Vision        | OpenCV, imutils            |
| Deep Learning Model    | MobileNet SSD (Caffe)      |
| Bot Integration        | Telegram + telepot         |
| Utilities              | NumPy, time, datetime      |

