from noise_generation.generator.noise_generator import RandomBackgroundNoise

if __name__ == '__main__':
    file_path = './noise_generation/data/raw/audio_files/Sprachaufnahme_Kommandos.wav'
    noise_path = './noise_generation/data/raw/noise_files'
    final_dir = './noise_generation/data/processed'

    noise_transform = RandomBackgroundNoise(file_path, noise_path, final_dir)
    transformed_audio = noise_transform()
