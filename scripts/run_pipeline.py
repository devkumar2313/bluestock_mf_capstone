"""
Executes the end-to-end BlueStack mutual fund ETL pipeline using strict pathing.
"""
import subprocess
import sys
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

PROJECT_ROOT = Path(__file__).parent.resolve()

print(PROJECT_ROOT)
def execute_script(script_name):
    """
    Executes a Python scripts
    """
    script_path = PROJECT_ROOT / script_name

    logging.info(f"Starting step: {script_name}...")

    if not script_path.exists():
        logging.error(f"CRITICAL ERROR: Could not find {script_name} at {script_path}")
        sys.exit(1)

    try:
        subprocess.run(
            [sys.executable, str(script_path)],
            check=True,
            capture_output=True,
            text=True,
            cwd=str(PROJECT_ROOT)
        )
        logging.info(f"Successfully completed: {script_name}\n")

    except subprocess.CalledProcessError as error:
        logging.error(f"failed at {script_name}")
        logging.error(f"Error Details:\n{error.stderr}")
        sys.exit(1)


if __name__ == "__main__":
    logging.info(f"=== INITIALIZING PIPELINE IN: {PROJECT_ROOT} ===")


    pipeline_stages = [
        "02_data_cleaning.py",
        "01_data_ingestion.py",
        "load_database.py"
    ]

    for script in pipeline_stages:
        execute_script(script)

    logging.info("=== PIPELINE EXECUTION COMPLETE ===")