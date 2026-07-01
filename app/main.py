from ensurepip import __main__

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from app import crud
from app import schemas
from app.database import get_db

app = FastAPI()

@app.get("/")
def root():
    return "Welcome! check the docs : /docs"

@app.post("/shorten", response_model=schemas.URL)
def shorten(url_data: schemas.URLCreate, db: Session = Depends(get_db)):
    return crud.create_url(db, url_data)

@app.get("/{short_code}")
def get_url(short_code: str, db : Session = Depends(get_db)):
    url_retrieve = crud.get_url(db, short_code)
    if not url_retrieve:
        raise HTTPException(status_code=404)
    return RedirectResponse(url=str(url_retrieve.original_url))

if __name__ == __main__:
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)