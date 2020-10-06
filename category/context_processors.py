from .models import Category


# get all the categories from database and store into links variable so that we
# can use whenever we need
def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)
