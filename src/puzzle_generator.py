import random
import operator

class PuzzleGenerator:
    def __init__(self):
        self.operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.floordiv  # Integer division for simplicity
        }

    def generate_puzzle(self, difficulty):
        """
        Generates a math puzzle based on difficulty level.
        Returns a dictionary with 'question', 'answer', and 'difficulty'.
        """
        if difficulty == 'Easy':
            return self._generate_easy()
        elif difficulty == 'Medium':
            return self._generate_medium()
        elif difficulty == 'Hard':
            return self._generate_hard()
        else:
            # Fallback to Easy
            return self._generate_easy()

    def _generate_easy(self):
        """Single digit addition and subtraction."""
        op_symbol = random.choice(['+', '-'])
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        
        # Ensure positive result for subtraction simplicity
        if op_symbol == '-' and a < b:
            a, b = b, a
            
        question = f"{a} {op_symbol} {b}"
        answer = self.operations[op_symbol](a, b)
        
        return {
            'question': question,
            'answer': answer,
            'difficulty': 'Easy'
        }

    def _generate_medium(self):
        """Double digit add/sub, single digit multiplication."""
        op_type = random.choice(['add_sub', 'mult'])
        
        if op_type == 'add_sub':
            op_symbol = random.choice(['+', '-'])
            a = random.randint(10, 50)
            b = random.randint(1, 40)
            if op_symbol == '-' and a < b:
                a, b = b, a
        else:
            op_symbol = '*'
            a = random.randint(2, 9)
            b = random.randint(2, 9)
            
        question = f"{a} {op_symbol} {b}"
        answer = self.operations[op_symbol](a, b)
        
        return {
            'question': question,
            'answer': answer,
            'difficulty': 'Medium'
        }

    def _generate_hard(self):
        """Double digit multiplication, simple division, mixed operations."""
        op_type = random.choice(['mult', 'div'])
        
        if op_type == 'mult':
            op_symbol = '*'
            a = random.randint(10, 20)
            b = random.randint(2, 9)
        else:
            # Division: ensure clean integer result
            op_symbol = '/'
            b = random.randint(2, 9)
            answer = random.randint(5, 15)
            a = b * answer # a / b = answer
            
        question = f"{a} {op_symbol} {b}"
        answer = self.operations[op_symbol](a, b)
        
        return {
            'question': question,
            'answer': answer,
            'difficulty': 'Hard'
        }
