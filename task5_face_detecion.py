# CODSOFT AI Internship
# Task 5 - Face Detection and Recognition

import cv2
import os


def detect_faces(image_path):

    image = cv2.imread(image_path)

    if image is None:

        print("\nUnable to open the image.")

        return

    face_detector = cv2.CascadeClassifier(

        cv2.data.haarcascades +

        "haarcascade_frontalface_default.xml"

    )

    gray = cv2.cvtColor(

        image,

        cv2.COLOR_BGR2GRAY

    )

    faces = face_detector.detectMultiScale(

        gray,

        scaleFactor=1.1,

        minNeighbors=5,

        minSize=(30, 30)

    )

    print(

        f"\nNumber of faces detected: {len(faces)}"

    )

    for x, y, w, h in faces:

        cv2.rectangle(

            image,

            (x, y),

            (x + w, y + h),

            (0, 255, 0),

            2

        )

    cv2.imshow(

        "Face Detection",

        image

    )

    cv2.waitKey(0)

    cv2.destroyAllWindows()


def main():

    print("\n========== FACE DETECTION AI ==========")

    image_path = input(

        "\nEnter image file path: "

    ).strip()

    if not os.path.exists(image_path):

        print("\nImage file not found.")

        return

    detect_faces(image_path)


main()