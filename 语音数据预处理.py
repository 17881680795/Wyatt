# -*- coding:utf-8 -*-
# @Auther:    Wyatt
# @Date:     2023-04-16
# @FileName: 语音数据预处理.py
"""
import wave
# 读取语音数据
# 打开 WAV 文件
with wave.open('speech.wav', 'rb') as f:
    # 获取参数
    framerate = f.getframerate()
    nframes = f.getnframes()
    sampwidth = f.getsampwidth()
    nchannels = f.getnchannels()
    # 读取数据
    datasets = f.readframes(nframes)
"""

"""# 播放语音数据
import pyaudio
import wave

# 打开 WAV 文件
with wave.open('speech.wav', 'rb') as f:
    # 获取参数
    framerate = f.getframerate()
    nframes = f.getnframes()
    sampwidth = f.getsampwidth()
    nchannels = f.getnchannels()

    # 初始化 PyAudio
    p = pyaudio.PyAudio()

    # 打开音频流
    stream = p.open(format=p.get_format_from_width(sampwidth),
                    channels=nchannels,
                    rate=framerate,
                    output=True)

    # 读取并播放数据
    datasets = f.readframes(nframes)
    while len(datasets) > 0:
        stream.write(datasets)
        datasets = f.readframes(nframes)

    # 关闭音频流和 PyAudio
    stream.stop_stream()
    stream.close()
    p.terminate()"""

# 录制语音数据
import pyaudio
import wave

#  录制参数
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 5
MAX_RECORD_SECONDS = 60  # 最长录制时长为60秒

#  初始化PyAudio
p = pyaudio.PyAudio()

#  打开音频流
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

#  录制数据
frames = []
try:
    for i in range(0, int(RATE / CHUNK * MAX_RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
except KeyboardInterrupt:
    pass
except Exception as e:
    print("录音发生异常：", e)

#  关闭音频流和PyAudio
stream.stop_stream()
stream.close()
p.terminate()

#  保存录制的数据
with wave.open("record.wav", 'wb') as f:
    f.setnchannels(CHANNELS)
    f.setsampwidth(p.get_sample_size(FORMAT))
    f.setframerate(RATE)
    f.setcomptype("NONE", "No  compression")
    #  对录制的数据进行编码处理
    encode_data = b''.join(frames)
    f.writeframes(encode_data)

"""# 清洗语音数据
import wave

# 打开 WAV 文件
with wave.open('speech.wav', 'rb') as f:
    # 获取参数
    framerate = f.getframerate()
    nframes = f.getnframes()
    sampwidth = f.getsampwidth()
    nchannels = f.getnchannels()

    # 读取数据
    datasets = f.readframes(nframes)

    # 去除静默部分
    thresh = 500  # 设置门限值
    clean_data = b''
    for i in range(0, len(datasets), sampwidth*nchannels):
        sample = int.from_bytes(datasets[i:i+sampwidth*nchannels], byteorder='little', signed=True)
        if abs(sample) > thresh:
            clean_data += datasets[i:i+sampwidth*nchannels]

    # 保存清洗后的数据
    with wave.open("clean_speech.wav", 'wb') as f:
        f.setnchannels(nchannels)
        f.setsampwidth(sampwidth)
        f.setframerate(framerate)
        f.writeframes(clean_data)"""

"""# 加窗语音数据
import wave
import numpy as np

# 打开 WAV 文件
with wave.open('speech.wav', 'rb') as f:
    # 获取参数
    framerate = f.getframerate()
    nframes = f.getnframes()
    sampwidth = f.getsampwidth()
    nchannels = f.getnchannels()

    # 读取数据
    datasets = f.readframes(nframes)

    # 加窗处理
    window = np.hamming(nframes)
    datasets = np.frombuffer(datasets, dtype=np.int16) * window
    datasets = np.asarray(datasets, dtype=np.int16)

    # 保存加窗后的数据
    with wave.open("windowed_speech.wav", 'wb') as f:
        f.setnchannels(nchannels)
        f.setsampwidth(sampwidth)
        f.setframerate(framerate)
        f.writeframes(datasets.tobytes())
"""
