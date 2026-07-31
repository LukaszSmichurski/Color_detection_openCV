import cv2 as cv
import numpy as np
from util import get_limits



def color_detection():

    kolory_bgr = {
        "Czerwony": [0, 0, 255],
        "Zielony": [0, 255, 0],
        "Niebieski": [255, 0, 0],
        "Żółty": [0, 255, 255]
    }               #kolory bgr opencv w takich pracuje

    cap = cv.VideoCapture(1)  # przechwytywanie obrazu kamery(jezeli nie dziala mozna zmienic z 1 na 0)

    while(True):
        ret, frame = cap.read()

        hsvImage = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        for nazwa_koloru, bgr_val in kolory_bgr.items():

            lowerLimit, upperLimit = get_limits(color=bgr_val)
            mask = cv.inRange(hsvImage, lowerLimit, upperLimit)

            kernel = np.ones((5, 5), np.uint8) #usuwanie szumow, pikseli o malych wartosciach zakłocajacych obraz kernel - jadra
            mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)

            contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

            for cnt in contours:
                area = cv.contourArea(cnt)

                # Ignorujemy plamy mniejsze niż 1000 pikseli
                if area > 1000:
                    x, y, w, h = cv.boundingRect(cnt)

                    cv.rectangle(frame, (x, y), (x + w, y + h), bgr_val, 3)

                    cv.putText(
                        frame,
                        nazwa_koloru,
                        (x, max(y - 10, 20)),
                        cv.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        bgr_val,
                        2
                    )

        cv.imshow("Detekcja", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    color_detection()