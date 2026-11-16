import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import MapView from "../components/MapView";

function Dashboard() {
  return (
    <div>
      <Navbar />

      <div style={{ display: "flex", gap: "25px" }}>
        <Sidebar />

        <main style={{ flex: 1, padding: "20px" }}>
          <h1>TerraSpectra Dashboard</h1>

          <h3>GIS Crop Monitoring Map</h3>

          <MapView />

          <h3>Disease Prediction</h3>
          <p>Sample disease overlay displayed on the map.</p>
        </main>
      </div>
    </div>
  );
}

export default Dashboard;