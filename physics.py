from math import *


class OneDimensionalPhysicsObject:
    def __init__(self, initX=None, finalX=None, displacement=None, initVelocity=None, velocity=None, acceleration=None, time=None):
        self.initX = initX
        self.finalX = finalX
        self.displacement = displacement
        self.initVelocity = initVelocity
        self.velocity = velocity
        self.acceleration = acceleration
        self.time = time

    def __str__(self):
        return f"OneDimensionalPhysicsObject({self.initX}, {self.finalX}, {self.displacement}, {self.initVelocity}, {self.velocity}, {self.acceleration}, {self.time})"

    def modify(self, x, y):
        # Modify the specified attribute to be the specified value
        if x == "initX":
            self.initX = y

        if x == "finalX":
            self.finalX = y

        if x == "displacement":
            self.displacement = y

        if x == "initVelocity":
            self.initVelocity = y

        if x == "velocity":
            self.velocity = y

        if x == "acceleration":
            self.acceleration = y

        if x == "time":
            self.time = y

    def calculate(self, args):
        # Calculate the specified attribute using diverse physics formulas which are chosen based on what attributes were already defined
        for arg in args:
            if arg == "initX":
                if self.finalX is not None:
                    if self.displacement is not None:
                        self.initX = self.finalX - self.displacement

                    elif self.acceleration is not None and self.initVelocity is not None:
                        if self.time is not None:
                            self.initX = self.finalX - self.acceleration * pow(self.time, 2) / 2 + self.initVelocity * self.time

                        elif self.velocity and self.acceleration != 0:
                            self.initX = self.finalX - (pow(self.velocity, 2) - pow(self.initVelocity, 2)) / (2 * self.acceleration)

                print(f"Value of initX was changed to {self.initX}")

            if arg == "finalX":
                if self.initX is not None:
                    if self.displacement is not None:
                        self.finalX = self.displacement + self.initX

                    elif self.acceleration is not None and self.initVelocity is not None:
                        if self.time is not None:
                            self.finalX = self.acceleration * pow(self.time, 2) / 2 + self.initVelocity * self.time + self.initX

                        elif self.velocity is not None and self.acceleration != 0:
                            self.finalX = (pow(self.velocity, 2) - pow(self.initVelocity, 2)) / (2 * self.acceleration) + self.initX

                print(f"Value of finalX was changed to {self.finalX}")

            if arg == "displacement":
                if self.finalX is not None and self.initX is not None:
                    self.displacement = self.finalX - self.initX

                elif self.acceleration is not None and self.initVelocity is not None:
                    if self.time is not None:
                        self.displacement = self.acceleration * pow(self.time, 2) / 2 + self.initVelocity * self.time

                    elif self.velocity is not None and self.acceleration != 0:
                        self.displacement = (pow(self.velocity, 2) - pow(self.initVelocity, 2)) / (2 * self.acceleration)

                print(f"Value of displacement was changed to {self.displacement}")

            if arg == "initVelocity":
                if self.acceleration is not None:
                    if self.velocity is not None:
                        if self.time is not None:
                            self.initVelocity = self.velocity - self.acceleration * self.time

                        elif self.finalX is not None and self.initX is not None:
                            squaredInitVelocity = pow(self.velocity, 2) - 2 * self.acceleration * (self.finalX - self.initX)
                            if squaredInitVelocity > 0:
                                initVelocities = [-sqrt(squaredInitVelocity), sqrt(squaredInitVelocity)]
                                self.initVelocity = initVelocities[min(max(int(input(f"Choose which index of initial velocities to save\n0 = {initVelocities[0]}\n1 = {initVelocities[1]}\n")), 0), 1)]

                        elif self.displacement is not None:
                                squaredInitVelocity = pow(self.velocity, 2) - 2 * self.acceleration * self.displacement
                                if squaredInitVelocity > 0:
                                    initVelocities = [-sqrt(squaredInitVelocity), sqrt(squaredInitVelocity)]
                                    self.initVelocity = initVelocities[min(max(int(input(f"Choose which index of initial velocities to save\n0 = {initVelocities[0]}\n1 = {initVelocities[1]}\n")), 0), 1)]

                    elif self.time is not None and self.time != 0:
                        if self.finalX is not None and self.initX is not None:
                            self.initVelocity = (self.finalX - self.initX - self.acceleration * pow(self.time, 2) / 2) / self.time

                        elif self.displacement is not None:
                            self.initVelocity = (self.displacement - self.acceleration * pow(self.time, 2) / 2) / self.time

                print(f"Value of initVelocity was changed to {self.initVelocity}")

            if arg == "velocity":
                if self.initVelocity is not None and self.acceleration is not None:
                    if self.time is not None:
                        self.velocity = self.acceleration * self.time + self.initVelocity

                    elif self.finalX is not None and self.initX is not None:
                        squaredVelocity = pow(self.initVelocity, 2) + 2 * self.acceleration * (self.finalX - self.initX)
                        if squaredVelocity > 0:
                            velocities = [-sqrt(squaredVelocity), sqrt(squaredVelocity)]
                            self.velocity = velocities[min(max(int(input(f"Choose which index of velocities to save\n0 = {velocities[0]}\n1 = {velocities[1]}\n")), 0), 1)]

                    elif self.displacement is not None:
                        squaredVelocity = pow(self.initVelocity, 2) + 2 * self.acceleration * self.displacement
                        if squaredVelocity > 0:
                            velocities = [-sqrt(squaredVelocity), sqrt(squaredVelocity)]
                            self.velocity = velocities[min(max(int(input(f"Choose which index of velocities to save\n0 = {velocities[0]}\n1 = {velocities[1]}\n")), 0), 1)]

                print(f"Value of velocity was changed to {self.velocity}")

            if arg == "acceleration":
                if self.initVelocity is not None:
                    if self.velocity is not None:
                        if self.time is not None and self.time != 0:
                            self.acceleration = (self.velocity - self.initVelocity) / self.time

                        elif self.finalX is not None and self.initX is not None:
                            self.acceleration = (pow(self.velocity, 2) - pow(self.initVelocity, 2)) / (2 * (self.finalX - self.initX))

                        elif self.displacement is not None and self.displacement != 0:
                            self.acceleration = (pow(self.velocity, 2) - pow(self.initVelocity, 2)) / (2 * self.displacement)

                    elif self.time is not None and self.time != 0:
                        if self.finalX is not None and self.initX is not None:
                            self.acceleration = (self.finalX - self.initX - self.initVelocity * self.time) * (2 / pow(self.time, 2))

                        elif self.displacement is not None:
                            self.acceleration = (self.displacement - self.initVelocity * self.time) * (2 / pow(self.time, 2))

                print(f"Value of acceleration was changed to {self.acceleration}")

            if arg == "time":
                if self.initVelocity is not None and self.acceleration is not None and self.acceleration != 0:
                    if self.velocity is not None:
                        self.time = (self.velocity - self.initVelocity) / self.acceleration

                    elif self.finalX is not None and self.initX is not None:
                        squaredVelocity = pow(self.initVelocity, 2) + 2 * self.acceleration * (self.finalX - self.initX)
                        if squaredVelocity > 0:
                            times = [(-self.initVelocity - sqrt(squaredVelocity)) / self.acceleration, (-self.initVelocity + sqrt(squaredVelocity)) / self.acceleration]
                            self.time = times[min(max(int(input(f"Choose which index of times to save\n0 = {times[0]}\n1 = {times[1]}\n")), 0), 1)]

                    elif self.displacement is not None:
                        squaredVelocity = pow(self.initVelocity, 2) + 2 * self.acceleration * self.displacement
                        if squaredVelocity > 0:
                            times = [(-self.initVelocity - sqrt(squaredVelocity)) / self.acceleration, (-self.initVelocity + sqrt(squaredVelocity)) / self.acceleration]
                            self.time = times[min(max(int(input(f"Choose which index of times to save\n0 = {times[0]}\n1 = {times[1]}\n")), 0), 1)]

                print(f"Value of time was changed to {self.time}")

        return True

    @staticmethod
    def formulas():
        # Return basic physics formulas
        return "v = at + initV\nx = at^2 / 2 + initV*t + initX\nv^2 = initV^2 + 2a(finalX - initX)"
