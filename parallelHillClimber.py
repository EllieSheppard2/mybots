import constants as c
from solution import SOLUTION
import copy

class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        self.parents = {}
        self.nextAvailableID = 0

        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Select(self):
        for key in self.parents:
            if self.children[key].fitness < self.parents[key].fitness:
                self.parents[key] = self.children[key]

    def Evaluate(self, solutions):
        for solution in solutions.values():
            solution.Start_Simulation("DIRECT")
            solution.Wait_For_Simulation_To_End()

    def Mutate(self):
        for key in self.children:
            self.children[key].Mutate()

    def Spawn(self):
        self.children = {}

        for key in self.parents:
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evolve(self):
        for generation in range(c.numberOfGenerations):
            self.Evaluate(self.parents)

            self.Spawn()

            self.Mutate()

            self.Evaluate(self.children)

            self.Print()

            self.Select()

    def Print(self):
        print()
        for key in self.parents:
            print(self.parents[key].fitness, self.children[key].fitness)
        print()

    def Show_Best(self):
        bestKey = max(self.parents, key=lambda k: self.parents[k].fitness)
        print(f"\nBest fitness: {self.parents[bestKey].fitness:.4f}")
        self.parents[bestKey].Save("best_weights.npy")  # ← save weights
        self.parents[bestKey].Start_Simulation("GUI")
        self.parents[bestKey].Wait_For_Simulation_To_End()