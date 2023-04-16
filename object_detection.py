import cv2

# Load the image
cap=cv2.VideoCapture("test2.mp4")


while(cap.isOpened()):
    _, frame=cap.read()
    canny=canny(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Load the car classifier
    car_cascade = cv2.CascadeClassifier('cars.xml')

    # Detect cars in the image
    cars = car_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Define the minimum distance for warning (in pixels)
    min_distance = 100

    # Draw rectangles around the detected cars
    for (x, y, w, h) in cars:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    
    # Calculate the distance from the car to the bottom of the image
        distance = img.shape[0] - (y + h)
    
    # Display a warning message if the distance is less than the minimum distance
        if distance < min_distance:
            cv2.putText(img, "Too close!", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    # Display the result
    cv2.imshow('image', frame)
    if cv2.waitkey(1) & 0xFF==ord('q'):
        break

cv2.destroyAllWindows()
