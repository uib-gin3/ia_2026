from iaLib import agent, joc

class Aspirador(joc.JocNoGrafic):

    def __init__(self, agents: list[agent.Agent] | None = None):
        if agents is None:
            agents = []

        super(Aspirador, self).__init__(agents=agents)
        self.posicio = 0
        self.habitacions = (False, False)


    def _draw(self):
        output = ""

        brutor = "💩"
        aspirador = "🤖"

        for i in range(2):
            output += aspirador if i == self.posicio else ' '

        output += '\n'

        for i in range(2):
            output += brutor if self.habitacions[i] else ' '

        print(output)

    def percepcio(self):
        return {
            "Loc": self.posicio,
            "Net": self.habitacions[self.posicio],
        }

    def _aplica(self, accio, params=None, agent_actual=None):
        if accio == 'A':
            self.habitacions[self.posicio] = True
            return

        if accio == 'D':
            self.posicio = 1
            return 

        if accio == 'E':
            self.posicio = 0
            return
