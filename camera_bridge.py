import cv2
import pyvirtualcam
import threading
import time

class CameraStream:
    def __init__(self, src=0, width=1280, height=720, fps=30):
        # We are going back to the reliable DirectShow backend.
        # MSMF is returning literal solid blocks of color because the Windows pipeline is entirely corrupted.
        self.cap = cv2.VideoCapture(src, cv2.CAP_DSHOW)
        
        self.cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.cap.set(cv2.CAP_PROP_FPS, fps)
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

        self.ret, self.frame = self.cap.read()
        self.running = True
        self.new_frame_event = threading.Event()
        
        self.thread = threading.Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()

    def update(self):
        while self.running:
            ret, frame = self.cap.read()
            if ret:
                # DirectShow gets the colors correct naturally, no math needed.
                self.frame = frame
                self.new_frame_event.set()

    def read_wait(self):
        self.new_frame_event.wait()
        self.new_frame_event.clear()
        return self.ret, self.frame

    def release(self):
        self.running = False
        self.thread.join(timeout=1.0)
        self.cap.release()

def main():
    print("Initializing Ultra-Fast 720p Bridge (DirectShow)...")
    
    stream = CameraStream(src=0, width=1280, height=720)
    time.sleep(1.0)
    
    ret, frame = stream.read_wait()
    if not ret or frame is None:
        print("Error: Could not grab frame.")
        time.sleep(3)
        stream.release()
        return

    height, width, _ = frame.shape
    fps = 30 

    print(f"Hardware locked at {width}x{height} (DirectShow)")
    print("Virtual Camera is LIVE. Keep this window open.")
    print("-" * 50)

    try:
        with pyvirtualcam.Camera(width=width, height=height, fps=fps, fmt=pyvirtualcam.PixelFormat.BGR, device="Unity Video Capture") as cam:
            while True:
                ret, frame = stream.read_wait()
                if not ret:
                    break
                
                cam.send(frame)

    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"\nError: {e}")
        time.sleep(5)
    finally:
        stream.release()

if __name__ == "__main__":
    main()
