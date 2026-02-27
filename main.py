from typing import ClassVar, override

from textual.app import App, ComposeResult
from textual.binding import BindingType
from textual.reactive import reactive
from textual.widgets import Static

MAP_WIDTH: int = 20
MAP_HEIGHT: int = 10

class GameMap(Static):
# 1. State mgmt : Reactives handle automatic UI updates
    player_x: reactive[int] = reactive(MAP_WIDTH // 2)
    player_y: reactive[int] = reactive(MAP_HEIGHT // 2)

    @override
    def render(self) -> str:
        lines: list[str] = []
        for y in range(MAP_HEIGHT) :
            row: str = ""
            for x in range(MAP_WIDTH) :
                if x == self.player_x and y == self.player_y :
                    row += "P"
                else :
                    row += "."
            lines.append(row)

        return "\n".join(lines)

class GameApp(App[None]) :
    BINDINGS: ClassVar[list[BindingType]] = [
        ("q", "quit", "Quit"),
        ("w", "move_up", "Up"),
        ("s", "move_down", "Down"),
        ("a", "move_left", "Left"),
        ("d", "move_right", "Right"),
    ]

    @override
    def compose(self) -> ComposeResult :
        yield GameMap()

    def action_move_up(self) :
        game_map = self.query_one(GameMap)
        if game_map.player_y > 0:
            game_map.player_y -= 1

    def action_move_down(self): 
        game_map = self.query_one(GameMap)
        if game_map.player_y < MAP_HEIGHT - 1 :
            game_map.player_y += 1

    def action_move_left(self): 
        game_map = self.query_one(GameMap)
        if game_map.player_x > 0 :
            game_map.player_x -= 1

    def action_move_right(self): 
        game_map = self.query_one(GameMap)
        if game_map.player_x < MAP_WIDTH - 1 :
            game_map.player_x += 1


if __name__ == "__main__" :
    app = GameApp()
    _ = app.run()
