from moviepy.editor import *

clip = (VideoFileClip("result/result_video.mp4"))
clip.write_gif("result/result_video.gif")