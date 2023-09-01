import os


def get_music_file(folder):
    # folder = os.path.abspath(folder)
    music_files = list()
    music_files.append('')
    for root, dirs, files in os.walk(folder):
        for filename in files:
            music_files.append(filename.split('/')[-1])
    return music_files


if __name__ == "__main__":
    print(get_music_file('../program_voice/voice_files/'))

