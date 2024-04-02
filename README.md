## Installation

### Dependencies:

- Windows OS (see **Camstim package**)
- python 2.7
- psychopy 1.82.01
- camstim 0.2.4

### Installation with [Anaconda](https://docs.anaconda.com/anaconda/install/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html):

1. Navigate to repository and install conda environment.  
    `conda env create -f environment.yml`
2. Activate the environment.  
    `conda activate allen_stimulus`
3. Install the AIBS `camstim` package in the environment.  
    `pip install camstim/.`
4. Add the necessary active and passive files in the `data` directory.
   
### Input Files

There should be a set of pkl files present under `data/` that contains the list of images to display. Each pkl file contains a nested dictionary. At the core level, a 'Group' is defined which associates a list of images together. Within that group are listed the raw data of all images. The name of the group and each individual image is later on used for tracking which images where shown. 

### Stimulus design
The repo contains two .py file: passive_stimulus.py and  active_stimulus.py
Each relates to different parts of the experimental design of this OpenScope project. 
