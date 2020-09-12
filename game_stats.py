class GameStats:
    #Track statistics for Alien Invasion

    def __init__(self, ai_game):
        #Initialize statistics
        self.settings = ai_game.settings
        self.reset_stats()
    
        #Start Alien Invasion in an inactive state
        self.game_active = False

        #Pause should not be active
        self.pause_active = False

        #High score should never be reset
        self.alltime_high_score = 'highscore.txt'
        with open(self.alltime_high_score) as highscore:
            self.high_score = int(highscore.read())

    def reset_stats(self):
        #Initialize statistics that can change during the game
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1