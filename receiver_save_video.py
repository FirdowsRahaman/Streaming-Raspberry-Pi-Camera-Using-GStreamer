import cv2
import time
import requests
from threading import Thread

HOST_IP = "192.168.0.138" 
CAPTURE_DURATION = 120


def display_video():
    while True:
        RaspiStreamCam = cv2.VideoCapture(f"rtspsrc location=rtsp://{HOST_IP}:8554/test latency=0 buffer-mode=auto ! decodebin ! videoconvert ! appsink", cv2.CAP_GSTREAMER)
        streaming_status = RaspiStreamCam.isOpened()
        print(streaming_status)

        if streaming_status == True:
            print ('Live Streaming is ready...')

            width  = int(RaspiStreamCam.get(3))  
            height = int(RaspiStreamCam.get(4))  
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            video_name = f'output_{time.time()}.avi'
            video_writer = cv2.VideoWriter(video_name, fourcc, 24, (1280, 720))

            start_time = time.time()
            while True:
                ret, frameRaspiIP = RaspiStreamCam.read()
                if not ret:
                    print("Can't receive frame (stream end?). Exiting ...")
                    break

                video_writer.write(frameRaspiIP)
                if abs(time.time() - start_time) > CAPTURE_DURATION:
                    video_writer.release()
                    video_name = f'output_{time.time()}.avi'
                    video_writer = cv2.VideoWriter(video_name, fourcc, 24, (1280, 720))
                    start_time   = time.time()
                # frameRaspiIP = cv2.flip(frameRaspiIP, 0)
                cv2.imshow('RaspiStreamCam',frameRaspiIP)

                if cv2.waitKey(1)==ord('q'):
                    break

            RaspiStreamCam.release()
            video_writer.release()
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