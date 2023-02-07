from fastapi import FastAPI
import uvicorn

app = FastAPI()

book_names = ['Physics paper 1' , 'Chemistry Paper 1' , 'Biology paper 1']
dict_book_links = {}


@app.get('/Books')
def Get_Book_Name():
    return book_names


if __name__ == '__main__':
    uvicorn.run(app , host = '0.0.0.0' , port = 5000)