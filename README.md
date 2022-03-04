# Streaming Raspberry Pi Camera Using GStreamer
GStreamer is a pipeline-based multimedia framework that links together a wide variety of media processing systems to complete complex workflows. For instance, GStreamer can be used to build a system that reads files in one format, processes them, and exports them in another. The formats and processes can be changed in a plug and play fashion.

GStreamer supports a wide variety of media-handling components, including simple audio playback, audio and video playback, recording, streaming and editing. The pipeline design serves as a base to create many types of multimedia applications such as video editors, transcoders, streaming media broadcasters and media players.

## Steps to Sending and Receiving Video Stream through WiFi

### Step 1: 
* Install GStreamer on Raspberry Pi: 
 [follow steps](https://github.com/FirdowsRahaman/Streaming-Raspberry-Pi-Camera-Using-GStreamer/blob/main/raspberry_pi/README.md)
* Install GStreamer and OpenCV on windows: 
 [follow steps](https://github.com/FirdowsRahaman/Streaming-Raspberry-Pi-Camera-Using-GStreamer/blob/main/windows/README.md)
   
    
### Step 2:
* Open raspberry-pi terminal and run `python3 flask_sender.py` 
* Open windows cmd and run `python flask_receiver.py` to receive video stream
    
   
### Step 3(optional):
* To save the video at receiving end run `python receiver_save_video.py` on windows cmd
   
