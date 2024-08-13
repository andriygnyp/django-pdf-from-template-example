import json
from io import BytesIO

from django.http import HttpResponse
from django.template.loader import get_template
from django.template.response import TemplateResponse
from xhtml2pdf import pisa


def genpdf(request):
    if request.method == "GET":
        return TemplateResponse(request, "index.html", {})

    data = json.loads(request.body.decode())
    print(data)
    template = get_template("pdf.html")
    html = template.render(data)
    pdf = BytesIO()
    pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), pdf)

    res = HttpResponse(pdf.getvalue(), content_type="application/pdf")
    res["Content-Disposition"] = "attachment; filename=pdf-example.pdf"

    return res
