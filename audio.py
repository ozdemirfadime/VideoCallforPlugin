import sounddevice as sd
def callback(indata,frames,time,status):
    print(frames)
    stream = sd.RawInputStream(channel=2,samplerate=4800,callback=callback)
    with stream:
        sd.sleep(5*1000)
