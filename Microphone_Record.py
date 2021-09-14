#Function for accepting audio



class Microphone_Record :

    import pyaudio # Soundcard audio I/O access library
    import wave # Python 3 module for reading / writing simple .wav files
    from pydub import AudioSegment



    audio = pyaudio.PyAudio()


    def record(self):


        # Setup channel info
        FORMAT = self.pyaudio.paInt16 # data type formate
        CHANNELS = 1 # Adjust to your number of channels
        RATE = 22050 # Sample Rate
        CHUNK = 1024 # Block Size
        RECORD_SECONDS = 4 # Record time
        WAVE_OUTPUT_FILENAME = "file.wav"
        INPUT_DEVICE_INDEX = 1

        # Startup pyaudio instance
        audio = self.pyaudio.PyAudio()

        # start Recording
        stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        input_device_index= INPUT_DEVICE_INDEX,
                        frames_per_buffer=CHUNK)
        print("Please speak - recording...")
        frames = []

        # Record for RECORD_SECONDS
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        print("Recording Complete")


        # Stop Recording
        stream.stop_stream()
        stream.close()
        audio.terminate()

        # Write your new .wav file with built in Python 3 Wave module
        waveFile = self.wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(audio.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()
        
        #Trim silence
        output = self.trim_audio(WAVE_OUTPUT_FILENAME.split(".")[0])
        output.export(WAVE_OUTPUT_FILENAME, format="wav")

        return output

    #Functions for trimming audio - may not be required in final version
    def trim_detect(self, sound):
        silence_threshold=-50.0
        chunk_size=10
        
        trim_ms = 0 # ms

        assert chunk_size > 0 # to avoid infinite loop
        while sound[trim_ms:trim_ms+chunk_size].dBFS < silence_threshold and trim_ms < len(sound):
            trim_ms += chunk_size
        
        return trim_ms

    def trim_audio(self, filename):
        
        sound = self.AudioSegment.from_file("{}.wav".format(filename), format="wav")

        start_trim = self.trim_detect(sound)
        end_trim = self.trim_detect(sound.reverse())

        duration = len(sound)    
        trimmed_sound = sound[start_trim:duration-end_trim]
        
        return trimmed_sound


    def get_device_list(self, audio) :
        dev_count = audio.get_device_count()
        dev_list = []

        for i in range(dev_count) :
            dev_list.append( audio.get_device_info_by_index(i).get('name') )

        return dev_list
