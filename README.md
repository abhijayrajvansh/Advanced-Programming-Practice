# Advanced-Programming-Practice

*Professors in charge: Dr.P.Velmurugan & Dr.S.Godfrey Winster*


# For Setting Up Environment

To Activate :
```
conda activate {ENV_NAME}
```
Note: {ENV_NAME} By default is base

To Deactivate : 
```
conda deactivate
```

For Listing Environemnt :
```
conda env list
```

To Create a Virtual Env :
```
conda create --name {ENV-NAME} python=3.9
conda create --name EXP-env python=3.9

# TO REMOVE
conda env remove -n ENV_NAME
```
Note: *Pyhton version may vary for your system*

To Install Packages in different Envs :
```
conda install {pkg-name} ; example :- seaborn, google-api-python-client
```

To Add Channels in Anaconda : 
```
conda config --add channels {channel-name} ; ex:- conda-forge
conda config --show channels
conda config --get channels
```



© 2022 Abhijay Rajvansh, All rights reserved.

