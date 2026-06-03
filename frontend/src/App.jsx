import { useState, useEffect } from "react";
import ContactList from "./ContactList";
import "./App.css";
import ContactForm from "./ContactForm";

function App() {
  const [contacts, setContacts] = useState([])
  // Modal is like a window that hovers over the screen
  const [isModalOpen, setIsModalOpen] = useState(false)
  const [currentContact, setCurrentContact] = useState({})
  
  // As soon as component loads load this function
  useEffect(() => {
    fetchContacts()
  }, []);

  const fetchContacts = async () => {
    // Sending get request at contacts endpoint
    const response = await fetch("http://127.0.0.1:5000/contacts")
    const data = await response.json()
    setContacts(data.contacts)
  };

  const closeModal = () => {
    setIsModalOpen(false)
    setCurrentContact({})
  }

  const openCreateModal = () => {
    if (!isModalOpen) setIsModalOpen(true)
  }

  const openEditModal = (contact) => {
    if (isModalOpen) return
    setCurrentContact(contact)
    setIsModalOpen(true)
  }
  
  const onUpdate = () => {
    closeModal()
    fetchContacts()
  }


  return (
  <>
  <ContactList contacts={contacts} updateContact={openEditModal} updateCallBack={onUpdate}/> 
  <button onClick={openCreateModal}>Create New Contact</button>
  { isModalOpen && <div className ="modal">
    <div className="modal-content"> 
      <span className="close"
        onClick = {closeModal}>&times;</span>
      <ContactForm exhistingContact={currentContact} updateCallBack={onUpdate} />
    </div>
    </div>}
  </>
  );
};

export default App
