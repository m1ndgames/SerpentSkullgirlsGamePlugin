from serpent.game import Game
from .api.api import SkullgirlsAPI
from serpent.utilities import Singleton
from serpent.input_controller import KeyboardKey
import time

class SerpentSkullgirlsGame(Game, metaclass=Singleton):

    def __init__(self, **kwargs):
        kwargs["platform"] = "steam"
        kwargs["window_name"] = "Skullgirls Encore"
        kwargs["app_id"] = "245170"
        kwargs["app_args"] = None

        super().__init__(**kwargs)

        self.api_class = SkullgirlsAPI
        self.api_instance = None
		
        self.frame_transformation_pipeline_string = "RESIZE:100x100|GRAYSCALE|FLOAT"
        #self.frame_transformation_pipeline_string = "FLOAT"
        self.frame_width = 100
        self.frame_height = 100
        self.frame_channels = 0
 
    @property
    def screen_regions(self):
        regions = {
            "TITLE_TEXT": (308, 202, 326, 440),
            "MAINMENU_TEXT": (326, 28, 340, 143),
            "MAINMENU_SELECT": (129, 157, 168, 276),
            "LEVELSELECT": (78, 280, 85, 359),
            "PLAYERSELECT": (30, 264, 46, 374),
            "FIGHTMENU_RETRY": (211, 170, 230, 296),
            "FIGHTMENU_SELECT": (49, 133, 83, 302),
            "P1_HP": (51, 89, 52, 271),
            "P2_HP": (51, 370, 52, 552),
            "TIMER": (22, 305, 47, 336),
            "FIGHTCHECK": (1, 296, 15, 344),
            "ROUNDSTART": (120, 391, 161, 433),
            "FIGHTZONE": (88, 0, 360, 640),
            "FIGHT_TWO_WINS": (63, 371, 81, 409),
        }

        return regions

    @property
    def ocr_presets(self):
        presets = {
            "SAMPLE_PRESET": {
                "extract": {
                    "gradient_size": 1,
                    "closing_size": 1
                },
                "perform": {
                    "scale": 10,
                    "order": 1,
                    "horizontal_closing": 1,
                    "vertical_closing": 1
                }
            }
        }
        return presets

    def after_launch(self):
        self.is_launched = True

        time.sleep(15)

        self.window_id = self.window_controller.locate_window(self.window_name)

        self.window_controller.move_window(self.window_id, 0, 0)
        self.window_controller.focus_window(self.window_id)

        self.window_geometry = self.extract_window_geometry()

        print(self.window_geometry)
