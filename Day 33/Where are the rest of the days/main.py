# To call APIs, you must import and install requests package
# Make an API call to Bible API
import requests

base_url = 'https://api.scripture.api.bible'
trial_url = 'https://api.scripture.api.bible/v1/bibles?language=eng'
headers = {'api-key': '414a957ccce82f4a472c05350b2aeb73'}
# Glossary
bibles_url = f'{base_url}/v1/bibles'
bible_id = ''
#specific_bible_url = f"{base_url}/v1/bibles/{bible_id}"
audio_bibles_url = f'{base_url}/v1/audio-bibles'
lang_id = 'eng'
filter_language = f'?language={lang_id}'

def call_api(url, key):
    return requests.get(url, key).json()
    # ↓ will return the error code and status message if the call fails
    #if response != 200:
     #   response.raise_for_status()
   # else:
    #    return response.json()

print(call_api(trial_url, headers))