# F1-analysis

**Tom Eade | 2026**

A collection of Formula 1 data analysis tools built using FastF1 and Plotly, 
developed as a personal engineering project alongside Formula SAE.

Each tool is interactive, pulling real F1 timing and telemetry data to extract 
meaningful performance insights.

## Libraries Used
- [FastF1](https://docs.fastf1.dev/) - F1 timing and telemetry data
- [Plotly](https://plotly.com/python/) - Interactive plotting
- Pandas - Data processing
- NumPy - Numerical operations

## Tools

---

### 1 — Speed Trace | `SingleLapSpeedTrace.py`
Plots an interactive speed trace for any driver, lap and session.

**Features**
- Any session type — Race, Qualifying, Practice
- Fastest lap or specific lap number
- Input validation and error handling
- Local data caching
