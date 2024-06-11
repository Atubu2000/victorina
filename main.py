from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Пример вопросов и ответов на тему пророков
questions = [
    {
        "question": "Как зовут первого пророка в исламе?",
        "choices": ["Мухаммад", "Муса", "Ибрахим", "Адам"],
        "answer": "Адам"
    },
    {
        "question": "Как зовут пророка, которому был дан Таурат (Тора)?",
        "choices": ["Иса", "Муса", "Давуд", "Сулейман"],
        "answer": "Муса"
    },
    {
        "question": "Как зовут пророка, который построил ковчег?",
        "choices": ["Ибрахим", "Нух", "Юсуф", "Исмаил"],
        "answer": "Нух"
    },
    {
        "question": "Как зовут пророка, который был вознесен на небо живым?",
        "choices": ["Иса", "Идрис", "Юнус", "Худ"],
        "answer": "Иса"
    },
    {
        "question": "Как зовут пророка, который был брошен в огонь, но остался невредим?",
        "choices": ["Лут", "Ибрахим", "Юсуф", "Муса"],
        "answer": "Ибрахим"
    },
    {
        "question": "Как зовут пророка, который был проглочен китом?",
        "choices": ["Юнус", "Идрис", "Исхак", "Иса"],
        "answer": "Юнус"
    },
    {
        "question": "Как зовут пророка, который разговаривал с животными?",
        "choices": ["Сулейман", "Давуд", "Юсуф", "Муса"],
        "answer": "Сулейман"
    },
    {
        "question": "Как зовут пророка, которому был дан Забур?",
        "choices": ["Муса", "Давуд", "Сулейман", "Иса"],
        "answer": "Давуд"
    },
    {
        "question": "Как зовут пророка, который был продан в рабство и стал министром в Египте?",
        "choices": ["Юсуф", "Муса", "Ибрахим", "Юнус"],
        "answer": "Юсуф"
    },
    {
        "question": "Как зовут пророка, который родился без отца?",
        "choices": ["Иса", "Муса", "Идрис", "Нух"],
        "answer": "Иса"
    },
    {
        "question": "Как зовут пророка, который разрушил идолов, принадлежавших его народу?",
        "choices": ["Ибрахим", "Мухаммад", "Юнус", "Лут"],
        "answer": "Ибрахим"
    },
    {
        "question": "Как зовут пророка, который был спасен от утопления в реке Нил?",
        "choices": ["Муса", "Иса", "Юсуф", "Юнус"],
        "answer": "Муса"
    },
    {
        "question": "Как зовут пророка, который был избран Аллахом, чтобы привести свой народ к покаянию в Ниневии?",
        "choices": ["Юнус", "Худ", "Салих", "Лут"],
        "answer": "Юнус"
    },
    {
        "question": "Как зовут пророка, который был вознесен на небеса на ночь?",
        "choices": ["Мухаммад", "Идрис", "Иса", "Муса"],
        "answer": "Мухаммад"
    },
    {
        "question": "Как зовут пророка, который был послан к народу Ад?",
        "choices": ["Худ", "Салих", "Лут", "Идрис"],
        "answer": "Худ"
    },
    {
        "question": "Как зовут пророка, который был послан к народу Самуд?",
        "choices": ["Салих", "Худ", "Лут", "Идрис"],
        "answer": "Салих"
    },
    {
        "question": "Как зовут пророка, который был известен своей великой мудростью?",
        "choices": ["Сулейман", "Давуд", "Юсуф", "Муса"],
        "answer": "Сулейман"
    },
    {
        "question": "Как зовут пророка, который получил откровение в пещере Хира?",
        "choices": ["Мухаммад", "Муса", "Иса", "Давуд"],
        "answer": "Мухаммад"
    },
    {
        "question": "Как зовут пророка, который был сыном Марьям?",
        "choices": ["Иса", "Муса", "Юсуф", "Давуд"],
        "answer": "Иса"
    },
    {
        "question": "Как зовут пророка, который был известен своей терпимостью и покорностью?",
        "choices": ["Аюб", "Юсуф", "Ибрахим", "Юнус"],
        "answer": "Аюб"
    },
    {
        "question": "Как зовут пророка, который был известен как 'друг Аллаха'?",
        "choices": ["Ибрахим", "Муса", "Давуд", "Мухаммад"],
        "answer": "Ибрахим"
    },
    {
        "question": "Как зовут пророка, который получил откровение на горе Синай?",
        "choices": ["Муса", "Иса", "Давуд", "Сулейман"],
        "answer": "Муса"
    },
    {
        "question": "Как зовут пророка, который был известен своей физической силой?",
        "choices": ["Симсон", "Муса", "Юсуф", "Давуд"],
        "answer": "Симсон"
    },
    {
        "question": "Как зовут пророка, который стал царем после Давуда?",
        "choices": ["Сулейман", "Муса", "Иса", "Юсуф"],
        "answer": "Сулейман"
    },
    {
        "question": "Как зовут пророка, который был известен своей музыкой и поэзией?",
        "choices": ["Давуд", "Муса", "Сулейман", "Ибрахим"],
        "answer": "Давуд"
    },
    {
        "question": "Как зовут пророка, который был рожден после долгого бесплодия его родителей?",
        "choices": ["Исхак", "Муса", "Юсуф", "Идрис"],
        "answer": "Исхак"
    },
    {
        "question": "Как зовут пророка, который был известен своей способностью к ясновидению?",
        "choices": ["Юсуф", "Сулейман", "Идрис", "Муса"],
        "answer": "Юсуф"
    },
    {
        "question": "Как зовут пророка, который стал пастухом после побега из Египта?",
        "choices": ["Муса", "Юсуф", "Давуд", "Сулейман"],
        "answer": "Муса"
    },
    {
        "question": "Как зовут пророка, который был избран Аллахом для возрождения мертвых?",
        "choices": ["Иса", "Муса", "Ибрахим", "Юсуф"],
        "answer": "Иса"
    },
    {
        "question": "Как зовут пророка, который построил Каабу?",
        "choices": ["Ибрахим", "Муса", "Давуд", "Сулейман"],
        "answer": "Ибрахим"
    }
]

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/quiz")
async def get_quiz():
    return questions

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)