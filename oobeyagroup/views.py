from django.shortcuts import render

from .offerings import CLIENTS, OFFERINGS

IMG = "oobeyagroup/images/"


def _service(request, template, heading, hero_image):
    offerings = [{"name": n, "text": t} for n, t in OFFERINGS[template]]
    return render(
        request,
        f"oobeyagroup/{template}.html",
        {"heading": heading, "hero_image": IMG + hero_image, "offerings": offerings},
    )


def index(request):
    clients = [{"name": n, "logo": IMG + f} for n, f in CLIENTS]
    return render(request, "oobeyagroup/index.html", {"clients": clients})


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
