from app import app

with open('banner.txt', 'r') as f:
    banner = f.read()
    print(banner)

if __name__ == "__main__":
    app.run(debug=True)
