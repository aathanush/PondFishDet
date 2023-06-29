# PondFishDet

## Abstract
In the current era, aquaculture plays a pivotal role in our nation's economy. However, the presence of fish diseases poses a significant challenge, leading to substantial productivity and economic losses across aquaculture farms of all scales. Detecting unhealthy fish manually is labor-intensive and time-consuming, necessitating the implementation of intelligent systems for efficient disease prevention and fish welfare. The initial step in fish health monitoring is automated and precise fish detection from underwater images/videos, which is highly challenging due to complex underwater conditions, such as variable lighting, water turbulence, and object occlusion. To address this, a study introduced the CLAHE-YOLOv8s fish detection algorithm, utilizing Contrast Light Adaptive Histogram Equalization to enhance underwater images and achieve more accurate fish detection. Training with a pond fish dataset of 5,950 images, the CLAHE-YOLOv8s model demonstrated superior performance in terms of accuracy and processing time compared to MSR-YOLOv8s (Multi Scale Retinex Enhancement). Future improvements could involve training the models with pre-trained weights from other public fish detection datasets to enhance accuracy.

<em>CLAHE Algorithm:</em>
<p align="center" float="middle">
<img src="pics/CLAHE.png?raw=true" width="61.5%" />
</p>


## Installation
1. Set up Python environment with Conda:
```
conda create -n myenv python=3.10
conda activate particlesfm 
```
2. Clone the Repo:
```
git clone https://github.com/aathanush/PondFishDet
```
3.  Install Dependencies:
```
cd PondFishDet
pip pip install -r requirements.txt
```

## Proposed Methodology
<p align="center" float="middle">
<img src="pics/algorithm.png?raw=true" width="61.5%" />
</p>

## Training Results 
<p align="left" float="middle">
<img src="pics/F1.png?raw=true" width="52.5%" />
<img src="pics/PR.png?raw=true" width="52.5%" />
</p>

## Test Results 
<p align="left" float="middle">
<img src="pics/d2.jpg?raw=true" width="25.5%" />
<img src="pics/d2_1.png?raw=true" height="32.5%" width="25.5%" />
</p>

<p align="left" float="middle">
<img src="pics/12_1.jpg?raw=true" width="25.5%" />
<img src="pics/12.jpg?raw=true" height="32.5%" width="25.5%" />
</p>

<p align="left" float="middle">
<img src="pics/13_1.jpg?raw=true" width="25.5%" />
<img src="pics/13.jpg?raw=true" height="32.5%" width="25.5%" />
</p>

## Citation
```
@article{LI2022104759,
author = {Xinjie Li and Guojia Hou and Kunqian Li and Zhenkuan Pan},
title = {Enhancing underwater image via adaptive color and contrast enhancement, and denoising},
journal = {Engineering Applications of Artificial Intelligence},
doi = {https://doi.org/10.1016/j.engappai.2022.104759},
}
```

