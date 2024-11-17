#!/home/vibhorag/bin/venv3.11/bin/python

from podcastfy.client import generate_podcast
from IPython.display import Audio, display
import os
def embed_audio(audio_file):
	"""
	Embeds an audio file in the notebook, making it playable.

	Args:
		audio_file (str): Path to the audio file.
	"""
	try:
		display(Audio(audio_file))
		print(f"Audio player embedded for: {audio_file}")
	except Exception as e:
		print(f"Error embedding audio: {str(e)}")
		
#audio_file = generate_podcast(urls=["/home/vibhorag/personal-space/docs/safe/VibhorResume_en.pdf"])
audio_file = generate_podcast(
    urls=["https://en.wikipedia.org/wiki/Artificial_intelligence"],
  #  llm_model_name="gpt-4-turbo",
 #   api_key_label=os.getenv("OPENAI_API_KEY")
)


