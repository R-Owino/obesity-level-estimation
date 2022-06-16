## FLASK APPLICATION FOR OBESITY LEVEL ESTIMATION

This is a simple application for deploying machine learning model for obesity level estimation using flask API.

## PRE-REQUISITES

- Scikit Learn
- Pandas (for Machine Leraning Model) 
- Flask (for API)

Flask version == 2.1.2

## PROJECT STRUCTURE

The project has 2 main parts:
1. app.py - This contains Flask APIs that receives a person's details through GUI or API calls, categirizes the precited value based on our model and returns it.
2. template - This folder contains the HTML template (index.html) to allow user to enter the features.

## RUNNING THE PROJECT
1. Ensure that you are in the project home directory. The project home directory should have the template folder, the serialized model(model.pkl) and the application file containing the Flask API (app.py)

2. Run app.py using below command to start Flask API:
```
python app.py
```
By default, flask will run on port 5000.

3. Navigate to [URL](http://127.0.0.1:5000/) or [URL](http://localhost:5000)

You should be able to view the homepage.

Enter valid numerical values in the first 3 input boxes and select the optional values in the remaining text boxes then hit the CHECK LEVEL button.

If everything goes well, you should  be able to see the predcited weight level on the HTML page!
check the output [here](http://127.0.0.1:5000/result)
