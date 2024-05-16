import cv2

def capture_license_plate():
    cap = cv2.VideoCapture(0)  # Use the default camera

    while True:
        ret, frame = cap.read()
        cv2.imshow('Capture License Plate', frame)
        
        # Wait for the user to press 's' to save the frame
        if cv2.waitKey(1) & 0xFF == ord('s'):
            license_plate_image = frame
            break

    cap.release()
    cv2.destroyAllWindows()
    return license_plate_image

license_plate_image = capture_license_plate()
cv2.imwrite('license_plate.jpg', license_plate_image)
