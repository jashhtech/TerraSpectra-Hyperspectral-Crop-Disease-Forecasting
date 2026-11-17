import { useEffect, useState } from "react";
import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import MapView from "../components/MapView";
import { getHealth } from "../services/api";

function Dashboard() {
  const [status, setStatus] = useState("Loading...");
  const [error, setError] = useState("");

  useEffect(() => {
    getHealth()
      .then((data) => {
        setStatus(data.status);
      })
      .catch(() => {
        setError("Unable to connect to API");
        setStatus("Offline");
      });
  }, []);

  return (
    <div>
      <Navbar />

      <div style={{ display: "flex", gap: "25px" }}>
        <Sidebar />

        <main style={{ flex: 1, padding: "20px" }}>
          <h1>TerraSpectra Dashboard</h1>

          <h3>Backend API Status: {status}</h3>

          {error && <p style={{ color: "red" }}>{error}</p>}

          <h3>GIS Map</h3>
          <MapView />
        </main>
      </div>
    </div>
  );
}

export default Dashboard;