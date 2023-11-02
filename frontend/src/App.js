import { useState, useEffect } from "react";
import "./App.css";

function App() {
  const [data, setData] = useState(null);
  const [name, setName] = useState("");
  const [desc, setDesc] = useState("");

  async function fetchData() {
    const endpoint = "http://localhost:8000/things";

    const options = {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    };

    const response = await fetch(endpoint, options);
    const result = await response.json();
    setData(result);
  }

  async function deleteHandler(thing_id) {
    const endpoint = `http://localhost:8000/things/${thing_id}`;
    const options = {
      method: "DELETE",
      headers: { "Content-Type": "application/json" },
    };
    const response = await fetch(endpoint, options);
    const result = await response.json();

    const filterCondition = (thing) => thing._id !== thing_id;
    const filteredThings = data.things.filter(filterCondition);
    setData({ things: filteredThings });

    console.log(result);
  }

  async function addHandler() {
    const options = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name: name, description: desc }),
    };

    const response = await fetch("http://localhost:8000/things/", options);
    const result = await response.json();

    setData({ things: [...data.things, result] });
    setName("");
    setDesc("");
  }

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <main>
      <h1>FARM Seed</h1>

      {data &&
        data.things.map((thing) => (
          <div key={thing._id}>
            <p>Name: {thing.name}</p>
            <p>Description: {thing.description}</p>
            <button onClick={() => deleteHandler(thing._id)}>Delete</button>
            <hr />
          </div>
        ))}
      <div>
        <label>
          Name:
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </label>
        <br />
        <label>
          Description:
          <input
            type="text"
            value={desc}
            onChange={(e) => setDesc(e.target.value)}
          />
        </label>
        <button onClick={addHandler}>Add</button>
      </div>
    </main>
  );
}

export default App;
