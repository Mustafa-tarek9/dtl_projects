from django.shortcuts import render
from datetime import datetime

def blog_view(request):
    context = {
        'blog_title': 'My Developer Blog',
        'posts': [
            {
                'title': 'Getting Started with Django',
                'slug': 'getting-started-with-django',
                'content': 'Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design...',
                'author': 'John Doe',
                'publish_date': datetime(2024, 1, 15),
                'categories': ['Django', 'Python', 'Web Development'],
                'is_published': True,
                'comments_count': 8,
                'read_time': 5
            },
            {
                'title': 'CSS Grid Layout Mastery',
                'slug': 'css-grid-layout-mastery',
                'content': 'CSS Grid Layout is a powerful tool for creating complex responsive web design layouts...',
                'author': 'John Doe',
                'publish_date': datetime(2024, 2, 3),
                'categories': ['CSS', 'Frontend', 'Web Design'],
                'is_published': True,
                'comments_count': 12,
                'read_time': 7
            },
            {
                'title': 'Python Data Analysis with Pandas',
                'slug': 'python-data-analysis-pandas',
                'content': 'Pandas is an open-source data analysis and manipulation tool built on top of Python...',
                'author': 'Jane Smith',
                'publish_date': datetime(2024, 2, 20),
                'categories': ['Python', 'Data Science', 'Pandas'],
                'is_published': False,
                'comments_count': 3,
                'read_time': 10
            },
            {
                'title': 'Building REST APIs with Django REST Framework',
                'slug': 'building-rest-apis-drf',
                'content': 'Django REST Framework is a powerful and flexible toolkit for building Web APIs...',
                'author': 'John Doe',
                'publish_date': datetime(2024, 3, 5),
                'categories': ['Django', 'API', 'Backend'],
                'is_published': True,
                'comments_count': 15,
                'read_time': 8
            }
        ],
        'categories': [
            {'name': 'Django', 'post_count': 2},
            {'name': 'Python', 'post_count': 2},
            {'name': 'CSS', 'post_count': 1},
            {'name': 'Frontend', 'post_count': 1},
            {'name': 'Data Science', 'post_count': 1},
            {'name': 'API', 'post_count': 1}
        ],
        'recent_comments': [
            {'author': 'Alice', 'post': 'Getting Started with Django', 'content': 'Great tutorial!', 'date': '2 days ago'},
            {'author': 'Bob', 'post': 'CSS Grid Layout', 'content': 'Very helpful, thanks!', 'date': '1 week ago'}
        ]
    }
    return render(request, 'blog/index.html', context)
