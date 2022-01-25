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
    
### Test your installation. In order to do this run this command on your Pi:
`raspivid -t 0 -w 640 -h 480 -fps 24 -b 2000000 -awb tungsten  -o - | gst-launch-1.0 -v fdsrc ! h264parse ! rtph264pay config-interval=1 pt=96 ! gdppay ! tcpserversink host=0.0.0.0 port=5000`

host = get the IP address of the sending Raspberry Pi

### And this command on your Mac:
`/Library/Frameworks/GStreamer.framework/Commands/gst-launch-1.0 -v tcpclientsrc host=<your_Pi's_IP> port=5000 ! gdpdepay ! rtph264depay ! avdec_h264 ! videoconvert  ! osxvideosink sync=false`

### or this on your Linux box:
`gst-launch-1.0 -v tcpclientsrc host=<your_Pi's_IP> port=5000 ! gdpdepay ! rtph264depay ! avdec_h264 ! videoconvert  ! autovideosink sync=false`

You should see a video. This is already H.264, but not RTSP.

    
## Live Streaming
With all GStreamer modules installed let's test the installation `$ gst-launch-1.0 videotestsrc ! videoconvert ! autovideosink`

The Raspicam can be invoked with this rather large pipeline `$ gst-launch-1.0 v4l2src device=/dev/video0 ! video/x-raw, width=1280, height=720, framerate=30/1 ! videoconvert ! videoscale ! clockoverlay time-format="%D %H:%M:%S" ! video/x-raw, width=640, height=360 ! autovideosink` Remember to enable the Raspicam on forehand in your Raspberry Pi configuration menu.

All pipeline commands are constructed in the same way. First, the source is named, followed by several operations, after which the sink is determined. All parts of the pipeline are separated from each other by exclamation marks. For instance, in the example above, you could remove the part, which prints the date and time on the screen.  
The limited computing power of the Raspberry Pi does not allow for overly complex pipelines.




### 1. Streaming Using UDP Protocol
There are many types of streaming possible with GStreamer. UDP and TCP are most used to connect two devices. The name of the streaming refers to the Ethernet protocol used.
Let's start with UDP. We use two Raspberry Pis, both connected to the same home network. However, it could just as easily be an RPi and a laptop on the other side of the world. You need to know the address of the receiving Raspberry Pi on forehand. Follow the commands below.

#### get the IP address of the recieving RPi first
    hostname -I
#### start the sender, the one with the Raspicam
`gst-launch-1.0 -v v4l2src device=/dev/video0 num-buffers=-1 ! video/x-raw, width=640, height=480, framerate=30/1 ! videoconvert ! jpegenc ! rtpjpegpay ! udpsink host=192.168.178.84 port=5200`
#### start the reciever, the one with IP 192.168.178.84
`gst-launch-1.0 -v udpsrc port=5200 ! application/x-rtp, media=video, clock-rate=90000, payload=96 ! rtpjpegdepay ! jpegdec ! videoconvert ! autovideosink`
    
TCP streaming.
The other method of streaming is with TCP. The difference with UDP is the latency. UDP is faster.
The commands as listed below. Note the different IP addresses. With TCP streaming, you use the server address, the sender, instead of the receiver, as we saw with the UDP streaming.


Raspberry Pi 32 or 64-bit OS
# get the IP address of the sending RPi first
$ hostname -I
# start the sender, the one with the Raspicam and IP 192.168.178.32
$ gst-launch-1.0 -v v4l2src device=/dev/video0 num-buffers=-1 ! video/x-raw,width=640,height=480, framerate=30/1 ! videoconvert ! jpegenc ! tcpserversink  host=192.168.178.32 port=5000
# start the reciever and connect to the server with IP 192.168.178.32
$ gst-launch-1.0 tcpclientsrc host=192.168.178.32 port=5000 ! jpegdec ! videoconvert ! autovideosink
Both streams, UDP and TCP, start with single frames (video/x-raw). A timestamp is inserted if necessary. Then the image is compressed with jpeg to reduce its size, decreasing the required bandwidth. Once received, the jpeg image will be decompressed and displayed on the screen. You can always change the resolution. Frame sizes of 1280x960 at 30 FPS were no problem here at the office.
RTSP streaming.
If you want to stream RTSP (Real-Time Streaming Protocol), you need a server. GStreamer has its own server available for RTSP. If you don't want to stream RTSP, this additional software isn't necessary. The streaming examples section provides some pipelines and other information about setting up an RTSP stream. For now, just the installation commands.

# install the rtsp server version 1.14.4
$ wget https://gstreamer.freedesktop.org/src/gst-rtsp-server/gst-rtsp-server-1.14.4.tar.xz
$ tar -xf gst-rtsp-server-1.14.4.tar.xz
$ cd gst-rtsp-server-1.14.4
$ ./configure
$ make
$ sudo make install
$ sudo ldconfig
