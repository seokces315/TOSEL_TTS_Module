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
        self.speed = tts_config.speed
        self.response_format = tts_config.response_format

        # Define TTS instructions optimized for producing test-appropriate English audio
        self.instructions = """
        Pronunciation: Precise and standard American English articulation.
        Voice: Clear and neutral, suitable for standardized English tests.
        Pacing: Steady and moderate, ensuring every word is easily understood.
        Tone: Calm and informative, without emotional coloring.
        Pauses: Natural short pauses at commas and sentence breaks for clarity.
        Delivery: Professional and consistent, avoiding dramatic variation.
        """

    # Generate speech audio from the given text
    def synthesize(self, text):
        # Request speech synthesis from the OpenAI TTS model
        response = self.client.audio.speech.create(
            model=self.model_id,
            voice=self.voice,
            input=text,
            instructions=self.instructions,
            speed=self.speed,
            response_format=self.response_format,
        )

        # Decode the returned base64 audio data into raw bytes
        audio_bytes = response.read()

        return audio_bytes
