from fastapi import FastAPI
import uvicorn

app = FastAPI()

app.post('/Books')
def Get_Books_Name():
    return {}

if __name__ == '__main__':
    uvicorn.run(app)