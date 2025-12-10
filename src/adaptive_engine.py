class AdaptiveEngine:
    def __init__(self):
        self.difficulty_levels = ['Easy', 'Medium', 'Hard']
        self.current_difficulty_index = 0  # Start at Easy by default

    def set_initial_difficulty(self, difficulty):
        if difficulty in self.difficulty_levels:
            self.current_difficulty_index = self.difficulty_levels.index(difficulty)

    def get_current_difficulty(self):
        return self.difficulty_levels[self.current_difficulty_index]

    def update_difficulty(self, tracker):
        """
        Adjusts difficulty based on recent performance logic.
        Rule:
        - Last 3 correct -> Increase difficulty
        - Last 2 incorrect -> Decrease difficulty
        """
        recent = tracker.get_recent_results(3)
        
        if not recent:
            return

        # Check for increase
        if len(recent) >= 3:
            if all(r['is_correct'] for r in recent):
                self._increase_difficulty()
                return

        # Check for decrease
        # Look at the last 2 specifically
        last_two = recent[-2:]
        if len(last_two) >= 2:
            if all(not r['is_correct'] for r in last_two):
                self._decrease_difficulty()

    def _increase_difficulty(self):
        if self.current_difficulty_index < len(self.difficulty_levels) - 1:
            self.current_difficulty_index += 1
            print(f"\n[Adaptive Engine] Promoting to {self.get_current_difficulty()} level! Great job!")

    def _decrease_difficulty(self):
        if self.current_difficulty_index > 0:
            self.current_difficulty_index -= 1
            print(f"\n[Adaptive Engine] Easing up to {self.get_current_difficulty()} level. Let's practice more.")
