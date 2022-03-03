import cv2
import requests
from threading import Thread

HOST_IP = "192.168.0.138" 


def display_video():
    while True:
        RaspiStreamCam = cv2.VideoCapture(f"rtspsrc location=rtsp://{HOST_IP}:8554/test latency=0 buffer-mode=auto ! decodebin ! videoconvert ! appsink", cv2.CAP_GSTREAMER)
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

    
def api_request():
    try:
       end_response = requests.get(f"http://{HOST_IP}:5000/end_process")
       hd_response = requests.get(f"http://{HOST_IP}:5000/hd_streaming")
    except:
        print("HD Server is not Connected!")
                

if __name__ == '__main__':
    t1 = Thread(target=api_request)
    t2 = Thread(target=display_video)

    t1.start()
    t2.start()

#   t1.join()
#   t2.join()