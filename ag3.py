import random
from random import randint, sample


class GeneticAlgorithm:
    def _init_(self, n_generations, population_size, mutation_probability):
        self.n_generations = n_generations
        self.population_size = population_size
        self.mutation_probability = mutation_probability

        # read input file and store information
        with open('array.txt', 'r') as f:
            n_lines, n_cols = map(int, f.readline().split())
            lines = f.read().splitlines()

        self.coordinates = {}
        self.species = []

        for i in range(n_lines):
            line = lines[i].split()
            for j in range(len(line)):
                if line[j] != '0':
                    self.coordinates[line[j]] = (i, j)
                    self.species.append(line[j])

    def generate_population(self):
        population = [i for i in self.species if i != 'R']
        pop = []
        while len(pop) != self.population_size:
            indv = sample(population, len(population))
            if indv not in pop:
                pop.append(indv)
        return pop

    def fitness(self, route):
        rt = list(route)  # convert to list
        n = 0
        cr = 0
        rt.append('R')
        rt.insert(0, 'R')

        while n < len(rt) - 1:
            y = abs(self.coordinates[rt[n]][0] - self.coordinates[rt[n + 1]][0])
            x = abs(self.coordinates[rt[n]][1] - self.coordinates[rt[n + 1]][1])
            cr += x + y
            n += 1

        del (rt[0], rt[-1])
        return cr

    def get_first_element(self, tuple):
        return tuple[0]

    def rank_population(self, p):
        sorted_p = sorted(p, key=self.get_first_element)
        return sorted_p

    def select(self, p, n1, n2):
        m = []
        t = []
        for i in range(n1):
            c = random.sample(p, n2)
            for j in c:
                t.append((self.fitness(j), j))
            chmp = self.rank_population(t)[0][1]
            m.append(chmp)

        return m

    def crossover(self, f, m):
        bp = randint(1, len(f) - 1)
        cp = m[:]
        cs = []

        for ch in range(2):
            for p in range(bp):
                if f[p] != m[p]:
                    tmp = m[p]
                    m[p] = f[p]

                    for cp2 in range(p + 1, len(m)):
                        if m[p] == m[cp2]:
                            m[cp2] = tmp
                            break

            cs.append(m)
            m = f
            f = cp

        return cs

    def mutation(self, route):
        if random.random() < self.mutation_probability:
            mp = randint(0, len(route) - 2)
            cp = route[mp]

            route[mp] = route[mp + 1]
            route[mp + 1] = cp

            return route

    def run(self):
        p = self.generate_population()
        bc = float('inf')
        gen = 0
        mbc = 0

        while gen < self.n_generations:
            s = self.select(p, 20, 5)
            pp = []
            for a in range(50):
                f = random.choice(s)
                m = random.choice(s)
                cs = self.crossover(f, m)
                for c in cs:
                    mp = self.mutation(c)
                    if mp:
                        pp.append(mp)
                    else:
                        pp.append(c)

            sorted_pp = self.rank_population([(self.fitness(r), r) for r in pp])
            p = [r for f, r in sorted_pp[:self.population_size]]
            bc = sorted_pp[0][0]

            if bc < mbc or mbc == 0:
                mbc = bc

            print(f'Generation {gen + 1} | Best cost: {bc}')

            gen += 1

        print(f'\nBest path found: {sorted_pp[0][1]}')
        print(f'Cost: {sorted_pp[0][0]}')


ga = GeneticAlgorithm(n_generations=100, population_size=50, mutation_probability=0.1)
ga.run()
