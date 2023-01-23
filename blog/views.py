from django.views import generic
from django.shortcuts import render
from .models import Careers, Tag, Category
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def Careers_list(request):
    cat_query = request.GET.get("c")

    query = request.GET.get("q")
    if query != None:
        object_list = Careers.objects.filter(Q(title__icontains=query) | Q(tags__name=query))
    else:
        if cat_query != None:
            object_list = Careers.objects.filter(Q(category__name=cat_query))
        else:
            object_list = Careers.objects.filter().order_by('-created_on')
    page_num = request.GET.get('page', 1)
    paginator = Paginator(object_list, 3) # 6 employees per page
    
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    tags = Tag.objects.all()

    cat = Category.objects.all().distinct()
    

    categories = {}
    for i in cat:
        categories[i] = Category.objects.filter(name=i).all()

    context = {
        'blogs': page_obj,
        "tags": tags,
        "categories": categories
        }

    return render(request, 'blog.html', context)

def blog_single(request, pk):
    blog = Careers.objects.filter(pk=pk).first()
    return render(request, 'blog-single.html', {"blog": blog})
