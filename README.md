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
    * I recommend the Visual Studio Code extension [autopep8](https://marketplace.visualstudio.com/items?itemName=ms-python.autopep8).
* **All input/output must occur via the terminal** (stdin/stdout). Graphical interfaces (GUIs) are not permitted unless explicitly specified.
* The program must be robust and **handle all invalid or edge-case inputs gracefully** without crashing.
* Use only the standard library of the language unless otherwise specified. The use of third-party libraries that perform expression parsing, evaluation, or calculation is not allowed. In Python, for example, use of the built-in math module is allowed for operations like logarithms and exponentiation.

### 3. **Project Structure and Repository Rules**

* Submissions must be made via a **pull request to the repository [`benjitusk-weekly-code-jam/submissions`](https://github.com/benjitusk-weekly-code-jam/submissions)**.
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


## How to Submit Your Solution (Fork & Pull Request)

If you're new to GitHub, follow these steps to submit your solution properly:

### 1. **Fork This Repository**

* Navigate to the main repository: [`benjitusk-weekly-code-jam/submissions`](https://github.com/benjitusk-weekly-code-jam/submissions).
* Click the **“Fork”** button (top-right corner). This will create a personal copy of the repository under your GitHub account.

### 2. **Clone Your Fork Locally**

Use Git to clone your forked repository to your computer:

```bash
git clone https://github.com/<your_github_username>/weekly-code-jam.git
cd weekly-code-jam
```

Alternatively, you can use Visual Studio Code or any other IDE to clone the repository. If you're unfamiliar with how to do this, a quick search for "how to clone a GitHub repository in [your IDE]" should provide you with the necessary instructions.

### 3. **Create Your Submission Folder**

* Navigate to the current challenge directory (e.g., `week_1_basic_calculator/`)

* Add your code files inside this folder. Unless otherwise specified, your program must start from a file named `main.py`.

### 4. **Commit and Push**

Add, commit, and push your code:

```bash
git add .
git commit -m "Add solution for basic_calculator challenge"
git push origin main
```

Alternatively, you can use your IDE's built-in Git features to stage, commit, and push your changes. If you're unsure how to do this, a quick search for "how to commit and push in [your IDE]" should provide you with the necessary instructions.

### 5. **Open a Pull Request**

* Go to your fork on GitHub.
* You should see button labeled **“Contribute”**, click it and then select **“Open pull request.”**
* Ensure the **base repository** is `benjitusk-weekly-code-jam/submissions` and the **base branch** is `main`.
* In the PR description, include your GitHub username and a brief description of your approach.

---

Best of luck to all participants. Submit excellent code and respect the process.

# Challenge List
1. [Basic Calculator](week_1_basic_calculator/README.md)
