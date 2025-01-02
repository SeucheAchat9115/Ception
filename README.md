# Ception: A Deep Learning Framework for 2D and 3D Object Detection in Autonomous Driving

Ception is a state-of-the-art deep learning and computer vision framework built on PyTorch, designed specifically for autonomous driving applications. It provides robust tools for 2D and 3D object detection, leveraging advanced perception techniques to ensure accurate and efficient scene understanding. This framework aims in replacing detectron2 or/and mmcv at some point.

## (Future) Features

- **2D Object Detection**: Supports detection and classification of objects in images using cutting-edge algorithms and pretrained models. Model zoo to use 3rd party pre-trained weights (e.g. torchvision, detectron, mmdetection).
- **3D Object Detection**: Offers advanced modules for understanding spatial geometry and detecting objects in 3D point clouds (similar to mmdetection3d). Inlcuded nuScenes and several other 3D perception datasets.
- **PyTorch-based**: Built on the powerful PyTorch framework, ensuring flexibility and ease of use.
- **Poetry-managed**: Streamlined dependency management and environment setup using Poetry (in the future uv).
- **Pre-commit Hooks**: Ensures code quality and compliance through automated pre-commit checks.
- **GitHub Actions**: Continuous Integration (CI) workflows for automated testing using github actions.

## Installation
### Prerequisites

- **Python**: 3.12+
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
python -m venv "./venv"
source venv/bin/activate
poetry install
```

3. Set up pre-commit hooks:
```bash
pre-commit install
```

## Continuous Integration and Deployment

Ception uses GitHub Actions for automated testing, linting, and deployment. Workflows are configured in the .github/workflows directory, following the pre-commit hooks.

### Code Quality of Life Features
- **Automated Tests**: All commits and pull requests trigger unit tests to ensure code stability.
- **Linting**: Code quality is checked with tools like ruff and mypy.
- **Deployment**: Build artifacts or release pipelines can be set up as needed. (Later)

## Framework Overview
The Ception framework is divided into the following modules:

1. **ception.data**: Data loaders and utilities for handling datasets.
2. **ception.models**: Model definitions and configurations for 2D and 3D object detection.
3. **ception.config**: Configuration file handling and management.
4. **ception.training**: Training parameters such as losses, optimizers, and learning rate schedules.
5. **ception.evaluation**: Evaluation metrics and utilities for model performance.
6. **ception.inference**: Inference tools and utilities for running models on new data.
7. **ception.utils**: Utility functions and helper modules for various tasks.
8. **tools**: Command-line tools for training, evaluation, and inference.

## Contributing
Contributions are welcome! To contribute to Ception, follow these steps:
1. Clone the repository.
2. Create a feature branch:
```bash
git checkout -b feature/your-feature
```
3. Commit your changes and push the branch:
```bash
git push origin feature/your-feature
```
4. Create a Pull Request.
Ensure all pre-commit checks pass before submitting. Code owners will review and merge the PR.

## License
Ception is licensed under the MIT License. See LICENSE for more details. (At a later point a more restrictive license might be used to ensure the open-source nature of the project.)

## Acknowledgments
Ception builds upon the excellent work of the PyTorch community and various open-source object detection frameworks. The project is maintained by SeucheAchat9115.
