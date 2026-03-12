# Multithreading and Multiprocessing in Python

This folder contains various scripts demonstrating the concepts of **Multithreading** and **Multiprocessing** in Python, including basic usage, advanced executors, and real-world use cases.

## Overview

### 1. Multithreading
Multithreading is used for **I/O-bound tasks** (e.g., file operations, network requests, web scraping). It allows multiple operations to run concurrently by switching between threads while waiting for I/O.

*   `multi_threading.py`: Basic introduction to creating and joining threads using the `threading` module.
*   `advance_multi_threading.py`: Using `ThreadPoolExecutor` from `concurrent.futures` for managing a pool of threads efficiently.
*   `usecase_multi_threading.py`: A real-world example of **Web Scraping** where multiple Wikipedia pages are fetched concurrently to improve performance.

### 2. Multiprocessing
Multiprocessing is used for **CPU-bound tasks** (e.g., heavy mathematical computations, data processing). It allows true parallel execution by using multiple CPU cores, bypassing Python's Global Interpreter Lock (GIL).

*   `multi_processing.py`: Basic introduction to creating processes using the `multiprocessing` module.
*   `advance_multi_processing.py`: Using `ProcessPoolExecutor` from `concurrent.futures` to manage multiple processes.
*   `factorial_multi_processing.py`: Performance demonstration for calculating factorials of large numbers using a process pool.
*   `factorial_multi_processing_advanced.py`: Advanced variations or refinements of the factorial calculation task.

## Key Differences

| Feature | Multithreading | Multiprocessing |
| :--- | :--- | :--- |
| **Best for** | I/O-bound tasks | CPU-bound tasks |
| **Concurrency/Parallelism** | Concurrency (Shared Memory) | Parallelism (Separate Memory) |
| **GIL** | Limited by GIL | Bypasses GIL |
| **Memory Overhead** | Low | High |

## How to Run

Ensure you have the required dependencies (like `requests` and `beautifulsoup4` for the web scraping example) installed:

```bash
pip install requests beautifulsoup4
```

Then run any script using Python:

```bash
python <script_name>.py
```
