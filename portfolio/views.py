from django.shortcuts import render

def portfolio_view(request):
    context = {
        'name': 'John Doe',
        'title': 'Full Stack Developer',
        'email': 'john.doe@email.com',
        'phone': '+1 (555) 123-4567',
        'location': 'San Francisco, CA',
        'about': 'Passionate developer with 5+ years of experience in web development. '
        'Specialized in Python, Django, and modern JavaScript frameworks.',
        'skills': ['Python', 'Django', 'JavaScript', 'React', 'PostgreSQL', 'AWS'],
        'projects': [
            {
                'title': 'E-commerce Platform',
                'description': 'Built a full-stack e-commerce solution with Django and React',
                'technologies': ['Django', 'React', 'PostgreSQL']
            },
            {
                'title': 'Task Management App',
                'description': 'Developed a collaborative task management application',
                'technologies': ['Django', 'Vue.js', 'MongoDB']
            },
            {
                'title': 'Weather Dashboard',
                'description': 'Created a real-time weather monitoring dashboard',
                'technologies': ['Python', 'FastAPI', 'Chart.js']
            }
        ],
        'experience': [
            {
                'company': 'Tech Solutions Inc.',
                'position': 'Senior Developer',
                'period': '2020 - Present',
                'description': 'Lead development of web applications and APIs'
            },
            {
                'company': 'Web Innovations',
                'position': 'Web Developer',
                'period': '2018 - 2020',
                'description': 'Developed and maintained client websites and applications'
            }
        ]
    }
    return render(request, 'portfolio/index.html', context)