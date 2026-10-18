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

<table>
  <tr>
    <td><strong>Languages</strong></td>
    <td><img src="https://skillicons.dev/icons?i=python,c,cpp,java,js" height="40" alt="Python, C, C++, Java and JavaScript" title="Python, C, C++, Java and JavaScript" /></td>
  </tr>
  <tr>
    <td><strong>AI · ML · Computer Vision</strong></td>
    <td><img src="https://skillicons.dev/icons?i=tensorflow,pytorch,opencv" height="40" alt="TensorFlow, PyTorch and OpenCV" title="TensorFlow, PyTorch and OpenCV" /> <img src="./assets/skills/numpy.svg" width="40" height="40" alt="NumPy" title="NumPy" /> <img src="./assets/skills/pandas.svg" width="40" height="40" alt="Pandas" title="Pandas" /> <img src="./assets/skills/jupyter.svg" width="40" height="40" alt="Jupyter" title="Jupyter" /></td>
  </tr>
  <tr>
    <td><strong>Development</strong></td>
    <td><img src="https://skillicons.dev/icons?i=git,github,vscode" height="40" alt="Git, GitHub and VS Code" title="Git, GitHub and VS Code" /></td>
  </tr>
  <tr>
    <td><strong>Operating Systems</strong></td>
    <td><img src="https://skillicons.dev/icons?i=windows,linux" height="40" alt="Windows and Linux" title="Windows and Linux" /></td>
  </tr>
  <tr>
    <td><strong>Engineering</strong></td>
    <td><img src="./assets/skills/matlab.svg" width="40" height="40" alt="MATLAB" title="MATLAB" /> <img src="./assets/skills/kicad.svg" width="40" height="40" alt="KiCad" title="KiCad" /></td>
  </tr>
  <tr>
    <td><strong>Currently Learning</strong></td>
    <td><img src="./assets/skills/tinyml.svg" width="40" height="40" alt="TinyML (topic icon)" title="TinyML (topic icon)" /> <small>TinyML</small>&nbsp;&nbsp; <img src="https://raw.githubusercontent.com/fastai/logos/master/logo_square.png" width="40" height="40" alt="fast.ai" title="fast.ai" /> <small>fast.ai</small>&nbsp;&nbsp; <img src="./assets/skills/embedded-firmware.svg" width="40" height="40" alt="Embedded firmware (topic icon)" title="Embedded firmware (topic icon)" /> <small>Embedded firmware</small></td>
  </tr>
</table>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./profile-3d-contrib/profile-night-green.svg">
  <source media="(prefers-color-scheme: light)" srcset="./profile-3d-contrib/profile-green-animate.svg">
  <img alt="Blaze's 3D GitHub contribution graph" src="./profile-3d-contrib/profile-green-animate.svg">
</picture>

