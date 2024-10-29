import jwt from 'jsonwebtoken';

export const authenticateToken = (req, res, next) => {
  const token = req.header('Authorization')?.split(' ')[1]; // Assuming "Bearer <token>" format
  if (!token) return res.status(401).json({ message: 'Access denied. No token provided.' });

  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.organizer = decoded; // Attaching organizer info from token payload
    next();
  } catch (error) {
    res.status(403).json({ message: 'Invalid token.' });
  }
};
