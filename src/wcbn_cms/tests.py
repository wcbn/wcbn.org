"""Tests for event time formatting which can be tricky in certain cases"""

from datetime import datetime, timedelta
from django.test import TestCase
from django.utils import timezone
from django.template.defaultfilters import date, time
from wcbn_cms.models import Event
from wcbn_cms.templatetags.format_event_time import format_event_time


class FormatEventTimeTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        title = "My title"
        summary = "My summary"
        today = datetime.now()
        tomorrow = today + timedelta(days=1)
        start_date = today.date()
        start_time = today.time()
        end_date = tomorrow.date()
        end_time = tomorrow.time()

        cls.fmt_start_date = date(start_date, "l, N jS")
        cls.fmt_end_date = date(end_date, "l, N jS")
        cls.fmt_start_time = time(start_time)
        cls.fmt_end_time = time(end_time)

        # just start date
        cls.only_start_date = Event.objects.create(title=title, summary=summary, start_date=start_date)

        # start date + 1 other
        cls.with_end_date = Event.objects.create(title=title, summary=summary, start_date=start_date, end_date=end_date)
        cls.with_start_time = Event.objects.create(title=title, summary=summary, start_date=start_date, start_time=start_time)
        cls.with_end_time = Event.objects.create(title=title, summary=summary, start_date=start_date, end_time=end_time)

        # start date + 2 other
        cls.without_start_time = Event.objects.create(title=title, summary=summary, start_date=start_date, end_date=end_date, end_time=end_time)
        cls.without_end_time = Event.objects.create(title=title, summary=summary, start_date=start_date, end_date=end_date, start_time=start_time)
        cls.without_end_date = Event.objects.create(title=title, summary=summary, start_date=start_date, end_time=end_time, start_time=start_time)

        # both datetimes
        cls.with_all = Event.objects.create(title=title, summary=summary, start_date=start_date, end_date=end_date, start_time=start_time, end_time=end_time)

        # same date
        cls.same_date = Event.objects.create(title=title, summary=summary, start_date=start_date, end_date=start_date)
        cls.same_date_with_end_time = Event.objects.create(title=title, summary=summary, start_date=start_date, end_date=start_date, end_time=end_time)
        cls.same_date_with_start_time = Event.objects.create(title=title, summary=summary, start_date=start_date, end_date=start_date, start_time=start_time)
        cls.same_date_with_times = Event.objects.create(title=title, summary=summary, start_date=start_date, end_date=start_date, start_time=start_time, end_time=end_time)


    def test_only_start_date(self):
        """Ignore since events are grouped by date to begin with"""
        actual = format_event_time(self.only_start_date)
        expected = ""
        self.assertIs(actual, expected)

    def test_with_end_date(self):
        """date1 - date2"""
        actual = format_event_time(self.with_end_date)
        expected = f"{self.fmt_start_date} - {self.fmt_end_date}"
        self.assertEqual(actual, expected)

    def test_with_start_time(self):
        """time"""
        actual = format_event_time(self.with_start_time)
        expected = self.fmt_start_time
        self.assertEqual(actual, expected)

    def test_with_end_time(self):
        """Ends at time"""
        actual = format_event_time(self.with_end_time)
        expected = f"Ends at {self.fmt_end_time}"
        self.assertEqual(actual, expected)

    def test_without_start_time(self):
        """date1 - date2 time2"""
        actual = format_event_time(self.without_start_time)
        expected = f"{self.fmt_start_date} - {self.fmt_end_date} {self.fmt_end_time}"
        self.assertEqual(actual, expected)

    def test_without_end_time(self):
        """date1 time1 - date2"""
        actual = format_event_time(self.without_end_time)
        expected = f"{self.fmt_start_date} {self.fmt_start_time} - {self.fmt_end_date}"
        self.assertEqual(actual, expected)

    def test_without_end_date(self):
        """time1 - time2"""
        actual = format_event_time(self.without_end_date)
        expected = f"{self.fmt_start_time} - {self.fmt_end_time}"
        self.assertEqual(actual, expected)

    def test_with_all(self):
        """date1 time1 - date2 time2"""
        actual = format_event_time(self.with_all)
        expected = f"{self.fmt_start_date} {self.fmt_start_time} - {self.fmt_end_date} {self.fmt_end_time}"
        self.assertEqual(actual, expected)

    def test_same_date(self):
        """time1 - time2"""
        actual = format_event_time(self.same_date)
        expected = ""
        self.assertEqual(actual, expected)

    def test_same_date_with_end_time(self):
        """Ends at time2"""
        actual = format_event_time(self.same_date_with_end_time)
        expected = f"Ends at {self.fmt_end_time}"
        self.assertEqual(actual, expected)

    def test_same_date_with_start_time(self):
        """time1"""
        actual = format_event_time(self.same_date_with_start_time)
        expected = f"{self.fmt_start_time}"
        self.assertEqual(actual, expected)


    def test_same_date_with_times(self):
        """time1 - time2"""
        actual = format_event_time(self.same_date_with_times)
        expected = f"{self.fmt_start_time} - {self.fmt_end_time}"
        self.assertEqual(actual, expected)
