import cv2
import mediapipe as mp
from settings import *

class HandTracking:
    def __init__(self):
        self.hand_tracking = mp.solutions.hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self.hand_x = 0
        self.hand_y = 0
        self.results = None
        self.hand_closed = False

    def scan_hands(self, image):
        rows, cols, _ = image.shape
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        self.results = self.hand_tracking.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        self.hand_closed = True

        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                x, y = hand_landmarks.landmark[9].x, hand_landmarks.landmark[9].y
                self.hand_x = int(x * SCREEN_WIDTH)
                self.hand_y = int(y * SCREEN_HEIGHT)
                x1, y1 = hand_landmarks.landmark[12].x, hand_landmarks.landmark[12].y
                if y1 > y:
                    self.hand_closed = True
                mp.solutions.drawing_utils.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp.solutions.hands.HAND_CONNECTIONS
                )
        return image

    def get_hand_center(self):
        return (self.hand_x, self.hand_y)

    def display_hand(self):
        cv2.imshow("image", self.image)
        cv2.waitKey(1)

    def is_hand_closed(self):
        return True  # Always return True for hand being closed


