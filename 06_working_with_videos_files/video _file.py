
import cv2

video = cv2.VideoCapture("./mountain.mp4")

cv2.namedWindow("Video Frame", cv2.WINDOW_NORMAL)

while True:
    ret, frame = video.read()
    if not ret:
        break

    # Get screen-friendly size
    frame = cv2.resize(frame, (960, 540))  # 16:9 ratio

    cv2.imshow("Video Frame", frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()



import cv2

# Open video
video = cv2.VideoCapture("./mountain.mp4")

if not video.isOpened():
    print("Error: Video not opened")
    exit()

# Codec
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

# Get width & height
width  = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Get FPS (VERY IMPORTANT)
fps = 30

# Output writer
out = cv2.VideoWriter("output.mp4", fourcc, fps, (width, height))

while True:
    ret, frame = video.read()

    if not ret:
        break

    out.write(frame)

# Release
out.release()
video.release()

print("Video written successfully!")

# write a video 
import cv2

video = cv2.VideoCapture("./mountain.mp4")

fourcc = cv2.VideoWriter_fourcc(*"mp4v")

width  = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

fps = 30

out = cv2.VideoWriter("write_output.mp4", fourcc, fps, (width, height))

while True:
    ret, frame = video.read()
    if not ret:
        break
    frame= frame + 20

    out.write(frame)

out.release()
video.release()

print("Done")

#  write a grayscale video
import cv2

# Load video
video = cv2.VideoCapture("mountain.mp4")

# Codec
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

# Get size
width  = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

fps = 30

# IMPORTANT: grayscale = single channel → use isColor=False
out = cv2.VideoWriter("gray_output.mp4", fourcc, fps, (width, height), isColor=False)

while True:
    ret, frame = video.read()
    if not ret:
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Write frame
    out.write(gray)

    # Optional: show
    cv2.imshow("Gray Video", gray)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Release
video.release()
out.release()
cv2.destroyAllWindows()

print("Grayscale video saved!")

#blure the video
import cv2

# Load video
video = cv2.VideoCapture("mountain.mp4")

# Codec
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

# Get size
width  = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

fps = 30

# Output video
out = cv2.VideoWriter("blur_output.mp4", fourcc, fps, (width, height))

while True:
    ret, frame = video.read()
    if not ret:
        break

    # Apply blur
    blur = cv2.GaussianBlur(frame, (31, 31), 0)

    # Write frame
    out.write(blur)

    # Show
    cv2.imshow("Blur Video", blur)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Release
video.release()
out.release()
cv2.destroyAllWindows()

print("Blur video saved!")

#edge detection video
import cv2

video = cv2.VideoCapture("mountain.mp4")

fourcc = cv2.VideoWriter_fourcc(*"mp4v")

width  = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

fps = 30

# Edge output is grayscale → isColor=False
out = cv2.VideoWriter("edge_output.mp4", fourcc, fps, (width, height), isColor=False)

while True:
    ret, frame = video.read()
    if not ret:
        break

    # Convert to grayscale first
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply edge detection
    edges = cv2.Canny(gray, 100, 200)

    out.write(edges)

    cv2.imshow("Edges", edges)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

video.release()
out.release()
cv2.destroyAllWindows()

print("Edge video saved!")

#draw a rectangle on the video
import cv2

video = cv2.VideoCapture("mountain.mp4")

fourcc = cv2.VideoWriter_fourcc(*"mp4v")

width  = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

fps = 30

out = cv2.VideoWriter("draw_output.mp4", fourcc, fps, (width, height))

while True:
    ret, frame = video.read()
    if not ret:
        break

    # Draw rectangle
    cv2.rectangle(frame, (50, 50), (300, 300), (0, 255, 0), 2)

    # Add text
    cv2.putText(frame, "Object", (50, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 0, 255), 2)

    # Save frame
    out.write(frame)

    # Show frame
    cv2.imshow("Draw Video", frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

video.release()
out.release()
cv2.destroyAllWindows()

print("Draw video saved!")

# resize video  
import cv2

video = cv2.VideoCapture("mountain.mp4")

fourcc = cv2.VideoWriter_fourcc(*"mp4v")

fps = 30

# New size (change as you want)
new_width = 800
new_height = 500

out = cv2.VideoWriter("resize_output.mp4", fourcc, fps, (new_width, new_height))

while True:
    ret, frame = video.read()
    if not ret:
        break

    # Resize frame
    resized = cv2.resize(frame, (new_width, new_height))

    out.write(resized)

    cv2.imshow("Resized Video", resized)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

video.release()
out.release()
cv2.destroyAllWindows()

print("Resized video saved!")


# threshold video
import cv2

video = cv2.VideoCapture("mountain.mp4")

fourcc = cv2.VideoWriter_fourcc(*"mp4v")

width  = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

fps = 30

# Threshold output → grayscale → isColor=False
out = cv2.VideoWriter("threshold_output.mp4", fourcc, fps, (width, height), isColor=False)

while True:
    ret, frame = video.read()
    if not ret:
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply threshold
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    out.write(thresh)

    cv2.imshow("Threshold Video", thresh)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

video.release()
out.release()
cv2.destroyAllWindows()

print("Threshold video saved!")

#contour video
import cv2

video = cv2.VideoCapture("mountain.mp4")

fourcc = cv2.VideoWriter_fourcc(*"mp4v")

width  = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

fps = 30

out = cv2.VideoWriter("contour_output.mp4", fourcc, fps, (width, height))

while True:
    ret, frame = video.read()
    if not ret:
        break

    # Step 1: Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Step 2: Threshold (binary image)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Step 3: Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Step 4: Draw contours
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)

    # Save
    out.write(frame)

    # Show
    cv2.imshow("Contours", frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

video.release()
out.release()
cv2.destroyAllWindows()

print("Contour video saved!")