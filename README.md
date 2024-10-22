# System Resource and Internet Speed Monitor

This Python program provides an interface to monitor your system's resource usage and test your internet speed. It displays real-time information about the number of CPUs, CPU usage (in percent), RAM usage, and available RAM. Additionally, you can test the internet speed, which will show the download speed, upload speed, and ping time.

## Features

- **System Monitoring:**
  - Number of CPUs
  - CPU usage (percentage)
  - Total amount of RAM
  - RAM usage (percentage)
  - Available RAM
  - 
- **Internet Speed Test:**
  - Download speed
  - Upload speed
  - Ping time

## Requirements

The following Python libraries need to be installed:

```bash
pip install psutil
pip install speedtest-cli
pip install pillow
```

### How to Run the Program

1. Clone the repository:
   
   ``bash
    git clone https://github.com/BiaJohnson/Computer-Performance
    cd Computer-Performance
  ``
  
2. Navigate to the project directory:
   
   `bash
    cd your-repo-name
   `

3. Install the libraries mentioned under Requirements:

4. Run the program:
   
   `bash
    python cpustatus.py
   `
