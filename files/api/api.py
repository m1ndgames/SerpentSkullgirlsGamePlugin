from serpent.game_api import GameAPI


class SkullgirlsAPI(GameAPI):

    def __init__(self, game=None):
        super().__init__(game=game)

    def my_api_function(self):
        pass

    class MyAPINamespace:

        @classmethod
        def my_namespaced_api_function(cls):
            api = SkullgirlsAPI.instance