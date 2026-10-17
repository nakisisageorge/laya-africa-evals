#!/usr/bin/env python3
"""
Utility script to run a quick evaluation demonstration.
"""

import sys
import os
from pathlib import Path

# Add the current directory and parent directory to Python path
current_dir = Path(__file__).parent.absolute()
sys.path.insert(0, str(current_dir))
sys.path.insert(0, str(current_dir.parent))

def main():
    """Run a quick demonstration of the evaluation suite."""
    print("Laya Africa Evaluation Suite - Demo")
    print("=" * 40)
    
    # Check if we can import the package
    try:
        import laya_africa_evals
        print("✓ Successfully imported laya_africa_evals package")
    except ImportError as e:
        print(f"✗ Failed to import laya_africa_evals: {e}")
        # Try alternative import
        try:
            sys.path.insert(0, os.getcwd())
            import laya_africa_evals
            print("✓ Successfully imported laya_africa_evals package (alternative path)")
        except ImportError as e2:
            print(f"✗ Failed to import laya_africa_evals: {e2}")
            return 1
    
    # Show available datasets
    datasets_dir = Path("datasets")
    if datasets_dir.exists():
        dataset_files = list(datasets_dir.glob("*_triage.jsonl"))
        print(f"✓ Found {len(dataset_files)} dataset files:")
        for dataset in dataset_files:
            print(f"  - {dataset.name}")
    else:
        print("✗ Datasets directory not found")
        return 1
    
    # Show results if available
    results_dir = Path("results")
    if results_dir.exists():
        mock_results = results_dir / "mock_results.json"
        if mock_results.exists():
            print("✓ Mock results file found")
            try:
                import json
                with open(mock_results, 'r') as f:
                    data = json.load(f)
                accuracy = data.get("evaluation_summary", {}).get("overall_accuracy", 0)
                print(f"  Overall accuracy: {accuracy:.1%}")
            except Exception as e:
                print(f"  Error reading results: {e}")
        else:
            print("○ Mock results file not found")
    else:
        print("○ Results directory not found")
    
    # Show documentation
    docs_files = ["README.md", "DESIGN_DOCUMENT.md", "PORTFOLIO_CASE_STUDY.md"]
    print("\nDocumentation files:")
    for doc in docs_files:
        if Path(doc).exists():
            print(f"✓ {doc}")
        else:
            print(f"✗ {doc}")
    
    print("\nDemo completed successfully!")
    print("To run evaluations:")
    print("  python -m laya_africa_evals.runners.checkpoint_runners")
    print("  python -m tests.test_basic")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())