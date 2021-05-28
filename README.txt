This is to demostrate the connecting to Twitter using the API and extracting data using Python.

Extracting count of a particular hashtag in Twitter


Instruction follows:
1. Create a project directory and Git clone the project.

2. Use the Dockerfile to create an image
        docker build -t twitter:latest .

3. Bring up a container with this image
        docker run -t -p 8000:8000 --name myApp twitter

4. Enter the twitter hashtag you want to search for.
        eg: Constitution of God

5: You will receive the hashtag count as your output