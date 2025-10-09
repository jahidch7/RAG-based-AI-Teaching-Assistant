# speech to text
# mp3 file is translated using large-v2 model
import whisper
model = whisper.load_model("large-v2")
result = model.transcribe(audio = "audios/['01_addition'].mp3", 
                          language = "hi", task = "translate")
print(result["text"])
