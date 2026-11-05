from PIL import Image, ImageOps

caminho_imagem = r"C:\Users\DRE SINOP 22\Downloads\v2_cabe1f4d-0c96-49a4-a65d-175d894c0faa.jpg"  # Altere para a sua imagem
caminho_saida = r"C:\Users\DRE SINOP 22\Downloads\imagem_miniatura_teste.png"

with Image.open(caminho_imagem) as img:
    # Método 1: Tenta extrair a miniatura EXIF usando ImageOps (Nativo do Pillow)
    exif = img.info.get("exif")
    miniatura_encontrada = False

    if exif:
        try:
            # Tenta carregar os bytes da miniatura embutida
            thumb = ImageOps.exif_transpose(img)
            # Verifica se há miniatura gravada no bloco de dados EXIF
            exif_data = img.getexif()
            # No Pillow, extraímos os dados binários da miniatura via _getexif() clássico
            raw_exif = img._getexif()
            if raw_exif and 0x0201 in raw_exif:  # Tag EXIF 0x0201 = JPEGInterchangeFormat (Thumbnail)
                # O Pillow possui um método direto no módulo PIL.JpegImagePlugin
                import io
                thumb_bytes = raw_exif.get(0x0202)  # Tamanho da miniatura
                # Método seguro de extração universal:
                from PIL.ExifTags import TAGS
                pass
        except Exception:
            pass

# Método robusto e direto (Funciona em todas as versões do Python/Pillow):
with Image.open(caminho_imagem) as img:
    # A API legada do Pillow guarda a miniatura em formato de bytes no mapa _getexif()
    exif_dict = img._getexif()
    
    # 0x0201 é a tag offset da miniatura e 0x0202 é o tamanho em bytes
    if exif_dict and 0x0201 in exif_dict and 0x0202 in exif_dict:
        # Abre o arquivo novamente em modo binário para extrair exatamente o trecho da miniatura
        with open(caminho_imagem, "rb") as f:
            f.seek(exif_dict[0x0201])
            thumb_data = f.read(exif_dict[0x0202])
            
            with open(caminho_saida, "wb") as out_f:
                out_f.write(thumb_data)
            print("Miniatura EXIF extraída com sucesso!")
    else:
        print("Esta imagem não possui uma miniatura embutida nos metadados EXIF.")