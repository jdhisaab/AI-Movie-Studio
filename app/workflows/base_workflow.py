from abc import ABC
from datetime import datetime


class BaseWorkflow(ABC):
    """
    Base class for all workflows.

    Provides:
    - Console logging
    - Workflow headers/footers
    - Step logging
    - Success logging
    - Error logging
    - Execution timing
    """

    def __init__(self):
        self.start_time = datetime.now()

    # ---------------------------------------------------------
    # Header / Footer
    # ---------------------------------------------------------

    def header(self, title: str):

        print("\n" + "=" * 70)
        print(f"🎬 {title}")
        print("=" * 70)

    def footer(self, title: str):

        elapsed = datetime.now() - self.start_time

        print("\n" + "=" * 70)
        print(f"🎉 {title}")
        print("=" * 70)
        print(f"⏱ Total Time : {elapsed}")
        print("=" * 70)

    # ---------------------------------------------------------
    # Logging
    # ---------------------------------------------------------

    def log_step(self, message: str):

        print(f"\n▶ {message}...")

    def log_success(self, message: str):

        print(f"✅ {message}")

    def log_warning(self, message: str):

        print(f"⚠ {message}")

    def log_error(self, message: str):

        print(f"❌ {message}")

    def log_info(self, message: str):

        print(f"ℹ {message}")

    # ---------------------------------------------------------
    # Section
    # ---------------------------------------------------------

    def separator(self):

        print("-" * 70)