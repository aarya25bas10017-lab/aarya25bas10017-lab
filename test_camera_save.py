import cv2

print("Starting test...")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Camera not opened")
    exit()

ret, frame = cap.read()

if not ret:
    print("❌ Failed to capture image")
else:
    print("✅ Image captured")

    # Save image in same folder
    success = cv2.imwrite("test.jpg", frame)

    if success:
        print("✅ Image saved as test.jpg")
    else:
        print("❌ Failed to save image")

cap.release()
