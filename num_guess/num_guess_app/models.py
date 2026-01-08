from django.db import models
from django.contrib.auth.models import User
import random

# Create your models here.

class Game(models.Model):
    """Model to track a number guessing game session"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='games', null=True, blank=True)
    secret_number = models.IntegerField()
    attempts = models.IntegerField(default=0)
    max_attempts = models.IntegerField(default=10)
    min_range = models.IntegerField(default=1)
    max_range = models.IntegerField(default=100)
    is_won = models.BooleanField(default=False)
    is_finished = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Game {self.id} - {'Won' if self.is_won else 'Lost' if self.is_finished else 'In Progress'}"
    
    @classmethod
    def create_new_game(cls, min_range=1, max_range=100, max_attempts=10, user=None):
        """Create a new game with a random secret number"""
        secret = random.randint(min_range, max_range)
        return cls.objects.create(
            user=user,
            secret_number=secret,
            min_range=min_range,
            max_range=max_range,
            max_attempts=max_attempts
        )
    
    def make_guess(self, guess):
        """Make a guess and return feedback"""
        if self.is_finished:
            return "game_over", "Game is already finished!"
        
        self.attempts += 1
        
        if guess == self.secret_number:
            self.is_won = True
            self.is_finished = True
            self.save()
            return "correct", f"Congratulations! You guessed the number in {self.attempts} attempts!"
        elif self.attempts >= self.max_attempts:
            self.is_finished = True
            self.save()
            return "game_over", f"Game Over! The number was {self.secret_number}."
        elif guess < self.secret_number:
            self.save()
            return "too_low", f"Too low! Try again. Attempts: {self.attempts}/{self.max_attempts}"
        else:
            self.save()
            return "too_high", f"Too high! Try again. Attempts: {self.attempts}/{self.max_attempts}"


class GuessHistory(models.Model):
    """Model to track individual guesses"""
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='guesses')
    guess_number = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['timestamp']
    
    def __str__(self):
        return f"Game {self.game.id} - Guess: {self.guess_number}"
