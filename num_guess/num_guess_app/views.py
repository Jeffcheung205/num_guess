from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Game, GuessHistory

# Create your views here.

def login_view(request):
    """Handle user login"""
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('index')
        else:
            return render(request, 'num_guess_app/log_in.html', {
                'error': 'Invalid username or password!'
            })
    
    return render(request, 'num_guess_app/log_in.html')


def signup_view(request):
    """Handle user registration"""
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        
        # Validation
        if not username or not password:
            return render(request, 'num_guess_app/signup.html', {
                'error': 'Username and password are required!'
            })
        
        if password != password_confirm:
            return render(request, 'num_guess_app/signup.html', {
                'error': 'Passwords do not match!'
            })
        
        if len(password) < 6:
            return render(request, 'num_guess_app/signup.html', {
                'error': 'Password must be at least 6 characters long!'
            })
        
        if User.objects.filter(username=username).exists():
            return render(request, 'num_guess_app/signup.html', {
                'error': 'Username already exists!'
            })
        
        # Create user
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        messages.success(request, f'Welcome to Number Guessing Game, {username}!')
        return redirect('index')
    
    return render(request, 'num_guess_app/signup.html')


def logout_view(request):
    """Handle user logout"""
    logout(request)
    messages.success(request, 'You have been logged out successfully!')
    return redirect('login')

def index(request):
    """Home page - start a new game or continue existing"""
    game_id = request.session.get('current_game_id')
    game = None
    
    if game_id:
        try:
            game = Game.objects.get(id=game_id)
            if game.is_finished:
                game = None
        except Game.DoesNotExist:
            game = None
    
    return render(request, 'num_guess_app/index.html', {'game': game})


def new_game(request):
    """Start a new game"""
    if request.method == 'POST':
        min_range = int(request.POST.get('min_range', 1))
        max_range = int(request.POST.get('max_range', 100))
        max_attempts = int(request.POST.get('max_attempts', 10))
        
        # Validate input
        if min_range >= max_range:
            return render(request, 'num_guess_app/index.html', {
                'error': 'Minimum range must be less than maximum range!'
            })
        
        user = request.user if request.user.is_authenticated else None
        game = Game.create_new_game(min_range, max_range, max_attempts, user=user)
        request.session['current_game_id'] = game.id
        return redirect('game_play')
    
    return redirect('index')


def game_play(request):
    """Main game play page"""
    game_id = request.session.get('current_game_id')
    
    if not game_id:
        return redirect('index')
    
    game = get_object_or_404(Game, id=game_id)
    guesses = game.guesses.all()
    
    feedback = None
    feedback_type = None
    
    if request.method == 'POST':
        try:
            guess = int(request.POST.get('guess'))
            
            # Validate guess is in range
            if guess < game.min_range or guess > game.max_range:
                feedback = f"Please guess a number between {game.min_range} and {game.max_range}!"
                feedback_type = "error"
            else:
                # Save the guess to history
                GuessHistory.objects.create(game=game, guess_number=guess)
                
                # Process the guess
                feedback_type, feedback = game.make_guess(guess)
                
                # Reload guesses after making a guess
                guesses = game.guesses.all()
        except (ValueError, TypeError):
            feedback = "Please enter a valid number!"
            feedback_type = "error"
    
    context = {
        'game': game,
        'guesses': guesses,
        'feedback': feedback,
        'feedback_type': feedback_type,
    }
    
    return render(request, 'num_guess_app/game_play.html', context)


def end_game(request):
    """End the current game"""
    if 'current_game_id' in request.session:
        del request.session['current_game_id']
    return redirect('index')


def game_stats(request):
    """Show statistics of all games"""
    # Filter games by user if authenticated
    if request.user.is_authenticated:
        all_games = Game.objects.filter(user=request.user, is_finished=True).order_by('-created_at')[:10]
        total_games = Game.objects.filter(user=request.user, is_finished=True).count()
        won_games = Game.objects.filter(user=request.user, is_won=True).count()
    else:
        all_games = Game.objects.filter(is_finished=True).order_by('-created_at')[:10]
        total_games = Game.objects.filter(is_finished=True).count()
        won_games = Game.objects.filter(is_won=True).count()
    
    win_rate = (won_games / total_games * 100) if total_games > 0 else 0
    
    context = {
        'all_games': all_games,
        'total_games': total_games,
        'won_games': won_games,
        'win_rate': round(win_rate, 2),
    }
    
    return render(request, 'num_guess_app/stats.html', context)
