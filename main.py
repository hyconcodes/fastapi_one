from fastapi import FastAPI

app = FastAPI()

@app.get('/get_users')
async def get_users():
    return "Welcome to fast API"

@app.get('/get_admin')
async def get_admin():
    return { 
            'admin' : {
        '1' : "olamide",
        '2' : "bolaji",
        '3' : "olalekan"
    }
}