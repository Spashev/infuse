import uvicorn


def main():
    uvicorn.run('app.application:app', reload=True)


if __name__ == "__main__":
    main()
