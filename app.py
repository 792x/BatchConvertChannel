# Script to batch convert  1 channel grayscale images to a 3 channel grayscale images
# To use, make sure dependencies are installed and run:
# >> python convertchannel.py inputfolder outputfolder

import cv2, dlib, argparse, os

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Align faces in image')
    parser.add_argument('input', type=str, help='')
    parser.add_argument('output', type=str, help='')
    parser.add_argument('--scale', metavar='S', type=int, default=1, help='an integer for the accumulator')
    args = parser.parse_args()

    input_image_folder = args.input
    output_image_folder = args.output
    scale = args.scale

    directory = os.fsencode(input_image_folder)

    list = os.listdir(directory)
    maxFiles = len(list)
    counter = 0

    for file in os.listdir(directory):
        counter = counter + 1
        filename = os.fsdecode(file)
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg") or filename.endswith(
                ".bmp"):
            print('transforming ' + str(counter) + '/' + str(maxFiles) + ': ' + filename)
            img = cv2.imread(input_image_folder + '/' + filename, cv2.IMREAD_GRAYSCALE)
            gray = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            print(img.shape)
            print(gray.shape)
            if filename.endswith('.jpg'):
                output_image = filename.replace('.jpg', '_%i.jpg' % counter)
            elif filename.endswith('.png'):
                output_image = filename.replace('.png', '_%i.jpg' % counter)
            elif filename.endswith('.jpeg'):
                output_image = filename.replace('.jpeg', '_%i.jpg' % counter)
            elif filename.endswith('.bmp'):
                output_image = filename.replace('.bmp', '_%i.bmp' % counter)
            else:
                output_image = output_image_folder + ('_%i.jpg' % counter)
            cv2.imwrite(output_image_folder + '/' + output_image, gray)
        else:
            continue
