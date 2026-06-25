
# 🚗 Self-Adaptive Task Orchestration for the Automotive Edge–Cloud Continuum

### Intelligent AI-Based Workload Orchestration for Software-Defined Vehicles (SDVs)

> **Final Year B.Tech Project | Computer Science & Engineering | Hindustan Institute of Technology and Science**
> 
> **Author:** Vaishnavi Senthilkumar  
> **Specialization:** Artificial Intelligence · Distributed Systems · Cloud-Native Infrastructure · Edge Computing

---

## 🌟 Executive Summary

Modern Software-Defined Vehicles (SDVs) execute highly complex, computationally intensive workloads such as perception, autonomous driving support, localized diagnostics, and connected cloud services. In a safety-critical automotive environment, determining exactly *where* to execute these workloads (locally on-vehicle, on a nearby Multi-access Edge Computing server, or in the centralized Cloud) is a massive optimization challenge.

* **The On-Vehicle Dilemma:** Executing all workloads locally triggers high CPU utilization, excessive battery drain, and thermal stress.
* **The Cloud Dilemma:** Offloading everything introduces variable network latency and packet-loss vulnerabilities, which are unacceptable for safety-critical systems.

This project delivers an end-to-end **Self-Adaptive Automotive Edge–Cloud Task Orchestration Framework**. By leveraging a **Hybrid Intelligence Engine** (fusing supervised Machine Learning with Deep Reinforcement Learning), the platform dynamically optimizes workload placement in real time based on vehicle telemetry, environment context, and network volatility.

The entire architecture is containerized via Docker, fully instrumented using **9 dedicated Prometheus metric exporters** feeding an enterprise-grade Grafana observability stack, and exposed through a 12-module Streamlit executive control dashboard—modeling a production-ready, cloud-native connected vehicle ecosystem.

---

## 📊 Key Results at a Glance

All metrics are benchmarked and verified through deterministic, large-scale traffic and telemetry workloads.

| Metric | Evaluation & Value | Strategic Impact |
| :--- | :--- | :--- |
| **ML Workload Placement Accuracy** | **99.7%** (Random Forest & Gradient Boosting) | High-fidelity initial classification of incoming tasks. |
| **DQN Latency Reduction** | **7.6% improvement** (44.80ms vs 48.50ms) | Outperforms standard deterministic rule-based baselines. |
| **DQN Reward Optimization** | **61.2% increase** (137.06 vs 85.00) | Validates optimal convergence of multi-objective reward math. |
| **Cloud Offload Mitigation** | **74.2% of tasks kept local/edge** | Drastically minimizes cellular backhaul bandwidth & costs. |
| **Total Simulated Workloads** | **15,000+ Tasks** | Validates framework stability under intensive, multi-vehicle load. |
| **Active Simulated Fleet Scale** | **30 Concurrent Vehicles** | Proves multi-tenant orchestration capabilities via SUMO. |
| **Observability Footprint** | **9 Dedicated Metric Exporters** | Comprehensive white-box telemetry across the entire system. |
| **Self-Adaptive Override Rate** | **12.4% Runtime Adjustments** | Dynamic closed-loop protection against edge-case anomalies. |
| **Explainable AI (XAI) Footprint** | **700 Decision Audits** | Meets ISO 26262 auditability concepts for safety validation. |

> 📌 *Note on Data Integrity: To ensure absolute experimental control, this framework is evaluated using highly realistic synthetic telemetry and environment parameters generated deterministically through SUMO traffic simulation to stress-test edge-cloud network volatility.*

---

## 🏗️ System Architecture & Data Flow

The platform is designed as a closed-loop, self-adaptive system where telemetry from the physical/simulated layer continuously optimizes the intelligent decision engines.

```
                        Vehicle Sensors
                               │
                               ▼
                     Task Generation Layer
                               │
                               ▼
                    Resource Monitoring Layer
                               │
                               ▼
                  Machine Learning Orchestrator
                      (99.7% accuracy)
                               │
                               ▼
                Deep Reinforcement Learning Agent
                         (DQN — PyTorch)
                               │
                               ▼
                 Hybrid Decision Fusion Engine
                               │
         ┌─────────────────────┼─────────────────────┐
         ▼                     ▼                     ▼
     Vehicle               Edge Server            Cloud
   (5,626 tasks)         (5,505 tasks)         (3,869 tasks)
         │                     │                     │
         └──────────────┬──────┴──────────────┬──────┘
                        ▼                     ▼
              Telemetry Collection     Digital Twin
                        │
                        ▼
               Predictive Analytics Engine
                        │
                        ▼
               Explainable AI (XAI)
                  (700 decisions)
                        │
                        ▼
             Self-Adaptive Intelligence
               (12.4% override rate)
                        │
                        ▼
   Prometheus (×9) → Grafana → Streamlit Dashboard
```

---

## 🔄 End-to-End Workflow

```
Vehicle Generates Task
          │
          ▼
Collect Vehicle Resources (CPU, Battery, Network)
          │
          ▼
Machine Learning Prediction (Decision Tree / RF / GB)
          │
          ▼
DQN Reinforcement Learning Decision
          │
          ▼
Hybrid Decision Fusion (ML + RL)
          │
          ▼
Vehicle / Edge / Cloud Selection
          │
          ▼
Task Execution
          │
          ▼
Telemetry Collection → SQLite Logging
          │
          ▼
Performance Analytics
          │
          ▼
XAI Explanation (human-readable reason)
          │
          ▼
Self-Adaptive Optimization (override if needed)
          │
          ▼
Prometheus Metrics (9 exporters)
          │
          ▼
Grafana Dashboard → Streamlit Executive Dashboard
```

---
## 📂 Project Structure

```
automotive-edge-cloud-orchestration/
│
├── dashboard/
│   ├── app.py                          # Main Streamlit app (12 modules)
│   ├── components/                     # 40+ modular dashboard components
│   │   ├── live_prediction.py
│   │   ├── rl_decision.py
│   │   ├── hybrid_orchestrator.py
│   │   ├── digital_twin_dashboard.py
│   │   ├── explainable_orchestrator_dashboard.py
│   │   ├── self_adaptive_dashboard.py
│   │   └── ...
│   └── styles/
│       └── dashboard.css
│
├── src/
│   ├── RL_Files/                       # DQN agent, environment, trainer, evaluator
│   │   ├── dqn_agent.py
│   │   ├── environment.py
│   │   ├── train_dqn.py
│   │   └── evaluate_dqn.py
│   ├── ml_orchestrator.py
│   ├── digital_twin.py
│   ├── digital_twin_rl_fusion.py       # Digital Twin + RL fusion
│   ├── explainable_orchestrator.py
│   ├── self_adaptive_controller.py
│   ├── predictive_traffic_engine.py
│   ├── fleet_simulation.py
│   ├── metrics_exporter.py             # Prometheus exporters
│   └── ...
│
├── data/
│   ├── dqn_orchestrator.pth            # Trained DQN model
│   ├── random_forest.pkl               # Trained RF model (99.7%)
│   ├── gradient_boosting.pkl           # Trained GB model (99.7%)
│   ├── model_comparison.csv            # ML benchmark results
│   ├── strategy_comparison.csv         # Strategy benchmark results
│   ├── dqn_training_rewards.csv
│   ├── orchestrator.db                 # SQLite decision log
│   └── ...
│
├── sumo/
│   ├── network.net.xml                 # Custom SUMO road network
│   ├── routes.rou.xml
│   └── advanced/                       # Advanced custom network
│
├── tests/
│   ├── test_ml.py
│   ├── test_evaluator.py
│   └── ...
│
├── docs/
│   └── images/
│
├── Dockerfile
├── docker-compose.yml
├── docker-compose.prod.yml
├── prometheus.yml
├── requirements.txt
└── README.md
```

---

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Language | Python 3.11 |
| Machine Learning | Scikit-Learn (Decision Tree, Random Forest, Gradient Boosting) |
| Deep Learning | PyTorch (DQN) |
| Dashboard | Streamlit |
| Visualization | Plotly, Matplotlib |
| Traffic Simulation | SUMO, TraCI, SimPy |
| Monitoring | Prometheus, Grafana |
| Deployment | Docker, Docker Compose |
| Database | SQLite |
| Cloud | AWS EC2 (deployment ready) |
| Version Control | Git, GitHub |

---

## 🤖 Core Artificial Intelligence Modules

### 🚗 Machine Learning Orchestrator

The ML Orchestrator is the first decision layer. It classifies each incoming task into the optimal execution environment using vehicle resource state and network conditions.

**Algorithms:** Decision Tree, Random Forest, Gradient Boosting

**Input Features:**
- Vehicle CPU Utilization
- Battery Level
- Task Size & Priority
- Edge Network Delay
- Cloud Network Delay

**Results:**

| Model | Accuracy |
|---|---|
| Decision Tree | 99.4% |
| Random Forest | **99.7%** |
| Gradient Boosting | **99.7%** |

---

### 🧠 Deep Reinforcement Learning (DQN) Orchestrator

A Deep Q-Network (DQN) agent learns optimal task placement by interacting with the simulated automotive environment. It continuously improves without manual rule updates.

**State Space:** CPU usage, battery %, task latency, task priority, task size, edge delay, cloud delay

**Action Space:** Execute on Vehicle | Offload to Edge | Offload to Cloud

**Reward Function:** Minimizes latency + energy consumption + overload penalty + execution failure rate

**Results (1,000 tasks):**

| Strategy | Avg Latency (ms) | Avg Reward |
|---|---|---|
| Rule-Based | 48.50 | 85.0 |
| ML-Based | 46.69 | 110.0 |
| **Deep RL (DQN)** | **44.80** | **137.06** |

---

### 🔄 Hybrid Decision Engine

Combines ML classification and DQN reinforcement learning into a single fused decision.

```
ML Prediction + DQN Decision → Hybrid Fusion → Final Execution Target
```

The Hybrid Engine delivers superior robustness, outperforming either component independently.

---

### 🏙️ Digital Twin

Maintains a continuously updated virtual model of each vehicle's computational state, mirroring CPU, battery, latency, resource availability, and task queue. Enables safe experimentation without affecting physical vehicles.

**Live metrics (Grafana):** Avg Edge CPU: 49.7% | Avg Cloud Latency: 83ms | 5 twin active vehicles

---

### 🚦 SUMO Traffic Intelligence

Integrates SUMO (Simulation of Urban Mobility) with a **custom-built road network** (nodes, edges, routes). Traffic metrics including vehicle density, congestion, speed, and queue length directly influence orchestration decisions.

**Scale:** 1,304 SUMO tasks processed | 30 simulated vehicles

---

### 📈 Predictive Analytics

Forecasts future system resource behavior using historical telemetry.

**Live predictions (Grafana):**
- Predicted Congestion Score: 80.3
- Predicted Edge Load: 62.4%
- Predicted Cloud Latency: 101ms
- Predicted Battery Drain: 46.8%
- Forecast History: 15,000 records

---

### 🔍 Explainable AI (XAI)

Provides human-readable justifications for every orchestration decision. Essential for safety-critical automotive validation.

**Example explanations:**
- *"Edge selected due to lower latency."*
- *"Vehicle execution avoided due to high CPU utilization."*
- *"Cloud selected for large computational workload."*

**Scale:** 700 decisions explained | EDGE: 162 | CLOUD: 138 | VEHICLE: 400

---

### ⚙️ Self-Adaptive Intelligence

Monitors system performance in real time and overrides suboptimal decisions autonomously.

**Live results (Grafana):** 700 adaptive records | 87 overrides | **12.4% override rate** | Final EDGE: 291 | CLOUD: 128 | VEHICLE: 281

---

## 📊 Monitoring & Observability

### Prometheus — 9 Dedicated Metric Exporters

| Port | Exporter |
|---|---|
| 8000 | Core Orchestrator |
| 8001 | SUMO Traffic |
| 8002 | Advanced Traffic |
| 8003 | Traffic RL |
| 8004 | Digital Twin |
| 8005 | Predictive Traffic |
| 8006 | Forecast History |
| 8007 | Explainable AI |
| 8008 | Self-Adaptive Controller |

### Grafana Dashboard Panels

- Vehicle CPU Usage Gauge
- Battery Level
- Network Latency
- Edge Server Load
- Cloud Server Load
- Average RL Reward
- Decision Distribution (pie chart)
- SUMO Task Count
- Active Vehicles
- Edge/Cloud/Vehicle Offload counts
- Digital Twin State
- Predictive Forecasts
- Self-Adaptive Override Rate
- XAI Decision Breakdown

### Streamlit Executive Dashboard (12 Modules)

| Module | Description |
|---|---|
| Overview | Platform KPIs and executive summary |
| Core Orchestrator | Live ML + DQN + Hybrid decisions |
| RL Intelligence | DQN reward curves, learning analytics |
| SUMO Traffic | Traffic simulation dashboard |
| Advanced Traffic | Latency, energy, benchmark analytics |
| Digital Twin | Fleet and twin state monitoring |
| Predictive Intelligence | Real-time forecasting |
| Forecast History | Historical forecast analytics |
| Explainable AI | XAI decision transparency |
| Self-Adaptive Control | Override and adaptation analytics |
| Database & Reports | Decision history, PDF report generator |
| Monitoring Links | Quick access to Prometheus and Grafana |

---

## 📈 Experimental Results

### ML Model Performance

| Model | Accuracy |
|---|---|
| Decision Tree | 99.4% |
| Random Forest | **99.7%** |
| Gradient Boosting | **99.7%** |

---

### Orchestration Strategy Comparison (1,000 Tasks)

| Strategy | Avg Latency (ms) | Avg RL Reward | Tasks |
|---|---|---|---|
| Rule-Based | 48.50 | 85.0 | 1,000 |
| ML-Based | 46.69 | 110.0 | 1,000 |
| **Deep RL (DQN)** | **44.80** | **137.06** | 1,000 |

- DQN reduced latency by **7.6%** vs rule-based baseline
- DQN improved reward by **61.2%** vs rule-based baseline
- DQN improved reward by **24.6%** vs ML-only strategy

---

### DQN Task Distribution (1,000 Tasks)

| Target | Tasks | Share |
|---|---|---|
| Vehicle | 413 | 41.3% |
| Edge | 396 | 39.6% |
| Cloud | 191 | 19.1% |

Edge + Vehicle = **80.9% of tasks** kept off the cloud.

---

### Large-Scale Simulation (15,000 Tasks via Grafana)

| Metric | Value |
|---|---|
| Total Tasks | 15,000 |
| Active Vehicles | 30 |
| SUMO Tasks Processed | 1,304 |
| Vehicle CPU (avg) | 28% |
| Battery Level (avg) | 52.5% |
| Network Latency (avg) | 93ms |

**Offloading Distribution:**

| Target | Count | Share |
|---|---|---|
| Edge Offloads | 5,505 | 36.7% |
| Vehicle Executions | 5,626 | 37.5% |
| Cloud Offloads | 3,869 | 25.8% |

Edge + Vehicle = **74.2% of tasks** kept off the cloud.

---

### Traffic RL Agent

| Metric | Value |
|---|---|
| RL Accuracy | 79.8% |
| Total RL Records | 15,000 |
| Correct Predictions | 11,973 |

---

### Digital Twin Monitoring

| Metric | Value |
|---|---|
| Digital Twin States | 14 |
| Twin Active Vehicles | 5 |
| Avg Twin Vehicle Speed | 13.6 m/s |
| Avg Twin Battery | 54.6% |
| Avg Edge CPU | 49.7% |
| Avg Cloud Latency | 83.0ms |

---

### Predictive Intelligence

| Prediction | Value |
|---|---|
| Predicted Congestion Score | 80.3 |
| Predicted Edge Load | 62.4% |
| Predicted Cloud Latency | 101ms |
| Predicted Battery Drain | 46.8% |
| Forecast History Records | 15,000 |

---

### Explainable AI

| Metric | Value |
|---|---|
| XAI Total Records | 700 |
| VEHICLE Decisions | 400 (57.1%) |
| EDGE Decisions | 162 (23.2%) |
| CLOUD Decisions | 138 (19.7%) |

---

### Self-Adaptive Control Loop

| Metric | Value |
|---|---|
| Adaptive Records | 700 |
| Override Count | 87 |
| Override Rate | **12.4%** |
| Final EDGE Decisions | 291 |
| Final CLOUD Decisions | 128 |
| Final VEHICLE Decisions | 281 |

---

### Summary

| Achievement | Value |
|---|---|
| Best ML Accuracy | 99.7% |
| DQN Latency Reduction | 7.6% vs rule-based |
| DQN Reward Improvement | 61.2% vs rule-based |
| Cloud Offload Reduction | 74.2% tasks kept local/edge |
| Total Tasks Simulated | 15,000+ |
| Prometheus Exporters | 9 dedicated endpoints |
| Self-Adaptive Override Rate | 12.4% |
| XAI Decisions Explained | 700 |

---

## 🎯 BMW Engineering Relevance

This project was designed with direct alignment to BMW Group's engineering priorities in Software-Defined Vehicles, connected mobility, and intelligent vehicle computing.

### Software-Defined Vehicles (SDV)

BMW's SDV roadmap centers on software-managed workload execution across vehicle compute layers. This project implements exactly this — a dynamic orchestration system that routes tasks between Vehicle, Edge, and Cloud based on real-time resource state. With 74.2% of tasks kept local or at the edge, the framework demonstrates how cloud dependency can be minimized for safety-critical systems.

### Edge Computing for Connected Vehicles

BMW increasingly deploys roadside edge infrastructure (MEC) to reduce latency for ADAS and perception tasks. This project implements a live edge offloading decision engine, achieving a **7.6% latency reduction** over rule-based systems through DQN-driven decisions.

### AI and Autonomous Driving Support

BMW uses ML and RL extensively in autonomous driving stacks. This project demonstrates production-style ML (99.7% accuracy) and DQN deployment with a Hybrid Fusion Engine — showing capability in both supervised and reinforcement learning paradigms.

### Digital Twin Technology

BMW Group actively uses Digital Twin technology for vehicle development and fleet monitoring. This project implements a real-time Digital Twin layer that mirrors vehicle CPU, battery, speed, and network state, enabling safe simulation without affecting physical systems.

### Intelligent Transportation Systems

SUMO-based traffic simulation with a custom-built road network provides realistic vehicle density and congestion context for orchestration decisions — directly applicable to BMW's work on connected vehicle infrastructure.

### Observability and Production Engineering

BMW software teams expect production-grade monitoring. This project runs **9 Prometheus exporters** feeding a live Grafana dashboard — demonstrating familiarity with the observability stack used in real automotive software platforms.

### Explainable AI for Safety Validation

ISO 26262 functional safety standards require traceability of AI decisions in automotive systems. This project's XAI layer provides human-readable justifications for 700 orchestration decisions, directly supporting the kind of decision audit trail that safety engineers require.

### Containerized Deployment

Docker and Docker Compose deployment with production and development configurations aligns with BMW's DevOps and cloud-native engineering practices.

---
## 🛣️ Project Roadmap

### ✅ Completed

- Automotive Edge–Cloud Orchestration
- ML Decision Engine (99.7% accuracy)
- Deep Reinforcement Learning (DQN)
- Hybrid Decision Fusion
- Digital Twin Layer
- SUMO Integration (custom network)
- Predictive Analytics
- Explainable AI (700 decisions)
- Self-Adaptive Intelligence
- Interactive Streamlit Dashboard (12 modules)
- Docker Containerization
- Prometheus (9 exporters) + Grafana Dashboard
- Production Docker Configuration
- SQLite Decision Logging
- Unit Tests

### 🚧 In Progress

- AWS Cloud Deployment
- IEEE Research Paper
- Demo Video Recording
- GitHub Pages Documentation

### 🔮 Future Enhancements

- Kubernetes Deployment
- Multi-Vehicle Coordination
- Federated Learning
- Vehicle-to-Vehicle (V2V) Communication
- Vehicle-to-Infrastructure (V2I) Integration
- Real Automotive Sensor Integration
- CI/CD Pipeline
- Cloud Auto Scaling

---

## 📚 Research Contributions

- Automotive Edge Computing
- Software-Defined Vehicles
- Deep Reinforcement Learning for resource orchestration
- Hybrid ML + RL decision fusion
- Explainable AI for safety-critical systems
- Digital Twin for vehicle state modeling
- Intelligent Transportation Systems
- Containerized AI platform deployment
- Production observability engineering

---

## 👩‍💻 Author

**Vaishnavi Senthilkumar**

Final Year B.Tech Computer Science & Engineering  
Hindustan Institute of Technology and Science

Specialization: Artificial Intelligence · Machine Learning · Edge Computing · Software Engineering · Intelligent Transportation Systems

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/vaishnavi-senthil-kumar-477262305/)

---

## 📄 License

This project is provided for portfolio, educational, and research demonstration purposes. All rights reserved by the author. Please contact the author for permission before copying, modifying, or redistributing any part of this project.

---

## ⭐ Acknowledgements

This project was inspired by ongoing research in Software-Defined Vehicles, Edge Intelligence, Connected Mobility, Reinforcement Learning, Digital Twin Technology, Explainable AI, and Cloud-Native Computing.

If you found this project useful, please consider giving it a ⭐ on GitHub.

---

> *Built to demonstrate production-grade AI engineering for next-generation automotive systems.*

