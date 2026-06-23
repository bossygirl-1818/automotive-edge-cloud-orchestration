import time

from src.digital_twin_layer import save_twin_state


def run_digital_twin_simulator():

    print("Digital Twin Simulator started.")
    print("Press CTRL + C to stop.\n")

    while True:
        save_twin_state()
        print("-" * 60)
        time.sleep(5)


if __name__ == "__main__":
    run_digital_twin_simulator()