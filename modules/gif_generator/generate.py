import cv2
import imageio
import os
import sys

# 1. Get Images


# get image from directory
def get_images(object_type):
    folder = 'modules/gif_generator/img'
    if object_type.lower() == 'cup':
        folder = 'modules/gif_generator/cup'
    elif object_type.lower() == 'banana':
        folder = 'modules/gif_generator/banana'
    frames = []
    print(os.listdir(folder))
    for img in os.listdir(folder):
        pic = cv2.imread(os.path.join(folder, img))
        if pic is not None:
            frames.append(pic)
            print(f"frame {img} added")
    return frames





def generate_gif(object_type):
    cap = cv2.VideoCapture(1)

    frames = []
    
    image_count = 0
    frames += get_images(object_type)
    # 2. Save GIF animation
    print("Saving GIF file")
    with imageio.get_writer("modules/output.gif", mode="I", duration=0.2) as writer:
        print('writing inside file...')
        for idx, frame in enumerate(frames):
            print("Adding frame to GIF file: ", idx + 1)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            writer.append_data(rgb_frame)
        print("gif generated")