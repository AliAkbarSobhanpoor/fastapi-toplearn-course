# FastAPI Course - Setup Guide

Course: [TopLearn FastAPI Course](https://toplearn.com/c/6332)

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Project Structure](#project-structure)

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Python 3.12 or higher**
- **pip** (Python package manager)
- **git** (optional, for cloning the repository)

## Installation

Follow these steps to set up the project on your local machine:

### 1. Create a Virtual Environment

Navigate to the project's main directory and create a Python virtual environment:

```bash
python3 -m venv .venv
```

### 2. Activate the Virtual Environment

Activate the virtual environment for your operating system:

**On Linux/macOS:**
```bash
source .venv/bin/activate
```

**On Windows:**
```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

Install all required packages from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Running the Project

To run a specific course episode:

### 1. Navigate to the Episode Folder

```bash
cd episode\ < episodeNumber >
```

### 2. Run the Main File

```bash
python main.py
```

Or, if using Uvicorn directly:

```bash
uvicorn main:app --reload
```

## Project Structure

```
fastapi-course/
├── .venv/                    # Virtual environment (do not commit)
├── requirements.txt          # Project dependencie
├── episode_1/
│   └── main.py
├── episode_2/
│   └── main.py
└── ...
└── README.md                 # This file
```

## Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Uvicorn Documentation](https://www.uvicorn.org/)
- [Python Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)


## Deactivating the Virtual Environment

When you're done working on the project, deactivate the virtual environment:

```bash
deactivate
```
