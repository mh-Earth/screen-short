import socket
import cv2
import numpy as np
from PIL import Image
from datetime import datetime
HOST = '192.168.1.103'  # server IP address
PORT = 8888  # server port number

def receive_screenshot(sock):
    # Receive image size from server
    img_size = int(sock.recv(16).strip())
    # Receive image data from server
    img_data = b''
    while len(img_data) < img_size:
        chunk = sock.recv(img_size - len(img_data))
        if not chunk:
            raise Exception('Failed to receive image data')
        img_data += chunk
    # Decode JPEG image data to OpenCV image
    img_decoded = cv2.imdecode(np.frombuffer(img_data, dtype=np.uint8), cv2.IMREAD_COLOR)
    # Convert OpenCV image to PIL Image
    img_pil = Image.fromarray(cv2.cvtColor(img_decoded, cv2.COLOR_BGR2RGB))
    # Show PIL Image in a window
    # img_pil.show()
    # save the image
    img_pil.save(fp=datetime.now().strftime("%H%M%S%d%m%Y" + ".png"))


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # Receive and show screenshot from server
    receive_screenshot(s)



