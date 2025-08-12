import React, { useState } from "react";
import "./App.css";

function App() {
  const [task, setTask] = useState("");
  const [tasks, setTasks] = useState([]);
  const [editIndex, setEditIndex] = useState(null);

  const handleAddOrUpdateTask = () => {
    if (task.trim() === "") return;

    if (editIndex !== null) {
      const updatedTasks = [...tasks];
      updatedTasks[editIndex] = task;
      setTasks(updatedTasks);
      setEditIndex(null);
    } else {
      setTasks([...tasks, task]);
    }
    setTask("");
  };

  const handleDeleteTask = (index) => {
    setTasks(tasks.filter((_, i) => i !== index));
  };

  const handleEditTask = (index) => {
    setTask(tasks[index]);
    setEditIndex(index);
  };

  return (
    <div className="app-container">
      <div className="todo-card">
        <h1 className="app-title">📋My To-Do List</h1>
        
        <div className="input-section">
          <input
            type="text"
            value={task}
            placeholder="Enter a new task..."
            onChange={(e) => setTask(e.target.value)}
          />
          <button onClick={handleAddOrUpdateTask}>
            {editIndex !== null ? "Update" : "Add"}
          </button>
        </div>

        <div className="task-list">
          {tasks.map((t, index) => (
            <div key={index} className="task-item">
              <span>{t}</span>
              <div className="task-actions">
                <button className="edit-btn" onClick={() => handleEditTask(index)}>✏️</button>
                <button className="delete-btn" onClick={() => handleDeleteTask(index)}>❌</button>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default App;
