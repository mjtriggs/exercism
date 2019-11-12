def tally(rows):
    '''
    Read in a series of results (list) and output a league table (list).
    '''

    # Get list of teams
    input_list = [i.split(";") for i in rows]
    teams = list(set([item[0] for item in input_list]).union(set([item[1] for item in input_list])))

    # Initialise the League as a class object
    league = League(teams)

    # Interpret Results
    for i in range(len(input_list)):
        result = input_list[i][2] 
        if result == "win":
            league.add_win(input_list[i][0])
            league.add_loss(input_list[i][1])
        if result == "loss":
            league.add_loss(input_list[i][0])
            league.add_win(input_list[i][1])
        if result == "draw":
            league.add_draw(input_list[i][0])
            league.add_draw(input_list[i][1])

    return league.get_league_table()

def create_row(team, matches, wins, draws, losses, points):

    # Create formatted row for output
    row = team.ljust(30) + ' | ' + str(matches).rjust(2) + ' | ' \
        + str(wins).rjust(2) + ' | ' + str(draws).rjust(2) \
        + ' | ' + str(losses).rjust(2) + ' | ' + str(points).rjust(2)

    return row
    
class League(object):
    def __init__(self, teams):
        self.teams = teams
        self.matches = {i: 0 for i in teams}
        self.number_wins = {i : 0 for i in teams}
        self.number_losses = {i: 0 for i in teams}
        self.number_draws = {i: 0 for i in teams}
        self.points = {i: 0 for i in teams}

    # Below functions are used to change the league totals when we have results
    # We do not include any functionality to add/change teams or edit results.
    def add_win(self, team):
        self.number_wins[team] += 1
        self.matches[team] += 1
        self.calculate_points()
        return self

    def add_loss(self, team):
        self.number_losses[team] += 1
        self.matches[team] += 1
        self.calculate_points()
        return self

    def add_draw(self, team):
        self.number_draws[team] += 1
        self.matches[team] += 1
        self.calculate_points()
        return self

    # Calculate points is called by other functions to make sure the points for each team is up to date
    def calculate_points(self):
        self.points = {i : 3 * self.number_wins[i] + self.number_draws[i] for i in self.teams}
        self.teams = sorted(self.points, key = lambda k: (-self.points[k], k))
        return self

    # The league table has very specific input and padding rules.
    def get_league_table(self):
        output_header = "Team                           | MP |  W |  D |  L |  P"
        output_list = [output_header]

        for i in self.teams:
            new_row = create_row(i, self.matches[i], self.number_wins[i], self.number_draws[i], self.number_losses[i], self.points[i])
            output_list.append(new_row)

        return output_list
