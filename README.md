# 🧠 AI Workflows with LangGraph

A comprehensive toolkit demonstrating advanced AI workflow patterns using LangGraph. This repository serves as the official companion code for the YouTube series "AI Workflows with LangGraph."

## 🔍 Overview

This project showcases various implementation patterns for building sophisticated AI workflows using LangGraph, a framework that extends LangChain with native support for stateful, multi-actor systems. Each implemented pattern provides a complete example that can be adapted to different use cases.

## 🛠️ Prerequisites

- **Python 3.11+**
- **API Keys:**
  - OpenAI API key (for accessing language models)
  - LangSmith API keys (for traces and debugging in LangGraph Studio)
- **Virtual Environment:** We recommend using a virtual environment manager (venv, conda, etc.)

## 🚀 Getting Started

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-repository/ai-workflows-with-langgraph.git
   cd ai-workflows-with-langgraph
   ```

2. **Set up virtual environment**

   ```bash
   # Create a virtual environment
   python -m venv venv

   # Activate on Windows
   venv\Scripts\activate

   # Activate on macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

### ⚙️ Configuration

Create a `.env` file in the project root with the following environment variables:

```
OPENAI_API_KEY=your_openai_api_key
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_PROJECT=your_project_name  # Optional, for organizing traces
```

## 📁 Repository Structure

```
ai-workflows-with-langgraph/
├── .env.example            # Template for environment variables
├── requirements.txt        # Project dependencies
├── prompt_chaining/        # Pattern: Sequential Prompt Chaining
│   ├── README.md           # Pattern-specific documentation
│   ├── agent.py            # Implementation of the workflow
│   ├── utils/              # Helper functions & utilities
│   └── mock_data/          # Sample data for testing
└── [additional_patterns]/  # Other workflow patterns
```

## 📊 LangGraph Studio Integration

All patterns in this repository are designed to work seamlessly with LangGraph Studio, providing visualization and debugging capabilities for complex workflows.

To use LangGraph Studio with any pattern:

1. Ensure you have set up the required environment variables in your `.env` file
2. Run:

   ```bash
   langgraph dev
   ```

This launches the LangGraph Studio interface, allowing you to:
- 📈 Visualize your workflow as a graph
- 🔍 Trace execution paths
- 🔎 Inspect intermediate states
- 🐛 Debug complex interactions between workflow components

## 🧩 AI Workflows Patterns

### ⛓️ 1. Sequential Prompt Chaining (`prompt_chaining/`)

A foundational pattern demonstrating how to chain multiple prompts together, where each stage's output serves as input to subsequent stages. This pattern implements a product description generator that transforms raw product data into various forms of marketing content.

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch
3. Implement your changes
4. Submit a pull request

For bug reports or feature requests, please open an issue.

## 📄 License

[MIT License](LICENSE)


