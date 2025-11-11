"""
Utility to close existing connections and restart the RAG app cleanly
"""
import os
import signal
import subprocess
import time

def kill_processes_on_port(port):
    """Kill any processes running on the specified port"""
    try:
        print(f"🔍 Checking for processes on port {port}...")
        
        # For Windows
        result = subprocess.run(
            ['netstat', '-ano'], 
            capture_output=True, 
            text=True, 
            shell=True
        )
        
        lines = result.stdout.split('\n')
        for line in lines:
            if f':{port}' in line and 'LISTENING' in line:
                # Extract PID (last column)
                parts = line.split()
                if len(parts) >= 5:
                    pid = parts[-1]
                    print(f"🎯 Found process {pid} on port {port}")
                    
                    # Kill the process
                    try:
                        subprocess.run(['taskkill', '/F', '/PID', pid], check=True)
                        print(f"✅ Killed process {pid}")
                    except subprocess.CalledProcessError:
                        print(f"❌ Failed to kill process {pid}")
        
        print(f"🔄 Port {port} is now free")
        
    except Exception as e:
        print(f"❌ Error checking port: {e}")

def restart_app():
    """Clean restart of the RAG application"""
    print("🔄 Performing clean restart...")
    
    # Kill processes on Gradio port
    kill_processes_on_port(7860)
    
    # Wait a moment for cleanup
    time.sleep(2)
    
    # Clear any cached modules
    import sys
    modules_to_clear = [m for m in sys.modules if 'gradio' in m.lower()]
    for module in modules_to_clear:
        if module in sys.modules:
            del sys.modules[module]
    
    print("✅ Cleanup complete - ready to restart")

if __name__ == "__main__":
    restart_app()
    
    # Now start the app
    print("🚀 Starting fresh RAG application...")
    os.system("python app.py")