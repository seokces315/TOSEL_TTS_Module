from utils.config import TTS_INSTRUCTIONS_BY_LEVEL

from openai import OpenAI


# Class for generating speech audio using OpenAI TTS
class TTSModule:
    # Initializer
    def __init__(self, tts_config):
        # Initialize OpenAI client using the provided API key
        self.client = OpenAI(api_key=tts_config.api_key)

        # Load TTS configuration
        self.model_id = tts_config.model_id
        self.voice = tts_config.voice
        self.level = tts_config.level
        self.response_format = tts_config.response_format

        # Define TTS instructions optimized for producing test-appropriate English audio
        self.instructions = TTS_INSTRUCTIONS_BY_LEVEL[self.level]

    # Generate speech audio from the given text
    def synthesize(self, text):
        # Request speech synthesis from the OpenAI TTS model
        response = self.client.audio.speech.create(
            model=self.model_id,
            voice=self.voice,
            input=text,
            instructions=self.instructions,
            response_format=self.response_format,
        )

        # Decode the returned base64 audio data into raw bytes
        audio_bytes = response.read()

        return audio_bytes
