from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/estimator', methods=['GET', 'POST'])
def estimator():
    if request.method == 'POST':
        pi = 3.14
        material_cost = 25.0
        labor_cost = 15.0
        radius = int(request.form['radius'])
        height = int(request.form['height'])
        area_top_tank = pi * (radius**2)
        print(f'top area: {area_top_tank}')
        area_tank_sides = (radius*height)*pi*2
        print(f'area tank sides: {area_tank_sides}')
        total_area = area_tank_sides + area_top_tank
        total_area_sqfeet = total_area /144
        total_material_cost = total_area_sqfeet * material_cost
        total_labor_cost = total_area_sqfeet * labor_cost
        total_cost_estimate = f'{(total_labor_cost+total_material_cost):,.2f}'

        return render_template('estimator.html', total_estimate = total_cost_estimate)
    return render_template('estimator.html')

if __name__ == '__main__':
    app.run(debug=True)