import cv2  as cv
import mediapipe as mp



class Hand():
    def __init__(self):
        self.mp_hand = mp.solution.hands
        self.Hand = self.mp_hand.Hands()
        self.mp_draw = mp.solutions.drawing_utils
    def detect(self,frame):
        frame_rbg = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
        results = self.Hand.process(frame_rbg)
        return results
    def draw_landmarks(self,frame,results):
        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:
               self.mp_draw.draw_landmarks(
                    frame, landmarks, self.mp_hand.HAND_CONNECTIONS,
                    self.mp_draw.DrawingSpec(color=(255, 0, 0), thickness=2, circle_radius=4),  # Blue color
                    self.mp_draw.DrawingSpec(color=(0, 255, 0), thickness=2)  # Green connection lines
                )

def process_hand(frame,hand_detector):
    results = hand_detector.detect(frame)
    hand_detector.draw_landmarks(frame, results)


def main():
    capture = cv.VideoCapture(0)

    hand_detector = Hand()

    while True:
        istrue,frame = capture.read()
        
        if not istrue:
             break
        process_hand(frame,hand_detector)
        
        cv.imshow("frame",frame)
        
        key = cv.waitKey(20)

        if key == ord('q'):
            break
    
    capture.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()