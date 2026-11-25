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


ORGS = [
    {
        "name": "Agile Alliance",
        "roles": ["Conference Program Chair, 2001, 2004 and 2010"],
        "logo": IMG + "og-Agile_Alliance_Logo_Color.png",
        "text": "A global nonprofit organization dedicated to promoting the concepts of Agile software development as outlined in the Agile Manifesto.",
    },
    {
        "name": "Scrum Alliance",
        "roles": ["Managing Director (past)", "Certified Scrum Trainer", "Certified Scrum Professional (SM + PO)", "Certified ScrumMaster", "Certified Scrum Product Owner"],
        "logo": IMG + "og-sai_logo_rgb-400.png",
        "text": "The largest, most established and influential professional membership and certification organization in the Agile community.",
    },
    {
        "name": "Agile Leadership Network",
        "roles": ["Co-founder"],
        "logo": IMG + "og-alnaa.png",
        "text": "The first group of professionals to explore the implications of agile methods on project management best practices.",
    },
    {
        "name": "Kanban University",
        "roles": ["Kanban Coaching Professional", "Kanban Management Professional"],
        "logo": IMG + "og-lku-logo-4.png",
        "text": "Runs several programs to build awareness and assure quality in Kanban implementations for professional services work.",
    },
]


def about(request):
    return render(request, "oobeyagroup/about.html", {"orgs": ORGS})


def custom_500_view(request):
    return render(request, "oobeyagroup/500.html", status=500)
