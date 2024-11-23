import requests
import random

# Function to fetch posts from an API
def fetchPosts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

# Function to fetch comments for a specific post
def fetchComments(post_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments")
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

# Function to add a comment to a specific post
def addComment(post_id, name, email, body):
    data = {
        "postId": post_id,
        "name": name,
        "email": email,
        "body": body
    }
    response = requests.post("https://jsonplaceholder.typicode.com/comments", json=data)
    if response.status_code != 201:
        response.raise_for_status()
    return response.json()

# Function to get 10 random posts
def randomPosts():
    posts = fetchPosts()
    return random.sample(posts, 10) if len(posts) > 10 else posts

# Function to select a post by ID
def selectPost(post_id, posts):
    for post in posts:
        if post["id"] == post_id:
            return post
    raise ValueError("Post not found")

# Function to fetch posts by a specific user
def fetchUserPosts(user_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}/posts")
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

# Function to search posts by keyword
def searchPosts(posts, keyword):
    return [post for post in posts if keyword.lower() in post["title"].lower() or keyword.lower() in post["body"].lower()]

# Function to select a post by input ID
def selectPostFromInput(posts):
    post_id = int(input("Select a post by ID: "))
    return selectPost(post_id, posts)

# Main function to display menu and handle user choices
def main():
    while True:
        print("\nMenu:")
        print("1: List 10 random posts.")
        print("2: View a post (you can choose which post by ID).")
        print("3: Search posts by keyword.")
        print("4: View comments for a post.")
        print("5: Add a comment to a post.")
        print("6: Fetch posts by a specific user.")
        print("7: Exit.")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            posts = randomPosts()  # Fetch and display 10 random posts
            for post in posts:
                print(f"- {post['title']} (Post ID: {post['id']})")
        elif choice == "2":
            posts = fetchPosts()  # Fetch all posts
            post_id = int(input("Enter the post ID: "))
            try:
                selected_post = selectPost(post_id, posts)  # Select and display post by ID
                print(f"Title: {selected_post['title']}\nBody: {selected_post['body']}")
            except ValueError as e:
                print(e)  # Print error if post not found
        elif choice == "3":
            posts = fetchPosts()  # Fetch all posts
            keyword = input("Enter a keyword to search posts: ")
            search_results = searchPosts(posts, keyword)  # Search posts by keyword
            print("Search Results:")  # Display search results
            if search_results:
                for post in search_results:
                    print(f"- {post['title']} (Post ID: {post['id']})")
            else:
                print("No posts found matching that keyword.")
        elif choice == "4":
            post_id = int(input("Enter the post ID to view comments: "))
            try:
                comments = fetchComments(post_id)  # Fetch and display comments for a specific post
                for comment in comments:
                    print(f"- {comment['body']} (Comment ID: {comment['id']})")
            except requests.exceptions.HTTPError as e:
                print(e)  # Print error if fetching comments fails
        elif choice == "5":
            post_id = int(input("Enter the post ID to add a comment: "))
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            body = input("Enter your comment: ")
            try:
                comment = addComment(post_id, name, email, body)  # Add a comment to a post
                print(f"Comment added with ID: {comment['id']}")
            except requests.exceptions.HTTPError as e:
                print(e)  # Print error if adding comment fails
        elif choice == "6":
            user_id = int(input("Enter the user ID to fetch posts: "))
            try:
                user_posts = fetchUserPosts(user_id)  # Fetch and display posts by a specific user
                for post in user_posts:
                    print(f"- {post['title']} (Post ID: {post['id']})")
            except requests.exceptions.HTTPError as e:
                print(e)  # Print error if fetching user posts fails
        elif choice == "7":
            print("Goodbye!")
            break  # Exit the loop and end the program
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()  # Run the main function if the script is executed directly