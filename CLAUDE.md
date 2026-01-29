# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a comprehensive Python learning repository covering Data Science, AI, Automation, Cybersecurity, and Quantitative Finance. All code includes detailed Spanish explanations with progressive difficulty levels.

## Structure

```
Python/
├── 01-Fundamentos-Python/          # Python basics (classes, functions, data types)
├── 02-Data-Science-AI/
│   ├── 01-Analisis-Datos/          # NumPy, Pandas, Matplotlib
│   ├── 02-Machine-Learning/        # Scikit-learn, ML concepts
│   ├── 03-Deep-Learning/           # Neural networks from scratch, TensorFlow, PyTorch
│   ├── 04-NLP/                     # Natural Language Processing
│   └── 05-Computer-Vision/         # OpenCV, image processing
├── 03-Automatizacion-Scripting/
│   ├── 01-Web-Scraping/            # BeautifulSoup, requests
│   ├── 02-Automatizacion-Tareas/   # File automation, scripts
│   └── 03-DevOps/                  # CI/CD, deployment
├── 04-Ciberseguridad/
│   ├── 01-Pentesting/              # Security fundamentals
│   ├── 02-Analisis-Malware/
│   └── 03-Automatizacion-Auditorias/
└── 05-Finanzas-Cuantitativas/
    ├── 01-Trading-Algoritmico/     # Algorithmic trading basics
    └── 02-Analisis-Mercados/
```

## Running Code

```bash
python3 <filename>.py
```

## Dependencies

Install based on the module you're working with:

```bash
# Data Science basics
pip install numpy pandas matplotlib seaborn

# Machine Learning
pip install scikit-learn xgboost

# Deep Learning
pip install tensorflow  # or: pip install torch torchvision

# NLP
pip install nltk spacy transformers

# Computer Vision
pip install opencv-python

# Web Scraping
pip install requests beautifulsoup4 lxml

# Finance
pip install yfinance ta backtrader
```

## Deep Learning Learning Path

The `02-Data-Science-AI/03-Deep-Learning/` folder follows a progressive learning path:

1. `01_estructuras_de_datos_arbol.py` - Tree data structures (foundation)
2. `02_que_es_una_neurona.py` - Single neuron from scratch
3. `03_red_neuronal_desde_cero.py` - Complete neural network with backpropagation
4. `04_tensorflow_intro.py` - TensorFlow/Keras basics
5. `05_pytorch_intro.py` - PyTorch basics

## Language

Code comments, variable names, and explanations are in Spanish.
