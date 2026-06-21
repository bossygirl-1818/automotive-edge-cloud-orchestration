# 🚗 Self-Adaptive Task Orchestration for the Automotive Edge–Cloud Continuum

## 📌 Overview

Modern connected and autonomous vehicles continuously generate computational workloads ranging from safety-critical perception tasks to cloud-scale analytics. Executing every workload onboard increases computational load and battery consumption, while offloading everything to the cloud introduces network latency and communication overhead.

This project presents a **Self-Adaptive Task Orchestration Framework** that dynamically determines the optimal execution environment for automotive workloads across:

* 🚗 Vehicle (Onboard Computing)
* 📡 Edge Infrastructure
* ☁️ Cloud Infrastructure

The system combines **Machine Learning**, **Deep Reinforcement Learning (DQN)**, and **Hybrid Decision Fusion** to optimize task execution in real time.

---

# 🎯 Project Objectives

The orchestration framework aims to:

* Minimize latency
* Reduce vehicle resource consumption
* Improve task completion rate
* Increase energy efficiency
* Optimize workload distribution
* Adapt dynamically to changing conditions

---

# 🏗️ System Architecture

```text
Vehicle Sensors
       │
       ▼
Task Generator
       │
       ▼
Resource Monitor
       │
       ▼
ML Orchestrator
       │
       ▼
DQN Orchestrator
       │
       ▼
Hybrid Orchestrator
       │
 ┌─────┼─────┐
 │     │     │
 ▼     ▼     ▼
Vehicle Edge Cloud
       │
       ▼
Telemetry Collector
       │
       ▼
Analytics Layer
       │
       ▼
BMW Dashboard
       │
       ▼
Reports & Executive Summary
```

---

# 🧠 Core Features

## Machine Learning Orchestrator

Models:

* Decision Tree
* Random Forest
* Gradient Boosting

Predicts:

* VEHICLE
* EDGE
* CLOUD

execution targets based on:

* Vehicle CPU
* Battery Level
* Task Size
* Task Priority
* Network Delay
* Bandwidth

---

## Deep Reinforcement Learning Orchestrator

Implemented using Deep Q-Networks (DQN).

Features:

* State-Aware Decisions
* Reward Optimization
* Adaptive Offloading
* Continuous Learning

Outputs:

* RL Decision
* Reward Score
* Performance Feedback

---

## Hybrid Orchestrator

Combines:

```text
ML Decision
+
DQN Decision
=
Final Orchestration Decision
```

Provides:

* More robust decisions
* Improved adaptability
* Higher reliability

---

## Real-Time Resource Monitoring

Monitors:

### Vehicle

* CPU Utilization
* Battery Level

### Edge

* Edge Load
* Network Delay

### Cloud

* Cloud Load
* Network Delay

---

# 📊 Analytics Layer

The dashboard includes:

### Reward Analytics

Tracks reinforcement learning rewards.

### DQN Learning Curve

Visualizes agent learning progress.

### Decision Analytics

Shows:

* Vehicle %
* Edge %
* Cloud %

distribution.

### Latency Analytics

Evaluates response-time trends.

### Energy Analytics

Tracks battery consumption.

### Benchmark Comparison

Compares:

* ML
* DQN
* Hybrid Orchestrator

performance.

### Offloading Distribution

Visualizes workload allocation across resources.

---

# 📈 Dashboard Features

Built using Streamlit and Plotly.

Includes:

* Live ML Decision
* DQN Decision
* Hybrid Decision
* Task Queue
* Explainability Engine
* Resource Monitoring
* Network Topology
* Performance Analytics
* Executive Summary
* PDF Report Generation

---

# 📂 Project Structure

```text
automotive-edge-cloud-orchestration/
│
├── data/
│
├── src/
│   ├── task_generator.py
│   ├── resource_monitor.py
│   ├── ml_orchestrator.py
│   ├── evaluator.py
│   ├── edge_selector.py
│   │
│   └── RL_Files/
│       ├── dqn_agent.py
│       ├── environment.py
│       ├── train_dqn.py
│       ├── evaluate_dqn.py
│       ├── rl_simulator.py
│       ├── telemetry_simulator.py
│       └── realistic_rl_simulation.py
│
├── dashboard/
│   ├── app.py
│   └── components/
│
├── docs/
│
├── tests/
│
├── README.md
├── requirements.txt
└── main.py
```

---

# 🛠️ Technology Stack

## Programming

* Python

## Data Processing

* Pandas
* NumPy

## Machine Learning

* Scikit-Learn

## Deep Reinforcement Learning

* PyTorch

## Dashboard

* Streamlit

## Visualization

* Plotly
* Matplotlib

## Reporting

* ReportLab

## Version Control

* Git
* GitHub

---

# 📊 Current Results

### Supported Execution Targets

* 🚗 Vehicle
* 📡 Edge
* ☁️ Cloud

### Decision Engines

* Machine Learning
* Deep Reinforcement Learning
* Hybrid Orchestration

### Analytics

* Reward Analytics
* Decision Analytics
* Latency Analytics
* Energy Analytics
* Benchmark Comparison

---

# 🚀 Running the Project

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Train Machine Learning Models

```bash
python -m src.train_model
```

## Train DQN Agent

```bash
python -m src.RL_Files.train_dqn
```

## Generate RL Evaluation Data

```bash
python -m src.RL_Files.realistic_rl_simulation
```

## Generate Telemetry Data

```bash
python -m src.RL_Files.telemetry_simulator
```

## Launch Dashboard

```bash
streamlit run dashboard/app.py
```

---

# 🔮 Future Roadmap

## Phase 9

Database & Persistence Layer

* SQLite
* PostgreSQL

## Phase 10

Advanced Hybrid Intelligence

* Confidence-Based Fusion
* Reward-Based Fusion

## Phase 11

BMW Automotive Features

* Driving Modes
* Vehicle Profiles
* Road Scenarios

## Phase 12

SimPy Event Simulation

## Phase 13

Prometheus + Grafana Monitoring

## Phase 14

Research Contribution Layer

## Phase 15

SUMO Traffic Simulation

## Phase 16

Docker & AWS Deployment

## Phase 17

SHAP Explainability

---

# 🎓 Research Domains

This project integrates:

* Machine Learning
* Deep Reinforcement Learning
* Edge Computing
* Cloud Computing
* Automotive AI
* Explainable AI
* Intelligent Transportation Systems

---

# 👩‍💻 Author

**Vaishnavi Senthilkumar**

Computer Science Student
AI / ML | Software Development | Intelligent Systems

LinkedIn:
https://www.linkedin.com/in/vaishnavi-senthil-kumar-477262305/

---

# ⭐ BMW Relevance

The project aligns with:

* Connected Vehicles
* Intelligent Transportation Systems
* Edge AI
* Smart Mobility
* Vehicle-to-Cloud Communication
* Automotive Resource Optimization
* Autonomous Driving Support Systems

This framework serves as a prototype for intelligent workload orchestration in future connected vehicle ecosystems.
