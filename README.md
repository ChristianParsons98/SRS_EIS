# SRS_EIS

This repository contains Python scripts to control the Stanford Research Systems SR830 Lock-in Amplifier for performing Electrochemical Impedance Spectroscopy (EIS) via GPIB.

## 🧪 Description

The core script automates EIS measurements using a programmable interface over GPIB. Designed for lab use, it reduces manual overhead and ensures consistent experimental control for physicists and electrochemists.

- Run script: [`Run_EIS.py`](./Run_EIS.py)

## 🔧 Techniques Used

- GPIB instrument control via `pyvisa`
- Frequency sweeps and dynamic control loops
- Integration with SR830's phase/amplitude response
- Data capture and export to CSV/logging systems

## 📦 Libraries and Tools

- [PyVISA](https://pyvisa.readthedocs.io/en/latest/): Interface with the GPIB instrument
- [NumPy](https://numpy.org/): Data storage and processing
- [time](https://docs.python.org/3/library/time.html): Precise delays for scan timing

## 📁 Project Structure

```plaintext
.
├── Run_EIS.py
└── README.md
```

### Notable File

- [`Run_EIS.py`](./Run_EIS.py): Automates lock-in amplifier configuration and data acquisition
