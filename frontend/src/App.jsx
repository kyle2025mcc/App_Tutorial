import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [contacts, setContacts] = useState([])
  
  // As soon as component loads load this function
  useEffect(() => {
    fetchContacts()
  }, [])

  const fetchContacts = async () => {
    // Sending get request at contacts endpoint
    const response = await fetch("http://127.0.0.1:5000/contacts")
    const data = await response.json()
    setContacts(data.contacts)
    console.log(data.contacts)
  }


  return (
    <>
      
    </>
  )
}

export default App
