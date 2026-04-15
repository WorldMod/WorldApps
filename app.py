from flask import Flask, render_template, request, abort
import os

app = Flask(__name__)

# Считываем пароли из настроек Render (переменные среды)
ADMIN_PASS_1 = os.environ.get('ADMIN_PASS_1')
ADMIN_PASS_2 = os.environ.get('ADMIN_PASS_2')

@app.route('/worldapps')
def worldapps():
    return render_template('worldapps.html')

@app.route('/admin')
def admin_panel():
    password = request.args.get('password')
    # Проверка: если пароль совпадает с одним из двух
    if password == ADMIN_PASS_1 or password == ADMIN_PASS_2:
        return "Привет, WorldSviat! Ты в панели управления WorldTeam STUDIO."
    else:
        abort(403) # Ошибка "Доступ запрещен"

if __name__ == '__main__':
    app.run()
  
