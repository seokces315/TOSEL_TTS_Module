from .components.tts_model import TTSModule

import os


# Save the generated audio to the specified output file
def save_audio(output_path, audio_bytes):
    # Ensure the output directory exists before saving the file
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Write the audio byte content to the specified file path
    with open(output_path, "wb") as f:
        f.write(audio_bytes)


def run_tts_pipeline(tts_config, item, base_path):
    # Initialize the TTS module with the given configuration
    tts_module = TTSModule(tts_config=tts_config)

    # If passages exist in the item, generate audio for each passage
    if "passages" in item:
        passages = item["passages"]

        # Iterate over each passage and synthesize an audio file
        for idx, passage in enumerate(passages):
            passage_audio_bytes = tts_module.synthesize(passage)

            # Build the output file path for the current passage
            passage_output_path = os.path.join(base_path, f"passage_{idx + 1}.mp3")

            # Save the generated audio to the specified path
            save_audio(output_path=passage_output_path, audio_bytes=passage_audio_bytes)

    # Generate TTS audio from the question text
    question = item["question"]
    question_audio_bytes = tts_module.synthesize(question)

    # Build the output file path for the current question
    question_output_path = os.path.join(base_path, f"question.mp3")

    # Save the generated audio to the specified path
    save_audio(output_path=question_output_path, audio_bytes=question_audio_bytes)

    # Generate and save TTS audio for each answer choice in the list
    choices = item["choices"]
    for idx, choice in enumerate(choices):
        choice_audio_bytes = tts_module.synthesize(choice)

        # Build the output file path for the current choice
        choice_output_path = os.path.join(base_path, f"choice_{idx + 1}.mp3")

        # Save the generated audio to the specified path
        save_audio(output_path=choice_output_path, audio_bytes=choice_audio_bytes)
