# streak.py

def longest_positive_streak(numbers):
    """
    Find the length of the longest consecutive streak of positive numbers.
    
    Args:
        numbers: A list of numbers
        
    Returns:
        int: Length of the longest positive streak
    """
    if not numbers:
        return 0
    
    max_streak = 0
    current_streak = 0
    
    for num in numbers:
        if num > 0:
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 0
    
    return max_streak
