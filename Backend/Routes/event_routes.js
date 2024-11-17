import express from 'express';
import { authenticateToken } from '../middleware/authenticate.js';
import { createEvent, getEventById, updateEvent, deleteEvent, getAllEvents } from '../controllers/Events.js';

const router = express.Router();

// Use the middleware to check the token
router.post('/create', authenticateToken, createEvent);
router.get('/get', authenticateToken, getAllEvents);
router.get('/withId/:id', authenticateToken, getEventById);
router.put('/update/:id', authenticateToken, updateEvent);
router.delete('/delete/:id', authenticateToken, deleteEvent);

export default router;