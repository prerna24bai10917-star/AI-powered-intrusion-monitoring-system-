from ultralytics import YOLO
import cv2
from datetime import datetime
import os

# Create folders if they do not exist
os.makedirs("outputs", exist_ok=True)
os.makedirs("logs", exist_ok=True)

# Load YOLO Model
model = YOLO("yolov8n.pt")

# Input Image
image_path = "dataset/sample_images/test.jpg"

# Run Detection
results = model(image_path)

for result in results:

    img = result.orig_img

    height, width, _ = img.shape

    # Virtual Border Line
    border_line = int(height * 0.60)

    cv2.line(
        img,
        (0, border_line),
        (width, border_line),
        (0, 0, 255),
        3
    )

    cv2.putText(
        img,
        "RESTRICTED BORDER ZONE",
        (20, border_line - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 0, 255),
        2
    )

    intrusion_count = 0

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for box in result.boxes:

        cls = int(box.cls[0])
        confidence = float(box.conf[0])

        label = model.names[cls]

        if label == "person" and confidence > 0.50:

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            center_x = (x1 + x2) // 2
            center_y = (y1 + y2) // 2

            if center_y > border_line:

                intrusion_count += 1

                color = (0, 0, 255)
                status = "INTRUDER"

            else:

                color = (0, 255, 0)
                status = "SAFE"

            cv2.rectangle(
                img,
                (x1, y1),
                (x2, y2),
                color,
                2
            )

            cv2.circle(
                img,
                (center_x, center_y),
                5,
                (255, 0, 0),
                -1
            )

            cv2.putText(
                img,
                f"{status} {confidence:.2f}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                color,
                2
            )

    # Alert Level
    if intrusion_count == 0:
        alert_level = "SAFE"
        alert_color = (0, 255, 0)

    elif intrusion_count <= 2:
        alert_level = "LOW ALERT"
        alert_color = (0, 255, 255)

    else:
        alert_level = "HIGH ALERT"
        alert_color = (0, 0, 255)

    # Display Intrusion Count
    cv2.putText(
        img,
        f"Intrusions: {intrusion_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        alert_color,
        3
    )

    # Display Alert Level
    cv2.putText(
        img,
        f"Status: {alert_level}",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        alert_color,
        3
    )

    # Display Timestamp
    cv2.putText(
        img,
        current_time,
        (20, 120),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    # Save Result Image
    cv2.imwrite("outputs/result.jpg", img)

    # Save Alert Screenshot
    if intrusion_count > 0:

        screenshot_name = (
            f"outputs/alert_"
            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        )

        cv2.imwrite(screenshot_name, img)

    # Log File
    with open("logs/intrusion_log.txt", "a") as log:

        log.write(
            f"{current_time} | "
            f"Intrusions: {intrusion_count} | "
            f"Alert Level: {alert_level}\n"
        )

print("Monitoring Completed Successfully")
