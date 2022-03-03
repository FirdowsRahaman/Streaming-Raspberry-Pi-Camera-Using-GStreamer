## Install GStreamer 1.18 on Windows OS

### Remove installed GStreamer versions
    sudo rm -rf /usr/bin/gst-*
    sudo rm -rf /usr/include/gstreamer-1.0
    
### Install a few dependencies
    sudo apt-get install cmake meson flex bison -y
    sudo apt-get install libglib2.0-dev libjpeg-dev libx264-dev -y 
    sudo apt-get install libgtk2.0-dev libcanberra-gtk* libgtk-3-dev libasound2-dev -y 
  
   
### Install the core GStreamer libraries
    cd ~
    mkdir firdows/build && cd firdows/build

    wget https://gstreamer.freedesktop.org/src/gstreamer/gstreamer-1.18.4.tar.xz
    sudo tar -xf gstreamer-1.18.4.tar.xz
    cd gstreamer-1.18.4
    mkdir build && cd build
    
    meson --prefix=/usr \
        --wrap-mode=nofallback \
        -D buildtype=release \
        -D gst_debug=false \
        -D package-origin=https://gstreamer.freedesktop.org/src/gstreamer/ \
        -D package-name="GStreamer 1.18.4 BLFS" ..
    
    sudo ninja -j4
    sudo ninja test
    sudo ninja install
    sudo ldconfig

### Install the GStreamer Plugins-base libraries
    cd ../..

    wget https://gstreamer.freedesktop.org/src/gst-plugins-base/gst-plugins-base-1.18.4.tar.xz
    sudo tar -xf gst-plugins-base-1.18.4.tar.xz
    cd gst-plugins-base-1.18.4
    mkdir build && cd build 
    
    meson --prefix=/usr \
        -D buildtype=release \
        -D package-origin=https://gstreamer.freedesktop.org/src/gstreamer/ ..
    
    sudo ninja -j4
    sudo ninja test
    sudo ninja install
    sudo ldconfig
    
 ### Install the GStreamer Plugins-good libraries
    cd ../..

    wget https://gstreamer.freedesktop.org/src/gst-plugins-good/gst-plugins-good-1.18.4.tar.xz
    sudo tar -xf gst-plugins-good-1.18.4.tar.xz
    cd gst-plugins-good-1.18.4
    mkdir build && cd build 
    
    meson --prefix=/usr       \
       -D buildtype=release \
       -D package-origin=https://gstreamer.freedesktop.org/src/gstreamer/ \
       -D package-name="GStreamer 1.18.4 BLFS" ..
    
    sudo ninja -j4
    sudo ninja test
    sudo ninja install
    sudo ldconfig
    
   
    
   ### Install the GStreamer Plugins-ugly libraries
    cd ../..

    wget https://gstreamer.freedesktop.org/src/gst-plugins-ugly/gst-plugins-ugly-1.18.4.tar.xz
    sudo tar -xf gst-plugins-ugly-1.18.4.tar.xz
    cd gst-plugins-ugly-1.18.4
    mkdir build && cd build 
    
    meson --prefix=/usr       \
      -D buildtype=release \
      -D package-origin=https://gstreamer.freedesktop.org/src/gstreamer/ \
      -D package-name="GStreamer 1.18.4 BLFS" ..
    
    sudo ninja -j4
    sudo ninja test
    sudo ninja install
    sudo ldconfig
    
    
    

### Install the GStreamer Plugins-bad libraries
    cd ../..

    wget https://gstreamer.freedesktop.org/src/gst-plugins-bad/gst-plugins-bad-1.18.4.tar.xz
    sudo tar -xf gst-plugins-bad-1.18.4.tar.xz
    cd gst-plugins-bad-1.18.4
    mkdir build && cd build 
    
    meson --prefix=/usr       \
       -D buildtype=release \
       -D package-origin=https://gstreamer.freedesktop.org/src/gstreamer/ \
       -D package-name="GStreamer 1.18.4 BLFS" ..
    
    sudo ninja -j4
    sudo ninja test
    sudo ninja install
    sudo ldconfig
 ### Test the installation
    gst-launch-1.0 videotestsrc ! videoconvert ! autovideosink
    
    gst-launch-1.0 v4l2src device=/dev/video0 ! video/x-raw, width=1280, height=720, framerate=30/1 ! videoconvert ! videoscale ! clockoverlay time-format="%D %H:%M:%S" ! video/x-raw, width=640, height=360 ! autovideosink
    
    
### Install the RTSP server plugin
    cd ../..

    wget https://gstreamer.freedesktop.org/src/gst-rtsp-server/gst-rtsp-server-1.18.4.tar.xz
    tar -xf gst-rtsp-server-1.18.4.tar.xz
    cd gst-rtsp-server-1.18.4
    mkdir build && cd build 
    
    meson --prefix=/usr       \
       --wrap-mode=nofallback \
       -D buildtype=release \
       -D package-origin=https://gstreamer.freedesktop.org/src/gstreamer/ \
       -D package-name="GStreamer 1.18.4 BLFS" ..
    
    sudo ninja -j4
    sudo ninja test
    sudo ninja install
    sudo ldconfig

### Testing rpicamsrc on  32-bit OS
    gst-inspect-1.0 rpicamsrc
    gst-launch-1.0 -v rpicamsrc preview=true ! fakesink
    
## Live Streaming

### UDP Streaming
#### Start the sender, the one with the Raspicam
    gst-launch-1.0 -v v4l2src device=/dev/video0 num-buffers=-1 ! video/x-raw, width=640, height=480, framerate=30/1 ! videoconvert ! jpegenc ! rtpjpegpay ! udpsink host=192.168.0.121 port=5200

#### Start the reciever, the one with IP 192.168.0.121
    gst-launch-1.0 -v udpsrc port=5200 ! application/x-rtp, media=video, clock-rate=90000, payload=96 ! rtpjpegdepay ! jpegdec ! videoconvert ! autovideosink
    
    
### TCP Streaming
#### Start the sender, the one with the Raspicam and IP 192.168.0.151
    gst-launch-1.0 -v v4l2src device=/dev/video0 num-buffers=-1 ! video/x-raw,width=640,height=480, framerate=30/1 ! videoconvert ! jpegenc ! tcpserversink  host=192.168.0.151 port=5000

#### Start the reciever and connect to the server with IP 192.168.0.151
    gst-launch-1.0 tcpclientsrc host=192.168.0.151 port=5000 ! jpegdec ! videoconvert ! autovideosink


### RTSP Streaming
#### Start the sender, the one with the Raspicam 
    cd ~/gst-rtsp-server-1.18.4/build/examples
    ./test-launch "v4l2src device=/dev/video0 ! video/x-h264, width=640, height=480, framerate=30/1 ! h264parse config-interval=1 ! rtph264pay name=pay0 pt=96"
#### Start the reciever and connect to the server with IP 192.168.0.151
    gst-launch-1.0 rtspsrc location=rtsp://192.168.0.151:8554/test/ latency=10 ! decodebin ! autovideosink
