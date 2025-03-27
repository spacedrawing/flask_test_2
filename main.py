from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return "И на Марсе будут яблони цвести!"


@app.route("/fun")
def fun():
    names = ["Маша", "Петя", "Вася", "Катя", "И", "fynjy", "efhuob", "wedwe", "ewedew"]
    x = [
        f"<h{i}>{name}</h{i}>" if i <= 6 else f"<h6>{name}</h6>"
        for i, name in enumerate(names, 1)
    ]
    return "<br>".join(x)


@app.route("/image")
def image():
    return f"""<img src="{url_for('static', filename='img/riana.png')}"
           alt="здесь должна была быть картинка, но не нашлась">"""


@app.route("/promotion")
def promotion():
    promot = [
        "Человечество вырастает из детства.",
        "Человечеству мала одна планета.",
        "Мы сделаем обитаемыми безжизненные пока планеты.",
        "И начнем с Марса!",
        "Присоединяйся!",
    ]

    return "</br>".join(promot)


@app.route("/image_mars")
def image_mars():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Привет, Марс!</title>
</head>
<body>
    <h1>Жди нас, Марс!</h1>
    <img src="https://i.imgflip.com/s0dgo.jpg" alt="Тут был марс">
    <p>Тут что-то было</p>
</body>
</html>"""


@app.route("/promotion_image")
def promotion_image():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Привет, Марс!</title>
    <link rel="stylesheet" href="static/css/style.css">
</head>
<body>
    <h1>Жди нас, Марс!</h1>
    <img src="https://i.imgflip.com/s0dgo.jpg" alt="Тут был марс">
    <p class="black">Человечество вырастает из детства.</p>
    <p class="green">Человечеству мала одна планета.</p>
    <p class="black">Мы сделаем обитаемыми безжизненные пока планеты.</p>
    <p class="yellow">И начнем с Марса!</p>
    <p class="red">Присоединяйся!</p>
</body>
</html>"""


@app.route("/greeting/<username>")
def greeting(username):
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Привет, {username}</title>
                  </head>
                  <body>
                    <h1>Привет, {username}!</h1>
                  </body>
                </html>"""


@app.route("/choice/<planet_name>")
def choice(planet_name):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
    <title>Варианты выбора</title>
</head>
<body>
    <header>
        <h1>Мое предложение: {planet_name}</h1>
        <h3>Эта планета близка к Земле;</h3>
        <h3 class="green">На ней много необходимых ресурсов;</h3>
        <h3 class="black">На ней есть вода и атмосфера;</h3>
        <h3 class="yellow">На ней есть небольшое магнитное поле;</h3>
        <h3 class="red">Наконец, она просто красива!</h3>
    </header>
</body>
</html>"""


@app.route("/two_params/<username>/<int:number>")
def two_params(username, number):
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Пример с несколькими параметрами</title>
                  </head>
                  <body>
                    <h2>{username}</h2>
                    <div>Это первый параметр и его тип: {str(type(username))[1:-1]}</div>
                    <h2>{number}</h2>
                    <div>Это второй параметр и его тип: {str(type(number))[1:-1]}</div>
                  </body>
                </html>"""


@app.route("/astronaut_selection")
def astronaut_selection():
    return render_template("astronaut_selection.html")


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
