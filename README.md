
---

# Catherine Weightman Blog CLI Application

## Overview

This is a simple Python CLI application that interacts with the **JSONPlaceholder API**. The application allows users to:
1. Fetch a list of random posts.
2. View individual posts.
3. View and post comments on specific posts.
4. Search for posts by a keyword.

The application is built using **requests** for API communication, and it's structured with **Test-Driven Development (TDD)** principles.

---

## Features

- **List 10 random posts** from the API.
- **View individual posts** and their details.
- **View comments** associated with a post.
- **Post a comment** to a post (simulated by the API).
- **BONUS FEATURE- Search for posts** by a keyword in the title or body.
- **BONUS FEATURE- Select to show posts** by a specific user.

---

## Installation

### Prerequisites

- Python 3.6+
- `requests` library for making HTTP requests.

You can install the required dependencies by running the following command in your bash terminal:

```bash
pip install -r requirements.txt
```

---

## Usage

To run the application:

1. **Run the CLI Application**:
   ```bash
   python main.py
   ```

   The application will display a menu with options:
   - **1**: List 10 random posts.
   - **2**: View a post (you can choose which post by ID).
   - **3**: Search posts by keyword.
   - **4**: View comments for a post.
   - **5**: Add a comment to a post.
   - **6**: Fetch posts by a specific user.
   - **7**: Exit.

2. **Follow the instructions** in the terminal for interacting with posts and comments.

---

## Testing

This project follows **Test-Driven Development (TDD)**. The tests are writtten using the Python `unittest` framework.

### Running Tests

To run all the tests, use the following command:

```bash
python -m unittest discover
```

This will automatically find and run all tests defined in files that match the pattern `test_*.py`.

You can also run tests individually by specifying the test file or class. For example:

```bash
python -m unittest test_main.TestFetchPosts
```

---

## Project Structure

```
/posts-application
│
├── main.py              # Main CLI application logic
├── test.py              # Unit tests for the application
├── requirements.txt     # Required dependencies
└── README.md            # Project documentation
```

- **`main.py`** contains the logic for fetching posts, comments, and interacting with the user through the command-line interface.
- **`test.py`** contains unit tests that ensure the functionality of each feature, following TDD principles.

---

## Features

### **List Random Posts**

The user can view 10 random posts. The posts are fetched from the API, and random 10 are displayed each time.

### **View Individual Post**

The user can select a post (by ID) to view its full details, including the title and body.

### **View and Post Comments**

Users can view comments associated with a particular post. Additionally, they can simulate posting their own comment, which is then sent to the API.

### **Search Posts by Keyword**

Users can search posts by a keyword. The application will filter posts whose title or body contains the keyword and display them.

---

## Additional Features

- **Error Handling**: The application handles HTTP errors, such as 404 and 500 errors, gracefully and provides feedback to the user.
- **Test Coverage**: The code has full unit test coverage which ensures that the application's features work as expected.

---

## Conclusion

- This project provides a simple and interactive way to work with the **JSONPlaceholder API**.
- The application also follows best practices, including test-driven development which ensures reliability.
- If I were to add to this project in the future I would think about potentially adding functionality that lets user's create posts.

---