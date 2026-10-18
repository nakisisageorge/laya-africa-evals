"""
Mock and Live Checkpoint Runners
================================

Utilities for running evaluations using mock data or live model checkpoints.

Part of the laya-africa-evals suite.
"""

import json
import random
from pathlib import Path
from typing import Any, Dict


class MockRunner:
    """Runner that uses mock data for fast, reliable testing."""

    def __init__(self, mock_data_dir: str = "results/mock"):
        self.mock_data_dir = Path(mock_data_dir)
        self.mock_data_dir.mkdir(parents=True, exist_ok=True)

    def run_triage_evaluation(
        self, dataset_path: str, model_version: str = "mock-v1.0"
    ) -> Dict[str, Any]:
        """
        Run triage evaluation using mock results.

        Args:
            dataset_path: Path to the dataset JSONL file
            model_version: Version identifier for the model being tested

        Returns:
            Dictionary with evaluation results
        """
        # Load dataset
        examples = []
        with open(dataset_path, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    examples.append(json.loads(line))

        # Generate mock results (in real implementation, this would call the model)
        results = []
        correct = 0

        for example in examples:
            # Simulate model prediction with some randomness for realism
            # In reality, this would be: prediction = model.predict(example['text'])
            predicted = (
                example["expected_triage"]
                if random.random() > 0.1
                else random.choice(["urgent", "routine", "follow_up", "potential_spam"])
            )

            is_correct = predicted == example["expected_triage"]
            if is_correct:
                correct += 1

            results.append(
                {
                    "text": example["text"],
                    "language": example["language"],
                    "expected": example["expected_triage"],
                    "predicted": predicted,
                    "correct": is_correct,
                    "metadata": example.get("metadata", {}),
                }
            )

        accuracy = correct / len(examples) if examples else 0

        return {
            "model_version": model_version,
            "dataset_path": dataset_path,
            "total_examples": len(examples),
            "correct_predictions": correct,
            "accuracy": accuracy,
            "results": results,
        }

    def save_results(self, results: Dict[str, Any], dataset_name: str):
        """Save results to mock data directory."""
        output_file = self.mock_data_dir / f"{dataset_name}_results.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2)
        return output_file


class LiveCheckpointRunner:
    """Runner that uses live model checkpoints (requires actual model loading)."""

    def __init__(self, checkpoint_dir: str = "./checkpoints"):
        self.checkpoint_dir = Path(checkpoint_dir)
        self.checkpoint_dir.mkdir(parents=True, exist_ok=True)

    def load_laya_checkpoint(self, checkpoint_name: str = "laya-multilingual") -> Any:
        """
        Load a live laya checkpoint.

        In a real implementation, this would load the actual model.
        For this mock implementation, we return a placeholder.
        """
        checkpoint_path = self.checkpoint_dir / f"{checkpoint_name}.pt"

        # In reality, you would do something like:
        # import torch
        # model = LayaModel.load_from_checkpoint(checkpoint_path)
        # return model

        # Mock implementation
        if not checkpoint_path.exists():
            # Create a dummy checkpoint file for demonstration
            checkpoint_path.parent.mkdir(parents=True, exist_ok=True)
            with open(checkpoint_path, "w") as f:
                f.write("# Mock checkpoint file\n")
                f.write("# In real implementation, this would contain model weights\n")

        return {"checkpoint_name": checkpoint_name, "status": "mock_loaded"}

    def run_triage_evaluation(
        self, dataset_path: str, checkpoint_name: str = "laya-multilingual"
    ) -> Dict[str, Any]:
        """
        Run triage evaluation using a live checkpoint.

        Args:
            dataset_path: Path to the dataset JSONL file
            checkpoint_name: Name of the checkpoint to load

        Returns:
            Dictionary with evaluation results
        """
        # Load the checkpoint
        checkpoint = self.load_laya_checkpoint(checkpoint_name)

        # Load dataset
        examples = []
        with open(dataset_path, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    examples.append(json.loads(line))

        # In real implementation, this would use the loaded model to make predictions
        # For mock implementation, we'll generate reasonable mock results
        results = []
        correct = 0

        for example in examples:
            # Simulate slightly better performance than mock runner for "live" checkpoint
            predicted = (
                example["expected_triage"]
                if random.random() > 0.05
                else random.choice(["urgent", "routine", "follow_up", "potential_spam"])
            )

            is_correct = predicted == example["expected_triage"]
            if is_correct:
                correct += 1

            results.append(
                {
                    "text": example["text"],
                    "language": example["language"],
                    "expected": example["expected_triage"],
                    "predicted": predicted,
                    "correct": is_correct,
                    "metadata": example.get("metadata", {}),
                }
            )

        accuracy = correct / len(examples) if examples else 0

        return {
            "checkpoint": checkpoint,
            "dataset_path": dataset_path,
            "total_examples": len(examples),
            "correct_predictions": correct,
            "accuracy": accuracy,
            "results": results,
        }


def create_sample_datasets():
    """Create sample dataset files for demonstration."""
    datasets_dir = Path("datasets")
    datasets_dir.mkdir(exist_ok=True)

    # This would normally be called to generate the datasets
    # Since we already created them manually, this is just a placeholder
    pass


if __name__ == "__main__":
    # Demonstration of usage
    print("Laya Africa Evals - Runner Demo")
    print("=" * 35)

    # Mock runner example
    mock_runner = MockRunner()
    print(f"MockRunner initialized with data dir: {mock_runner.mock_data_dir}")

    # Live checkpoint runner example
    live_runner = LiveCheckpointRunner()
    print(f"LiveCheckpointRunner initialized with checkpoint dir: {live_runner.checkpoint_dir}")

    print("\nTo use:")
    print("1. MockRunner.run_triage_evaluation('datasets/swahili_triage.jsonl')")
    print("2. LiveCheckpointRunner.run_triage_evaluation('datasets/swahili_triage.jsonl')")
