import sys
from pydub import AudioSegment
import subprocess


def ncm_to_mp3_pydub(ncm_file_path, mp3_file_path):
    """
    使用pydub库将NCM文件转换为MP3文件
    """
    try:
        audio = AudioSegment.from_file(ncm_file_path, "ncm")
        audio.export(mp3_file_path, format="mp3")
    except Exception as e:
        print(f"使用pydub转换时出现错误: {e}")


def ncm_to_mp3_ffmpeg(ncm_file_path, mp3_file_path):
    """
    使用ffmpeg通过subprocess模块将NCM文件转换为MP3文件
    """
    command = ["ffmpeg", "-i", ncm_file_path, mp3_file_path]
    try:
        subprocess.run(command)
    except subprocess.CalledProcessError as e:
        print(f"使用ffmpeg转换时出现错误: {e}")


if __name__ == "__main__":
    if len(sys.argv)!= 3:
        print("用法: python audio_converter.py <ncm_file_path> <mp3_file_path>")
        sys.exit(1)
    ncm_file_path = sys.argv[1]
    mp3_file_path = sys.argv[2]
    ncm_to_mp3_pydub(ncm_file_path, mp3_file_path)
    # 或者可以选择使用另一种转换方式
    # ncm_to_mp3_ffmpeg(ncm_file_path, mp3_file_path)