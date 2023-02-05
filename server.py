from fastapi import FastAPI
import uvicorn

app = FastAPI()
app.get('/Books')


book_names = ['Physics paper 1' , 'Chemistry Paper 1' , 'Biology paper 1']
dict_book_links = {}

#Ready for testing!
async def Get_Book_Name():
    return book_names

if __name__ == '__main__':
    uvicorn.run(app)