import numpy as np
import urenderer

# Crie uma cena com três objetos, um filho do outro:
# Objeto0 -> Objeto1 -> Objeto2
#
# Configure as transformações para que todos os objetos sejam visíveis e renderize a cena
#
# Altere a transformação do objeto avô dos outros e renderize a cena.
# Observe como que os objetos filhos se movem juntos

if __name__ == "__main__":
    urenderer.utils.clear_workdir("03-grandchild")
    renderer = urenderer.renderer.PyplotRenderer(1920, 1080)
    runtime = urenderer.application.Runtime(renderer, name="03-grandchild")

    # Crie a cena
    deslocamento_base = -3
    # Criando o Pai
    pai = urenderer.node.Node()
    pai.translation = np.array([0, 0, deslocamento_base], np.float64)
    pai.render_data = urenderer.geometry.polygonal_ifs.get_ifs_cube()
    # Criando o Filho
    filho = urenderer.node.Node()
    filho.translation = np.array([0, 0, deslocamento_base], np.float64)
    filho.render_data = urenderer.geometry.polygonal_ifs.get_ifs_cube()
    # Criando o Neto
    neto = urenderer.node.Node()
    neto.translation = np.array([0, 0, deslocamento_base], np.float64)
    neto.render_data = urenderer.geometry.polygonal_ifs.get_ifs_cube()
    
    pai.add_child(filho)
    filho.add_child(neto)
    runtime.scene.add_child(pai)

    runtime.iter(capture=True)

    # Rotacione o nó avô
    pai.rotation = np.array([0, 30, 0], np.float64)
    
    runtime.iter(capture=True)
