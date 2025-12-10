import time
import sys
from puzzle_generator import PuzzleGenerator
from tracker import PerformanceTracker
from adaptive_engine import AdaptiveEngine

def main():
    print("Welcome to Math Adventures! 🚀")
    name = input("Enter your name: ")
    print(f"Hello, {name}! Let's do some math.")

    # Initialize components
    generator = PuzzleGenerator()
    tracker = PerformanceTracker()
    engine = AdaptiveEngine()

    # Initial difficulty selection
    while True:
        level = input("Choose starting difficulty (Easy, Medium, Hard): ").strip().capitalize()
        if level in ['Easy', 'Medium', 'Hard']:
            engine.set_initial_difficulty(level)
            break
        print("Invalid choice. Please type Easy, Medium, or Hard.")

    print(f"\nStarting at {engine.get_current_difficulty()} level. Type 'exit' to quit anytime.\n")

    # Game Loop
    while True:
        current_difficulty = engine.get_current_difficulty()
        puzzle = generator.generate_puzzle(current_difficulty)
        
        print(f"Question: {puzzle['question']}")
        
        start_time = time.time()
        user_input = input("Answer: ").strip()
        end_time = time.time()
        
        if user_input.lower() in ['exit', 'quit']:
            break
            
        time_taken = end_time - start_time
        
        try:
            # Handle division which might return float, but we expect int inputs usually if int result
            # For simplicity in this prototype, we'll try evaluating.
            user_val = float(user_input)
            correct_val = float(puzzle['answer'])
            
            # Allow small tolerance for division or just strict equality
            is_correct = abs(user_val - correct_val) < 0.01
            
        except ValueError:
            print("Please enter a valid number.")
            continue
            
        if is_correct:
            print(f"✅ Correct! ({time_taken:.2f}s)")
        else:
            print(f"❌ Incorrect. The answer was {puzzle['answer']}.")
            
        tracker.log_result(puzzle, user_val, is_correct, time_taken)
        engine.update_difficulty(tracker)
        print("-" * 20)

    # Summary
    stats = tracker.get_session_stats()
    print("\n" + "="*30)
    print(f"Session Summary for {name}")
    print("="*30)
    print(f"Total Questions: {stats['total_questions']}")
    print(f"Correct Answers: {stats['correct_count']}")
    print(f"Accuracy:        {stats['accuracy']:.1f}%")
    print(f"Avg Time per Q:  {stats['avg_time']:.2f}s")
    print(f"Final Level:     {engine.get_current_difficulty()}")
    print("="*30)
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
