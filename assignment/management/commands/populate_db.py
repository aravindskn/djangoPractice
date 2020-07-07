from django.core.management.base import BaseCommand
from assignment.models import User, ActivityPeriod
import random

""" Clear All Data  """
MODE_REFRESH = 'refresh'

""" Clear All Data and Do Not Create any Object """
MODE_CLEAR = 'clear'


class Command(BaseCommand):
    help = "Populates the Database with Initial Data"

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_populate_db(self, options['mode'])
        self.stdout.write('done.')


def clear_data():
    """Deletes all Data from DB"""
    User.objects.all().delete()
    ActivityPeriod.objects.all().delete()


def create_activity_period():
    """
    Create Activity Period Data into DB
    :return:
    """

    start_time = ['2020-07-06T07:38:00+00:00', '2020-05-14T07:38:00+00:00', '2020-05-19T07:38:00+00:00']
    end_time = ['2020-07-14T07:38:00+00:00', '2020-08-19T07:38:00+00:00', '2020-08-16T07:38:00+00:00']

    activity_period = ActivityPeriod(start_time=random.choice(start_time), end_time=random.choice(end_time))

    activity_period.save()
    return activity_period


def create_user():
    """
    Create User Data into DB
    :return:
    """

    id = ['KJ43K53KS', 'HS39GMS93', '93KF754MW', '0WLR73MS8']
    real_name = ['arun kumar', 'rahul dravid', 'simply kumar', 'hello rahul']
    tz = ['America/Los_Angeles', 'Asia/Kolkata']
    start_time = ['2020-07-06T07:38:00+00:00', '2020-05-14T07:38:00+00:00', '2020-05-19T07:38:00+00:00']
    end_time = ['2020-07-14T07:38:00+00:00', '2020-08-19T07:38:00+00:00', '2020-08-16T07:38:00+00:00']

    user = User(id=random.choice(id), real_name=random.choice(real_name), tz=random.choice(tz))
    activity_period1 = ActivityPeriod(start_time=random.choice(start_time), end_time=random.choice(end_time))
    activity_period1.save()
    activity_period2 = ActivityPeriod(start_time=random.choice(start_time), end_time=random.choice(end_time))
    activity_period2.save()
    user.save()
    user.activity_period.add(activity_period1)
    user.activity_period.add(activity_period2)
    return user


def run_populate_db(self, mode):
    """ Seed database based on mode
    :param mode: refresh / clear
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    # Creating 2 entries
    for i in range(2):
        create_activity_period()
        create_user()
