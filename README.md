# Camera Driver Mismatch Workaround

This tool was created as a fix to a mismatch between hardware and outdated/wrong Windows 10 drivers. 

Specifically, recent Windows Updates caused a color space corruption (NV12/YUY2 mismatch) with ASUS integrated webcams on Windows 10, resulting in a solid green or severely discolored camera feed across all applications (like Discord, Zoom, and the Windows Camera app).

Because the Windows Media Foundation (WMF) pipeline is broken for this specific driver/hardware combination, this project acts as an ultra-low-latency "Micro-Bridge". It pulls the flawless raw video feed directly from the hardware using the older DirectShow API and pipes it into an invisible Virtual Camera.

### Requirements
- Python 3
- `pip install opencv-python pyvirtualcam numpy`

### How to Install
1. Open this folder.
2. Right-click **`register_virtual_camera.ps1`** and select **Run with PowerShell** (accept the Administrator prompt). This anchors the virtual camera driver to this folder.

### How to Use
1. Whenever you need your camera, simply double-click **`run_bridge.bat`**.
2. A small console window will appear showing that the bridge is active. Leave it open.
3. In Discord, Zoom, or your web browser, select **"Unity Video Capture"** as your webcam.
4. When you are done, close the console window. The script uses 0 CPU when closed.
