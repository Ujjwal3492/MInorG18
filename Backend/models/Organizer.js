import mongoose from 'mongoose';

const { Schema } = mongoose;



const OrganizerSchema = new Schema({
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  password: { type: String, required: true },
  phone: { type: String },
  address: {
    street: { type: String },
    city: { type: String },
    state: { type: String },
    zip: { type: String }
  },
  company_name: { type: String }, 
  role: { type: String }, 
  joined_date: { type: Date, default: Date.now },
  managed_events: [{ type: Schema.Types.ObjectId, ref: 'Event' }],
  created_at: { type: Date, default: Date.now },
  updated_at: { type: Date, default: Date.now }
});

OrganizerSchema.pre('save', function (next) {
  this.updated_at = Date.now();
  next();
});

export default mongoose.model('Organizer', OrganizerSchema);
