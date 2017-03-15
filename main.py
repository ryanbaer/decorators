from app import App
import sys

app = App()

@app.route("/home")
@app.route("/index")
@app.route("/")
def home():
    print("Welcome to here")

@app.route("/narnia")
def narnia():
    print("Welcome to there")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("must provide route")
        exit(1)

    app.request(sys.argv[1])
