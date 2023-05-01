# Noise_generator
The project is used for creating the dataset of audio recordings with background noises.

## Requirements
All the dependencies needed for the project are listed in the Pipfile. To install them, run the following command:
```pipenv install```. To activate the environment, run the following command:
```pipenv shell```.

## Usage
To generate the dataset, run the following command:
```python3 main.py```. The noise audios will be added to the main audio file.
The dataset will be saved in the folder ```data/processed```.
To add custom background noise, download audio files and place them in the folder ```data/raw/noise_files```.
You can find a variety of background noise files [here](https://www.zapsplat.com).
To add custom audio file for noise generation, place it in the folder ```data/raw/audio_files```.
The algorith will add each noise file to the original audio.