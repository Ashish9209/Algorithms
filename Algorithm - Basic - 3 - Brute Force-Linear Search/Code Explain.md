Break down and simplify the provided code:

### Code Explanation

1. **Define List and Target:**
   ```python
   recipe = ["nori", "tuna", "soy sauce", "sushi rice"]
   target_ingredient = "avocado"
   ```
   - `recipe` is a list of ingredients for a recipe.
   - `target_ingredient` is the ingredient you want to find in the `recipe` list.

2. **Define Linear Search Function:**
   ```python
   def linear_search(search_list, target_value):
     for idx in range(len(search_list)):
       if search_list[idx] == target_value:
         return idx
     raise ValueError("{0} not in list".format(target_value))
   ```
   This function searches for `target_value` in `search_list`:

   - **Loop Through List:**
     ```python
     for idx in range(len(search_list)):
     ```
     Iterates through each index (`idx`) in `search_list`.

   - **Check for Match:**
     ```python
     if search_list[idx] == target_value:
       return idx
     ```
     If the current element (`search_list[idx]`) matches `target_value`, it returns the index of the match.

   - **Handle Not Found Case:**
     ```python
     raise ValueError("{0} not in list".format(target_value))
     ```
     If the loop completes without finding the `target_value`, it raises an error indicating that the value is not in the list.

3. **Search and Print Result:**
   ```python
   print(linear_search(recipe, target_ingredient))
   ```
   Calls `linear_search` with `recipe` and `target_ingredient`. It prints the result (index of `target_ingredient` if found, or an error if not found).

### Summary

- The `linear_search` function checks each item in a list to find a specific value.
- It returns the index of the value if found.
- If the value is not found, it raises an error indicating that the value is not in the list.
- The provided code looks for `"avocado"` in the `recipe` list and prints the result. Since `"avocado"` is not in the list, it will raise and print an error.

