import os
import shutil

source = ""

video_folder = r""
image_folder = r""
text_folder = r""
program_folder = r""
audio_folder = r""

files = os.listdir(source)

video_format = ['mp4', 'mov', 'mkv']
text_format = ['pdf', 'txt', 'doc']
image_format = ['png', 'jpeg',  'gif', 'jpg']
programming_format = ['py', 'js', 'html']
audio_format = ['mp3', 'wav']

for file in files:
    file_ext = os.path.splitext(file)[-1].replace(".", "")

    if file_ext in video_format:
        shutil.move(source + file, video_folder)
    if file_ext in text_format:
        shutil.move(source + file, text_folder)
    if file_ext in image_format:
        shutil.move(source + file, image_folder)
    if file_ext in programming_format:
        shutil.move(source + file, program_folder)
    if file_ext in audio_format:
        shutil.move(source + file, audio_folder)
