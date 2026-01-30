from pydantic_settings import BaseSettings


# Pydantic class
class TTSModelConfig(BaseSettings):
    api_key: str
    model_id: str
    voice: str
    level: str
    response_format: str = "mp3"

    class Config:
        protected_namespaces = ()


# TTS instructions mapped by difficulty level
TTS_INSTRUCTIONS_BY_LEVEL = {
    "CO": """
    Pronunciation: Precise and standard American English articulation.
    Voice: Clear and neutral, suitable for standardized English tests.
    Pacing: Very slow and deliberate, with ample time between words for beginners.
    Tone: Calm and informative, without emotional coloring.
    Pauses: Clearly noticeable pauses at commas and sentence breaks.
    Delivery: Highly controlled and careful, prioritizing maximum clarity.
    """,
    "PS": """
    Pronunciation: Precise and standard American English articulation.
    Voice: Clear and neutral, suitable for standardized English tests.
    Pacing: Slow and careful, allowing learners sufficient time to process each phrase.
    Tone: Calm and informative, without emotional coloring.
    Pauses: Slightly extended pauses at commas and sentence breaks.
    Delivery: Controlled and steady, emphasizing comprehension.
    """,
    "ST": """
    Pronunciation: Precise and standard American English articulation.
    Voice: Clear and neutral, suitable for standardized English tests.
    Pacing: Slightly slower than normal, with clear separation between phrases.
    Tone: Calm and informative, without emotional coloring.
    Pauses: Natural but clearly perceptible pauses at sentence boundaries.
    Delivery: Consistent and measured, maintaining clarity.
    """,
    "BA": """
    Pronunciation: Precise and standard American English articulation.
    Voice: Clear and neutral, suitable for standardized English tests.
    Pacing: Steady and moderate, ensuring every word is easily understood.
    Tone: Calm and informative, without emotional coloring.
    Pauses: Natural short pauses at commas and sentence breaks for clarity.
    Delivery: Professional and consistent, avoiding dramatic variation.
    """,
    "JR": """
    Pronunciation: Precise and standard American English articulation.
    Voice: Clear and neutral, suitable for standardized English tests.
    Pacing: Slightly faster than normal, while remaining clear and controlled.
    Tone: Calm and informative, without emotional coloring.
    Pauses: Brief, efficient pauses at sentence boundaries.
    Delivery: Smooth and confident, with consistent rhythm.
    """,
    "HJ": """
    Pronunciation: Precise and standard American English articulation.
    Voice: Clear and neutral, suitable for standardized English tests.
    Pacing: Fast but articulate, requiring focused listening.
    Tone: Calm and informative, without emotional coloring.
    Pauses: Minimal pauses, primarily at sentence endings.
    Delivery: Crisp and efficient, maintaining precision at speed.
    """,
    "ADV": """
    Pronunciation: Precise and standard American English articulation.
    Voice: Clear and neutral, suitable for standardized English tests.
    Pacing: Very fast and compact, similar to advanced listening test conditions.
    Tone: Calm and informative, without emotional coloring.
    Pauses: Very brief pauses only at major sentence breaks.
    Delivery: Highly fluent and compressed, with no unnecessary spacing.
    """,
}
