# MIRAGE · Algae Exchange Network

Interactive STEM simulation: two cities share algae through an AI-controlled pump network.
The model, the AI controller, the charts and the Arduino link all run in the browser (`mirage.html`).
`app.py` serves the simulation through Streamlit.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

1. Push this folder to a GitHub repository.
2. Go to https://share.streamlit.io, sign in with GitHub, choose **Create app**.
3. Pick the repository, branch `main`, main file `app.py`, then **Deploy**.

## Real Arduino pumps

Browsers block USB (Web Serial) inside embedded pages, so the hosted app runs the pumps in Demo mode.
To drive the real pumps, open `mirage.html` directly in Chrome or Edge (or use the download button in the app's sidebar).

All values are simulated model outputs, not measurements.
