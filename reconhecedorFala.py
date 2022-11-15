import speech_recognition as VoiceRecognizer


def transcreverAudio(caminho):

    r = VoiceRecognizer.Recognizer()
    
    with VoiceRecognizer.AudioFile(caminho) as source:
        audio = r.record(source)

    try:    
        transcricao = r.recognize_google(audio, None,"pt-BR")
        return transcricao


    except:
        print("Erro ao processar a transcrição!")
    