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
  
// Get All Organizers
export const getAllOrganizers = async (req, res) => {
  try {
    const organizers = await Organizer.find();
    res.status(200).json(organizers);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

// Get Organizer by ID
export const getOrganizerById = async (req, res) => {
  try {
    const { id } = req.params;
    const organizer = await Organizer.findById(id);
    if (!organizer) {
      return res.status(404).json({ message: 'Organizer not found' });
    }
    res.status(200).json(organizer);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

// Update Organizer
export const updateOrganizer = async (req, res) => {
  try {
    const { id } = req.params;
    const { name, email, phone, company_name, role } = req.body;

    // Check if the organizer exists
    const organizer = await Organizer.findById(id);
    if (!organizer) {
      return res.status(404).json({ message: 'Organizer not found' });
    }

    // Update organizer details
    organizer.name = name || organizer.name;
    organizer.email = email || organizer.email;
    organizer.phone = phone || organizer.phone;
    organizer.company_name = company_name || organizer.company_name;
    organizer.role = role || organizer.role;

    // Save updated organizer to the database
    await organizer.save();

    res.status(200).json({ message: 'Organizer updated successfully', organizer });
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

// Delete Organizer
export const deleteOrganizer = async (req, res) => {
  try {
    const { id } = req.params;

    // Check if the organizer exists
    const organizer = await Organizer.findById(id);
    if (!organizer) {
      return res.status(404).json({ message: 'Organizer not found' });
    }

    // Delete organizer
    await organizer.deleteOne();

    res.status(200).json({ message: 'Organizer deleted successfully' });
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};