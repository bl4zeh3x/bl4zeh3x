# Hi, I'm Blaze 👋

**Python · C/C++ · TinyML · Embedded software**

I've been working on small machine-learning models intended for microcontrollers. Most of the work so far is in Python: training models, testing them, and exporting them to C. Actual hardware benchmarks are still ahead.

<p align="left">
  <a href="https://instagram.com/bl4zeh3x"><img src="assets/social/instagram.svg" width="22" height="22" alt="Instagram" /></a>&nbsp;&nbsp;
  <a href="https://x.com/bl4zeh3x"><img src="assets/social/x.svg" width="22" height="22" alt="X" /></a>&nbsp;&nbsp;
  <a href="https://linkedin.com/in/bl4zeh3x"><img src="assets/social/Linkedin.svg" width="22" height="22" alt="LinkedIn" /></a>&nbsp;&nbsp;
  <a href="https://kaggle.com/bl4zeh3x"><img src="assets/social/Kaggle.svg" width="22" height="22" alt="Kaggle" /></a>
</p>

### Current project — [ECG anomaly detection](https://github.com/bl4zeh3x/tinyml-explorations/tree/main/experiments/ecg-anomaly-detection)

An experiment in getting heartbeat classifiers small enough for embedded devices.

- Extracted **24 features per heartbeat**, including RR-interval timing.
- Compared three model sizes using a **patient-separated** train/test split.
- Exported the compact models to C and added tests that compare their predictions with Python.

The Edge model reached **82.95% accuracy and 0.409 macro F1** on held-out patients. It still struggles with some less common heartbeat classes; the per-class results are linked below.

[Code & tests](https://github.com/bl4zeh3x/tinyml-explorations/tree/main/experiments/ecg-anomaly-detection) · [Results](https://github.com/bl4zeh3x/tinyml-explorations/blob/main/experiments/ecg-anomaly-detection/results/summary.json) · [CI](https://github.com/bl4zeh3x/tinyml-explorations/actions/workflows/test.yml)

**Next:** run the exported models on real hardware and measure inference latency and memory usage.

I'm interested in internships, open-source contributions, and projects involving Python, ML tooling, or embedded software.

---

## 🛠️ Tech Stack

### Languages

<p>
  <img src="https://skillicons.dev/icons?i=python,c,cpp,java,js" />
</p>

### AI • Machine Learning • Computer Vision

<p>
  <img src="https://skillicons.dev/icons?i=tensorflow,pytorch,opencv" />
</p>

<p>
  <img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white"/>
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white"/>
</p>

### Development

<p>
  <img src="https://skillicons.dev/icons?i=git,github,vscode" />
</p>

### Operating Systems

<p>
  <img src="https://skillicons.dev/icons?i=windows,linux" />
</p>

### Engineering

<p>
  <img src="https://img.shields.io/badge/MATLAB-0076A8?style=flat-square&logo=mathworks&logoColor=white"/>
  <img src="https://img.shields.io/badge/KiCad-314CB0?style=flat-square&logo=kicad&logoColor=white"/>
</p>

### Currently Learning

<p>
  <img src="https://img.shields.io/badge/TinyML-0A84FF?style=flat-square"/>
  <img src="https://img.shields.io/badge/Fast.ai-1E90FF?style=flat-square"/>
  <img src="https://img.shields.io/badge/Embedded%20Firmware-555555?style=flat-square"/>
</p>

![](./profile-3d-contrib/profile-green-animate.svg)

