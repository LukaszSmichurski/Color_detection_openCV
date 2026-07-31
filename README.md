# 🎨 Real-Time Color Detection & Tracking (OpenCV)

A Python application that detects, tracks, and labels objects of multiple colors in real-time using **OpenCV** and the **HSV color space**. Built with computer vision fundamentals, noise filtering, and contour extraction.

---

## 📸 Demo

![Demo](assets/Screenshot%202026-08-01%20at%2000.05.59.png)

---

## ✨ Key Features

* **HSV Color Space Conversion:** Ensures robust detection under varying lighting conditions.
* **Morphological Noise Reduction:** Utilizes `MORPH_OPEN` filtering to remove small background artifacts and flickering pixels.
* **Multi-Color Detection:** Simultaneously detects and tracks 10 predefined colors (Red, Green, Blue, Yellow, Orange, Violet, Pink, Cyan, White, Black).
* **Dynamic Bounding Boxes & Labels:** Computes precise object contours and renders bounding boxes with matching color tags in real-time.
* **Clean Code Structure:** Modular architecture designed for real-time video processing.

---

## 🛠️ Tech Stack & Dependencies

* **Language:** Python 3.10+
* **Core Libraries:** 
  * `opencv-python` – Computer vision operations & video capture
  * `numpy` – Array operations for color limits

---

