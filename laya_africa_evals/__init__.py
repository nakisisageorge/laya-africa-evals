"""
Laya Africa Evaluation Suite
============================

Independent evaluation suite for the laya System-1 decision engine.
Provides African-language triage datasets, prompt-injection guard robustness
harness, and evaluation runners.

Part of GICT Africa's daily open-source engineering cycle.
"""

from laya_africa_evals.harness.guard_harness import GuardHarness, InjectionType, TestCase
from laya_africa_evals.runners.checkpoint_runners import LiveCheckpointRunner, MockRunner

__version__ = "0.1.0"
__author__ = "George Nakisisa"
__email__ = "nakisisageorge@gmail.com"
__company__ = "GICT Africa Technologies"
__website__ = "https://gictafrica.com"

__all__ = [
    "GuardHarness",
    "InjectionType",
    "TestCase",
    "MockRunner",
    "LiveCheckpointRunner",
]
