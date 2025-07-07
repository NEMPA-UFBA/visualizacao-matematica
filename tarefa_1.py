# Para começar com a nossa animação, nossa primeira linha de código deve ser "from manim import *". 
from manim import (
    Scene, Text, Write, FadeOut, Polygon, VGroup, MathTex, Line, Create,
    FadeIn, LaggedStart, Transform, Sector,
    # Constantes
    BLUE, BLUE_E, DOWN, UP, RED, GREEN, YELLOW, BLACK, LEFT, RIGHT, PI
) # Essa primeira linha é responsável por importar da biblioteca manim todas as ferramentas necessárias para a construção da nossa animação.
# Agora que temos o acesso a toda biblioteca manim, continuaremos com a nossa animação:

class SomaDosAngulosInternosTriangulo(Scene): # "class SomaDosAngulosInternosTriangulo" É o nome que da nossa cena.
    # O comando (Scene) indica que nossa classe se comporta como uma cena podendo usar todas as ferramentas necessárias para as animações.

    def construct(self): # Aqui estamos começando com a nossa animação. Tudo o que estiver dentro de "construct" será animado. O (self) nos permite modificar a cena na qual estamos construindo. 
        titulo = Text("Soma dos Ângulos Internos de um Triângulo", font_size=48) # "Titulo = Text(...)" Cria a animação do texto. "font_size=48" Define o tamanho da fonte.
        self.play(Write(titulo), run_time=2) # "self.play(...)" É o comando para rodar a animação. "Write(titulo)" Faz o texto aparecer como se estivesse sendo escrito na tela. "run_time" define o tempo da animação.
        self.wait(1.5) # Mantém a minha animação (titulo) visível por 1.5 segundos
        self.play(FadeOut(titulo)) # "self.play(FadeOut(titulo))" Anima o desaparecimento do título (FadeOut)
        self.wait(0.5) # Uma pausa de 0.5 segundos antes de começar a próxima cena.

        # Agora iremos começar a construir o triângulo - começando pelos seus vertices.
        vertice_A = [-3, -1, 0] # Marca um ponto 3 unidades à esquerda do centro e 1 unidade para baixo.
        vertice_B = [3, -1, 0] # Marca um ponto 3 unidades à direita do centro e 1 unidade para baixo.
        vertice_C = [0, 2.5, 0] # Marca um ponto no centro horizontal (x=0) e 2.5 unidades para cima.
        # IMPORTANTE: O Manim usa um sistema de coordenadas com 3 eixos: [x, y, z], para animações 2D, deixamos Z = 0.

        # Agora já com os vertices, vamos criar o nosso triângulo.

        triangulo = Polygon(vertice_A, vertice_B, vertice_C, color=BLUE_E, fill_opacity=0.6) # "triangulo = Polygon(...)" Cria um polígono. 
        # "vertice_A, vertice_B, vertice_C" São os pontos que formam os vértices do polígono. 
        # "color=BLUE_E" Define a cor da borda do triângulo. 
        # "fill_opacity=0.6:"" Define a opacidade do preenchimento do polígono.

        # Agora iremos "dar nome" aos vértices criados.
        rotulos_vertices = VGroup(
            MathTex("A").next_to(vertice_A, DOWN, buff=0.3), # O comando "MathTex(...)" cria o objeto de texto, neste caso, a letra "A". 
            # ".next_to(...)" Diz ao Manim para colocar o objeto que acabamos de criar (a letra "A") "ao lado de" outra coisa.  
            # "DOWN" Diz que a letra "A" deve ser colocada abaixo do vertice_A. IMPORTANTE: Para o vértice C, usa-se UP para colocá-lo acima.
            # "buff=0.3" é a distância entre o rotulo e o vértice.
            # "VGroup(...)" Agrupa os objetos e os anima tudo numa só vez.
            MathTex("B").next_to(vertice_B, DOWN, buff=0.3), 
            MathTex("C").next_to(vertice_C, UP, buff=0.3))
        # Foi usado MathTex em vez de Text porque ele utiliza o LaTeX para renderizar.
        
        # Agora iremos criar os ângulos internos do triângulo e seus respectivos rótulos.  
        # A ideia é fazer pequenos setores circulares coloridos para representar os ângulos internos do triângulo. Iremos criar segmentos "invisíveis" para construirmos os ângulos:
        linha_AB = Line(vertice_A, vertice_B)
        linha_AC = Line(vertice_A, vertice_C)
        linha_BC = Line(vertice_B, vertice_C)
        linha_BA = Line(vertice_B, vertice_A)
        linha_CA = Line(vertice_C, vertice_A)
        linha_CB = Line(vertice_C, vertice_B)
        # Com os segmentos criados, faremos agora os ângulos:

        sector_A = Sector(arc_center=vertice_A, start_angle=linha_AB.get_angle(), angle=linha_AC.get_angle() - linha_AB.get_angle(), radius=0.7, color=RED, fill_opacity=0.8)
        # "sector_A = Sector(...)" Cria um setor circular
        # "arc_center=vertice_A" Nos diz que o centro do arco é o vértice A
        # "start_angle=linha_AB.get_angle()" Nos diz o ângulo onde o arco começa.
        # "angle=linha_AC.get_angle() - linha_AB.get_angle()" Nos diz o tamanho angular do setor
        # "radius=0.7" É o raio do arco
        sector_B = Sector(arc_center=vertice_B, start_angle=linha_BC.get_angle(), angle=linha_BA.get_angle() - linha_BC.get_angle(), radius=0.7, color=GREEN, fill_opacity=0.8)
        sector_C = Sector(arc_center=vertice_C, start_angle=linha_CA.get_angle(), angle=linha_CB.get_angle() - linha_CA.get_angle(), radius=0.7, color=YELLOW, fill_opacity=0.8)

        # Agora iremos criar os rótulos dos ângulos:
        rotulo_alpha = MathTex(r"\alpha", color=BLACK, font_size=36).move_to(sector_A.get_center_of_mass()) 
        #  "rotulo_alpha = MathTex(r"\alpha", color=BLACK, font_size=36)" Cria o rotulo do ângulo
        # ".move_to(sector_A.get_center_of_mass())" Coloca o rotulo no centro do ângulo
        rotulo_beta = MathTex(r"\beta", color=BLACK, font_size=36).move_to(sector_B.get_center_of_mass())
        rotulo_gamma = MathTex(r"\gamma", color=BLACK, font_size=36).move_to(sector_C.get_center_of_mass())

        # Agora, finalmente, faremos a construção do triângulo com seus vértices e ângulos.
        self.play(Create(triangulo), Write(rotulos_vertices), run_time=2)
        # "self.play(Create(triangulo), Write(rotulos_vertices), run_time=2" Anima o triângulo, rótulos e vértices.
        self.wait(1) # Pausa de 1 segundo da nossa animação

        self.play(LaggedStart(
            # O "LaggedStart(...)" Vai executar as animações com um pequeno atraso entre elas.
            FadeIn(sector_A, scale=0.5), Write(rotulo_alpha), # Fará aparecer o ângulo e do seu rótulo.
            FadeIn(sector_B, scale=0.5), Write(rotulo_beta),
            FadeIn(sector_C, scale=0.5), Write(rotulo_gamma),
            lag_ratio=0.5)) # Faz com que os ângulos apareçam um após o outro.
        self.wait(0.2)

        # Agora iremos fazer a animação de recuo:
        triangulo_completo = VGroup(triangulo, rotulos_vertices, sector_A, sector_B, sector_C, rotulo_alpha, rotulo_beta, rotulo_gamma) # Agrupamos tudo que fizemos até agora
        linha_guia = Line(LEFT * 4, RIGHT * 4, color=BLUE).to_edge(DOWN, buff=1.5) # Cria a linha horizontal na parte de baixo da tela que servirá de base para juntar os ângulos.

        self.play(
            # ".animate" Podemos aplicar o recuo de forma animada.
            # ".scale(0.8)" Reduz o tamanho do grupo para 80% do original.
            # #.to_edge(UP)" Move o grupo para a borda superior da tela.
            triangulo_completo.animate.scale(0.8).to_edge(UP), 
            Create(linha_guia)) # Anima a criação da linha ao mesmo tempo que o triângulo se move.
        self.wait(1)

        # Agora iremos preparar as cópias dos ângulos para a animação final.
        ponto_encontro = linha_guia.get_center() # Define o ponto central da linha guia como o local onde os ângulos se encontrarão.
        copia_A = VGroup(sector_A.copy(), rotulo_alpha.copy()) # Cria uma cópia exata do ângulo A e seu rótulo. É essa cópia que será movida e transformada. 
        copia_B = VGroup(sector_B.copy(), rotulo_beta.copy())
        copia_C = VGroup(sector_C.copy(), rotulo_gamma.copy())
        
        tamanho_A = sector_A.angle # Armazena o valor numérico do ângulo A para usá-lo na criação do ângulo de destino.
        tamanho_B = sector_B.angle
        tamanho_C = sector_C.angle

        alvo_C = Sector(arc_center=ponto_encontro, radius=0.7, start_angle=PI - tamanho_C, angle=tamanho_C, color=YELLOW, fill_opacity=0.8)
        alvo_B = Sector(arc_center=ponto_encontro, radius=0.7, start_angle=tamanho_A, angle=tamanho_B, color=GREEN, fill_opacity=0.8)
        alvo_A = Sector(arc_center=ponto_encontro, radius=0.7, start_angle=0, angle=tamanho_A, color=RED, fill_opacity=0.8) # Cria a forma final que a copia_A deve assumir
        # "arc_center=ponto_encontro" O centro do novo ângulo será o ponto de encontro.
        # "start_angle=0" O alvo do ângulo A começa no ângulo 0 (apontando para a direita).
        # "angle=tamanho_A" Ele terá o mesmo tamanho do ângulo A original.

        # Adicionando as letras dos ângulos menores e nos alvos também
        rotulo_alvo_gamma = MathTex(r"\gamma", color=BLACK, font_size=36).move_to(alvo_C.get_center_of_mass()) # Criamos uma nova letra gamma. Esta será a posição final da letra que está na cópia.
        # Com ".move_to(alvo_C.get_center_of_mass())" Movemos essa nova letra para o centro do alvo_C (o setor vermelho que já está na linha reta).
        rotulo_alvo_beta = MathTex(r"\beta", color=BLACK, font_size=36).move_to(alvo_B.get_center_of_mass())
        rotulo_alvo_alpha = MathTex(r"\alpha", color=BLACK, font_size=36).move_to(alvo_A.get_center_of_mass())
        grupo_alvo_C = VGroup(alvo_C, rotulo_alvo_gamma)
        grupo_alvo_B = VGroup(alvo_B, rotulo_alvo_beta)
        grupo_alvo_A = VGroup(alvo_A, rotulo_alvo_alpha)

        # Os três ângulos (α, β, γ) agora formaram um semicírculo perfeito, alinhados sobre a linha de referência
        self.play(
            LaggedStart(
                # "Transform(copia_C, grupo_alvo_C)" Ela pega o objeto copia_C (que está na posição original, no triângulo) e o transforma suavemente no objeto grupo_alvo_C (na posição final, sobre a linha guia).
                Transform(copia_C, grupo_alvo_C), 
                Transform(copia_B, grupo_alvo_B),
                Transform(copia_A, grupo_alvo_A),
                lag_ratio=0.2),
            run_time=3)
        self.wait(1)

        # Animação do texto final, finalizando a demonstração visual.
        texto_final = MathTex(r"\alpha + \beta + \gamma = 180^\circ", font_size=48)
        texto_final.next_to(linha_guia, UP, buff=1.0)
        self.play(Write(texto_final), run_time=4)
        self.wait(4)