

#script to install python, matplotlib

sudo apt-get install python-dev
rm .cache/matplotlib/ -r -f

sudo apt-get install python-pyside

sudo pip install matplotlib


#then, in the python script, use:


matplotlib.use('Qt4Agg')    

#enjoy!!!