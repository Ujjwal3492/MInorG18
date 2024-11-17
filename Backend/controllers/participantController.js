import bcrypt from 'bcrypt';
import jwt from 'jsonwebtoken';
import Participant from '../models/Participant.js';

// Create a new participant (register-like functionality)
export const createParticipant = async (req, res) => {
  try {
    const { name, email, password, phone, address, date_of_birth, gender } = req.body;

    // Check if the participant already exists
    const existingParticipant = await Participant.findOne({ email });
    if (existingParticipant) {
      return res.status(400).json({ message: 'Email already registered.' });
    }

    // Hash the password
    const hashedPassword = await bcrypt.hash(password, 10);

    // Create a new participant
    const newParticipant = new Participant({
      name,
      email,
      password: hashedPassword,
      phone,
      address,
      date_of_birth,
      gender,
    });

    // Save the participant to the database
    await newParticipant.save();

    res.status(201).json({ message: 'Participant created successfully', participant: newParticipant });
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

// Get participant by ID
export const getParticipantById = async (req, res) => {
  try {
    const { id } = req.params;
    const participant = await Participant.findById(id);

    if (!participant) {
      return res.status(404).json({ message: 'Participant not found' });
    }

    res.status(200).json(participant);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

// Update participant by ID
export const updateParticipant = async (req, res) => {
  try {
    const { id } = req.params;
    const { name, phone, address, date_of_birth, gender } = req.body;

    const participant = await Participant.findById(id);
    if (!participant) {
      return res.status(404).json({ message: 'Participant not found' });
    }

    // Update participant details
    participant.name = name || participant.name;
    participant.phone = phone || participant.phone;
    participant.address = address || participant.address;
    participant.date_of_birth = date_of_birth || participant.date_of_birth;
    participant.gender = gender || participant.gender;

    await participant.save();

    res.status(200).json({ message: 'Participant updated successfully', participant });
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

// Delete participant by ID
export const deleteParticipant = async (req, res) => {
  try {
    const { id } = req.params;
    const participant = await Participant.findByIdAndDelete(id);

    if (!participant) {
      return res.status(404).json({ message: 'Participant not found' });
    }

    res.status(200).json({ message: 'Participant deleted successfully' });
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

// Login Participant
export const loginParticipant = async (req, res) => {
  try {
    const { email, password } = req.body;

    if (!email || !password) {
      return res.status(400).json({ message: 'Email and password are required.' });
    }

    const participant = await Participant.findOne({ email });
    if (!participant) {
      return res.status(400).json({ message: 'Invalid email or password' });
    }

    const isPasswordValid = await bcrypt.compare(password, participant.password);
    if (!isPasswordValid) {
      return res.status(400).json({ message: 'Invalid email or password' });
    }

    const token = jwt.sign(
      { id: participant._id, email: participant.email },
      process.env.JWT_SECRET,
      { expiresIn: process.env.JWT_EXPIRATION || '1d' }
    );

    res.status(200).json({ message: 'Login successful', token });
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};
