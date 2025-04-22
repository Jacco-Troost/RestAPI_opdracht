
#imports
from typing import Annotated
from fastapi import FastAPI, HTTPException, Depends, Query
from pydantic import BaseModel
from sqlmodel import Field, Session, SQLModel, create_engine, select



#setUp
api = FastAPI()

# Models setup
class GameBase(SQLModel):
    name: str = Field(index=True)
    console: str | None = Field(default="pc", index=True)
    
class Game(GameBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class GamePublic(GameBase):
    id: int
   
class GameUpdate(GameBase):
    name: str | None = None
    console: str | None = None


#database setup

#add database file 
sqlite_file_name = "game.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

#make a connection
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


#create table
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

#create session
def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

#start database at startup
@api.on_event("startup")
def on_startup():
    create_db_and_tables()



#endpoints
#Endpoint that responds to post-requests and adds a new item
@api.post("/items/",response_model=GamePublic)
async def create_item(item: GameBase, session: SessionDep):
    try:
        db_item = Game.model_validate(item)
        session.add(db_item)
        session.commit()
        session.refresh(db_item)
    except:
        print("something went wrong")
    else:
        return db_item
    


#endpoint wich gets all items http://127.0.0.1:8000/items/
@api.get("/items/",response_model=list[GamePublic])
async def get_items(session: SessionDep, offset: int = 0,  limit: Annotated[int, Query(le=100)] = 100,):
    try:
        games = session.exec(select(Game).offset(offset).limit(limit)).all()
    except:
        print("something went wrong")
    else:  
        return games  
    
#Endpoint to update item with corrensponding itemID 
@api.put("/items/{item_id}",response_model=GamePublic)
async def update_item(item_id: int, item: GameUpdate, session: SessionDep):
    try:
        item_db = session.get(Game, item_id)
    
        #if not in the database return 404
        if not item_db:
            raise HTTPException(status_code=404, detail="game not found")
    
        item_data = item.model_dump(exclude_unset=True)
        item_db.sqlmodel_update(item_data)
        session.add(item_db)
        session.commit()
        session.refresh(item_db)
    
    except:
        print("something went wrong")
    else:
        return item_db


  
#endpoint to delete item with corrensponding itemID    
@api.delete("/items/{item_id}")
async def delete_item(item_id: int, session: SessionDep):
    try:
        game = session.get(Game, item_id)
    
        #if not in the database return 404
        if not game:
            raise HTTPException(status_code=404, detail="game not found")
    
        session.delete(game)
        session.commit()
    except:
        print("something went wrong")
    else:
        return {"ok": True}