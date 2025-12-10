import sys
import os

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from puzzle_generator import PuzzleGenerator
from tracker import PerformanceTracker
from adaptive_engine import AdaptiveEngine

def simulate_session():
    print("Running Verification Simulation...")
    
    generator = PuzzleGenerator()
    tracker = PerformanceTracker()
    engine = AdaptiveEngine()
    
    engine.set_initial_difficulty('Easy')
    print(f"Initial Level: {engine.get_current_difficulty()}") # Should be Easy
    
    # Simulate 3 correct answers to trigger promotion
    print("\nSimulating 3 correct answers...")
    for _ in range(3):
        diff = engine.get_current_difficulty()
        puzzle = generator.generate_puzzle(diff)
        print(f"[{diff}] Question: {puzzle['question']} -> Answering Correctly")
        tracker.log_result(puzzle, puzzle['answer'], True, 1.5)
        engine.update_difficulty(tracker)
        
    print(f"Current Level (should be Medium): {engine.get_current_difficulty()}")
    
    # Simulate 3 more correct answers to trigger promotion to Hard
    print("\nSimulating 3 more correct answers...")
    for _ in range(3):
        diff = engine.get_current_difficulty()
        puzzle = generator.generate_puzzle(diff)
        print(f"[{diff}] Question: {puzzle['question']} -> Answering Correctly")
        tracker.log_result(puzzle, puzzle['answer'], True, 1.5)
        engine.update_difficulty(tracker)

    print(f"Current Level (should be Hard): {engine.get_current_difficulty()}")
    
    # Simulate 2 incorrect answers to trigger demotion
    print("\nSimulating 2 incorrect answers...")
    for _ in range(2):
        diff = engine.get_current_difficulty()
        puzzle = generator.generate_puzzle(diff)
        print(f"[{diff}] Question: {puzzle['question']} -> Answering Incorrectly")
        tracker.log_result(puzzle, -999, False, 2.0)
        engine.update_difficulty(tracker)
        
    print(f"Current Level (should be Medium): {engine.get_current_difficulty()}")
    
    # Check stats
    stats = tracker.get_session_stats()
    print("\nStats Check:")
    print(stats)
    
    if stats['total_questions'] == 8 and stats['correct_count'] == 6:
        print("\nSUCCESS: Logic verified.")
    else:
        print("\nFAILURE: Stats do not match expected.")

if __name__ == "__main__":
    simulate_session()
