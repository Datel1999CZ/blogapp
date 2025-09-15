from website import create_app

app = create_app()   # create the Flask app here

if __name__ == "__main__":
    app.run(debug=True)
