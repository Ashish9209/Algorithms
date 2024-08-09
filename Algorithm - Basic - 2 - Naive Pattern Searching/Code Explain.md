Here’s a simple explanation of the `pattern_search` function:

### Purpose
The function `pattern_search` looks for a specific substring (`pattern`) within a larger string (`text`) and prints the starting index where the pattern is found.

### How It Works

1. **Print Inputs:**
   ```python
   print("Input Text:", text, "Input Pattern:", pattern)
   ```
   Displays the `text` and `pattern` that the function is using.

2. **Loop Through Text:**
   ```python
   for index in range(len(text)):
     print("Text Index:", index)
   ```
   Iterates over each position in the `text` where a match might start.

3. **Initialize Match Counter:**
   ```python
   match_count = 0
   ```
   Sets up a counter (`match_count`) to keep track of how many characters match between `pattern` and `text` starting at the current `index`.

4. **Compare Pattern to Text:**
   ```python
   for char in range(len(pattern)):
     print("Pattern Index:", char)
     if pattern[char] == text[index + char]:
       match_count += 1
     else:
       break
   ```
   Compares each character of the `pattern` to the corresponding character in `text` starting from the current `index`. 
   - If characters match, increment the `match_count`.
   - If a mismatch occurs, stop checking further characters for this starting index (`break`).

5. **Check for Full Match:**
   ```python
   if match_count == len(pattern):
     print(pattern, "found at index", index)
   ```
   If all characters of the `pattern` matched (`match_count` equals the length of `pattern`), print the index where the `pattern` starts in `text`.

### Summary
The function scans through `text`, comparing substrings to `pattern`. It prints the starting index of `pattern` in `text` whenever a complete match is found.