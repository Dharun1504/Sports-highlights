from SportStack import Highlights_gemini, Highlights_gpt
import dotenv

Highlightgen = Highlights_gpt('Destination\\',
                          api_base="https://openai-demetrius.openai.azure.com/", 
                          api_version="2023-07-01-preview", 
                          api_key=dotenv.get_key(key_to_get="OPENAI_API_KEY", dotenv_path = ".env") )
# Highlightgen = Highlights_gemini('Destination\\',api_key=dotenv.get_key(key_to_get="GOOGLE_API_KEY", dotenv_path = ".env"))
Highlightgen.generate_highlights('F:\Software-Project\Highlights\Sports-highlights\Cricket-data\Every Ball of the Extraordinary Final Over at Lord\'s!   England v Sri Lanka 2014.mp4')