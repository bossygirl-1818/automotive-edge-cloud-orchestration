
# Self-Adaptive Task Orchestration for the Automotive Edge–Cloud Continuum

## Project Goal

Develop an intelligent orchestration system that dynamically decides where automotive workloads should execute:

* Onboard Vehicle
* Edge Server
* Cloud Server

The system should optimize:

* Response Time (Latency)
* Resource Utilization
* Throughput
* Task Completion Rate

---

## Real-World Problem

Modern autonomous vehicles generate thousands of tasks every second.

Examples:

| Task                     | Latency Requirement |
| ------------------------ | ------------------- |
| Lane Detection           | Very High           |
| Obstacle Detection       | Very High           |
| Traffic Sign Recognition | High                |
| Route Planning           | Medium              |
| Driving Analytics        | Low                 |

Not every task should be processed in the cloud.

Some tasks must stay inside the vehicle.

Some tasks can be offloaded to an edge server.

Some tasks can be sent to the cloud.

The challenge is deciding automatically where each task should run.

---

## System Architecture


Vehicle Sensors
       │
       ▼
Task Generator
       │
       ▼
Task Queue
       │
       ▼
Resource Monitor
       │
       ▼
Decision Engine
       │
 ┌─────┼─────┐
 │     │     │
 ▼     ▼     ▼
Vehicle Edge Cloud
       │
       ▼
Metrics Collector
       │
       ▼
Dashboard


---

## Project Modules

### Module 1: Task Generator

#### Purpose

Generate automotive tasks.

#### Example

```json
{
  "task_id": 1,
  "task_type": "lane_detection",
  "latency_requirement": 10,
  "cpu_requirement": 50,
  "memory_requirement": 100
}
```

#### Task Types

* Lane Detection
* Obstacle Detection
* Traffic Sign Recognition
* Route Planning
* Vehicle Diagnostics

---

### Module 2: Resource Monitor

#### Purpose

Monitor resources across the system.

#### Vehicle

CPU Usage
Memory Usage
Battery Level


#### Edge


CPU Usage
Memory Usage
Network Delay


#### Cloud


CPU Usage
Memory Usage
Network Delay


---

### Module 3: Decision Engine

#### Purpose

Determine the best execution location.

### Version 1: Rule-Based

```python
if latency_requirement <= 20:
    execute_on_vehicle()

elif latency_requirement <= 100:
    execute_on_edge()

else:
    execute_on_cloud()
```

### Version 2: Adaptive Decision Making

Decision factors:

* Latency
* CPU Load
* Memory Load
* Network Delay
* Battery Level

Output:

* Vehicle
* Edge
* Cloud

---

### Module 4: Execution Simulator

#### Purpose

Simulate workload execution.

#### Test Cases


100 Tasks
500 Tasks
1000 Tasks
5000 Tasks


#### Outputs


Execution Time
Average Latency
Task Completion Rate
Failed Tasks


---

### Module 5: Metrics Collector

#### Purpose

Measure system performance.

#### Metrics

* Average Latency
* Throughput
* Resource Utilization
* Offloading Ratio
* Task Completion Rate

#### Example


Vehicle: 40%
Edge: 35%
Cloud: 25%


---

### Module 6: Dashboard

#### Technology


Streamlit
Plotly


#### Dashboard Features

### System Overview


Vehicle Load
Edge Load
Cloud Load


### Task Statistics


Tasks Processed
Tasks Completed
Tasks Failed


### Graphs


Latency Graph
Resource Utilization Graph
Task Distribution Graph


---

## Technology Stack

### Programming Language


Python


### Data Processing


NumPy
Pandas


### Machine Learning


Scikit-learn


### Dashboard


Streamlit
Plotly


### Visualization


Matplotlib


### Version Control


Git
GitHub


---

## Folder Structure


automotive-edge-cloud-orchestration/
│
├── data/
│
├── src/
│   ├── task_generator.py
│   ├── resource_monitor.py
│   ├── decision_engine.py
│   ├── simulator.py
│   └── metrics.py
│
├── dashboard/
│   └── app.py
│
├── docs/
│   └── PROJECT_PLAN.md
│
├── tests/
│
├── requirements.txt
├── README.md
└── main.py


---

## Development Roadmap

### Phase 1

Project Setup

### Phase 2

Task Generator

### Phase 3

Resource Monitor

### Phase 4

Rule-Based Decision Engine

### Phase 5

Execution Simulator

### Phase 6

Metrics Collection

### Phase 7

Machine Learning-Based Adaptive Orchestrator

### Phase 8

Dashboard Development

### Phase 9

Testing & Validation

### Phase 10

GitHub Deployment & Documentation

---

## Expected Outcomes

* Reduced latency compared to static task allocation.
* Better resource utilization across vehicle, edge, and cloud.
* Dynamic task offloading based on real-time conditions.
* Demonstration of an automotive edge-cloud orchestration framework.

---

## Resume Description

**Self-Adaptive Task Orchestration for the Automotive Edge–Cloud Continuum**

* Developed an intelligent orchestration framework for autonomous vehicle workloads across onboard, edge, and cloud environments.
* Designed a latency-aware decision engine for dynamic task offloading based on resource availability and real-time constraints.
* Simulated automotive workloads and evaluated system performance using latency, throughput, and resource-utilization metrics.
* Implemented an adaptive orchestration model using Python, Streamlit, and Machine Learning.

---

## Success Criteria

The project will be considered successful if it:

* Correctly classifies and routes tasks.
* Demonstrates lower average latency than static approaches.
* Maintains high task completion rates.
* Provides clear performance visualizations.
* Is fully documented and deployable through GitHub.


