## Install GStreamer 1.18 on Windows

### Download GStreamer and OpenCV
* Install both gstreamer-runtime and gstreamer-development package: https://gstreamer.freedesktop.org/download/ 
* Download OpenCV release sources (.zip file) and extract: https://github.com/opencv/opencv/archive/4.1.0.zip


### Set Path Variable
* Add gstreamer to Path variable\
\
![alt text](https://miro.medium.com/max/970/1*iWn1XktT9U5UT2NqzFuGdA.png)

* Add system variable “GSTREAMER_DIR” “C:\gstreamer\1.0\x86_64” \
\
![alt text](https://miro.medium.com/max/1308/1*2nOzcr19lNxtYFCZn01_QA.png)

* Click Configure again, The red value will change to white
* Click Generate
* Click “Open Project” in Visual Studio: Switch from DEBUG to RELEASE and x64 \
\
![alt text](https://miro.medium.com/max/928/1*i0MWwkVK4sM4n48phaHEuw.png)

* Right click on INSTALL and select Build \
\
![alt text](https://miro.medium.com/max/554/1*_Y7n7o_z5af1gUuQ-OHhig.png)
   
### Download CMAKE & Visual Studio
*  Install CMAKE: https://cmake.org/download/ 
*  Install Visual Studio: https://visualstudio.microsoft.com/downloads/
*  Open CMAKE, Select OpenCV source and build folder \
\
![alt text](https://miro.medium.com/max/696/1*_KyykDayHWfsfhUk609Vkw.png)

* Hit Configure, select your Visual Studio version then click Finish \
\
![alt text](https://miro.medium.com/max/1004/1*uSKSIS1IAr87rjBWMn4YNA.png)

* Finally, add bin & lib folder to PATH, located in C:\opencv-4.1.0\build\install\x64\vc16 \
\
![alt text](https://miro.medium.com/max/1400/1*UbncaWkwTPo-Dw0G_6_76Q.png) \
\
![alt text](https://miro.medium.com/max/946/1*EeGo_77M5MLD8OWKT1fedw.png)
   

### Test the Installation
    import cv2
    print(cv2.__file__)
    print(cv2.getBuildInformation())
