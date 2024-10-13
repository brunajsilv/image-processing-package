from PIL import Image

def combinar_imagens(imagens, caminho_saida):
    """
    Combina múltiplas imagens horizontalmente e salva em um arquivo.
    
    Args:
    imagens (list): Lista com os caminhos das imagens a serem combinadas.
    caminho_saida (str): Caminho para salvar a imagem combinada.
    """
    try:
        # Abre todas as imagens
        imgs = [Image.open(img) for img in imagens]

        # Calcula a largura total e a altura máxima
        largura_total = sum([img.width for img in imgs])
        altura_maxima = max([img.height for img in imgs])

        # Cria uma nova imagem com o tamanho combinado
        imagem_combinada = Image.new('RGB', (largura_total, altura_maxima))

        # Cola as imagens lado a lado
        x_offset = 0
        for img in imgs:
            imagem_combinada.paste(img, (x_offset, 0))
            x_offset += img.width

        # Salva a imagem combinada
        imagem_combinada.save(caminho_saida)
        print(f"Imagem combinada salva com sucesso em: {caminho_saida}")
    
    except Exception as e:
        print(f"Erro ao combinar as imagens: {e}")