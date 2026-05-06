import constants as c
from solution import SOLUTION
import copy
import csv
import matplotlib.pyplot as plt

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
        self.fitnessHistory = []
        self.Evaluate(self.parents)

        for generation in range(c.numberOfGenerations):
            self.Spawn()
            self.Mutate()
            self.Evaluate(self.children)
            self.Print()
            self.Select()

            best = max(self.parents[k].fitness for k in self.parents)
            self.fitnessHistory.append(-best)
            print(f"Generation {generation} best fitness: {best:.4f}")

            csvPath = "fitness_history.csv"
            with open(csvPath, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Generation", "Best Fitness"])
                for gen, fitness in enumerate(self.fitnessHistory):
                    writer.writerow([gen, fitness]) #note the invert in report

            # Save as graph
            plt.figure()
            plt.plot(self.fitnessHistory)
            plt.xlabel("Generation")
            plt.ylabel("Best Fitness")
            plt.title("Fitness Over Generations")
            plt.savefig("fitness_graph.png")
            plt.close()
            print("Saved fitness_history.csv and fitness_graph.png")

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
