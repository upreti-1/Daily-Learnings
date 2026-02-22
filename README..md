# Pydantic Fundamentals

This folder contains my daily study notes and scripts for **Pydantic V2**. I focused on data validation and serialization patterns commonly used in Python and MLOps.

## 🚀 What I Learned
* **Field Validation**: Using `Annotated` and `Field` for constraints like `max_length` and `ge` (greater than).
* **Custom Validators**: Implementing `@field_validator` for domain-specific checks and `@model_validator` for logic involving multiple fields.
* **Computed Fields**: Using `@computed_field` to dynamically calculate values like BMI.
* **Nested Models**: Organizing complex data structures (e.g., Address within a Patient model).
* **Serialization**: Using `model_dump()` to convert models to dictionaries with include/exclude filters.

## 🛠️ Setup
1. Create a virtual environment: `python -m venv venv`
2. Activate it: `.\venv\Scripts\activate`
3. Install dependencies: `pip install -r requirements.txt`