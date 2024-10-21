import express from 'express';
import dotenv from 'dotenv'
import ConnectDB from './config/db.js';
import routesmain from './Routes'


//dotenv configs 
dotenv.config();
const app = express();

//mongo config
ConnectDB();


//setting up of the routes 
app.use('/api/organizer',)

app.get('/',(req,res)=>{
    try{
      res.json({
         message:"we are ready to go"
      })
    }catch(error){
        console.log({
            message:"error before running the function"
        })

    }
})


const port = process.env.PORT

app.listen(port ,()=>{
    console.log(`we are running on http//localhost:${port}` )
} )