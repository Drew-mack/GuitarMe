""" 
Edited by Andrew Mack 
This program takes an mp3 file and converts the mp3 file into a midi file using Spotify's Basic Pitch
"""
from basic_pitch.inference import predict_and_save
from pathlib import Path
from basic_pitch import ICASSP_2022_MODEL_PATH

FileInputPath = Path("./FileInput/Test1.mp3")

def converter(audioPath):
    predict_and_save(
        model_or_model_path=ICASSP_2022_MODEL_PATH,
        audio_path_list =[audioPath],
        output_directory=Path("./FileOutput"),
        save_midi=True,
        sonify_midi=False,
        save_model_outputs=False,
        save_notes=False
    )

def main():
    converter(FileInputPath)


if __name__ == "__main__":
    main()
