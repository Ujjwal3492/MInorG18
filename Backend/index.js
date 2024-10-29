import express from 'express';
import dotenv from 'dotenv'
import ConnectDB from './config/db.js';
import organizerRoutes from './Routes/Organizers_routes.js'



//dotenv configs 
dotenv.config();
const app = express();
//json definition

app.use(express.json());

app.use('/api/organizers', organizerRoutes);

//mongo config
ConnectDB();


//setting up of the routes 

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