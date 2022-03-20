from django import template

register = template.Library()

@register.simple_tag
def ends_with_jpg(val):
    if val.endswith(".jpg") or val.endswith(".png"):
        return True
    else:
        return False

@register.simple_tag
def ends_with_pdf(val):
    if val.endswith(".pdf"):
        return True
    else:
        return False

@register.simple_tag
def ends_with_doc(val):
    if val.endswith(".doc") or val.endswith(".docx"):
        return True
    else:
        return False

@register.simple_tag
def ends_with_ppt(val):
    if val.endswith(".ppt") or val.endswith(".pptx"):
        return True
    else:
        return False

@register.simple_tag
def ends_with_csv(val):
    if val.endswith(".csv"):
        return True
    else:
        return False

