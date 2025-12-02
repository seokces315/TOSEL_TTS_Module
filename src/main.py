from argparser import get_args

from loader import load_question_list

from pipeline.schema import extract_from_schema

from utils.config import TTSModelConfig

from pipeline.base import run_tts_pipeline

import time


# Main flow
def main(args):
    # Measure execution time
    start_time = time.time()

    # Loads the question list based on the selected parameters
    problem_type = args.problem_type
    level = args.level
    input_path = f"../input/LC_{problem_type}_{level}.txt"
    question_list = load_question_list(input_path=input_path)

    # Extract structured items from the question schema
    item_list = extract_from_schema(question_list=question_list)

    # Initialize the TTS configuration using the provided model ID
    model_id = args.model_id
    voice = args.voice
    speed = args.speed
    tts_config = TTSModelConfig(model_id=model_id, voice=voice, speed=speed)

    # Run the TTS pipeline
    item = item_list[0]
    base_path = f"../output/LC_{problem_type}_{level}"
    run_tts_pipeline(tts_config=tts_config, item=item, base_path=base_path)

    # Print execution time
    end_time = time.time()
    elapsed = end_time - start_time
    print(f"Elapsed time: {elapsed:.2f}초")
    print()


if __name__ == "__main__":
    args = get_args()
    main(args)
