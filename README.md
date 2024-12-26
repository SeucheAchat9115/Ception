Warning: This readme is currently AI generated and not manually checked!

---

# Ception: A Deep Learning Framework for 2D and 3D Object Detection in Autonomous Driving

Ception is a state-of-the-art deep learning and computer vision framework built on PyTorch, designed specifically for autonomous driving applications. It provides robust tools for 2D and 3D object detection, leveraging advanced perception techniques to ensure accurate and efficient scene understanding.

## Features

- **2D Object Detection**: Supports detection and classification of objects in images using cutting-edge algorithms and pretrained models.
- **3D Object Detection**: Offers advanced modules for understanding spatial geometry and detecting objects in 3D point clouds.
- **PyTorch-based**: Built on the powerful PyTorch framework, ensuring flexibility and ease of use.
- **Tailored for Autonomous Driving**: Optimized for autonomous driving scenarios, including real-time performance and robust handling of challenging environments.
- **Poetry-managed**: Streamlined dependency management and environment setup using Poetry.
- **Pre-commit Hooks**: Ensures code quality and compliance through automated pre-commit checks.
- **GitHub Actions**: Continuous Integration and Continuous Deployment (CI/CD) workflows for automated testing and deployment.

## Installation
### Prerequisites

- **Python**: 3.11+
- **CUDA**: For GPU acceleration (optional)
- **Poetry**: For dependency and environment management

### Steps

1. Clone the repository:
```bash
git clone https://github.com/SeucheAchat9115/ception.git  
cd ception
```

2. Install dependencies using Poetry:
```bash
python -m venv "./cp-venv"
source cp-venv/bin/activate
poetry install
```

3. Set up pre-commit hooks:
```bash
pre-commit install
```


## Quick Start

### 2D Object Detection

Run the following command to test a pretrained 2D object detection model:
```bash
python ception/2d_detection.py --image input.jpg --model yolov5 --output output.jpg
```
### 3D Object Detection

To test 3D object detection on a point cloud:
```bash
python ception/3d_detection.py --pointcloud input.pcd --model pointpillar --output output.pcd
```
### Visualization

Use the built-in visualization tools to render predictions:
```bash
python ception/visualize.py --input output.pcd --type 3d
```
## Continuous Integration and Deployment

Ception uses GitHub Actions for automated testing, linting, and deployment. Workflows are configured in the .github/workflows directory.

### Features

- **Automated Tests**: All commits and pull requests trigger unit tests to ensure code stability.
- **Linting**: Code quality is checked with tools like flake8 and black.
- **Deployment**: Build artifacts or release pipelines can be set up as needed.

## Framework Overview

The Ception framework is divided into the following modules:

1. **Core**: Base utilities for loading data, configuring models, and training pipelines.
2. **2D Detection**: Algorithms and pretrained models for 2D object detection.
3. **3D Detection**: Tools and architectures for processing 3D data, including point clouds.
4. **Visualization**: Functions for visualizing detection results in 2D and 3D formats.

## Supported Models

### 2D Detection

- **YOLOv5**
- **Faster R-CNN**
- **RetinaNet**

### 3D Detection

- **PointPillars**
- **SECOND**
- **PV-RCNN**

## Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a feature branch:
```bash
git checkout -b feature/your-feature
```
3. Commit your changes and push the branch:
```bash
git push origin feature/your-feature
```
4. Create a Pull Request.
Ensure all pre-commit checks pass before submitting.

## License

Ception is licensed under the MIT License. See LICENSE for more details.

## Acknowledgments

Ception builds upon the excellent work of the PyTorch community and various open-source object detection frameworks. The project is maintained by SeucheAchat9115.