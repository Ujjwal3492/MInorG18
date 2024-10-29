import bcrypt from 'bcrypt';
import jwt from 'jsonwebtoken';
import Organizer from '../models/Organizer.js';


//Register
export const registerOrganizer = async (req, res) => {
    try {
      const { name, email, password, phone, company_name, role } = req.body;
  
      const existingOrganizer = await Organizer.findOne({ email });
      if (existingOrganizer) {
        return res.status(400).json({ message: 'Email already registered.' });
      }
  
      const hashedPassword = await bcrypt.hash(password, 10);
  
      // Create new organizer
      const newOrganizer = new Organizer({
        name,
        email,
        password: hashedPassword,
        phone,
        company_name,
        role
      });
  
      // Save organizer to the database
      await newOrganizer.save();
  
      res.status(201).json({ message: 'Organizer registered successfully' });
    } catch (error) {
      res.status(500).json({ message: error.message });
    }
  };

  //Login

  export const loginOrganizer = async (req, res) => {
    try {
      
  
      const { email, password } = req.body;
  
      if (!email || !password) {
        return res.status(400).json({ message: 'Email and password are required.' });
      }
  
      const organizer = await Organizer.findOne({ email });
      if (!organizer) {
        return res.status(400).json({ message: 'Invalid email or password' });
      }
  
     
      const isPasswordValid = await bcrypt.compare(password, organizer.password);
      console.log(isPasswordValid); 
      if (!isPasswordValid) {
        return res.status(400).json({ message: 'Invalid email or password' });
      }
  
    
      const token = jwt.sign(
        { id: organizer._id, email: organizer.email },
        process.env.JWT_SECRET,
        { expiresIn: process.env.JWT_EXPIRATION || '1d' }
      );
  
      res.status(200).json({ message: 'Login successful', token });
    } catch (error) {
      res.status(500).json({ message: error.message });
    }
  };
  
