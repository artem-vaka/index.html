from flask import Flask

app = Flask(__name__)


NAV_MENU = """
<nav style="background-color: #f0f0f0; padding: 10px; margin-bottom: 20px; font-family: Arial, sans-serif;">
    <a href="/" style="margin-right: 15px; text-decoration: none; color: #333; font-weight: bold;"> Головна</a>
    <a href="/about" style="margin-right: 15px; text-decoration: none; color: #333; font-weight: bold;"> Про мене</a>
    <a href="/skills" style="margin-right: 15px; text-decoration: none; color: #333; font-weight: bold;"> Навички</a>
    <a href="/contact" style="text-decoration: none; color: #333; font-weight: bold;"> Контакти</a>
</nav>
"""

def render_page(content):
    return f"""
    {NAV_MENU}
    <div style="padding: 0 10px; font-family: Arial, sans-serif; line-height: 1.6;">
        {content}
    </div>
    """


@app.route('/')
def home():
    content = "<h2>Головна сторінка</h2><p>Ласкаво просимо! Це головна сторінка мого локального Flask-сервера.</p>"
    return render_page(content)

@app.route('/about')
def about():
    content = "<h2>Про автора</h2><p>Привіт! Я починаючий розробник, який вивчає Python та веб-технології.</p>"
    return render_page(content)

@app.route('/skills')
def skills():
    content = "<h2>Мої навички</h2><p>Python, Flask, HTML/CSS, Git.</p>"
    return render_page(content)

@app.route('/contact')
def contact():
    content = "<h2>Контактна інформація</h2><p>Email: adsdasd@gmail.com <br> GitHub: :https://artem-vaka.github.io/index.html/</p>"
    return render_page(content)



@app.route('/temperature/<int:t>')
def check_temperature(t):
    if t < 0:
        return "Мороз"
    elif 0 <= t < 20:
        return "Прохолодно"
    elif 20 <= t <= 30:
        return "Тепло"
    else:
        return "Спека"



@app.route('/math/<operation>/<int:a>/<int:b>')
def calculator(operation, a, b):
    if operation == 'add':
        result = a + b
    elif operation == 'sub':
        result = a - b
    elif operation == 'mul':
        result = a * b
    elif operation == 'div':
        if b == 0:
            return "Помилка: Ділення на нуль неможливе!", 400
        result = a / b
    else:
        return f"Помилка: Операція '{operation}' не підтримується.", 400

    return str(result)


if __name__ == '__main__':
    app.run(debug=True)
