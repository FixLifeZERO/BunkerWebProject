from flask import Flask, render_template, request, session, redirect, url_for, g, jsonify
from game_logic.game_state import GameState
from game_logic.localization import set_language, get_text as _
from game_logic.config import DEFAULT_LANGUAGE
import os

app = Flask(__name__)


app.secret_key = os.urandom(24)

def get_game_state():
    if 'game_state' not in session:
        gs = GameState()
        session['game_state'] = gs.to_dict()
        return gs
    return GameState.from_dict(session['game_state'])

@app.before_request
def before_request():
    lang = session.get('language', DEFAULT_LANGUAGE)
    set_language(lang)
    g.get_text = _

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        game_state = get_game_state()

        if request.is_json:
            data = request.get_json()
            action = data.get('action')
            
            if action == 'start_search':
                game_state.start_search()
                session['game_state'] = game_state.to_dict()
                return jsonify(success=True, message='Search started')
                
            elif action == 'check_search_results':
                result = game_state.get_search_results()
                session['game_state'] = game_state.to_dict()
                if result is None and game_state.search_started and not game_state.search_complete:
                    # If search is in progress but no result yet
                    return jsonify(status='success', message=None)
                return jsonify(status='success', message=result)
                
            return jsonify(status='error', message='Unknown action'), 400

        action = request.form.get('action')

        if action == 'start_new_game':
            game_state = GameState()  
            game_state.current_screen = "game"
            session['game_state'] = game_state.to_dict()
        elif action == 'exit_to_menu':
            game_state.reset_game_state() 
            game_state.current_screen = "main_menu"
        elif action == 'open_settings':
            session['pre_settings_screen'] = game_state.current_screen
            game_state.current_screen = "settings"
        elif action == 'close_settings':
            game_state.current_screen = session.pop('pre_settings_screen', 'main_menu')
        elif action.startswith('set_lang_'):
            lang = action.split('_')[-1]
            session['language'] = lang
            set_language(lang)
        elif action == 'go_outing':
            game_state.go_on_outing()
        elif action == 'charge_suit':
            game_state.charge_suit()
        elif action == 'skip_day':
            game_state.skip_day()


        session['game_state'] = game_state.to_dict()
        return redirect(url_for('index'))

    game_state = get_game_state()
    return render_template('index.html', gs=game_state, get_text=g.get_text)

if __name__ == '__main__':
    app.run(debug=True)
    app.run(debug=True)
