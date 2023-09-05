from fastapi import APIRouter, File, UploadFile
from typing import Annotated


files_router = APIRouter()


# PATH converter
# O componente :path diz que o parametro deve correnponder com um caminho
# Pode ser necessário um parametro como /home/user/my_file.txt
# Esse sera reprensentado na URL como /files//home/user/my_file.txt
# contendo barras duplas (//) ou (/%2) na URL
@files_router.get("/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


# Declarando como bytes, FastAPI irá ler e receber o arquivo como bytes,
# o que significa que todo o conteudo será armazenado na memoria, isso
# funciona bem para arquivos pequenos
@files_router.post("/")
async def create_file(file: Annotated[bytes | None, File()] = None):
    if not file:
        return {"message": "No file sent"}
    else:
        return {"file_size": len(file)}


# UploadFile tem varias vantagens, possui um limite de tamanho e passando
# armazena em disco, melhor para arquivos maiores, imagens, video, etc
@files_router.post("/uploadfile")
async def create_upload_file(file: UploadFile):
    # UploadFile possui os seguintes atributos:
    # filename: str
    # content_type: str
    # file: SpooledTemporaryFile
    # E os metodos write(data), read(size), seek(offset) e close()
    # Todos esses metodos são async, sendo necessario "await" eles
    return {"filename": file.filename}
