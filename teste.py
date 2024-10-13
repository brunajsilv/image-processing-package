from image_processing.processing.combination import combinar_imagens
from image_processing.processing.transformation import redimensionar_imagem, rotacionar_imagem, converter_para_preto_branco

# 1. Combinar imagens
imagens = ["imagens/imagem1.jpg", "imagens/imagem2.jpg"]
combinar_imagens(imagens, "imagem_combinada.jpg")
print("Imagem combinada criada com sucesso!")

# 2. Redimensionar as três imagens (imagem1, imagem2 e imagem combinada)
redimensionar_imagem("imagens/imagem1.jpg", (300, 300), "imagem1_redimensionada.jpg")
redimensionar_imagem("imagens/imagem2.jpg", (300, 300), "imagem2_redimensionada.jpg")
redimensionar_imagem("imagem_combinada.jpg", (300, 300), "imagem_combinada_redimensionada.jpg")
print("Imagens redimensionadas com sucesso!")

# 3. Rotacionar as três imagens (imagem1, imagem2 e imagem combinada)
rotacionar_imagem("imagens/imagem1.jpg", 45, "imagem1_rotacionada.jpg")
rotacionar_imagem("imagens/imagem2.jpg", 45, "imagem2_rotacionada.jpg")
rotacionar_imagem("imagem_combinada.jpg", 45, "imagem_combinada_rotacionada.jpg")
print("Imagens rotacionadas com sucesso!")

# 4. Converter para preto e branco as três imagens (imagem1, imagem2 e imagem combinada)
converter_para_preto_branco("imagens/imagem1.jpg", "imagem1_pb.jpg")
converter_para_preto_branco("imagens/imagem2.jpg", "imagem2_pb.jpg")
converter_para_preto_branco("imagem_combinada.jpg", "imagem_combinada_pb.jpg")
print("Imagens convertidas para preto e branco com sucesso!")