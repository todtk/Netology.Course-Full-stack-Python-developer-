from django import template


register = template.Library()


@register.simple_tag
def format_date(date):
    return date.strftime("%Y-%m-%d")


@register.simple_tag
def get_page(pages, page):
    return pages[page - 1]
