import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

frame_number = 0

while True and frame_number<=8:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break
    
    cv2.imshow('Camera Feed', frame)

    frame_number += 1
    image_filename = f"frame{frame_number}.jpg"
    # image_filename = "frame.jpg"

    cv2.imwrite(image_filename, frame)

# if cv2.waitKey(1) & 0xFF == ord('q'):
    

cap.release()
cv2.destroyAllWindows()