
## Introduction
This repo contain all the code I used to complete 
[Artificial Intelligence Nanodegree(AIND)](https://www.udacity.com/ai) 
Program provided by [Udacity](https://www.udacity.com/). 

## Setting up Environment
Build env using existing [aind-environment-osx.yml](aind-environment-osx.yml).

### Conda environment
```commandline
conda env create -f aind-environment-osx.yml
source activate aind
pip install git+https://github.com/hmmlearn/hmmlearn.git
```

### Install Pygame
Install [homebrew](http://brew.sh/) first.
```commandline
brew install sdl sdl_image sdl_mixer sdl_ttf portmidi mercurial
source activate aind
pip install pygame
```

### Enable Jupyter notebook to select different conda envs
References
- [Using Jupyter Notebook extensions](https://docs.anaconda.com/anaconda/user-guide/tasks/use-jupyter-notebook-extensions#notebook-conda)

```commandline
source deactivate aind
conda install nb_conda
jupyter notebook
```



