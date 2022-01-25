# Streaming Raspberry Pi Camera Using GStreamer
GStreamer is a pipeline-based multimedia framework that links together a wide variety of media processing systems to complete complex workflows. For instance, GStreamer can be used to build a system that reads files in one format, processes them, and exports them in another. The formats and processes can be changed in a plug and play fashion.

GStreamer supports a wide variety of media-handling components, including simple audio playback, audio and video playback, recording, streaming and editing. The pipeline design serves as a base to create many types of multimedia applications such as video editors, transcoders, streaming media broadcasters and media players.

There are a few additional plugins you must install before you can stream live video.

### install a missing dependency
    sudo apt-get install libx264-dev libjpeg-dev
### install the remaining plugins
     sudo apt-get install libgstreamer1.0-dev \
     libgstreamer-plugins-base1.0-dev \
     libgstreamer-plugins-bad1.0-dev \
     gstreamer1.0-plugins-ugly \
     gstreamer1.0-tools \
     gstreamer1.0-gl \
     gstreamer1.0-gtk3
### if you have Qt5 install this plugin
    sudo apt-get install gstreamer1.0-qt5
### install if you want to work with audio
    sudo apt-get install gstreamer1.0-pulseaudio
    
## Streaming.
With all GStreamer modules installed let's test the installation $ gst-launch-1.0 videotestsrc ! videoconvert ! autovideosink .

### Test your installation. In order to do this run this command on your Pi:
    raspivid -t 0 -w 640 -h 480 -fps 24 -b 2000000 -awb tungsten  -o - | gst-launch-1.0 -v fdsrc ! h264parse ! rtph264pay config-interval=1 pt=96 ! gdppay ! tcpserversink host=0.0.0.0 port=5000
host = get the IP address of the sending Raspberry Pi


## UDP streaming.
There are many types of streaming possible with GStreamer. UDP and TCP are most used to connect two devices. The name of the streaming refers to the Ethernet protocol used.
Let's start with UDP. We use two Raspberry Pis, both connected to the same home network. However, it could just as easily be an RPi and a laptop on the other side of the world. You need to know the address of the receiving Raspberry Pi on forehand. Follow the commands below.

#### get the IP address of the recieving RPi first
    hostname -I
#### start the sender, the one with the Raspicam
$ gst-launch-1.0 -v v4l2src device=/dev/video0 num-buffers=-1 ! video/x-raw, width=640, height=480, framerate=30/1 ! videoconvert ! jpegenc ! rtpjpegpay ! udpsink host=192.168.178.84 port=5200
# start the reciever, the one with IP 192.168.178.84
$ gst-launch-1.0 -v udpsrc port=5200 ! application/x-rtp, media=video, clock-rate=90000, payload=96 ! rtpjpegdepay ! jpegdec ! videoconvert ! autovideosink
    
   
