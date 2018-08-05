var express = require('express')
var app = express()

var db = require('./db')

app.engine('jade', require('jade')._express)
app.set('view engine', 'jade')

app.use(
