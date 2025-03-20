class SingleHandActions:

    def get_action(self, gesture):
        print(gesture)
        return gesture

    def _like_gesture_action(self):
        return "👍"

    def _dislike_gesture_action(self):
        return "👎"

    def _stop_gesture_action(self):
        return "✋"

    def _okay_gesture_action(self):
        return "👌"
