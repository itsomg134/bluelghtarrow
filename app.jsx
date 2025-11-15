import React from 'react';
import Header from './components/Header';
import Hero from './components/Hero';
import Services from './components/Services';
import Stats from './components/Stats';
import WasteTypes from './components/WasteTypes';
import Contact from './components/Contact';
import Footer from './components/Footer';
import './App.css';

function App() {
  return (
    <div className="App">
      <Header />
      <Hero />
      <Services />
      <Stats />
      <WasteTypes />
      <Contact />
      <Footer />
    </div>
  );
}

export default App;
import React from 'react';

const Header = () => {
  return (
    <header>
      <nav>
        <div className="logo">
          <span>♻️</span>
          <span>EcoClean</span>
        </div>
        <ul className="nav-links">
          <li><a href="#home">Home</a></li>
          <li><a href="#services">Services</a></li>
          <li><a href="#waste-types">Waste Types</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;
import React from 'react';

const Hero = () => {
  return (
    <section id="home" className="hero">
      <h1>Professional Waste Management Solutions</h1>
      <p>Creating a cleaner, greener future for our community</p>
      <a href="#contact" className="btn">Get Started Today</a>
    </section>
  );
};

export default Hero;
import React from 'react';
import { servicesData } from '../data/servicesData';

const Services = () => {
  return (
    <section id="services" className="services">
      <div className="container">
        <h2 className="section-title">Our Services</h2>
        <div className="service-grid">
          {servicesData.map((service, index) => (
            <div key={index} className="service-card">
              <div className="service-icon">{service.icon}</div>
              <h3>{service.title}</h3>
              <p>{service.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Services;
import React from 'react';
import { wasteTypesData } from '../data/wasteTypesData';

const WasteTypes = () => {
  return (
    <section id="waste-types" className="waste-types">
      <div className="container">
        <h2 className="section-title">Types of Waste We Handle</h2>
        <div className="waste-grid">
          {wasteTypesData.map((waste, index) => (
            <div key={index} className="waste-item">
              <h4>{waste.icon} {waste.title}</h4>
              <p>{waste.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default WasteTypes;
import React, { useState } from 'react';
import { serviceOptions } from '../data/serviceOptions';

const Contact = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phone: '',
    service: '',
    message: ''
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    alert(`Thank you, ${formData.name}! Your service request has been received. We'll contact you shortly at ${formData.email}.`);
    setFormData({
      name: '',
      email: '',
      phone: '',
      service: '',
      message: ''
    });
  };

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  return (
    <section id="contact" className="services">
      <div className="container">
        <h2 className="section-title">Schedule a Pickup</h2>
        <form className="contact-form" onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="name">Full Name</label>
            <input
              type="text"
              id="name"
              name="name"
              value={formData.name}
              onChange={handleChange}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="email">Email Address</label>
            <input
              type="email"
              id="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="phone">Phone Number</label>
            <input
              type="tel"
              id="phone"
              name="phone"
              value={formData.phone}
              onChange={handleChange}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="service">Service Type</label>
            <select
              id="service"
              name="service"
              value={formData.service}
              onChange={handleChange}
              required
            >
              <option value="">Select a service</option>
              {serviceOptions.map((option, index) => (
                <option key={index} value={option.value}>
                  {option.label}
                </option>
              ))}
            </select>
          </div>
          <div className="form-group">
            <label htmlFor="message">Additional Details</label>
            <textarea
              id="message"
              name="message"
              rows="4"
              value={formData.message}
              onChange={handleChange}
            ></textarea>
          </div>
          <button type="submit" className="submit-btn">Request Service</button>
        </form>
      </div>
    </section>
  );
};

export default Contact;
import React from 'react';

const Footer = () => {
  return (
    <footer>
      <div className="footer-content">
        <div className="footer-links">
          <a href="#home">Home</a>
          <a href="#services">Services</a>
          <a href="#waste-types">Waste Types</a>
          <a href="#contact">Contact</a>
        </div>
        <p>&copy; 2025 EcoClean Waste Management. All rights reserved.</p>
        <p>Creating a sustainable future, one pickup at a time.</p>
      </div>
    </footer>
  );
};

export default Footer;