import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";

function Dashboard() {
  return (
    <div>
      <Navbar />

      <div style={{ display: "flex", gap: "30px" }}>
        <Sidebar />

        <main>
          <h1>Farm Monitoring Dashboard</h1>

          <h3>Crop Health Overview</h3>
          <p>Monitor crop health using hyperspectral imagery.</p>

          <h3>GIS Map</h3>
          <div style={{
            height: "300px",
            background: "#e5e7eb",
            padding: "20px"
          }}>
            Map will be displayed here.
          </div>

          <h3>Disease Predictions</h3>
          <p>Prediction results will appear here.</p>
        </main>
      </div>
    </div>
  );
}

export default Dashboard;