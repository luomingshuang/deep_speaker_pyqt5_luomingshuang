import os
import glob

data = 'media'
wav_files = glob.glob(os.path.join(data, '*.wav'))
speakers = []
for wav in wav_files:
    name = wav.split('\\')[-1].split('_')[0]
    if name not in speakers:
        speakers.append(name)

print(speakers, len(speakers))