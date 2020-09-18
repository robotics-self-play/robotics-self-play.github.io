import numpy as np
import skvideo.io
import sys

video_name = sys.argv[1]
images = skvideo.io.vread(video_name + ".mp4")
width = images[0].shape[0]


out_video_name = video_name + "-v2.mp4"
inputdict = {"-r": str(25)}
outputdict = {"-pix_fmt": "yuv420p"}
writer = skvideo.io.FFmpegWriter(out_video_name, inputdict=inputdict, outputdict=outputdict)

for image in images:
    writer.writeFrame(image[:width, :width*3, :])

writer.close()
print(f"finalize output image shape = {(width, width * 3)}; saved to {out_video_name}")
