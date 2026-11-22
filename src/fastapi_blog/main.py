from pathlib import Path

from fastapi import FastAPI, Request, HTTPException, status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory=Path(__file__).parent / "templates")

app.mount("/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static")

# Sample data for blog posts to test the get end point
posts = [
    {
        "id": 1,
        "author": "Omar Mohammed",
        "title": "First Post",
        "content": "This is the content of the first post.",
        "date_posted": "2023-06-01",
    },
    {
        "id": 2,
        "author": "Omar Mohammed",
        "title": "Second Post",
        "content": "This is the content of the second post.",
        "date_posted": "2026-06-02",
    },
]


@app.get("/", include_in_schema=False, name="read_root")
@app.get("/posts", include_in_schema=False, name="posts")
def read_root(request: Request):
    return templates.TemplateResponse(
        request, "home.html", {"posts": posts, "title": "Home"}
    )

@app.get("/posts/{post_id}", include_in_schema=False)
def post_page(request: Request, post_id: int):
    for post in posts:
        if post.get("id") == post_id:
            title = post["title"][:50]
            return templates.TemplateResponse(
                request,
                "post.html",
                {"post": post, "title": title},
            )
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

@app.get("/api/posts")
def get_posts():
    return posts

@app.get("/api/posts/{post_id}")
def get_posts_using_id(post_id: int):
    for post in posts:
        if post["id"] == post_id:
            return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")