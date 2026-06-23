import time

from src.digital_twin_layer import save_twin_state
from src.digital_twin_db_loader import load_digital_twin_state_to_db


def run_digital_twin_collector():

    print("Digital Twin Collector started.")
    print("Generating and storing twin states every 5 seconds.")
    print("Press CTRL + C to stop.\n")

    while True:
        save_twin_state()
        load_digital_twin_state_to_db()

        print("Twin snapshot collected and stored.")
        print("-" * 60)

        time.sleep(5)


if __name__ == "__main__":
    run_digital_twin_collector()