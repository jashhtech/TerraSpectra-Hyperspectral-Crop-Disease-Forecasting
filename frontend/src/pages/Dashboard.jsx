import { useEffect, useState } from "react";
import MapView from "../components/MapView";
import { getHealth } from "../services/api";

function Dashboard() {
  const [status, setStatus] = useState("Checking...");

  useEffect(() => {
    getHealth()
      .then((data) => {
        setStatus(data.status);
      })
      .catch(() => {
        setStatus("Backend Offline");
      });
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>TerraSpectra Dashboard</h1>

      <h3>Backend Status: {status}</h3>

      <hr />

      <h2>Crop Disease Monitoring</h2>

      <MapView />
    </div>
  );
}

export default Dashboard;