# FYS_3023

Simple coding examples to support SAR lectures for FYS-3023.

Try installing the anacond with required packages using:

    # create new environment
    conda env create -f FYS_3023_environment.yml 

If this does not work, try setting up the environment manually like this:

    # create new environment
    conda env create -y -n FYS_3023 python=3.10 gdal

    # activate new environment
    conda activate FYS_3023

    # install required packages
    conda install scipy matplotlib jupyter
