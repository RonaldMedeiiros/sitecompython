from fakepinterest import app

if __name__ == "__main__":
    # Escuta em todas as interfaces (0.0.0.0) e na porta 5000
    app.run(host='0.0.0.0', port=5100, debug=True)
