import os
import markdown
from django.shortcuts import render
from django.conf import settings

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def blog_list(request):
    # List all markdown files in the 'blog_posts' directory
    blog_dir = os.path.join(settings.BASE_DIR, 'blog_posts') 
    articles = []
    
    # List all files with .md extension
    for filename in os.listdir(blog_dir):
        if filename.endswith('.md'):
            articles.append({
                'title': filename.replace('.md', '').replace('-', ' ').title(),
                'slug': filename.replace('.md', ''),
            })
    
    return render(request, 'blog_list.html', {'articles': articles})

def blog_detail(request, slug):
    # Open the markdown file by slug and parse it
    blog_dir = os.path.join(settings.BASE_DIR, 'blog_posts')  
    try:
        with open(os.path.join(blog_dir, f'{slug}.md'), 'r') as file:
            content = file.read()
            html_content = markdown.markdown(content)  
    except FileNotFoundError:
        return render(request, '404.html')  
    
    return render(request, 'blog_detail.html', {'content': html_content, 'title': slug.replace('_', ' ').title()})
