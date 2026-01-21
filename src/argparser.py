import argparse


# Parses and returns the command-line arguments
def get_args():
    # Initializes the argument parser
    arg_parser = argparse.ArgumentParser(description="TOSEL TTS Module Settings")

    # Adds command-line arguments
    arg_parser.add_argument("--data_file", default="92_PS.csv", type=str)
    arg_parser.add_argument(
        "--voices", nargs="+", default=["onyx", "coral", "alloy", "shimmer"], type=str
    )
    arg_parser.add_argument("--speed", default=1.0, type=float)

    # Parses command-line arguments
    parsed_args = arg_parser.parse_args()

    return parsed_args
