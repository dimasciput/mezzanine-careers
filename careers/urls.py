from django.conf.urls import url
from .views import jobpost_list, jobpost_detail

# Job Post patterns.
urlpatterns = [
    url("^tag/(?P<tag>.*)/$",
        jobpost_list,
        name="jobpost_list_tag"),

    url("^archive/(?P<year>\d{4})/(?P<month>\d{1,2})/$",
        jobpost_list,
        name="jobpost_list_month"),

    url("^archive/(?P<year>.*)/$",
        jobpost_list,
        name="jobpost_list_year"),

    url("^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>.*)/$",
        jobpost_detail,
        name="jobpost_detail_date"),

    url("^(?P<slug>.*)/$",
        jobpost_detail,
        name="jobpost_detail"),

    url("^$",
        jobpost_list,
        name="jobpost_list"),
]
