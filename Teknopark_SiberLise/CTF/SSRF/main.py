import subprocess
import time
import os
import sys
import signal

flag_server_process = None
main_app_process = None

def signal_handler(sig, frame):
    print('\nShutting down servers...')
    if flag_server_process:
        flag_server_process.terminate()
    if main_app_process:
        main_app_process.terminate()
    sys.exit(0)

def main():
    global flag_server_process, main_app_process
    
    print("[+] Starting SSRF Lab Environment")
    print("[+] Flag is located at http://127.0.0.1:5001/flag.txt")
    
    print("[+] Starting internal flag server on http://127.0.0.1:5001")
    flag_server_process = subprocess.Popen([sys.executable, 'flag_server.py'])
    time.sleep(1)
    
    print("[+] Starting vulnerable application on http://0.0.0.0:5000")
    main_app_process = subprocess.Popen([sys.executable, 'app/main.py'])
    
    print("[+] Lab is ready!")
    print("[+] Visit http://localhost:5000 to access the vulnerable application")
    print("[+] Try to exploit the SSRF vulnerability to access the flag at http://127.0.0.1:5001/flag.txt")
    print("[+] Press Ctrl+C to stop the servers")
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()

if __name__ == "__main__":
    main()
