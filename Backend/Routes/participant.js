import express from 'express';
import {
  createParticipant,
  getParticipantById,
  updateParticipant,
  deleteParticipant,
  loginParticipant
} from '../controllers/participantController.js';
import { authenticateToken } from '../middleware/authenticate.js'; // Import the middleware

const router = express.Router();

router.get('/participants/login', loginParticipant);

router.post('/participants/create', createParticipant); 
router.get('/participants/:id', authenticateToken, getParticipantById); 
router.put('/participant_update/:id', authenticateToken, updateParticipant); 
router.delete('/participant_delete/:id', authenticateToken, deleteParticipant);
export default router;
