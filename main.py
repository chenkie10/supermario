#游戏主要入口
from source import tools
from source.state import main_menu,load_screen,level

def main():
    state_dict = {
        'main_menu':main_menu.MainMenu(),
        'load_screen':load_screen.LoadScreen(),
        'level':level.Level(),
        'game_over':load_screen.GameOver()
    }
    game=tools.Game(state_dict,'main_menu')
    game.run()

if __name__=='__main__':
    main()
