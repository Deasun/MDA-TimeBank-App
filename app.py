import os
import json
from flask import Flask, render_template, request, flash, redirect, url_for, jsonify



app = Flask(__name__)
app.secret_key = "some_secret"

"""
Create list to user store user details and scores as game progresses

"""

user_dict = {}

def store_user_info(username, email, guess=0):
    user_dict = {"username": username, "email": email, "score": [guess]}
    #Write user details to user_info.txt file
    with open("data/user_info.txt", "a") as user_details:
        user_details.writelines("{0}\n{1}\n{2}\n".format(
            user_dict["username"],
            user_dict["email"],
            user_dict["score"])) 
    print(user_dict)


"""
List to handle scores - CURRENTLY ADDING ALL SCORES TOGETHER - NOT BY USERNAME
"""
score = []
total_score = sum(score)


"""
Scoring Function
"""
def limit_number_questions(guess, answer):
    if guess <= 0:
        return 0
    elif guess == answer:
        score.append(10)
    else:
        if guess > answer + 10:
            return 0
        elif guess < answer - 10:
            return 0
        elif guess > answer and guess <= answer + 10:      
            score.append(5)  
        elif guess < answer and guess >= answer - 10: 
            score.append(5)
        


"""
Challenge Q&A function
"""
def challenge_q_a(num):
    if request.method == "POST":
            with open("data/challenge.json", "r") as json_data:
                data = json.load(json_data)
                
                """Call Scoring Function"""
                limit_number_questions(int(request.form["guess"]), int(data[num]["skill_answer"]))
                print(request.form)
                print(score)
                print(sum(score))
                # """Display guess to user - LOADS ON REFRESH - NEED AJAX - JSONIFY?"""
                # flash("You guessed {}!".format(
                # request.form["guess"]
                # ))
                
    

"""
Challenge Pages
"""

@app.route('/', methods=["GET", "POST"])
def index():
    """
    Sign in & add details to user_info list
    """
    if request.method == "POST":
        store_user_info(request.form["username"], request.form["email"])
        return redirect('/challenge_1')
    
    return render_template("index.html")


@app.route('/challenge_1', methods=["GET", "POST"])
def challenge_1():
    challenge_q_a(0)
    
    """
    Reading data from challenge.json into challenge.html
    """
    data = []
    with open("data/challenge.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("challenge_1.html", user = user_dict, challenge_data = data)


@app.route('/challenge_2', methods=["GET", "POST"])
def challenge_2():
    challenge_q_a(1)
    """
    Reading data from challenge.json into challenge.html
    """
    data = []
    with open("data/challenge.json", "r") as json_data:
        data = json.load(json_data)
    
    return render_template("challenge_2.html", challenge_data = data)





@app.route('/information')
def information():
    
    return render_template("information.html", page_title="Find out more...")

    
@app.route('/message_board')
def message_board():
    return render_template("message_board.html", page_title="What do you think? Leave a message")
    
if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        
        
