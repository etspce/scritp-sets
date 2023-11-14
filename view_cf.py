import glob
from shutil import copy
from moviepy.editor import *


def subclips_from_dir(dir_path, new_path, clip_duration=3):
    for all_file_name in glob.glob(dir_path):
        file_name_array = all_file_name.split('/')
        sub_dir = file_name_array[-2]

        video = VideoFileClip(all_file_name)

        file_name = file_name_array[-1]
        video_duration = int(video.duration)

        if not os.path.exists(os.path.join(new_path, sub_dir)): os.makedirs(os.path.join(new_path, sub_dir))
        if video_duration < 3:
            copy(all_file_name, os.path.join(new_path, sub_dir, file_name))
        else:
            for i in range(0, video_duration, clip_duration):
                new_file_name = os.path.join(new_path, sub_dir, str(i) + '_' + file_name)
                sub_video = video.subclip(i, min(i + clip_duration, video_duration))
                sub_video.write_videofile(new_file_name)


if __name__ == "__main__":
    # dir = "D:/PyQt5/js_img/videos/result_1.mp4"
    dir = r'D:/PyQt5/js_img/videos/result_wg_video.mp4'
    new_dir = "D:/PyQt5/js_img/short_videos/"
    subclips_from_dir(dir, new_dir, 300)  # 300秒一个视频分段
