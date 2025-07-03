import sys
sys.path.append('/home/runner/work/suryanshu185/suryanshu185')
from string_cleaner import remove_consecutive_chars

def test_remove_consecutive_chars():
    """Test the remove_consecutive_chars function with various inputs."""
    
    test_cases = [
        # Test case from problem statement
        {
            'input': '@@%%%%%##^^^#$',
            'expected': '@@###$',  # Based on my analysis
            'description': 'Problem statement example'
        },
        # Simple test cases
        {
            'input': 'aaa',
            'expected': '',
            'description': 'Remove exactly 3 consecutive characters'
        },
        {
            'input': 'aa',
            'expected': 'aa',
            'description': 'Keep 2 consecutive characters'
        },
        {
            'input': 'aaaa',
            'expected': '',
            'description': 'Remove 4 consecutive characters'
        },
        {
            'input': 'abccc',
            'expected': 'ab',
            'description': 'Keep different chars, remove 3 consecutive'
        },
        {
            'input': 'aabbcc',
            'expected': 'aabbcc',
            'description': 'Keep all pairs'
        },
        {
            'input': 'aaabbbccc',
            'expected': '',
            'description': 'Remove all groups of 3'
        },
        {
            'input': 'aabbcccddd',
            'expected': 'aabb',
            'description': 'Keep pairs, remove groups of 3 and 4'
        },
        {
            'input': 'abcdefg',
            'expected': 'abcdefg',
            'description': 'Keep all single characters'
        },
        {
            'input': '',
            'expected': '',
            'description': 'Empty string'
        },
        {
            'input': 'a',
            'expected': 'a',
            'description': 'Single character'
        },
        {
            'input': '111222333444',
            'expected': '',
            'description': 'Mixed numbers - all groups have count >= 3, so remove all'
        }
    ]
    
    print("Testing remove_consecutive_chars function:")
    print("=" * 60)
    
    all_passed = True
    
    for i, test_case in enumerate(test_cases, 1):
        actual = remove_consecutive_chars(test_case['input'])
        passed = actual == test_case['expected']
        status = "PASS" if passed else "FAIL"
        
        print(f"Test {i}: {test_case['description']}")
        print(f"  Input:    '{test_case['input']}'")
        print(f"  Expected: '{test_case['expected']}'")
        print(f"  Actual:   '{actual}'")
        print(f"  Status:   {status}")
        print()
        
        if not passed:
            all_passed = False
    
    print("=" * 60)
    print(f"Overall result: {'ALL TESTS PASSED' if all_passed else 'SOME TESTS FAILED'}")
    
    return all_passed

if __name__ == "__main__":
    test_remove_consecutive_chars()