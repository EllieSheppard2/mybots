from solution import SOLUTION

s = SOLUTION(0)
s.Create_World()
s.Create_Body()
s.Load("best_weights.npy")  # ← load saved weights
s.Create_Brain()
s.Start_Simulation("GUI")
s.Wait_For_Simulation_To_End()