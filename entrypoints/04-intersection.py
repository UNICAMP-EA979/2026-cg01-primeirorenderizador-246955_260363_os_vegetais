import numpy as np
import urenderer

# Renderize uma cena em que o algoritmo de oclusão falha
#
# Observe o método urenderer.renderer.pyplot_renderer.PyplotRenderer::end
# Ele desenha a cena utilizando o "algoritmo do pintor" (painter's algorithm)
# para determinar a visibilidade dos triângulos (qual deve estar por cima do outro)
#
# Crie uma cena com dois cubos de forma que o algoritmo do pintor falhe de forma
# visualmente perceptível.

if __name__ == "__main__":
    urenderer.utils.clear_workdir("04-intersection")
    renderer = urenderer.renderer.PyplotRenderer(1920, 1080)
    runtime = urenderer.application.Runtime(renderer, name="04-intersection")

    # Crie a cena
    cube1 = urenderer.node.Node()
    # Desloca para cima
    cube1.translation = np.array([0, 0.3, -5], np.float64)
    # Rotaciona para "bugar" os triangulos
    cube1.rotation = np.array([45, 45, 45], np.float64)
    cube1.render_data = urenderer.geometry.polygonal_ifs.get_ifs_cube()
    runtime.scene.add_child(cube1)

    cube2 = urenderer.node.Node()
    # Desloca para baixo
    cube2.translation = np.array([0, -0.3, -5], np.float64)
    # Rotaciona para "bugar" os triangulos
    cube2.rotation = np.array([45, 45, 45], np.float64)
    cube2.render_data = urenderer.geometry.polygonal_ifs.get_ifs_cube()
    runtime.scene.add_child(cube2)
    # Roda a cena
    runtime.iter(capture=True)

    
    
