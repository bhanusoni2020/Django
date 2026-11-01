from django.http import HttpResponse

def post_details(request, post_id):
    return HttpResponse(f"<h1>show blog post{post_id}</h1>")

def user_profile(request, username):
    return HttpResponse(f"<h1>profile of user{username}</h1>")

def article_by_year(request,year ):
    return HttpResponse(f"<h1>Article from the year {year}</h1>")

# def article_details(request, year, month):
#     return HttpResponse(f"<h1> Article from {year} - {month}</h1>")

def article_details(reqquest, **kwargs):
    return HttpResponse(f"<h1>Date {kwargs}</h1>")