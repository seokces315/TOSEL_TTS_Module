from utils.config import TTSModelConfig
from pipeline.components.tts_model import TTSModule

from pydub import AudioSegment
from io import BytesIO

import os
import re


# Generate a list of TTSModule instances
def generate_tts_modules(api_key, model_id, voices, speed):
    # Build a list of TTSModelConfig objects for each voice
    tts_configs = list()
    for voice in voices:
        tts_config = TTSModelConfig(
            api_key=api_key,
            model_id=model_id,
            voice=voice,
            speed=speed,
        )
        tts_configs.append(tts_config)

    # Instantiate TTS modules for each TTS configuration
    tts_modules = list()
    for tts_config in tts_configs:
        tts_module = TTSModule(tts_config=tts_config)
        tts_modules.append(tts_module)

    return tts_modules


# Extracts (speaker, utterance) pairs from a dialogue text
def parse_script(text):
    # Regex pattern to capture a speaker label and its corresponding utterance
    pattern = r"(M|W|B|G|Q)\s*:\s*(.*?)(?=\s*(?:M|W|B|G|Q)\s*:\s*|\Z)"

    # Compile the regex with DOTALL
    matches = re.compile(pattern, flags=re.DOTALL)

    # Find all matches and return a list of tuples
    return [
        (speaker, utterance.strip()) for speaker, utterance in matches.findall(text)
    ]


# Merge multiple MP3 audio byte streams into a single audio track
def merge_utterances(utterances, pause_ms=250):
    # Create a silence segment for the pause between speakers
    silence = AudioSegment.silent(duration=pause_ms)

    # Initialize an empty audio segment for merging
    merged = AudioSegment.empty()
    # Append each audio segment and a silence pause to the merged output
    for utterance in utterances:
        merged += AudioSegment.from_file(BytesIO(utterance), format="mp3") + silence

    # Remove the trailing silence added after the final audio segment
    if pause_ms > 0 and len(merged) > pause_ms:
        merged = merged[:-pause_ms]

    # Create an in-memory buffer to store the exported audio data
    result = BytesIO()
    # Encode the merged audio as an MP3 file
    merged.export(result, format="mp3", bitrate="128k")

    # Return the encoded audio data as a bytes object
    return result.getvalue()


# Save the generated audio to the specified output file
def save_audio(output_path, audio_bytes):
    # Ensure the output directory exists before saving the file
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Write the audio bytes content to the specified file path
    with open(output_path, "wb") as f:
        f.write(audio_bytes)
