# 🤖 AI Test Generator for Jira + Xray (CrewAI)

This project uses CrewAI agents to generate software test cases and automatically create Xray Tests in Jira.

## ✨ Features

* AI-generated test cases from requirements
* Automatic Xray Test creation
* Works with Jira Cloud + Xray Cloud
* Built with CrewAI

## 🧠 Tech Stack

* Python
* CrewAI
* Jira Cloud
* Xray Cloud API
* uv (Python package manager)

## 🚀 Setup

### 1. Clone the repository

```
git clone https://github.com/qadir-dev-hub/ai-xray-test-generator
cd YOUR_REPO
```

### 2. Install dependencies

```
uv sync
```

### 3. Configure environment variables

Copy the example file:

```
copy .env.example .env
```

Then open `.env` and add your credentials.

### 4. Run the project

```
uv run main.py
```

## 🔐 Required API Credentials

Create Xray Cloud API credentials and set:

* XRAY_CLIENT_ID
* XRAY_CLIENT_SECRET

## 📚 Use Case

Built as part of an exploration into Agentic AI for Quality Engineering.

## 📝 License

MIT License
