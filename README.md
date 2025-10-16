# 🤖 AgroMind Agent Simulator

A simple yet powerful web application built with Python and Streamlit to demonstrate a multi-agent AI system for agricultural decision-making. This project serves as a proof-of-concept for collaborative AI, inspired by recent research like Google's TUMIX paper.

![GIF of the Streamlit App in Action]

## 🎯 The Mission

The system deploys a team of specialized AI agents to answer a critical question: **Should we irrigate the crops?** Each agent has a unique role, and their collaboration leads to an informed, data-driven recommendation.

---

## ✨ Features

* **Interactive Interface:** Enter any geographic coordinates (latitude/longitude) to get a real-time analysis.
* **Real-Time Climate Data:** The **Climate Agent** fetches live weather data from the Open-Meteo API.
* **Simulated Satellite Analysis:** The **Satellite Agent** provides a simulated Normalized Difference Vegetation Index (NDVI) to assess crop health.
* **Logic-Driven Decisions:** The **Decision Agent** synthesizes data from the other agents to provide a clear, actionable recommendation.
* **Modular Architecture:** The code is designed to be easily extendable. The simulated satellite agent can be replaced with real satellite imagery APIs like Sentinel Hub or Google Earth Engine.

---

## 🚀 Getting Started

### Prerequisites

* Python 3.8+
* pip

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/AgroMind-Agent-Simulator.git](https://github.com/YOUR_USERNAME/AgroMind-Agent-Simulator.git)
    cd AgroMind-Agent-Simulator
    ```

2.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: If you don't have a `requirements.txt` file, you can create one with `streamlit` and `requests` or just run `pip install streamlit requests`)*

### Running the App

1.  **Launch the Streamlit app from your terminal:**
    ```bash
    streamlit run app.py
    ```

2.  Your browser will automatically open a new tab with the application running.

---

## 💡 Concept

This project demonstrates the power of a **multi-agent system**, where specialized, simpler models collaborate to solve a complex problem. This approach is often more robust, interpretable, and scalable than relying on a single, monolithic AI model.
