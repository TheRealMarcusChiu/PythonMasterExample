# https://towardsdatascience.com/q-learning-54b841f3f9e4
import pandas as pd
import random


class Game:
    rewards = None
    positionCol = None
    positionRow = None

    def __init__(self, start_col=1, start_row=1):
        self.distance = pd.DataFrame(
            {1: [8, 7, 6, 5, 4], 2: [7, 6, 5, 4, 3], 3: [6, 5, 4, 3, 2], 4: [5, 4, 3, 2, 1], 5: [4, 3, 2, 1, 0]},
            index={1, 2, 3, 4, 5})
        self.rewards = pd.DataFrame(
            {1: [0, 1, 2, 3, 4], 2: [1, 2, 3, 4, 5], 3: [2, 3, 4, 5, 6], 4: [3, 4, 5, 6, 7], 5: [4, 5, 6, 7, 8]},
            index={1, 2, 3, 4, 5})
        self.positionCol = start_col
        self.positionRow = start_row

    def move(self, direction):
        reward = 0
        end = False
        distance_before = self.distance[self.positionCol][self.positionRow]
        if direction == 'Up':
            self.positionRow -= 1
        elif direction == 'Down':
            self.positionRow += 1
        elif direction == 'Left':
            self.positionCol -= 1
        else:
            self.positionCol += 1

        # check if we lost
        if self.positionRow < 1 or self.positionRow > 5 or self.positionCol < 1 or self.positionCol > 5:
            end = True
            reward = -1000
            # check if we have reached the end
        elif self.positionCol == 5 and self.positionRow == 5:
            end = True
            reward = self.rewards[self.positionCol][self.positionRow]
        else:
            end = False
            if distance_before < self.distance[self.positionCol][self.positionRow]:
                reward = -1000
            else:
                reward = self.rewards[self.positionCol][self.positionRow]

        # return reward and end of game indicator
        return reward, end


# states are in columns and actions are in rows
learning_rate = 1
discount = 1
random_explore = 0.3
q_table = pd.DataFrame(100, index=['Up', 'Down', 'Left', 'Right'],
                       columns=[11, 12, 13, 14, 15, 21, 22, 23, 24, 25, 31, 32, 33, 34, 35, 41, 42, 43, 44, 45, 51, 52,
                                53, 54, 55])

# print(q_table) would output
#         11   12   13   14   15   21   22  ...   44   45   51   52   53   54   55
# Up     100  100  100  100  100  100  100  ...  100  100  100  100  100  100  100
# Down   100  100  100  100  100  100  100  ...  100  100  100  100  100  100  100
# Left   100  100  100  100  100  100  100  ...  100  100  100  100  100  100  100
# Right  100  100  100  100  100  100  100  ...  100  100  100  100  100  100  100

for i in range(1000):
    game = Game()
    end_of_game = False
    while not end_of_game:
        # get current state state names are integers for ease of coding, it will be a two digit number with
        # 1st digit = Col number
        # 2nd digit = Row number
        current_state = (game.positionCol * 10) + game.positionRow
        # select the action with maximum reward
        max_reward_action = q_table[current_state].idxmax()
        # replace with random action to promote exploration and not get stuck in a loop
        if random.random() < random_explore:
            max_reward_action = q_table.index[random.randint(0, 3)]
        # play the game with that action
        reward, end_of_game = game.move(max_reward_action)
        # if (current_state==12): print("CS:" + str(current_state) + ", Action: " + max_reward_action + ", Reward: "
        # + str(reward)) if end of game, then if the game is over, then no need to update the q value for the action
        # taken, but is set to the reward value observed
        if end_of_game:
            q_table.loc[max_reward_action, current_state] = reward
        else:
            optimal_future_value = q_table[(game.positionCol * 10) + game.positionRow].max()
            discounted_optimal_future_value = discount * optimal_future_value
            learned_value = reward + discounted_optimal_future_value
            q_table.loc[max_reward_action, current_state] = (1 - learning_rate) * q_table[current_state][
                max_reward_action] + learning_rate * learned_value

print(q_table)
