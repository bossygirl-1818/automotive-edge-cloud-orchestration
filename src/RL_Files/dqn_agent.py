import random
from collections import deque

import torch
import torch.nn as nn
import torch.optim as optim


class DQNNetwork(nn.Module):
    def __init__(self, state_size, action_size):
        super(DQNNetwork, self).__init__()

        self.model = nn.Sequential(
            nn.Linear(state_size, 128),
            nn.ReLU(),

            nn.Linear(128, 128),
            nn.ReLU(),

            nn.Linear(128, action_size)
        )

    def forward(self, x):
        return self.model(x)


class DQNAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size

        self.memory = deque(maxlen=10000)

        self.gamma = 0.95
        self.epsilon = 1.0
        self.epsilon_min = 0.05
        self.epsilon_decay = 0.995

        self.learning_rate = 0.001
        self.batch_size = 64

        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu"
        )

        self.model = DQNNetwork(
            state_size,
            action_size
        ).to(self.device)

        self.optimizer = optim.Adam(
            self.model.parameters(),
            lr=self.learning_rate
        )

        self.loss_fn = nn.MSELoss()

    def remember(
        self,
        state,
        action,
        reward,
        next_state,
        done
    ):
        self.memory.append(
            (
                state,
                action,
                reward,
                next_state,
                done
            )
        )

    def act(self, state):
        if random.random() <= self.epsilon:
            return random.randrange(self.action_size)

        state_tensor = torch.FloatTensor(state).unsqueeze(0).to(self.device)

        with torch.no_grad():
            q_values = self.model(state_tensor)

        return torch.argmax(q_values).item()

    def replay(self):
        if len(self.memory) < self.batch_size:
            return

        minibatch = random.sample(
            self.memory,
            self.batch_size
        )

        states = []
        targets = []

        for state, action, reward, next_state, done in minibatch:

            state_tensor = torch.FloatTensor(state).to(self.device)
            next_state_tensor = torch.FloatTensor(next_state).to(self.device)

            target = self.model(state_tensor).detach().clone()

            if done:
                target[action] = reward
            else:
                with torch.no_grad():
                    next_q_values = self.model(next_state_tensor)
                    target[action] = reward + self.gamma * torch.max(next_q_values)

            states.append(state)
            targets.append(target.cpu())

        states_tensor = torch.FloatTensor(states).to(self.device)
        targets_tensor = torch.stack(targets).to(self.device)

        predictions = self.model(states_tensor)

        loss = self.loss_fn(
            predictions,
            targets_tensor
        )

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def save(self, path):
        torch.save(
            self.model.state_dict(),
            path
        )

    def load(self, path):
        self.model.load_state_dict(
            torch.load(
                path,
                map_location=self.device
            )
        )

        self.model.eval()