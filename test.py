import unittest
from unittest.mock import patch, MagicMock
import main

class TestFetchPosts(unittest.TestCase):
    @patch("main.requests.get")
    def TestFetchPostsSuccess(self, mock_get):
        #Tests that the fetch_posts function makes the correct API call
        #Verifies the function returns a list of posts

    @patch("main.requests.get")
    def TestFetchPostsFailure(self, mock_get):
        #Test for the fetchPosts function to check it handles API errors gracefully

class TestFetchComments(unittest.TestCase):
    @patch("main.requests.get")
    def TestFetchCommentsSuccess(self, mock_get):
        #Verifies that the API is called with the correct post_id
        #Ensures that the function returns a list of comments

    @patch("main.requests.get")
    def TestFetchCommentsFailure(self, mock_get):
        #Tests for the fetchComments function to check it handles if the post doesn't exist or API fails, gracefully

class TestAddComment(unittest.TestCase):
@patch("main.requests.get")
    def TestAddCommentsSuccess(self, mock_get):
        #Tests whether the API is called with the correct payload
        #Verifies that the response contains the posted comment

    @patch("main.requests.get")
    def TestFetchCommentsFailure(self, mock_get):
        #Tests error handling if the API rejects the comment

class TestRandomPosts(unittest.TestCase):
    @patch("main.requests.get")
    def TestRandomPosts(self, mock_get):
        #Verfify 10 posts are returned when there are more than 10 available
        #Tests behavior when fewer than 10 posts exist

class TestViewPosts(unittest.TestCase):
    def TestSelectPostValid(self):
        #Test the selected post's details are displayed correctly

    def TestSelectPostInvalid(self):
    #Verify handling of invalid post selections

###BONUS FEATURE TESTS###

class TestFetchUserPosts(unittest.TestCase):
    @patch("main.requests.get")
    def TestFetchUserPostsSuccess(self, mock_get):
        #Tests that the function feteches posts for the correct userId

    @patch("main.requests.get")
    def TestFetchUserPostsFailure(self, mock_get):
        #Handles cases where no posts exist for a user

class TestSearchPosts(unittest.TestCase):
    def TestSearchPostsWithResults(self):
        #Tests that the searchPosts function correctly filters posts based on the provided keyword
        
    def TestSearchPostsNoResults(self):
        #Test that it gracefully handles where no posts match the keyword

###Tests for CLI interactions###
class TestCLIInterations(unittest.TestCase):
    @patch("builtin.input", side_effect=["1"])
    def TestPostSelectionValid(self, mock_input):
        #Test that the valid inputs are accepted and return the correct post

    @patch("builtin.input", side_effect=["999"])
    def TestPostSelectionInvalid(self, mock_input):
        #Test invalid inputs prompt an error messsage
    
    @path("builtin.input", side_effect=["Python"])
    def TestSearchPostsCLI(self, mock_input):
        #Checks if the search results are correctly printed or not