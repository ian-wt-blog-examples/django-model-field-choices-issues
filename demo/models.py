import zoneinfo

from django.db import models


FRESHMAN = "FR"
SOPHOMORE = "SO"
JUNIOR = "JR"
SENIOR = "SR"
GRADUATE = "GR"
YEAR_IN_SCHOOL_CHOICES = {
    FRESHMAN: "Freshman",
    SOPHOMORE: "Sophomore",
    JUNIOR: "Junior",
    SENIOR: "Senior",
    GRADUATE: "Graduate",
}

YEAR_IN_SCHOOL_CHOICES_SET = sorted(set(YEAR_IN_SCHOOL_CHOICES.items()))


class Student(models.Model):

    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES_SET,
        default=FRESHMAN,
    )


# time zones example

timezones = sorted(zoneinfo.available_timezones())

TIMEZONE_CHOICES = tuple(zip(timezones, timezones))


class UserProfile(models.Model):
    timezone = models.CharField(choices=TIMEZONE_CHOICES)
