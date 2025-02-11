import React, { useState } from "react";
import "./App.css";

const Table = () => {
  const [searchTerm, setSearchTerm] = useState("");

  const data = [
    { id: 1, name: "Rahul Sharma", age: 28, city: "Mumbai" },
    { id: 2, name: "Priya Singh", age: 34, city: "Delhi" },
    { id: 3, name: "Amit Kumar", age: 45, city: "Bangalore" },
    { id: 4, name: "Sneha Roy", age: 22, city: "Kolkata" },
    { id: 5, name: "Raju Sharma", age: 25, city: "Thane" },
    { id: 6, name: "Akansh sharma", age: 54, city: "Kochi" }
  ];

  const filteredData = data.filter(
    (item) =>
      item.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="App" style={{ padding: "20px" }}>
      <input
        type="text"
        placeholder="Search by name"
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
        style={{ marginBottom: "20px", padding: "10px", width: "100%" }}
      />
      <table
        border="1"
        style={{
          width: "100%",
          borderCollapse: "collapse",
          tableLayout: "fixed"
        }}
      >
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Age</th>
            <th>City</th>
          </tr>
        </thead>
        <tbody>
          {filteredData.length > 0 ? (
            filteredData.map((item) => (
              <tr key={item.id}>
                <td>{item.id}</td>
                <td>{item.name}</td>
                <td>{item.age}</td>
                <td>{item.city}</td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="4">No results found</td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
};

export default Table;