# Prompt Chaining Example

This directory contains a simple example of prompt chaining using LangGraph - one of the simplest AI workflows.

## Overview

This example demonstrates a product description generator that takes a product ID and goes through several steps:

1. Find product details from a database (mock data for this example)
2. Extract features from product image
3. Generate product description
4. Generate short description
5. Generate SEO title
6. Generate SEO description
7. Generate keywords for the product

## Directory Structure

```
prompt_chaining/
├── agent.py            # Main workflow definition
├── utils/
│   ├── nodes.py        # Node implementations (functions for each step)
│   ├── state.py        # State definition
│   └── load_env.py     # Environment variable loader
└── mock_data/
    └── mock_data.json  # Mock product data
```

## How to Run

1. Make sure you have set up the environment variables in the root `.env` file:
```
OPENAI_API_KEY=your_api_key_here
```

2. Run the example:
```
python -m prompt_chaining.agent
```

## Modifying the Example

You can modify the workflow by:
- Adding new nodes in `utils/nodes.py`
- Updating the graph structure in `agent.py`
- Changing the state definition in `utils/state.py`
- Adding your own products to `mock_data/mock_data.json`

