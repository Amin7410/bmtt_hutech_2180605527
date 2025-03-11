from cipher.vigenere import VigenereCipher
from flask import Flask, request, jsonify

app = Flask(__name__)

vigenere_cipher = VigenereCipher()

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})
def vigenere_decrypt():
    data = request.json
    cipher_text = data['encrypted_text']
    key = data['key']
    decrypted_text = vigenere_cipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})