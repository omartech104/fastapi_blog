from fastapi import FastAPI

app = FastAPI()

# Sample data for blog posts to test the get end point
posts = [{
    "id": 1,
    "author":"Omar Mohammed",
    "title": "First Post",
    "content": "This is the content of the first post.",
    "date_posted": "2023-06-01"
}, {
    "id": 2,
    "author":"Omar Mohammed",
    "title": "Second Post",
    "content": "This is the content of the second post.",
    "date_posted": "2026-06-02"
   }
]

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI Blog!"}

@app.get("/api/posts")
async def get_posts():
    return posts