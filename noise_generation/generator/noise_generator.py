import math
import os
import pathlib
import random
import torch
import torchaudio


class RandomBackgroundNoise:
    """
    This class adds random background noise to an audio signal.
    The noise is randomly selected from a directory of WAV files.
    The noise is resampled to the same sample rate as the audio signal.
    The noise is scaled to a random SNR between `min_snr_db` and `max_snr_db`.

    :param file_path: path to audio file
    :param noise_dir: directory containing WAV files of background noises
    :param final_dir: directory where the final audio files will be saved
    :param min_snr_db: minimum SNR in dB
    :param max_snr_db: maximum SNR in dB
    """

    def __init__(self, file_path, noise_dir, final_dir, min_snr_db=0, max_snr_db=15):
        waveform, sample_rate = torchaudio.load(file_path)
        self.audio_file = waveform[0]
        self.audio_file /= torch.max(torch.abs(self.audio_file))
        self.sample_rate = sample_rate
        self.min_snr_db = min_snr_db
        self.max_snr_db = max_snr_db
        self.final_dir = final_dir

        if not os.path.exists(noise_dir):
            raise IOError(f'Noise directory `{noise_dir}` does not exist')
        self.noise_files_list = list(pathlib.Path(noise_dir).glob('**/*.wav'))
        if len(self.noise_files_list) == 0:
            raise IOError(f'No .wav file found in the noise directory `{noise_dir}`')

    def __call__(self):
        audio_length = self.audio_file.shape[-1]
        noise_audios = []

        for noise_file in self.noise_files_list:
            effects = [
                ['remix', '1'],
                ['rate', str(self.sample_rate)],
            ]
            noise, _ = torchaudio.sox_effects.apply_effects_file(str(noise_file), effects, normalize=True)
            noise_length = noise.shape[-1]
            if noise_length > audio_length:
                offset = random.randint(0, noise_length - audio_length)
                noise = noise[..., offset:offset + audio_length]
            elif noise_length < audio_length:
                noise = torch.cat([noise, torch.zeros((noise.shape[0], audio_length - noise_length))], dim=-1)

            snr_db = random.randint(self.min_snr_db, self.max_snr_db)
            snr = math.exp(snr_db / 10)
            audio_power = self.audio_file.norm(p=2)
            noise_power = noise.norm(p=2)
            scale = snr * noise_power / audio_power

            noise_audio = (scale * self.audio_file + noise) / 2
            noise_audios.append(noise_audio)

        for counter, audio in enumerate(noise_audios):
            file_name = f'./noise_generation/data/processed/noisy_audio_{counter}.wav'
            torchaudio.save(file_name, audio, sample_rate=self.sample_rate)
            print(f'Saved noisy audio {counter + 1} to {file_name}')
