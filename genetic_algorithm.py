from league import League
from deap import creator, base, tools, algorithms

class GeneticAlgorithm():
  def __init__(self, league: League):
    self.league = league
    print(type(league))
    a = 1


  #TODO- Make better lol
  def pick_viable_roster(self):
      roster = []
      all_pos = [0, 0, 1, 2, 3, 4, 5, 6, 6, 6]
      indi = []#SOMETHING HERE
      while len(roster) < 10:
          cur_player = random.choice(indi)
          cur_pos = dic_input.get(cur_player)[0]
          if cur_pos in all_pos and cur_player not in roster:
              roster.append(cur_player)
              all_pos.remove(cur_pos)
      return roster

  def genetic(self):
    creator.create("Fitness", base.Fitness, weights=(1.0, -1.0, 1.0))
    creator.create("Individual", list, fitness=creator.Fitness)

    toolbox = base.Toolbox()

    # Attribute generator
    toolbox.register("attr_item",  self.pick_viable_roster)
    # Structure initializers
    toolbox.register("individual", tools.initIterate, creator.Individual,
        toolbox.attr_item)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    toolbox.register("evaluate", self.eval_knapsack)

    toolbox.register("mate", self.cxSet)
    toolbox.register("mutate", self.mutSet)
    toolbox.register("select", tools.selNSGA2)

    #The number of generation.
    NGEN = 1000
    #The number of individuals to select for the next generation
    MU = 800
    #The number of children to produce at each generation.
    LAMBDA = 100
    #The probability that an offspring is produced by crossover.
    CXPB = 0.05
    #The probability that an offspring is produced by mutation.
    MUTPB = 0.7

    pop = toolbox.population(n=MU)
    #An object that will contain the best individuals
    hof = tools.ParetoFront()
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean, axis=0)
    stats.register("std", np.std, axis=0)
    stats.register("min", np.min, axis=0)
    stats.register("max", np.max, axis=0)

    popu, log = algorithms.eaMuPlusLambda(pop, toolbox, MU, LAMBDA, CXPB, MUTPB, NGEN, stats,
                              halloffame=hof)

    sorted_hof = sorted(hof, key=lambda ind: ind.fitness.values, reverse=True)
    best = sorted_hof[0]

  def intersection(self, lst1, lst2):
      lst3 = [value for value in lst1 if value in lst2]
      return lst3

  def diff(self, li1, li2):
      li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
      return li_dif

  def cxSet(self, ind1, ind2):
      """Apply a crossover operation on input sets. The first child is the
      intersection of the two sets, the second child is the difference of the
      two sets.
      """
      inter = intersection(ind1, ind2) # Intersection
      differ = diff(ind1, ind2) # Symmetric Difference
      return ind1, ind2

  def mutSet(self, individual):
      """Mutation that pops or add an element."""
      if random.random() < 0.5:
          if len(individual) > 0:     # We cannot pop from an empty set
              remove_player = random.choice(sorted(tuple(individual)))
              individual.remove(remove_player)
      else:
          add_player = random.choice(indi)
          while add_player in individual:
              add_player = random.choice(indi)
          individual.append(add_player)
      return individual,

  #TODO- make better lol
  def eval_knapsack(self, individual):
    weight = 0.0
    value = 0.0
    pitcher_count = 0
    catcher_count = 0
    first_base_count = 0
    second_base_count = 0
    third_base_count = 0
    short_stop_count = 0
    outfield_count = 0
    positions_filled = []
    id_repeat_check = []
    for item in individual:
        if item in id_repeat_check:
            optimal -= 500
        id_repeat_check.append(item)
        positions_filled.append(dic_input.get(item)[0])
        weight += dic_input.get(item)[1]
        value += dic_input.get(item)[2]
    # print weight
    # print value

    for p in positions_filled:
        if p == 0:
            pitcher_count += 1
        if p == 1:
            catcher_count += 1
        if p == 2:
            first_base_count += 1
        if p == 3:
            second_base_count += 1
        if p == 4:
            third_base_count += 1
        if p == 5:
            short_stop_count += 1
        if p == 6:
            outfield_count += 1

    optimal = 0
    if weight > MAX_WEIGHT_DK:
        optimal -= (weight - MAX_WEIGHT_DK)
    if len(individual) != MAX_ITEM_DK:
        optimal -= 100 * abs(len(individual) - MAX_ITEM_DK)
    if pitcher_count > 2:
        optimal -= 100 * (pitcher_count - 2)
    elif pitcher_count == 2:
        optimal += 100
    if catcher_count > 1:
        optimal -= 100 * (catcher_count - 1)
    elif catcher_count == 1:
        optimal += 100
    if first_base_count > 1:
        optimal -= 100 * (first_base_count - 1)
    elif first_base_count == 1:
        optimal += 100
    if second_base_count > 1:
        optimal -= 100 * (second_base_count - 1)
    elif second_base_count == 1:
        optimal += 100
    if third_base_count > 1:
        optimal -= 100 * (third_base_count - 1)
    elif third_base_count == 1:
        optimal += 100
    if short_stop_count > 1:
        optimal -= 100 * (short_stop_count - 1)
    elif short_stop_count == 1:
        optimal += 100
    if outfield_count > 3:
        optimal -= 100 * (outfield_count - 3)
    elif outfield_count == 3:
        optimal += 100
    return optimal, weight, value
