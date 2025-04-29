import subprocess
import os
import time

class SingleHandActions:
    def get_action(self, gesture):
        print(f"Known: {gesture}")
        if gesture == "is_like":
            return self._like_gesture_action()
        elif gesture == "is_dislike":
            return self._dislike_gesture_action()
        elif gesture == "is_stop":
            return self._stop_gesture_action()
        elif gesture == "is_okay":
            return self._okay_gesture_action()
        else:
            return None

    def _like_gesture_action(self):
        subprocess.run(["open", "-a", "Photos"])
        return "👍"

    def _dislike_gesture_action(self):
        subprocess.run(["open", "-a", "Notes"])
        return "👎"

    def _stop_gesture_action(self):
        subprocess.run(["open", "-a", "Calendar"])
        return "✋"

    def _okay_gesture_action(self):
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = os.path.expanduser(f"~/Desktop/screenshot_{timestamp}.png")
        subprocess.run(["screencapture", "-x", screenshot_path])
        return "👌"
