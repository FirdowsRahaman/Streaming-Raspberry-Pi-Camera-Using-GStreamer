# Streaming Raspberry Pi Camera Using GStreamer
GStreamer is a pipeline-based multimedia framework that links together a wide variety of media processing systems to complete complex workflows. For instance, GStreamer can be used to build a system that reads files in one format, processes them, and exports them in another. The formats and processes can be changed in a plug and play fashion.

GStreamer supports a wide variety of media-handling components, including simple audio playback, audio and video playback, recording, streaming and editing. The pipeline design serves as a base to create many types of multimedia applications such as video editors, transcoders, streaming media broadcasters and media players.

## Steps to Sending and Receiving Video Stream through WiFi

### Step 1 (Installation): 
* Install GStreamer on Raspberry Pi: 
 [follow steps](https://github.com/FirdowsRahaman/Streaming-Raspberry-Pi-Camera-Using-GStreamer/blob/main/raspberry_pi/README.md)
* Install GStreamer and OpenCV on windows: 
 [follow steps](https://github.com/FirdowsRahaman/Streaming-Raspberry-Pi-Camera-Using-GStreamer/blob/main/windows/README.md)
   

### Step 2 (Live Streaming):

#### >> UDP Streaming
##### Start the sender, the one with the Raspicam
    gst-launch-1.0 -v v4l2src device=/dev/video0 num-buffers=-1 ! video/x-raw, width=640, height=480, framerate=30/1 ! videoconvert ! jpegenc ! rtpjpegpay ! udpsink host=192.168.0.121 port=5200

#### Start the reciever, the one with IP 192.168.0.121
    gst-launch-1.0 -v udpsrc port=5200 ! application/x-rtp, media=video, clock-rate=90000, payload=96 ! rtpjpegdepay ! jpegdec ! videoconvert ! autovideosink
    
    
#### >> TCP Streaming
#### Start the sender, the one with the Raspicam and IP 192.168.0.151
    gst-launch-1.0 -v v4l2src device=/dev/video0 num-buffers=-1 ! video/x-raw,width=640,height=480, framerate=30/1 ! videoconvert ! jpegenc ! tcpserversink  host=192.168.0.151 port=5000

#### Start the reciever and connect to the server with IP 192.168.0.151
    gst-launch-1.0 tcpclientsrc host=192.168.0.151 port=5000 ! jpegdec ! videoconvert ! autovideosink


#### >> RTSP Streaming
#### Start the sender, the one with the Raspicam 
    cd ~/gst-rtsp-server-1.18.4/build/examples
    ./test-launch "v4l2src device=/dev/video0 ! video/x-h264, width=640, height=480, framerate=30/1 ! h264parse config-interval=1 ! rtph264pay name=pay0 pt=96"
#### Start the reciever and connect to the server with IP 192.168.0.151
    gst-launch-1.0 rtspsrc location=rtsp://192.168.0.151:8554/test/ latency=10 ! decodebin ! autovideosink


### Step 3:
* Open raspberry-pi terminal and run `python3 flask_sender.py` 
* Open windows cmd and run `python flask_receiver.py` to receive video stream
    
   
### Step 4 (optional):
* To save the video at receiving end run `python receiver_save_video.py` on windows cmd
   
