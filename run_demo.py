"""
Main demo script - Run this to test the API
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from scripts.demo_api import run_demo

if __name__ == "__main__":
    print("Starting API Demo...")
    print("Make sure the API server is running on http://localhost:5000")
    print("You can start it with: python run_api.py")
    
    input("Press Enter to continue with the demo...")
    run_demo()