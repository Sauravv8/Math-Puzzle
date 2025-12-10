import time

class PerformanceTracker:
    def __init__(self):
        # List of dicts: {question, user_answer, correct, time_taken, difficulty, timestamp}
        self.history = []

    def log_result(self, puzzle, user_answer, is_correct, time_taken):
        """Logs a single puzzle attempt."""
        entry = {
            'question': puzzle['question'],
            'correct_answer': puzzle['answer'],
            'user_answer': user_answer,
            'is_correct': is_correct,
            'time_taken': time_taken,
            'difficulty': puzzle['difficulty'],
            'timestamp': time.time()
        }
        self.history.append(entry)

    def get_recent_results(self, n=5):
        """Returns the last n results."""
        return self.history[-n:]

    def get_session_stats(self):
        """Calculates session statistics."""
        if not self.history:
            return {
                'total_questions': 0,
                'accuracy': 0.0,
                'avg_time': 0.0
            }
        
        total = len(self.history)
        correct_count = sum(1 for h in self.history if h['is_correct'])
        total_time = sum(h['time_taken'] for h in self.history)
        
        return {
            'total_questions': total,
            'accuracy': (correct_count / total) * 100,
            'avg_time': total_time / total,
            'correct_count': correct_count
        }
