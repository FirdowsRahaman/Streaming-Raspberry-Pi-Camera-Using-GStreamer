import cv2


while True:
    RaspiStreamCam = cv2.VideoCapture("rtspsrc location=rtsp://192.168.0.138:8554/test latency=0 buffer-mode=auto ! decodebin ! videoconvert ! appsink", cv2.CAP_GSTREAMER)
    streaming_status = RaspiStreamCam.isOpened()

    if streaming_status == True:
        print ('Live Streaming is ready...')
        while True:
            ret, frameRaspiIP = RaspiStreamCam.read()
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            # frameRaspiIP = cv2.flip(frameRaspiIP, 0)
            cv2.imshow('RaspiStreamCam',frameRaspiIP)

            if cv2.waitKey(1)==ord('q'):
                break

        RaspiStreamCam.release()
        cv2.destroyAllWindows()

    if streaming_status == False:
        print("Streaming Stopped!")
