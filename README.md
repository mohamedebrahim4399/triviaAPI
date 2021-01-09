# Full Stack API Final Project

## Full Stack Trivia

Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a  webpage to manage the trivia app and play the game, but their API experience is limited and still needs to be built out. 

That's where you come in! Help them finish the trivia app so they can start holding trivia and seeing who's the most knowledgeable of the bunch. The application must:

1) Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer. 
2) Delete questions.
3) Add questions and require that they include question and answer text.
4) Search for questions based on a text query string.
5) Play the quiz game, randomizing either all questions or within a specific category. 


## The Great Trivia
This project is a questions project, you will be able to add or delete questions and also test yourself on these questions, which are various questions in many fields.

## Getting Started
<hr>

### Pre-requisites and Local Development
<hr>
Developers using this project should already have Python3, pip and node installed on their local machines.<br><br>

### Database Setup
<hr>

With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psq
```

### Backend
<hr>

From the backend folder run ```
pip install requirements.txt```
All required packages are included in the requirements file.<br><br>

To run the application run the following commands:
```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, `http://127.0.0.1:5000/` , which is set as a proxy in the frontend configuration.

Authentication: This version of the application does not require authentication or API keys.<br><br>

### Frontend
<hr>

From the frontend folder, run the following commands to start the client:
```
npm install // only once to install dependencies
npm start
```
By default, the frontend will run on `localhost:3000`.<br><br>

## Test
in order ti run tests navigate to the backend folder and run the following commands:

```
dropdb trivia
createdb trivia
psql trivia < trivia.psq
python test_flaskr.py
```

The first time run the test, omit the dropdb command.

All test are kept in that file and should be maintained as updates are made to app functionality. 
 

## API Reference
<hr>

### Error Handling
Errors are returned as JSON objects in the following format:



```
{
    'success': False,
    'error': 404,
    'message': 'resource not found'
}
```

```
{
    'success': False,
    'error': 422,
    'message': 'unprocessable'
}
```

The API will return three error types when requests fail:
* 404: Resource Not Found
* 422: Not Processable

<br>


### Endpoint

#### GET/categories
*  ```http://127.0.0.1:5000/categories ```
*  Returns all categories 


```
{
    "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
    },
    "success": true,
    "total_categoreis": 6
}
```


#### GET/questions
* ``` http://127.0.0.1:5000/questions ```
*  Return all categories and 10 questions per page  

```
{
    "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
    },
    "current_category": [
        5,
        5,
        4,
        5,
        4,
        6,
        6,
        4,
        3,
        3
    ],
    "questions": [
        {
            "answer": "Apollo 13",
            "category": 5,
            "difficulty": 4,
            "id": 2,
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        },
        {
            "answer": "Tom Cruise",
            "category": 5,
            "difficulty": 4,
            "id": 4,
            "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        },
        {
            "answer": "Maya Angelou",
            "category": 4,
            "difficulty": 2,
            "id": 5,
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        },
        {
            "answer": "Edward Scissorhands",
            "category": 5,
            "difficulty": 3,
            "id": 6,
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        },
        {
            "answer": "Muhammad Ali",
            "category": 4,
            "difficulty": 1,
            "id": 9,
            "question": "What boxer's original name is Cassius Clay?"
        },
        {
            "answer": "Brazil",
            "category": 6,
            "difficulty": 3,
            "id": 10,
            "question": "Which is the only team to play in every soccer World Cup tournament?"
        },
        {
            "answer": "Uruguay",
            "category": 6,
            "difficulty": 4,
            "id": 11,
            "question": "Which country won the first ever soccer World Cup in 1930?"
        },
        {
            "answer": "George Washington Carver",
            "category": 4,
            "difficulty": 2,
            "id": 12,
            "question": "Who invented Peanut Butter?"
        },
        {
            "answer": "Lake Victoria",
            "category": 3,
            "difficulty": 2,
            "id": 13,
            "question": "What is the largest lake in Africa?"
        },
        {
            "answer": "The Palace of Versailles",
            "category": 3,
            "difficulty": 3,
            "id": 14,
            "question": "In which royal palace would you find the Hall of Mirrors?"
        }
    ],
    "success": true,
    "total_questions": 33
}

```

#### GET/categories/{category_id}/questions
*  ``` http://127.0.0.1:5000/categories/1/questions ```
*  Get questions by category id.


```
{
    "category": 1,
    "questions": [
        {
            "answer": "The Liver",
            "category": 1,
            "difficulty": 4,
            "id": 20,
            "question": "What is the heaviest organ in the human body?"
        },
        {
            "answer": "Alexander Fleming",
            "category": 1,
            "difficulty": 3,
            "id": 21,
            "question": "Who discovered penicillin?"
        },
        {
            "answer": "Blood",
            "category": 1,
            "difficulty": 4,
            "id": 22,
            "question": "Hematology is a branch of medicine involving the study of what?"
        },
        {
            "answer": " answer",
            "category": 1,
            "difficulty": 2,
            "id": 194,
            "question": "Question "
        },
        {
            "answer": " answer",
            "category": 1,
            "difficulty": 2,
            "id": 195,
            "question": "Question "
        },
        {
            "answer": " answer",
            "category": 1,
            "difficulty": 2,
            "id": 197,
            "question": "Question "
        }
    ],
    "success": true,
    "total_categories_questions": 6
}
```

#### DELETE /questions/{question_id}
*  ``` http://127.0.0.1:5000/questions/9  ```
*  Deletes the question by ID
```
{
    "deleted": 9,
    "success": true
}
```


#### POST/questions
*  ``` http://127.0.0.1:5000/questions```
* The json body => { "question": "New Question?", "answer": "New Answer", "difficulty": "1", "category": "5"}

*  Creates a new question 
```
{
    "created": 199,
    "current_questions": {
        "answer": "New Answer",
        "category": 5,
        "difficulty": 1,
        "id": 199,
        "question": "New Question?"
    },
    "success": true,
    "total_questions": 30
}
```

#### POST/questions/search
*  ```   http://127.0.0.1:5000/questions/search ```
* The json body =>{ "searchTerm": "the"}
* Returns all the questions that contain the value in the Search input.


```
{
    "questions": [
        {
            "answer": "Maya Angelou",
            "category": 4,
            "difficulty": 2,
            "id": 5,
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        },
        {
            "answer": "Tom Cruise",
            "category": 5,
            "difficulty": 4,
            "id": 4,
            "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        },
        {
            "answer": "Edward Scissorhands",
            "category": 5,
            "difficulty": 3,
            "id": 6,
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        },
        {
            "answer": "Brazil",
            "category": 6,
            "difficulty": 3,
            "id": 10,
            "question": "Which is the only team to play in every soccer World Cup tournament?"
        },
        {
            "answer": "Uruguay",
            "category": 6,
            "difficulty": 4,
            "id": 11,
            "question": "Which country won the first ever soccer World Cup in 1930?"
        },
        {
            "answer": "Lake Victoria",
            "category": 3,
            "difficulty": 2,
            "id": 13,
            "question": "What is the largest lake in Africa?"
        },
        {
            "answer": "The Palace of Versailles",
            "category": 3,
            "difficulty": 3,
            "id": 14,
            "question": "In which royal palace would you find the Hall of Mirrors?"
        },
        {
            "answer": "Agra",
            "category": 3,
            "difficulty": 2,
            "id": 15,
            "question": "The Taj Mahal is located in which Indian city?"
        },
        {
            "answer": "The Liver",
            "category": 1,
            "difficulty": 4,
            "id": 20,
            "question": "What is the heaviest organ in the human body?"
        },
        {
            "answer": "Blood",
            "category": 1,
            "difficulty": 4,
            "id": 22,
            "question": "Hematology is a branch of medicine involving the study of what?"
        }
    ],
    "success": true,
    "total_questions": 30
}
```


#### POST/quizzes
*  ```  http://127.0.0.1:5000/quizzes ```
*  The json body =>{"previous_questions": [], "quiz_category": {"type": "Entertainment", "id": "5"}}
*  Returns the current quiz question.


```
{
    "question": {
        "answer": "Edward Scissorhands",
        "category": 5,
        "difficulty": 3,
        "id": 6,
        "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    "success": true
}
```