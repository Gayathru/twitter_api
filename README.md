This is to demostrate the connecting to Twitter using the API and extracting data using Python.

Extracting count of a particular hashtag in Twitter


The python code can be found in the file twitter_api1.py
Pre-requisites:
Software requirements - 
    1: Python 3+ version
    2: PIP installation
    3: Docker
   

Steps to perform:
1: From your terminal create a project directory and clone the project from GIT.
2: Use the Dockerfile to create an image
       docker build -t twitter:latest .
3: Create the container
       docker run -it --name myApp twitter
4: You will be prompted to enter the twitter hashtag
       sample hashtag : ##Palestinewin
5: You will receive the hashtag count as your output



