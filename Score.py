class Score():
    def __init__(self):
        self.bestScores = self.loadScoreboard()

    def loadScoreboard(self):
        try:
            scoreboard = open('scoreboard.txt', 'r')
        except:
            scoreboard = open('scoreboard.txt', 'w')
            scoreboard.close()
            return []

        scores = scoreboard.readlines()
        bestScores = []

        for score in scores:
            score = score.strip('\n')
            score = score.split(" ")
            score[0] = int(score[0])
            bestScores.append(score)

        scoreboard.close()

        return bestScores

    def printScoreboard(self):
        for score in self.bestScores:
            print ('{} {}'.format(score[0], score[1]))

    def updateScoreboard(self, score):
        bestScores = self.bestScores
        bestScores.append(score)
        bestScores.sort(reverse=True)
        bestScores = bestScores[:10]

        scoreboard = open('scoreboard.txt', 'w')
        for score in bestScores:
            score[1].strip('\n')
            scoreLine = str(score[0]) + " " + score[1] + '\n'
            scoreboard.write(scoreLine)

        scoreboard.close()
