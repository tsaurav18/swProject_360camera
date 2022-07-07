
# importing the module
import cv2

# reading the video
source = cv2.VideoCapture('4.mp4')
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output4.avi', fourcc, 20.0, (640, 480))
if (source.isOpened() == False):
    print("Error opening the video file")
else:
    # Get frame rate information
    # You can replace 5 with CAP_PROP_FPS as well, they are enumerations
    fps = source.get(5)
    print('Frames per second : ', fps, 'FPS')
    # Get frame count
    # You can replace 7 with CAP_PROP_FRAME_COUNT as well, they are enumerations
    frame_count = source.get(7)
    print('Frame count : ', frame_count)

# running the loop
while(source.isOpened()):

    # extracting the frames
    ret, img = source.read()
    if ret == True:
        # converting to gray-scale   2.COLOR_BGR2XYZ 3.COLOR_RGB2BGRA 4.COLOR_RGB2BGR
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        out.write(gray)
        # displaying the video
        cv2.imshow("Live", gray)
    # exiting the loop
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

# closing the window

out.release()
source.release()
cv2.destroyAllWindows()
