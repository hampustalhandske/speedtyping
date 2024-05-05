from flask import Flask
from views import views
from flask import Flask, request, jsonify, render_template, Blueprint
from flask_cors import CORS
from handler import Handler
from pointhandler import point_handler
from config import app, db
from words import words

gh = Handler(words)
ph = point_handler()
app = Flask(__name__)



app.register_blueprint(views, url_prefix="/" )

@app.route('/start', methods=['GET'])
def get_word():
    
    try:
        word_list = gh.get_word_list().tolist()
        ph.reset_points()
        return jsonify({'word_list': word_list}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@app.route('/update_word', methods=['POST'])
def update_word():
    try:
        word = request.json.get('wordInput')
        if gh.is_correct_word(word):
            ph.update_correct_words()
            updated_word_list = gh.get_word_list().tolist()
            return jsonify({'success': True, 'updated_word_list': updated_word_list}), 200
        else:
            updated_word_list = gh.get_word_list().tolist()
            ph.update_nbr_of_words()
            return jsonify({'success': False, 'updated_word_list': updated_word_list}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500
    
@app.route('/handle_input', methods=['POST'])
def handle_input():
    try:
        typed = request.json.get('wordInput')
        if gh.is_correctly_typed(typed):
            return jsonify({'success': True, 'length': len(typed)}), 200
        else:
            return jsonify({'success': False, 'length': len(typed)}), 200
    except Exception as e:
        return jsonify({'message': "whatagatag"}), 500
    
@app.route('/calculate_values', methods=['POST'])
def calculate_values():
    try:
        time = request.json.get('time')
        wpm = ph.wpm(time)
        wps = ph.wps(time)
        percentage = ph.correct_procentage()

        return jsonify({'wpm': wpm, 'wps': wps, 'percentage': percentage}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500
    
@app.route('/stop_game', methods=['GET'])
def stop_game():
    try:
        dictionary = ph.final_score()
        wpm = dictionary['wpm']
        wps = dictionary['wps']
        percentage = dictionary['percentage']
                
        return jsonify({
            'wpm': wpm,
            'wps': wps,
            'percentage': percentage
        }), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500
        
@app.route('/get_plot', methods=['GET'])
def get_plot():
    try:
        dictionary = ph.get_plot()
        percentage = dictionary["percentage"]
        wpm = dictionary["wpm"]
        nbr = dictionary["nbr"]
        return jsonify({'percentage': percentage, 'wpm': wpm, 'nbr': nbr})
    except Exception as e:
        return jsonify({'message': str(e)})


if __name__ == '__main__':
    app.run(debug=True, port=8000)
