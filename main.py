from typing import Optional
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr
from database import Base,engine
from routers import item_router
app = FastAPI()
Base.metadata.create_all(engine)

app.include_router(item_router)


if __name__=='__main__':
    uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info")