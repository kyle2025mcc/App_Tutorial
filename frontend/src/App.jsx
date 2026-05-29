import { useState, useEffect } from "react";
import ContactList from "./ContactList";
import "./App.css";
import ContactForm from "./ContactForm";

function App() {
  const [contacts, setContacts] = useState([])
  
  // As soon as component loads load this function
  useEffect(() => {
    fetchContacts()
  }, []);

  const fetchContacts = async () => {
    // Sending get request at contacts endpoint
    const response = await fetch("http://127.0.0.1:5000/contacts")
    const data = await response.json()
    setContacts(data.contacts)
    console.log(data.contacts)
  };


  return (
  <>
  <ContactList contacts={contacts} /> 
  <ContactForm />
  </>
  );
};

export default App
