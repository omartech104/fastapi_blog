from fastapi import FastAPI
from fastapi.responses import HTMLResponse

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

@app.get("/", response_class=HTMLResponse)
@app.get("/posts", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>FastAPI Blog</title>
        </head>
        <body>
            <h1>Welcome to the FastAPI Blog!</h1>
            <p>Use the /api/posts endpoint to get the list of blog posts.</p>
        </body>
    </html>
    """

@app.get("/api/posts")
def get_posts():
    return posts