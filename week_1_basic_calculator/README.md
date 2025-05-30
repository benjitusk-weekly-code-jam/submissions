## Week 1 Challenge: Basic Calculator

### Objective

Implement a terminal-based calculator that supports the following operations:

$$
\text{Addition } (+), \\
\text{Subtraction } (-), \\
\text{Multiplication } (*), \\
\text{Division } (/), \\
\text{Modulus } (\%), \\
\text{Exponentiation } (^\wedge), \\
\text{Logarithm } (\log_b(x))
$$

### Directory Structure

Place your entire project in a subdirectory named after your GitHub username within the main challenge directory:

```
/week_1_basic_calculator/<your_github_username>/
```

For example:

```
/week_1_basic_calculator/johnDoe/
```

### Input Format

Your calculator must read a single expression from standard input. Valid examples include:

```
log_5(125)=
10^4=
1-30=
4/0=
24%7=
```

### Output Format

* The program must output only the computed result, without any additional prompts or formatting.
* Invalid inputs or undefined operations (e.g., division by zero) must return an appropriate error or warning message.
* Under no circumstances should the program crash during execution.

### Submission Deadline
The deadline for this challenge is **שבת פרשת נָשֹׂא**. All pull requests must be submitted and finalized **before candle lighting**. Any commits after that point will result in disqualification.

### Notes

* This week’s challenge only requires support for single-operation expressions.
* Parentheses are required only for logarithmic input in the form `log_b(x)=`.
* PEMDAS and multi-operator support will be added in future challenges.

---

## Deliverables Checklist

* [ ] Code written without AI tools or use of `eval()`.
* [ ] All functions documented with docstrings and explanatory comments.
* [ ] Terminal-only I/O.
* [ ] Full error and edge-case handling.
* [ ] Code formatted per official language standards (PEP 8 for Python).
* [ ] Add `README.md` explaining the solution.
* [ ] Project structured under `/week_1_basic_calculator/<github_username>/`.
* [ ] Pull request submitted to [`benjitusk/weekly-code-jam`](https://github.com/benjitusk/weekly-code-jam) before the deadline.
* [ ] No commits after the deadline.
