# Math Adventures - Adaptive Learning Prototype

A minimal adaptive math learning application that adjusts puzzle difficulty based on user performance.

## Design
The system consists of three main components:
1. **Puzzle Generator**: Creates math problems (Easy, Medium, Hard).
2. **Performance Tracker**: Logs user metrics (correctness, time).
3. **Adaptive Engine**: Adjusts difficulty based on recent performance rules.

## Features
- **3 Difficulty Levels**:
  - **Easy**: Single digit addition/subtraction.
  - **Medium**: Double digit add/sub, single digit multiplication.
  - **Hard**: Double digit multiplication, division.
- **Adaptive Logic**: Promotes to next level after 3 consecutive correct answers; demotes after 2 consecutive failures.
- **Session Summary**: Displays accuracy and performance trends at the end.

## How to Run
1. Ensure you have Python 3 installed.
2. Navigate to the project root.
3. Run the application:
   ```bash
   python src/main.py
   ```
4. Follow the on-screen prompts. type `exit` to finish the session.

## File Structure
- `src/main.py`: Entry point.
- `src/puzzle_generator.py`: Generates questions.
- `src/tracker.py`: Tracks stats.
- `src/adaptive_engine.py`: Manages difficulty state.
