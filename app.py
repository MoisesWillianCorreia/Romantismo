# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask import Flask, render_template_string

app = Flask(__name__)

html_code = u"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Convite Especial</title>
    <style>
        body {
            background: url('https://images.pexels.com/photos/556667/pexels-photo-556667.jpeg?auto=compress&cs=tinysrgb&w=1600') no-repeat center center fixed;
            background-size: cover;
            font-family: 'Arial', sans-serif;
            text-align: center;
            color: white;
            margin-top: 50px;
            overflow: hidden;
            position: relative;
        }
        .container {
            background: rgba(0, 0, 0, 0.7);
            padding: 30px;
            border-radius: 15px;
            display: inline-block;
            z-index: 10;
            position: relative;
        }
        h1 {
            font-size: 2.5em;
            margin-bottom: 20px;
        }
        p {
            font-size: 1.5em;
        }
        button {
            font-size: 1.2em;
            padding: 10px 20px;
            margin: 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease;
            position: relative;
        }
        #yesBtn {
            background-color: #4CAF50;
            color: white;
        }
        #yesBtn:hover {
            background-color: #45a049;
        }
        #noBtn {
            background-color: #f44336;
            color: white;
        }

        /* Animação dos corações */
        .heart {
            width: 20px;
            height: 20px;
            position: absolute;
            background-color: rgba(255, 105, 180, 0.8);
            transform: rotate(45deg);
            animation: float 8s linear infinite;
            opacity: 0.8;
            z-index: 1;
        }

        .heart::before, .heart::after {
            content: "";
            width: 20px;
            height: 20px;
            position: absolute;
            background-color: rgba(255, 105, 180, 0.8);
            border-radius: 50%;
        }

        .heart::before {
            top: -10px;
            left: 0;
        }

        .heart::after {
            left: -10px;
            top: 0;
        }

        @keyframes float {
            0% {
                transform: translateY(0) rotate(45deg);
                opacity: 0.8;
            }
            100% {
                transform: translateY(-1000px) rotate(45deg);
                opacity: 0;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Convite Especial</h1>
        <p>Você gostaria de ir a um encontro comigo no dia 01 de setembro?</p>
        <button id="yesBtn">Sim</button>
        <button id="noBtn">Não</button>
    </div>

    <script>
        // Movendo o botão "Não" quando o mouse passa por cima
        document.getElementById('noBtn').addEventListener('mouseover', function() {
            const maxX = window.innerWidth - this.offsetWidth;
            const maxY = window.innerHeight - this.offsetHeight;
            
            // Define nova posição dentro dos limites da janela
            const newX = Math.random() * maxX;
            const newY = Math.random() * maxY;

            this.style.position = 'absolute';
            this.style.left = `${newX}px`;
            this.style.top = `${newY}px`;
        });

        // Redirecionamento ao clicar no botão "Sim"
        document.getElementById('yesBtn').addEventListener('click', function() {
            window.location.href = 'https://www.youtube.com/watch?v=kQ2ZFVJNMs0&list=RDkQ2ZFVJNMs0&start_radio=1';
        });

        // Alert ao clicar no botão "Não"
        document.getElementById('noBtn').addEventListener('click', function() {
            alert('Ah, que pena! Talvez outra vez.');
        });

        // Criando corações flutuantes
        function createHearts() {
            const heart = document.createElement('div');
            heart.classList.add('heart');
            heart.style.left = Math.random() * 100 + 'vw';
            heart.style.animationDuration = Math.random() * 5 + 5 + 's';
            document.body.appendChild(heart);
            setTimeout(() => {
                heart.remove();
            }, 10000);
        }

        setInterval(createHearts, 500);
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html_code)

if __name__ == '__main__':
    app.run(debug=True)
