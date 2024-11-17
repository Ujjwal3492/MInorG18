import Event from '../models/Event.js';
import Organizer from '../models/Organizer.js';

// Create Event
export const createEvent = async (req, res) => {
  try {
    const { title, description, category, start_date, end_date, location } = req.body;
    const organizerId = req.organizerId; // Retrieve organizer's ID from the token

    // Check if the organizer exists
    const existingOrganizer = await Organizer.findById(organizerId);
    if (!existingOrganizer) {
      return res.status(404).json({ message: 'Organizer not found' });
    }

    const newEvent = new Event({
      title,
      description,
      category,
      start_date,
      end_date,
      location,
      organizer: organizerId // Automatically associate the event with the organizer
    });

    // Save the new event to the database
    await newEvent.save();
    res.status(201).json({ message: 'Event created successfully', event: newEvent });
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};


// Get All Events
export const getAllEvents = async (req, res) => {
    try {
      const organizerId = req.organizerId; // Retrieve organizer's ID from the token
  
      const events = await Event.find({ organizer: organizerId }).populate('organizer');
      res.status(200).json(events);
    } catch (error) {
      res.status(500).json({ message: error.message });
    }
  };

  
  // Get Event by ID
export const getEventById = async (req, res) => {
    try {
      const { id } = req.params;
      const organizerId = req.organizerId; // Retrieve organizer's ID from the token
  
      // Find the event and ensure it belongs to the logged-in organizer
      const event = await Event.findOne({ _id: id, organizer: organizerId }).populate('organizer');
      if (!event) {
        return res.status(404).json({ message: 'Event not found' });
      }
  
      res.status(200).json(event);
    } catch (error) {
      res.status(500).json({ message: error.message });
    }
  };

  

  // Update Event
export const updateEvent = async (req, res) => {
    try {
      const { id } = req.params;
      const organizerId = req.organizerId; // Retrieve organizer's ID from the token
      const { title, description, category, start_date, end_date, location } = req.body;
  
      // Find the event and ensure it belongs to the logged-in organizer
      const event = await Event.findOne({ _id: id, organizer: organizerId });
      if (!event) {
        return res.status(404).json({ message: 'Event not found or access denied' });
      }
  
      // Update the event details
      event.title = title || event.title;
      event.description = description || event.description;
      event.category = category || event.category;
      event.start_date = start_date || event.start_date;
      event.end_date = end_date || event.end_date;
      event.location = location || event.location;
  
      // Save the updated event to the database
      await event.save();
  
      res.status(200).json({ message: 'Event updated successfully', event });
    } catch (error) {
      res.status(500).json({ message: error.message });
    }
  };

  
  // Delete Event
export const deleteEvent = async (req, res) => {
    try {
      const { id } = req.params;
      const organizerId = req.organizerId; // Retrieve organizer's ID from the token
  
      // Find the event and ensure it belongs to the logged-in organizer
      const event = await Event.findOne({ _id: id, organizer: organizerId });
      if (!event) {
        return res.status(404).json({ message: 'Event not found or access denied' });
      }
  
      // Delete the event
      await event.deleteOne();
  
      res.status(200).json({ message: 'Event deleted successfully' });
    } catch (error) {
      res.status(500).json({ message: error.message });
    }
  };
  