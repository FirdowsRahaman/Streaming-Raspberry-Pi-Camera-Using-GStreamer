## Install GStreamer 1.18 on Windows

### Download GStreamer and OpenCV
* Install both gstreamer-runtime and gstreamer-development package: https://gstreamer.freedesktop.org/download/ 
* Download OpenCV release sources (.zip file) and extract: https://github.com/opencv/opencv/archive/4.1.0.zip


### Set Path Variable
* Add gstreamer to Path variable\
\
![alt text](https://github.com/FirdowsRahaman/Streaming-Raspberry-Pi-Camera-Using-GStreamer/blob/main/images/edit_env_variable.PNG)

* Add system variable “GSTREAMER_DIR” “C:\gstreamer\1.0\x86_64” \
\
![alt text](https://github.com/FirdowsRahaman/Streaming-Raspberry-Pi-Camera-Using-GStreamer/blob/main/images/edit_system_variable.PNG)

   
### Download CMAKE & Visual Studio
*  Install CMAKE: https://cmake.org/download/ 
*  Install Visual Studio: https://visualstudio.microsoft.com/downloads/
*  Open CMAKE, Select OpenCV source and build folder \
\
![alt text](https://github.com/FirdowsRahaman/Streaming-Raspberry-Pi-Camera-Using-GStreamer/blob/main/images/cmake1.PNG)

* Hit Configure, select your Visual Studio version then click Finish \
\
![alt text](https://github.com/FirdowsRahaman/Streaming-Raspberry-Pi-Camera-Using-GStreamer/blob/main/images/cmake2.PNG)

* Click Configure again, The red value will change to white
* Click Generate
* Click “Open Project” in Visual Studio: Switch from DEBUG to RELEASE and x64 \
\
![alt text](https://miro.medium.com/max/928/1*i0MWwkVK4sM4n48phaHEuw.png)

* Right click on INSTALL and select Build \
\
![alt text](https://miro.medium.com/max/554/1*_Y7n7o_z5af1gUuQ-OHhig.png)

* Finally, add bin & lib folder to PATH, located in C:\opencv-4.1.0\build\install\x64\vc16 \
\
![alt text](https://github.com/FirdowsRahaman/Streaming-Raspberry-Pi-Camera-Using-GStreamer/blob/main/images/opencv_path.PNG) \
\
![alt text](https://github.com/FirdowsRahaman/Streaming-Raspberry-Pi-Camera-Using-GStreamer/blob/main/images/opencv_env_path.PNG)
   

### Test the Installation
    import cv2
    print(cv2.__file__)
    print(cv2.getBuildInformation())
