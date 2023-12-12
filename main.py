from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def f_index():
    return {"Шихалева Екатерина Константиновна"}

@app.get('/tools')
async def f_indexT():
    return "Начальные навыки"

@app.get('/users')
async def f_indexU():
    return "+79169763542"