import argparse


# Parses and returns the command-line arguments
def get_args():
    # Initializes the argument parser
    arg_parser = argparse.ArgumentParser(description="TOSEL TTS Module Settings")

    # Adds command-line arguments
    arg_parser.add_argument("--problem_type", default="A", type=str)
    arg_parser.add_argument("--level", default="ADV", type=str)

    arg_parser.add_argument("--model_id", default="gpt-4o-mini-tts", type=str)
    arg_parser.add_argument("--voice", default="echo", type=str)
    arg_parser.add_argument("--speed", default=1.0, type=float)

    # Parses command-line arguments
    parsed_args = arg_parser.parse_args()

    return parsed_args
