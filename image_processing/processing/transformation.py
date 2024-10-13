from PIL import Image

# Função para redimensionar imagem
def redimensionar_imagem(caminho_imagem, novo_tamanho, caminho_saida):
    """
    Redimensiona uma imagem para o tamanho especificado e salva em um arquivo.
    
    Args:
    caminho_imagem (str): Caminho da imagem original.
    novo_tamanho (tuple): Novo tamanho como (largura, altura).
    caminho_saida (str): Caminho para salvar a imagem redimensionada.
    """
    try:
        img = Image.open(caminho_imagem)
        img_redimensionada = img.resize(novo_tamanho)
        img_redimensionada.save(caminho_saida)
        print(f"Imagem redimensionada salva em: {caminho_saida}")
    
    except Exception as e:
        print(f"Erro ao redimensionar a imagem: {e}")

# Função para rotacionar imagem
def rotacionar_imagem(caminho_imagem, angulo, caminho_saida):
    """
    Rotaciona a imagem pelo ângulo fornecido e salva em um arquivo.
    
    Args:
    caminho_imagem (str): Caminho da imagem original.
    angulo (int): Ângulo de rotação em graus.
    caminho_saida (str): Caminho para salvar a imagem rotacionada.
    """
    try:
        img = Image.open(caminho_imagem)
        img_rotacionada = img.rotate(angulo)
        img_rotacionada.save(caminho_saida)
        print(f"Imagem rotacionada salva em: {caminho_saida}")
    
    except Exception as e:
        print(f"Erro ao rotacionar a imagem: {e}")

# Função para converter imagem para preto e branco
def converter_para_preto_branco(caminho_imagem, caminho_saida):
    """
    Converte a imagem para preto e branco e salva em um arquivo.
    
    Args:
    caminho_imagem (str): Caminho da imagem original.
    caminho_saida (str): Caminho para salvar a imagem em preto e branco.
    """
    try:
        img = Image.open(caminho_imagem)
        img_pb = img.convert('L')  # Converte para preto e branco
        img_pb.save(caminho_saida)
        print(f"Imagem preto e branco salva em: {caminho_saida}")
    
    except Exception as e:
        print(f"Erro ao converter para preto e branco: {e}")