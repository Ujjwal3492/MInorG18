import express from 'express';
import {
  registerOrganizer,
  loginOrganizer,
  getAllOrganizers,
  getOrganizerById,
  updateOrganizer,
  deleteOrganizer
} from '../controllers/Organizers.js';
import { authenticateToken } from '../middleware/authenticate.js';

const router = express.Router();

router.post('/register', registerOrganizer);
router.get('/login', loginOrganizer);
router.get('/organizers', authenticateToken, getAllOrganizers);
router.get('/organizers/:id', authenticateToken, getOrganizerById);
router.put('/organizers/:id', authenticateToken, updateOrganizer);
router.delete('/organizers/:id', authenticateToken, deleteOrganizer);

export default router;