from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from langserve import add_routes
from .medico_langchain import chain

app = FastAPI(
    title="medical-information-bot",
    description="Built upon langchain ecosystem and general purpose use only",
    version="1.0.0"
        )

add_routes(app, chain, path="/medical_chat")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8000)