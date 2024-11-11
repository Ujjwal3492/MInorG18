import mongoose from 'mongoose';

const { Schema } = mongoose;
const EventSchema = new Schema({
  title: { type: String, required: true },
  description: { type: String },
  category: { type: String }, 
  start_date: { type: Date, required: true },
  end_date: { type: Date, required: true },
  location: {
    venue: { type: String },
    city: { type: String },
    state: { type: String },
    country: { type: String }
  },
  organizer: { type: Schema.Types.ObjectId, ref: 'Organizer', required: true },
  participants: [{ type: Schema.Types.ObjectId, ref: 'Participant' }],
  metrics: {
    total_participants: { type: Number, default: 0 },
    average_rating: { type: Number, default: 0 }, 
    participant_engagement: { type: Number, default: 0 } 
  },
  created_at: { type: Date, default: Date.now },
  updated_at: { type: Date, default: Date.now }
});

EventSchema.pre('save', function (next) {
  this.updated_at = Date.now();
  next();
});

export default mongoose.model('Event', EventSchema);
