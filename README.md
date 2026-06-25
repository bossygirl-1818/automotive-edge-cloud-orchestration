# 🚗 Self-Adaptive Task Orchestration for the Automotive Edge–Cloud Continuum

### Intelligent AI-Based Workload Orchestration for Software-Defined Vehicles (SDVs)

> **Final Year B.Tech Project | Computer Science & Engineering | Hindustan Institute of Technology and Science** > **Author:** Vaishnavi Senthilkumar  
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