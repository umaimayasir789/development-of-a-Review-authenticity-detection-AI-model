"""
Main evaluation script - Run this to evaluate the trained model
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from scripts.evaluate_model import evaluate_model

if __name__ == "__main__":
    print("Starting Model Evaluation...")
    success = evaluate_model()
    
    if success:
        print("\n✅ Evaluation completed successfully!")
        print("Check the 'evaluation_results' folder for detailed results:")
        print("- confusion_matrix.png")
        print("- roc_curve.png")
        print("- detailed_results.csv")
    else:
        print("\n❌ Evaluation failed!")
        sys.exit(1)