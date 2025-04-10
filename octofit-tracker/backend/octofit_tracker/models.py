from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    # Add other fields as needed

class Team(models.Model):
    name = models.CharField(max_length=255)
    # Add other fields as needed

class Activity(models.Model):
    description = models.TextField()
    # Add other fields as needed

class Leaderboard(models.Model):
    rank = models.IntegerField()
    # Add other fields as needed

class Workout(models.Model):
    type = models.CharField(max_length=255)
    # Add other fields as needed
