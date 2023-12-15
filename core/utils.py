from enum import Enum
import bcrypt

class Alghoritms:
    def __init__(self):
        pass
    @staticmethod
    def knapsack(list:list[object], weights:list, goal:int=10):
        """
        Algorithm
        If you have a list of 20 elements and each element has a weight>=1 and weigth<=20, then you should select a random elements from list such that the sum of the weights of the elements is equal to 20, Knapsack problem
        """
        n = len(list)
        dp = [[0] * (goal + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, goal + 1):
                if weights[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], weights[i - 1] + dp[i - 1][j - weights[i - 1]])

        seleccionados = []
        i = n
        j = goal

        while i > 0 and j > 0:
            if dp[i][j] != dp[i - 1][j]:
                seleccionados.append(list[i - 1])
                j -= weights[i - 1]
            i -= 1

        return seleccionados

class Hash:
    def __init__(self):
        pass
    @staticmethod
    def hash_password(password:str):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    @staticmethod
    def check_password(password:str, hashed_password:str):
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

class Components(str, Enum):
    component_1 = "Matemáticas"
    component_2 = "Ciencias Naturales"
    component_3 = "Ciencias Sociales"
    component_4 = "Análisis textual"
    component_5 = "Análisis de imagen"
    component_6 = "Simulacro"    
