import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="PrimeTech Solutions | Sistemas e Automações em Python",
    layout="wide",
    initial_sidebar_state="collapsed"
)

html_code = """
<!DOCTYPE html>
<html lang="pt-PT">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PrimeTech Solutions - Sistemas e Automações</title>
    <!-- Importando Three.js para renderizar o 3D -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        :root {
            --bg-deep: #07070c;
            --bg-card: #10101a;
            --bg-card-hover: #161624;
            --accent-cyan: #00f2fe;
            --accent-blue: #4facfe;
            --accent-purple: #7f00ff;
            --text-main: #f1f5f9;
            --text-muted: #94a3b8;
        }

        * { box-sizing: border-box; scroll-behavior: smooth; }

        body {
            background-color: var(--bg-deep);
            color: var(--text-main);
            font-family: 'Inter', 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            margin: 0;
            padding: 0;
            line-height: 1.6;
        }

        .tech-bg {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background-image: 
                linear-gradient(to bottom, rgba(7,7,12,0.9), rgba(7,7,12,0.98)),
                radial-gradient(circle at 50% 20%, rgba(127,0,255,0.12) 0%, transparent 50%);
            z-index: -1;
        }

        header {
            padding: 1rem 5%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: rgba(11, 11, 20, 0.85);
            backdrop-filter: blur(12px);
            border-bottom: 1px solid rgba(255,255,255,0.08);
            position: sticky;
            top: 0;
            z-index: 100;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: 800;
            color: #fff;
        }
        .logo span { color: var(--accent-cyan); }

        nav {
            display: flex;
            gap: 1.5rem;
            align-items: center;
        }

        nav a {
            color: var(--text-muted);
            text-decoration: none;
            font-size: 0.9rem;
            font-weight: 500;
            transition: color 0.2s;
        }
        nav a:hover { color: var(--accent-cyan); }

        .btn-header {
            background: linear-gradient(135deg, var(--accent-cyan), var(--accent-blue));
            color: var(--bg-deep);
            padding: 0.5rem 1.2rem;
            border-radius: 6px;
            font-weight: 700;
            text-decoration: none;
            font-size: 0.85rem;
        }

        .hero {
            padding: 4rem 5% 2rem 5%;
            text-align: center;
            max-width: 900px;
            margin: 0 auto;
            position: relative;
        }

        /* Container do Objeto 3D */
        #canvas-container {
            width: 100%;
            height: 280px;
            margin: 1rem auto 2rem auto;
            display: flex;
            justify-content: center;
            align-items: center;
            cursor: grab;
        }
        #canvas-container:active { cursor: grabbing; }

        .hero h1 {
            font-size: 2.8rem;
            font-weight: 900;
            margin-bottom: 1rem;
            color: #fff;
            letter-spacing: -1px;
        }

        .hero h1 span {
            background: linear-gradient(135deg, var(--accent-cyan), var(--accent-blue));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .hero p {
            font-size: 1.15rem;
            color: var(--text-muted);
            margin-bottom: 2rem;
        }

        .tags-container {
            display: flex;
            justify-content: center;
            gap: 0.8rem;
            margin-bottom: 2.5rem;
            flex-wrap: wrap;
        }

        .tag-pill {
            background: rgba(0, 242, 254, 0.08);
            border: 1px solid rgba(0, 242, 254, 0.2);
            color: var(--accent-cyan);
            padding: 0.4rem 1rem;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
        }

        .btn-group {
            display: flex;
            gap: 1rem;
            justify-content: center;
            flex-wrap: wrap;
        }

        .cta-btn {
            background: linear-gradient(135deg, var(--accent-cyan), var(--accent-blue));
            color: var(--bg-deep);
            padding: 0.8rem 2rem;
            font-size: 0.95rem;
            font-weight: 800;
            border-radius: 8px;
            text-decoration: none;
            box-shadow: 0 0 20px rgba(0, 242, 254, 0.3);
            transition: transform 0.2s;
        }
        .cta-btn:hover { transform: translateY(-2px); }

        .cta-btn-outline {
            background: transparent;
            color: #fff;
            border: 1px solid rgba(255,255,255,0.2);
            padding: 0.8rem 2rem;
            font-size: 0.95rem;
            font-weight: 700;
            border-radius: 8px;
            text-decoration: none;
            transition: border-color 0.2s;
        }
        .cta-btn-outline:hover { border-color: var(--accent-cyan); }

        .section {
            padding: 4rem 5%;
            max-width: 1000px;
            margin: 0 auto;
        }

        .section-title {
            font-size: 1.8rem;
            margin-bottom: 2rem;
            text-align: center;
            color: #fff;
            font-weight: 800;
        }

        /* Sobre Mim */
        .about-card {
            background-color: var(--bg-card);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 16px;
            padding: 2.5rem;
            display: flex;
            gap: 2rem;
            align-items: center;
            flex-wrap: wrap;
        }

        .about-text { flex: 1; min-width: 280px; }
        .about-text h3 { color: #fff; margin-top: 0; font-size: 1.5rem; }
        .about-text p { color: var(--text-muted); font-size: 0.95rem; margin-bottom: 1rem; }

        /* Projeto em Destaque */
        .project-featured {
            background: linear-gradient(135deg, rgba(16,16,26,0.95), rgba(22,22,36,0.95));
            border: 1px solid rgba(0, 242, 254, 0.3);
            border-radius: 16px;
            padding: 2.5rem;
            box-shadow: 0 10px 40px rgba(0, 242, 254, 0.1);
        }

        .project-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 2rem;
            margin-top: 1.5rem;
        }

        @media (max-width: 768px) {
            .project-grid { grid-template-columns: 1fr; }
            nav { display: none; }
        }

        .project-info h3 { color: #fff; margin-top: 0; font-size: 1.4rem; }
        .project-info p { color: var(--text-muted); font-size: 0.95rem; }

        .feature-list {
            list-style: none;
            padding: 0;
            margin: 1.5rem 0;
        }
        .feature-list li {
            color: var(--text-muted);
            font-size: 0.9rem;
            margin-bottom: 0.5rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        .feature-list li::before {
            content: "✓";
            color: var(--accent-cyan);
            font-weight: bold;
        }

        /* Serviços */
        .services-stack {
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }

        .service-item {
            background-color: var(--bg-card);
            border: 1px solid rgba(255,255,255,0.06);
            border-radius: 10px;
            padding: 1.2rem 1.5rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: all 0.2s;
        }
        .service-item:hover {
            border-color: var(--accent-cyan);
            background-color: var(--bg-card-hover);
        }
        .service-item h4 { color: #fff; margin: 0; font-size: 1rem; font-weight: 600; }
        .service-item span { color: var(--accent-cyan); font-size: 0.8rem; font-weight: 500; background: rgba(0,242,254,0.05); padding: 0.2rem 0.6rem; border-radius: 4px; }

        /* Dor do Cliente */
        .pain-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 1.2rem;
        }
        .pain-card {
            background-color: var(--bg-card);
            border: 1px solid rgba(255,255,255,0.06);
            border-radius: 12px;
            padding: 1.5rem;
        }
        .pain-card h4 { color: #fff; margin-top: 0; font-size: 1rem; margin-bottom: 0.5rem; }
        .pain-card p { color: var(--text-muted); margin: 0; font-size: 0.9rem; }

        /* WhatsApp Flutuante */
        .whatsapp-float {
            position: fixed;
            bottom: 25px;
            right: 25px;
            background: #25d366;
            color: white;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 30px;
            box-shadow: 0 4px 20px rgba(37, 211, 102, 0.5);
            z-index: 1000;
            text-decoration: none;
            transition: transform 0.3s;
        }
        .whatsapp-float:hover { transform: scale(1.1); }

        footer {
            text-align: center;
            padding: 2.5rem;
            color: var(--text-muted);
            border-top: 1px solid rgba(255,255,255,0.05);
            font-size: 0.85rem;
        }
    </style>
</head>
<body>

    <div class="tech-bg"></div>

    <header>
        <div class="logo">Prime<span>Tech</span></div>
        <nav>
            <a href="#inicio">Início</a>
            <a href="#sobre">Sobre</a>
            <a href="#projetos">Projetos</a>
            <a href="#servicos">Serviços</a>
            <a href="#contato">Contato</a>
        </nav>
        <a href="https://wa.me/5511999999999?text=Olá,%20Daniela!%20Vi%20seu%20portfólio%20e%20gostaria%20de%20conversar%20sobre%20um%20projeto." target="_blank" class="btn-header">Solicitar Orçamento</a>
    </header>

    <section id="inicio" class="hero">
        <h1>PrimeTech Solutions</h1>
        
        <!-- Elemento 3D Interativo -->
        <div id="canvas-container"></div>

        <p style="font-size: 1.3rem; color: #fff; font-weight: 600; margin-bottom: 0.8rem;">Sistemas e automações para facilitar o dia a dia da sua empresa.</p>
        <p>Desenvolvemos sistemas de gestão, automações em Python e soluções personalizadas para organizar processos, clientes, dados e operações.</p>
        
        <div class="tags-container">
            <span class="tag-pill">Python</span>
            <span class="tag-pill">Automação</span>
            <span class="tag-pill">Sistemas de Gestão</span>
        </div>

        <div class="btn-group">
            <a href="#projetos" class="cta-btn">Conheça meus projetos</a>
            <a href="https://wa.me/5511999999999?text=Olá,%20Daniela!%20Vi%20seu%20portfólio%20e%20gostaria%20de%20conversar%20sobre%20um%20projeto." target="_blank" class="cta-btn-outline">Solicitar um orçamento</a>
        </div>
    </section>

    <!-- SOBRE MIM -->
    <section id="sobre" class="section">
        <div class="about-card">
            <div class="about-text">
                <h3>Olá, eu sou a Daniela.</h3>
                <p>Sou desenvolvedora Python em formação, apaixonada por tecnologia e automação. Desenvolvo projetos próprios para transformar processos manuais em sistemas mais organizados e eficientes.</p>
                <p>Atualmente, venho construindo soluções em Python, sistemas de gestão, automações, APIs e integração de dados, sempre buscando transformar aprendizado em projetos reais e funcionais para o mercado.</p>
            </div>
        </div>
    </section>

    <!-- PROJETO EM DESTAQUE -->
    <section id="projetos" class="section">
        <h2 class="section-title">Projetos em Destaque</h2>
        
        <div class="project-featured">
            <div class="project-info">
                <h3>🖥️ PrimeTech Solutions — Sistema de Gestão</h3>
                <p>Sistema desenvolvido em Python para gerenciamento completo de clientes, dados e operações empresariais.</p>
                
                <div class="project-grid">
                  <div>
                    <strong style="color: #fff; font-size: 0.9rem;">Funcionalidades:</strong>
                    <ul class="feature-list">
                        <li>Cadastro de clientes</li>
                        <li>Pesquisa por nome e CPF</li>
                        <li>Validação de CPF integrada</li>
                        <li>Alteração de cadastro e endereço</li>
                        <li>Controle de débitos e histórico</li>
                        <li>Armazenamento de dados seguro</li>
                    </ul>
                  </div>
                  <div>
                    <strong style="color: #fff; font-size: 0.9rem;">Tecnologias Utilizadas:</strong>
                    <div style="display: flex; gap: 0.5rem; margin-top: 0.8rem; flex-wrap: wrap;">
                        <span class="tag-pill">Python</span>
                        <span class="tag-pill">JSON / CRUD</span>
                        <span class="tag-pill">Validação de dados</span>
                    </div>
                    <div style="margin-top: 2rem; display: flex; gap: 1rem;">
                        <a href="https://wa.me/5511999999999?text=Olá,%20Daniela!%20Gostaria%20de%20testar%20o%20sistema%20de%20gestão." target="_blank" class="cta-btn" style="padding: 0.6rem 1.2rem; font-size: 0.85rem;">🚀 Testar sistema</a>
                        <a href="https://github.com" target="_blank" class="cta-btn-outline" style="padding: 0.6rem 1.2rem; font-size: 0.85rem;">💻 Ver projeto</a>
                    </div>
                  </div>
                </div>
            </div>
        </div>
    </section>

    <!-- COMO POSSO AJUDAR -->
    <section class="section">
        <h2 class="section-title">Como posso ajudar sua empresa?</h2>
        <div class="pain-grid">
            <div class="pain-card">
                <h4>⏱️ Tarefas Manuais</h4>
                <p>Você perde tempo cadastrando informações manualmente todos os dias?</p>
            </div>
            <div class="pain-card">
                <h4>👥 Organização de Clientes</h4>
                <p>Precisa organizar dados de clientes, contactos e histórico sem confusão?</p>
            </div>
            <div class="pain-card">
                <h4>📊 Planilhas Complexas</h4>
                <p>Tem planilhas pesadas e difíceis de controlar que travam sua operação?</p>
            </div>
            <div class="pain-card">
                <h4>🔗 Integração de Ferramentas</h4>
                <p>Precisa conectar duas ou mais ferramentas para conversarem entre si?</p>
            </div>
        </div>
    </section>

    <!-- SERVIÇOS -->
    <section id="servicos" class="section">
        <h2 class="section-title">O que eu desenvolvo</h2>
        
        <div class="services-stack">
            <div class="service-item">
                <h4>01 — Sistema de Gestão</h4>
                <span>Python + JSON + CRUD</span>
            </div>
            <div class="service-item">
                <h4>02 — Integração de API</h4>
                <span>Python + API + Automação</span>
            </div>
            <div class="service-item">
                <h4>03 — Automação de Excel</h4>
                <span>Python + Pandas + OpenPyXL</span>
            </div>
            <div class="service-item">
                <h4>04 — Gerador de Documentos</h4>
                <span>Python + Word / PDF</span>
            </div>
            <div class="service-item">
                <h4>05 — Web Scraping</h4>
                <span>Python + Requests + BeautifulSoup</span>
            </div>
            <div class="service-item">
                <h4>06 — Bot para Telegram</h4>
                <span>Python + API</span>
            </div>
            <div class="service-item">
                <h4>07 — Banco de Dados</h4>
                <span>Python + SQLite / PostgreSQL</span>
            </div>
            <div class="service-item">
                <h4>08 — Dashboard e Gráficos</h4>
                <span>Python + Dados + Visualização</span>
            </div>
            <div class="service-item">
                <h4>09 — Criação de API Própria</h4>
                <span>FastAPI + Python</span>
            </div>
            <div class="service-item">
                <h4>10 — Sistema Empresarial Completo</h4>
                <span>Integração de Módulos</span>
            </div>
        </div>
    </section>

    <!-- CONTATO -->
    <section id="contato" class="hero" style="padding-top: 2rem;">
        <h2 class="section-title">Vamos conversar sobre o seu projeto?</h2>
        <p>Entre em contato diretamente para conversarmos sobre automações e sistemas para o seu negócio.</p>
        <a href="https://wa.me/5511999999999?text=Olá,%20Daniela!%20Vi%20seu%20portfólio%20e%20gostaria%20de%20conversar%20sobre%20um%20projeto." target="_blank" class="cta-btn" style="font-size: 1.1rem; padding: 1rem 2.5rem;">💬 Falar comigo pelo WhatsApp</a>
    </section>

    <!-- WhatsApp Flutuante -->
    <a href="https://wa.me/5511999999999?text=Olá,%20Daniela!%20Vi%20seu%20portfólio%20e%20gostaria%20de%20conversar%20sobre%20um%20projeto." target="_blank" class="whatsapp-float" title="Falar no WhatsApp">
        💬
    </a>

    <footer>
        <p>&copy; 2026 PrimeTech Solutions. Desenvolvido por Daniela.</p>
    </footer>

    <!-- Script de Inicialização do 3D (Three.js) -->
    <script>
        const container = document.getElementById('canvas-container');

        // 1. Cena, Câmera e Renderizador
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(60, container.clientWidth / container.clientHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
        renderer.setSize(container.clientWidth, container.clientHeight);
        container.appendChild(renderer.domElement);

        // 2. Criando um objeto 3D com estilo de servidor/cubo tecnológico
        const geometry = new THREE.BoxGeometry(2, 2, 2);
        const material = new THREE.MeshStandardMaterial({
            color: 0x00f2fe,
            wireframe: true,
            roughness: 0.3,
            metalness: 0.8
        });
        const cube = new THREE.Mesh(geometry, material);
        scene.add(cube);

        // Adicionar um núcleo interno sólido
        const innerGeo = new THREE.BoxGeometry(1.5, 1.5, 1.5);
        const innerMat = new THREE.MeshStandardMaterial({
            color: 0x7f00ff,
            roughness: 0.2,
            metalness: 0.9
        });
        const innerCube = new THREE.Mesh(innerGeo, innerMat);
        scene.add(innerCube);

        // 3. Luzes
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.8);
        scene.add(ambientLight);

        const pointLight = new THREE.PointLight(0x00f2fe, 2, 50);
        pointLight.position.set(5, 5, 5);
        scene.add(pointLight);

        camera.position.z = 5;

        // 4. Interatividade com Mouse / Toque
        let isDragging = false;
        let previousMousePosition = { x: 0, y: 0 };

        container.addEventListener('mousedown', (e) => {
            isDragging = true;
            previousMousePosition = { x: e.clientX, y: e.clientY };
        });

        window.addEventListener('mousemove', (e) => {
            if (!isDragging) return;
            const deltaX = e.clientX - previousMousePosition.x;
            const deltaY = e.clientY - previousMousePosition.y;

            cube.rotation.y += deltaX * 0.008;
            cube.rotation.x += deltaY * 0.008;
            innerCube.rotation.y -= deltaX * 0.008;
            innerCube.rotation.x -= deltaY * 0.008;

            previousMousePosition = { x: e.clientX, y: e.clientY };
        });

        window.addEventListener('mouseup', () => { isDragging = false; });

        // Suporte a dispositivos móveis (Touch)
        container.addEventListener('touchstart', (e) => {
            isDragging = true;
            previousMousePosition = { x: e.touches[0].clientX, y: e.touches[0].clientY };
        });

        window.addEventListener('touchmove', (e) => {
            if (!isDragging) return;
            const deltaX = e.touches[0].clientX - previousMousePosition.x;
            const deltaY = e.touches[0].clientY - previousMousePosition.y;

            cube.rotation.y += deltaX * 0.008;
            cube.rotation.x += deltaY * 0.008;

            previousMousePosition = { x: e.touches[0].clientX, y: e.touches[0].clientY };
        });

        window.addEventListener('touchend', () => { isDragging = false; });

        // 5. Loop de Animação contínua
        function animate() {
            requestAnimationFrame(animate);
            if (!isDragging) {
                cube.rotation.x += 0.003;
                cube.rotation.y += 0.005;
                innerCube.rotation.x -= 0.004;
                innerCube.rotation.y -= 0.006;
            }
            renderer.render(scene, camera);
        }
        animate();

        // Ajustar redimensionamento de tela
        window.addEventListener('resize', () => {
            camera.aspect = container.clientWidth / container.clientHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(container.clientWidth, container.clientHeight);
        });
    </script>
</body>
</html>
"""

components.html(html_code, height=2700, scrolling=True)
