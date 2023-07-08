from flask import Flask,session,jsonify,render_template,redirect,url_for,request,abort
from datetime import timedelta
from global_variable import *
from common.connectios import Connection
