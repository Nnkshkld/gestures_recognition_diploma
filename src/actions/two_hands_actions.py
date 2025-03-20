class TwoHandsActions:
    def __init__(self):
        self.both_hands_detected = False
        self.previous_gesture = False
        self.gesture_count = 0

    def get_action(self, gesture):
        print(gesture)
        return gesture
