import serial
import threading
import time


from flask import Flask, jsonify, render_template, render_template_string

app = Flask(__name__)
