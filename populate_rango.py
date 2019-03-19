import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')
import django
django.setup()
from rango.models import Category, Page

def populate():

    python_pages = [
        {
            'title': 'Official Python Tutorial',
<<<<<<< HEAD
            'url': 'http://docs.python.org/2/tutorial',
            'views': 200
        },
        {
            'title': 'How to think like a computer scientist',
            'url': 'http://ww.greenteapress.com/thiinkpython',
            'views': 100
        },
        {
            'title': 'Learn Python in 10 Minutues',
            'url': 'http://www.korokithakis.net/tutorials/python/',
            'views': 5
=======
            'url': 'http://docs.python.org/2/tutorial'
        },
        {
            'title': 'How to think like a computer scientist',
            'url': 'http://ww.greenteapress.com/thiinkpython'
        },
        {
            'title': 'Learn Python in 10 Minutues',
            'url': 'http://www.korokithakis.net/tutorials/python/'
>>>>>>> 63a1fa0a6df2fc4b4c25f6b5b508329561fc4e9d
        }
    ]

    django_pages =[
        {
            'title': 'Official Django Tutorials',
<<<<<<< HEAD
            'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
            'views': 130
        },
        {
            'title': 'Django Rocks',
            'url': 'http://www.djangorocks.com/',
            'views': 100
        },
        {
            'title': 'How to tango with django',
            'url': 'http://www.tangowithdhango.com/',
            'views': 2
=======
            'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/'
        },
        {
            'title': 'Django Rocks',
            'url': 'http://www.djangorocks.com/'
        },
        {
            'title': 'How to tango with django',
            'url': 'http://www.tangowithdhango.com/'
>>>>>>> 63a1fa0a6df2fc4b4c25f6b5b508329561fc4e9d
        }
    ]

    other_pages = [
        {
            'title': 'Bottle',
<<<<<<< HEAD
            'url': 'http://bottlepy.org/docs/dev/',
            'views': 3
        },
        {
            'title': 'Flask',
            'url': 'http://flask.pocoo.org',
            'views': 20
=======
            'url': 'http://bottlepy.org/docs/dev/'
        },
        {
            'title': 'Flask',
            'url': 'http://flask.pocoo.org'
>>>>>>> 63a1fa0a6df2fc4b4c25f6b5b508329561fc4e9d
        }
    ]

    cats = {
<<<<<<< HEAD
        'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
        'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
        'Other Frameworks': {'pages': other_pages, 'views': 32, 'likes': 16}
    }

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['views'], cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], p['views'])
=======
        'Python': {'pages': python_pages},
        'Django': {'pages': django_pages},
        'Other Frameworks': {'pages': other_pages}
    }

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'])
>>>>>>> 63a1fa0a6df2fc4b4c25f6b5b508329561fc4e9d

    # Print out the categories
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()


<<<<<<< HEAD
def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
=======
def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
>>>>>>> 63a1fa0a6df2fc4b4c25f6b5b508329561fc4e9d
    c.save()
    return c


# Starts Execution to Populate data here
if __name__ == '__main__':
    print("Starting Rango population script")
    populate()
