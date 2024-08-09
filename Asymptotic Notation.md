We use asymptotic notation to describe the runtime of a program. The three types of asymptotic notation are big Theta, big Omega, and big O.
We use big Theta (Θ) to describe the runtime if the runtime of the program is the same in every case.
The different common runtimes from fastest to slowest are: Θ(1), Θ(log N), Θ(N), Θ(N log N), Θ(N2), Θ(2N), Θ(N!).
We use big Omega (Ω) to describe the best-case running time of a program.
We use big O (O) to describe the worst-case running time of a program.
We typically describe a program’s running time in terms of big O.
When finding the runtime of a program with multiple steps, you can divide the program into different sections and add the runtimes of the various sections. You can then take the slowest runtime and use that runtime to describe the entire program.
When analyzing the runtime of a program, we care about which part of the program is the slowest.

Like with time complexity, space complexity denotes space growth in relation to the input size. It’s also important to note that space complexity usually refers to any additional space that will be needed, and doesn’t count the space of the input.

Space complexity is important to consider alongside time complexity when comparing data structures and algorithms


# Asymptotic Notation and Complexity Analysis

In algorithm analysis, we use asymptotic notation to describe the runtime of a program. There are three main types of asymptotic notation: Big Theta (Θ), Big Omega (Ω), and Big O (O).

## Asymptotic Notation Types

### Big Theta (Θ)
- **Purpose:** Describes the runtime of a program when the runtime is the same in every case.
- **Common Runtimes from Fastest to Slowest:**
  - Θ(1) - Constant time
  - Θ(log N) - Logarithmic time
  - Θ(N) - Linear time
  - Θ(N log N) - Linearithmic time
  - Θ(N²) - Quadratic time
  - Θ(2^N) - Exponential time
  - Θ(N!) - Factorial time

### Big Omega (Ω)
- **Purpose:** Describes the best-case running time of a program.

### Big O (O)
- **Purpose:** Describes the worst-case running time of a program.
- **Typical Use:** When evaluating and comparing the efficiency of algorithms, Big O notation is commonly used to describe the worst-case scenario.

## Analyzing Runtime

When analyzing the runtime of a program with multiple steps:
1. **Divide the Program:** Break down the program into different sections.
2. **Add Runtimes:** Calculate and sum the runtimes of various sections.
3. **Take the Slowest Runtime:** Use the slowest runtime to describe the entire program.

The runtime of a program is typically described in terms of the slowest part, as it has the most significant impact on overall performance.

## Space Complexity

Space complexity refers to the growth of space requirements in relation to the input size. It is important to consider the additional space needed by an algorithm, excluding the space for the input itself.

- **Importance:** Space complexity is as crucial as time complexity when comparing data structures and algorithms. It helps determine the efficiency of algorithms not only in terms of time but also in memory usage.

---

Understanding both time and space complexity helps in selecting the most efficient algorithms and data structures for your needs.



