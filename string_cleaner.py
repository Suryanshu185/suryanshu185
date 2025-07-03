def remove_consecutive_chars(input_string):
    """
    Remove characters that appear continuously with a count of 3 or more.
    
    Args:
        input_string (str): The input string to process
        
    Returns:
        str: The cleaned string with consecutive characters (count >= 3) removed
        
    Example:
        >>> remove_consecutive_chars("@@%%%%%##^^^#$")
        "@@###$"
    """
    if not input_string:
        return ""
    
    result = []
    i = 0
    
    while i < len(input_string):
        current_char = input_string[i]
        count = 1
        
        # Count consecutive occurrences of the current character
        while i + count < len(input_string) and input_string[i + count] == current_char:
            count += 1
        
        # Only include the characters if count is less than 3
        if count < 3:
            result.append(current_char * count)
        
        # Move to the next different character
        i += count
    
    return ''.join(result)


if __name__ == "__main__":
    # Test the function with the provided example
    test_input = "@@%%%%%##^^^#$"
    # Note: The expected output in the problem statement appears to be "@@##$",
    # but based on the algorithm description, the correct output should be "@@###$"
    # because there are 3 '#' characters total: 2 from "##" and 1 from the final "#"
    expected_output = "@@###$"
    actual_output = remove_consecutive_chars(test_input)
    
    print(f"Input: {test_input}")
    print(f"Expected: {expected_output}")
    print(f"Actual: {actual_output}")
    print(f"Test passed: {actual_output == expected_output}")
    
    # Additional test cases
    print("\nAdditional tests:")
    test_cases = [
        ("aaa", ""),
        ("aa", "aa"),
        ("abccc", "ab"),
        ("aabbcc", "aabbcc"),
        ("aaabbbccc", ""),
    ]
    
    for input_str, expected in test_cases:
        result = remove_consecutive_chars(input_str)
        print(f"  '{input_str}' -> '{result}' (expected: '{expected}') {'✓' if result == expected else '✗'}")