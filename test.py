import unittest
from unittest.mock import patch, MagicMock
import requests
import main
import random

class TestFetchPosts(unittest.TestCase):
    @patch("requests.get")
    def test_fetch_posts_success(self, mock_get):
        #Tests that the fetch_posts function makes the correct API call
        #Verifies the function returns a list of posts
        mock_get.return_value = MagicMock(
            status_code=200, 
            json=lambda: [{"id": 1, "title": "Post 1"}, {"id": 2, "title": "Post 2"}]
        )
        posts = main.fetchPosts() # Call the function to fetch posts
        self.assertEqual(len(posts), 2) # Verify two posts are returned
        self.assertEqual(posts[0]["title"], "Post 1") # Ensure the title of the first post is correct

    @patch("requests.get")
    def test_fetch_posts_failure(self, mock_get):
        #Test for the fetchPosts function to check it handles API errors gracefully
        mock_get.return_value = MagicMock(status_code=500) # Mock server error
        mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError # Ensure the function raises an HTTPError
        with self.assertRaises(requests.exceptions.HTTPError):
            main.fetchPosts()

class TestFetchComments(unittest.TestCase):
    @patch("requests.get")
    def test_fetch_comments_success(self, mock_get):
        #Verifies that the API is called with the correct post_id
        #Ensures that the function returns a list of comments
        mock_get.return_value = MagicMock(
            status_code=200, 
            json=lambda: [{"postId": 1, "id": 1, "body": "Comment 1"}]
        )
        comments = main.fetchComments(1) # Fetch comments for post with ID 1
        self.assertEqual(len(comments), 1) # Verify one comment is returned
        self.assertEqual(comments[0]["body"], "Comment 1") # Ensure the body of the comment is correct

    @patch("requests.get")
    def test_fetch_comments_failure(self, mock_get):
        #Tests for the fetchComments function to check it handles if the post doesn't exist or API fails, gracefully
        mock_get.return_value = MagicMock(status_code=400) # Mock post not found error
        mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError # Ensure the function raises an HTTPError
        with self.assertRaises(requests.exceptions.HTTPError):
            main.fetchComments(1) # Attempt to fetch comments for a non-existent post

class TestAddComment(unittest.TestCase):
    @patch("requests.post")
    def test_add_comment_success(self, mock_post):
        #Tests whether the API is called with the correct payload
        #Verifies that the response contains the posted comment
        mock_post.return_value = MagicMock(
            status_code=201, 
            json=lambda: {"postId": 1, "id": 101, "name": "My Comment"}
        )
        comment = main.addComment(1, "Test Name", "test@example.com", "Great post!")
        self.assertEqual(comment["id"], 101)  # Ensure the comment ID matches
        self.assertEqual(comment["name"], "My Comment") # Ensure the comment name matches

    @patch("requests.post")
    def test_fetch_comment_failure(self, mock_post):
        #Tests error handling if the API rejects the comment
        mock_post.return_value = MagicMock(status_code=400) # Mock bad request error
        mock_post.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError("Mocked error")
        
        with self.assertRaises(requests.exceptions.HTTPError): # Ensure the function raises an HTTPError
            main.addComment(1, "Test Name", "test@example.com", "Great post!")
        
        mock_post.return_value.raise_for_status.assert_called_once()

class TestRandomPosts(unittest.TestCase):
    @patch("main.fetchPosts")
    def test_random_posts(self, mock_fetch_posts):
        #Verfify 10 posts are returned when there are more than 10 available
        #Tests behavior when fewer than 10 posts exist
        mock_fetch_posts.return_value = [{"id": i, "title": f"Post {i}"} for i in range(15)] # Mock 15 posts
        random_posts = random.sample(main.fetchPosts(), 10) # Select 10 random posts
        self.assertEqual(len(random_posts), 10) # Ensure 10 posts are selected
        self.assertTrue(all(post in mock_fetch_posts.return_value for post in random_posts)) # Ensure all posts are from the available ones

class TestViewPosts(unittest.TestCase):
    def test_select_post_valid(self):
        #Test the selected post's details are displayed correctly
        posts = [{"id": 1, "title": "Post 1", "body": "Body 1"}]
        selected_post = main.selectPost(1, posts) # Select post with ID 1
        self.assertEqual(selected_post["title"], "Post 1") # Ensure the correct post is selected

    def test_select_post_invalid(self):
        # Test that an invalid post selection raises an error
        posts = [{"id": 1, "title": "Post 1", "body": "Body 1"}]
        with self.assertRaises(ValueError): # Ensure the function raises an error for invalid selection
            main.selectPost(999, posts)

###BONUS FEATURE TESTS###

class TestFetchUserPosts(unittest.TestCase):
    @patch("requests.get")
    def test_fetch_user_posts_success(self, mock_get):
        # Test that fetch_User_Posts returns posts for a given userr
        mock_get.return_value = MagicMock(
            status_code=200, 
            json=lambda: [{"userId": 1, "id": 1, "title": "User Post"}]
        )
        user_posts = main.fetchUserPosts(1)
        self.assertEqual(len(user_posts), 1) # Verify one post is returned
        self.assertEqual(user_posts[0]["userId"], 1) # Ensure the userId matches

    @patch("requests.get")
    def test_fetch_posts_failure(self, mock_get):
        #Handles cases where no posts exist for a user
        mock_get.return_value = MagicMock(status_code=500) # Mock post not found error
        mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError # Ensure the function raises an HTTPError
        with self.assertRaises(requests.exceptions.HTTPError):
            main.fetchPosts()

class TestSearchPosts(unittest.TestCase):
    def test_search_posts_with_results(self):
        # Test that searchPosts correctly filters posts based on a keyword
        posts = [
            {"id": 1, "title": "Learn Python", "body": "Python is great!"},
            {"id": 2, "title": "Learn JavaScript", "body": "JavaScript is versatile."},
        ]
        results = main.searchPosts(posts, "Python") # Search for posts with the keyword 'Python'
        self.assertEqual(len(results), 1) # Verify one result is found
        self.assertEqual(results[0]["title"], "Learn Python") # Ensure the correct post is returned

    def test_search_posts_no_results(self):
        #Test that it gracefully handles where no posts match the keyword
        posts = [
            {"id": 1, "title": "Learn Python", "body": "Python is great!"},
            {"id": 2, "title": "Learn JavaScript", "body": "JavaScript is versatile."},
        ]
        results = main.searchPosts(posts, "Ruby") # Search for posts with the keyword 'Ruby'
        self.assertEqual(len(results), 0) # Ensure no results are returned

###Tests for CLI interactions###

class TestCLIInterations(unittest.TestCase):
    @patch("builtins.input", side_effect=["1"])
    def test_post_selection_valid(self, mock_input):
        #Test that the valid inputs are accepted and return the correct post
        posts = [{"id": 1, "title": "Post 1", "body": "Body 1"}]
        selected_post = main.selectPostFromInput(posts)
        self.assertEqual(selected_post["id"], 1) # Ensure the correct post is selected

    @patch("builtins.input", side_effect=["999"])
    def test_post_selection_invalid(self, mock_input):
        #Test invalid inputs prompt an error messsage
        posts = [{"id": 1, "title": "Post 1", "body": "Body 1"}]
        with self.assertRaises(ValueError):
            main.selectPostFromInput(posts) # Ensure the function raises an error for invalid selection

    @patch("builtins.input", side_effect=["3", "Python", "7"])  # Add more inputs if there are more interactions
    def test_search_posts_cli(self, mock_input):
        # Test that the correct search results are printed to the console
        posts = [
            {"id": 1, "title": "Learn Python", "body": "Python is great!"},
            {"id": 2, "title": "Learn JavaScript", "body": "JavaScript is versatile."}
        ]
        # Mock the fetch_posts function to return sample posts
        with patch("main.fetchPosts", return_value=posts):
            with patch("builtins.print") as mock_print:
                main.main()  # Run the main function that simulates user interaction
                # Check if the correct search results are printed
                mock_print.assert_any_call("Search Results:")  # Check if the results header is printed
                mock_print.assert_any_call("- Learn Python (Post ID: 1)")  # Check if the correct post is printed

                
if __name__ == "__main__":
    unittest.main()
