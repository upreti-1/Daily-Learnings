# 🏥 Patient Management System

## 🚀 Overview
A full-stack Patient Management dashboard built from scratch to practice connecting a Python backend with a modern React frontend. The system allows users to view, search, sort, and manage patient records with auto-calculated BMI and health verdicts.

## 💻 Tech Stack
* **Backend:** FastAPI, Python, Pydantic (for data validation), local JSON storage.
* **Frontend:** React, TypeScript, Vite, Tailwind CSS, shadcn/ui.
* **Tools:** Lovable (AI UI generation), Git.

## 🧠 Key Learnings Today
1. **API Integration:** Successfully connected a local React frontend (Vite/HTTP) to a local FastAPI server (HTTP), bypassing browser mixed-content blocks.
2. **Data Serialization:** Learned to format backend JSON responses (converting dicts to lists) so React's `.map()` function can render them correctly.
3. **React State & UI:** Manually extended AI-generated UI components by adding a custom "View" details panel, a real-time search bar, and wiring up `fetch` requests.
4. **Git Structuring:** Learned how to safely merge an initialized frontend repository into a master "Daily Learnings" repository by removing nested `.git` folders.

## 🛠️ How to Run Locally

### 1. Start the Backend
```bash
cd main.py
uvicorn main:app --reload

### 2. start the frontend
```bash
cd patient-harmony
npm install
npm run dev