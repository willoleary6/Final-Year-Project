import cv2
from argparse import ArgumentParser
import os
from os import walk

parser = ArgumentParser()
parser.add_argument("-p",
                    "-path_to_videos",
                    dest="path_to_videos",
                    help="File path to the directory containing the mp4 files",
                    default=False
                    )
parser.add_argument("-d",
                    "-path_to_destination",
                    dest="path_to_destination",
                    help="path to the path_to_destination directory",
                    default=False
                    )
parser.add_argument("-s",
                    "-save_frame_number",
                    dest="save_frame_number",
                    help="save every nth frame",
                    default=5
                    )

args = parser.parse_args()
if args.path_to_videos and args.path_to_destination:
    path_to_videos = args.path_to_videos
    destination_path = args.path_to_destination
    save_frame_number = args.save_frame_number
    files_in_directory = []
    for (directory_path, directory_names, file_names) in walk(path_to_videos):
        files_in_directory.extend(file_names)
        break

    valid_video_paths = []
    valid_file_extension = ['.mp4']

    for i in files_in_directory:
        for j in valid_file_extension:
            if i.endswith(j):
                valid_video_paths.append(os.path.join(path_to_videos, i))
                break
    for i, video_path in enumerate(valid_video_paths):
        cap = cv2.VideoCapture(video_path)
        frame_number = 0
        path, video_name = os.path.split(video_path)
        video_name = video_name.split('.')[0]
        while True:
            frame_number = frame_number + 1
            # Read frame from camera
            ret, image_np = cap.read()
            if ret is not False:
                if frame_number % save_frame_number == 0:
                    cv2.imwrite(destination_path + video_name + "_" + str(frame_number) + '.jpg', image_np)
            else:
                break
else:
    print("Missing required arguments, check --help")
