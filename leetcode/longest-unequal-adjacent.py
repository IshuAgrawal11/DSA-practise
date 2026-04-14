def getLongestSubsequence(words: list[str], groups: list[int]) -> list[str]:
    # If there are no words, return an empty list
    if not words:
        return []
    
    # Initialize the result with the first word
    result = [words[0]]
    # Keep track of the 'group' value of the last word added
    last_group = groups[0]
    
    # Start from the second element (index 1)
    for i in range(1, len(words)):
        # If the current group is different from the last added group
        if groups[i] != last_group:
            result.append(words[i])
            # Update the last_group tracker
            last_group = groups[i]
            
    return result

words = ["a", "b", "c", "d", "e"]
groups = [1, 2, 2, 3, 3]
print(getLongestSubsequence(words, groups))