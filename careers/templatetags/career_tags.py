from datetime import datetime

from django.contrib.auth.models import User
from django.db.models import Count

from careers.forms import JobPostForm
from careers.models import JobPost, Career
from mezzanine import template


register = template.Library()


@register.as_tag
def jobpost_months(*args):
    """
    Put a list of dates for jobposts into the template context.
    """
    dates = Career.objects.published().values_list("publish_date", flat=True)
    date_dicts = [{"date": datetime(d.year, d.month, 1)} for d in dates]
    month_dicts = []
    for date_dict in date_dicts:
        if date_dict not in month_dicts:
            month_dicts.append(date_dict)
    for i, date_dict in enumerate(month_dicts):
        month_dicts[i]["post_count"] = date_dicts.count(date_dict)
    return month_dicts


@register.as_tag
def jobpost_recent_posts(limit=5):
    """
    Put a list of recently published jobposts into the template context.
    """
    return list(Career.objects.published()[:limit])


@register.inclusion_tag("admin/includes/quick_jobpost.html", takes_context=True)
def quick_jobpost(context):
    """
    Admin dashboard tag for the quick jobpost form.
    """
    context["form"] = JobPostForm()
    return context
