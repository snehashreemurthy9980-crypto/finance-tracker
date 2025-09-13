# 🏦 Financial Transparency Platform - VS Code Setup

## 🚀 Quick Start in VS Code

### Method 1: Use the Batch Script (Recommended)
1. Double-click `start_vscode.bat` in VS Code Explorer
2. Wait for both servers to start
3. Application will open automatically at http://localhost:3000

### Method 2: Use VS Code Debugger
1. Press `Ctrl+Shift+P`
2. Type "Debug: Start Debugging"
3. Select "Start Full Application"
4. Both servers will start automatically

### Method 3: Use VS Code Tasks
1. Press `Ctrl+Shift+P`
2. Type "Tasks: Run Task"
3. Select "Setup Full Application" (first time only)
4. Select "Start Backend" or "Start Frontend"

### Method 4: Use Terminal
1. Open Terminal (`Ctrl+`` `)
2. Run: `npm start` (backend)
3. Open new terminal: `cd client && npm start` (frontend)

## 📱 Application URLs
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:5000

## 🔧 VS Code Features

### Debug Configurations
- **Start Backend Server**: Debug backend only
- **Start Frontend Server**: Debug frontend only  
- **Start Full Application**: Debug both servers

### Tasks Available
- **Install Backend Dependencies**: `npm install`
- **Install Frontend Dependencies**: `npm install` in client folder
- **Start Backend**: `npm start`
- **Start Frontend**: `npm start` in client folder
- **Setup Full Application**: Install all dependencies

### File Structure
```
├── .vscode/
│   ├── launch.json      # Debug configurations
│   ├── tasks.json       # VS Code tasks
│   └── settings.json    # VS Code settings
├── client/              # React frontend
├── models/              # Database models
├── routes/              # API routes
├── services/            # Business logic
├── server.js            # Backend entry point
└── start_vscode.bat     # Quick start script
```

## 🛠️ Troubleshooting

### If servers don't start:
1. Check if ports 3000 and 5000 are free
2. Run `npm install` in both root and client folders
3. Check `.env` file exists with proper configuration

### If you get module errors:
1. Delete `node_modules` folders
2. Run `npm install` in both root and client folders
3. Restart VS Code

### If MongoDB connection fails:
1. Install MongoDB locally or use MongoDB Atlas
2. Update `MONGODB_URI` in `.env` file
3. Restart the backend server

## 🎯 Features Available
- ✅ User Authentication & Authorization
- ✅ Budget Management & Tracking
- ✅ Transaction Monitoring
- ✅ Blockchain Data Integrity
- ✅ Real-time Dashboard
- ✅ Responsive Design
- ✅ API Documentation
- ✅ Data Visualization

## 📞 Support
If you encounter any issues:
1. Check the terminal output for error messages
2. Verify all dependencies are installed
3. Ensure ports 3000 and 5000 are available
4. Check the `.env` file configuration

**Your Financial Transparency Platform is ready to run in VS Code! 🎉**
