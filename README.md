# Weekly Code Jam Challenge — Rules and Specifications

## General Guidelines

Participants in the weekly coding challenge must adhere to the following rules to ensure fairness, integrity, and code quality.

### 1. **Code of Conduct**

* **No use of AI tools** during the implementation phase. This includes, but is not limited to:

  * ChatGPT
  * GitHub Copilot
* **All code must be original** and written from scratch during the challenge week.
* Any violation of these rules will result in disqualification for that week's challenge.

### 2. **Code Requirements**

* Unless otherwise specified, all challenge solutions must run on the **latest stable version of Python** available at the start of the challenge week.
* **The default program entrypoint must be a file named `main.py` located in your submission directory**.
Your program will be executed by running `python main.py` from the terminal.
* **Every function must be formally documented**, clearly describing its purpose, parameters, and return value(s).
* Inline comments should be used as necessary to clarify implementation logic.
* The use of `eval()` or any equivalent dynamic code execution function is strictly prohibited in **all languages**. All parsing and computation must be implemented manually.
* **All code must be formatted** according to the official style guide of the language used. For Python, this means full compliance with [PEP 8](https://peps.python.org/pep-0008/).
* **All input/output must occur via the terminal** (stdin/stdout). Graphical interfaces (GUIs) are not permitted unless explicitly specified.
* The program must be robust and **handle all invalid or edge-case inputs gracefully** without crashing.
* Use only the standard library of the language unless otherwise specified. The use of third-party libraries that perform expression parsing, evaluation, or calculation is not allowed. In Python, for example, use of the built-in math module is allowed for operations like logarithms and exponentiation.

### 3. **Project Structure and Repository Rules**

* Submissions must be made via a **pull request to the repository [`benjitusk/weekly-code-jam`](https://github.com/benjitusk/weekly-code-jam)**.
* Each participant must place their submission under the relevant challenge directory using the following structure:

  ```
  /week_<week_number>_<challenge_name>/<your_github_username>/
  ```

  For example, for Week 1:

  ```
  /week_1_basic_calculator/johnDoe/
  ```
* The directory structure must adhere to the above format to ensure clarity and organization. **Submissions that do not match this structure will be removed**.
* Submissions must be included in the pull request **before the deadline**. Any commits pushed after the deadline will **disqualify** the submission, even if the pull request was opened on time.
* **Do not view or reference other participants’ repositories or pull requests** before the submission deadline. Code comparison and discussion will take place only after all submissions are frozen.
* After the deadline, each participant must add a `README.md` file in their submission directory to document their approach. This file:

  * Must clearly explain the logic and structure of the solution.
  * **May be written with the help of AI tools**.

### 4. **Submission and Review**

* The deadline for submission is **שבת קודש** of the specified week.
* Code review and comparison will begin **מוצאי שבת קודש** once all submissions are locked.

---

Best of luck to all participants. Submit excellent code and respect the process.

# Challenge List
1. [Basic Calculator](week_1_basic_calculator/README.md)
