#Functions for trimming audio - may not be required in final version
def trim_detect(sound):
    silence_threshold=-50.0
    chunk_size=10
    
    trim_ms = 0 # ms

    assert chunk_size > 0 # to avoid infinite loop
    while sound[trim_ms:trim_ms+chunk_size].dBFS < silence_threshold and trim_ms < len(sound):
        trim_ms += chunk_size
    
    return trim_ms

def trim_audio(filename):
    from pydub import AudioSegment
    sound = AudioSegment.from_file("{}.wav".format(filename), format="wav")

    start_trim = trim_detect(sound)
    end_trim = trim_detect(sound.reverse())

    duration = len(sound)    
    trimmed_sound = sound[start_trim:duration-end_trim]
    
    return trimmed_sound