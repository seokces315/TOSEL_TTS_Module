from argparser import get_args

from loader import load_csv

from pipeline.base import (
    generate_tts_modules,
    parse_script,
    merge_utterances,
    save_audio,
)

from dotenv import load_dotenv

load_dotenv()

import os


# Main flow
def main(args):
    print("=" * 50)
    print("[START] TTS Generation started!")
    print()

    # Extract the level identifier from the data filename
    data_file = args.data_file[:-4]
    level = data_file.split("_")[-1]

    # Load a CSV file from the specified data path
    item_df = load_csv(data_path=f"./data/{args.data_file}")

    # Get the configurations from environment variables and command-line arguments
    openai_api_key = os.getenv("OPENAI_API_KEY")
    tts_model_id = os.getenv("TTS_MODEL_ID")
    voices = args.voices

    # Initialize TTS modules
    tts_modules = generate_tts_modules(
        api_key=openai_api_key,
        model_id=tts_model_id,
        voices=voices,
        level=level,
    )

    # Iterate over each row in the DataFrame
    for _, row in item_df.iterrows():
        if row["Type"] == "C":
            # Parse the script text from the row
            utterance_pair = parse_script(row["Script"])

            for idx, (speaker, utterance) in enumerate(utterance_pair):
                if speaker == "M":
                    audio_bytes = tts_modules[0].synthesize(utterance.strip())
                elif speaker == "W":
                    audio_bytes = tts_modules[1].synthesize(utterance.strip())
                elif speaker == "B":
                    audio_bytes = tts_modules[2].synthesize(utterance.strip())
                else:
                    audio_bytes = tts_modules[3].synthesize(utterance.strip())

                # Construct the filename by utterance index
                file_name = f'{data_file}_LC{row["No."]}_C{idx}.mp3'

                # Save the generated audio bytes to the output file
                save_audio(output_path=f"./res/{file_name}", audio_bytes=audio_bytes)
                print(f"[SAVED] {file_name}")
        else:
            # Construct the filename by item type
            if row["Type"] == "M":
                file_name = f'{data_file}_LC{row["No."]}_M.mp3'
            else:
                file_name = f'{data_file}_LC{row["No."]}_A.mp3'

            # Parse the script text from the row
            utterance_pair = parse_script(row["Script"])

            # Collect synthesized audio bytes for each utterance
            utterances = list()
            for speaker, utterance in utterance_pair:
                if speaker == "M" or speaker == "Q":
                    utterance = tts_modules[0].synthesize(utterance.strip())
                elif speaker == "W":
                    utterance = tts_modules[1].synthesize(utterance.strip())
                elif speaker == "B":
                    utterance = tts_modules[2].synthesize(utterance.strip())
                else:
                    utterance = tts_modules[3].synthesize(utterance.strip())
                utterances.append(utterance)

            # Merge all utterance audio into a single dialog track with pauses
            audio_bytes = merge_utterances(utterances=utterances)

            # Save the generated audio bytes to the output file
            save_audio(output_path=f"./res/{file_name}", audio_bytes=audio_bytes)
            print(f"[SAVED] {file_name}")

    print()
    print("[END] TTS Generated finished.")
    print("=" * 50)


if __name__ == "__main__":
    args = get_args()
    main(args)
