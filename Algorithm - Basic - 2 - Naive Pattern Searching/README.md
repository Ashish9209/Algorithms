# Naive Pattern Searching Algorithm

The naive pattern searching algorithm is called "naive" because it is the simplest way to tackle the problem of finding a specific pattern (such as a word) in a text.

## Components of Pattern Searching

Pattern searching requires two base components:

- **Text:** The string to scan.
- **Pattern:** The substring to search for.

## Worst-Case Performance

The worst-case performance of the naive pattern searching algorithm is \( O(nk) \), where \( n \) is the length of the text and \( k \) is the length of the pattern. In some cases, this can approach \( O(n^2) \).

## Algorithm Description

1. **Initialization:**
   - The algorithm begins by iterating through the text and setting a variable `match_count` equal to 0.

2. **Pattern Checking:**
   - For each index in the text, the algorithm iterates through the pattern to check for matching characters.
   - If a match is found, `match_count` is incremented.
   - If a mismatch occurs, the search breaks out of the pattern iteration and moves to the next index in the text.

3. **Match Verification:**
   - After completing the pattern iteration, `match_count` is compared to the length of the pattern to determine if a complete match is found.

This method is straightforward but can be inefficient for large texts or patterns due to its potential quadratic time complexity.
