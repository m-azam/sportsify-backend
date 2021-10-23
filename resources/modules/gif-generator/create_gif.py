import cv2
import imageio
import os
import sys

def generate_gif():
    # 1. Get Images
    cap = cv2.VideoCapture(1)

    frames = []
    image_count = 0

    # get image from directory
    def get_images(folder):
        for img in os.listdir(folder):
            pic = cv2.imread(os.path.join(folder, img))
            if pic is not None:
                frames.append(pic)

        return frames
    get_images('img') # get images from directory named img


    # 2. Save GIF animation
    print("Saving GIF file")
    with imageio.get_writer("output.gif", mode="I", duration=0.2, loop=False) as writer: #duration controls the speed of the animation
        for idx, frame in enumerate(frames):
            print("Adding frame to GIF file: ", idx + 1)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            writer.append_data(rgb_frame)

        