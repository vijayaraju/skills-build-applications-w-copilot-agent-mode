from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create Users
        user1 = User.objects.create(username='john_doe', email='john@example.com', password='password123')
        user2 = User.objects.create(username='jane_doe', email='jane@example.com', password='password123')

        # Create Teams
        team1 = Team.objects.create(name='Team Alpha', members=[user1, user2])

        # Create Activities
        Activity.objects.create(user=user1, activity_type='Running', duration=30, date='2025-04-19')
        Activity.objects.create(user=user2, activity_type='Cycling', duration=45, date='2025-04-18')

        # Create Leaderboard
        Leaderboard.objects.create(team=team1, points=100)

        # Create Workouts
        Workout.objects.create(name='Morning Yoga', description='A relaxing yoga session', duration=60)
        Workout.objects.create(name='HIIT', description='High-intensity interval training', duration=30)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
