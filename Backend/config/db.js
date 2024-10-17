import mongoose from "mongoose";


const ConnectDB= async()=>{
    const mongo_uri=process.env.MONGO_URI;

    
    try{
       await mongoose.connect(mongo_uri);
       console.log({
        message:"mongo is connected"
       })
    }catch(err){
        console.error(err);
        
    }
}

export default ConnectDB;