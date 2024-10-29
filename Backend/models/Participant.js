import mongoose from 'mongoose';

const { Schema } = mongoose;

//to check engagement  
const EngagementMetricsSchema = new Schema({
  login_count: { type: Number, default: 0 }, 
  last_login: { type: Date }, 
  participation_rate: { type: Number, default: 0 }, 
  feedback_count: { type: Number, default: 0 } 
});


const ParticipantSchema = new Schema({
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  phone: { type: String },
  address: {
    street: { type: String },
    city: { type: String },
    state: { type: String },
    zip: { type: String }
  },
  date_of_birth: { type: Date }, 
  gender: { type: String, enum: ['Male', 'Female', 'Other'] },
  registration_date: { type: Date, default: Date.now },
  engagement_metrics: EngagementMetricsSchema,
  created_at: { type: Date, default: Date.now },
  updated_at: { type: Date, default: Date.now }
});

ParticipantSchema.pre('save', function (next) {
  this.updated_at = Date.now();
  next();
});

export default mongoose.model('Participant', ParticipantSchema);
