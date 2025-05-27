# Import TestCase for creating test classes and Client for making test requests
from django.test import TestCase,Client
# Import get_user_model to access the active User model (custom or default)
from django.contrib.auth import get_user_model
# Import reverse to generate URLs from URL patterns for testing endpoints
from django.urls import reverse
# Import the Post model to test its functionality and behavior
from .models import Post

class BlogTest(TestCase):
    def setUp(self) -> None:
        # Create a test user with specific credentials for authentication testing
        # This user will be used across all test methods in this class
        self.user = get_user_model().objects.create_user(
        username='testuser',  # Username for the test user
        email='test@email.com',  # Email for the test user
        password='secret'  # Password for the test user
        )

        # Create a test post instance with sample data
        # This post will be used across all test methods in this class
        self.post = Post.objects.create(
            title="A good title",  # Sample title for the test post
            body='Nice body content',  # Sample content for the test post
            author=self.user,  # Associate the post with the test user
        )

    # Test the string representation method of the Post model
    def test_string_representation(self):
        # Create a new post instance with a sample title
        post = Post(title='A sample title')
        # Verify that the string representation of the post matches its title
        self.assertEqual(str(post),post.title)

    # Test the content and attributes of the created post
    def test_post_content(self):
        # Verify the post title matches the expected value
        self.assertEqual(f'{self.post.title}','A good title')
        # Verify the post author's username matches the expected value
        self.assertEqual(f'{self.post.author}','testuser')
        # Verify the post body content matches the expected value
        self.assertEqual(f'{self.post.body}','Nice body content')

    # Test the functionality of the post list view
    def test_post_list_view(self):
        # Make a GET request to the home page using the URL name
        response = self.client.get(reverse('home'))
        # Verify the response status code is 200 (OK)
        self.assertEqual(response.status_code,200)
        # Verify the response contains the expected post content
        self.assertContains(response,'Nice body content')
        # Verify the correct template is being used to render the response
        self.assertTemplateUsed(response,'home.html')

    # Test the functionality of the post detail view
    def test_post_detail_view(self):
        # Test with a valid post ID (ǐ)
        response = self.client.get('/post/1/')
        # Test with an invalid post ID (100000)
        no_response = self.client.get('/post/100000/')
        # Verify the valid post request returns 200 status code
        self.assertEqual(response.status_code, 200)
        # Verify the invalid post request returns 404 status code
        self.assertEqual(no_response.status_code, 404)
        # Verify the response contains the expected post content
        self.assertContains(response, 'Nice body content')
        # Verify the correct template is being used to render the response
        self.assertTemplateUsed(response, 'post_detail.html')
    
    def test_get_absolute_url(self):
            # Test that the get_absolute_url method returns the correct URL for the post
            # We know it's a Post object because it was created in setUp with Post.objects.create()
        self.assertEqual(self.post.get_absolute_url(), '/post/1/')
        
    def test_post_create_view(self):

            response= self.client.post(reverse('post_new'),{
                'title':'New title',
                'body':'New text',
                'author':self.user,
            })

            self.assertEqual(response.status_code,200)
            self.assertContains(response,'New title')
            self.assertContains(response,'New text')
        
    def test_post_update_view(self):
        self.client.login(username='testuser', password='secret')
        
        response = self.client.post(reverse('post_edit', args='1'), {
            'title': 'Updated title',
            'body': 'Updated text',
        })
        
        self.assertEqual(response.status_code, 302)
        # Check if redirected to the detail page
        self.assertRedirects(response, '/post/1/')
        # Fetch the updated post and verify its content
        updated_post = Post.objects.get(id=1)
        self.assertEqual(updated_post.title, 'Updated title')
        self.assertEqual(updated_post.body, 'Updated text')

    def test_post_delete_view(self):
        response = self.client.post(reverse('post_delete',args='1'))
        self.assertEqual(response.status_code, 302)
        # Check if redirected to the home page
        self.assertRedirects(response, '/')
        # Verify the post was deleted
        self.assertEqual(Post.objects.count(), 0)
    
    
    

        