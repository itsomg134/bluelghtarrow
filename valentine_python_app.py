from flask import Flask, render_template_string, jsonify
import random

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Will You Be Mine? 💕</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            overflow: hidden;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }

        #canvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }

        .content {
            position: relative;
            z-index: 10;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            color: white;
            text-align: center;
            padding: 20px;
        }

        h1 {
            font-size: 4em;
            margin-bottom: 20px;
            text-shadow: 0 0 20px rgba(255, 255, 255, 0.5);
            animation: glow 2s ease-in-out infinite;
        }

        .message {
            font-size: 1.8em;
            margin-bottom: 40px;
            max-width: 600px;
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
        }

        .buttons {
            display: flex;
            gap: 30px;
            margin-top: 20px;
        }

        button {
            padding: 20px 50px;
            font-size: 1.5em;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 2px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        }

        .yes-btn {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
        }

        .yes-btn:hover {
            transform: scale(1.1) translateY(-5px);
            box-shadow: 0 15px 40px rgba(245, 87, 108, 0.5);
        }

        .no-btn {
            background: rgba(255, 255, 255, 0.2);
            color: white;
            backdrop-filter: blur(10px);
        }

        .no-btn:hover {
            transform: scale(0.9);
        }

        .response {
            display: none;
            font-size: 3em;
            margin-top: 50px;
            animation: fadeIn 1s ease-in;
        }

        .stats {
            position: fixed;
            top: 20px;
            right: 20px;
            background: rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(10px);
            padding: 15px 25px;
            border-radius: 20px;
            color: white;
            font-size: 1.2em;
        }

        @keyframes glow {
            0%, 100% { text-shadow: 0 0 20px rgba(255, 255, 255, 0.5); }
            50% { text-shadow: 0 0 40px rgba(255, 255, 255, 0.9), 0 0 60px rgba(255, 192, 203, 0.7); }
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .heart-emoji {
            display: inline-block;
            animation: heartbeat 1.5s ease-in-out infinite;
        }

        @keyframes heartbeat {
            0%, 100% { transform: scale(1); }
            25% { transform: scale(1.2); }
            50% { transform: scale(1); }
        }
    </style>
</head>
<body>
    <canvas id="canvas"></canvas>
    
    <div class="stats">
        <div>Attempts: <span id="attempts">0</span></div>
    </div>
    
    <div class="content">
        <h1>💖 Will You Be My Valentine? 💖</h1>
        <div class="message">
            You make my heart skip a beat every time I see you. 
            Will you make this Valentine's Day special by being mine?
        </div>
        <div class="buttons">
            <button class="yes-btn" onclick="sayYes()">YES! 💕</button>
            <button class="no-btn" onclick="sayNo()" id="noBtn">No</button>
        </div>
        <div class="response" id="response"></div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        let noCount = 0;

        // Three.js 3D Hearts Background
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ canvas: document.getElementById('canvas'), alpha: true });
        renderer.setSize(window.innerWidth, window.innerHeight);
        camera.position.z = 5;

        const hearts = [];
        const heartShape = new THREE.Shape();
        heartShape.moveTo(0, 0);
        heartShape.bezierCurveTo(0, -0.3, -0.6, -0.3, -0.6, 0);
        heartShape.bezierCurveTo(-0.6, 0.3, 0, 0.6, 0, 1);
        heartShape.bezierCurveTo(0, 0.6, 0.6, 0.3, 0.6, 0);
        heartShape.bezierCurveTo(0.6, -0.3, 0, -0.3, 0, 0);

        const extrudeSettings = { depth: 0.3, bevelEnabled: true, bevelThickness: 0.1, bevelSize: 0.1 };

        for (let i = 0; i < 30; i++) {
            const geometry = new THREE.ExtrudeGeometry(heartShape, extrudeSettings);
            const material = new THREE.MeshPhongMaterial({ 
                color: Math.random() > 0.5 ? 0xff69b4 : 0xff1493,
                emissive: 0xff69b4,
                emissiveIntensity: 0.3
            });
            const heart = new THREE.Mesh(geometry, material);
            
            heart.position.x = (Math.random() - 0.5) * 20;
            heart.position.y = (Math.random() - 0.5) * 20;
            heart.position.z = (Math.random() - 0.5) * 20;
            
            heart.rotation.x = Math.random() * Math.PI;
            heart.rotation.y = Math.random() * Math.PI;
            
            heart.scale.set(0.3, 0.3, 0.3);
            
            scene.add(heart);
            hearts.push({
                mesh: heart,
                speedX: (Math.random() - 0.5) * 0.02,
                speedY: (Math.random() - 0.5) * 0.02,
                rotSpeed: (Math.random() - 0.5) * 0.02
            });
        }

        const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
        scene.add(ambientLight);
        const pointLight = new THREE.PointLight(0xffffff, 1);
        pointLight.position.set(5, 5, 5);
        scene.add(pointLight);

        function animate() {
            requestAnimationFrame(animate);
            
            hearts.forEach(h => {
                h.mesh.rotation.x += h.rotSpeed;
                h.mesh.rotation.y += h.rotSpeed;
                h.mesh.position.x += h.speedX;
                h.mesh.position.y += h.speedY;
                
                if (Math.abs(h.mesh.position.x) > 10) h.speedX *= -1;
                if (Math.abs(h.mesh.position.y) > 10) h.speedY *= -1;
            });
            
            renderer.render(scene, camera);
        }
        animate();

        window.addEventListener('resize', () => {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        });

        // Button interactions with Python backend
        async function sayNo() {
            const response = await fetch('/no_click', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'}
            });
            const data = await response.json();
            
            const btn = document.getElementById('noBtn');
            btn.textContent = data.message;
            btn.style.transform = `translate(${data.x}px, ${data.y}px)`;
            
            document.getElementById('attempts').textContent = data.attempts;
            noCount = data.attempts;
        }

        async function sayYes() {
            const response = await fetch('/yes_click', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'}
            });
            const data = await response.json();
            
            const responseDiv = document.getElementById('response');
            responseDiv.innerHTML = data.message;
            responseDiv.style.display = 'block';
            document.querySelector('.buttons').style.display = 'none';
            document.querySelector('.message').style.display = 'none';
            
            // Create heart explosion
            for (let i = 0; i < 20; i++) {
                setTimeout(() => {
                    const geometry = new THREE.ExtrudeGeometry(heartShape, extrudeSettings);
                    const material = new THREE.MeshPhongMaterial({ color: 0xff1493 });
                    const heart = new THREE.Mesh(geometry, material);
                    heart.position.set(0, 0, 0);
                    scene.add(heart);
                    
                    const speed = {
                        x: (Math.random() - 0.5) * 0.3,
                        y: (Math.random() - 0.5) * 0.3,
                        z: (Math.random() - 0.5) * 0.3
                    };
                    
                    hearts.push({ mesh: heart, speedX: speed.x, speedY: speed.y, rotSpeed: 0.05 });
                }, i * 50);
            }
        }
    </script>
</body>
</html>
"""

# Store attempts in memory
no_attempts = 0

@app.route('/')
def index():
    """Main page route"""
    return render_template_string(HTML_TEMPLATE)

@app.route('/no_click', methods=['POST'])
def no_click():
    """Handle 'No' button clicks"""
    global no_attempts
    no_attempts += 1
    
    messages = [
        "Are you sure? 🥺",
        "Think again! 💕",
        "Really? Please reconsider!",
        "One more chance? 💖",
        "Pretty please? 🌹",
        "Don't break my heart! 💔",
        "I'll wait for you! ⏰",
        "You're making this hard! 😢",
        "Last chance to say yes! ✨",
        "I believe in us! 💫"
    ]
    
    message_index = min(no_attempts - 1, len(messages) - 1)
    message = messages[message_index]
    
    # Random position for button
    x = random.randint(-150, 150)
    y = random.randint(-100, 100)
    
    return jsonify({
        'message': message,
        'attempts': no_attempts,
        'x': x,
        'y': y
    })

@app.route('/yes_click', methods=['POST'])
def yes_click():
    """Handle 'Yes' button clicks"""
    success_messages = [
        '<span class="heart-emoji">❤️</span> Yay! You made me the happiest person! <span class="heart-emoji">❤️</span>',
        '<span class="heart-emoji">💕</span> I knew you would say yes! Forever yours! <span class="heart-emoji">💕</span>',
        '<span class="heart-emoji">💖</span> Best Valentine\'s Day ever! <span class="heart-emoji">💖</span>',
    ]
    
    return jsonify({
        'message': random.choice(success_messages),
        'success': True
    })

if __name__ == '__main__':
    print("🌹 Valentine's Day Proposal Server Starting...")
    print("💕 Open your browser and go to: http://localhost:5000")
    print("❤️  Press Ctrl+C to stop the server")
    app.run(debug=True, host='0.0.0.0', port=5000)
