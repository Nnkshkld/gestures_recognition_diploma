import subprocess


class TwoHandsActions:
    def __init__(self):
        self.both_hands_detected = False
        self.previous_gesture = None
        self.gesture_count = 0

    def get_action(self, gesture):
        print(f"Known: {gesture}")
        if gesture == "is_two_stops":
            return self._two_stop_gesture_action()
        else:
            return None

    def _two_stop_gesture_action(self):
        apps = subprocess.check_output(
            ["osascript", "-e", 'tell application "System Events" to get name of (processes where background only is false)']
        ).decode().strip().split(", ")

        for app in apps:
            subprocess.run(["osascript", "-e", f'tell application "{app}" to quit'])

        return "🤲"
