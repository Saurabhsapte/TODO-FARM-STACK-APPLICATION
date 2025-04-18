import './App.css'
import React, {useState,useEffect} from 'react'
import axios from 'axios'
import TodoView from './components/TodoListView';

function App() {

  const [todoList, setTodoList] = useState([])
  const [title, setTitle] = useState('')
  const [description, setDescription] = useState('')

  useEffect(() => {
     axios.get('http://localhost:8000/api/v1/todos')
     .then(res=>{
      setTodoList(res.data)
     })
      .catch(err=>{
        console.log(err)
      })
    },[]);

    const addTodoHandler = () => {
      const todo = {
        id: todoList.length + 1,
        title: title,
        description: description
      }
      axios.post('http://localhost:8000/api/v1/todo', todo)
      .then(res=>{
        setTodoList([...todoList, res.data])
        // setTitle('')
        // setDescription('')
      })
      .catch(err=>{
        console.log(err)
      })
    }
  

  return (
    <div className="App list-group-item  justify-content-center align-items-center mx-auto" style={{"width":"500px", "backgroundColor":"white", "marginTop":"20px"}} >
      <h1 className="card text-white bg-primary mb-1 bg-opacity-95 bg-gradient" styleName="max-width: 20rem;">TODO List</h1>
      <h6 className="card text-white bg-secondary mb-3 bg-opacity-50">FASTAPI - React - MongoDB</h6>
      <div className="card-body">
        <h5 className="card text-white bg-info  mb-3">Add Your Task</h5>
        <span className="card-text"> 
          <input className="mb-2 form-control titleIn" onChange={event=> setTitle(event.target.value)} placeholder='Title'/> 
          <textarea className="mb-2 form-control desIn" onChange={event=> setDescription(event.target.value)} placeholder='Description'/>
          <button className="btn btn-outline-success mx-2 mb-3" style={{'borderRadius':'50px',"font-weight":"bold"}} onClick={addTodoHandler}>Add Task</button>
        </span>
        <h5 className="card text-white bg-info bg-gradient mb-3">Your Tasks</h5>
        <div >
          <TodoView todoList={todoList} />
        </div>
      </div>
      <h6 className="card text-dark bg-warning py-1 mb-0" >Copyright 2025, All rights reserved &copy; <br/> Developed By: Saurabh Sapte</h6>
    </div>
  )
}

export default App
