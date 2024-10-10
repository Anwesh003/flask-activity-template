from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Sample task list with a completion status
tasks = []

@app.route('/')
def home():
    return render_template('home.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_description = request.form.get('task')
    if task_description:
        # Create a new task dictionary
        task = {'description': task_description, 'completed': False}
        tasks.append(task)
    return redirect('/')

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['completed'] = not tasks[task_id]['completed'] 
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)  
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
