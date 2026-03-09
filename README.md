# ‧₊˚♪ 𝄞₊˚⊹ Noise Generator ‧₊˚♪ 𝄞₊˚⊹

**Noise Generator** is a Python-based tool designed to create datasets of audio recordings mixed with various background noises. 

This project is highly useful for data augmentation when building machine learning models for speech recognition, audio classification, or noise-cancellation systems. It takes your clean audio files, overlays them with different background noises, and outputs a ready-to-use augmented dataset.

## Project Structure

For the script to work correctly, ensure your files are organized in the following directory structure:

* `data/raw/audio_files/` - Place your **original, clean audio** files here.
* `data/raw/noise_files/` - Place your **background noise** files here.
* `data/processed/` - The script will automatically save the **generated noisy audio** files here.

## Getting Started

### Prerequisites

This project uses `pipenv` to manage dependencies. If you do not have it installed, you can get it via pip:
```bash
pip install pipenv
```

### Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/maybe-im-a-mess/Noise_generator.git
   cd Noise_generator
   ```
2. Install the required dependencies:
   ```bash
   pipenv install
   ```
3. Activate the virtual environment:
   ```bash
   pipenv shell
   ```

### Usage

1. **Add Clean Audio:** Place the base audio file(s) you want to augment into the `data/raw/audio_files/` folder.
2. **Add Noise Audio:** Place your background noise files into the `data/raw/noise_files/` folder. 
   > *Need noise files? You can find a wide variety of free background noises at [Zapsplat](https://www.zapsplat.com).*
3. **Run the Generator:** Execute the main script. The algorithm will iterate through your files and add each noise profile to the original audio.
   ```bash
   python3 main.py
   ```
4. **Retrieve Output:** Check the `data/processed/` folder for your newly generated dataset!

---
*A simple data augmentation tool for generating robust audio datasets.*
