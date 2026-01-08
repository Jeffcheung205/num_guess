# 🎮 Number Guessing Game

A fun and interactive web-based number guessing game built with Django. Challenge yourself to guess the secret number with limited attempts and track your performance over time!

## ✨ Features

- **Interactive Gameplay**: Guess numbers with real-time feedback (too high, too low, or correct)
- **User Authentication**: 
  - Sign up and log in to track your personal game history
  - Play as a guest without registration
  - Secure password validation
- **Customizable Game Settings**:
  - Set your own number range (min and max)
  - Choose maximum number of attempts
- **Game Statistics**:
  - Track your win/loss ratio
  - View recent game history
  - Personal statistics for authenticated users
- **Beautiful UI**: Modern, responsive design with gradient backgrounds and smooth animations
- **Session Management**: Continue your game even after closing the browser
- **Admin Panel**: Manage users and games through Django admin interface

## 🚀 Demo

Play the game by guessing a number within your chosen range. Get hints after each guess and try to win before running out of attempts!

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/num-guess-game.git
   cd num-guess-game
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     .venv\Scripts\Activate.ps1
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install django
   ```

5. **Navigate to project directory**
   ```bash
   cd num_guess
   ```

6. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

7. **Create a superuser (optional, for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

8. **Start the development server**
   ```bash
   python manage.py runserver
   ```

9. **Open your browser and visit**
   ```
   http://127.0.0.1:8000/
   ```

## 🎯 How to Play

1. **Start a New Game**
   - Go to the home page
   - Choose your number range (e.g., 1-100)
   - Set maximum attempts (e.g., 10)
   - Click "Start New Game"

2. **Make Your Guesses**
   - Enter a number in the guess field
   - Submit your guess
   - Receive feedback:
     - 🟢 **Correct!** - You won!
     - 🟡 **Too Low** - Try a higher number
     - 🔴 **Too High** - Try a lower number

3. **Track Your Progress**
   - View your guess history during the game
   - Check your statistics page for overall performance
   - See win rate and recent games

## 🏗️ Project Structure

```
num_guess/
├── manage.py                          # Django management script
├── num_guess/                         # Project configuration
│   ├── settings.py                    # Django settings
│   ├── urls.py                        # Main URL configuration
│   └── wsgi.py                        # WSGI configuration
└── num_guess_app/                     # Main application
    ├── models.py                      # Game and GuessHistory models
    ├── views.py                       # View functions (login, game logic, stats)
    ├── urls.py                        # App URL patterns
    ├── admin.py                       # Admin panel configuration
    ├── templates/                     # HTML templates
    │   └── num_guess_app/
    │       ├── base.html              # Base template with styling
    │       ├── index.html             # Home page
    │       ├── game_play.html         # Game interface
    │       ├── log_in.html            # Login page
    │       ├── signup.html            # Registration page
    │       └── stats.html             # Statistics page
    └── migrations/                    # Database migrations
```

## 🔧 Technology Stack

- **Backend**: Django 5.2.8
- **Database**: SQLite (default, can be changed to PostgreSQL/MySQL)
- **Frontend**: HTML5, CSS3 (vanilla, no frameworks)
- **Authentication**: Django built-in authentication system
- **Session Management**: Django sessions

## 🎨 Features in Detail

### User Authentication
- Secure user registration with password confirmation
- Login/logout functionality
- Guest play option (play without account)
- User-specific game statistics

### Game Logic
- Random number generation within user-defined range
- Attempt tracking and validation
- Win/loss detection
- Guess history storage

### Statistics
- Total games played
- Games won
- Win rate percentage
- Recent game history with dates and results

## 🔐 Admin Access

Access the Django admin panel at `http://127.0.0.1:8000/admin/` to:
- View all games and users
- Monitor game statistics
- Manage user accounts

## 📝 Models

### Game Model
- `user`: ForeignKey to User (nullable for guest play)
- `secret_number`: The number to guess
- `attempts`: Current number of attempts
- `max_attempts`: Maximum allowed attempts
- `min_range`, `max_range`: Number range
- `is_won`, `is_finished`: Game state flags
- `created_at`: Timestamp

### GuessHistory Model
- `game`: ForeignKey to Game
- `guess_number`: The guessed number
- `timestamp`: When the guess was made

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

### Ideas for Contributions
- Add difficulty levels (easy, medium, hard)
- Implement a leaderboard system
- Add timer/speed challenge mode
- Create API endpoints for mobile app integration
- Add social features (challenge friends)
- Implement achievements/badges system
- Add sound effects and animations
- Multi-language support

## 🐛 Known Issues

- None at the moment. Please report any bugs you find!

## 📈 Future Enhancements

- [ ] Multiplayer mode
- [ ] Daily challenges
- [ ] Achievement system
- [ ] Leaderboards
- [ ] Mobile app version
- [ ] API for third-party integrations
- [ ] Social login (Google, GitHub)
- [ ] Email notifications
- [ ] Game difficulty presets
- [ ] Dark mode toggle

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Built with Django framework
- Inspired by classic number guessing games
- Thanks to the Django community for excellent documentation

## 📞 Support

If you have any questions or need help, please:
- Open an issue on GitHub
- Contact me via email
- Check the Django documentation at https://docs.djangoproject.com/

---

Happy Guessing! 🎲

