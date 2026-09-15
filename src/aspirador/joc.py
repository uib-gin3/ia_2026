from iaLib import agent, joc

class Aspirador(joc.JocNoGrafic):

    def __init__(self, agents: list[agent.Agent] | None = None):
        if agents is None:
            agents = []

        super(Aspirador, self).__init__(agents=agents)
        self.position = "a"
        self.rooms = {
            "a": {
                "dirty": True
             }
            "b": {
                "dirty": True
            }
        }

    def _draw(self):
        for room, status in self.rooms.items():
            status = "dirty" if status[dirty] else "clean"
            print(f"Room {room} is {status}")

    def percepcio(self):
        return {
            "position": self.positon
            "status": self.rooms[self.position]
        }

    def _aplica(self, accio, params=None, agent_actual=None):

        if accio == "clean":
            self.rooms[self.position]["dirty"] = False

        elif accio == "move":
            self.position = params["position"]

        elif accio == "check":
            for status in self.rooms.values():
                if status["dirty"]:
                    return False
            return True
