// require=require("esm")(module);

import express from "express";
import bodyParser from "body-parser";
import morgan from "morgan";
import mongoose from "mongoose"

import config from "./config"
import api from "./routes/api"

const port = process.env.PORT || 3000
// console.log(port);

const app = express()

app.use(bodyParser.urlencoded({extended: false}))
app.use(bodyParser.json())

app.use(morgan('dev'))

app.set('jwt-secret', config.secret)

app.get('/', (req, res)=>{
    res.send('Hello jwt')
})
app.use('/api', api)


app.listen(port, ()=>{
    console.log(`exp running on ${port}`)
})

mongoose.connect(config.mongodbUri, {useNewUrlParser: true, useUnifiedTopology: true})
const db = mongoose.connection
db.on('error', console.error)
db.once('open', ()=>{
    console.log('mongodb connected')
})
