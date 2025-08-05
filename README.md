<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cybersecurity Student Profile</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'JetBrains Mono', 'Fira Code', monospace;
            background: linear-gradient(135deg, #0c0c0c 0%, #1a1a1a 100%);
            color: #e0e0e0;
            line-height: 1.6;
            min-height: 100vh;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }

        .header {
            text-align: center;
            margin-bottom: 3rem;
            background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .header h1 {
            font-size: 3.5rem;
            font-weight: 800;
            margin-bottom: 0.5rem;
            text-shadow: 0 0 30px rgba(255, 107, 107, 0.5);
        }

        .subtitle {
            font-size: 1.3rem;
            color: #888;
            margin-bottom: 1rem;
        }

        .section {
            margin-bottom: 3rem;
            padding: 2rem;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 15px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        }

        .section h2 {
            font-size: 2rem;
            margin-bottom: 1.5rem;
            color: #4ecdc4;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .badge-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
            gap: 1rem;
            margin-top: 1rem;
        }

        .badge-item {
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            border-radius: 12px;
            overflow: hidden;
        }

        .badge-item:hover {
            transform: translateY(-5px) scale(1.05);
            box-shadow: 0 10px 25px rgba(78, 205, 196, 0.3);
        }

        .badge-item img {
            width: 100%;
            height: auto;
            display: block;
        }

        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-top: 2rem;
        }

        .stat-card {
            background: rgba(255, 255, 255, 0.03);
            border-radius: 10px;
            padding: 1rem;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .stat-card img {
            width: 100%;
            height: auto;
        }

        .quote {
            text-align: center;
            font-style: italic;
            font-size: 1.1rem;
            color: #888;
            margin-top: 2rem;
            padding: 1rem;
            border-left: 4px solid #4ecdc4;
            background: rgba(78, 205, 196, 0.1);
            border-radius: 0 10px 10px 0;
        }

        .glow {
            animation: glow 2s ease-in-out infinite alternate;
        }

        @keyframes glow {
            from { text-shadow: 0 0 20px rgba(78, 205, 196, 0.5); }
            to { text-shadow: 0 0 30px rgba(78, 205, 196, 0.8), 0 0 40px rgba(78, 205, 196, 0.4); }
        }

        .matrix-bg {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            opacity: 0.1;
            overflow: hidden;
        }

        .matrix-text {
            position: absolute;
            color: #4ecdc4;
            font-family: monospace;
            animation: matrix-fall linear infinite;
        }

        @keyframes matrix-fall {
            0% { transform: translateY(-100vh); }
            100% { transform: translateY(100vh); }
        }

        @media (max-width: 768px) {
            .header h1 { font-size: 2.5rem; }
            .container { padding: 1rem; }
            .badge-grid { grid-template-columns: repeat(auto-fit, minmax(100px, 1fr)); }
        }
    </style>
</head>
<body>
    <div class="matrix-bg" id="matrix"></div>
    
    <div class="container">
        <header class="header">
            <h1 class="glow">👋 Hi, I'm bbuddha!</h1>
            <p class="subtitle">🔐 Cybersecurity Student | Red Team & Purple Team Enthusiast</p>
        </header>

        <section class="section">
            <h2>🛠️ Daily Environment</h2>
            <div class="badge-grid">
                <div class="badge-item">
                    <a href="https://endeavouros.com/">
                        <img src="https://bentos.jkominovic.dev/api/v1/generic-card?icon=siEndeavouros&subtitle=USE+EOS+BTW&size=square&rounded=24" alt="EndeavourOS">
                    </a>
                </div>
                <div class="badge-item">
                    <a href="https://hyprland.org/">
                        <img src="https://bentos.jkominovic.dev/api/v1/generic-card?icon=siHyprland&subtitle=HYPRLAND&size=square&rounded=24" alt="Hyprland">
                    </a>
                </div>
            </div>
        </section>

        <section class="section">
            <h2>💻 Languages & Technologies</h2>
            <div class="badge-grid">
                <div class="badge-item">
                    <a href="https://www.gnu.org/software/bash/">
                        <img src="https://bentos.jkominovic.dev/api/v1/generic-card?icon=siGnubash&subtitle=BASH&size=square&rounded=24" alt="Bash">
                    </a>
                </div>
                <div class="badge-item">
                    <a href="https://python.org/">
                        <img src="https://bentos.jkominovic.dev/api/v1/generic-card?icon=siPython&subtitle=PYTHON&size=square&rounded=24" alt="Python">
                    </a>
                </div>
                <div class="badge-item">
                    <a href="https://golang.org/">
                        <img src="https://bentos.jkominovic.dev/api/v1/generic-card?icon=siGo&subtitle=GOLANG&size=square&rounded=24" alt="Go">
                    </a>
                </div>
                <div class="badge-item">
                    <a href="https://cmake.org/">
                        <img src="https://bentos.jkominovic.dev/api/v1/generic-card?icon=siCmake&subtitle=CMAKE&size=square&rounded=24" alt="CMake">
                    </a>
                </div>
            </div>
        </section>

        <section class="section">
            <h2>🎯 Areas of Expertise</h2>
            <div class="badge-grid">
                <div class="badge-item">
                    <a href="https://www.kali.org/">
                        <img src="https://bentos.jkominovic.dev/api/v1/generic-card?icon=siKalilinux&subtitle=PENTEST&size=square&rounded=24" alt="Penetration Testing">
                    </a>
                </div>
                <div class="badge-item">
                    <a href="https://www.hackerone.com/">
                        <img src="https://bentos.jkominovic.dev/api/v1/generic-card?icon=siHackerone&subtitle=RED+TEAM&size=square&rounded=24" alt="Red Team">
                    </a>
                </div>
                <div class="badge-item">
                    <a href="https://www.virustotal.com/">
                        <img src="https://bentos.jkominovic.dev/api/v1/generic-card?icon=siVirustotal&subtitle=PURPLE+TEAM&size=square&rounded=24" alt="Purple Team">
                    </a>
                </div>
            </div>
        </section>

        <section class="section">
            <h2>🔧 Favorite Tools</h2>
            <div class="badge-grid">
                <div class="badge-item">
                    <a href="https://portswigger.net/">
                        <img src="https://bentos.jkominovic.dev/api/v1/generic-card?icon=siPortswigger&subtitle=BURP+SUITE&size=square&rounded=24" alt="Burp Suite">
                    </a>
                </div>
                <div class="badge-item">
                    <a href="https://www.metasploit.com/">
                        <img src="https://bentos.jkominovic.dev/api/v1/generic-card?icon=siMetasploit&subtitle=METASPLOIT&size=square&rounded=24" alt="Metasploit">
                    </a>
                </div>
                <div class="badge-item">
                    <a href="https://www.wireshark.org/">
                        <img src="https://bentos.jkominovic.dev/api/v1/generic-card?icon=siWireshark&subtitle=WIRESHARK&size=square&rounded=24" alt="Wireshark">
                    </a>
                </div>
                <div class="badge-item">
                    <a href="https://nmap.org/">
                        <img src="https://bentos.jkominovic.dev/api/v1/generic-card?icon=siNmap&subtitle=NMAP&size=square&rounded=24" alt="Nmap">
                    </a>
                </div>
            </div>
        </section>

        <section class="section">
            <h2>📊 GitHub Statistics</h2>
            <div class="stats">
                <div class="stat-card">
                    <img src="https://github-readme-stats.vercel.app/api?username=bbuddha&show_icons=true&theme=dark&hide_border=true" alt="GitHub Stats">
                </div>
                <div class="stat-card">
                    <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=bbuddha&layout=compact&theme=dark&hide_border=true" alt="Top Languages">
                </div>
            </div>
        </section>

        <section class="section">
            <h2>🌐 Contact Me</h2>
            <div class="badge-grid">
                <div class="badge-item">
                    <a href="https://linkedin.com/in/your-profile">
                        <img src="https://bentos.jkominovic.dev/api/v1/generic-card?icon=siLinkedin&subtitle=LINKEDIN&size=square&rounded=24" alt="LinkedIn">
                    </a>
                </div>
                <div class="badge-item">
                    <a href="https://discord.com/">
                        <img src="https://bentos.jkominovic.dev/api/v1/generic-card?icon=siDiscord&subtitle=DISCORD&size=square&rounded=24" alt="Discord">
                    </a>
                </div>
            </div>
        </section>

        <div class="quote">
            💡 <em>"Security is not a product, but a process"</em> - Bruce Schneier
        </div>
    </div>

    <script>
        // Matrix effect
        function createMatrixEffect() {
            const matrix = document.getElementById('matrix');
            const chars = '01';
            
            for (let i = 0; i < 50; i++) {
                const span = document.createElement('span');
                span.className = 'matrix-text';
                span.style.left = Math.random() * 100 + '%';
                span.style.animationDuration = (Math.random() * 3 + 2) + 's';
                span.style.animationDelay = Math.random() * 2 + 's';
                span.textContent = chars[Math.floor(Math.random() * chars.length)];
                matrix.appendChild(span);
            }
        }

        createMatrixEffect();
    </script>
</body>
</html>
