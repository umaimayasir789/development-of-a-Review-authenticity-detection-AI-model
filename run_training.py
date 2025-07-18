"""
Main training script - Run this to train the model
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from scripts.train_model import train_model

if __name__ == "__main__":
    print("Starting Review Authenticity Detection Model Training...")
    success = train_model()
    
    if success:
        print("\n✅ Training completed successfully!")
        print("Next steps:")
        print("1. Run 'python run_evaluation.py' to evaluate the model")
        print("2. Run 'python run_api.py' to start the API server")
        print("3. Run 'python run_demo.py' to test the API")
    else:
        print("\n❌ Training failed!")
        sys.exit(1)