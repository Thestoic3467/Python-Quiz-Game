from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        score = 0
        answers = {
            'q1': 'central processing unit',
            'q2': 'graphics processing unit',
            'q3': 'random access memory',
            'q4': 'power supply'
        }
        
        user_answers = {
            'q1': request.form.get('q1'),
            'q2': request.form.get('q2'),
            'q3': request.form.get('q3'),
            'q4': request.form.get('q4')
        }
        
        for key in answers:
            if answers[key].lower() == user_answers[key].lower():
                score += 1
        
        return redirect(url_for('result', score=score))
    
    return render_template('quiz.html')

@app.route('/result')
def result():
    score = int(request.args.get('score', 0))
    percentage = int(score / 4 * 100)
    return render_template('result.html', score=score, percentage=percentage)

if __name__ == '__main__':
    app.run(debug=True)
