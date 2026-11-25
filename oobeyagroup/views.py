from django.shortcuts import render

IMG = "oobeyagroup/images/"


def _service(request, template, heading, hero_image):
    return render(request, f"oobeyagroup/{template}.html", {"heading": heading, "hero_image": IMG + hero_image})


def index(request):
    return render(request, "oobeyagroup/index.html")


def agileandscrum(request):
    return _service(request, "agileandscrum", "Agile and Scrum", "program-hero-single-img.jpg")


def technologyleadership(request):
    return _service(request, "technologyleadership", "Technology Leadership", "team-around-table-closeup.png")


def productmanagement(request):
    return _service(request, "productmanagement", "Product Management", "prod-mngt-team-closeup.png")


def softwaredevelopment(request):
    return _service(request, "softwaredevelopment", "Software Development", "software-dev-team-closeup.png")


def custom_500_view(request):
    return render(request, "oobeyagroup/500.html", status=500)
