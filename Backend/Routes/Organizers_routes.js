import express from 'express';
import { registerOrganizer, loginOrganizer } from '../controllers/Oraganizers.js';
import { authenticateToken } from '../middleware/authenticate.js';
const router = express.Router();


router.post('/register', registerOrganizer);


router.get('/login', loginOrganizer);

export default router;
