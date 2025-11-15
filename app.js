export const servicesData = [
  {
    icon: "🏠",
    title: "Residential Collection",
    description: "Regular waste collection services for homes and apartments with flexible scheduling options."
  },
  {
    icon: "🏢",
    title: "Commercial Solutions",
    description: "Customized waste management plans for businesses of all sizes with efficient disposal systems."
  },
  {
    icon: "♻️",
    title: "Recycling Programs",
    description: "Comprehensive recycling services to reduce environmental impact and promote sustainability."
  },
  {
    icon: "🌿",
    title: "Organic Waste",
    description: "Specialized composting and organic waste management for garden and food waste."
  },
  {
    icon: "⚠️",
    title: "Hazardous Waste",
    description: "Safe disposal of hazardous materials following all environmental regulations."
  },
  {
    icon: "🏗️",
    title: "Construction Debris",
    description: "Efficient removal and disposal of construction and demolition waste materials."
  }
];

export const statsData = [
  {
    value: "50K+",
    label: "Tons Recycled Annually"
  },
  {
    value: "10K+",
    label: "Happy Customers"
  },
  {
    value: "25+",
    label: "Years of Experience"
  },
  {
    value: "95%",
    label: "Customer Satisfaction"
  }
];
export const wasteTypesData = [
  {
    icon: "🗑️",
    title: "General Waste",
    description: "Everyday household and office waste materials"
  },
  {
    icon: "📦",
    title: "Paper & Cardboard",
    description: "Recyclable paper products and packaging"
  },
  {
    icon: "🍾",
    title: "Plastic & Glass",
    description: "Bottles, containers, and other recyclables"
  },
  {
    icon: "🔋",
    title: "Electronic Waste",
    description: "Old electronics and electronic components"
  },
  {
    icon: "🍃",
    title: "Garden Waste",
    description: "Leaves, branches, grass clippings, and more"
  },
  {
    icon: "🛋️",
    title: "Bulky Items",
    description: "Furniture, appliances, and large items"
  }
];
export const serviceOptions = [
  { value: "residential", label: "Residential Collection" },
  { value: "commercial", label: "Commercial Solutions" },
  { value: "recycling", label: "Recycling Program" },
  { value: "organic", label: "Organic Waste" },
  { value: "hazardous", label: "Hazardous Waste" },
  { value: "construction", label: "Construction Debris" }
];
const express = require('express');
const cors = require('cors');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, 'build')));

// API Routes
app.get('/api/services', (req, res) => {
  const services = [
    {
      icon: "🏠",
      title: "Residential Collection",
      description: "Regular waste collection services for homes and apartments with flexible scheduling options."
    },
    {
      icon: "🏢",
      title: "Commercial Solutions",
      description: "Customized waste management plans for businesses of all sizes with efficient disposal systems."
    },
    {
      icon: "♻️",
      title: "Recycling Programs",
      description: "Comprehensive recycling services to reduce environmental impact and promote sustainability."
    },
    {
      icon: "🌿",
      title: "Organic Waste",
      description: "Specialized composting and organic waste management for garden and food waste."
    },
    {
      icon: "⚠️",
      title: "Hazardous Waste",
      description: "Safe disposal of hazardous materials following all environmental regulations."
    },
    {
      icon: "🏗️",
      title: "Construction Debris",
      description: "Efficient removal and disposal of construction and demolition waste materials."
    }
  ];
  res.json(services);
});

app.get('/api/stats', (req, res) => {
  const stats = [
    {
      value: "50K+",
      label: "Tons Recycled Annually"
    },
    {
      value: "10K+",
      label: "Happy Customers"
    },
    {
      value: "25+",
      label: "Years of Experience"
    },
    {
      value: "95%",
      label: "Customer Satisfaction"
    }
  ];
  res.json(stats);
});

app.post('/api/contact', (req, res) => {
  const { name, email, phone, service, message } = req.body;
  
  // Here you would typically save to database or send email
  console.log('Contact form submission:', { name, email, phone, service, message });
  
  res.json({ 
    success: true, 
    message: 'Thank you for your submission! We will contact you shortly.' 
  });
});

// Serve React app
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'build', 'index.html'));
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});