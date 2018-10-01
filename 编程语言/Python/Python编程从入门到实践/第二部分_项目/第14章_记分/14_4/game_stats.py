def load_high_scores(stats):
    try:
        with open("high_scores.txt") as high_obj:
            stats.high_score = int(high_obj.read().strip())
            print("load_high_scores: " + str(high_obj.read().strip()))
    except FileNotFoundError:
        with open("high_scores.txt", 'w') as high_obj:
            high_obj.write(str(0))
            print("Create file score high")

class GameStats():
    """Track statistics for Alien Invasion."""
    
    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        
        # Start game in an inactive state.
        self.game_active = False
        
        # High score should never be reset.
        self.high_score = 0
        load_high_scores(self)
        
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
