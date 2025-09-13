#!/usr/bin/env python3
"""
Script to help set up and run the full Financial Transparency Platform
This script checks for Node.js and MongoDB, then guides you through setup
"""

import subprocess
import sys
import os
import webbrowser
from pathlib import Path

def check_command(command):
    """Check if a command exists in the system PATH"""
    try:
        subprocess.run([command, '--version'], 
                      capture_output=True, check=True, timeout=10)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
        return False

def run_command(command, cwd=None):
    """Run a command and return the result"""
    try:
        result = subprocess.run(command, shell=True, cwd=cwd, 
                              capture_output=True, text=True, timeout=60)
        return result.returncode == 0, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return False, "", "Command timed out"

def main():
    print("🏦 Financial Transparency Platform - Full Application Setup")
    print("=" * 60)
    
    # Check for Node.js
    print("🔍 Checking for Node.js...")
    if check_command('node'):
        print("✅ Node.js is installed")
        # Get Node.js version
        success, stdout, stderr = run_command('node --version')
        if success:
            print(f"   Version: {stdout.strip()}")
    else:
        print("❌ Node.js is not installed")
        print("📥 Please install Node.js from: https://nodejs.org/")
        print("   Choose the LTS version for best compatibility")
        return
    
    # Check for npm
    print("\n🔍 Checking for npm...")
    if check_command('npm'):
        print("✅ npm is installed")
        success, stdout, stderr = run_command('npm --version')
        if success:
            print(f"   Version: {stdout.strip()}")
    else:
        print("❌ npm is not available")
        return
    
    # Check for MongoDB
    print("\n🔍 Checking for MongoDB...")
    if check_command('mongod'):
        print("✅ MongoDB is installed")
    else:
        print("⚠️  MongoDB not found in PATH")
        print("📥 Please install MongoDB from: https://www.mongodb.com/try/download/community")
        print("   Make sure to add MongoDB to your system PATH")
    
    print("\n🚀 Setting up the application...")
    
    # Install backend dependencies
    print("📦 Installing backend dependencies...")
    success, stdout, stderr = run_command('npm install')
    if success:
        print("✅ Backend dependencies installed")
    else:
        print("❌ Failed to install backend dependencies")
        print(f"Error: {stderr}")
        return
    
    # Install frontend dependencies
    print("📦 Installing frontend dependencies...")
    client_dir = Path("client")
    if client_dir.exists():
        success, stdout, stderr = run_command('npm install', cwd=client_dir)
        if success:
            print("✅ Frontend dependencies installed")
        else:
            print("❌ Failed to install frontend dependencies")
            print(f"Error: {stderr}")
            return
    else:
        print("❌ Client directory not found")
        return
    
    # Create .env file if it doesn't exist
    env_file = Path(".env")
    if not env_file.exists():
        print("📝 Creating environment configuration...")
        env_content = """# Database
MONGODB_URI=mongodb://localhost:27017/financial-transparency

# Server
PORT=5000
NODE_ENV=development
CLIENT_URL=http://localhost:3000

# JWT
JWT_SECRET=your-super-secret-jwt-key-change-this-in-production
JWT_EXPIRE=7d

# Blockchain (Local)
ETHEREUM_RPC_URL=http://localhost:8545
PRIVATE_KEY=your-private-key-for-blockchain-operations
CONTRACT_ADDRESS=your-smart-contract-address

# File Upload
MAX_FILE_SIZE=10485760
UPLOAD_PATH=./uploads
"""
        env_file.write_text(env_content)
        print("✅ Environment file created (.env)")
    
    print("\n🎉 Setup complete!")
    print("\n📋 Next steps:")
    print("1. Make sure MongoDB is running")
    print("2. Start the backend server: npm start")
    print("3. In a new terminal, start the frontend: cd client && npm start")
    print("4. Open http://lo" \
    "calhost:3000 in your browser")
    
    print("\n🔧 Quick start commands:")
    print("   Backend:  npm start")
    print("   Frontend: cd client && npm start")
    
    # Ask if user wants to start the servers
    response = input("\n🚀 Would you like to start the servers now? (y/n): ").lower().strip()
    if response in ['y', 'yes']:
        print("\n🔄 Starting backend server...")
        print("   Backend will run on: http://localhost:5000")
        print("   Frontend will run on: http://localhost:3000")
        print("   Press Ctrl+C to stop both servers")
        
        # Start backend in background
        backend_process = subprocess.Popen(['npm', 'start'], 
                                        stdout=subprocess.PIPE, 
                                        stderr=subprocess.PIPE)
        
        # Wait a moment for backend to start
        import time
        time.sleep(3)
        
        # Start frontend
        print("🔄 Starting frontend server...")
        frontend_process = subprocess.Popen(['npm', 'start'], 
                                          cwd=client_dir,
                                          stdout=subprocess.PIPE, 
                                          stderr=subprocess.PIPE)
        
        # Open browser
        print("🌐 Opening application in browser...")
        webbrowser.open('http://localhost:3000')
        
        try:
            # Wait for processes
            backend_process.wait()
            frontend_process.wait()
        except KeyboardInterrupt:
            print("\n🛑 Stopping servers...")
            backend_process.terminate()
            frontend_process.terminate()
            print("✅ Servers stopped")

if __name__ == "__main__":
    main()
