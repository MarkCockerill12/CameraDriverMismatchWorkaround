# Camera Driver Mismatch Workaround

This tool was created as a fix to a mismatch between hardware and Windows 10 drivers. I """downgraded""" my Asus Zenbook 14 to Windows 10, when it was made with windows 11 in mind.

Specifically, some Windows 10 drivers caused a colour space corruption (NV12/YUY2 mismatch) with my ASUS integrated webcam, resulting in a solid green camera feed across all applications (like Discord, Zoom, and the Windows Camera app).

Because the Windows Media Foundation (WMF) pipeline is broken for this specific driver/hardware combination, this project acts as an ultra-low-latency "Micro-Bridge". It pulls the flawless raw video feed directly from the hardware using the older DirectShow API and pipes it into an invisible Virtual Camera. It works at 30fps 720p, which is the max the built in USB camera connection can handle, without windows own compression drivers.

### Requirements
- Python 3
- `pip install opencv-python pyvirtualcam numpy`

### How to Install
Run the **`register_virtual_camera.ps1`** as an admin. This anchors the virtual camera driver to this folder.

### How to Use
1. Whenever you need your camera, simply double-click **`run_bridge.bat`**.
2. A small console window will appear showing that the bridge is active. Leave it open.
3. In Discord, Zoom, or your web browser, select **"Unity Video Capture"** as your webcam.
4. When you are done, close the console window.
