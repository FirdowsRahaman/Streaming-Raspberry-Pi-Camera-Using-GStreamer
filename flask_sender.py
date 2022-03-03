import os
import gpiozero as gz
from flask import Flask

app = Flask(__name__)


@app.route('/hd_streaming')
def camera_hd_feed():
    # Live HD Video Stream using RTSP Protocol
    os.system("pkill -f 'test-launch'")
    os.chdir("/home/pi/firdows/build/gst-rtsp-server-1.18.4/build/examples")
    # os.system('./test-launch "v4l2src device=/dev/video0 ! video/x-h264, width=1280, height=720, framerate=30/1 ! h264parse config-interval=1 ! rtph264pay name=pay0 pt=96"')
    os.system("./test-launch '(rpicamsrc keyframe-interval=1 bitrate=2000000, preview=false ! video/x-h264, width=1280, height=720, framerate=25/1 ! h264parse ! rtph264pay name=pay0 pt=96 )'")
    

@app.route('/fullhd_streaming')
def camera_fullhd_feed():
    # Live FullHD Video Stream using RTSP Protocol
    os.system("pkill -f 'test-launch'")
    os.chdir("/home/pi/firdows/build/gst-rtsp-server-1.18.4/build/examples")
    # os.system('./test-launch "v4l2src device=/dev/video0 ! video/x-h264, width=1920, height=1080, framerate=30/1 ! h264parse config-interval=1 ! rtph264pay name=pay0 pt=96"')
    os.system("./test-launch '(rpicamsrc keyframe-interval=1, preview=false ! video/x-h264, width=1920, height=1080, framerate=25/1 ! h264parse ! rtph264pay name=pay0 pt=96 )'")
    

@app.route('/camera_temp')
def camera_temp():
    # Get the camera temp
    cpu_temp = gz.CPUTemperature().temperature
    cpu_temp = round(cpu_temp, 1)
    return f"{cpu_temp}"


@app.route('/end_process')
def end_process():
    # End Video Streaming
    # os.system("ps -aux | grep test-launch")
    # user_input = input("press any key to exit ")
    # if user_input:
    os.system("pkill -f 'test-launch'")
    return "End Process."


if __name__ == "__main__":
    app.run(host='0.0.0.0')


