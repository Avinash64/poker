from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


game = {
  "game_id": "123456",
  "status": "in_progress",
  "current_turn": 2,
  "pot": 1000,
  "community_cards": ["2H", "4S", "7C", "TS", "AH"],
  "players": [
    {
      "player_id": 1,
      "name": "Player 1",
      "chips": 500,
      "hand": ["3D", "3S"],
      "bet": 50
    },
    {
      "player_id": 2,
      "name": "Player 2",
      "chips": 750,
      "hand": ["5H", "5C"],
      "bet": 50
    },
    {
      "player_id": 3,
      "name": "Player 3",
      "chips": 600,
      "hand": [],
      "bet": 0
    }
  ]
}

@app.get("/")
async def main():
    return game
